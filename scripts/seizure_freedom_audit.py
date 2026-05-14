#!/usr/bin/env python3
import csv
import re
import xml.etree.ElementTree as ET
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASM_CSV = ROOT / "ASM-list.csv"
RCT_REPORT = ROOT / "pubmed_cache" / "reports" / "pubmed_rct_audit.csv"
EFETCH_DIR = ROOT / "pubmed_cache" / "efetch"
OUT_REPORT = ROOT / "pubmed_cache" / "reports" / "seizure_freedom_audit.csv"
OUTPUT_FIELD = "diff_seizure_freedom_maximum_effective_dose"
OLD_FIELD = "seizure_freedom_rct_rates"
REFRESH_DATE = "05-14-2026"


SEIZURE_FREEDOM_TERMS = re.compile(
    r"seizure[- ]free|seizure freedom|freedom from|free of .*seizure|"
    r"spasm[- ]free|seizure-free days|cessation|ceased|100% reduction|"
    r"75-100% reduction|days free",
    re.I,
)


def pct(value):
    return None if value is None else round(float(value), 2)


def diff(active, placebo):
    return pct(float(active) - float(placebo))


def extraction(
    status,
    active=None,
    placebo=None,
    dose="",
    endpoint="",
    note="",
    include=True,
):
    active = pct(active)
    placebo = pct(placebo)
    differential = diff(active, placebo) if active is not None and placebo is not None else None
    return {
        "extraction_status": status,
        "active_rate_percent": active,
        "placebo_rate_percent": placebo,
        "differential_percent": differential,
        "dose_or_regimen": dose,
        "endpoint": endpoint,
        "included_in_csv_summary": "yes" if include and differential is not None else "no",
        "audit_note": note,
    }


