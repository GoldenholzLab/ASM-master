#!/usr/bin/env python3
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "ASM-list.csv"
AUDIT_PATH = ROOT / "pubmed_cache" / "reports" / "mechanism_audit.csv"
MOA_FIELDS = [
    "mechanism_of_action",
    "mechanism_source",
    "mechanism_source_tier",
    "mechanism_confidence",
]
NAME_KEY = "generic_name"
REFRESH_KEY = "data_most_recently_refreshed"


def split_sources(value):
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def source_union(existing, additions):
    seen = []
    for source in split_sources(existing) + split_sources(additions):
        if source and source not in seen:
            seen.append(source)
    return "; ".join(seen)


def read_dicts(path):
    with path.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        return reader.fieldnames or [], list(reader)


def main():
    if not AUDIT_PATH.exists():
        raise SystemExit(f"Missing mechanism audit source: {AUDIT_PATH.relative_to(ROOT)}")

    fieldnames, rows = read_dicts(CSV_PATH)
    audit_fieldnames, audit_rows = read_dicts(AUDIT_PATH)
    missing_audit_fields = [field for field in [NAME_KEY, *MOA_FIELDS] if field not in audit_fieldnames]
    if missing_audit_fields:
        raise SystemExit(f"Mechanism audit is missing field(s): {', '.join(missing_audit_fields)}")

    audit_by_name = {row[NAME_KEY]: row for row in audit_rows if row.get(NAME_KEY)}
    missing = sorted(row[NAME_KEY] for row in rows if row.get(NAME_KEY) not in audit_by_name)
    extra = sorted(name for name in audit_by_name if name not in {row.get(NAME_KEY) for row in rows})
    if missing or extra:
        raise SystemExit(f"Mechanism audit mismatch. Missing={missing}; extra={extra}")

    for row in rows:
        audit = audit_by_name[row[NAME_KEY]]
        for field in MOA_FIELDS:
            row[field] = audit.get(field, "")
        row["evidence_sources"] = source_union(row.get("evidence_sources", ""), audit.get("mechanism_source", ""))
        if audit.get(REFRESH_KEY):
            row[REFRESH_KEY] = audit[REFRESH_KEY]

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    print(f"Updated {len(rows)} mechanism rows from {AUDIT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
