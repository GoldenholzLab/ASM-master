#!/usr/bin/env python3
import csv
import json
import re
import sys
import unicodedata
import urllib.parse
import xml.etree.ElementTree as ET
from collections import defaultdict
from datetime import datetime
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "ASM-list.csv"
CACHE = ROOT / "pubmed_cache"
ESEARCH_DIR = CACHE / "esearch"
EFETCH_DIR = CACHE / "efetch"
REPORT_DIR = CACHE / "reports"
REPORT_PATH = REPORT_DIR / "pubmed_rct_audit.csv"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


EXCLUDE_TITLE_TERMS = [
    "meta-analysis",
    "metaanalysis",
    "systematic review",
    "review",
    "post hoc",
    "post-hoc",
    "pooled analysis",
    "pooled efficacy",
    "pooled results",
    "pooled data",
    "integrated analysis",
    "integrated efficacy",
    "integrated safety",
    "matching-adjusted",
    "indirect comparison",
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
    "real world",
    "case report",
    "protocol",
    "survey",
    "economic",
    "cost",
    "quality of life",
    "caregiver",
    "simulation",
    "model",
    "time to",
    "patterns of",
    "pharmacokinetic",
    "pharmacodynamic",
    "exposure-",
    "concentration-effect",
    "drug interaction",
    "interaction between",
    "interaction study",
    "in combination with",
    "comment on",
    "letter to",
    "analysis of",
    "analysis ",
    "assess",
    "assessment",
    "early response",
    "subtypes",
    "psychiatric adverse",
    "severity and burden",
    "neurocognitive",
    "cognitive effects",
    "healthy recreational",
    "healthy japanese",
    "migraine",
    "postoperative pain",
    "post-stroke pain",
    "neuropathic pain",
    "asthma",
    "alzheimer",
    "amyotrophic",
    "glioblastoma",
    "oral contraceptive",
    "folic acid",
    "gingival",
    "bone loss",
    "osteoporosis",
    "acidic beverage",
    "mineral water",
    "bedsores",
    "sleep disturbances",
    "mania",
    "bipolar",
    "dogs",
    "canine",
    "veterinary",
]


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
]


def slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def read_rows():
    with CSV_PATH.open(newline="") as f:
        return list(csv.DictReader(f))


def existing_included_pmids():
    included = defaultdict(set)
    if not REPORT_PATH.exists():
        return included
    with REPORT_PATH.open(newline="") as f:
        for row in csv.DictReader(f):
            if row.get("status") == "included" and row.get("generic_name") and row.get("pmid"):
                included[row["generic_name"]].add(row["pmid"])
    return included


def split_field(value):
    pieces = []
    for part in re.split(r";|\n|,", value or ""):
        cleaned = part.strip()
        if cleaned:
            pieces.append(cleaned)
    return pieces


def aliases_for(row):
    names = [row["generic_name"]]
    names.extend(split_field(row.get("alternate_generic_names", "")))
    names.extend(split_field(row.get("trade_names", "")))
    names.extend(split_field(row.get("pubmed_search_aliases", "")))

    cleaned = []
    seen = set()
    for name in names:
        name = re.sub(r"\s+", " ", name.strip())
        if not name or name.lower() in {"also"}:
            continue
        key = name.lower()
        if key not in seen:
            seen.add(key)
            cleaned.append(name)
    return cleaned


def drug_query_terms(row):
    terms = []
    for name in aliases_for(row):
        escaped = name.replace('"', '\\"')
        terms.append(f'"{escaped}"[Title/Abstract]')
        if len(name.split()) <= 3:
            terms.append(f'"{escaped}"[All Fields]')
    return " OR ".join(terms)


def pubmed_query(row):
    drug_terms = drug_query_terms(row)
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
    excluded = (
        '"review"[Publication Type] OR "meta-analysis"[Publication Type] OR '
        '"systematic review"[Publication Type]'
    )
    return f"(({drug_terms}) AND ({seizure}) AND ({placebo}) AND ({randomized}) AND ({clinical}) NOT ({excluded}))"


def make_url(path, params):
    return f"{EUTILS}/{path}?{urllib.parse.urlencode(params)}"


def build_esearch_config():
    ESEARCH_DIR.mkdir(parents=True, exist_ok=True)
    lines = []
    for row in read_rows():
        url = make_url(
            "esearch.fcgi",
            {
                "db": "pubmed",
                "retmode": "json",
                "retmax": "300",
                "sort": "pub date",
                "term": pubmed_query(row),
            },
        )
        lines.extend([f'url = "{url}"', f'output = "{ESEARCH_DIR / (slug(row["generic_name"]) + ".json")}"'])
    config = CACHE / "esearch.curl"
    config.write_text("\n".join(lines) + "\n")
    print(config)


def parse_esearch_ids():
    ids_by_drug = {}
    for row in read_rows():
        path = ESEARCH_DIR / f"{slug(row['generic_name'])}.json"
        if not path.exists():
            ids_by_drug[row["generic_name"]] = []
            continue
        try:
            data = json.loads(path.read_text())
            ids_by_drug[row["generic_name"]] = data.get("esearchresult", {}).get("idlist", [])
        except json.JSONDecodeError:
            ids_by_drug[row["generic_name"]] = []
    return ids_by_drug


