#!/usr/bin/env python3
"""
Comprehensive ASM update checker.

Default behavior is conservative:
  * fetch FDA/DailyMed/openFDA, Epilepsy Foundation, ILAE, NIH ClinicalTrials.gov,
    and PubMed evidence;
  * write findings to pubmed_cache/reports/update_check/;
  * do not edit ASM-list.csv unless --apply is passed;
  * only apply additive/non-conflicting edits automatically;
  * hold contradictory edits for explicit approval.

Approval flow for contradictions:
  1. Run without approval. Review update_check_approval_template.json.
  2. Copy wanted finding ids into approved_findings.
  3. Rerun with --apply --approve-contradictions path/to/file.json.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import html
import json
import re
import sys
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "ASM-list.csv"
DEFAULT_CACHE_DIR = ROOT / ".update-check-cache"
DEFAULT_REPORT_DIR = ROOT / "pubmed_cache" / "reports" / "update_check"
TODAY = datetime.now().strftime("%m-%d-%Y")
ISO_TODAY = datetime.now().strftime("%Y-%m-%d")
YMD_TODAY = datetime.now().strftime("%Y%m%d")

DAILYMED_SPL_SEARCH = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name={term}"
DAILYMED_SPL_XML = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{setid}.xml"
DAILYMED_LABEL_URL = "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={setid}"
OPENFDA_LABEL_API = "https://api.fda.gov/drug/label.json"
PUBMED_EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
CLINICALTRIALS_API = "https://clinicaltrials.gov/api/v2/studies"
BOXED_WARNING_CODE = "34066-1"
INDICATIONS_CODE = "34067-9"

SOURCE_URLS = {
    "Epilepsy Foundation": "https://www.epilepsy.com/tools-resources/seizure-medication-list",
    "ILAE medical therapies": "https://www.ilae.org/patient-care/medical-therapies",
    "ILAE antiepileptic drugs": "https://www.ilae.org/patient-care/antiepileptic-drugs",
    "DailyMed": "https://dailymed.nlm.nih.gov/dailymed/",
    "openFDA labels": "https://open.fda.gov/apis/drug/label/",
    "PubMed E-utilities": "https://www.ncbi.nlm.nih.gov/books/NBK25501/",
    "NIH ClinicalTrials.gov": "https://clinicaltrials.gov/data-api/about-api",
}

SEIZURE_TERMS = [
    "epilepsy",
    "epilepsies",
    "epileptic",
    "seizure",
    "seizures",
    "infantile spasm",
    "infantile spasms",
    "lennox",
    "dravet",
    "status epilepticus",
    "tuberous sclerosis",
]

RCT_EXCLUDE_TITLE_TERMS = [
    "meta-analysis",
    "metaanalysis",
    "systematic review",
    "review",
    "post hoc",
    "post-hoc",
    "pooled analysis",
    "integrated analysis",
    "subgroup",
    "extension",
    "open-label",
    "open label",
    "long-term",
    "long term",
    "follow-up",
    "follow up",
    "observational",
    "retrospective",
    "real-world",
    "case report",
    "protocol",
    "survey",
    "pharmacokinetic",
    "pharmacodynamic",
    "healthy volunteer",
    "healthy subjects",
    "migraine",
    "neuropathic pain",
    "bipolar",
    "dogs",
    "canine",
    "veterinary",
]

SEMICOLON_FIELDS = {
    "alternate_generic_names",
    "trade_names",
    "evidence_sources",
    "pubmed_phase_ii_iii_rct_links",
    "pubmed_search_aliases",
    PLOT_RR50_FIELD if "PLOT_RR50_FIELD" in globals() else "plot_diff_50_responder_maximum_effective_dose",
    PLOT_MPC_FIELD if "PLOT_MPC_FIELD" in globals() else "plot_diff_median_pct_change_maximum_effective_dose",
    PLOT_SF_FIELD if "PLOT_SF_FIELD" in globals() else "plot_diff_seizure_freedom_maximum_effective_dose",
}

FILTER_DEFAULTS = {
    "filter_availability": "Needs review",
    "filter_metabolism": "Needs review",
    "filter_mechanism": "Needs review",
    "filter_epilepsy_type": "Needs review",
    "filter_formulation": "Needs review",
    "filter_enzyme_effect": "Needs review",
    "filter_qt_effect": "Needs review",
    "filter_symptom_category": "Needs review",
}

RCT_REPORT_PATH = ROOT / "pubmed_cache" / "reports" / "pubmed_rct_audit.csv"
OUTCOME_REPORT_PATH = ROOT / "pubmed_cache" / "reports" / "efficacy_outcome_audit.csv"

RR50_FIELD = "diff_50_responder_maximum_effective_dose"
MPC_FIELD = "diff_median_pct_change_maximum_effective_dose"
SF_FIELD = "diff_seizure_freedom_maximum_effective_dose"
PLOT_RR50_FIELD = "plot_diff_50_responder_maximum_effective_dose"
PLOT_MPC_FIELD = "plot_diff_median_pct_change_maximum_effective_dose"
PLOT_SF_FIELD = "plot_diff_seizure_freedom_maximum_effective_dose"

OUTCOME_SPECS = [
    (RR50_FIELD, PLOT_RR50_FIELD, "rr50_differential_percent", "rr50_included_in_csv_summary", "RR50 differential"),
    (MPC_FIELD, PLOT_MPC_FIELD, "mpc_differential_percent", "mpc_included_in_csv_summary", "MPC differential"),
    (SF_FIELD, PLOT_SF_FIELD, "sf_differential_percent", "sf_included_in_csv_summary", "seizure-freedom differential"),
]

DETAILED_FACT_FIELDS = [
    "epilepsy_type",
    "mechanism_of_action",
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
]

SOURCE_FACT_STOPWORDS = {
    "about",
    "above",
    "adults",
    "also",
    "appears",
    "available",
    "based",
    "because",
    "broad",
    "clinically",
    "current",
    "daily",
    "data",
    "described",
    "dose",
    "doses",
    "drug",
    "during",
    "effect",
    "effects",
    "established",
    "fda",
    "form",
    "found",
    "from",
    "human",
    "identified",
    "including",
    "individualized",
    "known",
    "label",
    "labeled",
    "major",
    "meaningful",
    "metabolism",
    "not",
    "notes",
    "oral",
    "range",
    "selected",
    "shown",
    "source",
    "tablet",
    "therapy",
    "treatment",
    "typical",
    "used",
    "with",
    "without",
}

# These names are used only as parsing hints for source pages that render
# medication lists as plain text. FDA/openFDA and DailyMed discovery remain the
# primary path for truly new approved drugs.
ASM_NAME_HINTS = {
    "acetazolamide",
    "adrenocorticotropic hormone",
    "beclamide",
    "brivaracetam",
    "cannabidiol",
    "carbamazepine",
    "cenobamate",
    "clobazam",
    "clonazepam",
    "clorazepate",
    "diazepam",
    "divalproex sodium",
    "eslicarbazepine acetate",
    "ethadione",
    "ethosuximide",
    "ethotoin",
    "everolimus",
    "ezogabine",
    "felbamate",
    "fenfluramine",
    "fosphenytoin",
    "gabapentin",
    "ganaxolone",
    "lacosamide",
    "lamotrigine",
    "levetiracetam",
    "lorazepam",
    "methsuximide",
    "midazolam",
    "oxcarbazepine",
    "perampanel",
    "phenobarbital",
    "phenytoin",
    "piracetam",
    "pregabalin",
    "primidone",
    "rufinamide",
    "stiripentol",
    "sultiame",
    "tiagabine",
    "topiramate",
    "valproic acid",
    "vigabatrin",
    "zonisamide",
}


@dataclass
class SourceObservation:
    source: str
    candidate_name: str
    evidence_url: str
    summary: str
    trade_names: list[str] = field(default_factory=list)
    raw: dict[str, Any] = field(default_factory=dict)


@dataclass
class Finding:
    id: str
    kind: str
    severity: str
    generic_name: str
    source: str
    evidence_url: str
    summary: str
    column: str = ""
    current_value: str = ""
    proposed_value: str = ""
    safe_to_apply: bool = False
    requires_approval: bool = False
    proposed_updates: dict[str, str] = field(default_factory=dict)
    details: dict[str, Any] = field(default_factory=dict)


class SourceError(RuntimeError):
    pass


class HttpClient:
    def __init__(self, cache_dir: Path, refresh: bool = False, offline: bool = False, throttle: float = 0.05):
        self.cache_dir = cache_dir
        self.refresh = refresh
        self.offline = offline
        self.throttle = throttle
        self.cache_dir.mkdir(parents=True, exist_ok=True)

    def get_bytes(self, url: str, suffix: str = ".txt") -> bytes:
        key = hashlib.sha256(url.encode("utf-8")).hexdigest()[:32]
        path = self.cache_dir / f"{key}{suffix}"
        if path.exists() and not self.refresh:
            return path.read_bytes()
        if self.offline:
            raise SourceError(f"offline mode and no cached response for {url}")
        request = urllib.request.Request(
            url,
            headers={
                "User-Agent": "ASM-master update_check/1.0 (+local research audit)",
                "Accept": "application/json,text/html,application/xml;q=0.9,*/*;q=0.8",
            },
        )
        try:
            with urllib.request.urlopen(request, timeout=60) as response:
                data = response.read()
        except urllib.error.HTTPError as exc:
            raise SourceError(f"HTTP {exc.code} for {url}") from exc
        except urllib.error.URLError as exc:
            raise SourceError(f"network error for {url}: {exc.reason}") from exc
        path.write_bytes(data)
        time.sleep(self.throttle)
        return data

    def get_text(self, url: str) -> str:
        return self.get_bytes(url, ".html").decode("utf-8", errors="replace")

    def get_json(self, url: str) -> dict[str, Any]:
        raw = self.get_bytes(url, ".json").decode("utf-8", errors="replace")
        try:
            return json.loads(raw)
        except json.JSONDecodeError as exc:
            raise SourceError(f"JSON parse error for {url}: {exc}") from exc


def normalize_space(value: str | None) -> str:
    return re.sub(r"\s+", " ", value or "").strip()


def strip_html(value: str) -> str:
    value = re.sub(r"(?is)<script\b.*?</script>", " ", value)
    value = re.sub(r"(?is)<style\b.*?</style>", " ", value)
    value = re.sub(r"(?s)<[^>]+>", " ", value)
    return normalize_space(html.unescape(value))


def normalize_key(value: str | None) -> str:
    value = unicodedata.normalize("NFKD", value or "")
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = value.replace("®", "").replace("™", "")
    value = re.sub(r"\([^)]*\)", " ", value)
    value = re.sub(r"[^a-zA-Z0-9]+", " ", value).lower()
    return normalize_space(value)


def strip_form_modifiers(value: str) -> str:
    key = normalize_key(value)
    key = re.sub(
        r"\b(oral solution|nasal spray|rectal gel|rectal|nasal|extended release|"
        r"modified release|delayed release|xr|er|odt|tablet|capsule|solution|"
        r"injection|suspension|hydrochloride)\b",
        " ",
        key,
    )
    return normalize_space(key)


def display_name(value: str) -> str:
    return normalize_space(value).lower()


def split_semicolon(value: str | None) -> list[str]:
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def split_loose(value: str | None) -> list[str]:
    return [part.strip() for part in re.split(r";|\n|,", value or "") if part.strip()]


def split_rct_entries(value: str | None) -> list[str]:
    value = normalize_space(value)
    if not value or value.lower() in {"n/a", "no pubmed phase ii/iii rcts found", "needs review"}:
        return []
    return [part.strip() for part in value.split(";") if part.strip()]


def merge_semicolon(existing: str, additions: list[str]) -> str:
    merged: list[str] = []
    seen: set[str] = set()
    for item in split_semicolon(existing) + additions:
        cleaned = normalize_space(item)
        key = normalize_key(cleaned)
        if cleaned and key not in seen:
            seen.add(key)
            merged.append(cleaned)
    return "; ".join(merged)


def append_note(existing: str, addition: str) -> str:
    existing = normalize_space(existing)
    addition = normalize_space(addition)
    if not addition:
        return existing
    if not existing:
        return addition
    if addition in existing:
        return existing
    return f"{existing} {addition}"


def remove_semicolon_value(existing: str, value_to_remove: str) -> str:
    remove_key = normalize_key(value_to_remove)
    kept = [item for item in split_semicolon(existing) if normalize_key(item) != remove_key]
    return "; ".join(kept)


def normalize_for_compare(value: str | None) -> str:
    return normalize_space(value).replace(" ,", ",").replace(" .", ".")


def is_blankish(value: str | None) -> bool:
    cleaned = normalize_space(value).lower()
    return cleaned in {"", "nr", "n/a", "needs review", "not reviewed"}


def read_dicts(path: Path) -> tuple[list[str], list[dict[str, str]]]:
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def write_dicts(path: Path, fieldnames: list[str], rows: list[dict[str, str]]) -> None:
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)


def format_number(value: str | float) -> str:
    number = round(float(value), 2)
    if number.is_integer():
        return str(int(number))
    return f"{number:.2f}".rstrip("0").rstrip(".")


def parse_float(value: str | None) -> float | None:
    value = normalize_space(value)
    if not value:
        return None
    try:
        return float(value)
    except ValueError:
        return None


def outcome_summary(rows: list[dict[str, str]], diff_field: str, include_field: str, noun: str) -> str:
    included = [row for row in rows if row.get(include_field) == "yes" and row.get(diff_field)]
    if not included:
        return ""
    values = [float(row[diff_field]) for row in included]
    low = min(values)
    high = max(values)
    value_text = f"{format_number(low)} %" if low == high else f"{format_number(low)}-{format_number(high)} %"
    details = "; ".join(
        f"{row['label']} {row['dose_or_regimen']} {format_number(row[diff_field])}%"
        for row in included
    )
    return f"{value_text} (drug minus placebo {noun} at maximum effective dose/regimen: {details})"


def outcome_plot(rows: list[dict[str, str]], diff_field: str, include_field: str) -> str:
    included = [row for row in rows if row.get(include_field) == "yes" and row.get(diff_field)]
    return "; ".join(
        f"{row['label']}|{format_number(row[diff_field])}|{row['pubmed_url']}|{row.get('n_analyzed_or_randomized', '')}"
        if row.get("n_analyzed_or_randomized")
        else f"{row['label']}|{format_number(row[diff_field])}|{row['pubmed_url']}"
        for row in included
    )


def extract_pubmed_links(value: str | None) -> list[dict[str, str]]:
    links: list[dict[str, str]] = []
    for entry in split_rct_entries(value):
        match = re.match(r"^(.*?)\|(https?://\S+)$", entry) or re.match(r"^(.*?):\s*(https?://\S+)$", entry)
        if not match:
            links.append({"entry": entry, "label": "", "url": "", "pmid": ""})
            continue
        label = normalize_space(match.group(1))
        url = match.group(2).rstrip(".,)")
        pmid_match = re.search(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", url)
        links.append({"entry": entry, "label": label, "url": url, "pmid": pmid_match.group(1) if pmid_match else ""})
    return links


def canonical_pubmed_links(value: str | None) -> str:
    entries = []
    for link in extract_pubmed_links(value):
        if link["pmid"]:
            label = link["label"] or f"PMID{link['pmid']}"
            entries.append(f"{label}|https://pubmed.ncbi.nlm.nih.gov/{link['pmid']}/")
        else:
            entries.append(link["entry"])
    return "; ".join(entries)


def row_terms(row: dict[str, str]) -> list[str]:
    terms = [row.get("generic_name", "")]
    terms.extend(split_semicolon(row.get("alternate_generic_names", "")))
    terms.extend(split_semicolon(row.get("trade_names", "")))
    terms.extend(split_semicolon(row.get("pubmed_search_aliases", "")))
    cleaned: list[str] = []
    seen: set[str] = set()
    for term in terms:
        term = re.sub(r"\s*\([^)]*\)", "", term or "").strip()
        lowered = term.lower()
        if not term or "no human" in lowered or "veterinary" in lowered:
            continue
        if len(term) < 3 or len(term.split()) > 6:
            continue
        key = normalize_key(term)
        if key not in seen:
            seen.add(key)
            cleaned.append(term)
    return cleaned


def slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "source"


def finding_id(kind: str, generic_name: str, column: str, source: str, proposed_value: str, evidence_url: str) -> str:
    payload = "|".join([kind, normalize_key(generic_name), column, source, evidence_url, proposed_value[:500]])
    return f"{kind}-{hashlib.sha256(payload.encode('utf-8')).hexdigest()[:12]}"


def make_finding(
    kind: str,
    severity: str,
    generic_name: str,
    source: str,
    evidence_url: str,
    summary: str,
    column: str = "",
    current_value: str = "",
    proposed_value: str = "",
    safe_to_apply: bool = False,
    requires_approval: bool = False,
    proposed_updates: dict[str, str] | None = None,
    details: dict[str, Any] | None = None,
) -> Finding:
    return Finding(
        id=finding_id(kind, generic_name, column, source, proposed_value, evidence_url),
        kind=kind,
        severity=severity,
        generic_name=generic_name,
        source=source,
        evidence_url=evidence_url,
        summary=summary,
        column=column,
        current_value=current_value,
        proposed_value=proposed_value,
        safe_to_apply=safe_to_apply,
        requires_approval=requires_approval,
        proposed_updates=proposed_updates or {},
        details=details or {},
    )


def parse_date(value: str | None) -> datetime:
    value = normalize_space(value)
    if not value:
        return datetime.min
    for fmt in ("%b %d, %Y", "%B %d, %Y", "%m-%d-%Y", "%Y-%m-%d", "%Y%m%d"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass
    try:
        parsed = parsedate_to_datetime(value)
        return parsed.replace(tzinfo=None)
    except Exception:
        return datetime.min


def xml_text(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return html.unescape(normalize_space(" ".join(element.itertext())))


def section_title(section: ET.Element, ns: dict[str, str]) -> str:
    return xml_text(section.find("hl7:title", ns))


def section_code(section: ET.Element, ns: dict[str, str]) -> tuple[str, str]:
    code = section.find("hl7:code", ns)
    if code is None:
        return "", ""
    return code.attrib.get("code", ""), code.attrib.get("displayName", "")


def title_from_xml(xml_bytes: bytes) -> str:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return ""
    ns = {"hl7": "urn:hl7-org:v3"}
    return xml_text(root.find(".//hl7:title", ns))


def extract_label_section(xml_bytes: bytes, target_code: str, title_prefixes: tuple[str, ...]) -> str:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return ""
    ns = {"hl7": "urn:hl7-org:v3"}
    matches: list[str] = []
    for section in root.findall(".//hl7:section", ns):
        title = section_title(section, ns).upper()
        code, display = section_code(section, ns)
        if code == target_code or title.startswith(title_prefixes) or display.upper().startswith(title_prefixes):
            text = xml_text(section)
            if text:
                matches.append(text)
    return max(matches, key=len) if matches else ""


def extract_full_label_text(xml_bytes: bytes) -> str:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return ""
    return xml_text(root)


def extract_boxed_warning(xml_bytes: bytes) -> tuple[str, str, str]:
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return "", "", ""
    ns = {"hl7": "urn:hl7-org:v3"}
    boxed_sections: list[dict[str, str]] = []
    for section in root.findall(".//hl7:section", ns):
        title = section_title(section, ns)
        code, display = section_code(section, ns)
        title_upper = title.upper()
        display_upper = display.upper()
        is_boxed = (
            code == BOXED_WARNING_CODE
            or title_upper.startswith("BOXED WARNING")
            or title_upper.startswith("WARNING:")
            or display_upper.startswith("BOXED WARNING")
        )
        if is_boxed:
            text = xml_text(section)
            lead = text.upper()[:300]
            if text and ("WARNING" in lead or "WARNINGS" in lead):
                boxed_sections.append({"title": title, "code": code, "text": text})
    if not boxed_sections:
        return "", "", ""
    selected = max(boxed_sections, key=lambda item: len(item["text"]))
    return selected["text"], selected["title"], selected["code"]


def reject_dailymed_title(title: str) -> bool:
    title_upper = title.upper()
    rejected = [
        "ANIMAL",
        "VETERINARY",
        "HOMEOPATHIC",
        "LABEL: OTC",
        "KBROVET",
        "K-BROVET",
        "LIBROMIDE",
    ]
    return any(term in title_upper for term in rejected)


def dailymed_search(client: HttpClient, term: str) -> list[dict[str, Any]]:
    url = DAILYMED_SPL_SEARCH.format(term=urllib.parse.quote(term))
    data = client.get_json(url)
    return data.get("data") or []


def fetch_dailymed_xml(client: HttpClient, setid: str) -> bytes:
    return client.get_bytes(DAILYMED_SPL_XML.format(setid=setid), ".xml")


def setids_from_existing_sources(row: dict[str, str]) -> list[str]:
    text = " ".join([row.get("fda_black_box_warning_source", ""), row.get("fda_black_box_warning", "")])
    return sorted(set(re.findall(r"setid=([0-9a-fA-F-]{20,})", text)))


def candidate_is_relevant(row: dict[str, str], candidate: dict[str, Any]) -> bool:
    original_title = (candidate.get("title") or "").lower()
    title = normalize_key(candidate.get("title", ""))
    generic = normalize_key(row.get("generic_name", ""))
    acceptable = [normalize_key(term) for term in row_terms(row)]
    acceptable = [term for term in acceptable if len(term) >= 5]
    if any(title.startswith(term) for term in acceptable):
        return True
    if f" {generic} " in f" {title} " and title.find(generic) < 35:
        return True
    original_index = original_title.find(row.get("generic_name", "").lower())
    if original_index >= 0 and "," in original_title[:original_index]:
        return False
    return f" {generic} " in f" {title} "


def score_dailymed_candidate(row: dict[str, str], candidate: dict[str, Any], boxed_text: str, indications: str) -> float:
    title = candidate.get("title", "")
    title_lower = title.lower()
    generic = row.get("generic_name", "").lower()
    score = 0.0
    if boxed_text:
        score += 10000
    if any(term in indications.lower() for term in SEIZURE_TERMS):
        score += 900
    for index, term in enumerate(row_terms(row)):
        if term.lower() in title_lower:
            score += 800 - index
    if generic and generic in title_lower:
        score += 300
    if "injection" in row.get("formulations_available", "").lower() and "injection" in title_lower:
        score += 120
    if any(bad in title_lower for bad in ["repack", "unit dose", "kit"]):
        score -= 50
    score += parse_date(candidate.get("published_date", "")).toordinal() / 1000000
    return score


def source_string_for_dailymed(candidate: dict[str, Any] | None, search_terms: list[str], status: str) -> str:
    if not candidate:
        return f"FDA/DailyMed search on {TODAY}: no current label found for terms [{'; '.join(search_terms)}]."
    setid = candidate.get("setid", "")
    return (
        f"FDA/DailyMed SPL; status={status}; setid={setid}; "
        f"published={candidate.get('published_date', '')}; title={candidate.get('title', '')}; "
        f"url={DAILYMED_LABEL_URL.format(setid=setid)}"
    )


def select_dailymed_label(client: HttpClient, row: dict[str, str]) -> dict[str, Any]:
    search_terms = row_terms(row) or [row.get("generic_name", "")]
    candidates_by_setid: dict[str, dict[str, Any]] = {}
    for setid in setids_from_existing_sources(row):
        try:
            xml_bytes = fetch_dailymed_xml(client, setid)
            title = title_from_xml(xml_bytes)
        except SourceError:
            title = ""
        candidates_by_setid[setid] = {"setid": setid, "title": title, "published_date": ""}

    for term in search_terms:
        for hit in dailymed_search(client, term)[:10]:
            title = hit.get("title", "")
            setid = hit.get("setid", "")
            if not setid or reject_dailymed_title(title):
                continue
            if not candidate_is_relevant(row, hit):
                continue
            candidates_by_setid.setdefault(setid, hit)
            if len(candidates_by_setid) >= 24:
                break
        if len(candidates_by_setid) >= 24:
            break

    evaluated: list[dict[str, Any]] = []
    for candidate in candidates_by_setid.values():
        setid = candidate["setid"]
        try:
            xml_bytes = fetch_dailymed_xml(client, setid)
        except SourceError:
            continue
        if not candidate.get("title"):
            candidate["title"] = title_from_xml(xml_bytes)
        boxed_text, boxed_title, boxed_code = extract_boxed_warning(xml_bytes)
        indications = extract_label_section(xml_bytes, INDICATIONS_CODE, ("INDICATIONS",))
        label_text = extract_full_label_text(xml_bytes)
        evaluated.append(
            {
                "candidate": candidate,
                "boxed_text": boxed_text,
                "boxed_title": boxed_title,
                "boxed_code": boxed_code,
                "indications": indications,
                "label_text": label_text,
                "score": score_dailymed_candidate(row, candidate, boxed_text, indications),
            }
        )

    if not evaluated:
        return {
            "status": "no_current_fda_label",
            "warning": "No current FDA/DailyMed label identified.",
            "source": source_string_for_dailymed(None, search_terms, "no_current_fda_label"),
            "candidate": {},
            "search_terms": search_terms,
            "boxed_title": "",
            "boxed_code": "",
            "indications": "",
            "label_text": "",
            "evidence_url": "",
        }

    selected = max(evaluated, key=lambda item: item["score"])
    candidate = selected["candidate"]
    setid = candidate["setid"]
    if selected["boxed_text"]:
        status = "boxed_warning_found"
        warning = selected["boxed_text"]
    else:
        status = "no_boxed_warning_in_selected_label"
        warning = "No FDA boxed warning identified in selected current DailyMed label."
    return {
        "status": status,
        "warning": warning,
        "source": source_string_for_dailymed(candidate, search_terms, status),
        "candidate": candidate,
        "search_terms": search_terms,
        "boxed_title": selected.get("boxed_title", ""),
        "boxed_code": selected.get("boxed_code", ""),
        "indications": selected.get("indications", ""),
        "label_text": selected.get("label_text", ""),
        "evidence_url": DAILYMED_LABEL_URL.format(setid=setid),
    }


def source_error_finding(source: str, evidence_url: str, message: str) -> Finding:
    return make_finding(
        kind="source_error",
        severity="warning",
        generic_name="",
        source=source,
        evidence_url=evidence_url,
        summary=message,
        details={"error": message},
    )


def text_has_seizure_context(text: str) -> bool:
    text = text.lower()
    return any(term in text for term in SEIZURE_TERMS)


def parse_epilepsy_foundation(html_text: str, known_names: set[str]) -> list[SourceObservation]:
    if "Attention Required!" in html_text and "Cloudflare" in html_text:
        raise SourceError("Epilepsy Foundation returned a Cloudflare block page")
    text = strip_html(html_text)
    observations: list[SourceObservation] = []

    # Visible cards use headings; these are the most reliable names when present.
    for match in re.finditer(r"(?is)<h[234][^>]*>\s*<a[^>]+href=[\"']([^\"']+)[\"'][^>]*>(.*?)</a>", html_text):
        href, label_html = match.groups()
        label = normalize_space(strip_html(label_html))
        if label and not re.search(r"view details|load more|clear filters", label, re.I):
            url = urllib.parse.urljoin(SOURCE_URLS["Epilepsy Foundation"], href)
            observations.append(
                SourceObservation(
                    source="Epilepsy Foundation",
                    candidate_name=label,
                    evidence_url=url,
                    summary=f"Medication appears on Epilepsy Foundation seizure medication list as '{label}'.",
                )
            )

    # The page also renders a select-style text list. It has weak delimiters, so
    # scan for known ASM names and known missing rows as parsing hints.
    for name in sorted(known_names | ASM_NAME_HINTS, key=len, reverse=True):
        pattern = rf"(?<![A-Za-z0-9]){re.escape(name)}(?:\s+(?:oral solution|nasal spray|rectal|xr|er|hydrochloride))?(?![A-Za-z0-9])"
        match = re.search(pattern, text, flags=re.I)
        if match:
            label = normalize_space(match.group(0))
            observations.append(
                SourceObservation(
                    source="Epilepsy Foundation",
                    candidate_name=label,
                    evidence_url=SOURCE_URLS["Epilepsy Foundation"],
                    summary=f"Medication name found on Epilepsy Foundation seizure medication list: '{label}'.",
                )
            )
    return dedupe_observations(observations)


def parse_ilae_pages(pages: dict[str, str], known_names: set[str]) -> list[SourceObservation]:
    observations: list[SourceObservation] = []
    hints = known_names | ASM_NAME_HINTS
    for label, page_text in pages.items():
        text = strip_html(page_text)
        source_url = SOURCE_URLS[label]
        for name in sorted(hints, key=len, reverse=True):
            if re.search(rf"(?<![A-Za-z0-9]){re.escape(name)}(?![A-Za-z0-9])", text, flags=re.I):
                observations.append(
                    SourceObservation(
                        source="ILAE",
                        candidate_name=name,
                        evidence_url=source_url,
                        summary=f"Medication term found on {label}.",
                    )
                )
    return dedupe_observations(observations)


def dedupe_observations(observations: list[SourceObservation]) -> list[SourceObservation]:
    seen: set[tuple[str, str, str]] = set()
    output: list[SourceObservation] = []
    for observation in observations:
        key = (observation.source, strip_form_modifiers(observation.candidate_name), observation.evidence_url)
        if key in seen:
            continue
        seen.add(key)
        output.append(observation)
    return output


def openfda_url(params: dict[str, str]) -> str:
    return f"{OPENFDA_LABEL_API}?{urllib.parse.urlencode(params)}"


def split_openfda_names(names: list[str]) -> list[str]:
    output: list[str] = []
    for name in names:
        cleaned = normalize_space(name)
        if not cleaned:
            continue
        parts = re.split(r"\s*(?:;|/|\band\b|\+)\s*", cleaned, flags=re.I)
        for part in parts:
            part = re.sub(r"\b\d+(?:\.\d+)?\s*(?:mg|mcg|g|ml|%)\b", " ", part, flags=re.I)
            part = normalize_space(part)
            if 2 < len(part) < 80:
                output.append(part)
    return output


def collect_openfda_candidates(client: HttpClient, since_ymd: str | None = None, limit: int = 100) -> list[SourceObservation]:
    observations: list[SourceObservation] = []
    query_terms = [
        "epilepsy",
        "seizure",
        "partial-onset seizures",
        "lennox-gastaut",
        "dravet",
        "tuberous sclerosis complex",
        "status epilepticus",
    ]
    for term in query_terms:
        search = f'indications_and_usage:"{term}"'
        if since_ymd:
            search = f"({search}) AND effective_time:[{since_ymd} TO {YMD_TODAY}]"
        url = openfda_url({"search": search, "limit": str(limit)})
        try:
            data = client.get_json(url)
        except SourceError as exc:
            # openFDA returns 404 JSON for no matches; treat it as no results.
            if "HTTP 404" in str(exc):
                continue
            raise
        for record in data.get("results", []):
            text = " ".join(record.get("indications_and_usage", []) + record.get("purpose", []))
            if not text_has_seizure_context(text):
                continue
            openfda = record.get("openfda", {})
            candidate_names = split_openfda_names(
                openfda.get("generic_name", [])
                or openfda.get("substance_name", [])
                or record.get("active_ingredient", [])
            )
            brand_names = split_openfda_names(openfda.get("brand_name", []))
            effective_time = record.get("effective_time", "")
            setid = (openfda.get("spl_set_id") or [""])[0]
            evidence_url = DAILYMED_LABEL_URL.format(setid=setid) if setid else SOURCE_URLS["openFDA labels"]
            for name in candidate_names:
                observations.append(
                    SourceObservation(
                        source="FDA/openFDA",
                        candidate_name=name,
                        evidence_url=evidence_url,
                        summary=(
                            f"openFDA label indication text matched '{term}'"
                            + (f"; effective_time={effective_time}" if effective_time else "")
                        ),
                        trade_names=brand_names,
                        raw={
                            "effective_time": effective_time,
                            "setid": setid,
                            "term": term,
                            "indications": normalize_space(text)[:1000],
                        },
                    )
                )
    return dedupe_observations(observations)


def aliases_for_pubmed(row: dict[str, str]) -> list[str]:
    names = [row.get("generic_name", "")]
    names.extend(split_loose(row.get("alternate_generic_names", "")))
    names.extend(split_loose(row.get("trade_names", "")))
    names.extend(split_loose(row.get("pubmed_search_aliases", "")))
    cleaned: list[str] = []
    seen: set[str] = set()
    for name in names:
        name = normalize_space(name)
        if not name or name.lower() in {"also"}:
            continue
        key = normalize_key(name)
        if key not in seen:
            seen.add(key)
            cleaned.append(name)
    return cleaned


def pubmed_drug_query_terms(row: dict[str, str]) -> str:
    terms: list[str] = []
    for name in aliases_for_pubmed(row):
        escaped = name.replace('"', '\\"')
        terms.append(f'"{escaped}"[Title/Abstract]')
        if len(name.split()) <= 3:
            terms.append(f'"{escaped}"[All Fields]')
    return " OR ".join(terms)


def pubmed_query(row: dict[str, str], since_date: str | None = None) -> str:
    drug_terms = pubmed_drug_query_terms(row)
    seizure = " OR ".join(f'"{term}"[Title/Abstract]' for term in SEIZURE_TERMS)
    placebo = '"placebo"[Title/Abstract] OR "placebo-controlled"[Title/Abstract] OR "placebo controlled"[Title/Abstract]'
    randomized = (
        '"randomized"[Title/Abstract] OR "randomised"[Title/Abstract] OR '
        '"randomly"[Title/Abstract] OR "randomized controlled trial"[Publication Type] OR '
        '"random allocation"[MeSH Terms] OR "double-blind"[Title/Abstract] OR "double blind"[Title/Abstract]'
    )
    clinical = (
        '"clinical trial"[Publication Type] OR "controlled clinical trial"[Publication Type] OR '
        '"randomized controlled trial"[Publication Type] OR "clinical trial, phase ii"[Publication Type] OR '
        '"clinical trial, phase iii"[Publication Type] OR "phase 2"[Title/Abstract] OR "phase II"[Title/Abstract] OR '
        '"phase 3"[Title/Abstract] OR "phase III"[Title/Abstract] OR "trial"[Title/Abstract]'
    )
    excluded = '"review"[Publication Type] OR "meta-analysis"[Publication Type] OR "systematic review"[Publication Type]'
    query = f"(({drug_terms}) AND ({seizure}) AND ({placebo}) AND ({randomized}) AND ({clinical}) NOT ({excluded}))"
    if since_date:
        start = since_date.replace("-", "/")
        query = f'({query}) AND ("{start}"[Date - Publication] : "3000"[Date - Publication])'
    return query


def eutils_url(path: str, params: dict[str, str]) -> str:
    return f"{PUBMED_EUTILS}/{path}?{urllib.parse.urlencode(params)}"


def pubmed_esearch(client: HttpClient, row: dict[str, str], since_date: str | None, retmax: int) -> list[str]:
    url = eutils_url(
        "esearch.fcgi",
        {
            "db": "pubmed",
            "retmode": "json",
            "retmax": str(retmax),
            "sort": "pub date",
            "term": pubmed_query(row, since_date),
        },
    )
    data = client.get_json(url)
    return data.get("esearchresult", {}).get("idlist", [])


def pubmed_efetch(client: HttpClient, pmids: list[str]) -> dict[str, dict[str, Any]]:
    articles: dict[str, dict[str, Any]] = {}
    if not pmids:
        return articles
    for index in range(0, len(pmids), 150):
        chunk = pmids[index : index + 150]
        url = eutils_url("efetch.fcgi", {"db": "pubmed", "retmode": "xml", "id": ",".join(chunk)})
        xml_bytes = client.get_bytes(url, ".xml")
        root = ET.fromstring(xml_bytes)
        for article in root.findall(".//PubmedArticle"):
            pmid = article.findtext(".//PMID", default="").strip()
            if not pmid:
                continue
            first_author = article.find(".//AuthorList/Author")
            last_name = first_author.findtext("LastName", default="") if first_author is not None else ""
            collective = first_author.findtext("CollectiveName", default="") if first_author is not None else ""
            articles[pmid] = {
                "pmid": pmid,
                "title": xml_text(article.find(".//ArticleTitle")),
                "abstract": xml_text(article.find(".//Abstract")),
                "year": pubmed_article_year(article),
                "first_author": last_name or collective or "PMID",
                "pub_types": [xml_text(node) for node in article.findall(".//PublicationType")],
            }
    return articles


def pubmed_article_year(article: ET.Element) -> str:
    for path in [
        ".//ArticleDate/Year",
        ".//JournalIssue/PubDate/Year",
        ".//PubMedPubDate[@PubStatus='pubmed']/Year",
        ".//PubMedPubDate[@PubStatus='medline']/Year",
    ]:
        node = article.find(path)
        if node is not None and node.text:
            return node.text.strip()
    medline = article.findtext(".//JournalIssue/PubDate/MedlineDate", default="")
    match = re.search(r"(19|20)\d{2}", medline)
    return match.group(0) if match else "n.d."


def ascii_label(value: str) -> str:
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^A-Za-z0-9]+", "", value)
    return value or "PMID"


def make_pubmed_label(article: dict[str, Any]) -> str:
    return f"{ascii_label(article.get('first_author', 'PMID'))}{article.get('year', 'n.d.')}"


def title_contains_drug(article: dict[str, Any], row: dict[str, str]) -> bool:
    title = article["title"].lower()
    for alias in aliases_for_pubmed(row):
        alias_l = alias.lower()
        if re.search(rf"(?<![a-z0-9]){re.escape(alias_l)}(?![a-z0-9])", title):
            return True
    return False


def title_names_primary_drug(article: dict[str, Any], row: dict[str, str]) -> bool:
    title = article["title"].lower()
    normalized = re.sub(r"[^a-z0-9]+", " ", title).strip()
    for alias in aliases_for_pubmed(row):
        alias_l = alias.lower()
        alias_norm = re.sub(r"[^a-z0-9]+", " ", alias_l).strip()
        if not alias_norm:
            continue
        patterns = [
            alias_norm,
            f"of {alias_norm}",
            f"with {alias_norm}",
            f"adjunctive {alias_norm}",
            f"add on {alias_norm}",
            f"{alias_norm} as",
            f"{alias_norm} for",
            f"{alias_norm} in",
            f"{alias_norm} therapy",
            f"{alias_norm} treatment",
            f"trial of {alias_norm}",
            f"evaluating {alias_norm}",
        ]
        if normalized.startswith(alias_norm) or any(pattern in normalized for pattern in patterns[1:]):
            return True
    return False


def title_has_seizure_context(article: dict[str, Any]) -> bool:
    title = article["title"].lower()
    return any(term in title for term in SEIZURE_TERMS + ["convulsion", "convulsions", "epileptiform"])


def is_pubmed_qualifying(article: dict[str, Any], row: dict[str, str], forced_pmids: set[str]) -> tuple[bool, str]:
    title = article["title"].lower()
    text = f"{article['title']} {article['abstract']}".lower()
    pub_types = " ".join(article["pub_types"]).lower()
    if article["pmid"] in forced_pmids:
        return True, "already included in CSV/report"
    if not title_contains_drug(article, row):
        return False, "drug term not in title"
    if not title_names_primary_drug(article, row):
        return False, "drug appears in title but not as primary intervention"
    if not title_has_seizure_context(article):
        return False, "title lacks seizure/epilepsy context"
    if any(term in title for term in RCT_EXCLUDE_TITLE_TERMS):
        return False, "excluded secondary/non-primary title"
    if (" vs " in title or "versus" in title or "comparison of" in title or "comparing" in title) and "placebo" not in title:
        return False, "active-comparator/comparison title without placebo"
    if not any(term in text for term in SEIZURE_TERMS):
        return False, "no seizure/epilepsy context"
    if "placebo" not in text:
        return False, "no placebo language"
    has_random = ("random" in text) or ("randomized controlled trial" in pub_types) or ("random allocation" in text)
    if not has_random:
        return False, "no randomized language"
    primary_title = any(
        marker in title
        for marker in [
            "randomized",
            "randomised",
            "placebo-controlled",
            "placebo controlled",
            "double-blind",
            "double blind",
            "phase ii",
            "phase 2",
            "phase iii",
            "phase 3",
            "phase ii/iii",
            "trial",
            "effect of",
            "effects of",
        ]
    )
    if not primary_title:
        return False, "title lacks primary randomized/placebo/phase trial language"
    clinical = (
        "randomized controlled trial" in pub_types
        or "clinical trial" in pub_types
        or "controlled clinical trial" in pub_types
        or "phase" in text
        or "double-blind" in text
        or "double blind" in text
    )
    if not clinical:
        return False, "not indexed/described as clinical trial"
    if any(kind in pub_types for kind in ["review", "meta-analysis"]):
        return False, "review/meta-analysis publication type"
    return True, "qualifying PubMed placebo-controlled randomized ASM trial report"


def existing_pmids(row: dict[str, str]) -> set[str]:
    text = " ".join(
        [
            row.get("pubmed_phase_ii_iii_rct_links", ""),
            row.get("rct_pubmed_verification_notes", ""),
        ]
    )
    return set(re.findall(r"pubmed\.ncbi\.nlm\.nih\.gov/(\d+)", text))


def clinicaltrials_url(row: dict[str, str], page_size: int) -> str:
    params = {
        "format": "json",
        "pageSize": str(page_size),
        "query.cond": "Epilepsy OR Seizures",
        "query.intr": row.get("generic_name", ""),
    }
    return f"{CLINICALTRIALS_API}?{urllib.parse.urlencode(params)}"


def nct_fields(study: dict[str, Any]) -> dict[str, Any]:
    protocol = study.get("protocolSection", {})
    identification = protocol.get("identificationModule", {})
    status = protocol.get("statusModule", {})
    design = protocol.get("designModule", {})
    arms = protocol.get("armsInterventionsModule", {})
    description = protocol.get("descriptionModule", {})
    references = protocol.get("referencesModule", {})
    return {
        "nct_id": identification.get("nctId", ""),
        "title": identification.get("briefTitle", ""),
        "overall_status": status.get("overallStatus", ""),
        "phases": design.get("phases", []),
        "allocation": (design.get("designInfo", {}) or {}).get("allocation", ""),
        "masking": (design.get("designInfo", {}) or {}).get("maskingInfo", {}).get("masking", ""),
        "interventions": [item.get("name", "") for item in arms.get("interventions", [])],
        "brief_summary": description.get("briefSummary", ""),
        "pmids": [ref.get("pmid", "") for ref in references.get("references", []) if ref.get("pmid")],
    }


def is_phase_ii_iii_placebo_randomized_trial(study: dict[str, Any]) -> bool:
    fields = nct_fields(study)
    text = " ".join(
        [
            fields["title"],
            fields["brief_summary"],
            " ".join(fields["interventions"]),
            fields["allocation"],
            fields["masking"],
            " ".join(fields["phases"]),
        ]
    ).lower()
    phase_ok = any(phase in {"PHASE2", "PHASE3", "PHASE2_PHASE3"} for phase in fields["phases"])
    return phase_ok and "placebo" in text and "random" in text and text_has_seizure_context(text)


def source_for_detailed_field(row: dict[str, str], field_name: str) -> str:
    if field_name == "mechanism_of_action":
        return row.get("mechanism_source", "")
    if field_name.startswith("fda_black_box_warning"):
        return row.get("fda_black_box_warning_source", "")
    if field_name in {RR50_FIELD, MPC_FIELD, SF_FIELD, PLOT_RR50_FIELD, PLOT_MPC_FIELD, PLOT_SF_FIELD}:
        return row.get("rct_pubmed_verification_notes", "") or row.get("pubmed_phase_ii_iii_rct_links", "")
    return row.get("evidence_sources", "")


def salient_terms(value: str, generic_name: str = "") -> list[str]:
    generic_parts = set(normalize_key(generic_name).split())
    terms: list[str] = []
    for term in re.findall(r"[A-Za-z][A-Za-z0-9+-]{3,}", value or ""):
        key = normalize_key(term)
        if not key or key in SOURCE_FACT_STOPWORDS or key in generic_parts:
            continue
        if key.startswith("cyp") or key.startswith("ugt") or key in {"sv2a", "gaba"}:
            terms.append(key)
            continue
        if len(key) >= 5:
            terms.append(key)
    seen: set[str] = set()
    output: list[str] = []
    for term in terms:
        if term not in seen:
            seen.add(term)
            output.append(term)
    return output[:18]


def numeric_terms(value: str) -> list[str]:
    numbers = []
    for match in re.finditer(r"(?<![A-Za-z])\d+(?:\.\d+)?(?![A-Za-z])", value or ""):
        number = match.group(0).lstrip("0") or "0"
        if number not in numbers:
            numbers.append(number)
    return numbers[:12]


def label_contains_number(label_text: str, number: str) -> bool:
    if "." in number:
        plain = re.escape(number.rstrip("0").rstrip("."))
        return re.search(rf"(?<!\d){plain}(?!\d)", label_text) is not None
    return re.search(rf"(?<!\d){re.escape(number)}(?:\.0+)?(?!\d)", label_text) is not None


def fact_concordance(value: str, source_text: str, generic_name: str, numeric_required: bool = False) -> dict[str, Any]:
    value = normalize_space(value)
    source_key = normalize_key(source_text)
    if not value or value.lower().startswith(("n/a", "nr/", "no pubmed", "needs review")):
        return {"checked": False, "ok": True, "reason": "blank_or_not_applicable"}

    numbers = numeric_terms(value)
    missing_numbers = [number for number in numbers if not label_contains_number(source_text, number)]
    terms = salient_terms(value, generic_name)
    matched_terms = [term for term in terms if re.search(rf"(?<![a-z0-9]){re.escape(term)}(?![a-z0-9])", source_key)]
    missing_terms = [term for term in terms if term not in matched_terms]

    if numbers and not missing_numbers:
        return {"checked": True, "ok": True, "numbers": numbers, "matched_terms": matched_terms}
    if numeric_required and numbers and missing_numbers:
        return {"checked": True, "ok": False, "missing_numbers": missing_numbers, "missing_terms": missing_terms}
    if not terms:
        return {"checked": False, "ok": True, "reason": "no_salient_terms"}
    required_matches = 1 if len(terms) <= 3 else max(2, min(4, len(terms) // 3))
    ok = len(matched_terms) >= required_matches
    return {
        "checked": True,
        "ok": ok,
        "terms": terms,
        "matched_terms": matched_terms,
        "missing_terms": missing_terms,
        "numbers": numbers,
        "missing_numbers": missing_numbers,
    }


def pubmed_label_matches(current_label: str, expected_label: str) -> bool:
    current = normalize_key(current_label)
    expected = normalize_key(expected_label)
    return current == expected or current.startswith(expected)


def plot_contains_outcome(plot_value: str, outcome_row: dict[str, str], diff_field: str) -> bool:
    if not outcome_row.get(diff_field):
        return True
    label = re.escape(outcome_row.get("label", ""))
    value = re.escape(format_number(outcome_row[diff_field]))
    url = re.escape(outcome_row.get("pubmed_url", ""))
    pattern = rf"{label}\|{value}\|{url}(?:\|\d+)?"
    return re.search(pattern, plot_value or "") is not None


class UpdateCheck:
    def __init__(self, args: argparse.Namespace):
        self.args = args
        self.csv_path = Path(args.csv)
        self.fieldnames, all_rows = read_dicts(self.csv_path)
        self.rows = all_rows[: args.max_drugs] if args.max_drugs else all_rows
        self.all_rows = all_rows
        self.client = HttpClient(Path(args.cache_dir), refresh=args.refresh, offline=args.offline, throttle=args.throttle)
        self.findings: list[Finding] = []
        self.source_observations: list[SourceObservation] = []
        self.name_index = self.build_name_index(self.all_rows)

    def build_name_index(self, rows: list[dict[str, str]]) -> dict[str, dict[str, str]]:
        index: dict[str, dict[str, str]] = {}
        for row in rows:
            for term in row_terms(row):
                index[normalize_key(term)] = row
                stripped = strip_form_modifiers(term)
                if stripped:
                    index.setdefault(stripped, row)
        return index

    def known_names(self) -> set[str]:
        names = set(ASM_NAME_HINTS)
        for row in self.all_rows:
            names.add(normalize_key(row.get("generic_name", "")))
            for term in row_terms(row):
                names.add(normalize_key(term))
        return {name for name in names if name}

    def enabled(self, source: str) -> bool:
        selected = set(self.args.sources)
        return "all" in selected or source in selected

    def find_row_for_candidate(self, candidate_name: str) -> dict[str, str] | None:
        for key in [normalize_key(candidate_name), strip_form_modifiers(candidate_name)]:
            if key in self.name_index:
                return self.name_index[key]
        return None

    def run(self) -> None:
        if self.enabled("local"):
            self.check_alias_uniqueness()
            self.check_source_reference_gaps()
            self.check_rct_audit_concordance()
            self.check_rct_link_validation(validate_articles=False)
            self.check_outcome_concordance()
        if self.enabled("epilepsy"):
            self.check_epilepsy_foundation()
        if self.enabled("ilae"):
            self.check_ilae()
        if self.enabled("fda"):
            self.check_openfda_discovery()
            self.check_fda_warnings()
        if self.enabled("pubmed"):
            self.check_pubmed()
            self.check_rct_link_validation(validate_articles=True)
        if self.enabled("nih"):
            self.check_clinicaltrials()

        self.review_source_observations()
        self.findings = self.dedupe_findings(self.findings)
        self.write_reports()
        if self.args.apply:
            self.apply_findings()

    def add_source_error(self, source: str, evidence_url: str, exc: Exception) -> None:
        self.findings.append(source_error_finding(source, evidence_url, str(exc)))

    def selected_names(self) -> set[str]:
        return {row.get("generic_name", "") for row in self.rows}

    def check_alias_uniqueness(self) -> None:
        occurrences: dict[str, list[dict[str, str]]] = defaultdict(list)
        for row in self.all_rows:
            generic = row.get("generic_name", "")
            row_fields = [
                ("generic_name", [generic]),
                ("alternate_generic_names", split_semicolon(row.get("alternate_generic_names", ""))),
                ("trade_names", split_semicolon(row.get("trade_names", ""))),
                ("pubmed_search_aliases", split_semicolon(row.get("pubmed_search_aliases", ""))),
            ]
            for field_name, values in row_fields:
                seen_in_field: set[str] = set()
                for value in values:
                    key = normalize_key(value)
                    if not key:
                        continue
                    occurrences[key].append(
                        {
                            "row": generic,
                            "field": field_name,
                            "value": value,
                            "current_value": row.get(field_name, ""),
                        }
                    )
                    if field_name != "generic_name" and key in seen_in_field:
                        proposed = merge_semicolon("", split_semicolon(row.get(field_name, "")))
                        self.findings.append(
                            make_finding(
                                kind="duplicate_alias_within_row",
                                severity="medium",
                                generic_name=generic,
                                source="Local CSV alias validation",
                                evidence_url=str(self.csv_path),
                                summary=f"Alias '{value}' is repeated in {field_name}.",
                                column=field_name,
                                current_value=row.get(field_name, ""),
                                proposed_value=proposed,
                                safe_to_apply=True,
                                proposed_updates={"__replace_fields__": json.dumps({field_name: proposed})},
                            )
                        )
                    seen_in_field.add(key)

        selected = self.selected_names()
        for key, items in sorted(occurrences.items()):
            rows = sorted({item["row"] for item in items})
            if len(rows) <= 1 or not selected.intersection(rows):
                continue
            generic_owners = [item for item in items if item["field"] == "generic_name"]
            if len(generic_owners) == 1:
                owner = generic_owners[0]["row"]
                for item in items:
                    if item["row"] == owner or item["field"] == "generic_name":
                        continue
                    proposed = remove_semicolon_value(item["current_value"], item["value"])
                    self.findings.append(
                        make_finding(
                            kind="alias_cross_row_conflict",
                            severity="critical",
                            generic_name=item["row"],
                            source="Local CSV alias validation",
                            evidence_url=str(self.csv_path),
                            summary=(
                                f"Alias '{item['value']}' in {item['row']} / {item['field']} also identifies the "
                                f"separate generic row '{owner}'. This may make the same drug appear more than once."
                            ),
                            column=item["field"],
                            current_value=item["current_value"],
                            proposed_value=proposed,
                            safe_to_apply=False,
                            requires_approval=True,
                            proposed_updates={"__replace_fields__": json.dumps({item["field"]: proposed})},
                            details={"alias_key": key, "conflicting_rows": rows, "owner_row": owner},
                        )
                    )
                continue
            self.findings.append(
                make_finding(
                    kind="duplicate_drug_row_conflict",
                    severity="critical",
                    generic_name="; ".join(rows),
                    source="Local CSV alias validation",
                    evidence_url=str(self.csv_path),
                    summary=f"The normalized name/alias '{key}' appears across multiple drug rows: {', '.join(rows)}.",
                    column="generic_name",
                    current_value="; ".join(f"{item['row']}:{item['field']}={item['value']}" for item in items),
                    proposed_value="Manual merge/reassignment required; no automatic row deletion is attempted.",
                    safe_to_apply=False,
                    requires_approval=True,
                    details={"alias_key": key, "occurrences": items},
                )
            )
        print("Local alias validation: completed")

    def check_source_reference_gaps(self) -> None:
        for row in self.rows:
            generic = row.get("generic_name", "")
            evidence_sources = row.get("evidence_sources", "")
            mechanism_source = row.get("mechanism_source", "")
            if mechanism_source and mechanism_source not in evidence_sources:
                self.findings.append(
                    make_finding(
                        kind="source_reference_gap",
                        severity="medium",
                        generic_name=generic,
                        source="Local source validation",
                        evidence_url=str(self.csv_path),
                        summary="mechanism_source is not represented in evidence_sources.",
                        column="evidence_sources",
                        current_value=evidence_sources,
                        proposed_value=mechanism_source,
                        safe_to_apply=True,
                        proposed_updates={"evidence_sources": mechanism_source},
                    )
                )
            for field_name in DETAILED_FACT_FIELDS:
                value = row.get(field_name, "")
                source_text = source_for_detailed_field(row, field_name)
                if is_blankish(value) or source_text:
                    continue
                proposed = f"Needs source verification for {field_name}"
                target_field = "mechanism_source" if field_name == "mechanism_of_action" else "evidence_sources"
                self.findings.append(
                    make_finding(
                        kind="source_reference_missing",
                        severity="high",
                        generic_name=generic,
                        source="Local source validation",
                        evidence_url=str(self.csv_path),
                        summary=f"{field_name} has a value but no source reference was found.",
                        column=target_field,
                        current_value=row.get(target_field, ""),
                        proposed_value=proposed,
                        safe_to_apply=True,
                        proposed_updates={target_field: proposed},
                    )
                )
        print("Local source-reference validation: completed")

    def check_rct_audit_concordance(self) -> None:
        if not RCT_REPORT_PATH.exists():
            self.findings.append(
                make_finding(
                    kind="rct_audit_missing",
                    severity="warning",
                    generic_name="",
                    source="Local RCT audit validation",
                    evidence_url=str(RCT_REPORT_PATH),
                    summary="pubmed_rct_audit.csv is missing; existing RCT link concordance against the local audit could not be checked.",
                )
            )
            return
        _, audit_rows = read_dicts(RCT_REPORT_PATH)
        included = [row for row in audit_rows if row.get("status") == "included"]
        csv_by_name = {row.get("generic_name", ""): row for row in self.rows}
        for audit in included:
            generic = audit.get("generic_name", "")
            row = csv_by_name.get(generic)
            if not row:
                continue
            pmid = audit.get("pmid", "")
            if not pmid or pmid in existing_pmids(row):
                continue
            link_value = f"{audit.get('label') or 'PMID' + pmid}|https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
            self.findings.append(
                make_finding(
                    kind="rct_audit_link_missing_from_csv",
                    severity="high",
                    generic_name=generic,
                    source="Local PubMed RCT audit",
                    evidence_url=audit.get("url", f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"),
                    summary="An included RCT in pubmed_rct_audit.csv is not listed in pubmed_phase_ii_iii_rct_links.",
                    column="pubmed_phase_ii_iii_rct_links",
                    current_value=row.get("pubmed_phase_ii_iii_rct_links", ""),
                    proposed_value=link_value,
                    safe_to_apply=True,
                    proposed_updates={
                        "pubmed_phase_ii_iii_rct_links": link_value,
                        "rct_pubmed_verification_notes": f"update_check on {TODAY}: restored included local RCT audit PMID {pmid}.",
                    },
                )
            )
        print("Local RCT audit concordance: completed")

    def check_rct_link_validation(self, validate_articles: bool) -> None:
        all_links: list[tuple[dict[str, str], dict[str, str]]] = []
        for row in self.rows:
            links = extract_pubmed_links(row.get("pubmed_phase_ii_iii_rct_links", ""))
            canonical = canonical_pubmed_links(row.get("pubmed_phase_ii_iii_rct_links", ""))
            if canonical and canonical != row.get("pubmed_phase_ii_iii_rct_links", ""):
                self.findings.append(
                    make_finding(
                        kind="rct_link_format_correction",
                        severity="medium",
                        generic_name=row.get("generic_name", ""),
                        source="Local PubMed link validation",
                        evidence_url=str(self.csv_path),
                        summary="One or more PubMed RCT links are not in canonical Label|https://pubmed.ncbi.nlm.nih.gov/PMID/ format.",
                        column="pubmed_phase_ii_iii_rct_links",
                        current_value=row.get("pubmed_phase_ii_iii_rct_links", ""),
                        proposed_value=canonical,
                        safe_to_apply=False,
                        requires_approval=True,
                        proposed_updates={"__replace_fields__": json.dumps({"pubmed_phase_ii_iii_rct_links": canonical})},
                    )
                )
            for link in links:
                if not link["pmid"]:
                    self.findings.append(
                        make_finding(
                            kind="rct_link_malformed",
                            severity="high",
                            generic_name=row.get("generic_name", ""),
                            source="Local PubMed link validation",
                            evidence_url=str(self.csv_path),
                            summary=f"RCT entry does not contain a parseable PubMed URL: {link['entry']}",
                            column="pubmed_phase_ii_iii_rct_links",
                            current_value=row.get("pubmed_phase_ii_iii_rct_links", ""),
                            proposed_value="Replace malformed entry with Label|https://pubmed.ncbi.nlm.nih.gov/PMID/ after manual review.",
                            safe_to_apply=False,
                            requires_approval=True,
                        )
                    )
                    continue
                all_links.append((row, link))

        if not validate_articles or not all_links:
            print("Local RCT link-format validation: completed")
            return

        pmids = sorted({link["pmid"] for _, link in all_links}, key=int)
        try:
            articles = pubmed_efetch(self.client, pmids)
        except SourceError as exc:
            self.add_source_error("PubMed", SOURCE_URLS["PubMed E-utilities"], exc)
            return
        for row, link in all_links:
            article = articles.get(link["pmid"])
            if not article:
                continue
            ok, reason = is_pubmed_qualifying(article, row, set())
            if not ok:
                note = (
                    f"update_check on {TODAY}: PMID {link['pmid']} needs manual review for "
                    f"{row.get('generic_name', '')}; PubMed validation reason: {reason}."
                )
                self.findings.append(
                    make_finding(
                        kind="rct_pubmed_concordance_problem",
                        severity="high",
                        generic_name=row.get("generic_name", ""),
                        source="PubMed",
                        evidence_url=f"https://pubmed.ncbi.nlm.nih.gov/{link['pmid']}/",
                        summary=(
                            "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III "
                            f"placebo-controlled randomized epilepsy criteria: {reason}."
                        ),
                        column="pubmed_phase_ii_iii_rct_links",
                        current_value=link["entry"],
                        proposed_value=note,
                        safe_to_apply=False,
                        requires_approval=True,
                        proposed_updates={"__append_fields__": json.dumps({"rct_pubmed_verification_notes": note})},
                        details={"article": article, "reason": reason},
                    )
                )
            expected_label = make_pubmed_label(article)
            if link["label"] and not pubmed_label_matches(link["label"], expected_label):
                current_field = row.get("pubmed_phase_ii_iii_rct_links", "")
                proposed_entry = f"{expected_label}|https://pubmed.ncbi.nlm.nih.gov/{link['pmid']}/"
                proposed_field = current_field.replace(link["entry"], proposed_entry)
                self.findings.append(
                    make_finding(
                        kind="rct_pubmed_label_mismatch",
                        severity="medium",
                        generic_name=row.get("generic_name", ""),
                        source="PubMed",
                        evidence_url=f"https://pubmed.ncbi.nlm.nih.gov/{link['pmid']}/",
                        summary=f"RCT link label '{link['label']}' does not match PubMed first-author/year label '{expected_label}'.",
                        column="pubmed_phase_ii_iii_rct_links",
                        current_value=current_field,
                        proposed_value=proposed_field,
                        safe_to_apply=False,
                        requires_approval=True,
                        proposed_updates={"__replace_fields__": json.dumps({"pubmed_phase_ii_iii_rct_links": proposed_field})},
                    )
                )
        print("PubMed RCT link/article validation: completed")

    def check_outcome_concordance(self) -> None:
        if not OUTCOME_REPORT_PATH.exists():
            self.findings.append(
                make_finding(
                    kind="outcome_audit_missing",
                    severity="warning",
                    generic_name="",
                    source="Local outcome validation",
                    evidence_url=str(OUTCOME_REPORT_PATH),
                    summary="efficacy_outcome_audit.csv is missing; RCT outcome concordance could not be checked.",
                )
            )
            return
        _, outcome_rows = read_dicts(OUTCOME_REPORT_PATH)
        selected = self.selected_names()
        by_drug: dict[str, list[dict[str, str]]] = defaultdict(list)
        for outcome in outcome_rows:
            generic = outcome.get("generic_name", "")
            if generic in selected:
                by_drug[generic].append(outcome)
                self.check_outcome_row_math(outcome)

        for row in self.rows:
            generic = row.get("generic_name", "")
            rows = by_drug.get(generic, [])
            linked_pmids = existing_pmids(row)
            for outcome in rows:
                pmid = outcome.get("pmid", "")
                if pmid and pmid not in linked_pmids:
                    link_value = f"{outcome.get('label') or 'PMID' + pmid}|https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                    self.findings.append(
                        make_finding(
                            kind="outcome_rct_link_missing_from_csv",
                            severity="high",
                            generic_name=generic,
                            source="Local outcome validation",
                            evidence_url=outcome.get("pubmed_url", f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/"),
                            summary="An outcome-audit RCT PMID is not listed in pubmed_phase_ii_iii_rct_links.",
                            column="pubmed_phase_ii_iii_rct_links",
                            current_value=row.get("pubmed_phase_ii_iii_rct_links", ""),
                            proposed_value=link_value,
                            safe_to_apply=True,
                            proposed_updates={"pubmed_phase_ii_iii_rct_links": link_value},
                        )
                    )
            for summary_field, plot_field, diff_field, include_field, noun in OUTCOME_SPECS:
                expected = outcome_summary(rows, diff_field, include_field, noun)
                if expected and normalize_for_compare(row.get(summary_field, "")) != normalize_for_compare(expected):
                    self.findings.append(
                        make_finding(
                            kind="rct_outcome_summary_mismatch",
                            severity="critical",
                            generic_name=generic,
                            source="Local outcome validation",
                            evidence_url=str(OUTCOME_REPORT_PATH),
                            summary=f"{summary_field} does not match efficacy_outcome_audit.csv included rows.",
                            column=summary_field,
                            current_value=row.get(summary_field, ""),
                            proposed_value=expected,
                            safe_to_apply=False,
                            requires_approval=True,
                            proposed_updates={"__replace_fields__": json.dumps({summary_field: expected})},
                        )
                    )
                for outcome in rows:
                    if outcome.get(include_field) != "yes" or not outcome.get(diff_field):
                        continue
                    if plot_contains_outcome(row.get(plot_field, ""), outcome, diff_field):
                        continue
                    plot_entry = f"{outcome['label']}|{format_number(outcome[diff_field])}|{outcome['pubmed_url']}"
                    self.findings.append(
                        make_finding(
                            kind="rct_outcome_plot_entry_missing",
                            severity="high",
                            generic_name=generic,
                            source="Local outcome validation",
                            evidence_url=outcome.get("pubmed_url", str(OUTCOME_REPORT_PATH)),
                            summary=f"{plot_field} is missing the included outcome value for {outcome.get('label')}.",
                            column=plot_field,
                            current_value=row.get(plot_field, ""),
                            proposed_value=plot_entry,
                            safe_to_apply=True,
                            proposed_updates={plot_field: plot_entry},
                        )
                    )
        print("Local RCT outcome concordance: completed")

    def check_outcome_row_math(self, outcome: dict[str, str]) -> None:
        specs = [
            ("rr50_active_percent", "rr50_placebo_percent", "rr50_differential_percent"),
            ("mpc_active_percent", "mpc_placebo_percent", "mpc_differential_percent"),
            ("sf_active_percent", "sf_placebo_percent", "sf_differential_percent"),
        ]
        for active_field, placebo_field, diff_field in specs:
            active = parse_float(outcome.get(active_field))
            placebo = parse_float(outcome.get(placebo_field))
            diff = parse_float(outcome.get(diff_field))
            if active is None or placebo is None or diff is None:
                continue
            expected = round(active - placebo, 2)
            if abs(expected - diff) <= 0.05:
                continue
            self.findings.append(
                make_finding(
                    kind="outcome_audit_math_error",
                    severity="critical",
                    generic_name=outcome.get("generic_name", ""),
                    source="Local outcome validation",
                    evidence_url=outcome.get("pubmed_url", str(OUTCOME_REPORT_PATH)),
                    summary=(
                        f"{diff_field} should equal {active_field} - {placebo_field}; "
                        f"expected {format_number(expected)} but audit row has {outcome.get(diff_field)}."
                    ),
                    column=diff_field,
                    current_value=outcome.get(diff_field, ""),
                    proposed_value=format_number(expected),
                    safe_to_apply=False,
                    requires_approval=True,
                    details={"outcome_row": outcome},
                )
            )

    def check_epilepsy_foundation(self) -> None:
        url = SOURCE_URLS["Epilepsy Foundation"]
        try:
            page = Path(self.args.epilepsy_html).read_text(encoding="utf-8") if self.args.epilepsy_html else self.client.get_text(url)
            observations = parse_epilepsy_foundation(page, self.known_names())
            self.source_observations.extend(observations)
            print(f"Epilepsy Foundation: collected {len(observations)} medication observation(s)")
        except SourceError as exc:
            self.add_source_error("Epilepsy Foundation", url, exc)
        except OSError as exc:
            self.add_source_error("Epilepsy Foundation", url, exc)

    def check_ilae(self) -> None:
        pages: dict[str, str] = {}
        snapshot_by_label = {
            "ILAE medical therapies": self.args.ilae_medical_html,
            "ILAE antiepileptic drugs": self.args.ilae_drugs_html,
        }
        for label in ["ILAE medical therapies", "ILAE antiepileptic drugs"]:
            try:
                snapshot = snapshot_by_label[label]
                pages[label] = Path(snapshot).read_text(encoding="utf-8") if snapshot else self.client.get_text(SOURCE_URLS[label])
            except SourceError as exc:
                self.add_source_error("ILAE", SOURCE_URLS[label], exc)
            except OSError as exc:
                self.add_source_error("ILAE", SOURCE_URLS[label], exc)
        observations = parse_ilae_pages(pages, self.known_names())
        self.source_observations.extend(observations)
        print(f"ILAE: collected {len(observations)} medication observation(s)")

    def check_openfda_discovery(self) -> None:
        since_ymd = self.args.since.replace("-", "") if self.args.since else None
        try:
            observations = collect_openfda_candidates(self.client, since_ymd=since_ymd, limit=self.args.openfda_limit)
            self.source_observations.extend(observations)
            print(f"FDA/openFDA: collected {len(observations)} seizure-label observation(s)")
        except SourceError as exc:
            self.add_source_error("FDA/openFDA", SOURCE_URLS["openFDA labels"], exc)

    def check_fda_warnings(self) -> None:
        for index, row in enumerate(self.rows, start=1):
            generic = row.get("generic_name", "")
            try:
                label = select_dailymed_label(self.client, row)
            except SourceError as exc:
                self.add_source_error("FDA/DailyMed", SOURCE_URLS["DailyMed"], exc)
                continue
            self.review_fda_warning(row, label)
            self.review_dailymed_fact_concordance(row, label)
            print(f"FDA warnings {index:02d}/{len(self.rows)} {generic}: {label['status']}")

    def review_fda_warning(self, row: dict[str, str], label: dict[str, Any]) -> None:
        generic = row.get("generic_name", "")
        proposed_warning = label.get("warning", "")
        current_warning = row.get("fda_black_box_warning", "")
        proposed_source = label.get("source", "")
        evidence_url = label.get("evidence_url", "") or SOURCE_URLS["DailyMed"]
        updates = {
            "fda_black_box_warning": proposed_warning,
            "fda_black_box_warning_source": proposed_source,
            "fda_black_box_warning_verified": TODAY,
            "data_most_recently_refreshed": TODAY,
            "evidence_sources": "FDA/DailyMed labeling",
        }
        if normalize_for_compare(current_warning) == normalize_for_compare(proposed_warning):
            # Metadata refresh only; the warning text itself did not change.
            metadata_updates = {
                "fda_black_box_warning_source": proposed_source,
                "fda_black_box_warning_verified": TODAY,
                "data_most_recently_refreshed": TODAY,
                "evidence_sources": "FDA/DailyMed labeling",
            }
            if row.get("fda_black_box_warning_source", "") != proposed_source or row.get("fda_black_box_warning_verified", "") != TODAY:
                self.findings.append(
                    make_finding(
                        kind="fda_warning_metadata_refresh",
                        severity="info",
                        generic_name=generic,
                        source="FDA/DailyMed",
                        evidence_url=evidence_url,
                        summary="FDA boxed-warning text matches current CSV; source metadata can be refreshed.",
                        column="fda_black_box_warning_source",
                        current_value=row.get("fda_black_box_warning_source", ""),
                        proposed_value=proposed_source,
                        safe_to_apply=True,
                        proposed_updates=metadata_updates,
                    )
                )
            return

        if is_blankish(current_warning):
            self.findings.append(
                make_finding(
                    kind="fda_warning_added",
                    severity="high",
                    generic_name=generic,
                    source="FDA/DailyMed",
                    evidence_url=evidence_url,
                    summary="FDA boxed-warning field is empty or unreviewed; current DailyMed warning can be added.",
                    column="fda_black_box_warning",
                    current_value=current_warning,
                    proposed_value=proposed_warning,
                    safe_to_apply=True,
                    proposed_updates=updates,
                    details={"status": label.get("status", ""), "candidate": label.get("candidate", {})},
                )
            )
            return

        self.findings.append(
            make_finding(
                kind="fda_warning_contradiction",
                severity="critical",
                generic_name=generic,
                source="FDA/DailyMed",
                evidence_url=evidence_url,
                summary=(
                    "Current FDA/DailyMed boxed-warning extraction differs from the CSV. "
                    "This is a direct contradiction and will not be applied without approval."
                ),
                column="fda_black_box_warning",
                current_value=current_warning,
                proposed_value=proposed_warning,
                safe_to_apply=False,
                requires_approval=True,
                proposed_updates=updates,
                details={"status": label.get("status", ""), "candidate": label.get("candidate", {})},
            )
        )

    def review_dailymed_fact_concordance(self, row: dict[str, str], label: dict[str, Any]) -> None:
        label_text = label.get("label_text", "")
        if not label_text:
            return
        evidence_url = label.get("evidence_url", "") or SOURCE_URLS["DailyMed"]
        generic = row.get("generic_name", "")
        for field_name in DETAILED_FACT_FIELDS:
            value = row.get(field_name, "")
            if is_blankish(value):
                continue
            source_text = source_for_detailed_field(row, field_name)
            if "FDA/DailyMed" not in source_text and "FDA label" not in source_text:
                continue
            numeric_required = field_name in {
                "half_life_range",
                "typical_doses_per_day",
                "minimum_effective_dose",
                "maximum_approved_daily_dose",
                "year_fda_cleared",
                "adverse_symptoms_percentages",
            }
            result = fact_concordance(value, label_text, generic, numeric_required=numeric_required)
            if not result.get("checked") or result.get("ok"):
                continue
            note = (
                f"update_check on {TODAY}: {field_name} was not concordant with the selected DailyMed label "
                f"({evidence_url}); review current text before relying on it."
            )
            self.findings.append(
                make_finding(
                    kind="source_fact_concordance_problem",
                    severity="high" if numeric_required else "medium",
                    generic_name=generic,
                    source="FDA/DailyMed",
                    evidence_url=evidence_url,
                    summary=f"{field_name} could not be verified against the selected FDA/DailyMed label.",
                    column=field_name,
                    current_value=value,
                    proposed_value=note,
                    safe_to_apply=False,
                    requires_approval=True,
                    proposed_updates={"__append_fields__": json.dumps({"status_or_notes": note})},
                    details=result,
                )
            )

    def check_pubmed(self) -> None:
        for index, row in enumerate(self.rows, start=1):
            generic = row.get("generic_name", "")
            try:
                pmids = pubmed_esearch(self.client, row, self.args.since, self.args.pubmed_retmax)
                articles = pubmed_efetch(self.client, pmids)
            except SourceError as exc:
                self.add_source_error("PubMed", SOURCE_URLS["PubMed E-utilities"], exc)
                continue
            existing = existing_pmids(row)
            new_count = 0
            for pmid in pmids:
                article = articles.get(pmid)
                if not article:
                    continue
                ok, reason = is_pubmed_qualifying(article, row, existing)
                if not ok or pmid in existing:
                    continue
                label = make_pubmed_label(article)
                link_value = f"{label}|https://pubmed.ncbi.nlm.nih.gov/{pmid}/"
                self.findings.append(
                    make_finding(
                        kind="new_pubmed_phase_ii_iii_rct",
                        severity="high",
                        generic_name=generic,
                        source="PubMed",
                        evidence_url=f"https://pubmed.ncbi.nlm.nih.gov/{pmid}/",
                        summary=f"New qualifying placebo-controlled randomized phase II/III ASM trial report: {article['title']}",
                        column="pubmed_phase_ii_iii_rct_links",
                        current_value=row.get("pubmed_phase_ii_iii_rct_links", ""),
                        proposed_value=link_value,
                        safe_to_apply=True,
                        proposed_updates={
                            "pubmed_phase_ii_iii_rct_links": link_value,
                            "rct_pubmed_verification_notes": (
                                f"update_check on {TODAY}: added PMID {pmid} after PubMed qualification "
                                f"as {reason}."
                            ),
                            "data_most_recently_refreshed": TODAY,
                        },
                        details={"article": article, "reason": reason},
                    )
                )
                new_count += 1
            print(f"PubMed {index:02d}/{len(self.rows)} {generic}: {new_count} new qualifying PMID(s)")

    def check_clinicaltrials(self) -> None:
        for index, row in enumerate(self.rows, start=1):
            generic = row.get("generic_name", "")
            url = clinicaltrials_url(row, self.args.clinicaltrials_page_size)
            try:
                data = self.client.get_json(url)
            except SourceError as exc:
                self.add_source_error("NIH ClinicalTrials.gov", SOURCE_URLS["NIH ClinicalTrials.gov"], exc)
                continue
            existing = existing_pmids(row)
            hits = 0
            for study in data.get("studies", []):
                if not is_phase_ii_iii_placebo_randomized_trial(study):
                    continue
                fields = nct_fields(study)
                nct_id = fields["nct_id"]
                evidence_url = f"https://clinicaltrials.gov/study/{nct_id}" if nct_id else SOURCE_URLS["NIH ClinicalTrials.gov"]
                pmids = [pmid for pmid in fields["pmids"] if pmid not in existing]
                self.findings.append(
                    make_finding(
                        kind="nih_clinicaltrial_phase_ii_iii_rct",
                        severity="medium",
                        generic_name=generic,
                        source="NIH ClinicalTrials.gov",
                        evidence_url=evidence_url,
                        summary=(
                            "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: "
                            f"{fields['title']}"
                        ),
                        safe_to_apply=False,
                        details={**fields, "new_reference_pmids": pmids},
                    )
                )
                hits += 1
            print(f"NIH ClinicalTrials.gov {index:02d}/{len(self.rows)} {generic}: {hits} matching trial(s)")

    def review_source_observations(self) -> None:
        grouped: dict[str, list[SourceObservation]] = defaultdict(list)
        for observation in self.source_observations:
            key = strip_form_modifiers(observation.candidate_name) or normalize_key(observation.candidate_name)
            if key:
                grouped[key].append(observation)

        for key, observations in sorted(grouped.items()):
            row = self.find_row_for_candidate(key)
            if row:
                self.review_known_medication_observations(row, observations)
                continue
            self.review_missing_medication(key, observations)

    def review_known_medication_observations(self, row: dict[str, str], observations: list[SourceObservation]) -> None:
        additions = sorted({trade for obs in observations for trade in obs.trade_names if trade})
        if not additions:
            return
        current = row.get("trade_names", "")
        missing = [trade for trade in additions if normalize_key(trade) not in {normalize_key(x) for x in split_semicolon(current)}]
        if not missing:
            return
        self.findings.append(
            make_finding(
                kind="trade_name_addition",
                severity="medium",
                generic_name=row.get("generic_name", ""),
                source="; ".join(sorted({obs.source for obs in observations})),
                evidence_url=observations[0].evidence_url,
                summary=f"Source labels mention trade name(s) not present in CSV: {', '.join(missing)}.",
                column="trade_names",
                current_value=current,
                proposed_value="; ".join(missing),
                safe_to_apply=True,
                proposed_updates={
                    "trade_names": "; ".join(missing),
                    "evidence_sources": "; ".join(sorted({obs.source for obs in observations})),
                    "data_most_recently_refreshed": TODAY,
                },
            )
        )

    def review_missing_medication(self, key: str, observations: list[SourceObservation]) -> None:
        evidence_sources = sorted({obs.source for obs in observations})
        source_summary = "; ".join(obs.summary for obs in observations[:3])
        candidate_name = display_name(key)
        dailymed_label: dict[str, Any] | None = None
        if self.enabled("fda") and not self.args.no_confirm_missing_with_dailymed:
            try:
                probe_row = {"generic_name": candidate_name, "alternate_generic_names": "", "trade_names": ""}
                dailymed_label = select_dailymed_label(self.client, probe_row)
            except SourceError:
                dailymed_label = None

        fda_confirmed = False
        if dailymed_label:
            indications = dailymed_label.get("indications", "")
            fda_confirmed = dailymed_label.get("status") != "no_current_fda_label" and text_has_seizure_context(indications)
        source_has_fda = any(obs.source.startswith("FDA") for obs in observations)
        safe = source_has_fda or fda_confirmed
        severity = "high" if safe else "medium"
        kind = "new_or_missing_approved_asm" if safe else "source_list_missing_medication"
        proposed_row = self.build_new_medication_row(candidate_name, observations, dailymed_label if fda_confirmed else None)
        self.findings.append(
            make_finding(
                kind=kind,
                severity=severity,
                generic_name=candidate_name,
                source="; ".join(evidence_sources),
                evidence_url=observations[0].evidence_url,
                summary=(
                    f"Medication candidate '{candidate_name}' was found in external source(s) but not in ASM-list.csv. "
                    + ("FDA/DailyMed confirmation supports adding a skeletal row." if safe else "No FDA/DailyMed seizure indication confirmation was found; manual review recommended.")
                    + f" Evidence: {source_summary}"
                ),
                column="generic_name",
                current_value="",
                proposed_value=candidate_name,
                safe_to_apply=safe,
                proposed_updates={"__new_row__": json.dumps(proposed_row, sort_keys=True)},
                details={
                    "observations": [asdict(obs) for obs in observations],
                    "fda_confirmed": fda_confirmed,
                    "dailymed_label": dailymed_label or {},
                    "proposed_row": proposed_row,
                },
            )
        )

    def build_new_medication_row(
        self,
        candidate_name: str,
        observations: list[SourceObservation],
        dailymed_label: dict[str, Any] | None,
    ) -> dict[str, str]:
        row = {field: "" for field in self.fieldnames}
        source_names = sorted({obs.source for obs in observations})
        trade_names = sorted({trade for obs in observations for trade in obs.trade_names if normalize_key(trade) != normalize_key(candidate_name)})
        row["generic_name"] = candidate_name
        if "trade_names" in row:
            row["trade_names"] = "; ".join(trade_names)
        if "status_or_notes" in row:
            row["status_or_notes"] = (
                "Potential ASM added by scripts/update_check.py from external source discovery; "
                "manually curate indication, dosing, mechanism, safety, and outcome columns before clinical use."
            )
        if "evidence_sources" in row:
            additions = source_names + (["FDA/DailyMed labeling"] if dailymed_label else [])
            row["evidence_sources"] = "; ".join(dict.fromkeys(additions))
        if "available_in_us" in row:
            row["available_in_us"] = "Yes" if dailymed_label else "Needs review"
        if "pubmed_phase_ii_iii_rct_links" in row:
            row["pubmed_phase_ii_iii_rct_links"] = "Needs review"
        if "rct_pubmed_verification_notes" in row:
            row["rct_pubmed_verification_notes"] = "Needs PubMed RCT audit after source-list discovery."
        if "data_most_recently_refreshed" in row:
            row["data_most_recently_refreshed"] = TODAY
        if dailymed_label:
            if "fda_black_box_warning" in row:
                row["fda_black_box_warning"] = dailymed_label.get("warning", "")
            if "fda_black_box_warning_source" in row:
                row["fda_black_box_warning_source"] = dailymed_label.get("source", "")
            if "fda_black_box_warning_verified" in row:
                row["fda_black_box_warning_verified"] = TODAY
            if "filter_availability" in row:
                row["filter_availability"] = "Available in US"
        for field, default in FILTER_DEFAULTS.items():
            if field in row and not row[field]:
                row[field] = default
        return row

    def dedupe_findings(self, findings: list[Finding]) -> list[Finding]:
        output: list[Finding] = []
        seen: set[str] = set()
        for finding in findings:
            if finding.id in seen:
                continue
            seen.add(finding.id)
            output.append(finding)
        severity_order = {"critical": 0, "high": 1, "medium": 2, "warning": 3, "info": 4}
        output.sort(key=lambda item: (severity_order.get(item.severity, 9), item.generic_name, item.kind))
        return output

    def report_paths(self) -> dict[str, Path]:
        report_dir = Path(self.args.report_dir)
        return {
            "dir": report_dir,
            "json": report_dir / "update_check_findings.json",
            "csv": report_dir / "update_check_findings.csv",
            "md": report_dir / "update_check_summary.md",
            "approvals": report_dir / "update_check_approval_template.json",
        }

    def write_reports(self) -> None:
        paths = self.report_paths()
        paths["dir"].mkdir(parents=True, exist_ok=True)
        payload = [asdict(finding) for finding in self.findings]
        paths["json"].write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        csv_fields = [
            "id",
            "severity",
            "kind",
            "generic_name",
            "source",
            "column",
            "safe_to_apply",
            "requires_approval",
            "summary",
            "evidence_url",
            "current_value",
            "proposed_value",
        ]
        with paths["csv"].open("w", newline="", encoding="utf-8") as handle:
            writer = csv.DictWriter(handle, fieldnames=csv_fields, extrasaction="ignore")
            writer.writeheader()
            for finding in self.findings:
                writer.writerow(asdict(finding))

        counts = defaultdict(int)
        for finding in self.findings:
            counts[finding.severity] += 1
        lines = [
            "# ASM update_check summary",
            "",
            f"Generated: {ISO_TODAY}",
            f"CSV: {self.csv_path}",
            "",
            "## Counts",
            "",
        ]
        for severity in ["critical", "high", "medium", "warning", "info"]:
            lines.append(f"- {severity}: {counts[severity]}")
        lines.extend(["", "## Findings", ""])
        for finding in self.findings:
            lines.append(f"### {finding.severity.upper()} {finding.id}")
            lines.append(f"- Kind: {finding.kind}")
            if finding.generic_name:
                lines.append(f"- Medication: {finding.generic_name}")
            lines.append(f"- Source: {finding.source}")
            if finding.column:
                lines.append(f"- Column: {finding.column}")
            lines.append(f"- Apply: safe={finding.safe_to_apply}; approval_required={finding.requires_approval}")
            lines.append(f"- Evidence: {finding.evidence_url}")
            lines.append(f"- Summary: {finding.summary}")
            lines.append("")
        paths["md"].write_text("\n".join(lines), encoding="utf-8")

        contradictions = [finding for finding in self.findings if finding.requires_approval]
        if contradictions:
            approvals = {
                "instructions": (
                    "Move finding ids from approval_candidates into approved_findings, then rerun "
                    "scripts/update_check.py with --apply --approve-contradictions this_file.json."
                ),
                "approved_findings": [],
                "approval_candidates": [
                    {
                        "id": finding.id,
                        "generic_name": finding.generic_name,
                        "kind": finding.kind,
                        "column": finding.column,
                        "summary": finding.summary,
                        "evidence_url": finding.evidence_url,
                    }
                    for finding in contradictions
                ],
            }
            paths["approvals"].write_text(json.dumps(approvals, indent=2, sort_keys=True) + "\n", encoding="utf-8")

        print(f"Wrote reports to {paths['dir']}")

    def load_approved_ids(self) -> set[str]:
        approved: set[str] = set()
        if self.args.approve_contradictions:
            path = Path(self.args.approve_contradictions)
            data = json.loads(path.read_text(encoding="utf-8"))
            approved.update(data.get("approved_findings", []))
        if self.args.interactive_approvals and sys.stdin.isatty():
            for finding in self.findings:
                if not finding.requires_approval:
                    continue
                print()
                print(f"Contradiction {finding.id} for {finding.generic_name} / {finding.column}")
                print(f"Current: {finding.current_value[:500]}")
                print(f"Proposed: {finding.proposed_value[:500]}")
                answer = input("Apply this contradictory change? Type 'yes' to approve: ").strip().lower()
                if answer == "yes":
                    approved.add(finding.id)
        return approved

    def apply_findings(self) -> None:
        approved_ids = self.load_approved_ids()
        row_by_name = {normalize_key(row.get("generic_name", "")): row for row in self.all_rows}
        applied = 0
        skipped_contradictions = 0
        for finding in self.findings:
            approved = finding.id in approved_ids
            if finding.requires_approval and not approved:
                skipped_contradictions += 1
                continue
            if not finding.safe_to_apply and not approved:
                continue

            if "__new_row__" in finding.proposed_updates:
                proposed_row = json.loads(finding.proposed_updates["__new_row__"])
                key = normalize_key(proposed_row.get("generic_name", ""))
                if key and key not in row_by_name:
                    self.all_rows.append(proposed_row)
                    row_by_name[key] = proposed_row
                    applied += 1
                continue

            key = normalize_key(finding.generic_name)
            row = row_by_name.get(key)
            if not row:
                continue
            changed = False
            if "__replace_fields__" in finding.proposed_updates:
                replacements = json.loads(finding.proposed_updates["__replace_fields__"])
                for field, proposed in replacements.items():
                    if field in self.fieldnames and row.get(field, "") != proposed:
                        row[field] = proposed
                        changed = True
            if "__append_fields__" in finding.proposed_updates:
                appends = json.loads(finding.proposed_updates["__append_fields__"])
                for field, proposed in appends.items():
                    if field in self.fieldnames:
                        merged_note = append_note(row.get(field, ""), proposed)
                        if merged_note != row.get(field, ""):
                            row[field] = merged_note
                            changed = True
            for field, proposed in finding.proposed_updates.items():
                if field not in self.fieldnames or field.startswith("__"):
                    continue
                current = row.get(field, "")
                if field == "rct_pubmed_verification_notes":
                    merged_note = append_note(current, proposed)
                    if merged_note != current:
                        row[field] = merged_note
                        changed = True
                    continue
                if field in SEMICOLON_FIELDS:
                    merged = merge_semicolon(current, split_semicolon(proposed) or [proposed])
                    if merged != current:
                        row[field] = merged
                        changed = True
                    continue
                if normalize_for_compare(current) == normalize_for_compare(proposed):
                    continue
                if is_blankish(current) or approved or field in {"fda_black_box_warning_source", "fda_black_box_warning_verified", "data_most_recently_refreshed"}:
                    row[field] = proposed
                    changed = True
            if changed:
                applied += 1

        if skipped_contradictions:
            print(
                f"{skipped_contradictions} contradictory finding(s) were not applied. "
                f"Review {self.report_paths()['approvals']} and rerun with --approve-contradictions."
            )
        if applied:
            write_dicts(self.csv_path, self.fieldnames, self.all_rows)
        print(f"Applied {applied} finding(s) to {self.csv_path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Comprehensively check ASM-list.csv against FDA/DailyMed/openFDA, Epilepsy Foundation, "
            "ILAE, NIH ClinicalTrials.gov, and PubMed. Default is report-only; pass --apply to edit CSV."
        )
    )
    parser.add_argument("--csv", default=str(CSV_PATH), help="CSV file to review/update.")
    parser.add_argument("--cache-dir", default=str(DEFAULT_CACHE_DIR), help="HTTP cache directory.")
    parser.add_argument("--report-dir", default=str(DEFAULT_REPORT_DIR), help="Directory for JSON/CSV/Markdown reports.")
    parser.add_argument(
        "--sources",
        nargs="+",
        default=["all"],
        choices=["all", "local", "fda", "epilepsy", "nih", "ilae", "pubmed"],
        help="Sources to check. Default: all.",
    )
    parser.add_argument("--apply", action="store_true", help="Apply safe additive updates to the CSV.")
    parser.add_argument(
        "--approve-contradictions",
        help="JSON file with approved_findings ids for contradictory updates.",
    )
    parser.add_argument(
        "--interactive-approvals",
        action="store_true",
        help="Prompt in the terminal before applying contradictory updates.",
    )
    parser.add_argument("--refresh", action="store_true", help="Refresh cached HTTP responses.")
    parser.add_argument("--offline", action="store_true", help="Use cached HTTP responses only.")
    parser.add_argument(
        "--since",
        help=(
            "Optional YYYY-MM-DD lower bound for PubMed publication dates and openFDA effective_time. "
            "Omit for a full comparison against existing CSV contents."
        ),
    )
    parser.add_argument("--max-drugs", type=int, help="Limit number of CSV rows checked; intended for smoke tests.")
    parser.add_argument("--pubmed-retmax", type=int, default=500, help="Maximum PubMed ids per medication.")
    parser.add_argument("--openfda-limit", type=int, default=100, help="Maximum openFDA label results per query term.")
    parser.add_argument("--clinicaltrials-page-size", type=int, default=100, help="Maximum ClinicalTrials.gov studies per medication.")
    parser.add_argument(
        "--epilepsy-html",
        help="Optional saved HTML snapshot of the Epilepsy Foundation seizure medication list, useful if command-line access is blocked.",
    )
    parser.add_argument("--ilae-medical-html", help="Optional saved HTML snapshot of the ILAE medical therapies page.")
    parser.add_argument("--ilae-drugs-html", help="Optional saved HTML snapshot of the ILAE antiepileptic drugs page.")
    parser.add_argument(
        "--no-confirm-missing-with-dailymed",
        action="store_true",
        help="Do not use DailyMed to confirm source-list-only missing medication candidates.",
    )
    parser.add_argument("--throttle", type=float, default=0.05, help="Seconds to sleep after uncached HTTP requests.")
    args = parser.parse_args()
    if args.since and not re.fullmatch(r"\d{4}-\d{2}-\d{2}", args.since):
        parser.error("--since must be YYYY-MM-DD")
    return args


def main() -> None:
    args = parse_args()
    checker = UpdateCheck(args)
    checker.run()


if __name__ == "__main__":
    main()
