#!/usr/bin/env python3
import argparse
import csv
import hashlib
import html
import json
import re
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime
from email.utils import parsedate_to_datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "ASM-list.csv"
AUDIT_PATH = ROOT / "pubmed_cache" / "reports" / "fda_boxed_warning_audit.csv"
CACHE_DIR = ROOT / ".fda-label-cache"
REFRESH_DATE = datetime.now().strftime("%m-%d-%Y")
DAILYMED_SPL_SEARCH = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls.json?drug_name={term}"
DAILYMED_SPL_XML = "https://dailymed.nlm.nih.gov/dailymed/services/v2/spls/{setid}.xml"
DAILYMED_LABEL_URL = "https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={setid}"
FDA_SOURCE = "FDA/DailyMed labeling"
BOXED_SECTION_CODE = "34066-1"


FIELDNAMES_TO_INSERT = [
    "fda_black_box_warning",
    "fda_black_box_warning_source",
    "fda_black_box_warning_verified",
]


def normalize_space(value):
    return re.sub(r"\s+", " ", value or "").strip()


def normalize_for_compare(value):
    return normalize_space(value).replace(" ,", ",").replace(" .", ".")


def split_semicolon(value):
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def row_terms(row):
    terms = [row.get("generic_name", "")]
    terms.extend(split_semicolon(row.get("alternate_generic_names", "")))
    terms.extend(split_semicolon(row.get("trade_names", "")))
    terms.extend(split_semicolon(row.get("pubmed_search_aliases", "")))
    cleaned = []
    seen = set()
    for term in terms:
        term = re.sub(r"\s*\([^)]*\)", "", term).strip()
        lowered = term.lower()
        if not term:
            continue
        if "no human" in lowered or "veterinary" in lowered:
            continue
        if len(term) < 3 or len(term.split()) > 5:
            continue
        key = lowered
        if key not in seen:
            seen.add(key)
            cleaned.append(term)
    return cleaned


def setids_from_existing_sources(row):
    text = " ".join(
        [
            row.get("fda_black_box_warning_source", ""),
            row.get("fda_black_box_warning", ""),
        ]
    )
    return sorted(set(re.findall(r"setid=([0-9a-fA-F-]{20,})", text)))


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "source"


def http_get(url, refresh=False, suffix=".txt"):
    CACHE_DIR.mkdir(exist_ok=True)
    key = hashlib.sha256(url.encode()).hexdigest()[:24]
    path = CACHE_DIR / f"{key}{suffix}"
    if path.exists() and not refresh:
        return path.read_bytes()
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "ASM-master FDA boxed warning updater/1.0"},
    )
    with urllib.request.urlopen(req, timeout=45) as response:
        data = response.read()
    path.write_bytes(data)
    time.sleep(0.02)
    return data