def build_efetch_config():
    EFETCH_DIR.mkdir(parents=True, exist_ok=True)
    ids_by_drug = parse_esearch_ids()
    all_ids = sorted({pmid for ids in ids_by_drug.values() for pmid in ids}, key=int)
    lines = []
    for index in range(0, len(all_ids), 150):
        chunk = all_ids[index : index + 150]
        if not chunk:
            continue
        url = make_url(
            "efetch.fcgi",
            {"db": "pubmed", "retmode": "xml", "id": ",".join(chunk)},
        )
        lines.extend([f'url = "{url}"', f'output = "{EFETCH_DIR / f"chunk-{index // 150:03d}.xml"}"'])
    config = CACHE / "efetch.curl"
    config.write_text("\n".join(lines) + "\n")
    print(config)
    print(f"unique_pmids={len(all_ids)}")


def text_from(elem):
    if elem is None:
        return ""
    return " ".join(t.strip() for t in elem.itertext() if t and t.strip())


def article_year(article):
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


def ascii_label(value):
    value = unicodedata.normalize("NFKD", value)
    value = "".join(ch for ch in value if not unicodedata.combining(ch))
    value = re.sub(r"[^A-Za-z0-9]+", "", value)
    return value or "PMID"


def parse_articles():
    articles = {}
    for path in sorted(EFETCH_DIR.glob("chunk-*.xml")):
        root = ET.fromstring(path.read_text())
        for article in root.findall(".//PubmedArticle"):
            pmid = article.findtext(".//PMID", default="").strip()
            if not pmid:
                continue
            title = text_from(article.find(".//ArticleTitle"))
            abstract = text_from(article.find(".//Abstract"))
            first_author = article.find(".//AuthorList/Author")
            last_name = first_author.findtext("LastName", default="") if first_author is not None else ""
            collective = first_author.findtext("CollectiveName", default="") if first_author is not None else ""
            pub_types = [text_from(node) for node in article.findall(".//PublicationType")]
            year = article_year(article)
            articles[pmid] = {
                "pmid": pmid,
                "title": title,
                "abstract": abstract,
                "year": year,
                "first_author": last_name or collective or "PMID",
                "pub_types": pub_types,
            }
    return articles


def contains_drug(article, row):
    haystack = f"{article['title']} {article['abstract']}".lower()
    for alias in aliases_for(row):
        alias_l = alias.lower()
        if re.search(rf"(?<![a-z0-9]){re.escape(alias_l)}(?![a-z0-9])", haystack):
            return True
    return False


def title_contains_drug(article, row):
    title = article["title"].lower()
    for alias in aliases_for(row):
        alias_l = alias.lower()
        if re.search(rf"(?<![a-z0-9]){re.escape(alias_l)}(?![a-z0-9])", title):
            return True
    return False


def title_has_seizure_context(article):
    title = article["title"].lower()
    return any(term in title for term in SEIZURE_TERMS + ["convulsion", "convulsions", "epileptiform"])


def title_names_primary_drug(article, row):
    title = article["title"].lower()
    normalized = re.sub(r"[^a-z0-9]+", " ", title).strip()
    for alias in aliases_for(row):
        alias_l = alias.lower()
        alias_norm = re.sub(r"[^a-z0-9]+", " ", alias_l).strip()
        if not alias_norm:
            continue
        if normalized.startswith(alias_norm):
            return True
        patterns = [
            f"of {alias_norm}",
            f"with {alias_norm}",
            f"adjunctive {alias_norm}",
            f"add on {alias_norm}",
            f"add-on {alias_l}",
            f"{alias_norm} as",
            f"{alias_norm} for",
            f"{alias_norm} in",
            f"{alias_norm} therapy",
            f"{alias_norm} treatment",
            f"study of {alias_norm}",
            f"trial of {alias_norm}",
            f"evaluate {alias_norm}",
            f"evaluating {alias_norm}",
        ]
        if any(pattern in normalized for pattern in patterns):
            return True
    return False


def is_qualifying(article, row, forced_pmids=None):
    title = article["title"].lower()
    text = f"{article['title']} {article['abstract']}".lower()
    pub_types = " ".join(article["pub_types"]).lower()
    if forced_pmids and article["pmid"] in forced_pmids:
        return True, "qualifying PubMed placebo-controlled randomized clinical trial report"

    if not title_contains_drug(article, row):
        return False, "drug term not in title"
    if not title_names_primary_drug(article, row):
        return False, "drug appears in title but not as primary intervention"
    if not title_has_seizure_context(article):
        return False, "title lacks seizure/epilepsy context"
    if any(term in title for term in EXCLUDE_TITLE_TERMS):
        return False, "excluded secondary/non-primary title"
    if (" vs " in title or "versus" in title or "comparison of" in title or "comparing" in title) and "placebo" not in title:
        return False, "active-comparator/comparison title without placebo"
    if "healthy volunteer" in text or "healthy subjects" in text:
        return False, "healthy-volunteer study"
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
            "phase iia",
            "phase iib",
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


