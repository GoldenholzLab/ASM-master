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
    "adverse_symptoms_percentages": "CNS: dizziness 23%, CNS: somnolence 22%, constitutional: fatigue 15%, confusional state 9%, urologic: urinary retention 2%",
    "alternate_generic_names": "retigabine",
    "available_in_us": "No - formerly FDA-approved/marketed; withdrawn/discontinued",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "17-31 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Lim2016 ezogabine/retigabine 600 mg/day 31%; French2011 ezogabine/retigabine 1200 mg/day 26.6%; Brodie2010 ezogabine/retigabine 900 mg/day 28.1%; Porter2007 retigabine 1200 mg/day 17%)",
    "diff_median_pct_change_maximum_effective_dose": "11.69-26.8 % (drug minus placebo MPC differential at maximum effective dose/regimen: Lim2016 ezogabine/retigabine 600 mg/day 11.69%; French2011 ezogabine/retigabine 1200 mg/day 26.8%; Brodie2010 ezogabine/retigabine 900 mg/day 24%; Porter2007 retigabine 1200 mg/day 22%)",
    "diff_seizure_freedom_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "enzyme_inducing_or_inhibiting": "Not a major CYP inducer/inhibitor",
    "epilepsy_type": "Focal",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; EMA Trobalt withdrawal page; ILAE/GSK discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling",
    "fda_black_box_warning": "No current FDA/DailyMed label identified.",
    "fda_black_box_warning_source": "FDA/DailyMed search on 05-20-2026: no current label found for terms [ezogabine; retigabine; Potiga; Trobalt].",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Not available in US",
    "filter_enzyme_effect": "Inhibitor",
    "filter_epilepsy_type": "Focal",
    "filter_formulation": "Tablet",
    "filter_mechanism": "Potassium channel",
    "filter_metabolism": "Liver/hepatic",
    "filter_qt_effect": "QT prolongation",
    "filter_symptom_category": "CNS; Constitutional; Urologic",
    "formulations_available": "Tablet",
    "generic_name": "ezogabine",
    "half_life_range": "7-11 h",
    "major_organ_for_metabolism": "Liver",
    "maximum_approved_daily_dose": "1200 mg/day",
    "mechanism_confidence": "High",
    "mechanism_of_action": "Neuronal potassium-channel opener; primarily activates Kv7/KCNQ channels, stabilizing resting membrane potential and reducing neuronal excitability.",
    "mechanism_source": "EMA Trobalt withdrawal page; Sills and Rogawski 2020 ASM mechanism review",
    "mechanism_source_tier": "EMA/UK SmPC",
    "minimum_effective_dose": "600 mg/day",
    "plot_diff_50_responder_maximum_effective_dose": "Lim2016|31|https://pubmed.ncbi.nlm.nih.gov/27376872/|75; French2011|26.6|https://pubmed.ncbi.nlm.nih.gov/21451152/|305; Brodie2010|28.1|https://pubmed.ncbi.nlm.nih.gov/20944074/|538; Porter2007|17|https://pubmed.ncbi.nlm.nih.gov/17420403/|399",
    "plot_diff_median_pct_change_maximum_effective_dose": "Lim2016|11.69|https://pubmed.ncbi.nlm.nih.gov/27376872/|75; French2011|26.8|https://pubmed.ncbi.nlm.nih.gov/21451152/|305; Brodie2010|24|https://pubmed.ncbi.nlm.nih.gov/20944074/|538; Porter2007|22|https://pubmed.ncbi.nlm.nih.gov/17420403/|399",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "Lim2016|https://pubmed.ncbi.nlm.nih.gov/27376872/; French2011|https://pubmed.ncbi.nlm.nih.gov/21451152/; Brodie2010|https://pubmed.ncbi.nlm.nih.gov/20944074/; Porter2007|https://pubmed.ncbi.nlm.nih.gov/17420403/",
    "pubmed_search_aliases": "retigabine",
    "qt_interval_effect": "QT prolongation not typical; urinary/retinal toxicity drove withdrawal",
    "rct_pubmed_verification_notes": "PubMed loop 20/65 on 2026-05-15: 4 qualifying placebo-controlled randomized clinical trial report(s) retained from 10 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.",
    "status_or_notes": "Ezogabine (U.S. name; retigabine in Europe/INN) was an approved adjunctive ASM for partial-onset seizures; withdrawn/discontinued.",
    "trade_names": "Potiga; Trobalt",
    "typical_doses_per_day": "Withdrawn; historical adult dose 600-1200 mg/day divided TID",
    "year_fda_cleared": "2011 FDA approval; EMA Trobalt/retigabine marketing authorisation granted 2011 and withdrawn 2018"
  },
  "existing_pubmed_links": [
    {
      "entry": "Lim2016|https://pubmed.ncbi.nlm.nih.gov/27376872/",
      "label": "Lim2016",
      "pmid": "27376872",
      "url": "https://pubmed.ncbi.nlm.nih.gov/27376872/"
    },
    {
      "entry": "French2011|https://pubmed.ncbi.nlm.nih.gov/21451152/",
      "label": "French2011",
      "pmid": "21451152",
      "url": "https://pubmed.ncbi.nlm.nih.gov/21451152/"
    },
    {
      "entry": "Brodie2010|https://pubmed.ncbi.nlm.nih.gov/20944074/",
      "label": "Brodie2010",
      "pmid": "20944074",
      "url": "https://pubmed.ncbi.nlm.nih.gov/20944074/"
    },
    {
      "entry": "Porter2007|https://pubmed.ncbi.nlm.nih.gov/17420403/",
      "label": "Porter2007",
      "pmid": "17420403",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17420403/"
    }
  ],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "CNS: dizziness 23%, CNS: somnolence 22%, constitutional: fatigue 15%, confusional state 9%, urologic: urinary retention 2%",
    "alternate_generic_names": "retigabine",
    "available_in_us": "No - formerly FDA-approved/marketed; withdrawn/discontinued",
    "diff_50_responder_maximum_effective_dose": "17-31 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Lim2016 ezogabine/retigabine 600 mg/day 31%; French2011 ezogabine/retigabine 1200 mg/day 26.6%; Brodie2010 ezogabine/retigabine 900 mg/day 28.1%; Porter2007 retigabine 1200 mg/day 17%)",
    "diff_median_pct_change_maximum_effective_dose": "11.69-26.8 % (drug minus placebo MPC differential at maximum effective dose/regimen: Lim2016 ezogabine/retigabine 600 mg/day 11.69%; French2011 ezogabine/retigabine 1200 mg/day 26.8%; Brodie2010 ezogabine/retigabine 900 mg/day 24%; Porter2007 retigabine 1200 mg/day 22%)",
    "diff_seizure_freedom_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "enzyme_inducing_or_inhibiting": "Not a major CYP inducer/inhibitor",
    "epilepsy_type": "Focal",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; EMA Trobalt withdrawal page; ILAE/GSK discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling",
    "fda_black_box_warning": "No current FDA/DailyMed label identified.",
    "fda_black_box_warning_source": "FDA/DailyMed search on 05-20-2026: no current label found for terms [ezogabine; retigabine; Potiga; Trobalt].",
    "formulations_available": "Tablet",
    "half_life_range": "7-11 h",
    "major_organ_for_metabolism": "Liver",
    "maximum_approved_daily_dose": "1200 mg/day",
    "mechanism_confidence": "High",
    "mechanism_of_action": "Neuronal potassium-channel opener; primarily activates Kv7/KCNQ channels, stabilizing resting membrane potential and reducing neuronal excitability.",
    "mechanism_source": "EMA Trobalt withdrawal page; Sills and Rogawski 2020 ASM mechanism review",
    "mechanism_source_tier": "EMA/UK SmPC",
    "minimum_effective_dose": "600 mg/day",
    "plot_diff_50_responder_maximum_effective_dose": "Lim2016|31|https://pubmed.ncbi.nlm.nih.gov/27376872/|75; French2011|26.6|https://pubmed.ncbi.nlm.nih.gov/21451152/|305; Brodie2010|28.1|https://pubmed.ncbi.nlm.nih.gov/20944074/|538; Porter2007|17|https://pubmed.ncbi.nlm.nih.gov/17420403/|399",
    "plot_diff_median_pct_change_maximum_effective_dose": "Lim2016|11.69|https://pubmed.ncbi.nlm.nih.gov/27376872/|75; French2011|26.8|https://pubmed.ncbi.nlm.nih.gov/21451152/|305; Brodie2010|24|https://pubmed.ncbi.nlm.nih.gov/20944074/|538; Porter2007|22|https://pubmed.ncbi.nlm.nih.gov/17420403/|399",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "Lim2016|https://pubmed.ncbi.nlm.nih.gov/27376872/; French2011|https://pubmed.ncbi.nlm.nih.gov/21451152/; Brodie2010|https://pubmed.ncbi.nlm.nih.gov/20944074/; Porter2007|https://pubmed.ncbi.nlm.nih.gov/17420403/",
    "pubmed_search_aliases": "retigabine",
    "qt_interval_effect": "QT prolongation not typical; urinary/retinal toxicity drove withdrawal",
    "trade_names": "Potiga; Trobalt",
    "typical_doses_per_day": "Withdrawn; historical adult dose 600-1200 mg/day divided TID",
    "year_fda_cleared": "2011 FDA approval; EMA Trobalt/retigabine marketing authorisation granted 2011 and withdrawn 2018"
  },
  "generic_name": "ezogabine",
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
      "column": "pubmed_phase_ii_iii_rct_links",
      "current_value": "Brodie2010|https://pubmed.ncbi.nlm.nih.gov/20944074/",
      "details": {
        "article": {
          "abstract": "This study assessed the efficacy and safety of the neuronal potassium channel opener ezogabine (US adopted name; EZG)/retigabine (international nonproprietary name; RTG) as adjunctive therapy for refractory partial-onset seizures. This was a multicenter, randomized, double-blind, placebo-controlled trial in adults with ≥4 partial-onset seizures per month receiving 1 to 3 antiepileptic drugs. EZG (RTG) or placebo, 3 times daily, was titrated to 600 or 900 mg/d over 4 weeks, and continued during a 12-week maintenance phase. Median percentage seizure reductions from baseline and responder rates (≥50% reduction in baseline seizure frequency) were assessed. The intention-to-treat population comprised 538 patients (placebo, n = 179; 600 mg, n = 181; 900 mg, n = 178), 471 of whom (placebo, n = 164; 600 mg, n = 158; 900 mg, n = 149) entered the maintenance phase. Median percentage seizure reductions were greater in EZG (RTG)-treated patients (600 mg, 27.9%, p = 0.007; 900 mg, 39.9%, p < 0.001) compared with placebo (15.9%). Responder rates were higher in EZG (RTG)-treated patients (600 mg, 38.6%, p < 0.001; 900 mg, 47.0%, p < 0.001) than with placebo (18.9%). Treatment discontinuations due to adverse events (AEs) were more likely with EZG (RTG) than with placebo (placebo, 8%; 600 mg, 17%, 900 mg, 26%). The most commonly reported (>10%) AEs in the placebo, EZG (RTG) 600 mg/d, and EZG (RTG) 900 mg/d groups were dizziness (7%, 17%, 26%), somnolence (10%, 14%, 26%), headache (15%, 11%, 17%), and fatigue (3%, 15%, 17%). In this dose-ranging, placebo-controlled trial, adjunctive EZG (RTG) was effective and generally well tolerated in adults with refractory partial-onset seizures. This study provides Class II evidence that adjunctive EZG/RTG reduces the occurrence of partial-onset seizures.",
          "first_author": "Brodie",
          "pmid": "20944074",
          "pub_types": [
            "Journal Article",
            "Multicenter Study",
            "Randomized Controlled Trial",
            "Research Support, Non-U.S. Gov't"
          ],
          "title": "Efficacy and safety of adjunctive ezogabine (retigabine) in refractory partial epilepsy.",
          "year": "2010"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/20944074/",
      "generic_name": "ezogabine",
      "id": "rct_pubmed_concordance_problem-cd4231675472",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 20944074 needs manual review for ezogabine; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 20944074 needs manual review for ezogabine; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "This Phase 3 study is being conducted to evaluate the efficacy and safety of retigabine dosed at 900 mg/day and 600 mg/day, in three equally divided doses, compared with placebo in patients with epilepsy who are receiving up to three established antiepileptic drugs (AEDs).",
        "interventions": [
          "Retigabine",
          "Retigabine",
          "Placebo"
        ],
        "masking": "DOUBLE",
        "nct_id": "NCT00235755",
        "new_reference_pmids": [
          "23342983",
          "22428574",
          "22512894"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "20944074",
          "23342983",
          "22428574",
          "22512894"
        ],
        "title": "Retigabine Efficacy and Safety Trial for Partial Onset Refractory Seizures in Epilepsy"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT00235755",
      "generic_name": "ezogabine",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-9ee147cafa57",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Retigabine Efficacy and Safety Trial for Partial Onset Refractory Seizures in Epilepsy"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "This Phase 3 study is being conducted to evaluate the efficacy and safety of retigabine dosed at 1200 mg/day, in three equally divided doses, compared with placebo in patients with epilepsy who are receiving up to three established antiepileptic drugs (AEDs).",
        "interventions": [
          "Retigabine",
          "Placebo"
        ],
        "masking": "DOUBLE",
        "nct_id": "NCT00232596",
        "new_reference_pmids": [
          "22512894"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "22512894"
        ],
        "title": "Retigabine (Adjunctive Therapy) Efficacy and Safety Study for Partial Onset Refractory Seizures in Epilepsy"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT00232596",
      "generic_name": "ezogabine",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-804a4c097573",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Retigabine (Adjunctive Therapy) Efficacy and Safety Study for Partial Onset Refractory Seizures in Epilepsy"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "To investigate the potential antiseizure effects of adjunctive XEN496 (ezogabine) compared with placebo in children with KCNQ2 Developmental and Epileptic Encephalopathy (KCNQ2-DEE).",
        "interventions": [
          "XEN496",
          "Placebo"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT04639310",
        "new_reference_pmids": [],
        "overall_status": "TERMINATED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [],
        "title": "XEN496 (Ezogabine) in Children With KCNQ2 Developmental and Epileptic Encephalopathy"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT04639310",
      "generic_name": "ezogabine",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-24297109c97d",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: XEN496 (Ezogabine) in Children With KCNQ2 Developmental and Epileptic Encephalopathy"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "The immediate release (IR) formulation of retigabine has been shown to be superior to placebo as adjunctive therapy in 3 adequate and well-controlled studies in subjects with drug-resistant partial-onset seizures (POS) who had previously failed to respond to two or more antiepileptic drugs (AEDs) and were still having seizures despite current treatment with 1, 2, or 3 AEDs. However, of 1244 subjects randomly assigned to treatment in these 3 clinical studies, only 10 were Asian subjects and only 5 of these Asian subjects were randomly assigned to treatment with retigabine. Therefore, this Phase III study is being conducted to evaluate the efficacy, safety and tolerability, and health outcomes of retigabine, at doses of 900 mg/day and 600 mg/day, compared with placebo in adult Asian subjects with drug-resistant POS.",
        "interventions": [
          "Retigabine 900mg/day",
          "Retigabine 600mg/day",
          "Placebo"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT01648101",
        "new_reference_pmids": [
          "6790275"
        ],
        "overall_status": "TERMINATED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "6790275"
        ],
        "title": "Assessment of the Efficacy and Safety of 2 Doses of Retigabine Immediate Release (900 mg/Day and 600 mg/Day) Used as Adjunctive Therapy in Adult Asian Subjects With Drug-resistant Partial-onset Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT01648101",
      "generic_name": "ezogabine",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-a11753eb757c",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Assessment of the Efficacy and Safety of 2 Doses of Retigabine Immediate Release (900 mg/Day and 600 mg/Day) Used as Adjunctive Therapy in Adult Asian Subjects With Drug-resistant Partial-onset Seizures"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "NON_RANDOMIZED",
        "brief_summary": "This Phase 3 trial is an open-label extension study of the placebo-controlled, double-blind VRX-RET-E22-302 trial. Patients who have completed the VRX-RET-E22-302 trial and who meet inclusion and exclusion criteria will be treated with 600-1200 mg/day of retigabine as an adjunct therapy to their current antiepileptic drugs (AEDs) or vagal nerve stimulation. Treatment will be continued until the subject withdraws from the study or until the program is discontinued. Patients will be recruited from 55-60 sites in Europe, Israel, Australia, and South Africa. The primary objective of the study is to evaluate the safety and tolerability of long-term therapy with retigabine administered as adjunctive therapy in adult epilepsy patients with partial-onset seizures, who completed the double-blind Study VRX-RET-E22-302. Secondary objectives are: to evaluate efficacy of long-term treatment with retigabine and patient quality of life and to evaluate whether retinal pigmentation, unexplained vision loss, pigmentation of non-retinal ocular tissue, and discoloration of nails, lips, skin or mucosa change over time after discontinuation of retigabine.",
        "interventions": [
          "Retigabine (INN), Ezogabine (USAN)"
        ],
        "masking": "NONE",
        "nct_id": "NCT00310388",
        "new_reference_pmids": [],
        "overall_status": "TERMINATED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [],
        "title": "Open-Label Extension Study of the Phase 3 VRX-RET-E22-302 Double-Blind Trial. 115097"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT00310388",
      "generic_name": "ezogabine",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-3d783a7a5dc5",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Open-Label Extension Study of the Phase 3 VRX-RET-E22-302 Double-Blind Trial. 115097"
    },
    {
      "column": "evidence_sources",
      "current_value": "NCBI LiverTox anticonvulsants table; EMA Trobalt withdrawal page; ILAE/GSK discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling",
      "details": {},
      "evidence_url": "/Users/dgoldenh/Documents/GitHub/ASM-master/ASM-list.csv",
      "generic_name": "ezogabine",
      "id": "source_reference_gap-2373830e56b1",
      "kind": "source_reference_gap",
      "proposed_updates": {
        "evidence_sources": "EMA Trobalt withdrawal page; Sills and Rogawski 2020 ASM mechanism review"
      },
      "proposed_value": "EMA Trobalt withdrawal page; Sills and Rogawski 2020 ASM mechanism review",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "medium",
      "source": "Local source validation",
      "summary": "mechanism_source is not represented in evidence_sources."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed search on 05-19-2026: no current label found for terms [ezogabine; retigabine; Potiga; Trobalt].",
      "details": {},
      "evidence_url": "https://open.fda.gov/apis/drug/label/",
      "generic_name": "ezogabine",
      "id": "fda_warning_metadata_refresh-8c970146d582",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "No current FDA/openFDA label identified.",
        "fda_black_box_warning_source": "FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [ezogabine; retigabine; Potiga; Trobalt].",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [ezogabine; retigabine; Potiga; Trobalt].",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [
    {
      "audit_note": "Asian phase III trial was stopped early; abstract reports 600 mg/day as the higher-performing arm versus placebo.",
      "dose_or_regimen": "ezogabine/retigabine 600 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "ezogabine",
      "label": "Lim2016",
      "mpc_active_percent": "33.9",
      "mpc_differential_percent": "11.69",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "22.21",
      "pmid": "27376872",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/27376872/",
      "rr50_active_percent": "31.0",
      "rr50_differential_percent": "31.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "0.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy and safety of retigabine/ezogabine as adjunctive therapy in adult Asian patients with drug-resistant partial-onset seizures: A randomized, placebo-controlled Phase III study."
    },
    {
      "audit_note": "Abstract reports 1200 mg/day double-blind-period values.",
      "dose_or_regimen": "ezogabine/retigabine 1200 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "ezogabine",
      "label": "French2011",
      "mpc_active_percent": "44.3",
      "mpc_differential_percent": "26.8",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "17.5",
      "pmid": "21451152",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/21451152/",
      "rr50_active_percent": "44.4",
      "rr50_differential_percent": "26.6",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "17.8",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Randomized, double-blind, placebo-controlled trial of ezogabine (retigabine) in partial epilepsy."
    },
    {
      "audit_note": "Abstract reports the highest effective arm in this RCT: 900 mg/day responder and median seizure-reduction values.",
      "dose_or_regimen": "ezogabine/retigabine 900 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "ezogabine",
      "label": "Brodie2010",
      "mpc_active_percent": "39.9",
      "mpc_differential_percent": "24.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "15.9",
      "pmid": "20944074",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/20944074/",
      "rr50_active_percent": "47.0",
      "rr50_differential_percent": "28.1",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "18.9",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy and safety of adjunctive ezogabine (retigabine) in refractory partial epilepsy."
    },
    {
      "audit_note": "Abstract reports dose-ranging 1200 mg/day values.",
      "dose_or_regimen": "retigabine 1200 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "ezogabine",
      "label": "Porter2007",
      "mpc_active_percent": "35.0",
      "mpc_differential_percent": "22.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "13.0",
      "pmid": "17420403",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/17420403/",
      "rr50_active_percent": "33.0",
      "rr50_differential_percent": "17.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "16.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Randomized, multicenter, dose-ranging trial of retigabine for partial-onset seizures."
    }
  ],
  "local_rct_audit_rows": [
    {
      "first_author": "Lim",
      "generic_name": "ezogabine",
      "label": "Lim2016",
      "pmid": "27376872",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy and safety of retigabine/ezogabine as adjunctive therapy in adult Asian patients with drug-resistant partial-onset seizures: A randomized, placebo-controlled Phase III study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/27376872/",
      "year": "2016"
    },
    {
      "first_author": "French",
      "generic_name": "ezogabine",
      "label": "French2011",
      "pmid": "21451152",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Randomized, double-blind, placebo-controlled trial of ezogabine (retigabine) in partial epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/21451152/",
      "year": "2011"
    },
    {
      "first_author": "Brodie",
      "generic_name": "ezogabine",
      "label": "Brodie2010",
      "pmid": "20944074",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy and safety of adjunctive ezogabine (retigabine) in refractory partial epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/20944074/",
      "year": "2010"
    },
    {
      "first_author": "Porter",
      "generic_name": "ezogabine",
      "label": "Porter2007",
      "pmid": "17420403",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Randomized, multicenter, dose-ranging trial of retigabine for partial-onset seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17420403/",
      "year": "2007"
    },
    {
      "first_author": "Brickel",
      "generic_name": "ezogabine",
      "label": "",
      "pmid": "31731109",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Safety of retigabine in adults with partial-onset seizures after long-term exposure: focus on unexpected ophthalmological and dermatological events.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31731109/",
      "year": "2019"
    },
    {
      "first_author": "Ossemann",
      "generic_name": "ezogabine",
      "label": "",
      "pmid": "27448328",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Effect of a single dose of retigabine in cortical excitability parameters: A cross-over, double-blind placebo-controlled TMS study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/27448328/",
      "year": "2016"
    },
    {
      "first_author": "Tompson",
      "generic_name": "ezogabine",
      "label": "",
      "pmid": "23916044",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Efficacy and tolerability exposure-response relationship of retigabine (ezogabine) immediate-release tablets in patients with partial-onset seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/23916044/",
      "year": "2013"
    },
    {
      "first_author": "Crean",
      "generic_name": "ezogabine",
      "label": "",
      "pmid": "23328270",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "The effects of ethanol on the pharmacokinetics, pharmacodynamics, safety, and tolerability of ezogabine (retigabine).",
      "url": "https://pubmed.ncbi.nlm.nih.gov/23328270/",
      "year": "2013"
    },
    {
      "first_author": "Porter",
      "generic_name": "ezogabine",
      "label": "",
      "pmid": "22512894",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Retigabine as adjunctive therapy in adults with partial-onset seizures: integrated analysis of three pivotal controlled trials.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/22512894/",
      "year": "2012"
    },
    {
      "first_author": "Plosker",
      "generic_name": "ezogabine",
      "label": "",
      "pmid": "16800718",
      "pub_types": "Evaluation Study; Journal Article",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Retigabine: in partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/16800718/",
      "year": "2006"
    }
  ],
  "possible_duplicate_name_hits": []
}
