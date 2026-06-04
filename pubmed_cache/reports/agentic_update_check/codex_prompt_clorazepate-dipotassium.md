You are a Codex sub-agent auditing one anti-seizure medication CSV row.

Task:
- Verify each populated fact in the row against trusted sources.
- Verify alternate names and trade names; the same drug should not appear as a separate row just because an alias exists.
- Verify PubMed links for phase II/III placebo-controlled RCTs, including PMID, drug, trial design, and placebo control.
- Verify differential RR50, median percent change, and seizure-freedom values against the cited RCT/outcome evidence.
- Verify whether each cited row source actually supports the specific cell facts it is being used for.
- For FDA black box warnings, use FDA/openFDA, FDA labels, or Drugs@FDA only. DailyMed is not permissible for this field.
- For non-US drugs, EMA/eMC/SmPC, ILAE, Epilepsy Foundation, NIH/NCBI/PubMed, and peer-reviewed literature may support non-FDA facts.
- Do not edit files. Return only your final structured JSON answer.

Trusted source domains to use or cite:
- api.fda.gov
- www.fda.gov
- www.accessdata.fda.gov
- pubmed.ncbi.nlm.nih.gov
- www.ncbi.nlm.nih.gov
- clinicaltrials.gov
- www.ema.europa.eu
- ema.europa.eu
- www.medicines.org.uk
- www.epilepsy.com
- www.ilae.org
- nih.gov

When a row value is wrong or missing, propose exact replacement text and source URLs. Do not recommend deleting existing CSV data unless the evidence directly contradicts it; direct contradictions require user approval.

Use web search if needed. If web search is unavailable, mark affected checks as insufficient_evidence instead of guessing.

Developer audit instructions:
You are auditing one row of an anti-seizure medication CSV. Produce JSON only. Verify each populated fact field against trusted sources. For black box warnings, use FDA sources only (FDA/openFDA, FDA labels, Drugs@FDA); do not rely on DailyMed for black box warning verification. For non-US drugs, EMA, eMC/SmPC, ILAE, Epilepsy Foundation, and peer-reviewed literature can support non-FDA facts. Verify alternate names and trade names; a drug should not be represented as a separate row just because an alias exists, and important aliases should be listed in alternate_generic_names, trade_names, or pubmed_search_aliases. Check that named sources in the row actually support the specific cell facts they are cited for. For placebo-controlled phase II/III RCTs, verify PubMed links, PMIDs, drug assignment, placebo control, trial phase/design, and whether differential RR50, MPC, and seizure-freedom values match cited RCT/outcome evidence. If a fact is plausible but the provided row lacks a source named in evidence_sources or RCT fields, mark missing_source. When proposing a change, give exact replacement text and source URLs. Do not recommend removing existing data unless there is a direct contradiction.

