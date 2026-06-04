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
    "adverse_symptoms_percentages": "CNS: drowsiness/sedation 20-60%, behavioral: hyperactivity/irritability 5-15%, dermatologic: rash 1-3%, respiratory: respiratory depression <1% at therapeutic doses",
    "alternate_generic_names": "phenobarbitone",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo RR50 differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_median_pct_change_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo MPC differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_seizure_freedom_maximum_effective_dose": "83.3 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Takami2019 phenobarbital 10 mg/kg IV 83.3%)",
    "enzyme_inducing_or_inhibiting": "Strong enzyme inducer: CYP and UGT pathways",
    "epilepsy_type": "Focal; Generalized tonic-clonic; Neonatal seizures; Status epilepticus",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review",
    "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; DEPENDENCE AND WITHDRAWAL REACTIONS AFTER USE OF SEZABY FOR A LONGER DURATION THAN RECOMMENDED; and ABUSE, MISUSE AND ADDICTION WITH UNAPPROVED USE IN ADOLESCENTS AND ADULTS Risks from Concomitant Use with Opioids Concomitant use of phenobarbital products, including SEZABY, and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. If a decision is made for concomitant use of these drugs, limit dosages and durations to the minimum required, and follow patients for signs and symptoms of respiratory depression and sedation [see Warnings and Precautions (5.1) and Drug Interactions (7.3)]. Dependence and Withdrawal Reactions After Use of SEZABY for a Longer Duration than Recommended The continued use of phenobarbital may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Although SEZABY is indicated only for short-term use [see Indications and Usage (1) and Dosage and Administration (2)], if used for a longer duration than recommended, abrupt discontinuation or rapid dosage reduction of SEZABY may precipitate acute withdrawal reactions, which can be life-threatening. For patients receiving SEZABY for longer duration than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue SEZABY [see Warnings and Precautions (5.2)]. Abuse, Misuse, and Addiction with Unapproved Use in Adolescents and Adults SEZABY is not approved for use in adolescents or adults. The unapproved use of SEZABY, in adolescents and adults exposes them to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of phenobarbital commonly involve concomitant use of other drugs, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes [see Warnings and Precaution (5.3)]. WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; DEPENDENCE AND WITHDRAWAL REACTIONS AFTER USE OF SEZABY FOR A LONGER DURATION THAN RECOMMENDED; and ABUSE, MISUSE, AND ADDICTION WITH UNAPPROVED USE IN ADOLESCENTS AND ADULTS See full prescribing information for complete boxed warning . Concomitant use of phenobarbital products, including SEZABY, and opioids may result in profound sedation, respiratory depression, coma, and death. If a decision is made to use concomitantly, limit dosages and durations to the minimum required, and monitor patients for respiratory depression and sedation. (5.1, 7.3) Although SEZABY is indicated only for short-term use (1, 2), if used for a longer duration than recommended, abrupt discontinuation or rapid dosage reduction may precipitate acute withdrawal reactions, which can be life-threatening. For patients receiving SEZABY for a longer duration than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue SEZABY. (5.2) SEZABY is not approved for use in adolescents or adults. The unapproved use of SEZABY in adolescents and adults exposes them to risks of abuse, misuse, and addiction, which can lead to overdose or death. (5.3)",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=boxed_warning_found; setid=8c7d0402-4977-4c25-bc4b-11db91339e9a; published=; title=These highlights do not include all the information needed to use SEZABY safely and effectively. See full prescribing information for SEZABY. SEZABY™ (phenobarbital sodium) for injection, for intravenous use, CIV Initial U.S. Approval: 2022; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "Inducer",
    "filter_epilepsy_type": "Focal; Generalized tonic-clonic; Neonatal seizures; Status epilepticus",
    "filter_formulation": "IV/IM injection; Liquid; Tablet",
    "filter_mechanism": "GABA",
    "filter_metabolism": "Liver/hepatic",
    "filter_qt_effect": "Other",
    "filter_symptom_category": "Behavioral; CNS; Dermatologic; Respiratory",
    "formulations_available": "Tablet; elixir/oral solution; IV/IM injection",
    "generic_name": "phenobarbital",
    "half_life_range": "53-118 h",
    "major_organ_for_metabolism": "Liver",
    "maximum_approved_daily_dose": "Individualized by serum level/tolerability; no single fixed max",
    "mechanism_confidence": "High",
    "mechanism_of_action": "Mechanism is not fully understood; barbiturate potentiation of synaptic inhibition through GABA-A receptors is the principal accepted antiseizure mechanism.",
    "mechanism_source": "FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "Individualized by serum level/tolerability; commonly 60 mg/day adult initial range",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "Takami2019|83.3|https://pubmed.ncbi.nlm.nih.gov/30954360/|13",
    "pubmed_phase_ii_iii_rct_links": "Takami2019|https://pubmed.ncbi.nlm.nih.gov/30954360/; Crawley2000|https://pubmed.ncbi.nlm.nih.gov/10703801/; Bacon1981|https://pubmed.ncbi.nlm.nih.gov/6116084/",
    "pubmed_search_aliases": "",
    "qt_interval_effect": "No direct QT effect established",
    "rct_pubmed_verification_notes": "PubMed loop 43/65 on 2026-05-15: 3 qualifying placebo-controlled randomized clinical trial report(s) retained from 44 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.",
    "status_or_notes": "Classic barbiturate ASM; also sedative/hypnotic uses historically.",
    "trade_names": "Luminal; Phenobarb; Solfoton",
    "typical_doses_per_day": "Adults often 60-200 mg/day once daily or divided; pediatric weight-based",
    "year_fda_cleared": "1912 legacy; predates modern FDA approval system"
  },
  "existing_pubmed_links": [
    {
      "entry": "Takami2019|https://pubmed.ncbi.nlm.nih.gov/30954360/",
      "label": "Takami2019",
      "pmid": "30954360",
      "url": "https://pubmed.ncbi.nlm.nih.gov/30954360/"
    },
    {
      "entry": "Crawley2000|https://pubmed.ncbi.nlm.nih.gov/10703801/",
      "label": "Crawley2000",
      "pmid": "10703801",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10703801/"
    },
    {
      "entry": "Bacon1981|https://pubmed.ncbi.nlm.nih.gov/6116084/",
      "label": "Bacon1981",
      "pmid": "6116084",
      "url": "https://pubmed.ncbi.nlm.nih.gov/6116084/"
    }
  ],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "CNS: drowsiness/sedation 20-60%, behavioral: hyperactivity/irritability 5-15%, dermatologic: rash 1-3%, respiratory: respiratory depression <1% at therapeutic doses",
    "alternate_generic_names": "phenobarbitone",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo RR50 differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_median_pct_change_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo MPC differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_seizure_freedom_maximum_effective_dose": "83.3 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Takami2019 phenobarbital 10 mg/kg IV 83.3%)",
    "enzyme_inducing_or_inhibiting": "Strong enzyme inducer: CYP and UGT pathways",
    "epilepsy_type": "Focal; Generalized tonic-clonic; Neonatal seizures; Status epilepticus",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review",
    "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; DEPENDENCE AND WITHDRAWAL REACTIONS AFTER USE OF SEZABY FOR A LONGER DURATION THAN RECOMMENDED; and ABUSE, MISUSE AND ADDICTION WITH UNAPPROVED USE IN ADOLESCENTS AND ADULTS Risks from Concomitant Use with Opioids Concomitant use of phenobarbital products, including SEZABY, and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. If a decision is made for concomitant use of these drugs, limit dosages and durations to the minimum required, and follow patients for signs and symptoms of respiratory depression and sedation [see Warnings and Precautions (5.1) and Drug Interactions (7.3)]. Dependence and Withdrawal Reactions After Use of SEZABY for a Longer Duration than Recommended The continued use of phenobarbital may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Although SEZABY is indicated only for short-term use [see Indications and Usage (1) and Dosage and Administration (2)], if used for a longer duration than recommended, abrupt discontinuation or rapid dosage reduction of SEZABY may precipitate acute withdrawal reactions, which can be life-threatening. For patients receiving SEZABY for longer duration than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue SEZABY [see Warnings and Precautions (5.2)]. Abuse, Misuse, and Addiction with Unapproved Use in Adolescents and Adults SEZABY is not approved for use in adolescents or adults. The unapproved use of SEZABY, in adolescents and adults exposes them to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of phenobarbital commonly involve concomitant use of other drugs, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes [see Warnings and Precaution (5.3)]. WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; DEPENDENCE AND WITHDRAWAL REACTIONS AFTER USE OF SEZABY FOR A LONGER DURATION THAN RECOMMENDED; and ABUSE, MISUSE, AND ADDICTION WITH UNAPPROVED USE IN ADOLESCENTS AND ADULTS See full prescribing information for complete boxed warning . Concomitant use of phenobarbital products, including SEZABY, and opioids may result in profound sedation, respiratory depression, coma, and death. If a decision is made to use concomitantly, limit dosages and durations to the minimum required, and monitor patients for respiratory depression and sedation. (5.1, 7.3) Although SEZABY is indicated only for short-term use (1, 2), if used for a longer duration than recommended, abrupt discontinuation or rapid dosage reduction may precipitate acute withdrawal reactions, which can be life-threatening. For patients receiving SEZABY for a longer duration than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue SEZABY. (5.2) SEZABY is not approved for use in adolescents or adults. The unapproved use of SEZABY in adolescents and adults exposes them to risks of abuse, misuse, and addiction, which can lead to overdose or death. (5.3)",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=boxed_warning_found; setid=8c7d0402-4977-4c25-bc4b-11db91339e9a; published=; title=These highlights do not include all the information needed to use SEZABY safely and effectively. See full prescribing information for SEZABY. SEZABY™ (phenobarbital sodium) for injection, for intravenous use, CIV Initial U.S. Approval: 2022; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a",
    "formulations_available": "Tablet; elixir/oral solution; IV/IM injection",
    "half_life_range": "53-118 h",
    "major_organ_for_metabolism": "Liver",
    "maximum_approved_daily_dose": "Individualized by serum level/tolerability; no single fixed max",
    "mechanism_confidence": "High",
    "mechanism_of_action": "Mechanism is not fully understood; barbiturate potentiation of synaptic inhibition through GABA-A receptors is the principal accepted antiseizure mechanism.",
    "mechanism_source": "FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "Individualized by serum level/tolerability; commonly 60 mg/day adult initial range",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "",
    "plot_diff_seizure_freedom_maximum_effective_dose": "Takami2019|83.3|https://pubmed.ncbi.nlm.nih.gov/30954360/|13",
    "pubmed_phase_ii_iii_rct_links": "Takami2019|https://pubmed.ncbi.nlm.nih.gov/30954360/; Crawley2000|https://pubmed.ncbi.nlm.nih.gov/10703801/; Bacon1981|https://pubmed.ncbi.nlm.nih.gov/6116084/",
    "pubmed_search_aliases": "",
    "qt_interval_effect": "No direct QT effect established",
    "trade_names": "Luminal; Phenobarb; Solfoton",
    "typical_doses_per_day": "Adults often 60-200 mg/day once daily or divided; pediatric weight-based",
    "year_fda_cleared": "1912 legacy; predates modern FDA approval system"
  },
  "generic_name": "phenobarbital",
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
      "column": "half_life_range",
      "current_value": "53-118 h",
      "details": {
        "checked": true,
        "missing_numbers": [
          "53",
          "118"
        ],
        "missing_terms": [],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5",
      "generic_name": "phenobarbital",
      "id": "source_fact_concordance_problem-431e2c430787",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: half_life_range was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: half_life_range was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "half_life_range could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "typical_doses_per_day",
      "current_value": "Adults often 60-200 mg/day once daily or divided; pediatric weight-based",
      "details": {
        "checked": true,
        "missing_numbers": [
          "200"
        ],
        "missing_terms": [
          "weight based"
        ],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5",
      "generic_name": "phenobarbital",
      "id": "source_fact_concordance_problem-c75a6b5d6c3b",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "typical_doses_per_day could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "year_fda_cleared",
      "current_value": "1912 legacy; predates modern FDA approval system",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1912"
        ],
        "missing_terms": [
          "legacy",
          "predates",
          "modern",
          "approval"
        ],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5",
      "generic_name": "phenobarbital",
      "id": "source_fact_concordance_problem-718752a7f920",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.",
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
        "brief_summary": "This study evaluated the efficacy and safety of two trough-ranges of everolimus given as adjunctive therapy in patients with tuberous sclerosis complex (TSC) who had refractory partial-onset seizures.\n\nThe study consisted of 4 phases for each patient Baseline phase:\\[From Screening Week -8 (V1) to randomization visit at Week 0 (V2)\\], Core phase \\[from randomization at Week 0 (V2) to Week 18 (V11)\\], Extension phase \\[from Week 18 (V11) until 48 weeks after the last patient had completed the core phase\\] and Post Extension phase \\[from end of Extension phase to end of study\\].",
        "interventions": [
          "RAD001",
          "Placebo",
          "Antiepileptic drug (1 to 3 only)",
          "open label RAD001 (only used for post-extension phase)"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT01713946",
        "new_reference_pmids": [
          "30169322",
          "27613521",
          "25682485"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "30169322",
          "27613521",
          "25682485"
        ],
        "title": "A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT01713946",
      "generic_name": "phenobarbital",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-4e9e485a3e95",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "This is a randomized, double-blind, parallel-group, Phase 3 study to evaluate the efficacy of the administration of phenobarbital Sodium Injection, United States Pharmacopeia, (USP), in participants who have suffered from a clinical seizure. As neonatal seizures can have long-term adverse effects, including death, placebo-controlled studies are not appropriate for this population. This study is designed to show phenobarbital is effective at preventing subsequent seizures by demonstrating greater efficacy at the higher (40 mg/kg) dose compared to the lower dose (20 mg/kg). It is important to note that, although phenobarbital is not approved for the treatment of neonatal seizures, it is commonly used for this indication and is considered the first-line therapy in the US and by the World Health Organization. The minimum recommended dose of phenobarbital used to treat neonatal seizures is 20 mg/kg. Therefore, the lower dose of phenobarbital used in this study is considered an \"effective\" dose for the treatment of neonatal seizures. The design of this study allows for assessment of the minimum recommended dose with the maximum recommended dose to show the increased efficacy of the high dose in various measures of reduction in seizures.",
        "interventions": [
          "Phenobarbital Sodium Injection"
        ],
        "masking": "DOUBLE",
        "nct_id": "NCT03602118",
        "new_reference_pmids": [],
        "overall_status": "WITHDRAWN",
        "phases": [
          "PHASE3"
        ],
        "pmids": [],
        "title": "Study to Evaluate Phenobarbital Sodium Injection for the Treatment of Neonatal Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT03602118",
      "generic_name": "phenobarbital",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-b42647f9800a",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Evaluate Phenobarbital Sodium Injection for the Treatment of Neonatal Seizures"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "Primary:\n\n\\- to evaluate the efficacy of phenobarbital in reducing seizure frequency.\n\nSecondary:\n\n* to confirm dose response relationship,\n* to assess the effects on Type I seizures,\n* to assess the safety of phenobarbital\n* to assess the drug tolerability.",
        "interventions": [
          "Phenobarbital",
          "Placebo tablet"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT01284556",
        "new_reference_pmids": [],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [],
        "title": "Evaluation Phenobarbital as Adjunctive Therapy in Participants With Partial Onset Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT01284556",
      "generic_name": "phenobarbital",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-8cae19b9ffa9",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Evaluation Phenobarbital as Adjunctive Therapy in Participants With Partial Onset Seizures"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "This is a randomized, double-blind, parallel-group, Phase 3 study to evaluate the efficacy of the administration of phenobarbital sodium injection in neonates who have suffered from electrographic or electroclinical seizure. As neonatal seizures can have long-term adverse effects, including death, placebo-controlled studies are not appropriate for this population. This study is designed to show intravenous phenobarbital is effective at preventing subsequent seizures by demonstrating greater efficacy at a higher dose compared to a lower dose.",
        "interventions": [
          "Phenobarbital Sodium Injection"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT04320940",
        "new_reference_pmids": [],
        "overall_status": "TERMINATED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [],
        "title": "Efficacy and Safety of Intravenous Phenobarbital in Neonatal Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT04320940",
      "generic_name": "phenobarbital",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-47a13d5b4f4d",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Intravenous Phenobarbital in Neonatal Seizures"
    },
    {
      "column": "qt_interval_effect",
      "current_value": "No direct QT effect established",
      "details": {
        "checked": true,
        "matched_terms": [],
        "missing_numbers": [],
        "missing_terms": [
          "direct"
        ],
        "numbers": [],
        "ok": false,
        "terms": [
          "direct"
        ]
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5",
      "generic_name": "phenobarbital",
      "id": "source_fact_concordance_problem-75185ea3a10c",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "qt_interval_effect could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=boxed_warning_found; setid=8c7d0402-4977-4c25-bc4b-11db91339e9a; published=; title=These highlights do not include all the information needed to use SEZABY safely and effectively. See full prescribing information for SEZABY. SEZABY™ (phenobarbital sodium) for injection, for intravenous use, CIV Initial U.S. Approval: 2022; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5",
      "generic_name": "phenobarbital",
      "id": "fda_warning_metadata_refresh-b88a4ceff2b0",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; DEPENDENCE AND WITHDRAWAL REACTIONS AFTER USE OF SEZABY FOR A LONGER DURATION THAN RECOMMENDED; and ABUSE, MISUSE AND ADDICTION WITH UNAPPROVED USE IN ADOLESCENTS AND ADULTS Risks from Concomitant Use with Opioids Concomitant use of phenobarbital products, including SEZABY, and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. If a decision is made for concomitant use of these drugs, limit dosages and durations to the minimum required, and follow patients for signs and symptoms of respiratory depression and sedation [see Warnings and Precautions (5.1) and Drug Interactions (7.3)]. Dependence and Withdrawal Reactions After Use of SEZABY for a Longer Duration than Recommended The continued use of phenobarbital may lead to clinically significant physical dependence. The risks of dependence and withdrawal increase with longer treatment duration and higher daily dose. Although SEZABY is indicated only for short-term use [see Indications and Usage (1) and Dosage and Administration (2)], if used for a longer duration than recommended, abrupt discontinuation or rapid dosage reduction of SEZABY may precipitate acute withdrawal reactions, which can be life-threatening. For patients receiving SEZABY for longer duration than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue SEZABY [see Warnings and Precautions (5.2)]. Abuse, Misuse, and Addiction with Unapproved Use in Adolescents and Adults SEZABY is not approved for use in adolescents or adults. The unapproved use of SEZABY, in adolescents and adults exposes them to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of phenobarbital commonly involve concomitant use of other drugs, alcohol, and/or illicit substances, which is associated with an increased frequency of serious adverse outcomes [see Warnings and Precaution (5.3)]. WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; DEPENDENCE AND WITHDRAWAL REACTIONS AFTER USE OF SEZABY FOR A LONGER DURATION THAN RECOMMENDED; and ABUSE, MISUSE, AND ADDICTION WITH UNAPPROVED USE IN ADOLESCENTS AND ADULTS See full prescribing information for complete boxed warning . Concomitant use of phenobarbital products, including SEZABY, and opioids may result in profound sedation, respiratory depression, coma, and death. If a decision is made to use concomitantly, limit dosages and durations to the minimum required, and monitor patients for respiratory depression and sedation. (5.1, 7.3) Although SEZABY is indicated only for short-term use (1, 2), if used for a longer duration than recommended, abrupt discontinuation or rapid dosage reduction may precipitate acute withdrawal reactions, which can be life-threatening. For patients receiving SEZABY for a longer duration than recommended, to reduce the risk of withdrawal reactions, use a gradual taper to discontinue SEZABY. (5.2) SEZABY is not approved for use in adolescents or adults. The unapproved use of SEZABY in adolescents and adults exposes them to risks of abuse, misuse, and addiction, which can lead to overdose or death. (5.3)",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=8c7d0402-4977-4c25-bc4b-11db91339e9a; effective_time=20251223; title=SEZABY / PHENOBARBITAL SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=8c7d0402-4977-4c25-bc4b-11db91339e9a; effective_time=20251223; title=SEZABY / PHENOBARBITAL SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [
    {
      "audit_note": "Abstract reports no post-dose seizures in 7 phenobarbital patients versus seizures in 5 of 6 placebo patients; converted to seizure-free patient rates.",
      "dose_or_regimen": "phenobarbital 10 mg/kg IV",
      "endpoint": "benign convulsions with mild gastroenteritis recurrence prevention",
      "generic_name": "phenobarbital",
      "label": "Takami2019",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "30954360",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/30954360/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "100.0",
      "sf_differential_percent": "83.3",
      "sf_included_in_csv_summary": "yes",
      "sf_placebo_percent": "16.7",
      "title": "Efficacy of phenobarbital for benign convulsions with mild gastroenteritis: A randomized, placebo-controlled trial."
    },
    {
      "audit_note": "Cerebral-malaria prophylaxis trial reports prevention of three-or-more seizures but increased mortality; not a seizure-frequency RR50/MPC or seizure-freedom endpoint.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "phenobarbital",
      "label": "Crawley2000",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "10703801",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/10703801/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Effect of phenobarbital on seizure frequency and mortality in childhood cerebral malaria: a randomised, controlled intervention study."
    },
    {
      "audit_note": "Febrile-convulsion prophylaxis trial reports subgroup recurrence reduction but no extractable active/placebo percentages in the abstract.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "phenobarbital",
      "label": "Bacon1981",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "6116084",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/6116084/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Placebo-controlled study of phenobarbitone and phenytoin in the prophylaxis of febrile convulsions."
    }
  ],
  "local_rct_audit_rows": [
    {
      "first_author": "Takami",
      "generic_name": "phenobarbital",
      "label": "Takami2019",
      "pmid": "30954360",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy of phenobarbital for benign convulsions with mild gastroenteritis: A randomized, placebo-controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/30954360/",
      "year": "2019"
    },
    {
      "first_author": "Crawley",
      "generic_name": "phenobarbital",
      "label": "Crawley2000",
      "pmid": "10703801",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Effect of phenobarbital on seizure frequency and mortality in childhood cerebral malaria: a randomised, controlled intervention study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10703801/",
      "year": "2000"
    },
    {
      "first_author": "Bacon",
      "generic_name": "phenobarbital",
      "label": "Bacon1981",
      "pmid": "6116084",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Placebo-controlled study of phenobarbitone and phenytoin in the prophylaxis of febrile convulsions.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/6116084/",
      "year": "1981"
    },
    {
      "first_author": "Mohammadi",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "42085751",
      "pub_types": "Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Investigating the effect of probiotics on seizure-related symptoms in children with medication-resistant epilepsy: a randomized clinical trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/42085751/",
      "year": "2026"
    },
    {
      "first_author": "Charalambous",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "41728120",
      "pub_types": "Journal Article",
      "reason": "not indexed/described as clinical trial",
      "status": "rejected",
      "title": "Antiseizure monotherapy with imepitoin or phenobarbital in feline idiopathic epilepsy: a multicenter, single-blinded, randomized and placebo-controlled study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/41728120/",
      "year": "2026"
    },
    {
      "first_author": "Moseley",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "38356105",
      "pub_types": "Randomized Controlled Trial; Journal Article; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Efficacy and Tolerability of Adjunctive Brivaracetam in Patients with Focal-Onset Seizures on Specific Concomitant Antiseizure Medications: Pooled Analysis of Double-Blind, Placebo-Controlled Trials.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/38356105/",
      "year": "2024"
    },
    {
      "first_author": "Nakatsuka",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "37674206",
      "pub_types": "Randomized Controlled Trial, Veterinary; Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Efficacy evaluation of a commercially available MCT enriched therapeutic diet on dogs with idiopathic epilepsy treated with zonisamide: a prospective, randomized, double-blinded, placebo-controlled, crossover dietary preliminary study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/37674206/",
      "year": "2023"
    },
    {
      "first_author": "Garcia",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "35967998",
      "pub_types": "Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Safety and efficacy of cannabidiol-cannabidiolic acid rich hemp extract in the treatment of refractory epileptic seizures in dogs.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/35967998/",
      "year": "2022"
    },
    {
      "first_author": "Hanael",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "35201995",
      "pub_types": "Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Telmisartan as an add-on treatment for dogs with refractory idiopathic epilepsy: a nonrandomized, uncontrolled, open-label clinical trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/35201995/",
      "year": "2022"
    },
    {
      "first_author": "Glass",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "34028496",
      "pub_types": "Comparative Study; Journal Article; Multicenter Study; Observational Study; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Safety of Early Discontinuation of Antiseizure Medication After Acute Symptomatic Neonatal Seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/34028496/",
      "year": "2021"
    },
    {
      "first_author": "Tavasolizadeh",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "32216594",
      "pub_types": "Letter; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "The effect of acidic beverage versus mineral water on the change in serum phenobarbital concentrations: a randomized clinical trial on children with seizure.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/32216594/",
      "year": "2020"
    },
    {
      "first_author": "Soul",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "33201535",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "A Pilot Randomized, Controlled, Double-Blind Trial of Bumetanide to Treat Neonatal Seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/33201535/",
      "year": "2020"
    },
    {
      "first_author": "Moseley",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "31675621",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Pharmacokinetic interaction of brivaracetam on other antiepileptic drugs in adults with focal seizures: Pooled analysis of data from randomized clinical trials.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31675621/",
      "year": "2019"
    },
    {
      "first_author": "Saxena",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "27889710",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Effect of Withholding Phenobarbitone Maintenance in Neonatal Seizures: A Randomized Controlled Trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/27889710/",
      "year": "2016"
    },
    {
      "first_author": "Schoemaker",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "27146213",
      "pub_types": "Clinical Trial, Phase II; Clinical Trial, Phase III; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Brivaracetam Population Pharmacokinetics and Exposure-Response Modeling in Adult Subjects With Partial-Onset Seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/27146213/",
      "year": "2016"
    },
    {
      "first_author": "Kälviäinen",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "26666500",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Brivaracetam in Unverricht-Lundborg disease (EPM1): Results from two randomized, double-blind, placebo-controlled studies.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/26666500/",
      "year": "2015"
    },
    {
      "first_author": "Law",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "26337751",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "A randomised trial of a medium-chain TAG diet as treatment for dogs with idiopathic epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/26337751/",
      "year": "2015"
    },
    {
      "first_author": "Lazzari",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "24010637",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Prevention of bone loss and vertebral fractures in patients with chronic epilepsy--antiepileptic drug and osteoporosis prevention trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/24010637/",
      "year": "2013"
    },
    {
      "first_author": "Muñana",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "22295869",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Evaluation of levetiracetam as adjunctive treatment for refractory canine epilepsy: a randomized, placebo-controlled, crossover trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/22295869/",
      "year": "2012"
    },
    {
      "first_author": "Pal",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "17356688",
      "pub_types": "Journal Article",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Phenobarbital for childhood epilepsy: systematic review.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17356688/",
      "year": "2006"
    },
    {
      "first_author": "Gidal",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "15823510",
      "pub_types": "Clinical Trial; Clinical Trial, Phase III; Comparative Study; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Effect of levetiracetam on the pharmacokinetics of adjunctive antiepileptic drugs: a pooled analysis of data from randomized clinical trials.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/15823510/",
      "year": "2005"
    },
    {
      "first_author": "PMID",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "11987312",
      "pub_types": "Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Gabapentin: new indication. Little impact on partial epilepsy in children between 3 and 12.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/11987312/",
      "year": "2002"
    },
    {
      "first_author": "De Santis",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "11903465",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Add-on phenytoin fails to prevent early seizures after surgery for supratentorial brain tumors: a randomized controlled study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/11903465/",
      "year": "2002"
    },
    {
      "first_author": "Spanaki",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "10534261",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, P.H.S.",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "The effect of vigabatrin (gamma-vinyl GABA) on cerebral blood flow and metabolism.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10534261/",
      "year": "1999"
    },
    {
      "first_author": "Sulzbacher",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "10416094",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, P.H.S.",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Late cognitive effects of early treatment with phenobarbital.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10416094/",
      "year": "1999"
    },
    {
      "first_author": "Wang",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "10082251",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Trial of antiepilepsirine (AES) in children with epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10082251/",
      "year": "1999"
    },
    {
      "first_author": "Thilothammal",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "8979563",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Comparison of phenobarbitone, phenytoin with sodium valproate: randomized, double-blind study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8979563/",
      "year": "1996"
    },
    {
      "first_author": "Botez",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "8269914",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Thiamine and folate treatment of chronic epileptic patients: a controlled study with the Wechsler IQ scale.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8269914/",
      "year": "1993"
    },
    {
      "first_author": "Rosman",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "8510706",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, P.H.S.",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "A controlled trial of diazepam administered during febrile illnesses to prevent recurrence of febrile seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8510706/",
      "year": "1993"
    },
    {
      "first_author": "Hirtz",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "8499051",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Does phenobarbital used for febrile seizures cause sleep disturbances?",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8499051/",
      "year": "1993"
    },
    {
      "first_author": "Farwell",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "2242106",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, P.H.S.",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Phenobarbital for febrile seizures--effects on intelligence and on seizure recurrence.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/2242106/",
      "year": "1990"
    },
    {
      "first_author": "Jawad",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "2498073",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Controlled trial of lamotrigine (Lamictal) for refractory partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/2498073/",
      "year": "1989"
    },
    {
      "first_author": "Schmidt",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "3511402",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Progabide for refractory partial epilepsy: a controlled add-on trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/3511402/",
      "year": "1986"
    },
    {
      "first_author": "Schmidt",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "6382068",
      "pub_types": "Clinical Trial; Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Progabide as an add-on drug for epilepsy refractory to high dose antiepileptic drug therapy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/6382068/",
      "year": "1984"
    },
    {
      "first_author": "Mamelle",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "6424041",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Prevention of recurrent febrile convulsions--a randomized therapeutic assay: sodium valproate, phenobarbital and placebo.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/6424041/",
      "year": "1984"
    },
    {
      "first_author": "Young",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "6848681",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, P.H.S.",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Failure of prophylactically administered phenytoin to prevent late posttraumatic seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/6848681/",
      "year": "1983"
    },
    {
      "first_author": "Camfield",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "6861601",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Normal serum 25-hydroxyvitamin D levels in phenobarbital-treated toddlers.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/6861601/",
      "year": "1983"
    },
    {
      "first_author": "Camfield",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "7381637",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "The first febrile seizure--antipyretic instruction plus either phenobarbital or placebo to prevent recurrence.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/7381637/",
      "year": "1980"
    },
    {
      "first_author": "Camfield",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "381616",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Side effects of phenobarbital in toddlers; behavioral and cognitive aspects.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/381616/",
      "year": "1979"
    },
    {
      "first_author": "Ahmad",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "22216504",
      "pub_types": "Controlled Clinical Trial; Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Controlled trial of frusemide as an antiepileptic drug in focal epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/22216504/",
      "year": "1976"
    },
    {
      "first_author": "Richens",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "1104059",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Controlled trial of sodium valproate in severe epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/1104059/",
      "year": "1975"
    },
    {
      "first_author": "Kutt",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "811074",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Carbamazepine in difficult to control epileptic out-patients.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/811074/",
      "year": "1975"
    },
    {
      "first_author": "Christiansen",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "4207965",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "\"Anticonvulsant action\" of vitamin D in epileptic patients? A controlled pilot study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/4207965/",
      "year": "1974"
    },
    {
      "first_author": "Christiansen",
      "generic_name": "phenobarbital",
      "label": "",
      "pmid": "4776883",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Incidence of anticonvulsant osteomalacia and effect of vitamin D: controlled therapeutic trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/4776883/",
      "year": "1973"
    }
  ],
  "possible_duplicate_name_hits": []
}
