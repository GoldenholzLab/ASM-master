#!/usr/bin/env python3
"""
Agentic ASM row verifier.

This complements scripts/update_check.py. It asks a GPT/Codex agent to review
one CSV drug row at a time, with local row context, existing PubMed/outcome
audit rows, deterministic update_check findings, and optional web search over
trusted domains. It writes reports and approval templates only; it does not edit
the CSV unless a future apply step is explicitly added.

Default live use routes through the local Codex CLI, so it can use an existing
ChatGPT/Codex login instead of an OpenAI API key:
  python3 scripts/agentic_update_check.py --row brivaracetam

Optional direct OpenAI API use:
  OPENAI_API_KEY=... python3 scripts/agentic_update_check.py --backend openai-api --row brivaracetam

Smoke-test without API calls:
  python3 scripts/agentic_update_check.py --backend preview --max-rows 1
"""

from __future__ import annotations

import argparse
import csv
import json
import os
import re
import shutil
import subprocess
import sys
import time
import urllib.error
import urllib.request
from collections import defaultdict
from dataclasses import dataclass, field
from datetime import datetime
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parents[0]
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

import update_check as deterministic  # noqa: E402


CSV_PATH = ROOT / "ASM-list.csv"
REPORT_DIR = ROOT / "pubmed_cache" / "reports" / "agentic_update_check"
DETERMINISTIC_REPORT = ROOT / "pubmed_cache" / "reports" / "update_check" / "update_check_findings.json"
RCT_REPORT = ROOT / "pubmed_cache" / "reports" / "pubmed_rct_audit.csv"
OUTCOME_REPORT = ROOT / "pubmed_cache" / "reports" / "efficacy_outcome_audit.csv"
OPENAI_RESPONSES_URL = "https://api.openai.com/v1/responses"
DEFAULT_CODEX_BIN = shutil.which("codex") or "/Applications/Codex.app/Contents/Resources/codex"
TODAY = datetime.now().strftime("%m-%d-%Y")
ISO_TODAY = datetime.now().strftime("%Y-%m-%d")

DEFAULT_ALLOWED_DOMAINS = [
    "api.fda.gov",
    "www.fda.gov",
    "www.accessdata.fda.gov",
    "pubmed.ncbi.nlm.nih.gov",
    "www.ncbi.nlm.nih.gov",
    "clinicaltrials.gov",
    "www.ema.europa.eu",
    "ema.europa.eu",
    "www.medicines.org.uk",
    "www.epilepsy.com",
    "www.ilae.org",
    "nih.gov",
]

FACT_FIELDS = [
    "alternate_generic_names",
    "trade_names",
    "pubmed_search_aliases",
    "evidence_sources",
    "available_in_us",
    "epilepsy_type",
    "mechanism_of_action",
    "mechanism_source",
    "mechanism_source_tier",
    "mechanism_confidence",
    "half_life_range",
    "major_organ_for_metabolism",
    "formulations_available",
    "typical_doses_per_day",
    "minimum_effective_dose",
    "maximum_approved_daily_dose",
    "enzyme_inducing_or_inhibiting",
    "qt_interval_effect",
    "adverse_symptoms_percentages",
    "year_fda_cleared",
    "fda_black_box_warning",
    "fda_black_box_warning_source",
    "pubmed_phase_ii_iii_rct_links",
    "diff_50_responder_maximum_effective_dose",
    "diff_median_pct_change_maximum_effective_dose",
    "diff_seizure_freedom_maximum_effective_dose",
    "plot_diff_50_responder_maximum_effective_dose",
    "plot_diff_median_pct_change_maximum_effective_dose",
    "plot_diff_seizure_freedom_maximum_effective_dose",
]


@dataclass
class AgenticResult:
    generic_name: str
    status: str
    raw_response: dict[str, Any] = field(default_factory=dict)
    parsed: dict[str, Any] = field(default_factory=dict)
    sources: list[dict[str, Any]] = field(default_factory=list)
    error: str = ""


