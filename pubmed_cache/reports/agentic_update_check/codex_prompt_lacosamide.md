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
    "adverse_symptoms_percentages": "CNS: dizziness 23-25%, CNS: somnolence 17%, CNS: headache 14%, GI: nausea 10%, ophthalmologic: diplopia 10%, cardiac: PR prolongation <1%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "3.9-21.8 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Makedonska2024 lacosamide 8-12 mg/kg/day 3.9%; Vossler2020 lacosamide up to 12 mg/kg/day or 400 mg/day 21.8%; Farkas2019 lacosamide target weight-based pediatric regimen 19.6%; Chung2010 lacosamide 400 mg/day 20%; Halasz2009 lacosamide 400 mg/day 14.7%; BenMenachem2007 lacosamide 400 mg/day 19%)",
    "diff_median_pct_change_maximum_effective_dose": "3.2-30 % (drug minus placebo MPC differential at maximum effective dose/regimen: Makedonska2024 lacosamide 8-12 mg/kg/day 3.2%; Farkas2019 lacosamide target weight-based pediatric regimen 30%; Chung2010 lacosamide 400 mg/day 16.5%; Halasz2009 lacosamide 400 mg/day 15.9%; BenMenachem2007 lacosamide 400 mg/day 29%)",
    "diff_seizure_freedom_maximum_effective_dose": "14.1 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Vossler2020 lacosamide up to 12 mg/kg/day or 400 mg/day 14.1%)",
    "enzyme_inducing_or_inhibiting": "Not a clinically meaningful enzyme inducer/inhibitor",
    "epilepsy_type": "Focal; Primary generalized tonic-clonic",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2; published=May 13, 2026; title=VIMPAT (LACOSAMIDE) TABLET, FILM COATED VIMPAT (LACOSAMIDE) INJECTION VIMPAT (LACOSAMIDE) SOLUTION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "Inducer; Inhibitor",
    "filter_epilepsy_type": "Focal; Primary generalized tonic-clonic",
    "filter_formulation": "Capsule; IV/IM injection; Liquid; Long acting; Tablet",
    "filter_mechanism": "Sodium channel",
    "filter_metabolism": "Liver/hepatic; Renal/no major metabolism",
    "filter_qt_effect": "PR interval effect; QT prolongation",
    "filter_symptom_category": "CNS; Cardiac; GI; Ophthalmologic",
    "formulations_available": "Tablet; oral solution; IV injection; extended-release capsule",
    "generic_name": "lacosamide",
    "half_life_range": "13 h",
    "major_organ_for_metabolism": "Liver and renal excretion",
    "maximum_approved_daily_dose": "400 mg/day",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Human antiseizure mechanism remains incompletely elucidated; lacosamide selectively enhances slow inactivation of voltage-gated sodium channels and stabilizes hyperexcitable neuronal membranes.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "200 mg/day",
    "plot_diff_50_responder_maximum_effective_dose": "Makedonska2024|3.9|https://pubmed.ncbi.nlm.nih.gov/38375995/|255; Vossler2020|21.8|https://pubmed.ncbi.nlm.nih.gov/32817358/|242; Farkas2019|19.6|https://pubmed.ncbi.nlm.nih.gov/31462582/|338; Chung2010|20|https://pubmed.ncbi.nlm.nih.gov/20132285/|405; Halasz2009|14.7|https://pubmed.ncbi.nlm.nih.gov/19183227/|485; BenMenachem2007|19|https://pubmed.ncbi.nlm.nih.gov/17635557/|418",
    "plot_diff_median_pct_change_maximum_effective_dose": "Makedonska2024|3.2|https://pubmed.ncbi.nlm.nih.gov/38375995/|255; Farkas2019|30|https://pubmed.ncbi.nlm.nih.gov/31462582/|338; Chung2010|16.5|https://pubmed.ncbi.nlm.nih.gov/20132285/|405; Halasz2009|15.9|https://pubmed.ncbi.nlm.nih.gov/19183227/|485; BenMenachem2007|29|https://pubmed.ncbi.nlm.nih.gov/17635557/|418",
    "plot_diff_seizure_freedom_maximum_effective_dose": "Vossler2020|14.1|https://pubmed.ncbi.nlm.nih.gov/32817358/|242",
    "pubmed_phase_ii_iii_rct_links": "Makedonska2024|https://pubmed.ncbi.nlm.nih.gov/38375995/; Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32817358/; Farkas2019|https://pubmed.ncbi.nlm.nih.gov/31462582/; FoldvarySchaefer2017|https://pubmed.ncbi.nlm.nih.gov/28866338/; Hong2016|https://pubmed.ncbi.nlm.nih.gov/27669155/; Rudd2015|https://pubmed.ncbi.nlm.nih.gov/25933358/; Chung2010|https://pubmed.ncbi.nlm.nih.gov/20132285/; Halasz2009|https://pubmed.ncbi.nlm.nih.gov/19183227/; BenMenachem2007|https://pubmed.ncbi.nlm.nih.gov/17635557/",
    "pubmed_search_aliases": "SPM 927",
    "qt_interval_effect": "No QT prolongation; can prolong PR interval",
    "rct_pubmed_verification_notes": "PubMed loop 26/65 on 2026-05-15: 9 qualifying placebo-controlled randomized clinical trial report(s) retained from 26 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.",
    "status_or_notes": "Current ASM for focal seizures; also used for primary generalized tonic-clonic seizures in some approvals.",
    "trade_names": "Motpoly XR; Vimpat",
    "typical_doses_per_day": "Adults: 200-400 mg/day; IR divided BID or XR once daily",
    "year_fda_cleared": "2008"
  },
  "existing_pubmed_links": [
    {
      "entry": "Makedonska2024|https://pubmed.ncbi.nlm.nih.gov/38375995/",
      "label": "Makedonska2024",
      "pmid": "38375995",
      "url": "https://pubmed.ncbi.nlm.nih.gov/38375995/"
    },
    {
      "entry": "Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32817358/",
      "label": "Vossler2020",
      "pmid": "32817358",
      "url": "https://pubmed.ncbi.nlm.nih.gov/32817358/"
    },
    {
      "entry": "Farkas2019|https://pubmed.ncbi.nlm.nih.gov/31462582/",
      "label": "Farkas2019",
      "pmid": "31462582",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31462582/"
    },
    {
      "entry": "FoldvarySchaefer2017|https://pubmed.ncbi.nlm.nih.gov/28866338/",
      "label": "FoldvarySchaefer2017",
      "pmid": "28866338",
      "url": "https://pubmed.ncbi.nlm.nih.gov/28866338/"
    },
    {
      "entry": "Hong2016|https://pubmed.ncbi.nlm.nih.gov/27669155/",
      "label": "Hong2016",
      "pmid": "27669155",
      "url": "https://pubmed.ncbi.nlm.nih.gov/27669155/"
    },
    {
      "entry": "Rudd2015|https://pubmed.ncbi.nlm.nih.gov/25933358/",
      "label": "Rudd2015",
      "pmid": "25933358",
      "url": "https://pubmed.ncbi.nlm.nih.gov/25933358/"
    },
    {
      "entry": "Chung2010|https://pubmed.ncbi.nlm.nih.gov/20132285/",
      "label": "Chung2010",
      "pmid": "20132285",
      "url": "https://pubmed.ncbi.nlm.nih.gov/20132285/"
    },
    {
      "entry": "Halasz2009|https://pubmed.ncbi.nlm.nih.gov/19183227/",
      "label": "Halasz2009",
      "pmid": "19183227",
      "url": "https://pubmed.ncbi.nlm.nih.gov/19183227/"
    },
    {
      "entry": "BenMenachem2007|https://pubmed.ncbi.nlm.nih.gov/17635557/",
      "label": "BenMenachem2007",
      "pmid": "17635557",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17635557/"
    }
  ],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "CNS: dizziness 23-25%, CNS: somnolence 17%, CNS: headache 14%, GI: nausea 10%, ophthalmologic: diplopia 10%, cardiac: PR prolongation <1%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "3.9-21.8 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Makedonska2024 lacosamide 8-12 mg/kg/day 3.9%; Vossler2020 lacosamide up to 12 mg/kg/day or 400 mg/day 21.8%; Farkas2019 lacosamide target weight-based pediatric regimen 19.6%; Chung2010 lacosamide 400 mg/day 20%; Halasz2009 lacosamide 400 mg/day 14.7%; BenMenachem2007 lacosamide 400 mg/day 19%)",
    "diff_median_pct_change_maximum_effective_dose": "3.2-30 % (drug minus placebo MPC differential at maximum effective dose/regimen: Makedonska2024 lacosamide 8-12 mg/kg/day 3.2%; Farkas2019 lacosamide target weight-based pediatric regimen 30%; Chung2010 lacosamide 400 mg/day 16.5%; Halasz2009 lacosamide 400 mg/day 15.9%; BenMenachem2007 lacosamide 400 mg/day 29%)",
    "diff_seizure_freedom_maximum_effective_dose": "14.1 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Vossler2020 lacosamide up to 12 mg/kg/day or 400 mg/day 14.1%)",
    "enzyme_inducing_or_inhibiting": "Not a clinically meaningful enzyme inducer/inhibitor",
    "epilepsy_type": "Focal; Primary generalized tonic-clonic",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2; published=May 13, 2026; title=VIMPAT (LACOSAMIDE) TABLET, FILM COATED VIMPAT (LACOSAMIDE) INJECTION VIMPAT (LACOSAMIDE) SOLUTION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2",
    "formulations_available": "Tablet; oral solution; IV injection; extended-release capsule",
    "half_life_range": "13 h",
    "major_organ_for_metabolism": "Liver and renal excretion",
    "maximum_approved_daily_dose": "400 mg/day",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Human antiseizure mechanism remains incompletely elucidated; lacosamide selectively enhances slow inactivation of voltage-gated sodium channels and stabilizes hyperexcitable neuronal membranes.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "200 mg/day",
    "plot_diff_50_responder_maximum_effective_dose": "Makedonska2024|3.9|https://pubmed.ncbi.nlm.nih.gov/38375995/|255; Vossler2020|21.8|https://pubmed.ncbi.nlm.nih.gov/32817358/|242; Farkas2019|19.6|https://pubmed.ncbi.nlm.nih.gov/31462582/|338; Chung2010|20|https://pubmed.ncbi.nlm.nih.gov/20132285/|405; Halasz2009|14.7|https://pubmed.ncbi.nlm.nih.gov/19183227/|485; BenMenachem2007|19|https://pubmed.ncbi.nlm.nih.gov/17635557/|418",
    "plot_diff_median_pct_change_maximum_effective_dose": "Makedonska2024|3.2|https://pubmed.ncbi.nlm.nih.gov/38375995/|255; Farkas2019|30|https://pubmed.ncbi.nlm.nih.gov/31462582/|338; Chung2010|16.5|https://pubmed.ncbi.nlm.nih.gov/20132285/|405; Halasz2009|15.9|https://pubmed.ncbi.nlm.nih.gov/19183227/|485; BenMenachem2007|29|https://pubmed.ncbi.nlm.nih.gov/17635557/|418",
    "plot_diff_seizure_freedom_maximum_effective_dose": "Vossler2020|14.1|https://pubmed.ncbi.nlm.nih.gov/32817358/|242",
    "pubmed_phase_ii_iii_rct_links": "Makedonska2024|https://pubmed.ncbi.nlm.nih.gov/38375995/; Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32817358/; Farkas2019|https://pubmed.ncbi.nlm.nih.gov/31462582/; FoldvarySchaefer2017|https://pubmed.ncbi.nlm.nih.gov/28866338/; Hong2016|https://pubmed.ncbi.nlm.nih.gov/27669155/; Rudd2015|https://pubmed.ncbi.nlm.nih.gov/25933358/; Chung2010|https://pubmed.ncbi.nlm.nih.gov/20132285/; Halasz2009|https://pubmed.ncbi.nlm.nih.gov/19183227/; BenMenachem2007|https://pubmed.ncbi.nlm.nih.gov/17635557/",
    "pubmed_search_aliases": "SPM 927",
    "qt_interval_effect": "No QT prolongation; can prolong PR interval",
    "trade_names": "Motpoly XR; Vimpat",
    "typical_doses_per_day": "Adults: 200-400 mg/day; IR divided BID or XR once daily",
    "year_fda_cleared": "2008"
  },
  "generic_name": "lacosamide",
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
      "current_value": "Makedonska2024|https://pubmed.ncbi.nlm.nih.gov/38375995/; Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32817358/; Farkas2019|https://pubmed.ncbi.nlm.nih.gov/31462582/; FoldvarySchaefer2017|https://pubmed.ncbi.nlm.nih.gov/28866338/; Hong2016|https://pubmed.ncbi.nlm.nih.gov/27669155/; Rudd2015|https://pubmed.ncbi.nlm.nih.gov/25933358/; Chung2010|https://pubmed.ncbi.nlm.nih.gov/20132285/; Halasz2009|https://pubmed.ncbi.nlm.nih.gov/19183227/; BenMenachem2007|https://pubmed.ncbi.nlm.nih.gov/17635557/",
      "details": {
        "article": {
          "abstract": "The objective of this study was to describe a priori protocol-defined analyses to evaluate the safety and tolerability of adjunctive oral lacosamide (200-600 mg/day) in adults (ages 16-70 years) with partial-onset seizures (POS) using data pooled from three similarly designed randomized, double-blind, placebo-controlled trials (SP667, SP754 [NCT00136019], SP755 [NCT00220415]). Patients with POS (≥2 years' duration, ≥2 previous antiepileptic drugs [AEDs]) uncontrolled by a stable dosing regimen of 1-3 concomitant AEDs were randomized to treatment with lacosamide at doses of 200 mg/day, 400 mg/day, or 600 mg/day, or placebo. Studies comprised a 4- to 6-week titration phase to target dose followed by a 12-week maintenance phase. Safety outcomes included treatment-emergent adverse events (TEAEs) of particular relevance to patients with POS, overall TEAEs, and discontinuations due to TEAEs. Post hoc analyses included evaluation of TEAEs potentially related to cognition and TEAEs leading to discontinuation analyzed by concomitant AEDs. One thousand three hundred eight patients were randomized to and received treatment; 944 to lacosamide and 364 to placebo. Most patients (84.4%) were taking 2 or 3 concomitant AEDs. The most common drug-associated TEAEs (reported by ≥5% of patients in any lacosamide dose group and with an incidence at least twice that reported for placebo during the treatment phase) were dizziness (30.6% for lacosamide vs 8.2% for placebo), nausea (11.4% vs 4.4%), and diplopia (10.5% vs 1.9%). Common drug-associated TEAEs generally appeared to be dose-related, and the incidence of each was lower during the 12-week maintenance phase than during the titration phase. Most TEAEs were either mild or moderate in intensity; severe TEAEs were predominantly observed with lacosamide 600 mg/day. No individual serious TEAE occurred in ≥1% of all lacosamide-treated patients. Treatment-emergent adverse events led to discontinuation in 8.1%, 17.2%, and 28.6% of the lacosamide 200-, 400-, and 600-mg/day groups, respectively (vs 4.9% of placebo). Few TEAEs were related to rash, weight loss/gain, changes in clinical chemistry parameters, or psychiatric disturbances, or were seizure-related. The odds of reporting any potential cognition-related TEAE vs placebo increased with dose and were similar between lacosamide doses of 200 and 400mg/day and placebo (odds ratio 1.3, 95% confidence interval 0.7-2.4). Discontinuations due to TEAEs based on most commonly used AEDs taken in combination with lacosamide (all doses combined) were carbamazepine (15.3% [51/334] vs 3.9% [5/129] placebo), lamotrigine (19.2% [56/291] vs 4.3% [5/117]), and levetiracetam (10.1% [28/278] vs 3.9% [4/103]). The safety and tolerability profile of adjunctive lacosamide in this detailed evaluation was similar to that observed in the individual double-blind trials. Adjunctive lacosamide was associated with TEAEs related to the nervous system and gastrointestinal tract, predominantly during titration. Copyright © 2015 The Authors. Published by Elsevier Inc. All rights reserved.",
          "first_author": "Biton",
          "pmid": "26414341",
          "pub_types": [
            "Journal Article",
            "Randomized Controlled Trial",
            "Research Support, Non-U.S. Gov't"
          ],
          "title": "Safety and tolerability of lacosamide as adjunctive therapy for adults with partial-onset seizures: Analysis of data pooled from three randomized, double-blind, placebo-controlled clinical trials.",
          "year": "2015"
        },
        "reason": "qualifying PubMed placebo-controlled randomized ASM trial report"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/26414341/",
      "generic_name": "lacosamide",
      "id": "new_pubmed_phase_ii_iii_rct-bf8800252922",
      "kind": "new_pubmed_phase_ii_iii_rct",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "pubmed_phase_ii_iii_rct_links": "Biton2015|https://pubmed.ncbi.nlm.nih.gov/26414341/",
        "rct_pubmed_verification_notes": "update_check on 05-19-2026: added PMID 26414341 after PubMed qualification as qualifying PubMed placebo-controlled randomized ASM trial report."
      },
      "proposed_value": "Biton2015|https://pubmed.ncbi.nlm.nih.gov/26414341/",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "high",
      "source": "PubMed",
      "summary": "New qualifying placebo-controlled randomized phase II/III ASM trial report: Safety and tolerability of lacosamide as adjunctive therapy for adults with partial-onset seizures: Analysis of data pooled from three randomized, double-blind, placebo-controlled clinical trials."
    },
    {
      "column": "pubmed_phase_ii_iii_rct_links",
      "current_value": "Makedonska2024|https://pubmed.ncbi.nlm.nih.gov/38375995/",
      "details": {
        "article": {
          "abstract": "Primary objective was to evaluate efficacy of lacosamide administered concomitantly with 1-3 antiseizure medications in young children with uncontrolled focal (partial-onset) seizures. Double-blind, parallel-group trial (SP0967: NCT02477839/2013-000717-20) conducted between June 2015 and May 2020 at hospitals and clinics in 25 countries. Patients (aged ≥1 month to <4 years) with uncontrolled focal seizures were randomized 1:1 to adjunctive lacosamide or placebo using an interactive voice/web response system and stratified by age. After a 20-day titration period, patients who reached target-dose range (8-12 mg/kg/day) entered a 7-day maintenance period. Region-specific primary efficacy variables were based on ≤72-h video-electroencephalograms: change in average daily frequency (ADF) of electrographic focal seizures as measured on end-of-maintenance video-electroencephalogram versus end-of-baseline video-electroencephalogram (United States); 50% responder rate (≥50% reduction in ADF of focal seizures) during maintenance (European Union). In total, 255 patients were randomized (lacosamide/placebo: 128/127) and received ≥1 trial medication dose. Percentage reduction in ADF of focal seizures for lacosamide (116 patients) versus placebo (120 patients) was 3.2% (95% confidence interval = -13.6 to 17.5, p = 0.69). 50% responder rate was 41.4% for lacosamide (116 patients), 37.5% for placebo (120 patients) (p = 0.58). Treatment-emergent adverse events were reported by 44.5% of lacosamide-treated patients (placebo 51.2%). Adjunctive lacosamide did not show superior efficacy versus placebo in young children with focal seizures. However, efficacy variables were potentially affected by high variability and low reliability between readers in video-electroencephalogram interpretation. Lacosamide was generally well tolerated; safety profile was acceptable and consistent with that in adults and children aged ≥4 years. © 2024 UCB Biopharma SRL. Annals of Clinical and Translational Neurology published by Wiley Periodicals LLC on behalf of American Neurological Association.",
          "first_author": "Makedonska",
          "pmid": "38375995",
          "pub_types": [
            "Randomized Controlled Trial",
            "Journal Article"
          ],
          "title": "Efficacy and tolerability of adjunctive lacosamide in patients aged <4 years with focal seizures.",
          "year": "2024"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/38375995/",
      "generic_name": "lacosamide",
      "id": "rct_pubmed_concordance_problem-4aece0205e3a",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 38375995 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 38375995 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "pubmed_phase_ii_iii_rct_links",
      "current_value": "Farkas2019|https://pubmed.ncbi.nlm.nih.gov/31462582/",
      "details": {
        "article": {
          "abstract": "To evaluate efficacy and tolerability of adjunctive lacosamide in children and adolescents with uncontrolled focal (partial-onset) seizures. In this double-blind trial (SP0969; NCT01921205), patients (age ≥4-<17 years) with uncontrolled focal seizures were randomized (1:1) to adjunctive lacosamide/placebo. After a 6-week titration, patients who reached the target dose range for their weight (<30 kg: 8-12 mg/kg/d oral solution; ≥30-<50 kg: 6-8 mg/kg/d oral solution; ≥50 kg: 300-400 mg/d tablets) entered a 10-week maintenance period. The primary outcome was change in focal seizure frequency per 28 days from baseline to maintenance. Three hundred forty-three patients were randomized; 306 (lacosamide 152 of 171 [88.9%]; placebo 154 of 172 [89.5%]) completed treatment (titration and maintenance). Adverse events (AEs) were the most common reasons for discontinuation during treatment (lacosamide 4.1%; placebo 5.8%). From baseline to maintenance, percent reduction in focal seizure frequency per 28 days for lacosamide (n = 170) vs placebo (n = 168) was 31.7% ( p = 0.0003). During maintenance, median percent reduction in focal seizure frequency per 28 days was 51.7% for lacosamide and 21.7% for placebo. Fifty percent responder rates (≥50% reduction) were 52.9% and 33.3% (odds ratio 2.17, p = 0.0006). During treatment, treatment-emergent AEs were reported by 67.8% lacosamide-treated patients (placebo 58.1%), most commonly (≥10%) somnolence (14.0%, placebo 5.2%) and dizziness (10.5%, placebo 3.5%). Adjunctive lacosamide was efficacious in reducing seizure frequency and generally well tolerated in patients (age ≥4-<17 years) with focal seizures. NCT01921205. This trial provides Class I evidence that for children and adolescents with uncontrolled focal seizures, adjunctive lacosamide reduces seizure frequency. Copyright © 2019 The Author(s). Published by Wolters Kluwer Health, Inc. on behalf of the American Academy of Neurology.",
          "first_author": "Farkas",
          "pmid": "31462582",
          "pub_types": [
            "Journal Article",
            "Multicenter Study",
            "Randomized Controlled Trial",
            "Research Support, Non-U.S. Gov't"
          ],
          "title": "Efficacy and tolerability of adjunctive lacosamide in pediatric patients with focal seizures.",
          "year": "2019"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/31462582/",
      "generic_name": "lacosamide",
      "id": "rct_pubmed_concordance_problem-fb99b1963c7c",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 31462582 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 31462582 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "pubmed_phase_ii_iii_rct_links",
      "current_value": "BenMenachem2007|https://pubmed.ncbi.nlm.nih.gov/17635557/",
      "details": {
        "article": {
          "abstract": "To evaluate the efficacy and safety of lacosamide when added to 1 or 2 antiepileptic drugs (AEDs) in adults with uncontrolled partial-onset seizures, and assess plasma concentrations of concomitant AEDs to determine any potential for drug interactions. During this multicenter, double-blind, placebo-controlled trial, patients were randomized to placebo or lacosamide 200, 400, or 600 mg/day after an 8-week baseline period. Lacosamide was titrated in weekly increments of 100 mg/day over 6 weeks and maintained for 12 weeks. Results were analyzed on an intention-to-treat basis. Four hundred eighteen patients were randomized and received trial medication; 312 completed the trial. The median percent reduction in seizure frequency per 28 days was 10%, 26%, 39%, and 40% in the placebo, lacosamide 200, 400, and 600 mg/day treatment groups, respectively. The median percent reduction in seizure frequency over placebo was significant for lacosamide 400 mg/day (p=0.0023) and 600 mg/day (p=0.0084). The 50% responder rates were 22%, 33%, 41%, and 38% for placebo, lacosamide 200, 400, and 600 mg/day, respectively. The 50% responder rate over placebo was significant for lacosamide 400 mg/day (p=0.0038) and 600 mg/day (p=0.0141). Adverse events that appeared dose-related included dizziness, nausea, fatigue, ataxia, vision abnormal, diplopia, and nystagmus. Lacosamide did not affect mean plasma concentrations of concomitantly administered AEDs. In this trial, adjunctive lacosamide significantly reduced seizure frequency in patients with uncontrolled partial-onset seizures. Along with favorable pharmacokinetic and tolerability profiles, these results support further development of lacosamide as an AED.",
          "first_author": "Ben-Menachem",
          "pmid": "17635557",
          "pub_types": [
            "Journal Article",
            "Multicenter Study",
            "Randomized Controlled Trial",
            "Research Support, Non-U.S. Gov't"
          ],
          "title": "Efficacy and safety of oral lacosamide as adjunctive therapy in adults with partial-onset seizures.",
          "year": "2007"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/17635557/",
      "generic_name": "lacosamide",
      "id": "rct_pubmed_concordance_problem-0a4a476b1dd1",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 17635557 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 17635557 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "year_fda_cleared",
      "current_value": "2008",
      "details": {
        "checked": true,
        "missing_numbers": [
          "2008"
        ],
        "missing_terms": [],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10",
      "generic_name": "lacosamide",
      "id": "source_fact_concordance_problem-ac3493599a74",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10); review current text before relying on it.",
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
        "brief_summary": "The purpose of this trial was to evaluate the safety and tolerability of SPM 927 when given as iv infusions compared with oral administration of the same dose strengths in subjects who were receiving oral SPM 927 for partial seizures with or without secondary generalization.\n\nTrial procedures will include medical history update, physical/ neurological exams, ECGs, blood /urine sample collections and seizure diary completion.\n\nSubjects completing the trial will return to the OLE trial to resume dosing with oral SPM 927.",
        "interventions": [
          "iv SPM 927 and oral placebo tablet",
          "oral SPM 927 tablet and iv placebo",
          "iv SPM 927 and oral placebo tablet",
          "oral SPM 927 tablet and iv placebo"
        ],
        "masking": "DOUBLE",
        "nct_id": "NCT00800215",
        "new_reference_pmids": [
          "17888078"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE2"
        ],
        "pmids": [
          "17888078"
        ],
        "title": "A Trial to Investigate the Safety, Tolerability and Pharmacokinetics of Intravenous SPM 927"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT00800215",
      "generic_name": "lacosamide",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-528188ee85a8",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Trial to Investigate the Safety, Tolerability and Pharmacokinetics of Intravenous SPM 927"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "The purpose of this study is to evaluate the efficacy and safety of 200 and 400 mg/day of orally administered Lacosamide as adjunctive therapy compared with placebo in Japanese and Chinese adults with uncontrolled Partial-Onset Seizures with or without secondary generalization.",
        "interventions": [
          "Lacosamide 50 mg",
          "Lacosamide 100 mg",
          "Placebo"
        ],
        "masking": "TRIPLE",
        "nct_id": "NCT01710657",
        "new_reference_pmids": [
          "23859801"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "23859801"
        ],
        "title": "A Trial to Evaluate the Efficacy and Safety of Adjunctive Therapy With Lacosamide in Adults With Partial-Onset Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT01710657",
      "generic_name": "lacosamide",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-b72a4e8b3b50",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Trial to Evaluate the Efficacy and Safety of Adjunctive Therapy With Lacosamide in Adults With Partial-Onset Seizures"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "Evaluating efficacy \\& safety of lacosamide versus Placebo in a blinded fashion as add-on Therapy for Primary Generalized Tonic-clonic (PGTC) seizures in subject 4 years of age or greater with idiopathic generalized epilepsy currently taking 1 to 3 antiepileptic drugs. Maximum duration of study drug administration is 28 weeks. Eligible subjects may choose to enter the open-label extension study after completion.",
        "interventions": [
          "Lacosamide Tablet",
          "Lasosamide Oral Solution",
          "Placebo Tablet",
          "Placebo Oral Solution"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT02408523",
        "new_reference_pmids": [],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [],
        "title": "A Study to Assess the Safety and Efficacy of Lacosamide Versus Placebo (a Pill Without Active Medication) in Patients With Idiopathic Generalised Epilepsy Who Are Already Taking Anti-epileptic Medications"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT02408523",
      "generic_name": "lacosamide",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-e8554c17c8ea",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Assess the Safety and Efficacy of Lacosamide Versus Placebo (a Pill Without Active Medication) in Patients With Idiopathic Generalised Epilepsy Who Are Already Taking Anti-epileptic Medications"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "The purpose of this trial is to assess the efficacy, safety and tolerability of lacosamide administered as add-on therapy with 1 to 3 anti-seizure medications. This trial is for children aged 1 month to less than 4 years with epilepsy who currently have uncontrolled partial-onset seizures.",
        "interventions": [
          "Lacosamide",
          "Placebo"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT02477839",
        "new_reference_pmids": [],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [],
        "title": "Efficacy and Safety of Lacosamide as Adjunctive Therapy in Subjects ≥1 Month to <4 Years With Partial-onset Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT02477839",
      "generic_name": "lacosamide",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-5009a84c2973",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Lacosamide as Adjunctive Therapy in Subjects ≥1 Month to <4 Years With Partial-onset Seizures"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "Study to evaluate the efficacy of Lacosamide (LCM) administered in addition to 1 to ≤3 other Anti-Epileptic Drugs in subjects with epilepsy ≥4 years to \\<17 years of age who currently have uncontrolled partial onset seizures.",
        "interventions": [
          "Lacosamide",
          "Placebo"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT01921205",
        "new_reference_pmids": [
          "34033237",
          "33998660"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "34033237",
          "33998660",
          "31462582"
        ],
        "title": "Study to Investigate Lacosamide as Add-on Therapy in Subjects ≥4 Years to <17 Years of Age With Partial Onset Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT01921205",
      "generic_name": "lacosamide",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-16953c5969f7",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Investigate Lacosamide as Add-on Therapy in Subjects ≥4 Years to <17 Years of Age With Partial Onset Seizures"
    },
    {
      "column": "trade_names",
      "current_value": "Motpoly XR; Vimpat",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22partial-onset+seizures%22&limit=100",
      "generic_name": "lacosamide",
      "id": "trade_name_addition-d6d72b750501",
      "kind": "trade_name_addition",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA",
        "trade_names": "LACOSAMIDE"
      },
      "proposed_value": "LACOSAMIDE",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "Source labels mention trade name(s) not present in CSV: LACOSAMIDE."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2; published=May 13, 2026; title=VIMPAT (LACOSAMIDE) TABLET, FILM COATED VIMPAT (LACOSAMIDE) INJECTION VIMPAT (LACOSAMIDE) SOLUTION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10",
      "generic_name": "lacosamide",
      "id": "fda_warning_metadata_refresh-141c484d2a9c",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "No FDA boxed warning identified in selected current FDA/openFDA label.",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=fb8235b4-4cd3-6f22-e053-6294a90a545c; effective_time=20250716; title=MOTPOLY XR / LACOSAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=fb8235b4-4cd3-6f22-e053-6294a90a545c; effective_time=20250716; title=MOTPOLY XR / LACOSAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [
    {
      "audit_note": "Abstract reports 50% responder rates and placebo-adjusted electrographic focal-seizure ADF reduction; efficacy was not statistically superior to placebo.",
      "dose_or_regimen": "lacosamide 8-12 mg/kg/day",
      "endpoint": "focal seizures in patients aged <4 years",
      "generic_name": "lacosamide",
      "label": "Makedonska2024",
      "mpc_active_percent": "",
      "mpc_differential_percent": "3.2",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "",
      "pmid": "38375995",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/38375995/",
      "rr50_active_percent": "41.4",
      "rr50_differential_percent": "3.9",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "37.5",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy and tolerability of adjunctive lacosamide in patients aged <4 years with focal seizures."
    },
    {
      "audit_note": "Abstract reports RR50 and Kaplan-Meier seizure freedom at day 166.",
      "dose_or_regimen": "lacosamide up to 12 mg/kg/day or 400 mg/day",
      "endpoint": "primary generalized tonic-clonic seizures",
      "generic_name": "lacosamide",
      "label": "Vossler2020",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "32817358",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/32817358/",
      "rr50_active_percent": "68.1",
      "rr50_differential_percent": "21.8",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "46.3",
      "sf_active_percent": "31.3",
      "sf_differential_percent": "14.1",
      "sf_included_in_csv_summary": "yes",
      "sf_placebo_percent": "17.2",
      "title": "Efficacy and safety of adjunctive lacosamide in the treatment of primary generalised tonic-clonic seizures: a double-blind, randomised, placebo-controlled trial."
    },
    {
      "audit_note": "Abstract reports pediatric target-regimen responder and median seizure-frequency reduction values.",
      "dose_or_regimen": "lacosamide target weight-based pediatric regimen",
      "endpoint": "pediatric focal seizures",
      "generic_name": "lacosamide",
      "label": "Farkas2019",
      "mpc_active_percent": "51.7",
      "mpc_differential_percent": "30.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "21.7",
      "pmid": "31462582",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/31462582/",
      "rr50_active_percent": "52.9",
      "rr50_differential_percent": "19.6",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "33.3",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy and tolerability of adjunctive lacosamide in pediatric patients with focal seizures."
    },
    {
      "audit_note": "Sleep/cognition study, not a seizure efficacy report.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "lacosamide",
      "label": "FoldvarySchaefer2017",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "28866338",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/28866338/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Wake up to sleep: The effects of lacosamide on daytime sleepiness in adults with epilepsy."
    },
    {
      "audit_note": "Abstract reports placebo-adjusted percentage reduction over placebo but not arm-specific responder or median values for the max-dose rollup.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "lacosamide",
      "label": "Hong2016",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "27669155",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/27669155/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy and safety of adjunctive lacosamide for the treatment of partial-onset seizures in Chinese and Japanese adults: A randomized, double-blind, placebo-controlled study."
    },
    {
      "audit_note": "Cardiac safety analysis, not a seizure efficacy report.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "lacosamide",
      "label": "Rudd2015",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "25933358",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/25933358/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Lacosamide cardiac safety: clinical trials in patients with partial-onset seizures."
    },
    {
      "audit_note": "Abstract reports 400 mg/day responder and median seizure-frequency reduction values.",
      "dose_or_regimen": "lacosamide 400 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "lacosamide",
      "label": "Chung2010",
      "mpc_active_percent": "37.3",
      "mpc_differential_percent": "16.5",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "20.8",
      "pmid": "20132285",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/20132285/",
      "rr50_active_percent": "38.3",
      "rr50_differential_percent": "20.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "18.3",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Lacosamide as adjunctive therapy for partial-onset seizures: a randomized controlled trial."
    },
    {
      "audit_note": "Abstract reports 400 mg/day responder and median seizure-frequency reduction values.",
      "dose_or_regimen": "lacosamide 400 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "lacosamide",
      "label": "Halasz2009",
      "mpc_active_percent": "36.4",
      "mpc_differential_percent": "15.9",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "20.5",
      "pmid": "19183227",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/19183227/",
      "rr50_active_percent": "40.5",
      "rr50_differential_percent": "14.7",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "25.8",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Adjunctive lacosamide for partial-onset seizures: Efficacy and safety results from a randomized controlled trial."
    },
    {
      "audit_note": "Abstract reports 400 mg/day responder and median seizure-frequency reduction values; 600 mg/day was not used because efficacy was not greater and tolerability was poorer.",
      "dose_or_regimen": "lacosamide 400 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "lacosamide",
      "label": "BenMenachem2007",
      "mpc_active_percent": "39.0",
      "mpc_differential_percent": "29.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "10.0",
      "pmid": "17635557",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/17635557/",
      "rr50_active_percent": "41.0",
      "rr50_differential_percent": "19.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "22.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy and safety of oral lacosamide as adjunctive therapy in adults with partial-onset seizures."
    }
  ],
  "local_rct_audit_rows": [
    {
      "first_author": "Makedonska",
      "generic_name": "lacosamide",
      "label": "Makedonska2024",
      "pmid": "38375995",
      "pub_types": "Randomized Controlled Trial; Journal Article",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy and tolerability of adjunctive lacosamide in patients aged <4 years with focal seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/38375995/",
      "year": "2024"
    },
    {
      "first_author": "Vossler",
      "generic_name": "lacosamide",
      "label": "Vossler2020",
      "pmid": "32817358",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't; Video-Audio Media",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy and safety of adjunctive lacosamide in the treatment of primary generalised tonic-clonic seizures: a double-blind, randomised, placebo-controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/32817358/",
      "year": "2020"
    },
    {
      "first_author": "Farkas",
      "generic_name": "lacosamide",
      "label": "Farkas2019",
      "pmid": "31462582",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy and tolerability of adjunctive lacosamide in pediatric patients with focal seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31462582/",
      "year": "2019"
    },
    {
      "first_author": "Foldvary-Schaefer",
      "generic_name": "lacosamide",
      "label": "FoldvarySchaefer2017",
      "pmid": "28866338",
      "pub_types": "Clinical Trial, Phase IV; Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Wake up to sleep: The effects of lacosamide on daytime sleepiness in adults with epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/28866338/",
      "year": "2017"
    },
    {
      "first_author": "Hong",
      "generic_name": "lacosamide",
      "label": "Hong2016",
      "pmid": "27669155",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy and safety of adjunctive lacosamide for the treatment of partial-onset seizures in Chinese and Japanese adults: A randomized, double-blind, placebo-controlled study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/27669155/",
      "year": "2016"
    },
    {
      "first_author": "Rudd",
      "generic_name": "lacosamide",
      "label": "Rudd2015",
      "pmid": "25933358",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Lacosamide cardiac safety: clinical trials in patients with partial-onset seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/25933358/",
      "year": "2015"
    },
    {
      "first_author": "Chung",
      "generic_name": "lacosamide",
      "label": "Chung2010",
      "pmid": "20132285",
      "pub_types": "Clinical Trial, Phase III; Comparative Study; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Lacosamide as adjunctive therapy for partial-onset seizures: a randomized controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/20132285/",
      "year": "2010"
    },
    {
      "first_author": "Halász",
      "generic_name": "lacosamide",
      "label": "Halasz2009",
      "pmid": "19183227",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Adjunctive lacosamide for partial-onset seizures: Efficacy and safety results from a randomized controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/19183227/",
      "year": "2009"
    },
    {
      "first_author": "Ben-Menachem",
      "generic_name": "lacosamide",
      "label": "BenMenachem2007",
      "pmid": "17635557",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy and safety of oral lacosamide as adjunctive therapy in adults with partial-onset seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17635557/",
      "year": "2007"
    },
    {
      "first_author": "Kerr",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "39052963",
      "pub_types": "Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Demonstration of Group-Level and Individual-Level Efficacy Using Time-to-Event Designs for Clinical Trials of Antiseizure Medications.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/39052963/",
      "year": "2024"
    },
    {
      "first_author": "Moseley",
      "generic_name": "lacosamide",
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
      "first_author": "Bozorg",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "38318689",
      "pub_types": "Randomized Controlled Trial; Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Pitfalls of using video-EEG for a trial endpoint in children aged <4 years with focal seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/38318689/",
      "year": "2024"
    },
    {
      "first_author": "Inoue",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "34246118",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Randomized Controlled Trial",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Safety and efficacy of adjunctive lacosamide in Chinese and Japanese adults with epilepsy and focal seizures: A long-term, open-label extension of a randomized, controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/34246118/",
      "year": "2021"
    },
    {
      "first_author": "Johnson",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "34033237",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Analyses of seizure responses supportive of a novel trial design to assess efficacy of antiepileptic drugs in infants and young children with epilepsy: Post hoc analyses of pediatric levetiracetam and lacosamide trials.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/34033237/",
      "year": "2021"
    },
    {
      "first_author": "Moseley",
      "generic_name": "lacosamide",
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
      "first_author": "Meador",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "26724782",
      "pub_types": "Clinical Trial, Phase II; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Cognitive effects of adjunctive perampanel for partial-onset seizures: A randomized trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/26724782/",
      "year": "2016"
    },
    {
      "first_author": "Biton",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "26414341",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Safety and tolerability of lacosamide as adjunctive therapy for adults with partial-onset seizures: Analysis of data pooled from three randomized, double-blind, placebo-controlled clinical trials.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/26414341/",
      "year": "2015"
    },
    {
      "first_author": "Kropeit",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "25932544",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Lacosamide cardiac safety: a thorough QT/QTc trial in healthy volunteers.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/25932544/",
      "year": "2015"
    },
    {
      "first_author": "Sperling",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "25082395",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Efficacy of lacosamide by focal seizure subtype.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/25082395/",
      "year": "2014"
    },
    {
      "first_author": "Lang",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "23778157",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Effects of lacosamide and carbamazepine on human motor cortex excitability: a double-blind, placebo-controlled transcranial magnetic stimulation study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/23778157/",
      "year": "2013"
    },
    {
      "first_author": "Sawh",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "23940830",
      "pub_types": "Journal Article",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Lacosamide adjunctive therapy for partial-onset seizures: a meta-analysis.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/23940830/",
      "year": "2013"
    },
    {
      "first_author": "Schmidt",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "23490458",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Clinical features associated with placebo response in refractory focal epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/23490458/",
      "year": "2013"
    },
    {
      "first_author": "Casas-Fernández",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "23193979",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Research Support, Non-U.S. Gov't",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Efficacy and tolerability of lacosamide in the concomitant treatment of 130 patients under 16 years of age with refractory epilepsy: a prospective, open-label, observational, multicenter study in Spain.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/23193979/",
      "year": "2012"
    },
    {
      "first_author": "Husain",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "22372628",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Research Support, Non-U.S. Gov't",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Long-term safety and efficacy in patients with uncontrolled partial-onset seizures treated with adjunctive lacosamide: results from a Phase III open-label extension trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/22372628/",
      "year": "2012"
    },
    {
      "first_author": "Chung",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "21090838",
      "pub_types": "Journal Article; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Examining the clinical utility of lacosamide: pooled analyses of three phase II/III clinical trials.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/21090838/",
      "year": "2010"
    },
    {
      "first_author": "Biton",
      "generic_name": "lacosamide",
      "label": "",
      "pmid": "17888078",
      "pub_types": "Comparative Study; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Intravenous lacosamide as replacement for oral lacosamide in patients with partial-onset seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17888078/",
      "year": "2007"
    }
  ],
  "possible_duplicate_name_hits": []
}
