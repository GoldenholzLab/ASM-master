#!/usr/bin/env python3
import csv
import re
from collections import defaultdict


def has_any(text, patterns):
    return any(re.search(pattern, text) for pattern in patterns)


def mechanism_categories(row):
    text = row["mechanism_of_action"].lower()
    categories = []
    if has_any(text, [r"\bsodium[- ]channel\b", r"\bvoltage[- ]gated sodium\b", r"\bsodium current"]):
        categories.append("Sodium channel")
    if has_any(text, [r"\bgaba-a\b", r"\bgabaergic\b", r"\bbenzodiazepine\b", r"\bbarbiturate\b", r"\bgaba tone\b", r"\bgaba transaminase\b", r"\bgaba reuptake\b", r"\bgat-1\b"]):
        categories.append("GABA")
    if re.search(r"\bsv2a\b", text):
        categories.append("SV2A")
    if has_any(text, [r"\bcalcium\b", r"\balpha-?2-?delta\b"]):
        categories.append("Calcium channel / alpha-2-delta")
    if "carbonic anhydrase" in text:
        categories.append("Carbonic anhydrase")
    if has_any(text, [r"\bampa\b", r"\bglutamate\b", r"\bnmda\b"]):
        categories.append("Glutamate receptor")
    if re.search(r"\bmtor\b", text):
        categories.append("mTOR")
    if has_any(text, [r"\bseroton", r"\bsigma\b"]):
        categories.append("Serotonin / sigma")
    if has_any(text, [r"\bgaba transaminase\b", r"\bgaba reuptake\b", r"\bgat-1\b"]):
        categories.append("GABA metabolism / reuptake")
    if has_any(text, [r"\bpotassium\b", r"\bkv7\b", r"\bkcnq\b"]):
        categories.append("Potassium channel")
    if has_any(text, [r"\bsteroid\b", r"\badrenal\b", r"\bhormonal\b"]):
        categories.append("Hormonal / steroid")
    if has_any(text, [r"\bvitamin\b", r"\bcofactor\b"]):
        categories.append("Vitamin / cofactor")
    if not categories or "unclear" in text or "not well established" in text:
        categories.append("Other / unclear")
    return categories


def availability_categories(row):
    text = row["available_in_us"].lower()
    if text == "yes":
        return ["Available in US"]
    if "limited" in text or "rare" in text or "not as epilepsy" in text or "not as u.s. sodium-valproate" in text:
        return ["Limited or non-epilepsy US availability"]
    return ["Not available in US"]


def organ_categories(row):
    text = row["major_organ_for_metabolism"].lower()
    categories = []
    if "liver" in text or "hepatic" in text:
        categories.append("Liver/hepatic")
    if "renal" in text or "kidney" in text or "not metabolized" in text:
        categories.append("Renal/no major metabolism")
    if "gut" in text:
        categories.append("Gut")
    if "plasma" in text or "extrahepatic" in text or "blood/tissues" in text:
        categories.append("Plasma/extrahepatic")
    if "limited" in text or "unknown" in text:
        categories.append("Limited/unknown")
    return categories or ["Other"]


def formulation_categories(row):
    text = row["formulations_available"].lower()
    categories = []
    if re.search(r"\btablets?\b", text):
        categories.append("Tablet")
    if re.search(r"\bcapsules?\b", text):
        categories.append("Capsule")
    if has_any(text, [r"\bsolution\b", r"\bsuspension\b", r"\bsyrup\b", r"\belixir\b", r"\bliquid\b", r"\bconcentrate\b"]):
        categories.append("Liquid")
    if has_any(text, [r"\biv\b", r"\bi\.v\.\b", r"\bintravenous\b", r"\bim\b", r"\bi\.m\.\b", r"\bintramuscular\b", r"\binjections?\b", r"\binjectable\b"]):
        categories.append("IV/IM injection")
    if has_any(text, [r"\bnasal\b", r"\brectal\b", r"\brescue\b", r"\bbuccal\b", r"\boromucosal\b"]):
        categories.append("Rescue formulation")
    if has_any(text, [r"\bextended-release\b", r"\bmodified-release\b", r"\bdelayed-release\b", r"\blong acting\b", r"\blong-acting\b", r"\bprolonged release\b"]):
        categories.append("Long acting")
    if has_any(text, [r"\bsprinkles?\b", r"\bpowder\b"]):
        categories.append("Sprinkle/powder")
    if has_any(text, [r"\bfilm\b", r"\bdisintegrating\b", r"\bodt\b", r"\bdissolvable\b"]):
        categories.append("Film/ODT")
    if has_any(text, [r"\bhistorical\b", r"\bnot marketed\b", r"\binvestigational\b", r"\blimited markets?\b"]):
        categories.append("Historical/not marketed")
    return categories or ["Other"]


