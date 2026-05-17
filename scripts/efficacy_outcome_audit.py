#!/usr/bin/env python3
import csv
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASM_CSV = ROOT / "ASM-list.csv"
REPORT_DIR = ROOT / "pubmed_cache" / "reports"
RCT_REPORT = REPORT_DIR / "pubmed_rct_audit.csv"
OUTCOME_REPORT = REPORT_DIR / "efficacy_outcome_audit.csv"
SEIZURE_FREEDOM_REPORT = REPORT_DIR / "seizure_freedom_audit.csv"
GAP_REPORT = REPORT_DIR / "efficacy_gap_review.csv"

RR50_FIELD = "diff_50_responder_maximum_effective_dose"
MPC_FIELD = "diff_median_pct_change_maximum_effective_dose"
SF_FIELD = "diff_seizure_freedom_maximum_effective_dose"
REFRESH_FIELD = "data_most_recently_refreshed"

OUTCOME_FIELDS = [
    "generic_name",
    "label",
    "pmid",
    "title",
    "dose_or_regimen",
    "endpoint",
    "rr50_active_percent",
    "rr50_placebo_percent",
    "rr50_differential_percent",
    "rr50_included_in_csv_summary",
    "mpc_active_percent",
    "mpc_placebo_percent",
    "mpc_differential_percent",
    "mpc_included_in_csv_summary",
    "sf_active_percent",
    "sf_placebo_percent",
    "sf_differential_percent",
    "sf_included_in_csv_summary",
    "audit_note",
    "pubmed_url",
]


def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore", lineterminator="\r\n")
        writer.writeheader()
        writer.writerows(rows)


def format_number(value):
    value = round(float(value), 2)
    if value.is_integer():
        return str(int(value))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def summarize(rows, diff_field, include_field, noun):
    included = [row for row in rows if row.get(include_field) == "yes" and row.get(diff_field) not in {"", None}]
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


def nonextractable_text(has_rcts, noun):
    if not has_rcts:
        return "No PubMed phase II/III RCTs found"
    return f"NR/not extractable as a drug-minus-placebo {noun} at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records"


def blank_outcome_row(rct_row):
    return {
        "generic_name": rct_row["generic_name"],
        "label": rct_row["label"],
        "pmid": rct_row["pmid"],
        "title": rct_row["title"],
        "dose_or_regimen": "",
        "endpoint": "",
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
        "audit_note": "Included RCT has not yet been manually extracted in efficacy_outcome_audit.csv.",
        "pubmed_url": rct_row["url"],
    }


def normalized_outcome_rows(rct_rows, existing_rows):
    existing_by_key = {
        (row.get("generic_name", ""), row.get("label", ""), row.get("pmid", "")): row
        for row in existing_rows
    }
    rows = []
    for rct_row in rct_rows:
        key = (rct_row["generic_name"], rct_row["label"], rct_row["pmid"])
        outcome = blank_outcome_row(rct_row)
        outcome.update({field: existing_by_key.get(key, {}).get(field, outcome[field]) for field in OUTCOME_FIELDS})
        outcome["generic_name"] = rct_row["generic_name"]
        outcome["label"] = rct_row["label"]
        outcome["pmid"] = rct_row["pmid"]
        outcome["title"] = rct_row["title"]
        outcome["pubmed_url"] = rct_row["url"]
        rows.append(outcome)
    return rows


