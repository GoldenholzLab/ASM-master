#!/usr/bin/env python3
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "ASM-list.csv"
FILTER_PREFIX = "filter_"
NAME_KEY = "generic_name"


def split_values(value):
    return [item.strip() for item in (value or "").split(";") if item.strip()]


with CSV_PATH.open(newline="") as handle:
    reader = csv.DictReader(handle)
    rows = list(reader)
    fieldnames = reader.fieldnames or []

filter_columns = [field for field in fieldnames if field.startswith(FILTER_PREFIX)]
errors = []

if not rows:
    errors.append("ASM-list.csv has no data rows")

if NAME_KEY not in fieldnames:
    errors.append(f"ASM-list.csv is missing required column {NAME_KEY}")

if not filter_columns:
    errors.append(f"ASM-list.csv has no {FILTER_PREFIX} columns")

for row_number, row in enumerate(rows, start=2):
    name = (row.get(NAME_KEY) or "").strip() or f"row {row_number}"
    if not (row.get(NAME_KEY) or "").strip():
        errors.append(f"row {row_number} is missing {NAME_KEY}")
    for column in filter_columns:
        if not split_values(row.get(column, "")):
            errors.append(f"{name} has no values in {column}")

for column in filter_columns:
    options = sorted({value for row in rows for value in split_values(row.get(column, ""))})
    print(f"{column}: {len(options)} option(s)")
    if not options:
        errors.append(f"{column} has no filter options")
        continue

    for option in options:
        matched = [row for row in rows if option in split_values(row.get(column, ""))]
        print(f"  {option}: {len(matched)}")
        if not matched:
            errors.append(f"{column}:{option} returned zero rows")
        for row in matched:
            if option not in split_values(row.get(column, "")):
                errors.append(f"{column}:{option} included bad row {row.get(NAME_KEY, '')}")

if errors:
    print("\nERRORS")
    for error in errors:
        print(error)
    raise SystemExit(1)

print("\nAll CSV-defined filter options passed audit.")