def parse_date(value):
    if not value:
        return datetime.min
    for fmt in ("%b %d, %Y", "%B %d, %Y"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            pass
    try:
        return parsedate_to_datetime(value).replace(tzinfo=None)
    except Exception:
        return datetime.min


def search_spls(term, refresh=False):
    url = DAILYMED_SPL_SEARCH.format(term=urllib.parse.quote(term))
    try:
        data = json.loads(http_get(url, refresh=refresh, suffix=".json").decode("utf-8"))
    except Exception:
        return []
    return data.get("data") or []


def fetch_xml(setid, refresh=False):
    url = DAILYMED_SPL_XML.format(setid=setid)
    return http_get(url, refresh=refresh, suffix=".xml")


def xml_text(element):
    text = normalize_space(" ".join(element.itertext()))
    return html.unescape(text)


def local_name(tag):
    return tag.rsplit("}", 1)[-1]


def section_title(section, ns):
    title = section.find("hl7:title", ns)
    return xml_text(title) if title is not None else ""


def section_code(section, ns):
    code = section.find("hl7:code", ns)
    if code is None:
        return "", ""
    return code.attrib.get("code", ""), code.attrib.get("displayName", "")


def extract_boxed_warning(xml_bytes):
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return "", "", ""
    ns = {"hl7": "urn:hl7-org:v3"}
    boxed_sections = []
    for section in root.findall(".//hl7:section", ns):
        title = section_title(section, ns)
        code, display = section_code(section, ns)
        title_upper = title.upper()
        display_upper = display.upper()
        is_boxed = code == BOXED_SECTION_CODE or title_upper.startswith("BOXED WARNING") or title_upper.startswith("WARNING:")
        if is_boxed:
            text = xml_text(section)
            lead = text.upper()[:300]
            if text and ("WARNING" in lead or "WARNINGS" in lead):
                boxed_sections.append({"title": title, "code": code, "text": text})
    if not boxed_sections:
        return "", "", ""
    selected = max(boxed_sections, key=lambda item: len(item["text"]))
    return selected["text"], selected["title"], selected["code"]


def title_from_xml(xml_bytes):
    try:
        root = ET.fromstring(xml_bytes)
    except ET.ParseError:
        return ""
    ns = {"hl7": "urn:hl7-org:v3"}
    title = root.find(".//hl7:title", ns)
    return xml_text(title) if title is not None else ""


def terms_for_row(row):
    return row_terms(row)


def reject_title(title):
    title_upper = title.upper()
    rejected = ["ANIMAL", "VETERINARY", "HOMEOPATHIC", "LABEL: OTC", "KBROVET", "K-BROVET", "LIBROMIDE"]
    return any(term in title_upper for term in rejected)


def normalized_term(value):
    return re.sub(r"[^a-z0-9]+", " ", value.lower()).strip()


def candidate_is_relevant(row, candidate):
    original_title = candidate.get("title", "").lower()
    title = normalized_term(candidate.get("title", ""))
    generic = normalized_term(row["generic_name"])
    acceptable = [normalized_term(term) for term in row_terms(row)]
    acceptable = [term for term in acceptable if len(term) >= 5]
    if any(title.startswith(term) for term in acceptable):
        return True
    if f" {generic} " in f" {title} " and title.find(generic) < 35:
        return True
    original_index = original_title.find(row["generic_name"].lower())
    if original_index >= 0 and "," in original_title[:original_index]:
        return False
    if f" {generic} " in f" {title} ":
        return True
    return False


def score_candidate(row, candidate, boxed_text):
    title = candidate.get("title", "")
    title_lower = title.lower()
    generic = row["generic_name"].lower()
    score = 0
    if boxed_text:
        score += 10000
    for index, term in enumerate(row_terms(row)):
        if term.lower() in title_lower:
            score += 800 - index
    if generic in title_lower:
        score += 300
    if "injection" in row.get("formulations_available", "").lower() and "injection" in title_lower:
        score += 120
    if any(bad in title_lower for bad in ["repack", "unit dose", "kit"]):
        score -= 50
    score += parse_date(candidate.get("published_date", "")).toordinal() / 1000000
    return score


def source_string(candidate, search_terms, status):
    if not candidate:
        return f"FDA/DailyMed search on {REFRESH_DATE}: no current label found for terms [{'; '.join(search_terms)}]."
    setid = candidate["setid"]
    return (
        f"FDA/DailyMed SPL; status={status}; setid={setid}; "
        f"published={candidate.get('published_date', '')}; title={candidate.get('title', '')}; "
        f"url={DAILYMED_LABEL_URL.format(setid=setid)}"
    )


def select_label(row, refresh=False):
    search_terms = terms_for_row(row)
    candidates_by_setid = {}
    for setid in setids_from_existing_sources(row):
        try:
            xml_bytes = fetch_xml(setid, refresh=refresh)
            title = title_from_xml(xml_bytes)
        except Exception:
            title = ""
        candidates_by_setid[setid] = {"setid": setid, "title": title, "published_date": ""}
    for term in search_terms:
        for hit in search_spls(term, refresh=refresh)[:8]:
            title = hit.get("title", "")
            setid = hit.get("setid", "")
            if not setid or reject_title(title):
                continue
            if not candidate_is_relevant(row, hit):
                continue
            candidates_by_setid.setdefault(setid, hit)
            if len(candidates_by_setid) >= 24:
                break
        if len(candidates_by_setid) >= 24:
            break

    evaluated = []
    for candidate in candidates_by_setid.values():
        setid = candidate["setid"]
        try:
            xml_bytes = fetch_xml(setid, refresh=refresh)
        except Exception:
            continue
        if not candidate.get("title"):
            candidate["title"] = title_from_xml(xml_bytes)
        boxed_text, boxed_title, boxed_code = extract_boxed_warning(xml_bytes)
        evaluated.append(
            {
                "candidate": candidate,
                "boxed_text": boxed_text,
                "boxed_title": boxed_title,
                "boxed_code": boxed_code,
                "score": score_candidate(row, candidate, boxed_text),
            }
        )

    if not evaluated:
        return {
            "status": "no_current_fda_label",
            "warning": "No current FDA/DailyMed label identified.",
            "source": source_string(None, search_terms, "no_current_fda_label"),
            "candidate": {},
            "search_terms": search_terms,
            "boxed_title": "",
            "boxed_code": "",
        }

    selected = max(evaluated, key=lambda item: item["score"])
    candidate = selected["candidate"]
    if selected["boxed_text"]:
        return {
            "status": "boxed_warning_found",
            "warning": selected["boxed_text"],
            "source": source_string(candidate, search_terms, "boxed_warning_found"),
            "candidate": candidate,
            "search_terms": search_terms,
            "boxed_title": selected["boxed_title"],
            "boxed_code": selected["boxed_code"],
        }
    return {
        "status": "no_boxed_warning_in_selected_label",
        "warning": "No FDA boxed warning identified in selected current DailyMed label.",
        "source": source_string(candidate, search_terms, "no_boxed_warning_in_selected_label"),
        "candidate": candidate,
        "search_terms": search_terms,
        "boxed_title": "",
        "boxed_code": "",
    }


def add_source(existing):
    parts = split_semicolon(existing)
    if FDA_SOURCE not in parts:
        parts.append(FDA_SOURCE)
    return "; ".join(parts)


def build_fieldnames(fieldnames):
    fieldnames = [field for field in fieldnames if field not in FIELDNAMES_TO_INSERT]
    output = []
    inserted = False
    for field in fieldnames:
        output.append(field)
        if field == "year_fda_cleared":
            output.extend(FIELDNAMES_TO_INSERT)
            inserted = True
    if not inserted:
        output.extend(FIELDNAMES_TO_INSERT)
    return output


def read_rows():
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def write_outputs(fieldnames, rows, audit_rows):
    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    audit_fields = [
        "generic_name",
        "status",
        "fda_black_box_warning",
        "fda_black_box_warning_source",
        "fda_black_box_warning_verified",
        "dailymed_setid",
        "dailymed_published_date",
        "dailymed_title",
        "dailymed_url",
        "boxed_section_title",
        "boxed_section_code",
        "search_terms",
        "warning_sha256",
    ]
    with AUDIT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=audit_fields, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(audit_rows)


def update(refresh=False):
    fieldnames, rows = read_rows()
    fieldnames = build_fieldnames(fieldnames)
    audit_rows = []
    for index, row in enumerate(rows, 1):
        result = select_label(row, refresh=refresh)
        candidate = result["candidate"]
        warning = result["warning"]
        source = result["source"]
        row["fda_black_box_warning"] = warning
        row["fda_black_box_warning_source"] = source
        row["fda_black_box_warning_verified"] = REFRESH_DATE
        row["data_most_recently_refreshed"] = REFRESH_DATE
        row["evidence_sources"] = add_source(row.get("evidence_sources", ""))
        setid = candidate.get("setid", "")
        audit_rows.append(
            {
                "generic_name": row["generic_name"],
                "status": result["status"],
                "fda_black_box_warning": warning,
                "fda_black_box_warning_source": source,
                "fda_black_box_warning_verified": REFRESH_DATE,
                "dailymed_setid": setid,
                "dailymed_published_date": candidate.get("published_date", ""),
                "dailymed_title": candidate.get("title", ""),
                "dailymed_url": DAILYMED_LABEL_URL.format(setid=setid) if setid else "",
                "boxed_section_title": result.get("boxed_title", ""),
                "boxed_section_code": result.get("boxed_code", ""),
                "search_terms": "; ".join(result["search_terms"]),
                "warning_sha256": hashlib.sha256(warning.encode("utf-8")).hexdigest(),
            }
        )
        print(f"{index:02d}/{len(rows)} {row['generic_name']}: {result['status']}", flush=True)
    write_outputs(fieldnames, rows, audit_rows)
    return rows, audit_rows


def verify(refresh=False):
    _, rows = read_rows()
    audit_rows = list(csv.DictReader(AUDIT_PATH.open(newline="", encoding="utf-8"))) if AUDIT_PATH.exists() else []
    audit_by_name = {row["generic_name"]: row for row in audit_rows}
    errors = []
    for index, row in enumerate(rows, 1):
        result = select_label(row, refresh=refresh)
        audit = audit_by_name.get(row["generic_name"], {})
        expected_warning = normalize_for_compare(result["warning"])
        observed_warning = normalize_for_compare(row.get("fda_black_box_warning", ""))
        if expected_warning != observed_warning:
            errors.append(f"{row['generic_name']}: CSV warning does not match freshly extracted FDA/DailyMed warning")
        if normalize_for_compare(audit.get("fda_black_box_warning", "")) != observed_warning:
            errors.append(f"{row['generic_name']}: audit warning does not match CSV warning")
        if row.get("fda_black_box_warning_source", "") != result["source"]:
            errors.append(f"{row['generic_name']}: source metadata changed from current DailyMed extraction")
        print(f"verify {index:02d}/{len(rows)} {row['generic_name']}: {result['status']}", flush=True)
    if errors:
        print("\nERRORS")
        for error in errors:
            print(error)
        raise SystemExit(1)
    print(f"Verified {len(rows)} FDA boxed-warning rows against DailyMed extraction.")


def main():
    parser = argparse.ArgumentParser(description="Update and verify FDA/DailyMed boxed-warning text in ASM-list.csv.")
    parser.add_argument("--verify", action="store_true", help="Verify CSV/audit warnings against current DailyMed extraction.")
    parser.add_argument("--refresh", action="store_true", help="Refresh the local DailyMed cache before extraction.")
    args = parser.parse_args()
    if args.verify:
        verify(refresh=args.refresh)
    else:
        update(refresh=args.refresh)


if __name__ == "__main__":
    main()