def main():
    if not OUTCOME_REPORT.exists():
        raise SystemExit(f"Missing extraction source: {OUTCOME_REPORT.relative_to(ROOT)}")

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    asm_rows = read_csv(ASM_CSV)
    rct_rows = [row for row in read_csv(RCT_REPORT) if row["status"] == "included"]
    outcome_rows = normalized_outcome_rows(rct_rows, read_csv(OUTCOME_REPORT))
    write_csv(OUTCOME_REPORT, outcome_rows, OUTCOME_FIELDS)

    seizure_rows = [
        {
            "generic_name": row["generic_name"],
            "label": row["label"],
            "pmid": row["pmid"],
            "title": row["title"],
            "active_rate_percent": row["sf_active_percent"],
            "placebo_rate_percent": row["sf_placebo_percent"],
            "differential_percent": row["sf_differential_percent"],
            "dose_or_regimen": row["dose_or_regimen"],
            "endpoint": row["endpoint"],
            "included_in_csv_summary": row["sf_included_in_csv_summary"],
            "extraction_status": "differential_extracted" if row["sf_included_in_csv_summary"] == "yes" else "reviewed_no_extractable_differential",
            "audit_note": row["audit_note"],
            "pubmed_url": row["pubmed_url"],
        }
        for row in outcome_rows
    ]
    write_csv(
        SEIZURE_FREEDOM_REPORT,
        seizure_rows,
        [
            "generic_name",
            "label",
            "pmid",
            "title",
            "active_rate_percent",
            "placebo_rate_percent",
            "differential_percent",
            "dose_or_regimen",
            "endpoint",
            "included_in_csv_summary",
            "extraction_status",
            "audit_note",
            "pubmed_url",
        ],
    )

    by_drug = defaultdict(list)
    rct_count = defaultdict(int)
    for row in outcome_rows:
        by_drug[row["generic_name"]].append(row)
        rct_count[row["generic_name"]] += 1

    refresh_date = datetime.now().strftime("%m-%d-%Y")
    for row in asm_rows:
        generic = row["generic_name"]
        has_rcts = rct_count[generic] > 0
        rr50 = summarize(by_drug[generic], "rr50_differential_percent", "rr50_included_in_csv_summary", "RR50 differential")
        mpc = summarize(by_drug[generic], "mpc_differential_percent", "mpc_included_in_csv_summary", "MPC differential")
        sf = summarize(by_drug[generic], "sf_differential_percent", "sf_included_in_csv_summary", "seizure-freedom differential")
        row[RR50_FIELD] = rr50 or nonextractable_text(has_rcts, "RR50 differential")
        row[MPC_FIELD] = mpc or nonextractable_text(has_rcts, "MPC differential")
        row[SF_FIELD] = sf or nonextractable_text(has_rcts, "seizure-freedom patient-rate differential")
        row[REFRESH_FIELD] = refresh_date

    write_csv(ASM_CSV, asm_rows, list(asm_rows[0].keys()))

    gap_rows = []
    for row in asm_rows:
        missing = [field for field in [RR50_FIELD, MPC_FIELD, SF_FIELD] if "%" not in row[field]]
        if missing:
            gap_rows.append(
                {
                    "generic_name": row["generic_name"],
                    "missing_fields": "; ".join(missing),
                    "rct_count": rct_count[row["generic_name"]],
                    "review_status": "no qualifying PubMed RCTs" if not rct_count[row["generic_name"]] else "reviewed RCTs; max-dose value not extractable",
                    "rct_links": row.get("pubmed_phase_ii_iii_rct_links", ""),
                }
            )
    write_csv(GAP_REPORT, gap_rows, ["generic_name", "missing_fields", "rct_count", "review_status", "rct_links"])

    print(f"Reviewed {len(outcome_rows)} included RCT rows from {OUTCOME_REPORT.relative_to(ROOT)}.")
    print(f"RR50 extracted for {sum(1 for row in outcome_rows if row['rr50_included_in_csv_summary'] == 'yes')} row(s).")
    print(f"MPC extracted for {sum(1 for row in outcome_rows if row['mpc_included_in_csv_summary'] == 'yes')} row(s).")
    print(f"Seizure freedom extracted for {sum(1 for row in outcome_rows if row['sf_included_in_csv_summary'] == 'yes')} row(s).")
    print(f"Wrote {SEIZURE_FREEDOM_REPORT.relative_to(ROOT)} and {GAP_REPORT.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
