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
RCT_AUDIT_PATH = ROOT / "pubmed_cache" / "reports" / "pubmed_rct_audit.csv"
EFFICACY_AUDIT_PATH = ROOT / "pubmed_cache" / "reports" / "efficacy_outcome_audit.csv"
SEIZURE_FREEDOM_AUDIT_PATH = ROOT / "pubmed_cache" / "reports" / "seizure_freedom_audit.csv"

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

PRIMARY_RCT_CORRECTIONS = {
    "diazepam": {
        "link": "AbouKhalil2013|https://pubmed.ncbi.nlm.nih.gov/24111974/",
        "sources": (
            "https://pubmed.ncbi.nlm.nih.gov/24111974/; "
            "https://clinicaltrials.gov/study/NCT00319501"
        ),
        "note": (
            "Phase III RCT audit 2026-07-12 added AbouKhalil2013 (PMID 24111974; "
            "NCT00319501), a randomized double-blind placebo-controlled diazepam "
            "auto-injector trial for acute repetitive seizures. Its time-to-next-seizure "
            "endpoint is not RR50, MPC, or a standard seizure-freedom patient rate."
        ),
    },
    "lorazepam": {
        "link": "Alldredge2001|https://pubmed.ncbi.nlm.nih.gov/11547716/",
        "sources": (
            "https://pubmed.ncbi.nlm.nih.gov/11547716/; "
            "https://clinicaltrials.gov/study/NCT00004297"
        ),
        "note": (
            "Phase III RCT audit 2026-07-12 added Alldredge2001 (PMID 11547716; "
            "NCT00004297), a randomized double-blind lorazepam/diazepam/placebo trial "
            "for out-of-hospital status epilepticus. Acute status termination is not "
            "represented as RR50, MPC, or a standard seizure-freedom patient rate."
        ),
    },
    "levetiracetam": {
        "link": "Manreza2021|https://pubmed.ncbi.nlm.nih.gov/34133509/",
        "sources": "https://pubmed.ncbi.nlm.nih.gov/34133509/",
        "note": (
            "Phase III RCT audit 2026-07-14 added Manreza2021 (PMID 34133509), "
            "a multicenter randomized double-blind placebo-controlled adjunctive "
            "levetiracetam trial in refractory focal epilepsy. The ITT population "
            "included 125 participants (62 levetiracetam; 63 placebo); 114 completed "
            "16 weeks. The paper reports RR50 and MPC but no extractable patient-level "
            "seizure-freedom rate."
        ),
        "diff_50_responder_maximum_effective_dose": (
            "7.1-49.4 % (drug minus placebo RR50 differential at maximum effective "
            "dose/regimen: Wu2018 LEV 1000-3000 mg/day 49.4%; Manreza2021 LEV up to "
            "3000 mg/day or 60 mg/kg/day 24.42%; PinaGarza2009 LEV 40-50 mg/kg/day "
            "23.5%; Peltola2009 LEV XR 1000 mg/day 13.9%; Wu2008 LEV 1000-3000 mg/day "
            "29.9%; Xiao2009 LEV 3000 mg/day 7.1%; Berkovic2007 LEV target 3000 mg/day "
            "adults or 60 mg/kg/day children 27%; Glauser2006 LEV target 60 mg/kg/day "
            "25%; Tsai2006 LEV up to 2000 mg/day 32.9%; BenMenachem2000 LEV 3000 "
            "mg/day 25.4%; Shorvon2000 LEV 2000 mg/day 21.2%; Cereghino2000 LEV 3000 "
            "mg/day 29%; Betts2000 LEV 2000 mg/day 32%)"
        ),
        "plot_diff_50_responder_maximum_effective_dose": (
            "Manreza2021|24.42|https://pubmed.ncbi.nlm.nih.gov/34133509/|125"
        ),
        "diff_median_pct_change_maximum_effective_dose": (
            "12.7-56.2 % (drug minus placebo MPC differential at maximum effective "
            "dose/regimen: Wu2018 LEV 1000-3000 mg/day 56.2%; Manreza2021 LEV up to "
            "3000 mg/day or 60 mg/kg/day 32.9%; PinaGarza2009 LEV 40-50 mg/kg/day "
            "36.5%; Peltola2009 LEV XR 1000 mg/day 12.7%; Wu2008 LEV 1000-3000 mg/day "
            "42.2%; Berkovic2007 LEV target 3000 mg/day adults or 60 mg/kg/day children "
            "28.3%; Glauser2006 LEV target 60 mg/kg/day 26.8%; Tsai2006 LEV up to 2000 "
            "mg/day 23.8%)"
        ),
        "plot_diff_median_pct_change_maximum_effective_dose": (
            "Manreza2021|32.9|https://pubmed.ncbi.nlm.nih.gov/34133509/|125"
        ),
    },
    "topiramate": {
        "link": "Chung2014|https://pubmed.ncbi.nlm.nih.gov/24902983/",
        "sources": (
            "https://pubmed.ncbi.nlm.nih.gov/24902983/; "
            "https://clinicaltrials.gov/study/NCT01142193"
        ),
        "note": (
            "Phase III RCT audit 2026-07-12 added Chung2014 (PMID 24902983; "
            "NCT01142193), the 249-participant PREVAIL trial of topiramate extended "
            "release 200 mg/day versus placebo."
        ),
        "diff_50_responder_maximum_effective_dose": (
            "14.7-43 % (drug minus placebo RR50 differential at maximum effective "
            "dose/regimen: Chung2014 topiramate extended release 200 mg/day 14.7%; "
            "Zhang2011 topiramate 200 mg/day 40.3%; Yen2000 topiramate 300 mg/day "
            "34.8%; PMID1999 topiramate 600 mg/day 37.7%; Sachdeo1999 topiramate "
            "approximately 6 mg/kg/day 25%; Elterman1999 topiramate 6 mg/kg/day 19%; "
            "Biton1999 topiramate approximately 6 mg/kg/day 36%; Sharief1996 topiramate "
            "400 mg/day 27%; Tassinari1996 topiramate 600 mg/day 37%; Faught1996 "
            "topiramate 400 mg/day 29%; Privitera1996 topiramate 600 mg/day 35%; "
            "BenMenachem1996 topiramate up to 800 mg/day 43%)"
        ),
        "plot_diff_50_responder_maximum_effective_dose": (
            "Chung2014|14.7|https://pubmed.ncbi.nlm.nih.gov/24902983/|249"
        ),
        "diff_median_pct_change_maximum_effective_dose": (
            "17.9-58 % (drug minus placebo MPC differential at maximum effective "
            "dose/regimen: Chung2014 topiramate extended release 200 mg/day 17.9%; "
            "Guberman2002 topiramate 200 mg/day 24%; PMID1999 topiramate 600 mg/day "
            "42.2%; Sachdeo1999 topiramate approximately 6 mg/kg/day 19.9%; Elterman1999 "
            "topiramate 6 mg/kg/day 22.6%; Biton1999 topiramate approximately 6 mg/kg/day "
            "47.7%; Sharief1996 topiramate 400 mg/day 40%; Tassinari1996 topiramate "
            "600 mg/day 58%; Faught1996 topiramate 400 mg/day 35%; Privitera1996 "
            "topiramate 600 mg/day 40%; BenMenachem1996 topiramate up to 800 mg/day 54%)"
        ),
        "plot_diff_median_pct_change_maximum_effective_dose": (
            "Chung2014|17.9|https://pubmed.ncbi.nlm.nih.gov/24902983/|249"
        ),
        "diff_seizure_freedom_maximum_effective_dose": (
            "1.6-6.7 % (drug minus placebo seizure-freedom differential at maximum "
            "effective dose/regimen: Chung2014 topiramate extended release 200 mg/day "
            "1.6%; PMID1999 topiramate 600 mg/day 6.7%)"
        ),
        "plot_diff_seizure_freedom_maximum_effective_dose": (
            "Chung2014|1.6|https://pubmed.ncbi.nlm.nih.gov/24902983/|249"
        ),
    },
}