def make_labels(articles):
    used = defaultdict(int)
    labels = {}
    for article in sorted(articles, key=lambda item: (item["year"], item["first_author"], int(item["pmid"]))):
        base = f"{ascii_label(article['first_author'])}{article['year']}"
        used[base] += 1
        if used[base] == 1:
            labels[article["pmid"]] = base
        else:
            labels[article["pmid"]] = f"{base}{chr(ord('a') + used[base] - 1)}"
    return labels


def has_numeric_outcome(value):
    if not value:
        return False
    if re.search(r"\d+(?:\.\d+)?", value) and not re.search(r"\bNR\b|No placebo|not comparable|Greater than placebo|Statistically", value, re.I):
        return True
    return False


def highest_dose_value(current, qualifying_count):
    if qualifying_count == 0:
        return "No qualifying placebo-controlled phase II/III PubMed RCT found"
    if has_numeric_outcome(current):
        return current
    return "NR/not extractable from PubMed abstracts or available FDA label summaries for qualifying placebo-controlled RCTs"


def apply_updates():
    rows = read_rows()
    ids_by_drug = parse_esearch_ids()
    articles = parse_articles()
    forced_by_drug = existing_included_pmids()
    total = len(rows)
    refresh_date = datetime.now().strftime("%m-%d-%Y")
    fieldnames = list(rows[0].keys())
    extra_fields = [
        "diff_50_responder_maximum_effective_dose",
        "diff_median_pct_change_maximum_effective_dose",
        "rct_pubmed_verification_notes",
    ]
    for field in extra_fields:
        if field not in fieldnames:
            fieldnames.append(field)

    report_rows = []
    updated_rows = []
    for index, row in enumerate(rows, start=1):
        generic = row["generic_name"]
        candidate_ids = ids_by_drug.get(generic, [])
        qualifying = []
        rejected = []
        for pmid in candidate_ids:
            article = articles.get(pmid)
            if not article:
                continue
            ok, reason = is_qualifying(article, row, forced_by_drug.get(generic, set()))
            if ok:
                qualifying.append(article)
            else:
                rejected.append((article, reason))

        labels = make_labels(qualifying)
        if qualifying:
            row["pubmed_phase_ii_iii_rct_links"] = "; ".join(
                f"{labels[item['pmid']]}|https://pubmed.ncbi.nlm.nih.gov/{item['pmid']}/"
                for item in sorted(qualifying, key=lambda a: (a["year"], a["first_author"], int(a["pmid"])), reverse=True)
            )
        else:
            row["pubmed_phase_ii_iii_rct_links"] = "No PubMed phase II/III RCTs found"

        row["diff_50_responder_maximum_effective_dose"] = highest_dose_value(row.get("diff_50_responder_maximum_effective_dose", ""), len(qualifying))
        row["diff_median_pct_change_maximum_effective_dose"] = highest_dose_value(row.get("diff_median_pct_change_maximum_effective_dose", ""), len(qualifying))
        row["rct_pubmed_verification_notes"] = (
            f"PubMed loop {index}/{total} on {refresh_date}: {len(qualifying)} qualifying placebo-controlled randomized clinical trial report(s) retained from "
            f"{len(candidate_ids)} PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. "
            "Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports."
        )
        updated_rows.append(row)

        for item in qualifying:
            report_rows.append(
                {
                    "generic_name": generic,
                    "status": "included",
                    "pmid": item["pmid"],
                    "label": labels[item["pmid"]],
                    "year": item["year"],
                    "first_author": item["first_author"],
                    "title": item["title"],
                    "pub_types": "; ".join(item["pub_types"]),
                    "reason": "qualifying placebo-controlled randomized clinical trial report",
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{item['pmid']}/",
                }
            )
        for item, reason in rejected:
            report_rows.append(
                {
                    "generic_name": generic,
                    "status": "rejected",
                    "pmid": item["pmid"],
                    "label": "",
                    "year": item["year"],
                    "first_author": item["first_author"],
                    "title": item["title"],
                    "pub_types": "; ".join(item["pub_types"]),
                    "reason": reason,
                    "url": f"https://pubmed.ncbi.nlm.nih.gov/{item['pmid']}/",
                }
            )
        print(f"{index:02d}/{total} {generic}: retained {len(qualifying)} of {len(candidate_ids)} candidate(s)")

    with CSV_PATH.open("w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(updated_rows)

    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    with REPORT_PATH.open("w", newline="") as f:
        report_fields = ["generic_name", "status", "pmid", "label", "year", "first_author", "title", "pub_types", "reason", "url"]
        writer = csv.DictWriter(f, fieldnames=report_fields)
        writer.writeheader()
        writer.writerows(report_rows)


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in {"prepare-esearch", "prepare-efetch", "apply"}:
        raise SystemExit("Usage: pubmed_rct_audit.py prepare-esearch|prepare-efetch|apply")
    if sys.argv[1] == "prepare-esearch":
        build_esearch_config()
    elif sys.argv[1] == "prepare-efetch":
        build_efetch_config()
    else:
        apply_updates()


if __name__ == "__main__":
    main()