def read_csv_dicts(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def read_optional_csv(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    _, rows = read_csv_dicts(path)
    return rows


def read_optional_json(path: Path) -> list[dict[str, Any]]:
    if not path.exists():
        return []
    return json.loads(path.read_text(encoding="utf-8"))


def normalize_space(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def selected_rows(rows: list[dict[str, str]], names: list[str], max_rows: int | None, start_after: str) -> list[dict[str, str]]:
    if names:
        wanted = {name.lower() for name in names}
        rows = [row for row in rows if row.get("generic_name", "").lower() in wanted]
    if start_after:
        output = []
        seen = False
        for row in rows:
            if seen:
                output.append(row)
            elif row.get("generic_name", "").lower() == start_after.lower():
                seen = True
        rows = output
    if max_rows:
        rows = rows[:max_rows]
    return rows


def group_by_generic(rows: list[dict[str, Any]]) -> dict[str, list[dict[str, Any]]]:
    grouped: dict[str, list[dict[str, Any]]] = defaultdict(list)
    for row in rows:
        grouped[row.get("generic_name", "")].append(row)
    return grouped


def split_name_values(value: str) -> list[str]:
    names: list[str] = []
    for part in re.split(r"[;,]", value or ""):
        cleaned = normalize_space(part)
        if cleaned and cleaned.upper() != "N/A":
            names.append(cleaned)
    return names


def normalize_name(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def build_alias_index(rows: list[dict[str, str]]) -> dict[str, list[dict[str, str]]]:
    index: dict[str, list[dict[str, str]]] = defaultdict(list)
    alias_fields = ["generic_name", "alternate_generic_names", "trade_names", "pubmed_search_aliases"]
    for row in rows:
        generic = row.get("generic_name", "")
        aliases: list[str] = []
        for field_name in alias_fields:
            if field_name == "generic_name":
                aliases.append(row.get(field_name, ""))
            else:
                aliases.extend(split_name_values(row.get(field_name, "")))
        seen: set[str] = set()
        for alias in aliases:
            normalized = normalize_name(alias)
            if not normalized or normalized in seen:
                continue
            seen.add(normalized)
            index[normalized].append({"generic_name": generic, "matched_name": alias})
    return index


def duplicate_alias_hits(row: dict[str, str], alias_index: dict[str, list[dict[str, str]]]) -> list[dict[str, Any]]:
    generic = row.get("generic_name", "")
    aliases = [generic]
    for field_name in ["alternate_generic_names", "trade_names", "pubmed_search_aliases"]:
        aliases.extend(split_name_values(row.get(field_name, "")))
    hits: list[dict[str, Any]] = []
    seen: set[str] = set()
    for alias in aliases:
        normalized = normalize_name(alias)
        if not normalized or normalized in seen:
            continue
        seen.add(normalized)
        matches = [match for match in alias_index.get(normalized, []) if match.get("generic_name") != generic]
        if matches:
            hits.append({"name": alias, "also_seen_in_rows": matches})
    return hits


def is_fda_source_url(url: str) -> bool:
    lowered = (url or "").lower()
    return any(
        domain in lowered
        for domain in [
            "api.fda.gov",
            "fda.gov",
            "accessdata.fda.gov",
        ]
    )


def extract_response_text(response: dict[str, Any]) -> str:
    if response.get("output_text"):
        return response["output_text"]
    chunks: list[str] = []
    for item in response.get("output", []) or []:
        if item.get("type") != "message":
            continue
        for content in item.get("content", []) or []:
            if content.get("type") in {"output_text", "text"} and content.get("text"):
                chunks.append(content["text"])
    return "\n".join(chunks).strip()


def parse_json_text(text: str) -> dict[str, Any]:
    cleaned = text.strip()
    fence = re.match(r"^```(?:json)?\s*(.*?)\s*```$", cleaned, flags=re.DOTALL | re.IGNORECASE)
    if fence:
        cleaned = fence.group(1).strip()
    return json.loads(cleaned)


def extract_response_sources(response: dict[str, Any]) -> list[dict[str, Any]]:
    sources: list[dict[str, Any]] = []
    for item in response.get("output", []) or []:
        if item.get("type") != "web_search_call":
            continue
        action = item.get("action", {}) or {}
        for source in action.get("sources", []) or []:
            sources.append(source)
    return sources


def json_schema() -> dict[str, Any]:
    fact_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "field": {"type": "string"},
            "current_value": {"type": "string"},
            "status": {
                "type": "string",
                "enum": ["verified", "incorrect", "missing", "missing_source", "insufficient_evidence", "not_applicable"],
            },
            "rationale": {"type": "string"},
            "supporting_sources": {"type": "array", "items": {"type": "string"}},
            "proposed_value": {"type": "string"},
            "requires_user_approval": {"type": "boolean"},
        },
        "required": [
            "field",
            "current_value",
            "status",
            "rationale",
            "supporting_sources",
            "proposed_value",
            "requires_user_approval",
        ],
    }
    link_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "label": {"type": "string"},
            "pmid": {"type": "string"},
            "url": {"type": "string"},
            "status": {"type": "string", "enum": ["verified", "wrong_drug", "not_placebo_rct", "not_phase_ii_iii", "broken_or_invalid", "insufficient_evidence"]},
            "rationale": {"type": "string"},
            "proposed_action": {"type": "string"},
        },
        "required": ["label", "pmid", "url", "status", "rationale", "proposed_action"],
    }
    missing_rct_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "title": {"type": "string"},
            "pmid": {"type": "string"},
            "url": {"type": "string"},
            "why_relevant": {"type": "string"},
            "proposed_link_text": {"type": "string"},
        },
        "required": ["title", "pmid", "url", "why_relevant", "proposed_link_text"],
    }
    outcome_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "field": {"type": "string"},
            "status": {"type": "string", "enum": ["verified", "incorrect", "insufficient_evidence", "not_applicable"]},
            "current_value": {"type": "string"},
            "proposed_value": {"type": "string"},
            "rationale": {"type": "string"},
            "supporting_sources": {"type": "array", "items": {"type": "string"}},
            "requires_user_approval": {"type": "boolean"},
        },
        "required": ["field", "status", "current_value", "proposed_value", "rationale", "supporting_sources", "requires_user_approval"],
    }
    update_item = {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "field": {"type": "string"},
            "current_value": {"type": "string"},
            "proposed_value": {"type": "string"},
            "reason": {"type": "string"},
            "source_urls": {"type": "array", "items": {"type": "string"}},
            "requires_user_approval": {"type": "boolean"},
        },
        "required": ["field", "current_value", "proposed_value", "reason", "source_urls", "requires_user_approval"],
    }
    return {
        "type": "object",
        "additionalProperties": False,
        "properties": {
            "generic_name": {"type": "string"},
            "overall_status": {"type": "string", "enum": ["verified", "needs_update", "conflict", "insufficient_evidence"]},
            "summary": {"type": "string"},
            "fact_checks": {"type": "array", "items": fact_item},
            "rct_link_checks": {"type": "array", "items": link_item},
            "missing_rcts": {"type": "array", "items": missing_rct_item},
            "outcome_checks": {"type": "array", "items": outcome_item},
            "black_box_warning": {
                "type": "object",
                "additionalProperties": False,
                "properties": {
                    "status": {"type": "string", "enum": ["verified", "incorrect", "missing", "insufficient_evidence", "not_applicable"]},
                    "current_value": {"type": "string"},
                    "proposed_value": {"type": "string"},
                    "rationale": {"type": "string"},
                    "fda_source_urls": {"type": "array", "items": {"type": "string"}},
                    "requires_user_approval": {"type": "boolean"},
                },
                "required": ["status", "current_value", "proposed_value", "rationale", "fda_source_urls", "requires_user_approval"],
            },
            "source_updates": {"type": "array", "items": update_item},
            "proposed_row_updates": {"type": "array", "items": update_item},
            "blocking_questions": {"type": "array", "items": {"type": "string"}},
        },
        "required": [
            "generic_name",
            "overall_status",
            "summary",
            "fact_checks",
            "rct_link_checks",
            "missing_rcts",
            "outcome_checks",
            "black_box_warning",
            "source_updates",
            "proposed_row_updates",
            "blocking_questions",
        ],
    }