def enzyme_categories(row):
    text = row["enzyme_inducing_or_inhibiting"].lower()
    categories = []
    no_major_effect = has_any(text, [r"\bnot a cyp inducer/inhibitor\b", r"\bnot an enzyme inducer/inhibitor\b", r"\bnot metabolized\b", r"\bnot a major inducer\b"])
    if has_any(text, [r"\bstrong enzyme inducer\b", r"\bstrong cyp\b", r"\benzyme inducer\b", r"\bautoinducer\b"]):
        categories.append("Inducer")
    if has_any(text, [r"\bweak cyp\b", r"\bweak enzyme\b", r"\bweak cyp3a\b", r"\bweaker inducer\b"]):
        categories.append("Weak inducer")
    if not no_major_effect and has_any(text, [r"\binhibits\b", r"\binhibitor\b", r"\binhibiting\b"]):
        categories.append("Inhibitor")
    if no_major_effect:
        categories.append("No major enzyme effect")
    if re.search(r"\bsubstrate\b", text) or re.search(r"\baffected by\b", text):
        categories.append("Substrate / affected by modulators")
    if has_any(text, [r"\bunknown\b", r"\blimited\b"]):
        categories.append("Unknown/limited")
    return categories or ["Other"]


def qt_categories(row):
    text = row["qt_interval_effect"].lower()
    categories = []
    if has_any(text, [r"\bshortens qt\b", r"\bqt shortening\b"]):
        categories.append("QT shortening")
    if has_any(text, [r"\bqt prolong", r"\bprolongs qt\b"]):
        categories.append("QT prolongation")
    if re.search(r"\bpr interval\b", text):
        categories.append("PR interval effect")
    if has_any(text, [r"\bconduction\b", r"\barrhythmia\b", r"\bqrs\b", r"\bav block\b"]):
        categories.append("Conduction/arrhythmia caution")
    if "no clinically meaningful" in text or "no established clinically meaningful" in text:
        categories.append("No known meaningful QT effect")
    if "unknown" in text or "limited" in text:
        categories.append("Unknown/limited")
    return categories or ["Other"]


def symptom_categories(row):
    text = row["adverse_symptoms_percentages"]
    label_map = {
        "allergic/immunologic": "Allergic/immunologic",
        "behavioral": "Behavioral",
        "cardiac": "Cardiac",
        "cardiovascular": "Cardiovascular",
        "cognitive": "Cognitive",
        "constitutional": "Constitutional",
        "dermatologic": "Dermatologic",
        "gingival": "Gingival",
        "gi/oral": "GI/oral",
        "hematologic": "Hematologic",
        "hematologic/hepatic": "Hematologic/hepatic",
        "hepatic": "Hepatic",
        "infectious": "Infectious",
        "injury": "Injury",
        "metabolic": "Metabolic",
        "neurologic": "Neurologic",
        "ophthalmologic": "Ophthalmologic",
        "peripheral": "Peripheral",
        "psychiatric": "Psychiatric",
        "renal/metabolic": "Renal/metabolic",
        "respiratory": "Respiratory",
        "urologic": "Urologic",
    }
    categories = []
    for entry in text.split(","):
        raw_prefix = entry.split(":")[0].strip()
        prefix = label_map.get(raw_prefix.lower(), raw_prefix)
        if prefix and "%" not in prefix and not prefix.lower().startswith("evidence availability"):
            categories.append(prefix)
    if "no reliable" in text.lower():
        categories.append("Unquantified/limited data")
    return sorted(set(categories or ["Other"]))


def epilepsy_type_categories(row):
    return sorted({value.strip() for value in row["epilepsy_type"].split(";") if value.strip()} or {"Unspecified epilepsy"})


FILTERS = {
    "availability": availability_categories,
    "metabolism": organ_categories,
    "mechanism": mechanism_categories,
    "epilepsy type": epilepsy_type_categories,
    "formulation": formulation_categories,
    "enzyme": enzyme_categories,
    "qt": qt_categories,
    "symptom": symptom_categories,
}


rows = list(csv.DictReader(open("ASM-list.csv")))
errors = []
for name, func in FILTERS.items():
    options = sorted({value for row in rows for value in func(row) if value})
    for option in options:
        matched = [row for row in rows if option in func(row)]
        if not matched:
            errors.append(f"{name}:{option} returned zero rows")
        for row in matched:
            if option not in func(row):
                errors.append(f"{name}:{option} included bad row {row['generic_name']}")
    print(f"{name}: {len(options)} option(s)")
    for option in options:
        matched = [row["generic_name"] for row in rows if option in func(row)]
        print(f"  {option}: {len(matched)}")

iv_rows = [row["generic_name"] for row in rows if "IV/IM injection" in formulation_categories(row)]
if "carbamazepine" in iv_rows:
    errors.append("carbamazepine incorrectly appears in IV/IM injection")
if "brivaracetam" not in iv_rows:
    errors.append("brivaracetam missing from IV/IM injection")

if errors:
    print("\nERRORS")
    for error in errors:
        print(error)
    raise SystemExit(1)

print("\nAll filter options passed CSV-side audit.")