PRIMARY_RCT_AUDIT_ROWS = [
    {
        "generic_name": "diazepam",
        "status": "included",
        "pmid": "24111974",
        "label": "AbouKhalil2013",
        "year": "2013",
        "first_author": "Abou-Khalil",
        "title": "A double-blind, randomized, placebo-controlled trial of a diazepam auto-injector administered by caregivers to patients with epilepsy who require intermittent intervention for acute repetitive seizures.",
        "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
        "reason": "qualifying phase III placebo-controlled randomized clinical trial report (NCT00319501)",
        "url": "https://pubmed.ncbi.nlm.nih.gov/24111974/",
    },
    {
        "generic_name": "lorazepam",
        "status": "included",
        "pmid": "11547716",
        "label": "Alldredge2001",
        "year": "2001",
        "first_author": "Alldredge",
        "title": "A comparison of lorazepam, diazepam, and placebo for the treatment of out-of-hospital status epilepticus.",
        "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, P.H.S.",
        "reason": "qualifying phase III placebo-controlled randomized clinical trial report (NCT00004297)",
        "url": "https://pubmed.ncbi.nlm.nih.gov/11547716/",
    },
    {
        "generic_name": "levetiracetam",
        "status": "included",
        "pmid": "34133509",
        "label": "Manreza2021",
        "year": "2021",
        "first_author": "Manreza",
        "title": "Efficacy and safety of levetiracetam as adjunctive therapy for refractory focal epilepsy.",
        "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial",
        "reason": "qualifying primary phase III placebo-controlled randomized clinical trial report; phase III design is explicit in the abstract and full text",
        "url": "https://pubmed.ncbi.nlm.nih.gov/34133509/",
    },
    {
        "generic_name": "topiramate",
        "status": "included",
        "pmid": "24902983",
        "label": "Chung2014",
        "year": "2014",
        "first_author": "Chung",
        "title": "Once-daily USL255 as adjunctive treatment of partial-onset seizures: randomized phase III study.",
        "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
        "reason": "qualifying phase III placebo-controlled randomized clinical trial report (NCT01142193)",
        "url": "https://pubmed.ncbi.nlm.nih.gov/24902983/",
    },
]