def developer_instructions() -> str:
    return (
        "You are auditing one row of an anti-seizure medication CSV. Produce JSON only. "
        "Verify each populated fact field against trusted sources. For black box warnings, use FDA sources only "
        "(FDA/openFDA, FDA labels, Drugs@FDA); do not rely on DailyMed for black box warning verification. "
        "For non-US drugs, EMA, eMC/SmPC, ILAE, Epilepsy Foundation, and peer-reviewed literature can support non-FDA facts. "
        "Verify alternate names and trade names; a drug should not be represented as a separate row just because an alias exists, "
        "and important aliases should be listed in alternate_generic_names, trade_names, or pubmed_search_aliases. "
        "Check that named sources in the row actually support the specific cell facts they are cited for. "
        "For placebo-controlled phase II/III RCTs, verify PubMed links, PMIDs, drug assignment, placebo control, trial phase/design, "
        "and whether differential RR50, MPC, and seizure-freedom values match cited RCT/outcome evidence. "
        "If a fact is plausible but the provided row lacks a source named in evidence_sources or RCT fields, mark missing_source. "
        "When proposing a change, give exact replacement text and source URLs. Do not recommend removing existing data unless there is a direct contradiction."
    )


def build_row_bundle(
    row: dict[str, str],
    rct_by_drug: dict[str, list[dict[str, str]]],
    outcome_by_drug: dict[str, list[dict[str, str]]],
    deterministic_by_drug: dict[str, list[dict[str, Any]]],
    alias_index: dict[str, list[dict[str, str]]],
) -> dict[str, Any]:
    generic = row.get("generic_name", "")
    fact_subset = {field_name: row.get(field_name, "") for field_name in FACT_FIELDS if field_name in row}
    existing_links = deterministic.extract_pubmed_links(row.get("pubmed_phase_ii_iii_rct_links", ""))
    return {
        "audit_date": ISO_TODAY,
        "generic_name": generic,
        "csv_row": row,
        "fact_fields_to_check": fact_subset,
        "existing_pubmed_links": existing_links,
        "possible_duplicate_name_hits": duplicate_alias_hits(row, alias_index),
        "local_rct_audit_rows": rct_by_drug.get(generic, []),
        "local_outcome_audit_rows": outcome_by_drug.get(generic, []),
        "latest_deterministic_update_check_findings_for_row": deterministic_by_drug.get(generic, []),
        "instructions": {
            "black_box_warning_policy": "FDA sources only. DailyMed is not permissible for black box warning verification.",
            "trusted_sources": DEFAULT_ALLOWED_DOMAINS,
            "required_row_source_policy": (
                "Every retained fact should have a named trusted source in evidence_sources, mechanism_source, "
                "fda_black_box_warning_source, or the RCT/outcome link fields."
            ),
        },
    }


