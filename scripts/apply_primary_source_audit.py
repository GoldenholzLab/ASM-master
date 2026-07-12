#!/usr/bin/env python3
"""Apply regulatory-label corrections from the committed row-by-row audit.

The agentic audit is intentionally report-only. This script applies only exact
CSV-field replacements supported entirely by primary regulatory sources. It
also removes explicitly disallowed secondary-list and review citations while
retaining the precise regulatory URLs used for each applied correction.
"""

from __future__ import annotations

import csv
import re
from collections import defaultdict
from datetime import datetime
from pathlib import Path
from urllib.parse import urlparse


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "ASM-list.csv"
FINDINGS_PATH = (
    ROOT
    / "pubmed_cache"
    / "reports"
    / "agentic_update_check"
    / "agentic_update_check_findings.csv"
)
UPDATE_FINDINGS_PATH = ROOT / "pubmed_cache" / "reports" / "update_check" / "update_check_findings.csv"

REGULATORY_HOSTS = {
    "api.fda.gov",
    "fda.gov",
    "accessdata.fda.gov",
    "www.accessdata.fda.gov",
    "www.fda.gov",
    "open.fda.gov",
    "ema.europa.eu",
    "www.ema.europa.eu",
    "medicines.org.uk",
    "www.medicines.org.uk",
    "swissmedic.ch",
    "www.swissmedic.ch",
    "aifa.gov.it",
    "www.aifa.gov.it",
    "halmed.hr",
    "www.halmed.hr",
    "ansm.sante.fr",
    "base-donnees-publique.medicaments.gouv.fr",
    "m.base-donnees-publique.medicaments.gouv.fr",
}

FORBIDDEN_SOURCE_PATTERNS = (
    "american epilepsy society 2024 u.s. asm summary",
    "epilepsy foundation australia asm list",
    "epilepsy society asm list",
    "healthline asm list",
    "ncbi livertox",
    "ncbi pubchem pharmacology records",
    "sills and rogawski 2020 asm mechanism review",
    "statpearls",
    "wikipedia anticonvulsant drug-class list",
)

NON_FACT_FIELDS = {
    "evidence_sources",
    "pubmed_phase_ii_iii_rct_links",
    "diff_50_responder_maximum_effective_dose",
    "plot_diff_50_responder_maximum_effective_dose",
    "diff_median_pct_change_maximum_effective_dose",
    "plot_diff_median_pct_change_maximum_effective_dose",
    "diff_seizure_freedom_maximum_effective_dose",
    "plot_diff_seizure_freedom_maximum_effective_dose",
}

FILTER_VALUE_ALIASES = {
    "filter_metabolism": {
        "Hepatic": ["Liver/hepatic"],
        "Hepatic/liver microsomal": ["Liver/hepatic"],
    },
    "filter_mechanism": {
        "Carbonic anhydrase inhibitor": ["Carbonic anhydrase"],
        "Hydantoin / phenytoin-like (limited confidence)": ["Sodium channel", "Other / unclear"],
        "Unknown/Other": ["Other / unclear"],
    },
    "filter_formulation": {
        "IV/IM injection": ["IV injection", "IM injection"],
        "Injection/infusion solution": ["IV injection"],
        "Liquid/oral solution": ["Liquid"],
    },
    "filter_enzyme_effect": {
        "Mixed inhibitor/inducer": ["Inducer", "Inhibitor"],
    },
    "filter_qt_effect": {
        "QT prolongation reported/rare": ["QT prolongation"],
    },
}

OUTCOME_FIELDS = [
    "diff_50_responder_maximum_effective_dose",
    "diff_median_pct_change_maximum_effective_dose",
    "diff_seizure_freedom_maximum_effective_dose",
]

PLOT_FIELDS = [
    "plot_diff_50_responder_maximum_effective_dose",
    "plot_diff_median_pct_change_maximum_effective_dose",
    "plot_diff_seizure_freedom_maximum_effective_dose",
]

URL_RE = re.compile(r"https?://[^;\s]+")


def read_csv(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)


def split_sources(value: str) -> list[str]:
    return [part.strip() for part in value.split(";") if part.strip()]


def source_union(*values: str) -> str:
    output: list[str] = []
    seen: set[str] = set()
    for value in values:
        for source in split_sources(value):
            if source not in seen:
                output.append(source)
                seen.add(source)
    return "; ".join(output)


def extract_urls(value: str) -> list[str]:
    return [url.rstrip(".,)") for url in URL_RE.findall(value)]


def is_regulatory_url(url: str) -> bool:
    host = (urlparse(url).hostname or "").lower()
    return host in REGULATORY_HOSTS


def has_forbidden_source(value: str) -> bool:
    lowered = value.lower()
    return any(pattern in lowered for pattern in FORBIDDEN_SOURCE_PATTERNS)