Row bundle JSON:
{
  "audit_date": "2026-05-20",
  "csv_row": {
    "adverse_symptoms_percentages": "N/A 0%: FDA label lists drowsiness, dizziness, GI complaints, nervousness, blurred vision, dry mouth, headache, mental confusion, insomnia, skin rashes, fatigue, ataxia, irritability, diplopia, depression, tremor, and slurred speech without quantified incidence percentages.",
    "alternate_generic_names": "clorazepate",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "N/A - selected FDA label does not define clinically meaningful enzyme induction or inhibition.",
    "epilepsy_type": "Focal",
    "evidence_sources": "FDA Orange Book products file; FDA/DailyMed labeling",
    "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs in patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation (See WARNINGS and PRECAUTIONS ). The use of benzodiazepines, including Clorazepate dipotassium tablets, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of benzodiazepines commonly involve concomitant use of other medications, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes. Before prescribing Clorazepate dipotassium tablets and throughout out treatment, assess each patient’s risk for abuse, misuse, and addiction (See WARNINGS ). The continued use of benzodiazepines, including Clorazepate dipotassium tablets, may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Abrupt discontinuation or rapid dosage reduction of Clorazepate dipotassium tablets after continued use may precipitate acute withdrawal reactions, which can be life- threatening. To reduce the risk of withdrawal reactions, use a gradual taper to discontinue Clorazepate dipotassium tablets or reduce the dosage (See DOSAGE AND ADMINISTRATION and WARNINGS ).",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=boxed_warning_found; setid=919cbd07-f587-4005-acff-26213dd1d1fb; published=Mar 26, 2026; title=CLORAZEPATE DIPOTASSIUM TABLET [AUROLIFE PHARMA LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=919cbd07-f587-4005-acff-26213dd1d1fb",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "Unknown/limited",
    "filter_epilepsy_type": "Focal",
    "filter_formulation": "Tablet",
    "filter_mechanism": "GABA",
    "filter_metabolism": "Liver/hepatic",
    "filter_qt_effect": "No known meaningful QT effect",
    "filter_symptom_category": "CNS; GI; Neurologic; Psychiatric; Respiratory",
    "formulations_available": "Oral tablet currently; oral capsule historical/discontinued in Orange Book",
    "generic_name": "clorazepate dipotassium",
    "half_life_range": "Nordiazepam active metabolite about 40-50 h; FDA label also describes serum half-life as about 2 days.",
    "major_organ_for_metabolism": "Liver metabolism; excreted primarily in urine per FDA label.",
    "maximum_approved_daily_dose": "90 mg/day maximum recommended daily dose in selected FDA label.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Benzodiazepine prodrug to nordiazepam; FDA labeling describes benzodiazepine CNS depressant pharmacology and notes benzodiazepines interact at GABA-A sites.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "22.5 mg/day initial adjunctive partial-seizure dose for patients older than 12 years in selected FDA label.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "clorazepate; Tranxene; Tranxene SD; Gen-Xene",
    "qt_interval_effect": "No QT interval effect described in selected FDA label.",
    "rct_pubmed_verification_notes": "No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-19-2026; RCT section set to N/A per current scope.",
    "status_or_notes": "FDA Orange Book pre-1982 benzodiazepine ASM; FDA-labeled as adjunctive therapy in partial seizures and also for anxiety and acute alcohol withdrawal.",
    "trade_names": "Clorazepate Dipotassium; Gen-Xene; Tranxene; Tranxene SD",
    "typical_doses_per_day": "Adjunctive partial seizures: FDA label starts patients older than 12 years at 7.5 mg three times daily with gradual adjustment.",
    "year_fda_cleared": "Approved Prior to Jan 1, 1982 (FDA Orange Book)"
  },
  "existing_pubmed_links": [],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "N/A 0%: FDA label lists drowsiness, dizziness, GI complaints, nervousness, blurred vision, dry mouth, headache, mental confusion, insomnia, skin rashes, fatigue, ataxia, irritability, diplopia, depression, tremor, and slurred speech without quantified incidence percentages.",
    "alternate_generic_names": "clorazepate",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "N/A - selected FDA label does not define clinically meaningful enzyme induction or inhibition.",
    "epilepsy_type": "Focal",
    "evidence_sources": "FDA Orange Book products file; FDA/DailyMed labeling",
    "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs in patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation (See WARNINGS and PRECAUTIONS ). The use of benzodiazepines, including Clorazepate dipotassium tablets, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of benzodiazepines commonly involve concomitant use of other medications, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes. Before prescribing Clorazepate dipotassium tablets and throughout out treatment, assess each patient’s risk for abuse, misuse, and addiction (See WARNINGS ). The continued use of benzodiazepines, including Clorazepate dipotassium tablets, may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Abrupt discontinuation or rapid dosage reduction of Clorazepate dipotassium tablets after continued use may precipitate acute withdrawal reactions, which can be life- threatening. To reduce the risk of withdrawal reactions, use a gradual taper to discontinue Clorazepate dipotassium tablets or reduce the dosage (See DOSAGE AND ADMINISTRATION and WARNINGS ).",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=boxed_warning_found; setid=919cbd07-f587-4005-acff-26213dd1d1fb; published=Mar 26, 2026; title=CLORAZEPATE DIPOTASSIUM TABLET [AUROLIFE PHARMA LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=919cbd07-f587-4005-acff-26213dd1d1fb",
    "formulations_available": "Oral tablet currently; oral capsule historical/discontinued in Orange Book",
    "half_life_range": "Nordiazepam active metabolite about 40-50 h; FDA label also describes serum half-life as about 2 days.",
    "major_organ_for_metabolism": "Liver metabolism; excreted primarily in urine per FDA label.",
    "maximum_approved_daily_dose": "90 mg/day maximum recommended daily dose in selected FDA label.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Benzodiazepine prodrug to nordiazepam; FDA labeling describes benzodiazepine CNS depressant pharmacology and notes benzodiazepines interact at GABA-A sites.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "22.5 mg/day initial adjunctive partial-seizure dose for patients older than 12 years in selected FDA label.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "clorazepate; Tranxene; Tranxene SD; Gen-Xene",
    "qt_interval_effect": "No QT interval effect described in selected FDA label.",
    "trade_names": "Clorazepate Dipotassium; Gen-Xene; Tranxene; Tranxene SD",
    "typical_doses_per_day": "Adjunctive partial seizures: FDA label starts patients older than 12 years at 7.5 mg three times daily with gradual adjustment.",
    "year_fda_cleared": "Approved Prior to Jan 1, 1982 (FDA Orange Book)"
  },
  "generic_name": "clorazepate dipotassium",
  "instructions": {
    "black_box_warning_policy": "FDA sources only. DailyMed is not permissible for black box warning verification.",
    "required_row_source_policy": "Every retained fact should have a named trusted source in evidence_sources, mechanism_source, fda_black_box_warning_source, or the RCT/outcome link fields.",
    "trusted_sources": [
      "api.fda.gov",
      "www.fda.gov",
      "www.accessdata.fda.gov",
      "pubmed.ncbi.nlm.nih.gov",
      "www.ncbi.nlm.nih.gov",
      "clinicaltrials.gov",
      "www.ema.europa.eu",
      "ema.europa.eu",
      "www.medicines.org.uk",
      "www.epilepsy.com",
      "www.ilae.org",
      "nih.gov"
    ]
  },
  "latest_deterministic_update_check_findings_for_row": [
    {
      "column": "year_fda_cleared",
      "current_value": "Approved Prior to Jan 1, 1982 (FDA Orange Book)",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1982"
        ],
        "missing_terms": [
          "prior",
          "orange"
        ],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5",
      "generic_name": "clorazepate dipotassium",
      "id": "source_fact_concordance_problem-efaa2b79f8e9",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "year_fda_cleared could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "epilepsy_type",
      "current_value": "Focal",
      "details": {
        "checked": true,
        "matched_terms": [],
        "missing_numbers": [],
        "missing_terms": [
          "focal"
        ],
        "numbers": [],
        "ok": false,
        "terms": [
          "focal"
        ]
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5",
      "generic_name": "clorazepate dipotassium",
      "id": "source_fact_concordance_problem-345f0268becd",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "epilepsy_type could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "formulations_available",
      "current_value": "Oral tablet currently; oral capsule historical/discontinued in Orange Book",
      "details": {
        "checked": true,
        "matched_terms": [],
        "missing_numbers": [],
        "missing_terms": [
          "currently",
          "capsule",
          "historical",
          "discontinued",
          "orange"
        ],
        "numbers": [],
        "ok": false,
        "terms": [
          "currently",
          "capsule",
          "historical",
          "discontinued",
          "orange"
        ]
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5",
      "generic_name": "clorazepate dipotassium",
      "id": "source_fact_concordance_problem-7e0919890a95",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: formulations_available was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: formulations_available was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "formulations_available could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "qt_interval_effect",
      "current_value": "No QT interval effect described in selected FDA label.",
      "details": {
        "checked": true,
        "matched_terms": [],
        "missing_numbers": [],
        "missing_terms": [
          "interval"
        ],
        "numbers": [],
        "ok": false,
        "terms": [
          "interval"
        ]
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5",
      "generic_name": "clorazepate dipotassium",
      "id": "source_fact_concordance_problem-ddfd8b960c44",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "qt_interval_effect could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=boxed_warning_found; setid=919cbd07-f587-4005-acff-26213dd1d1fb; published=Mar 26, 2026; title=CLORAZEPATE DIPOTASSIUM TABLET [AUROLIFE PHARMA LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=919cbd07-f587-4005-acff-26213dd1d1fb",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5",
      "generic_name": "clorazepate dipotassium",
      "id": "fda_warning_metadata_refresh-9beafe880f5a",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs in patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation (See WARNINGS and PRECAUTIONS ). The use of benzodiazepines, including Clorazepate dipotassium tablets, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of benzodiazepines commonly involve concomitant use of other medications, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes. Before prescribing Clorazepate dipotassium tablets and throughout out treatment, assess each patient’s risk for abuse, misuse, and addiction (See WARNINGS ). The continued use of benzodiazepines, including Clorazepate dipotassium tablets, may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Abrupt discontinuation or rapid dosage reduction of Clorazepate dipotassium tablets after continued use may precipitate acute withdrawal reactions, which can be life- threatening. To reduce the risk of withdrawal reactions, use a gradual taper to discontinue Clorazepate dipotassium tablets or reduce the dosage (See DOSAGE AND ADMINISTRATION and WARNINGS ).",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=919cbd07-f587-4005-acff-26213dd1d1fb; effective_time=20260325; title=CLORAZEPATE DIPOTASSIUM / CLORAZEPATE DIPOTASSIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=919cbd07-f587-4005-acff-26213dd1d1fb; effective_time=20260325; title=CLORAZEPATE DIPOTASSIUM / CLORAZEPATE DIPOTASSIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [],
  "local_rct_audit_rows": [],
  "possible_duplicate_name_hits": []
}