def openai_request(payload: dict[str, Any], args: argparse.Namespace) -> tuple[dict[str, Any], dict[str, Any]]:
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is required unless --no-api is used.")
    model = args.model or os.environ.get("OPENAI_MODEL") or "gpt-5.2"
    body: dict[str, Any] = {
        "model": model,
        "instructions": developer_instructions(),
        "input": [
            {
                "role": "user",
                "content": (
                    "Audit this ASM CSV row. Use web search when needed. Return structured JSON matching the schema.\n\n"
                    + json.dumps(payload, ensure_ascii=False)
                ),
            }
        ],
        "reasoning": {"effort": args.reasoning_effort},
        "text": {
            "format": {
                "type": "json_schema",
                "name": "asm_row_agentic_audit",
                "strict": True,
                "schema": json_schema(),
            }
        },
    }
    if args.web_search:
        body["tools"] = [
            {
                "type": "web_search",
                "filters": {"allowed_domains": args.allowed_domain},
                "external_web_access": not args.web_search_cache_only,
            }
        ]
        body["tool_choice"] = "auto"
        body["include"] = ["web_search_call.action.sources"]

    data = json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        OPENAI_RESPONSES_URL,
        data=data,
        method="POST",
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
            "User-Agent": "ASM-master agentic_update_check/1.0",
        },
    )
    for attempt in range(args.max_retries + 1):
        try:
            with urllib.request.urlopen(request, timeout=args.timeout) as response:
                raw = json.loads(response.read().decode("utf-8"))
            parsed_text = extract_response_text(raw)
            parsed = parse_json_text(parsed_text)
            return raw, parsed
        except urllib.error.HTTPError as exc:
            if exc.code not in {429, 500, 502, 503, 504} or attempt >= args.max_retries:
                body_text = exc.read().decode("utf-8", errors="replace")
                raise RuntimeError(f"OpenAI API HTTP {exc.code}: {body_text[:1000]}") from exc
            retry_after = exc.headers.get("Retry-After")
            try:
                delay = float(retry_after) if retry_after else 0.0
            except ValueError:
                delay = 0.0
            if delay <= 0:
                delay = min(120.0, 8.0 * (2**attempt))
            print(f"OpenAI API HTTP {exc.code}; sleeping {delay:.0f}s before retry {attempt + 1}/{args.max_retries}.", flush=True)
            time.sleep(delay)
        except urllib.error.URLError as exc:
            if attempt >= args.max_retries:
                raise RuntimeError(f"OpenAI API network error: {exc.reason}") from exc
            delay = min(120.0, 8.0 * (2**attempt))
            print(f"OpenAI API network error; sleeping {delay:.0f}s before retry {attempt + 1}/{args.max_retries}.", flush=True)
            time.sleep(delay)
        except json.JSONDecodeError as exc:
            raise RuntimeError(f"OpenAI response was not valid JSON: {exc}") from exc
    raise RuntimeError("OpenAI API retry loop ended unexpectedly.")