TOPIRAMATE_EFFICACY_AUDIT_ROW = {
    "generic_name": "topiramate",
    "label": "Chung2014",
    "pmid": "24902983",
    "title": "Once-daily USL255 as adjunctive treatment of partial-onset seizures: randomized phase III study.",
    "dose_or_regimen": "topiramate extended release 200 mg/day",
    "endpoint": "partial-onset seizures during the 11-week double-blind treatment phase",
    "rr50_active_percent": "37.9",
    "rr50_placebo_percent": "23.2",
    "rr50_differential_percent": "14.7",
    "rr50_included_in_csv_summary": "yes",
    "mpc_active_percent": "39.5",
    "mpc_placebo_percent": "21.6",
    "mpc_differential_percent": "17.9",
    "mpc_included_in_csv_summary": "yes",
    "sf_active_percent": "3.2",
    "sf_placebo_percent": "1.6",
    "sf_differential_percent": "1.6",
    "sf_included_in_csv_summary": "yes",
    "audit_note": "Primary phase III PREVAIL report; all 249 randomized participants were in the ITT population. Differentials are active minus placebo percentages at the sole studied 200 mg/day regimen.",
    "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/24902983/",
}

LEVETIRACETAM_EFFICACY_AUDIT_ROW = {
    "generic_name": "levetiracetam",
    "label": "Manreza2021",
    "pmid": "34133509",
    "title": "Efficacy and safety of levetiracetam as adjunctive therapy for refractory focal epilepsy.",
    "dose_or_regimen": "levetiracetam up to 3000 mg/day or 60 mg/kg/day; 2000 mg/day or 40 mg/kg/day permitted if the higher dose was not tolerated",
    "endpoint": "focal seizures during the 16-week double-blind treatment period",
    "rr50_active_percent": "38.71",
    "rr50_placebo_percent": "14.29",
    "rr50_differential_percent": "24.42",
    "rr50_included_in_csv_summary": "yes",
    "mpc_active_percent": "43.8",
    "mpc_placebo_percent": "10.9",
    "mpc_differential_percent": "32.9",
    "mpc_included_in_csv_summary": "yes",
    "sf_active_percent": "",
    "sf_placebo_percent": "",
    "sf_differential_percent": "",
    "sf_included_in_csv_summary": "no",
    "audit_note": "Primary phase III report. RR50 is from Table 3. MPC is the active-minus-placebo difference for the combined dose-adjustment and evaluation period in Figure 4. The ITT population was 125 (62 active, 63 placebo); 114 completed 16 weeks.",
    "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/34133509/",
}

