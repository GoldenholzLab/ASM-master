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
    "adverse_symptoms_percentages": "HALMED SmPC frequency categories: very rare events <0.01% include megaloblastic anemia; unknown frequency 0% exact percentage unavailable for CNS depression, mood changes/depression, dependence, nervousness, dizziness, somnolence, nystagmus, ataxia, headache, nausea, vomiting, constipation, bradycardia, respiratory insufficiency, SJS/TEN, rash, angioedema, osteomalacia/rickets.",
    "alternate_generic_names": "mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital",
    "available_in_us": "No - not currently available in U.S. for seizure control; European nationally authorized Phemiton documentation identified.",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "Enzyme inducer: barbiturate induction of hepatic microsomal enzymes, including CYP3A4-related interactions.",
    "epilepsy_type": "Generalized tonic-clonic; Absence; Generalized seizures",
    "evidence_sources": "HALMED Phemiton 200 mg SmPC (https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf); EMA methylphenobarbital nationally authorised products PSUSA/00002025/202303 (https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf); FDA/DailyMed labeling",
    "fda_black_box_warning": "No current FDA/DailyMed label identified.",
    "fda_black_box_warning_source": "FDA/DailyMed search on 05-20-2026: no current label found for terms [methylphenobarbital; mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal].",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Not available in US",
    "filter_enzyme_effect": "Inducer",
    "filter_epilepsy_type": "Absence; Generalized; Generalized tonic-clonic",
    "filter_formulation": "Tablet",
    "filter_mechanism": "GABA",
    "filter_metabolism": "Liver/hepatic; Renal/no major metabolism",
    "filter_qt_effect": "No known meaningful QT effect; Other",
    "filter_symptom_category": "Behavioral; Blood; CNS; Dermatologic; GI; Metabolic; Neurologic; Psychiatric; Respiratory",
    "formulations_available": "Tablet",
    "generic_name": "methylphenobarbital",
    "half_life_range": "About 75 h in children; about 100 h in adults",
    "major_organ_for_metabolism": "Liver; N-demethylation to phenobarbital; partial renal excretion",
    "maximum_approved_daily_dose": "HALMED SmPC: 600 mg/day maximum in adults.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Barbiturate related to phenobarbital and metabolized partly to phenobarbital; HALMED SmPC attributes anticonvulsant effect to effects on CNS impulse transmission, increased motor-cortex electrical threshold, and possible enhancement of GABA-mediated inhibitory synaptic activity.",
    "mechanism_source": "HALMED Phemiton 200 mg SmPC (https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf)",
    "mechanism_source_tier": "EMA/UK SmPC",
    "minimum_effective_dose": "HALMED SmPC: start with the lowest dose and titrate over several days; adult recommended range begins at 200 mg/day.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Phemiton; Prominal",
    "qt_interval_effect": "No QT interval effect described in HALMED SmPC; caution with impaired cardiac function and interacting cardiovascular drugs.",
    "rct_pubmed_verification_notes": "No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-20-2026; RCT section set to N/A per current scope.",
    "status_or_notes": "European nationally authorized barbiturate ASM; EMA PSUSA list identifies Phemiton 200 mg tablets as nationally authorized in Croatia and Slovenia, and HALMED SmPC lists generalized epileptic seizures.",
    "trade_names": "Mebaral; Mephyltaletten; Phemiton; Prominal",
    "typical_doses_per_day": "HALMED SmPC: adults 200-400 mg/day once daily or divided; children under 5 years 15-30 mg 3-4 times/day; children over 5 years 30-60 mg 3-4 times/day.",
    "year_fda_cleared": "Not FDA-cleared/currently available in U.S.; Croatia Phemiton first authorization 06 Apr 1994 and renewal 30 Mar 2020 per HALMED; EMA PSUSA lists Croatia and Slovenia nationally authorized products."
  },
  "existing_pubmed_links": [],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "HALMED SmPC frequency categories: very rare events <0.01% include megaloblastic anemia; unknown frequency 0% exact percentage unavailable for CNS depression, mood changes/depression, dependence, nervousness, dizziness, somnolence, nystagmus, ataxia, headache, nausea, vomiting, constipation, bradycardia, respiratory insufficiency, SJS/TEN, rash, angioedema, osteomalacia/rickets.",
    "alternate_generic_names": "mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital",
    "available_in_us": "No - not currently available in U.S. for seizure control; European nationally authorized Phemiton documentation identified.",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "Enzyme inducer: barbiturate induction of hepatic microsomal enzymes, including CYP3A4-related interactions.",
    "epilepsy_type": "Generalized tonic-clonic; Absence; Generalized seizures",
    "evidence_sources": "HALMED Phemiton 200 mg SmPC (https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf); EMA methylphenobarbital nationally authorised products PSUSA/00002025/202303 (https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf); FDA/DailyMed labeling",
    "fda_black_box_warning": "No current FDA/DailyMed label identified.",
    "fda_black_box_warning_source": "FDA/DailyMed search on 05-20-2026: no current label found for terms [methylphenobarbital; mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal].",
    "formulations_available": "Tablet",
    "half_life_range": "About 75 h in children; about 100 h in adults",
    "major_organ_for_metabolism": "Liver; N-demethylation to phenobarbital; partial renal excretion",
    "maximum_approved_daily_dose": "HALMED SmPC: 600 mg/day maximum in adults.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Barbiturate related to phenobarbital and metabolized partly to phenobarbital; HALMED SmPC attributes anticonvulsant effect to effects on CNS impulse transmission, increased motor-cortex electrical threshold, and possible enhancement of GABA-mediated inhibitory synaptic activity.",
    "mechanism_source": "HALMED Phemiton 200 mg SmPC (https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf)",
    "mechanism_source_tier": "EMA/UK SmPC",
    "minimum_effective_dose": "HALMED SmPC: start with the lowest dose and titrate over several days; adult recommended range begins at 200 mg/day.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Phemiton; Prominal",
    "qt_interval_effect": "No QT interval effect described in HALMED SmPC; caution with impaired cardiac function and interacting cardiovascular drugs.",
    "trade_names": "Mebaral; Mephyltaletten; Phemiton; Prominal",
    "typical_doses_per_day": "HALMED SmPC: adults 200-400 mg/day once daily or divided; children under 5 years 15-30 mg 3-4 times/day; children over 5 years 30-60 mg 3-4 times/day.",
    "year_fda_cleared": "Not FDA-cleared/currently available in U.S.; Croatia Phemiton first authorization 06 Apr 1994 and renewal 30 Mar 2020 per HALMED; EMA PSUSA lists Croatia and Slovenia nationally authorized products."
  },
  "generic_name": "methylphenobarbital",
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
  "latest_deterministic_update_check_findings_for_row": [],
  "local_outcome_audit_rows": [],
  "local_rct_audit_rows": [],
  "possible_duplicate_name_hits": []
}