def codex_prompt(payload: dict[str, Any], args: argparse.Namespace) -> str:
    allowed_domains = "\n".join(f"- {domain}" for domain in args.allowed_domain)
    return (
        "You are a Codex sub-agent auditing one anti-seizure medication CSV row.\n\n"
        "Task:\n"
        "- Verify each populated fact in the row against trusted sources.\n"
        "- Verify alternate names and trade names; the same drug should not appear as a separate row just because an alias exists.\n"
        "- Verify PubMed links for phase II/III placebo-controlled RCTs, including PMID, drug, trial design, and placebo control.\n"
        "- Verify differential RR50, median percent change, and seizure-freedom values against the cited RCT/outcome evidence.\n"
        "- Verify whether each cited row source actually supports the specific cell facts it is being used for.\n"
        "- For FDA black box warnings, use FDA/openFDA, FDA labels, or Drugs@FDA only. DailyMed is not permissible for this field.\n"
        "- For non-US drugs, EMA/eMC/SmPC, ILAE, Epilepsy Foundation, NIH/NCBI/PubMed, and peer-reviewed literature may support non-FDA facts.\n"
        "- Do not edit files. Return only your final structured JSON answer.\n\n"
        "Trusted source domains to use or cite:\n"
        f"{allowed_domains}\n\n"
        "When a row value is wrong or missing, propose exact replacement text and source URLs. "
        "Do not recommend deleting existing CSV data unless the evidence directly contradicts it; direct contradictions require user approval.\n\n"
        "Use web search if needed. If web search is unavailable, mark affected checks as insufficient_evidence instead of guessing.\n\n"
        "Developer audit instructions:\n"
        f"{developer_instructions()}\n\n"
        "Row bundle JSON:\n"
        f"{json.dumps(payload, ensure_ascii=False, indent=2, sort_keys=True)}\n"
    )


def codex_request(payload: dict[str, Any], args: argparse.Namespace, report_dir: Path) -> tuple[dict[str, Any], dict[str, Any]]:
    codex_bin = args.codex_bin
    if not codex_bin or not (Path(codex_bin).exists() or shutil.which(codex_bin)):
        raise RuntimeError(
            "Codex CLI was not found. Install/open Codex or pass --codex-bin with the Codex executable path."
        )

    report_dir.mkdir(parents=True, exist_ok=True)
    generic = payload.get("generic_name", "row")
    slug = deterministic.slug(generic)
    schema_path = report_dir / "agentic_update_check_schema.json"
    prompt_path = report_dir / f"codex_prompt_{slug}.md"
    output_path = report_dir / f"codex_last_message_{slug}.json"
    stdout_path = report_dir / f"codex_stdout_{slug}.log"
    stderr_path = report_dir / f"codex_stderr_{slug}.log"

    schema_path.write_text(json.dumps(json_schema(), indent=2, sort_keys=True) + "\n", encoding="utf-8")
    prompt = codex_prompt(payload, args)
    prompt_path.write_text(prompt, encoding="utf-8")
    for transient_path in [output_path, stdout_path, stderr_path]:
        try:
            transient_path.unlink()
        except FileNotFoundError:
            pass

    command = [codex_bin]
    if args.web_search:
        command.append("--search")
    if args.model:
        command.extend(["--model", args.model])
    command.extend(
        [
            "-a",
            "never",
            "exec",
        ]
    )
    command.extend(
        [
            "--cd",
            str(ROOT),
            "--sandbox",
            args.codex_sandbox,
            "--output-schema",
            str(schema_path),
            "--output-last-message",
            str(output_path),
            "--color",
            "never",
        ]
    )
    if args.codex_ephemeral:
        command.append("--ephemeral")
    command.append("-")

    env = os.environ.copy()
    if not args.codex_preserve_api_key:
        env.pop("OPENAI_API_KEY", None)

    try:
        completed = subprocess.run(
            command,
            input=prompt,
            text=True,
            capture_output=True,
            timeout=args.codex_timeout,
            cwd=str(ROOT),
            env=env,
            check=False,
        )
    except subprocess.TimeoutExpired as exc:
        stdout_path.write_text(exc.stdout or "", encoding="utf-8")
        stderr_path.write_text(exc.stderr or "", encoding="utf-8")
        raise RuntimeError(
            f"Codex exec timed out after {args.codex_timeout}s for {generic}. "
            f"Partial stdout/stderr were saved to {stdout_path} and {stderr_path}."
        ) from exc

    stdout_path.write_text(completed.stdout or "", encoding="utf-8")
    stderr_path.write_text(completed.stderr or "", encoding="utf-8")
    raw = {
        "backend": "codex",
        "command": command[:-1] + ["<stdin-prompt>"],
        "returncode": completed.returncode,
        "prompt_path": str(prompt_path),
        "schema_path": str(schema_path),
        "output_path": str(output_path),
        "stdout_path": str(stdout_path),
        "stderr_path": str(stderr_path),
    }
    if completed.returncode != 0:
        stdout_tail = (completed.stdout or "")[-2000:]
        stderr_tail = (completed.stderr or "")[-2000:]
        raise RuntimeError(
            f"Codex exec failed with exit code {completed.returncode}. "
            f"stdout tail: {stdout_tail} stderr tail: {stderr_tail}"
        )
    if not output_path.exists():
        raise RuntimeError(f"Codex exec completed but did not write {output_path}.")

    output_text = output_path.read_text(encoding="utf-8")
    parsed = parse_json_text(output_text)
    return raw, parsed