NONSTANDARD_ENDPOINT_EFFICACY_AUDIT_ROWS = [
    {
        "generic_name": "diazepam",
        "label": "AbouKhalil2013",
        "pmid": "24111974",
        "title": "A double-blind, randomized, placebo-controlled trial of a diazepam auto-injector administered by caregivers to patients with epilepsy who require intermittent intervention for acute repetitive seizures.",
        "dose_or_regimen": "single weight- and age-based diazepam auto-injector dose (5, 10, 15, or 20 mg)",
        "endpoint": "time to next seizure or rescue from 15 minutes to 12 hours postdose",
        "rr50_active_percent": "",
        "rr50_placebo_percent": "",
        "rr50_differential_percent": "",
        "rr50_included_in_csv_summary": "no",
        "mpc_active_percent": "",
        "mpc_placebo_percent": "",
        "mpc_differential_percent": "",
        "mpc_included_in_csv_summary": "no",
        "sf_active_percent": "",
        "sf_placebo_percent": "",
        "sf_differential_percent": "",
        "sf_included_in_csv_summary": "no",
        "audit_note": "Primary phase III report; 234 participants were randomized and 163 were included in the ITT analysis. The primary time-to-next-seizure/rescue endpoint is not RR50, MPC, or a standard seizure-freedom patient rate.",
        "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/24111974/",
    },
    {
        "generic_name": "lorazepam",
        "label": "Alldredge2001",
        "pmid": "11547716",
        "title": "A comparison of lorazepam, diazepam, and placebo for the treatment of out-of-hospital status epilepticus.",
        "dose_or_regimen": "lorazepam 2 mg IV or diazepam 5 mg IV, with one identical repeat dose if needed",
        "endpoint": "termination of status epilepticus on emergency-department arrival",
        "rr50_active_percent": "",
        "rr50_placebo_percent": "",
        "rr50_differential_percent": "",
        "rr50_included_in_csv_summary": "no",
        "mpc_active_percent": "",
        "mpc_placebo_percent": "",
        "mpc_differential_percent": "",
        "mpc_included_in_csv_summary": "no",
        "sf_active_percent": "",
        "sf_placebo_percent": "",
        "sf_differential_percent": "",
        "sf_included_in_csv_summary": "no",
        "audit_note": "Primary randomized phase III-associated report with 205 participants. Acute status termination is not RR50, MPC, or a standard longitudinal seizure-freedom patient rate.",
        "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/11547716/",
    },
]

TOPIRAMATE_SEIZURE_FREEDOM_AUDIT_ROW = {
    "generic_name": "topiramate",
    "label": "Chung2014",
    "pmid": "24902983",
    "title": "Once-daily USL255 as adjunctive treatment of partial-onset seizures: randomized phase III study.",
    "active_rate_percent": "3.2",
    "placebo_rate_percent": "1.6",
    "differential_percent": "1.6",
    "dose_or_regimen": "topiramate extended release 200 mg/day",
    "endpoint": "100% reduction in weekly seizure frequency during titration plus maintenance",
    "included_in_csv_summary": "yes",
    "extraction_status": "extracted_patient_rate_differential",
    "audit_note": "Primary phase III PREVAIL report: 4/124 topiramate and 2/125 placebo participants were seizure-free during treatment.",
    "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/24902983/",
}

