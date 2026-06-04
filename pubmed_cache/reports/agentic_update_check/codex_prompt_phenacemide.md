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
    "adverse_symptoms_percentages": "N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.",
    "alternate_generic_names": "",
    "available_in_us": "No - discontinued FDA Orange Book product",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe enzyme induction or inhibition.",
    "epilepsy_type": "Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)",
    "evidence_sources": "FDA Orange Book products file; FDA/DailyMed labeling",
    "fda_black_box_warning": "No current FDA/DailyMed label identified.",
    "fda_black_box_warning_source": "FDA/DailyMed search on 05-20-2026: no current label found for terms [phenacemide; Phenurone].",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Not available in US",
    "filter_enzyme_effect": "Unknown/limited",
    "filter_epilepsy_type": "Historical/unspecified epilepsy",
    "filter_formulation": "Historical/not marketed; Tablet",
    "filter_mechanism": "Other / unclear",
    "filter_metabolism": "Limited/unknown",
    "filter_qt_effect": "Unknown/limited",
    "filter_symptom_category": "Unquantified/limited data",
    "formulations_available": "Historical oral tablet (not marketed in U.S.)",
    "generic_name": "phenacemide",
    "half_life_range": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.",
    "major_organ_for_metabolism": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.",
    "maximum_approved_daily_dose": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a maximum approved daily dose.",
    "mechanism_confidence": "Limited",
    "mechanism_of_action": "N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.",
    "mechanism_source": "FDA Orange Book products file",
    "mechanism_source_tier": "Historical/limited",
    "minimum_effective_dose": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a minimum effective dose.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "Phenurone",
    "qt_interval_effect": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe QT effect.",
    "rct_pubmed_verification_notes": "No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-19-2026; RCT section set to N/A per current scope.",
    "status_or_notes": "FDA Orange Book pre-1982 legacy ASM product (Phenurone); discontinued U.S. product listing.",
    "trade_names": "Phenurone",
    "typical_doses_per_day": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide dosing.",
    "year_fda_cleared": "Approved Prior to Jan 1, 1982 (FDA Orange Book)"
  },
  "existing_pubmed_links": [],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.",
    "alternate_generic_names": "",
    "available_in_us": "No - discontinued FDA Orange Book product",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe enzyme induction or inhibition.",
    "epilepsy_type": "Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)",
    "evidence_sources": "FDA Orange Book products file; FDA/DailyMed labeling",
    "fda_black_box_warning": "No current FDA/DailyMed label identified.",
    "fda_black_box_warning_source": "FDA/DailyMed search on 05-20-2026: no current label found for terms [phenacemide; Phenurone].",
    "formulations_available": "Historical oral tablet (not marketed in U.S.)",
    "half_life_range": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.",
    "major_organ_for_metabolism": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.",
    "maximum_approved_daily_dose": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a maximum approved daily dose.",
    "mechanism_confidence": "Limited",
    "mechanism_of_action": "N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.",
    "mechanism_source": "FDA Orange Book products file",
    "mechanism_source_tier": "Historical/limited",
    "minimum_effective_dose": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a minimum effective dose.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "Phenurone",
    "qt_interval_effect": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe QT effect.",
    "trade_names": "Phenurone",
    "typical_doses_per_day": "N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide dosing.",
    "year_fda_cleared": "Approved Prior to Jan 1, 1982 (FDA Orange Book)"
  },
  "generic_name": "phenacemide",
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
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed search on 05-19-2026: no current label found for terms [phenacemide; Phenurone].",
      "details": {},
      "evidence_url": "https://open.fda.gov/apis/drug/label/",
      "generic_name": "phenacemide",
      "id": "fda_warning_metadata_refresh-fb184c2cfd32",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "No current FDA/openFDA label identified.",
        "fda_black_box_warning_source": "FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [phenacemide; Phenurone].",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [phenacemide; Phenurone].",
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