def result_to_findings(result: AgenticResult) -> list[dict[str, Any]]:
    if result.error:
        return [
            {
                "generic_name": result.generic_name,
                "kind": "agentic_error",
                "severity": "warning",
                "field": "",
                "status": "error",
                "current_value": "",
                "proposed_value": "",
                "requires_user_approval": False,
                "summary": result.error,
                "sources": "",
            }
        ]
    parsed = result.parsed
    findings: list[dict[str, Any]] = []

    def severity_for(status: str, approval: bool) -> str:
        if status in {"incorrect", "missing"} and approval:
            return "critical"
        if status in {"incorrect", "missing", "wrong_drug", "not_placebo_rct", "not_phase_ii_iii", "broken_or_invalid"}:
            return "high"
        if status in {"missing_source", "insufficient_evidence"}:
            return "medium"
        return "info"

    for item in parsed.get("fact_checks", []):
        status = item.get("status", "")
        if status == "verified":
            continue
        findings.append(
            {
                "generic_name": result.generic_name,
                "kind": "fact_check",
                "severity": severity_for(status, item.get("requires_user_approval", False)),
                "field": item.get("field", ""),
                "status": status,
                "current_value": item.get("current_value", ""),
                "proposed_value": item.get("proposed_value", ""),
                "requires_user_approval": item.get("requires_user_approval", False),
                "summary": item.get("rationale", ""),
                "sources": "; ".join(item.get("supporting_sources", [])),
            }
        )
    for item in parsed.get("rct_link_checks", []):
        status = item.get("status", "")
        if status == "verified":
            continue
        findings.append(
            {
                "generic_name": result.generic_name,
                "kind": "rct_link_check",
                "severity": severity_for(status, True),
                "field": "pubmed_phase_ii_iii_rct_links",
                "status": status,
                "current_value": item.get("url", ""),
                "proposed_value": item.get("proposed_action", ""),
                "requires_user_approval": True,
                "summary": item.get("rationale", ""),
                "sources": item.get("url", ""),
            }
        )
    for item in parsed.get("missing_rcts", []):
        findings.append(
            {
                "generic_name": result.generic_name,
                "kind": "missing_rct",
                "severity": "high",
                "field": "pubmed_phase_ii_iii_rct_links",
                "status": "missing",
                "current_value": "",
                "proposed_value": item.get("proposed_link_text", ""),
                "requires_user_approval": False,
                "summary": item.get("why_relevant", ""),
                "sources": item.get("url", ""),
            }
        )
    for item in parsed.get("outcome_checks", []):
        status = item.get("status", "")
        if status == "verified":
            continue
        findings.append(
            {
                "generic_name": result.generic_name,
                "kind": "outcome_check",
                "severity": severity_for(status, item.get("requires_user_approval", False)),
                "field": item.get("field", ""),
                "status": status,
                "current_value": item.get("current_value", ""),
                "proposed_value": item.get("proposed_value", ""),
                "requires_user_approval": item.get("requires_user_approval", False),
                "summary": item.get("rationale", ""),
                "sources": "; ".join(item.get("supporting_sources", [])),
            }
        )
    warning = parsed.get("black_box_warning", {})
    if warning and warning.get("status") != "verified":
        findings.append(
            {
                "generic_name": result.generic_name,
                "kind": "black_box_warning",
                "severity": severity_for(warning.get("status", ""), warning.get("requires_user_approval", False)),
                "field": "fda_black_box_warning",
                "status": warning.get("status", ""),
                "current_value": warning.get("current_value", ""),
                "proposed_value": warning.get("proposed_value", ""),
                "requires_user_approval": warning.get("requires_user_approval", False),
                "summary": warning.get("rationale", ""),
                "sources": "; ".join(warning.get("fda_source_urls", [])),
            }
        )
    if warning:
        non_fda_warning_sources = [
            source
            for source in warning.get("fda_source_urls", [])
            if source and not is_fda_source_url(source)
        ]
        if non_fda_warning_sources:
            findings.append(
                {
                    "generic_name": result.generic_name,
                    "kind": "black_box_warning_source_policy",
                    "severity": "critical",
                    "field": "fda_black_box_warning_source",
                    "status": "invalid_source",
                    "current_value": "",
                    "proposed_value": "Re-run or revise using FDA/openFDA, FDA labels, or Drugs@FDA sources only.",
                    "requires_user_approval": True,
                    "summary": "Agentic audit returned non-FDA source URLs for FDA black box warning verification.",
                    "sources": "; ".join(non_fda_warning_sources),
                }
            )
    for item in parsed.get("source_updates", []) + parsed.get("proposed_row_updates", []):
        findings.append(
            {
                "generic_name": result.generic_name,
                "kind": "proposed_row_update",
                "severity": "critical" if item.get("requires_user_approval") else "medium",
                "field": item.get("field", ""),
                "status": "proposed",
                "current_value": item.get("current_value", ""),
                "proposed_value": item.get("proposed_value", ""),
                "requires_user_approval": item.get("requires_user_approval", False),
                "summary": item.get("reason", ""),
                "sources": "; ".join(item.get("source_urls", [])),
            }
        )
    return findings


