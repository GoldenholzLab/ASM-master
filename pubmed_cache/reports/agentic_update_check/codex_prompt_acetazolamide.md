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
    "adverse_symptoms_percentages": "N/A 0%: FDA label lists paresthesia, hearing dysfunction/tinnitus, loss of appetite, taste alteration, GI disturbances, polyuria, drowsiness, confusion, rash, blood dyscrasias, electrolyte imbalance, and metabolic acidosis without quantified incidence percentages.",
    "alternate_generic_names": "acetazolamide sodium",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "No broad enzyme induction/inhibition described in selected FDA label; label notes interactions including altered phenytoin metabolism and reduced primidone/metabolite concentrations through decreased absorption.",
    "epilepsy_type": "Centrencephalic epilepsies; Absence; Generalized; Myoclonic; Adjunctive nonspecific epilepsy",
    "evidence_sources": "FDA Orange Book products file; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58093032-8480-4d0f-82be-92e643bdbea4; published=Jan 16, 2026; title=ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) INJECTION, POWDER, FOR SOLUTION [SAGENT PHARMACEUTICALS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58093032-8480-4d0f-82be-92e643bdbea4",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "No major enzyme effect",
    "filter_epilepsy_type": "Absence; Adjunctive nonspecific epilepsy; Generalized; Myoclonic",
    "filter_formulation": "Capsule; IV/IM injection; Long acting; Tablet",
    "filter_mechanism": "Carbonic anhydrase",
    "filter_metabolism": "Renal/no major metabolism",
    "filter_qt_effect": "No known meaningful QT effect",
    "filter_symptom_category": "CNS; Dermatologic; GI; Hematologic; Metabolic; Neurologic; Renal/metabolic",
    "formulations_available": "Oral tablet; extended-release capsule; IV injection as acetazolamide sodium",
    "generic_name": "acetazolamide",
    "half_life_range": "N/A - selected FDA/DailyMed label does not provide a half-life value.",
    "major_organ_for_metabolism": "N/A - selected FDA/DailyMed label does not identify a major metabolic organ; renal bicarbonate handling and urinary effects are clinically central.",
    "maximum_approved_daily_dose": "1000 mg/day; FDA label notes doses above 1 g/day do not appear to improve results.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Carbonic anhydrase inhibitor; FDA labeling states inhibition in the CNS appears to retard abnormal paroxysmal excessive neuronal discharge, while acknowledging that the basis of epilepsy benefit is not clearly known.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "375 mg/day or 8 mg/kg/day lower labeled epilepsy-adjunct range; individualized response noted in FDA label.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "Diamox; acetazolamide sodium",
    "qt_interval_effect": "No QT interval effect described in selected FDA label.",
    "rct_pubmed_verification_notes": "No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-19-2026; RCT section set to N/A per current scope.",
    "status_or_notes": "FDA Orange Book pre-1982 ASM adjunct; FDA-labeled for centrencephalic epilepsies and other non-seizure indications including glaucoma/edema/acute mountain sickness depending product.",
    "trade_names": "Acetazolamide; Acetazolamide Sodium; Diamox",
    "typical_doses_per_day": "Epilepsy adjunct: 8-30 mg/kg/day in divided doses; FDA label states optimum range appears to be 375-1000 mg/day.",
    "year_fda_cleared": "Approved Prior to Jan 1, 1982 (FDA Orange Book)"
  },
  "existing_pubmed_links": [],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "N/A 0%: FDA label lists paresthesia, hearing dysfunction/tinnitus, loss of appetite, taste alteration, GI disturbances, polyuria, drowsiness, confusion, rash, blood dyscrasias, electrolyte imbalance, and metabolic acidosis without quantified incidence percentages.",
    "alternate_generic_names": "acetazolamide sodium",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "No broad enzyme induction/inhibition described in selected FDA label; label notes interactions including altered phenytoin metabolism and reduced primidone/metabolite concentrations through decreased absorption.",
    "epilepsy_type": "Centrencephalic epilepsies; Absence; Generalized; Myoclonic; Adjunctive nonspecific epilepsy",
    "evidence_sources": "FDA Orange Book products file; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58093032-8480-4d0f-82be-92e643bdbea4; published=Jan 16, 2026; title=ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) INJECTION, POWDER, FOR SOLUTION [SAGENT PHARMACEUTICALS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58093032-8480-4d0f-82be-92e643bdbea4",
    "formulations_available": "Oral tablet; extended-release capsule; IV injection as acetazolamide sodium",
    "half_life_range": "N/A - selected FDA/DailyMed label does not provide a half-life value.",
    "major_organ_for_metabolism": "N/A - selected FDA/DailyMed label does not identify a major metabolic organ; renal bicarbonate handling and urinary effects are clinically central.",
    "maximum_approved_daily_dose": "1000 mg/day; FDA label notes doses above 1 g/day do not appear to improve results.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Carbonic anhydrase inhibitor; FDA labeling states inhibition in the CNS appears to retard abnormal paroxysmal excessive neuronal discharge, while acknowledging that the basis of epilepsy benefit is not clearly known.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "375 mg/day or 8 mg/kg/day lower labeled epilepsy-adjunct range; individualized response noted in FDA label.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "Diamox; acetazolamide sodium",
    "qt_interval_effect": "No QT interval effect described in selected FDA label.",
    "trade_names": "Acetazolamide; Acetazolamide Sodium; Diamox",
    "typical_doses_per_day": "Epilepsy adjunct: 8-30 mg/kg/day in divided doses; FDA label states optimum range appears to be 375-1000 mg/day.",
    "year_fda_cleared": "Approved Prior to Jan 1, 1982 (FDA Orange Book)"
  },
  "generic_name": "acetazolamide",
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
          "approved",
          "orange"
        ],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10",
      "generic_name": "acetazolamide",
      "id": "source_fact_concordance_problem-2f249df2d78f",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10); review current text before relying on it.",
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
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10",
      "generic_name": "acetazolamide",
      "id": "source_fact_concordance_problem-5a8dc6782798",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "qt_interval_effect could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58093032-8480-4d0f-82be-92e643bdbea4; published=Jan 16, 2026; title=ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) INJECTION, POWDER, FOR SOLUTION [SAGENT PHARMACEUTICALS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58093032-8480-4d0f-82be-92e643bdbea4",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10",
      "generic_name": "acetazolamide",
      "id": "fda_warning_metadata_refresh-a5437214f970",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "No FDA boxed warning identified in selected current FDA/openFDA label.",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=4dd56001-4941-4ff0-9f30-02a1bcc4fe7e; effective_time=20260410; title=Acetazolamide / ACETAZOLAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=4dd56001-4941-4ff0-9f30-02a1bcc4fe7e; effective_time=20260410; title=Acetazolamide / ACETAZOLAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10",
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