def regulatory_finding(finding: dict[str, str], fieldnames: set[str]) -> bool:
    if finding.get("kind") != "fact_check":
        return False
    if finding.get("status") not in {"incorrect", "missing", "missing_source"}:
        return False
    field = finding.get("field", "")
    if field not in fieldnames or field in NON_FACT_FIELDS:
        return False
    proposed = finding.get("proposed_value", "").strip()
    if not proposed or has_forbidden_source(proposed):
        return False
    if field == "adverse_symptoms_percentages" and "%" not in proposed:
        return False
    sources = finding.get("sources", "")
    urls = extract_urls(sources)
    return bool(urls) and all(is_regulatory_url(url) for url in urls)


def clean_secondary_sources(value: str) -> str:
    kept = [source for source in split_sources(value) if not has_forbidden_source(source)]
    if len(kept) > 1:
        kept = [
            source
            for source in kept
            if source != "FDA/DailyMed labeling"
            and not source.startswith("FDA/DailyMed Acthar Gel label")
        ]
    return "; ".join(kept)


def normalize_filter_values(row: dict[str, str]) -> None:
    for field, aliases in FILTER_VALUE_ALIASES.items():
        normalized: list[str] = []
        for value in split_sources(row.get(field, "")):
            for replacement in aliases.get(value, [value]):
                if replacement not in normalized:
                    normalized.append(replacement)
        row[field] = "; ".join(normalized)


def main() -> None:
    fieldnames, rows = read_csv(CSV_PATH)
    _, findings = read_csv(FINDINGS_PATH)
    by_name = {row["generic_name"]: row for row in rows}
    source_additions: dict[str, list[str]] = defaultdict(list)
    applied: list[tuple[str, str]] = []

    for finding in findings:
        if not regulatory_finding(finding, set(fieldnames)):
            continue
        generic = finding.get("generic_name", "")
        row = by_name.get(generic)
        if row is None:
            continue
        field = finding["field"]
        proposed = finding["proposed_value"].strip()
        if row.get(field, "") == proposed:
            continue
        expected_current = finding.get("current_value", "")
        if expected_current and row.get(field, "") != expected_current:
            continue
        row[field] = proposed
        applied.append((generic, field))
        source_additions[generic].extend(extract_urls(finding.get("sources", "")))

    refresh_date = datetime.now().strftime("%m-%d-%Y")
    warning_rows = {
        generic
        for generic, field in applied
        if field in {"fda_black_box_warning", "fda_black_box_warning_source"}
    }

    warning_updates = 0
    if UPDATE_FINDINGS_PATH.exists():
        _, update_findings = read_csv(UPDATE_FINDINGS_PATH)
        for finding in update_findings:
            if finding.get("kind") not in {"fda_warning_metadata_refresh", "fda_warning_contradiction"}:
                continue
            generic = finding.get("generic_name", "")
            field = finding.get("column", "")
            proposed = finding.get("proposed_value", "").strip()
            row = by_name.get(generic)
            if row is None or field not in fieldnames or not proposed:
                continue
            if row.get(field, "") != proposed:
                row[field] = proposed
                warning_updates += 1
            if finding.get("kind") == "fda_warning_contradiction":
                evidence_url = finding.get("evidence_url", "").strip()
                source_value = (
                    "FDA/openFDA drug label API; status=boxed_warning_found; "
                    f"api_url={evidence_url}"
                )
                if evidence_url and row.get("fda_black_box_warning_source", "") != source_value:
                    row["fda_black_box_warning_source"] = source_value
                    warning_updates += 1
            warning_rows.add(generic)

    for row in rows:
        generic = row["generic_name"]
        row["evidence_sources"] = clean_secondary_sources(row["evidence_sources"])
        row["mechanism_source"] = clean_secondary_sources(row["mechanism_source"])
        row["evidence_sources"] = source_union(
            row["evidence_sources"],
            row["mechanism_source"],
            "; ".join(source_additions.get(generic, [])),
        )
        row["data_most_recently_refreshed"] = refresh_date
        warning_source = row.get("fda_black_box_warning_source", "")
        if "status=no_boxed_warning_in_selected_fda_label" in warning_source:
            row["fda_black_box_warning"] = "No FDA boxed warning identified in selected current FDA/openFDA label."
        elif "no current FDA label found" in warning_source:
            row["fda_black_box_warning"] = "No current FDA/openFDA label identified."
        if generic in warning_rows:
            row["fda_black_box_warning_verified"] = refresh_date
        normalize_filter_values(row)
        if row.get("pubmed_phase_ii_iii_rct_links", "").strip().upper() == "N/A":
            for field in OUTCOME_FIELDS:
                row[field] = "N/A"
            for field in PLOT_FIELDS:
                row[field] = ""

    write_csv(CSV_PATH, fieldnames, rows)
    print(f"Applied {len(applied)} regulatory corrections across {len({name for name, _ in applied})} rows.")
    print(f"Applied {warning_updates} current FDA/openFDA boxed-warning updates.")
    print(f"Refreshed all {len(rows)} rows on {refresh_date}.")


if __name__ == "__main__":
    main()