def write_reports(results: list[AgenticResult], findings: list[dict[str, Any]], report_dir: Path) -> None:
    report_dir.mkdir(parents=True, exist_ok=True)
    (report_dir / "agentic_update_check_results.json").write_text(
        json.dumps([result.__dict__ for result in results], indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    (report_dir / "agentic_update_check_findings.json").write_text(
        json.dumps(findings, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )
    fields = [
        "generic_name",
        "kind",
        "severity",
        "field",
        "status",
        "requires_user_approval",
        "summary",
        "sources",
        "current_value",
        "proposed_value",
    ]
    with (report_dir / "agentic_update_check_findings.csv").open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(findings)
    lines = [
        "# Agentic update_check summary",
        "",
        f"Generated: {ISO_TODAY}",
        "",
        f"Rows audited: {len(results)}",
        f"Findings: {len(findings)}",
        "",
    ]
    for finding in findings:
        lines.append(f"## {finding['severity'].upper()} {finding['generic_name']} / {finding['kind']}")
        lines.append(f"- Field: {finding['field']}")
        lines.append(f"- Status: {finding['status']}")
        lines.append(f"- Approval required: {finding['requires_user_approval']}")
        lines.append(f"- Summary: {finding['summary']}")
        if finding["sources"]:
            lines.append(f"- Sources: {finding['sources']}")
        if finding["current_value"]:
            lines.append(f"- Current: {normalize_space(finding['current_value'])[:900]}")
        if finding["proposed_value"]:
            lines.append(f"- Proposed: {normalize_space(finding['proposed_value'])[:900]}")
        lines.append("")
    (report_dir / "agentic_update_check_summary.md").write_text("\n".join(lines), encoding="utf-8")
    approvals = {
        "instructions": "Review proposed findings. Copy approved finding indices into approved_findings if you later build/apply an updater.",
        "approved_findings": [],
        "approval_candidates": [
            {**finding, "index": index}
            for index, finding in enumerate(findings)
            if finding.get("requires_user_approval")
        ],
    }
    (report_dir / "agentic_update_check_approval_template.json").write_text(
        json.dumps(approvals, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Agentic GPT-backed ASM row verifier. Default writes reports only.")
    parser.add_argument("--csv", default=str(CSV_PATH), help="CSV file to audit.")
    parser.add_argument("--report-dir", default=str(REPORT_DIR), help="Directory for agentic reports.")
    parser.add_argument(
        "--backend",
        default=os.environ.get("AGENTIC_UPDATE_CHECK_BACKEND", "codex"),
        choices=["codex", "openai-api", "preview"],
        help="Execution backend. codex uses your logged-in Codex/ChatGPT account; openai-api uses OPENAI_API_KEY; preview makes bundles only.",
    )
    parser.add_argument("--model", default=os.environ.get("OPENAI_MODEL", ""), help="Optional model for row audits. Empty uses Codex/OpenAI defaults.")
    parser.add_argument("--reasoning-effort", default="medium", choices=["minimal", "low", "medium", "high"], help="Reasoning effort.")
    parser.add_argument("--row", action="append", default=[], help="Generic name to audit. Can be passed multiple times.")
    parser.add_argument("--max-rows", type=int, help="Limit rows for smoke tests or batched runs.")
    parser.add_argument("--start-after", default="", help="Resume after this generic_name.")
    parser.add_argument("--no-api", action="store_true", help="Deprecated alias for --backend preview.")
    parser.add_argument("--web-search", action=argparse.BooleanOptionalAction, default=True, help="Allow model web search over trusted domains.")
    parser.add_argument("--web-search-cache-only", action="store_true", help="OpenAI API backend only: use cached/indexed web search without live external web access.")
    parser.add_argument("--allowed-domain", action="append", default=list(DEFAULT_ALLOWED_DOMAINS), help="Allowed web_search domain. Can be repeated.")
    parser.add_argument("--sleep", type=float, default=1.0, help="Delay between row API calls.")
    parser.add_argument("--timeout", type=int, default=300, help="OpenAI API request timeout seconds.")
    parser.add_argument("--max-retries", type=int, default=5, help="OpenAI API retry count for transient errors.")
    parser.add_argument("--codex-bin", default=os.environ.get("CODEX_BIN", DEFAULT_CODEX_BIN), help="Codex CLI executable for --backend codex.")
    parser.add_argument("--codex-timeout", type=int, default=1800, help="Timeout seconds for each codex exec row audit.")
    parser.add_argument("--codex-sandbox", default="read-only", choices=["read-only", "workspace-write", "danger-full-access"], help="Sandbox for nested codex exec row audits.")
    parser.add_argument("--codex-ephemeral", action=argparse.BooleanOptionalAction, default=True, help="Run nested Codex sessions without persisting session files.")
    parser.add_argument("--codex-preserve-api-key", action="store_true", help="Do not remove OPENAI_API_KEY from the nested Codex environment.")
    args = parser.parse_args()
    if args.no_api:
        args.backend = "preview"
    if args.backend == "codex" and args.web_search_cache_only:
        print("--web-search-cache-only is not exposed by codex exec; continuing with Codex web-search behavior.", file=sys.stderr)
    # Remove duplicates while preserving order.
    seen = set()
    args.allowed_domain = [domain for domain in args.allowed_domain if not (domain in seen or seen.add(domain))]
    return args


def main() -> None:
    args = parse_args()
    _, rows = read_csv_dicts(Path(args.csv))
    rows = selected_rows(rows, args.row, args.max_rows, args.start_after)
    rct_by_drug = group_by_generic(read_optional_csv(RCT_REPORT))
    outcome_by_drug = group_by_generic(read_optional_csv(OUTCOME_REPORT))
    deterministic_by_drug = group_by_generic(read_optional_json(DETERMINISTIC_REPORT))
    alias_index = build_alias_index(rows)

    results: list[AgenticResult] = []
    all_findings: list[dict[str, Any]] = []
    preview_dir = Path(args.report_dir)
    preview_dir.mkdir(parents=True, exist_ok=True)

    for index, row in enumerate(rows, start=1):
        generic = row.get("generic_name", "")
        bundle = build_row_bundle(row, rct_by_drug, outcome_by_drug, deterministic_by_drug, alias_index)
        (preview_dir / f"row_bundle_{deterministic.slug(generic)}.json").write_text(
            json.dumps(bundle, indent=2, sort_keys=True) + "\n",
            encoding="utf-8",
        )
        print(f"{index:02d}/{len(rows)} {generic}: bundle assembled", flush=True)
        if args.backend == "preview":
            result = AgenticResult(generic_name=generic, status="preview_only", parsed={"overall_status": "not_run"})
            results.append(result)
            continue
        try:
            if args.backend == "codex":
                raw, parsed = codex_request(bundle, args, Path(args.report_dir))
                sources = []
            else:
                raw, parsed = openai_request(bundle, args)
                sources = extract_response_sources(raw)
            result = AgenticResult(
                generic_name=generic,
                status=parsed.get("overall_status", "unknown"),
                raw_response=raw,
                parsed=parsed,
                sources=sources,
            )
        except Exception as exc:
            result = AgenticResult(generic_name=generic, status="error", error=str(exc))
        results.append(result)
        findings = result_to_findings(result)
        all_findings.extend(findings)
        write_reports(results, all_findings, Path(args.report_dir))
        print(f"{index:02d}/{len(rows)} {generic}: {result.status}; findings={len(findings)}", flush=True)
        if index < len(rows):
            time.sleep(args.sleep)

    write_reports(results, all_findings, Path(args.report_dir))
    print(f"Wrote reports to {Path(args.report_dir)}")


if __name__ == "__main__":
    main()
