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
    "adverse_symptoms_percentages": "N/A 0%: FDA label lists anorexia, gastric upset, nausea, vomiting, cramps, abdominal pain, weight loss, diarrhea, drowsiness, headache, dizziness, euphoria, hiccups, irritability, hyperactivity, lethargy, fatigue, ataxia, rash/urticaria/SJS, blood dyscrasias, and psychiatric symptoms without quantified incidence percentages.",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "N/A - selected FDA label does not define clinically meaningful enzyme induction or inhibition; label notes interactions with other antiepileptic drug serum levels.",
    "epilepsy_type": "Absence",
    "evidence_sources": "FDA Orange Book products file; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6; published=Jul 16, 2024; title=ZARONTIN (ETHOSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "Unknown/limited",
    "filter_epilepsy_type": "Absence",
    "filter_formulation": "Capsule; Liquid",
    "filter_mechanism": "Other / unclear",
    "filter_metabolism": "Limited/unknown",
    "filter_qt_effect": "No known meaningful QT effect",
    "filter_symptom_category": "CNS; Dermatologic; GI; Hematologic; Neurologic; Psychiatric",
    "formulations_available": "Oral capsule; oral syrup/solution",
    "generic_name": "ethosuximide",
    "half_life_range": "N/A - selected FDA/DailyMed label does not provide a half-life value.",
    "major_organ_for_metabolism": "N/A - selected FDA/DailyMed label does not identify a major metabolic organ; label advises caution and monitoring with liver or renal disease.",
    "maximum_approved_daily_dose": "1500 mg/day; FDA label states doses exceeding 1.5 g/day should be used only under strict physician supervision.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "FDA labeling states ethosuximide suppresses the 3-cycle-per-second spike-wave activity of absence seizures and reduces attack frequency apparently by depression of motor cortex and elevation of CNS seizure threshold.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "250 mg/day age 3-6 years or 500 mg/day age 6 years and older initial labeled dose; titrate to control.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "Zarontin",
    "qt_interval_effect": "No QT interval effect described in selected FDA label.",
    "rct_pubmed_verification_notes": "No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-19-2026; RCT section set to N/A per current scope.",
    "status_or_notes": "FDA Orange Book pre-1982 succinimide ASM; FDA-labeled for control of absence (petit mal) epilepsy.",
    "trade_names": "Ethosuximide; Zarontin",
    "typical_doses_per_day": "Initial: 250 mg/day age 3-6 years or 500 mg/day age 6 years and older; increase by 250 mg every 4-7 days; optimal pediatric dose often 20 mg/kg/day per FDA label.",
    "year_fda_cleared": "Approved Prior to Jan 1, 1982 (FDA Orange Book)"
  },
  "existing_pubmed_links": [],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "N/A 0%: FDA label lists anorexia, gastric upset, nausea, vomiting, cramps, abdominal pain, weight loss, diarrhea, drowsiness, headache, dizziness, euphoria, hiccups, irritability, hyperactivity, lethargy, fatigue, ataxia, rash/urticaria/SJS, blood dyscrasias, and psychiatric symptoms without quantified incidence percentages.",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "N/A - selected FDA label does not define clinically meaningful enzyme induction or inhibition; label notes interactions with other antiepileptic drug serum levels.",
    "epilepsy_type": "Absence",
    "evidence_sources": "FDA Orange Book products file; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6; published=Jul 16, 2024; title=ZARONTIN (ETHOSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6",
    "formulations_available": "Oral capsule; oral syrup/solution",
    "half_life_range": "N/A - selected FDA/DailyMed label does not provide a half-life value.",
    "major_organ_for_metabolism": "N/A - selected FDA/DailyMed label does not identify a major metabolic organ; label advises caution and monitoring with liver or renal disease.",
    "maximum_approved_daily_dose": "1500 mg/day; FDA label states doses exceeding 1.5 g/day should be used only under strict physician supervision.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "FDA labeling states ethosuximide suppresses the 3-cycle-per-second spike-wave activity of absence seizures and reduces attack frequency apparently by depression of motor cortex and elevation of CNS seizure threshold.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "250 mg/day age 3-6 years or 500 mg/day age 6 years and older initial labeled dose; titrate to control.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "Zarontin",
    "qt_interval_effect": "No QT interval effect described in selected FDA label.",
    "trade_names": "Ethosuximide; Zarontin",
    "typical_doses_per_day": "Initial: 250 mg/day age 3-6 years or 500 mg/day age 6 years and older; increase by 250 mg every 4-7 days; optimal pediatric dose often 20 mg/kg/day per FDA label.",
    "year_fda_cleared": "Approved Prior to Jan 1, 1982 (FDA Orange Book)"
  },
  "generic_name": "ethosuximide",
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
      "column": "maximum_approved_daily_dose",
      "current_value": "1500 mg/day; FDA label states doses exceeding 1.5 g/day should be used only under strict physician supervision.",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1500"
        ],
        "missing_terms": [
          "states",
          "strict"
        ],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5",
      "generic_name": "ethosuximide",
      "id": "source_fact_concordance_problem-2cd845e7b7be",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "maximum_approved_daily_dose could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "year_fda_cleared",
      "current_value": "Approved Prior to Jan 1, 1982 (FDA Orange Book)",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1982"
        ],
        "missing_terms": [
          "orange"
        ],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5",
      "generic_name": "ethosuximide",
      "id": "source_fact_concordance_problem-f644fe6180da",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "year_fda_cleared could not be verified against the selected FDA/openFDA label."
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
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5",
      "generic_name": "ethosuximide",
      "id": "source_fact_concordance_problem-48f9a032d9e2",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "qt_interval_effect could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6; published=Jul 16, 2024; title=ZARONTIN (ETHOSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5",
      "generic_name": "ethosuximide",
      "id": "fda_warning_metadata_refresh-183ee13cd841",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "No FDA boxed warning identified in selected current FDA/openFDA label.",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=0e008f33-70a1-4bc6-b3a0-d45214418ab6; effective_time=20240715; title=Zarontin / ETHOSUXIMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=0e008f33-70a1-4bc6-b3a0-d45214418ab6; effective_time=20240715; title=Zarontin / ETHOSUXIMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [],
  "local_rct_audit_rows": [
    {
      "first_author": "Diezi",
      "generic_name": "ethosuximide",
      "label": "",
      "pmid": "36537292",
      "pub_types": "Randomized Controlled Trial; Clinical Trial, Phase I; Journal Article; Research Support, Non-U.S. Gov't",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "An innovative ethosuximide granule formulation designed for pediatric use: Comparative pharmacokinetics, safety, tolerability, and palatability profile versus reference syrup.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/36537292/",
      "year": "2023"
    },
    {
      "first_author": "Jiang",
      "generic_name": "ethosuximide",
      "label": "",
      "pmid": "31374046",
      "pub_types": "Clinical Trial Protocol; Journal Article",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "A statistical analysis plan for a randomized clinical trial to evaluate the efficacy and safety of ethosuximide in patients with treatment-resistant depression.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31374046/",
      "year": "2019"
    }
  ],
  "possible_duplicate_name_hits": []
}