LEVETIRACETAM_SEIZURE_FREEDOM_AUDIT_ROW = {
    "generic_name": "levetiracetam",
    "label": "Manreza2021",
    "pmid": "34133509",
    "title": "Efficacy and safety of levetiracetam as adjunctive therapy for refractory focal epilepsy.",
    "active_rate_percent": "",
    "placebo_rate_percent": "",
    "differential_percent": "",
    "dose_or_regimen": "levetiracetam up to 3000 mg/day or 60 mg/kg/day",
    "endpoint": "patient-level seizure freedom during double-blind treatment",
    "included_in_csv_summary": "no",
    "extraction_status": "reviewed_no_extractable_differential",
    "audit_note": "The primary report provides RR50 and MPC but does not report an extractable active-versus-placebo patient-level seizure-freedom rate.",
    "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/34133509/",
}

NONSTANDARD_ENDPOINT_SEIZURE_FREEDOM_AUDIT_ROWS = [
    {
        "generic_name": row["generic_name"],
        "label": row["label"],
        "pmid": row["pmid"],
        "title": row["title"],
        "active_rate_percent": "",
        "placebo_rate_percent": "",
        "differential_percent": "",
        "dose_or_regimen": row["dose_or_regimen"],
        "endpoint": row["endpoint"],
        "included_in_csv_summary": "no",
        "extraction_status": "reviewed_no_extractable_differential",
        "audit_note": row["audit_note"],
        "pubmed_url": row["pubmed_url"],
    }
    for row in NONSTANDARD_ENDPOINT_EFFICACY_AUDIT_ROWS
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


def remove_sources(value: str, removed: str) -> str:
    blocked = set(split_sources(removed))
    return "; ".join(source for source in split_sources(value) if source not in blocked)


def upsert_audit_rows(path: Path, records: list[dict[str, str]]) -> None:
    fieldnames, rows = read_csv(path)
    indexes = {
        (row["generic_name"], row["pmid"]): index
        for index, row in enumerate(rows)
    }
    for record in records:
        key = (record["generic_name"], record["pmid"])
        if key in indexes:
            rows[indexes[key]] = record
        else:
            indexes[key] = len(rows)
            rows.append(record)
    write_csv(path, fieldnames, rows)


def prepend_unique(value: str, item: str) -> str:
    parts = split_sources(value)
    if item in parts:
        return value
    return "; ".join([item, *parts])


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
    upsert_audit_rows(RCT_AUDIT_PATH, PRIMARY_RCT_AUDIT_ROWS)
    upsert_audit_rows(
        EFFICACY_AUDIT_PATH,
        [
            TOPIRAMATE_EFFICACY_AUDIT_ROW,
            LEVETIRACETAM_EFFICACY_AUDIT_ROW,
            *NONSTANDARD_ENDPOINT_EFFICACY_AUDIT_ROWS,
        ],
    )
    upsert_audit_rows(
        SEIZURE_FREEDOM_AUDIT_PATH,
        [
            TOPIRAMATE_SEIZURE_FREEDOM_AUDIT_ROW,
            LEVETIRACETAM_SEIZURE_FREEDOM_AUDIT_ROW,
            *NONSTANDARD_ENDPOINT_SEIZURE_FREEDOM_AUDIT_ROWS,
        ],
    )
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
        rct_correction = PRIMARY_RCT_CORRECTIONS.get(generic)
        if rct_correction:
            row["pubmed_phase_ii_iii_rct_links"] = prepend_unique(
                row["pubmed_phase_ii_iii_rct_links"], rct_correction["link"]
            )
            row["evidence_sources"] = remove_sources(
                row["evidence_sources"], rct_correction["sources"]
            )
            row["rct_pubmed_verification_notes"] = source_union(
                row["rct_pubmed_verification_notes"], rct_correction["note"]
            )
            for field in OUTCOME_FIELDS + PLOT_FIELDS:
                value = rct_correction.get(field)
                if not value:
                    continue
                if field.startswith("plot_"):
                    row[field] = prepend_unique(row[field], value)
                else:
                    row[field] = value
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
