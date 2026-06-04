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
    "adverse_symptoms_percentages": "CNS: somnolence/sedation 10%, respiratory: nasal discomfort 16% for nasal product, throat irritation 3%, respiratory depression 2%, GI: nausea 2%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo RR50 differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_median_pct_change_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo MPC differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_seizure_freedom_maximum_effective_dose": "16.1-19.3 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Spencer2020 midazolam nasal spray 5 mg 16.1%; Detyniecki2019 midazolam nasal spray 5 mg 19.3%)",
    "enzyme_inducing_or_inhibiting": "Not an inducer/inhibitor; CYP3A substrate",
    "epilepsy_type": "Seizure clusters / rescue; Status epilepticus",
    "evidence_sources": "Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling",
    "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death . Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation [see Warnings and Precautions (5.1) and Drug Interactions (7.2) ] . The use of benzodiazepines, including NAYZILAM, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of benzodiazepines commonly involve concomitant use of other medications, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes. Before prescribing NAYZILAM and throughout treatment, assess each patient's risk for abuse, misuse, and addiction [see Warnings and Precautions (5.2) ]. The continued use of benzodiazepines may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Although NAYZILAM is indicated only for intermittent use [see Indications and Usage (1) and Dosage and Administration (2) ] , if used more frequently than recommended abrupt discontinuation or rapid dosage reduction of NAYZILAM may precipitate acute withdrawal reactions, which can be life-threatening. For patients using NAYZILAM more frequently than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue NAYZILAM [see Warnings and Precautions (5.3) ]. WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS See full prescribing information for complete boxed warning. Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death ( 5.1 , 7.2 ) The use of benzodiazepines, including NAYZILAM, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Before prescribing NAYZILAM and throughout treatment, assess each patient's risk for abuse, misuse, and addiction ( 5.2 ). Although NAYZILAM is indicated only for intermittent use ( 1 , 2 ), if used more frequently than recommended, abrupt discontinuation or rapid dosage reduction of NAYZILAM may precipitate acute withdrawal reactions, which can be life-threatening. For patients using NAYZILAM more frequently than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue NAYZILAM ( 5.3 ).",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=boxed_warning_found; setid=2b29422e-54d5-4a49-8522-e9cf752368c3; published=Jan 31, 2023; title=NAYZILAM (MIDAZOLAM) SPRAY [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b29422e-54d5-4a49-8522-e9cf752368c3",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "Inhibitor; Substrate / affected by modulators",
    "filter_epilepsy_type": "Seizure clusters / rescue; Status epilepticus",
    "filter_formulation": "IV/IM injection; Liquid; Rescue formulation",
    "filter_mechanism": "GABA",
    "filter_metabolism": "Gut; Liver/hepatic",
    "filter_qt_effect": "No known meaningful QT effect",
    "filter_symptom_category": "CNS; GI; Respiratory",
    "formulations_available": "Nasal spray; buccal/oromucosal solution in some markets; IV/IM injection; oral syrup for sedation",
    "generic_name": "midazolam",
    "half_life_range": "1.5-6 h",
    "major_organ_for_metabolism": "Liver and gut",
    "maximum_approved_daily_dose": "Rescue dosing individualized by product/age/weight",
    "mechanism_confidence": "High",
    "mechanism_of_action": "Benzodiazepine positive allosteric modulator of GABA-A receptors; enhances GABAergic inhibition by binding at the benzodiazepine site.",
    "mechanism_source": "American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling",
    "mechanism_source_tier": "AES/FDA summary",
    "minimum_effective_dose": "Rescue dosing individualized by product/age/weight",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "Spencer2020|16.1|https://pubmed.ncbi.nlm.nih.gov/33140403/|62; Detyniecki2019|19.3|https://pubmed.ncbi.nlm.nih.gov/31140596/|201",
    "pubmed_phase_ii_iii_rct_links": "Spencer2020|https://pubmed.ncbi.nlm.nih.gov/33140403/; Detyniecki2019|https://pubmed.ncbi.nlm.nih.gov/31140596/",
    "pubmed_search_aliases": "Nayzilam; midazolam nasal spray",
    "qt_interval_effect": "No clinically meaningful QT effect established",
    "rct_pubmed_verification_notes": "PubMed loop 34/65 on 2026-05-15: 2 qualifying placebo-controlled randomized clinical trial report(s) retained from 11 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.",
    "status_or_notes": "Benzodiazepine used for seizure clusters/status epilepticus rescue; also used for procedural sedation/anesthesia.",
    "trade_names": "Nayzilam; Seizalam; Versed",
    "typical_doses_per_day": "Rescue/status dosing is intermittent, not chronic daily dosing",
    "year_fda_cleared": "1985 injection; 2019 nasal seizure-cluster product"
  },
  "existing_pubmed_links": [
    {
      "entry": "Spencer2020|https://pubmed.ncbi.nlm.nih.gov/33140403/",
      "label": "Spencer2020",
      "pmid": "33140403",
      "url": "https://pubmed.ncbi.nlm.nih.gov/33140403/"
    },
    {
      "entry": "Detyniecki2019|https://pubmed.ncbi.nlm.nih.gov/31140596/",
      "label": "Detyniecki2019",
      "pmid": "31140596",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31140596/"
    }
  ],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "CNS: somnolence/sedation 10%, respiratory: nasal discomfort 16% for nasal product, throat irritation 3%, respiratory depression 2%, GI: nausea 2%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo RR50 differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_median_pct_change_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo MPC differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_seizure_freedom_maximum_effective_dose": "16.1-19.3 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Spencer2020 midazolam nasal spray 5 mg 16.1%; Detyniecki2019 midazolam nasal spray 5 mg 19.3%)",
    "enzyme_inducing_or_inhibiting": "Not an inducer/inhibitor; CYP3A substrate",
    "epilepsy_type": "Seizure clusters / rescue; Status epilepticus",
    "evidence_sources": "Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling",
    "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death . Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation [see Warnings and Precautions (5.1) and Drug Interactions (7.2) ] . The use of benzodiazepines, including NAYZILAM, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of benzodiazepines commonly involve concomitant use of other medications, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes. Before prescribing NAYZILAM and throughout treatment, assess each patient's risk for abuse, misuse, and addiction [see Warnings and Precautions (5.2) ]. The continued use of benzodiazepines may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Although NAYZILAM is indicated only for intermittent use [see Indications and Usage (1) and Dosage and Administration (2) ] , if used more frequently than recommended abrupt discontinuation or rapid dosage reduction of NAYZILAM may precipitate acute withdrawal reactions, which can be life-threatening. For patients using NAYZILAM more frequently than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue NAYZILAM [see Warnings and Precautions (5.3) ]. WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS See full prescribing information for complete boxed warning. Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death ( 5.1 , 7.2 ) The use of benzodiazepines, including NAYZILAM, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Before prescribing NAYZILAM and throughout treatment, assess each patient's risk for abuse, misuse, and addiction ( 5.2 ). Although NAYZILAM is indicated only for intermittent use ( 1 , 2 ), if used more frequently than recommended, abrupt discontinuation or rapid dosage reduction of NAYZILAM may precipitate acute withdrawal reactions, which can be life-threatening. For patients using NAYZILAM more frequently than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue NAYZILAM ( 5.3 ).",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=boxed_warning_found; setid=2b29422e-54d5-4a49-8522-e9cf752368c3; published=Jan 31, 2023; title=NAYZILAM (MIDAZOLAM) SPRAY [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b29422e-54d5-4a49-8522-e9cf752368c3",
    "formulations_available": "Nasal spray; buccal/oromucosal solution in some markets; IV/IM injection; oral syrup for sedation",
    "half_life_range": "1.5-6 h",
    "major_organ_for_metabolism": "Liver and gut",
    "maximum_approved_daily_dose": "Rescue dosing individualized by product/age/weight",
    "mechanism_confidence": "High",
    "mechanism_of_action": "Benzodiazepine positive allosteric modulator of GABA-A receptors; enhances GABAergic inhibition by binding at the benzodiazepine site.",
    "mechanism_source": "American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling",
    "mechanism_source_tier": "AES/FDA summary",
    "minimum_effective_dose": "Rescue dosing individualized by product/age/weight",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "Spencer2020|16.1|https://pubmed.ncbi.nlm.nih.gov/33140403/|62; Detyniecki2019|19.3|https://pubmed.ncbi.nlm.nih.gov/31140596/|201",
    "pubmed_phase_ii_iii_rct_links": "Spencer2020|https://pubmed.ncbi.nlm.nih.gov/33140403/; Detyniecki2019|https://pubmed.ncbi.nlm.nih.gov/31140596/",
    "pubmed_search_aliases": "Nayzilam; midazolam nasal spray",
    "qt_interval_effect": "No clinically meaningful QT effect established",
    "trade_names": "Nayzilam; Seizalam; Versed",
    "typical_doses_per_day": "Rescue/status dosing is intermittent, not chronic daily dosing",
    "year_fda_cleared": "1985 injection; 2019 nasal seizure-cluster product"
  },
  "generic_name": "midazolam",
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
      "current_value": "1985 injection; 2019 nasal seizure-cluster product",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1985",
          "2019"
        ],
        "missing_terms": [],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5",
      "generic_name": "midazolam",
      "id": "source_fact_concordance_problem-a83ae075db9a",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "year_fda_cleared could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "This study is designed to evaluate the efficacy, safety, and tolerability of USL261 compared with that of intranasal (IN) placebo for the treatment of intermittent bouts of increased seizure activity.",
        "interventions": [
          "USL261",
          "Placebo"
        ],
        "masking": "TRIPLE",
        "nct_id": "NCT01999777",
        "new_reference_pmids": [],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "33140403"
        ],
        "title": "Study to Evaluate the Safety and Efficacy of USL261 in Patients With Increased Bouts of Seizure Activity in the EMU"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT01999777",
      "generic_name": "midazolam",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-b6d55568968d",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Evaluate the Safety and Efficacy of USL261 in Patients With Increased Bouts of Seizure Activity in the EMU"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "The purpose of this study is to examine the safety and effectiveness of USL261 for the outpatient treatment of seizure clusters.",
        "interventions": [
          "USL261",
          "Placebo"
        ],
        "masking": "TRIPLE",
        "nct_id": "NCT01390220",
        "new_reference_pmids": [
          "36410152"
        ],
        "overall_status": "TERMINATED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "36410152",
          "31140596"
        ],
        "title": "Study to Evaluate the Safety and Efficacy of USL261 (Intranasal Midazolam) in Patients With Seizure Clusters"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT01390220",
      "generic_name": "midazolam",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-56897abca4e0",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Evaluate the Safety and Efficacy of USL261 (Intranasal Midazolam) in Patients With Seizure Clusters"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "Generalized status epilepticus is a common pediatric neurological emergency with significant mortality and morbidity. Benzodiazepines remain the first anticonvulsive line but benzo-diazepines don't control seizures in about 30% of cases. GCSE may be more rapidly stopped and controlled through combining another drug with benzodiazepines such as Levetiracetam, acting by different pathways. This study aims to evaluate the effectiveness of combined levetiracetam and midazolam in treatment of generalized convulsive status epilepticus in children.",
        "interventions": [
          "Levetiracetam",
          "Midazolam",
          "Placebo"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT04926844",
        "new_reference_pmids": [
          "26900382",
          "33552322",
          "31879852",
          "30472551",
          "26627366",
          "26840871",
          "15210974",
          "12915336",
          "21898137",
          "32385134"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE2"
        ],
        "pmids": [
          "26900382",
          "33552322",
          "31879852",
          "30472551",
          "26627366",
          "26840871",
          "15210974",
          "12915336",
          "21898137",
          "32385134"
        ],
        "title": "Effectiveness of Combined Levetiracetam and Midazolam in Generalized Convulsive Status Epilepticus in Children"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT04926844",
      "generic_name": "midazolam",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-5b27e2248d8f",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Effectiveness of Combined Levetiracetam and Midazolam in Generalized Convulsive Status Epilepticus in Children"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "Generalized convulsive status epilepticus (GCSE) is a common neurological emergency in children. Benzodiazepines are the recommended first line antiseizure medication (ASMs), but they fail to control seizures in a third of cases. Combination of benzodiazepines with another ASM that has a different mechanism of action may be a promising option for faster control of GCSE. In this study, the investigators aim to evaluate the efficacy and safety of ketamine plus midazolam versus midazolam alone as first-line therapy of pediatric GCSE.",
        "interventions": [
          "Ketamine",
          "Midazolam",
          "Placebo"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT05779657",
        "new_reference_pmids": [
          "26336950",
          "31879852",
          "26900382",
          "25323468",
          "23197747",
          "23758557",
          "27500978",
          "17941842",
          "36792542",
          "31536850"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE2",
          "PHASE3"
        ],
        "pmids": [
          "26336950",
          "31879852",
          "26900382",
          "25323468",
          "23197747",
          "23758557",
          "27500978",
          "17941842",
          "36792542",
          "31536850"
        ],
        "title": "Combined Ketamine and Midazolam for Generalized Convulsive Status Epilepticus"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT05779657",
      "generic_name": "midazolam",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-03ccb5eab6aa",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Combined Ketamine and Midazolam for Generalized Convulsive Status Epilepticus"
    },
    {
      "column": "enzyme_inducing_or_inhibiting",
      "current_value": "Not an inducer/inhibitor; CYP3A substrate",
      "details": {
        "checked": true,
        "matched_terms": [],
        "missing_numbers": [],
        "missing_terms": [
          "inducer",
          "inhibitor",
          "cyp3a",
          "substrate"
        ],
        "numbers": [],
        "ok": false,
        "terms": [
          "inducer",
          "inhibitor",
          "cyp3a",
          "substrate"
        ]
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5",
      "generic_name": "midazolam",
      "id": "source_fact_concordance_problem-6b954d326c5f",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: enzyme_inducing_or_inhibiting was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: enzyme_inducing_or_inhibiting was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "enzyme_inducing_or_inhibiting could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=boxed_warning_found; setid=2b29422e-54d5-4a49-8522-e9cf752368c3; published=Jan 31, 2023; title=NAYZILAM (MIDAZOLAM) SPRAY [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b29422e-54d5-4a49-8522-e9cf752368c3",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5",
      "generic_name": "midazolam",
      "id": "fda_warning_metadata_refresh-6d6f723b88fd",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death . Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation [see Warnings and Precautions (5.1) and Drug Interactions (7.2) ] . The use of benzodiazepines, including NAYZILAM, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of benzodiazepines commonly involve concomitant use of other medications, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes. Before prescribing NAYZILAM and throughout treatment, assess each patient's risk for abuse, misuse, and addiction [see Warnings and Precautions (5.2) ]. The continued use of benzodiazepines may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Although NAYZILAM is indicated only for intermittent use [see Indications and Usage (1) and Dosage and Administration (2) ] , if used more frequently than recommended abrupt discontinuation or rapid dosage reduction of NAYZILAM may precipitate acute withdrawal reactions, which can be life-threatening. For patients using NAYZILAM more frequently than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue NAYZILAM [see Warnings and Precautions (5.3) ]. WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS See full prescribing information for complete boxed warning. Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death ( 5.1 , 7.2 ) The use of benzodiazepines, including NAYZILAM, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Before prescribing NAYZILAM and throughout treatment, assess each patient's risk for abuse, misuse, and addiction ( 5.2 ). Although NAYZILAM is indicated only for intermittent use ( 1 , 2 ), if used more frequently than recommended, abrupt discontinuation or rapid dosage reduction of NAYZILAM may precipitate acute withdrawal reactions, which can be life-threatening. For patients using NAYZILAM more frequently than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue NAYZILAM ( 5.3 ).",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2b29422e-54d5-4a49-8522-e9cf752368c3; effective_time=20230119; title=Nayzilam / MIDAZOLAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2b29422e-54d5-4a49-8522-e9cf752368c3; effective_time=20230119; title=Nayzilam / MIDAZOLAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [
    {
      "audit_note": "Abstract reports 6-hour post-treatment seizure freedom.",
      "dose_or_regimen": "midazolam nasal spray 5 mg",
      "endpoint": "seizure cluster/EMU 6-hour seizure freedom",
      "generic_name": "midazolam",
      "label": "Spencer2020",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "33140403",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/33140403/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "54.8",
      "sf_differential_percent": "16.1",
      "sf_included_in_csv_summary": "yes",
      "sf_placebo_percent": "38.7",
      "title": "Safety and efficacy of midazolam nasal spray for the treatment of intermittent bouts of increased seizure activity in the epilepsy monitoring unit: A double-blind, randomized, placebo-controlled trial."
    },
    {
      "audit_note": "Treatment success required seizure termination within 10 minutes and no recurrence 10 minutes to 6 hours after dosing.",
      "dose_or_regimen": "midazolam nasal spray 5 mg",
      "endpoint": "seizure cluster treatment success",
      "generic_name": "midazolam",
      "label": "Detyniecki2019",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "31140596",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/31140596/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "53.7",
      "sf_differential_percent": "19.3",
      "sf_included_in_csv_summary": "yes",
      "sf_placebo_percent": "34.4",
      "title": "Safety and efficacy of midazolam nasal spray in the outpatient treatment of patients with seizure clusters-a randomized, double-blind, placebo-controlled trial."
    }
  ],
  "local_rct_audit_rows": [
    {
      "first_author": "Spencer",
      "generic_name": "midazolam",
      "label": "Spencer2020",
      "pmid": "33140403",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Safety and efficacy of midazolam nasal spray for the treatment of intermittent bouts of increased seizure activity in the epilepsy monitoring unit: A double-blind, randomized, placebo-controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/33140403/",
      "year": "2020"
    },
    {
      "first_author": "Detyniecki",
      "generic_name": "midazolam",
      "label": "Detyniecki2019",
      "pmid": "31140596",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Safety and efficacy of midazolam nasal spray in the outpatient treatment of patients with seizure clusters-a randomized, double-blind, placebo-controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31140596/",
      "year": "2019"
    },
    {
      "first_author": "Othman",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "40186980",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Combined Ketamine and Midazolam Versus Midazolam Alone for Initial Treatment of Pediatric Generalized Convulsive Status Epilepticus (Ket-Mid Study): A Randomized Controlled Trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/40186980/",
      "year": "2025"
    },
    {
      "first_author": "Elshater",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "37211889",
      "pub_types": "Randomized Controlled Trial; Journal Article",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Levetiracetam and Midazolam vs Midazolam Alone for First-Line Treatment of Children With Generalized Convulsive Status Epilepticus (Lev-Mid Study): A Randomized Controlled Trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/37211889/",
      "year": "2023"
    },
    {
      "first_author": "Richard",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "31994022",
      "pub_types": "Clinical Trial, Phase I; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Multiple-Ascending Dose Study in Healthy Subjects to Assess the Pharmacokinetics, Tolerability, and CYP3A4 Interaction Potential of the T-Type Calcium Channel Blocker ACT-709478, A Potential New Antiepileptic Drug.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31994022/",
      "year": "2020"
    },
    {
      "first_author": "Kellinghaus",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "26554812",
      "pub_types": "Journal Article; Multicenter Study; Observational Study; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Making SENSE--Sustained Effort Network for treatment of Status Epilepticus as a multicenter prospective registry.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/26554812/",
      "year": "2015"
    },
    {
      "first_author": "Olischar",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "25040756",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "The addition of tramadol to the standard of i.v. acetaminophen and morphine infusion for postoperative analgesia in neonates offers no clinical benefit: a randomized placebo-controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/25040756/",
      "year": "2014"
    },
    {
      "first_author": "Ohlraun",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "23806032",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "CARbon DIoxide for the treatment of Febrile seizures: rationale, feasibility, and design of the CARDIF-study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/23806032/",
      "year": "2013"
    },
    {
      "first_author": "Mpimbaza",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "18166545",
      "pub_types": "Comparative Study; Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Comparison of buccal midazolam with rectal diazepam in the treatment of prolonged seizures in Ugandan children: a randomized clinical trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/18166545/",
      "year": "2008"
    },
    {
      "first_author": "Arya",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "11568372",
      "pub_types": "Clinical Trial; Evaluation Study; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Midazolam sedation in mechanically ventilated newborns: a double blind randomized placebo controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/11568372/",
      "year": "2001"
    },
    {
      "first_author": "Scott",
      "generic_name": "midazolam",
      "label": "",
      "pmid": "9578047",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Buccal absorption of midazolam: pharmacokinetics and EEG pharmacodynamics.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9578047/",
      "year": "1998"
    }
  ],
  "possible_duplicate_name_hits": []
}
