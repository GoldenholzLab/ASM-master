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
    "adverse_symptoms_percentages": "Swiss Fachinformation frequency categories: frequent 1-10% not itemized for all symptoms; occasional 0.1-1% calcium metabolism disorder and weight loss; rare 0.01-0.1% aplastic/megaloblastic anemia, pancytopenia, thrombocytopenia, leukopenia, agranulocytosis, allergic/respiratory hypersensitivity, hallucinations, hemorrhage, constipation, vomiting, gingival hyperplasia, SJS/TEN, exfoliative dermatitis, rash; frequency not reliably estimable 0% exact percentage unavailable for somnolence, ataxia, nystagmus, dizziness, respiratory depression, fatigue.",
    "alternate_generic_names": "barbesaclone; barbexaclonum",
    "available_in_us": "No - not available in U.S. for seizure control; historical Swiss/Italian European documentation identified.",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "Enzyme inducer: phenobarbital component induces hepatic microsomal enzymes/P450 with broad interaction potential.",
    "epilepsy_type": "Generalized tonic-clonic; Absence; Myoclonic-atonic; Myoclonic; Lennox-Gastaut syndrome; Focal; Infantile spasms/BNS",
    "evidence_sources": "Swiss Maliasin Fachinformation Swissmedic no. 31862 (https://ch.oddb.org/de/gcc/fachinfo/reg/31862); Swissmedic Journal 07/2006 Maliasin authorization entry (https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf); AIFA Barbesaclone distribution communication (https://www.aifa.gov.it/en/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-); FDA/DailyMed labeling",
    "fda_black_box_warning": "No current FDA/DailyMed label identified.",
    "fda_black_box_warning_source": "FDA/DailyMed search on 05-20-2026: no current label found for terms [barbexaclone; barbesaclone; barbexaclonum; Maliasin].",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Not available in US",
    "filter_enzyme_effect": "Inducer",
    "filter_epilepsy_type": "Absence; Epileptic spasms / infantile spasms; Focal; Generalized tonic-clonic; LGS; Myoclonic; Myoclonic-atonic",
    "filter_formulation": "Tablet",
    "filter_mechanism": "GABA",
    "filter_metabolism": "Liver/hepatic; Renal/no major metabolism",
    "filter_qt_effect": "Conduction/arrhythmia caution; Other",
    "filter_symptom_category": "Blood; CNS; Dermatologic; GI; Metabolic; Neurologic; Respiratory",
    "formulations_available": "Coated tablet/dragee",
    "generic_name": "barbexaclone",
    "half_life_range": "Phenobarbital component 2-4 days in adults; 3 days in children; 3-7 days in neonates; 4-8 days with cirrhosis",
    "major_organ_for_metabolism": "Liver metabolism of phenobarbital component with renal elimination; propylhexedrine oxidative metabolism described",
    "maximum_approved_daily_dose": "No explicit fixed maximum in Swiss Fachinformation; average adult daily dose 200-400 mg/day and pediatric 50-300 mg/day.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Phenobarbital and L-propylhexedrine salt; Swiss Fachinformation attributes antiseizure effect to phenobarbital-related barbiturate reduction of neuronal excitability and inhibition of pathologic CNS excitation, with propylhexedrine intended to counter unwanted sedation.",
    "mechanism_source": "Swiss Maliasin Fachinformation Swissmedic no. 31862 (https://ch.oddb.org/de/gcc/fachinfo/reg/31862)",
    "mechanism_source_tier": "EMA/UK SmPC",
    "minimum_effective_dose": "Swiss Fachinformation: adult titration begins at 100 mg/day; children may titrate slowly using 25 mg tablets.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "barbesaclone; barbexaclonum; Maliasin",
    "qt_interval_effect": "No QT interval effect described in Swiss Fachinformation; contraindications/cautions include tachyarrhythmias, severe angina, severe myocardial damage.",
    "rct_pubmed_verification_notes": "No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-20-2026; RCT section set to N/A per current scope.",
    "status_or_notes": "Historical European/Swiss/Italian ASM product; Swissmedic Journal lists Maliasin 25 mg/100 mg (barbexaclonum) as an antiepileptic under authorization no. 31862, Swiss Maliasin Fachinformation lists multiple epilepsy indications, and AIFA communications document Barbesaclone 25 mg/100 mg coated-tablet distribution access.",
    "trade_names": "Maliasin",
    "typical_doses_per_day": "Swiss Fachinformation: adults usually 200-400 mg/day; school-age children 50-300 mg/day; individualized titration from 100 mg/day in adults.",
    "year_fda_cleared": "Not FDA-cleared; Swissmedic Journal documents Maliasin authorization no. 31862 as an antiepileptic, and AIFA Barbesaclone 25 mg/100 mg distribution communications are documented."
  },
  "existing_pubmed_links": [],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "Swiss Fachinformation frequency categories: frequent 1-10% not itemized for all symptoms; occasional 0.1-1% calcium metabolism disorder and weight loss; rare 0.01-0.1% aplastic/megaloblastic anemia, pancytopenia, thrombocytopenia, leukopenia, agranulocytosis, allergic/respiratory hypersensitivity, hallucinations, hemorrhage, constipation, vomiting, gingival hyperplasia, SJS/TEN, exfoliative dermatitis, rash; frequency not reliably estimable 0% exact percentage unavailable for somnolence, ataxia, nystagmus, dizziness, respiratory depression, fatigue.",
    "alternate_generic_names": "barbesaclone; barbexaclonum",
    "available_in_us": "No - not available in U.S. for seizure control; historical Swiss/Italian European documentation identified.",
    "diff_50_responder_maximum_effective_dose": "N/A",
    "diff_median_pct_change_maximum_effective_dose": "N/A",
    "diff_seizure_freedom_maximum_effective_dose": "N/A",
    "enzyme_inducing_or_inhibiting": "Enzyme inducer: phenobarbital component induces hepatic microsomal enzymes/P450 with broad interaction potential.",
    "epilepsy_type": "Generalized tonic-clonic; Absence; Myoclonic-atonic; Myoclonic; Lennox-Gastaut syndrome; Focal; Infantile spasms/BNS",
    "evidence_sources": "Swiss Maliasin Fachinformation Swissmedic no. 31862 (https://ch.oddb.org/de/gcc/fachinfo/reg/31862); Swissmedic Journal 07/2006 Maliasin authorization entry (https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf); AIFA Barbesaclone distribution communication (https://www.aifa.gov.it/en/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-); FDA/DailyMed labeling",
    "fda_black_box_warning": "No current FDA/DailyMed label identified.",
    "fda_black_box_warning_source": "FDA/DailyMed search on 05-20-2026: no current label found for terms [barbexaclone; barbesaclone; barbexaclonum; Maliasin].",
    "formulations_available": "Coated tablet/dragee",
    "half_life_range": "Phenobarbital component 2-4 days in adults; 3 days in children; 3-7 days in neonates; 4-8 days with cirrhosis",
    "major_organ_for_metabolism": "Liver metabolism of phenobarbital component with renal elimination; propylhexedrine oxidative metabolism described",
    "maximum_approved_daily_dose": "No explicit fixed maximum in Swiss Fachinformation; average adult daily dose 200-400 mg/day and pediatric 50-300 mg/day.",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Phenobarbital and L-propylhexedrine salt; Swiss Fachinformation attributes antiseizure effect to phenobarbital-related barbiturate reduction of neuronal excitability and inhibition of pathologic CNS excitation, with propylhexedrine intended to counter unwanted sedation.",
    "mechanism_source": "Swiss Maliasin Fachinformation Swissmedic no. 31862 (https://ch.oddb.org/de/gcc/fachinfo/reg/31862)",
    "mechanism_source_tier": "EMA/UK SmPC",
    "minimum_effective_dose": "Swiss Fachinformation: adult titration begins at 100 mg/day; children may titrate slowly using 25 mg tablets.",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "N/A",
    "pubmed_search_aliases": "barbesaclone; barbexaclonum; Maliasin",
    "qt_interval_effect": "No QT interval effect described in Swiss Fachinformation; contraindications/cautions include tachyarrhythmias, severe angina, severe myocardial damage.",
    "trade_names": "Maliasin",
    "typical_doses_per_day": "Swiss Fachinformation: adults usually 200-400 mg/day; school-age children 50-300 mg/day; individualized titration from 100 mg/day in adults.",
    "year_fda_cleared": "Not FDA-cleared; Swissmedic Journal documents Maliasin authorization no. 31862 as an antiepileptic, and AIFA Barbesaclone 25 mg/100 mg distribution communications are documented."
  },
  "generic_name": "barbexaclone",
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