# Manual extraction map built by looping through every included PubMed RCT row
# and reviewing the current PubMed abstract text for seizure-freedom language.
# Values are active-rate minus placebo-rate. Rates are included in the CSV
# roll-up only when both active and placebo patient-rate percentages are
# extractable for the relevant maximum reported active RCT dose/regimen.
EXTRACTIONS = {
    ("brivaracetam", "Yu2026"): extraction(
        "differential_extracted",
        11.11,
        2.27,
        "BRV 200 mg/day",
        "seizure freedom during 12-week treatment",
        "Abstract reports 10/90 (11.11%) BRV vs 2/88 (2.27%) placebo.",
    ),
    ("brivaracetam", "Inoue2024"): extraction(
        "differential_extracted",
        6.8,
        0,
        "BRV 200 mg/day",
        "seizure-free during treatment period",
        "Highest BRV arm in abstract: 6.8% with 200 mg/day vs 0% placebo.",
    ),
    ("brivaracetam", "Ryvlin2013"): extraction(
        "differential_extracted",
        4.0,
        0,
        "BRV 100 mg/day",
        "complete seizure freedom",
        "Highest BRV arm in abstract: 4/100 on 100 mg/day vs 0/100 placebo.",
    ),
    ("brivaracetam", "French2010"): extraction(
        "differential_extracted",
        7.7,
        1.9,
        "BRV 50 mg/day",
        "POS seizure freedom during 7-week treatment",
        "Highest BRV arm in abstract: 7.7% with 50 mg/day vs 1.9% placebo.",
    ),
    ("cannabidiol", "Devinsky2017"): extraction(
        "differential_extracted",
        5.0,
        0,
        "cannabidiol 20 mg/kg/day",
        "became seizure-free",
        "Abstract reports 5% cannabidiol vs 0% placebo in Dravet syndrome.",
    ),
    ("cenobamate", "Lee2025"): extraction(
        "differential_extracted",
        52.4,
        2.6,
        "cenobamate 400 mg/day",
        "seizure-free during maintenance phase",
        "Highest cenobamate arm in abstract: 52.4% with 400 mg/day vs 2.6% placebo.",
    ),
    ("cenobamate", "Chung2020"): extraction(
        "differential_extracted",
        28.3,
        8.8,
        "cenobamate 200 mg/day",
        "seizure-free during maintenance",
        "Abstract reports 28.3% cenobamate vs 8.8% placebo.",
    ),
    ("diazepam", "Cereghino1998"): extraction(
        "differential_extracted",
        55.0,
        34.0,
        "single caregiver-administered rectal diazepam dose",
        "seizure free post-treatment",
        "Abstract reports 55% Diastat vs 34% placebo post-treatment.",
    ),
    ("lacosamide", "Vossler2020"): extraction(
        "differential_extracted",
        31.3,
        17.2,
        "lacosamide up to 12 mg/kg/day or 400 mg/day",
        "Kaplan-Meier estimated freedom from PGTCS at day 166",
        "Abstract reports 31.3% lacosamide vs 17.2% placebo; observed treatment-period freedom was 27.5% vs 13.2%.",
    ),
    ("levetiracetam", "Wu2018"): extraction(
        "differential_extracted",
        29.6,
        3.1,
        "LEV 1000-3000 mg/day",
        "freedom from GTC seizures during evaluation period",
        "Abstract reports 29.6% LEV vs 3.1% placebo.",
    ),
    ("levetiracetam", "Fattore2011"): extraction(
        "differential_extracted",
        18.4,
        0,
        "LEV up to 30 mg/kg/day",
        "free from clinical and EEG seizures during last 4 days",
        "Abstract reports 18.4% LEV vs 0% placebo.",
    ),
    ("levetiracetam", "Peltola2009"): extraction(
        "differential_extracted",
        10.1,
        1.3,
        "LEV XR 1000 mg/day",
        "free of partial-onset seizures during 12-week treatment",
        "Abstract reports 10.1% LEV XR vs 1.3% placebo.",
    ),
    ("levetiracetam", "Wu2008"): extraction(
        "differential_extracted",
        10.8,
        2.0,
        "LEV 1000-3000 mg/day",
        "freedom from partial-onset seizures during treatment",
        "Abstract reports 10.8% LEV vs 2.0% placebo.",
    ),
    ("levetiracetam", "Berkovic2007"): extraction(
        "differential_extracted",
        34.2,
        10.7,
        "adjunctive LEV",
        "free of GTC seizures during evaluation period",
        "Abstract reports 34.2% LEV vs 10.7% placebo for GTC seizure freedom; all-seizure freedom was 24.1% vs 8.3%.",
    ),
    ("levetiracetam", "Glauser2006"): extraction(
        "differential_extracted",
        6.9,
        1.0,
        "pediatric adjunctive LEV",
        "seizure-free during entire double-blind period",
        "Abstract reports 7/101 (6.9%) LEV vs 1/97 (1.0%) placebo.",
    ),
    ("levetiracetam", "Boon2002"): extraction(
        "differential_extracted",
        6.3,
        1.2,
        "LEV 2000 mg/day",
        "seizure-free during corresponding evaluation period",
        "Highest reported arm in abstract: 6.3% with 2000 mg/day vs 1.2% placebo.",
    ),
    ("levetiracetam", "Cereghino2000"): extraction(
        "aggregate_active_arms_not_summarized",
        5.5,
        0,
        "LEV 1000 and 3000 mg/day active arms aggregated",
        "became seizure free",
        "Abstract reports 11/199 active patients vs 0 placebo, but does not give a 3000 mg/day arm-specific seizure-free rate.",
        include=False,
    ),
    ("midazolam", "Spencer2020"): extraction(
        "differential_extracted",
        54.8,
        38.7,
        "midazolam nasal spray 5 mg",
        "seizure-free for 6 hours after treatment",
        "Abstract reports 54.8% MDZ-NS vs 38.7% placebo.",
    ),
    ("oxcarbazepine", "French2013"): extraction(
        "differential_extracted",
        11.4,
        3.3,
        "extended-release oxcarbazepine 2400 mg/day",
        "16-week seizure-free rate",
        "Highest active arm in abstract: 11.4% with 2400 mg/day vs 3.3% placebo.",
    ),
    ("perampanel", "French2015"): extraction(
        "differential_extracted",
        30.9,
        12.3,
        "adjunctive perampanel for PGTC seizures",
        "PGTC seizure freedom during maintenance",
        "Abstract reports 30.9% perampanel vs 12.3% placebo.",
    ),
    ("phenytoin", "Young2004"): extraction(
        "prophylaxis_event_rate_not_summarized",
        93.5,
        94.6,
        "early posttraumatic seizure prophylaxis",
        "posttraumatic seizure-free during 48-hour observation",
        "Derived from abstract counts: 3/46 phenytoin and 3/56 placebo had seizures. This prophylaxis endpoint is reported in the audit but not rolled into the ASM seizure-freedom summary.",
        include=False,
    ),
    ("stiripentol", "Guerrini2024"): extraction(
        "differential_extracted",
        38.0,
        0,
        "stiripentol add-on to clobazam/valproate",
        "free of GTCS",
        "Abstract reports 38% stiripentol vs 0% placebo free of GTCS.",
    ),
    ("stiripentol", "Chiron2000"): extraction(
        "differential_extracted",
        42.9,
        0,
        "stiripentol add-on to valproate and clobazam",
        "free of clonic or tonic-clonic seizures",
        "Abstract reports 9/21 (42.9%) stiripentol vs none on placebo.",
    ),
    ("vigabatrin", "Appleton1999"): extraction(
        "differential_extracted",
        35.0,
        10.0,
        "vigabatrin first-line infantile-spasm treatment",
        "spasm-free on final day of double-blind period",
        "Abstract reports 7/20 (35%) vigabatrin vs 2/20 (10%) placebo.",
    ),
}


NONEXTRACTABLE_REVIEWS = {
    ("brivaracetam", "Bast2022"): "Seizure-free status is part of the adaptive design, but the abstract does not report active and placebo seizure-freedom rates.",
    ("cenobamate", "Krauss2019"): "Seizure freedom is mentioned as background need; no active/placebo seizure-free rates are reported in the abstract.",
    ("clonazepam", "Navarro2015"): "Both arms received clonazepam; the abstract reports convulsion cessation after adding levetiracetam or placebo, not a placebo-controlled clonazepam seizure-freedom differential.",
    ("eslicarbazepine acetate", "Elger2007"): "Abstract reports 24% seizure-free in active QD/BID groups but does not state the placebo seizure-free percentage, so a differential cannot be calculated.",
    ("fenfluramine", "Sullivan2023"): "Abstract reports longest seizure-free interval, not seizure-free patient percentages.",
    ("fenfluramine", "Nabbout2020"): "Abstract reports longest seizure-free interval, not seizure-free patient percentages.",
    ("gabapentin", "Appleton1999"): "Abstract reports 3 gabapentin and 1 placebo patient seizure-free but does not report arm denominators or percentages in the abstract.",
    ("ganaxolone", "Sperling2017"): "Seizure-free days is listed as an endpoint, but the abstract does not report a seizure-free patient rate.",
    ("lacosamide", "Hong2016"): "Abstract states seizure-freedom rates were higher with lacosamide than placebo but does not report numeric rates.",
    ("lamotrigine", "Beran1998"): "Seizure-free count is reported for open-label follow-up, not the double-blind placebo-controlled period.",
    ("levetiracetam", "PeterDerex2022"): "Prophylaxis trial reports seizure occurrence in the first 72 hours, not an epilepsy-treatment seizure-free patient endpoint for CSV roll-up.",
    ("levetiracetam", "Navarro2015"): "Status epilepticus trial reports acute convulsion cessation, not seizure freedom; active arm was levetiracetam plus clonazepam vs placebo plus clonazepam.",
    ("levetiracetam", "BenMenachem2000"): "Abstract reports seizure-free patients during responder-selected monotherapy conversion but no placebo seizure-free rate.",
    ("perampanel", "Vossler2024"): "Seizure-freedom rates are listed as key secondary endpoints, but numeric rates are not reported in the abstract.",
    ("perampanel", "Nishida2017"): "Seizure freedom is listed as an endpoint, but numeric rates are not reported in the abstract.",
    ("perampanel", "Belousova2014"): "Seizure freedom is background text; no active/placebo seizure-free rates are reported.",
    ("pregabalin", "French2014"): "Historical-control monotherapy study reports active seizure-free counts but has no placebo arm percentage for differential calculation.",
    ("pregabalin", "Elger2005"): "Seizure-free interval is part of trial design/dose adjustment, not a reported active/placebo seizure-free outcome.",
    ("stiripentol", "Nabbout2020"): "Fenfluramine RCT reports longest seizure-free interval, not a stiripentol active/placebo seizure-free patient percentage.",
    ("tiagabine", "Kalviainen1998"): "Abstract reports increased days free of partial seizures, not seizure-free patient percentages.",
    ("topiramate", "BenMenachem1996"): "Abstract reports 75-100% seizure reduction, not complete seizure freedom.",
    ("vigabatrin", "Kalita2025"): "Abstract reports seizure-free days, not seizure-free patient percentages.",
}


def read_csv(path):
    with path.open(newline="") as handle:
        return list(csv.DictReader(handle))


def parse_pubmed_articles():
    articles = {}
    for xml_path in sorted(EFETCH_DIR.glob("*.xml")):
        root = ET.parse(xml_path).getroot()
        for article in root.findall(".//PubmedArticle"):
            pmid = (article.findtext(".//PMID") or "").strip()
            title_el = article.find(".//ArticleTitle")
            title = " ".join("".join(title_el.itertext()).split()) if title_el is not None else ""
            abstract_parts = []
            for part in article.findall(".//AbstractText"):
                label = part.attrib.get("Label", "")
                text = " ".join("".join(part.itertext()).split())
                abstract_parts.append(f"{label}: {text}" if label else text)
            articles[pmid] = {
                "title": title,
                "abstract": " ".join(abstract_parts),
            }
    return articles


def default_review(row, article):
    text = f"{article.get('title', '')} {article.get('abstract', '')}"
    if SEIZURE_FREEDOM_TERMS.search(text):
        note = NONEXTRACTABLE_REVIEWS.get(
            (row["generic_name"], row["label"]),
            "Reviewed seizure-freedom language in the PubMed record; no extractable active-placebo patient-rate differential was available.",
        )
        status = "reviewed_no_extractable_differential"
    else:
        note = "No seizure-freedom patient-rate language found in the PubMed title/abstract."
        status = "not_reported_in_pubmed_record"
    return extraction(status, note=note, include=False)


def report_row(row, article):
    item = EXTRACTIONS.get((row["generic_name"], row["label"]))
    if item is None:
        item = default_review(row, article)
    return {
        "generic_name": row["generic_name"],
        "label": row["label"],
        "pmid": row["pmid"],
        "title": row["title"],
        "active_rate_percent": "" if item["active_rate_percent"] is None else item["active_rate_percent"],
        "placebo_rate_percent": "" if item["placebo_rate_percent"] is None else item["placebo_rate_percent"],
        "differential_percent": "" if item["differential_percent"] is None else item["differential_percent"],
        "dose_or_regimen": item["dose_or_regimen"],
        "endpoint": item["endpoint"],
        "included_in_csv_summary": item["included_in_csv_summary"],
        "extraction_status": item["extraction_status"],
        "audit_note": item["audit_note"],
        "pubmed_url": row["url"],
    }


def format_number(value):
    value = round(float(value), 2)
    if value.is_integer():
        return str(int(value))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def summarize_drug(generic, items, has_qualifying_rcts):
    included = [item for item in items if item["included_in_csv_summary"] == "yes" and item["differential_percent"] != ""]
    if included:
        values = [float(item["differential_percent"]) for item in included]
        low = min(values)
        high = max(values)
        value_text = f"{format_number(low)} %" if low == high else f"{format_number(low)}-{format_number(high)} %"
        details = "; ".join(
            f"{item['label']} {item['dose_or_regimen']} {format_number(item['differential_percent'])}%"
            for item in included
        )
        return f"{value_text} (drug minus placebo seizure-freedom differential at maximum reported active RCT dose/regimen: {details})"
    if not has_qualifying_rcts:
        return "No PubMed phase II/III RCTs found"
    return "NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential from included phase II/III placebo-controlled RCT records"


def update_asm_csv(report_rows, included_rct_rows):
    rows = read_csv(ASM_CSV)
    old_fieldnames = list(rows[0].keys())
    fieldnames = []
    inserted = False
    for field in old_fieldnames:
        if field == OUTPUT_FIELD:
            if not inserted:
                fieldnames.append(OUTPUT_FIELD)
                inserted = True
            continue
        if field == OLD_FIELD:
            if not inserted:
                fieldnames.append(OUTPUT_FIELD)
                inserted = True
            continue
        fieldnames.append(field)
        if field == "diff_median_pct_change_maximum_effective_dose" and not inserted:
            fieldnames.append(OUTPUT_FIELD)
            inserted = True
    if not inserted:
        fieldnames.append(OUTPUT_FIELD)

    report_by_drug = defaultdict(list)
    for item in report_rows:
        report_by_drug[item["generic_name"]].append(item)
    rct_count_by_drug = defaultdict(int)
    for item in included_rct_rows:
        rct_count_by_drug[item["generic_name"]] += 1

    for row in rows:
        generic = row["generic_name"]
        row[OUTPUT_FIELD] = summarize_drug(generic, report_by_drug[generic], rct_count_by_drug[generic] > 0)
        row["data_most_recently_refreshed"] = REFRESH_DATE
        row.pop(OLD_FIELD, None)

    with ASM_CSV.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\r\n")
        writer.writeheader()
        writer.writerows(rows)


def main():
    included = [row for row in read_csv(RCT_REPORT) if row["status"] == "included"]
    articles = parse_pubmed_articles()
    report_rows = [report_row(row, articles.get(row["pmid"], {})) for row in included]

    OUT_REPORT.parent.mkdir(parents=True, exist_ok=True)
    fieldnames = [
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
    ]
    with OUT_REPORT.open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_rows)

    update_asm_csv(report_rows, included)

    extracted = sum(1 for row in report_rows if row["differential_percent"] != "")
    summarized = sum(1 for row in report_rows if row["included_in_csv_summary"] == "yes")
    print(f"Reviewed {len(report_rows)} included RCT rows.")
    print(f"Extracted active-placebo differentials for {extracted} RCT row(s).")
    print(f"Included {summarized} RCT row(s) in the ASM CSV roll-up.")
    print(f"Wrote {OUT_REPORT.relative_to(ROOT)} and updated {ASM_CSV.name}.")


if __name__ == "__main__":
    main()
