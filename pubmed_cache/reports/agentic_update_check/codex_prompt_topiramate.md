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
    "adverse_symptoms_percentages": "Neurologic: paresthesia 51%, CNS: somnolence 29%, CNS: dizziness 25%, cognitive: psychomotor slowing 21%, constitutional: fatigue 16%, metabolic: weight loss 16%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "19-43 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Zhang2011 topiramate 200 mg/day 40.3%; Yen2000 topiramate 300 mg/day 34.8%; PMID1999 topiramate 600 mg/day 37.7%; Sachdeo1999 topiramate approximately 6 mg/kg/day 25%; Elterman1999 topiramate 6 mg/kg/day 19%; Biton1999 topiramate approximately 6 mg/kg/day 36%; Sharief1996 topiramate 400 mg/day 27%; Tassinari1996 topiramate 600 mg/day 37%; Faught1996 topiramate 400 mg/day 29%; Privitera1996 topiramate 600 mg/day 35%; BenMenachem1996 topiramate up to 800 mg/day 43%)",
    "diff_median_pct_change_maximum_effective_dose": "19.9-58 % (drug minus placebo MPC differential at maximum effective dose/regimen: Guberman2002 topiramate 200 mg/day 24%; PMID1999 topiramate 600 mg/day 42.2%; Sachdeo1999 topiramate approximately 6 mg/kg/day 19.9%; Elterman1999 topiramate 6 mg/kg/day 22.6%; Biton1999 topiramate approximately 6 mg/kg/day 47.7%; Sharief1996 topiramate 400 mg/day 40%; Tassinari1996 topiramate 600 mg/day 58%; Faught1996 topiramate 400 mg/day 35%; Privitera1996 topiramate 600 mg/day 40%; BenMenachem1996 topiramate up to 800 mg/day 54%)",
    "diff_seizure_freedom_maximum_effective_dose": "6.7 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: PMID1999 topiramate 600 mg/day 6.7%)",
    "enzyme_inducing_or_inhibiting": "Weak CYP3A inducer at higher doses; inhibits CYP2C19; weak carbonic anhydrase inhibitor",
    "epilepsy_type": "Focal; Primary generalized tonic-clonic; LGS; Generalized",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=e2a4df59-fead-4a01-9021-9eda02c48010; published=Mar 23, 2026; title=EPRONTIA (TOPIRAMATE) SOLUTION [AZURITY PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e2a4df59-fead-4a01-9021-9eda02c48010",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "Inhibitor; Weak inducer",
    "filter_epilepsy_type": "Focal; Generalized; LGS; Primary generalized tonic-clonic",
    "filter_formulation": "Capsule; Liquid; Long acting; Sprinkle/powder; Tablet",
    "filter_mechanism": "GABA; Glutamate receptor; Sodium channel",
    "filter_metabolism": "Liver/hepatic; Renal/no major metabolism",
    "filter_qt_effect": "No known meaningful QT effect",
    "filter_symptom_category": "CNS; Cognitive; Constitutional; Metabolic; Neurologic",
    "formulations_available": "Tablet; sprinkle capsule; extended-release capsule; oral solution",
    "generic_name": "topiramate",
    "half_life_range": "19-23 h",
    "major_organ_for_metabolism": "Partial liver metabolism; renal excretion",
    "maximum_approved_daily_dose": "400 mg/day for most adult epilepsy indications; up to 1000 mg/day in older adjunctive labeling",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Precise anticonvulsant mechanism is unknown; preclinical effects include voltage-dependent sodium-channel blockade, GABA-A augmentation, AMPA/kainate antagonism, and carbonic-anhydrase inhibition.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "200 mg/day common adult epilepsy maintenance target",
    "plot_diff_50_responder_maximum_effective_dose": "Zhang2011|40.3|https://pubmed.ncbi.nlm.nih.gov/21672344/|86; Yen2000|34.8|https://pubmed.ncbi.nlm.nih.gov/10999555/|46; Sachdeo1999|25|https://pubmed.ncbi.nlm.nih.gov/10371538/|98; PMID1999|37.7|https://pubmed.ncbi.nlm.nih.gov/10612342/|177; Elterman1999|19|https://pubmed.ncbi.nlm.nih.gov/10227615/|86; Biton1999|36|https://pubmed.ncbi.nlm.nih.gov/10227614/|80; Tassinari1996|37|https://pubmed.ncbi.nlm.nih.gov/8764816/|60; Sharief1996|27|https://pubmed.ncbi.nlm.nih.gov/8956919/|47; Privitera1996|35|https://pubmed.ncbi.nlm.nih.gov/8649569/|190; Faught1996|29|https://pubmed.ncbi.nlm.nih.gov/8649570/|181; BenMenachem1996|43|https://pubmed.ncbi.nlm.nih.gov/8641230/|56",
    "plot_diff_median_pct_change_maximum_effective_dose": "Guberman2002|24|https://pubmed.ncbi.nlm.nih.gov/12225311/|263; Sachdeo1999|19.9|https://pubmed.ncbi.nlm.nih.gov/10371538/|98; PMID1999|42.2|https://pubmed.ncbi.nlm.nih.gov/10612342/|177; Elterman1999|22.6|https://pubmed.ncbi.nlm.nih.gov/10227615/|86; Biton1999|47.7|https://pubmed.ncbi.nlm.nih.gov/10227614/|80; Tassinari1996|58|https://pubmed.ncbi.nlm.nih.gov/8764816/|60; Sharief1996|40|https://pubmed.ncbi.nlm.nih.gov/8956919/|47; Privitera1996|40|https://pubmed.ncbi.nlm.nih.gov/8649569/|190; Faught1996|35|https://pubmed.ncbi.nlm.nih.gov/8649570/|181; BenMenachem1996|54|https://pubmed.ncbi.nlm.nih.gov/8641230/|56",
    "plot_diff_seizure_freedom_maximum_effective_dose": "PMID1999|6.7|https://pubmed.ncbi.nlm.nih.gov/10612342/|177",
    "pubmed_phase_ii_iii_rct_links": "Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/; Novotny2010|https://pubmed.ncbi.nlm.nih.gov/20089937/; Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/; Yen2000|https://pubmed.ncbi.nlm.nih.gov/10999555/; Sachdeo1999|https://pubmed.ncbi.nlm.nih.gov/10371538/; PMID1999|https://pubmed.ncbi.nlm.nih.gov/10612342/; Elterman1999|https://pubmed.ncbi.nlm.nih.gov/10227615/; Biton1999|https://pubmed.ncbi.nlm.nih.gov/10227614/; Faught1997|https://pubmed.ncbi.nlm.nih.gov/9092954/; Tassinari1996|https://pubmed.ncbi.nlm.nih.gov/8764816/; Sharief1996|https://pubmed.ncbi.nlm.nih.gov/8956919/; Privitera1996|https://pubmed.ncbi.nlm.nih.gov/8649569/; Faught1996|https://pubmed.ncbi.nlm.nih.gov/8649570/; BenMenachem1996|https://pubmed.ncbi.nlm.nih.gov/8641230/",
    "pubmed_search_aliases": "",
    "qt_interval_effect": "No clinically meaningful QT effect established",
    "rct_pubmed_verification_notes": "PubMed loop 59/65 on 2026-05-15: 14 qualifying placebo-controlled randomized clinical trial report(s) retained from 51 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.",
    "status_or_notes": "Current broad-use ASM; also used for migraine prevention and weight-loss combination therapy.",
    "trade_names": "Eprontia; Qudexy XR; Topamax; Topamax Sprinkle; Trokendi XR",
    "typical_doses_per_day": "Adults epilepsy: 200-400 mg/day divided or once daily XR; higher for some adjunctive regimens",
    "year_fda_cleared": "1996"
  },
  "existing_pubmed_links": [
    {
      "entry": "Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/",
      "label": "Zhang2011",
      "pmid": "21672344",
      "url": "https://pubmed.ncbi.nlm.nih.gov/21672344/"
    },
    {
      "entry": "Novotny2010|https://pubmed.ncbi.nlm.nih.gov/20089937/",
      "label": "Novotny2010",
      "pmid": "20089937",
      "url": "https://pubmed.ncbi.nlm.nih.gov/20089937/"
    },
    {
      "entry": "Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/",
      "label": "Guberman2002",
      "pmid": "12225311",
      "url": "https://pubmed.ncbi.nlm.nih.gov/12225311/"
    },
    {
      "entry": "Yen2000|https://pubmed.ncbi.nlm.nih.gov/10999555/",
      "label": "Yen2000",
      "pmid": "10999555",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10999555/"
    },
    {
      "entry": "Sachdeo1999|https://pubmed.ncbi.nlm.nih.gov/10371538/",
      "label": "Sachdeo1999",
      "pmid": "10371538",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10371538/"
    },
    {
      "entry": "PMID1999|https://pubmed.ncbi.nlm.nih.gov/10612342/",
      "label": "PMID1999",
      "pmid": "10612342",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10612342/"
    },
    {
      "entry": "Elterman1999|https://pubmed.ncbi.nlm.nih.gov/10227615/",
      "label": "Elterman1999",
      "pmid": "10227615",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10227615/"
    },
    {
      "entry": "Biton1999|https://pubmed.ncbi.nlm.nih.gov/10227614/",
      "label": "Biton1999",
      "pmid": "10227614",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10227614/"
    },
    {
      "entry": "Faught1997|https://pubmed.ncbi.nlm.nih.gov/9092954/",
      "label": "Faught1997",
      "pmid": "9092954",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9092954/"
    },
    {
      "entry": "Tassinari1996|https://pubmed.ncbi.nlm.nih.gov/8764816/",
      "label": "Tassinari1996",
      "pmid": "8764816",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8764816/"
    },
    {
      "entry": "Sharief1996|https://pubmed.ncbi.nlm.nih.gov/8956919/",
      "label": "Sharief1996",
      "pmid": "8956919",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8956919/"
    },
    {
      "entry": "Privitera1996|https://pubmed.ncbi.nlm.nih.gov/8649569/",
      "label": "Privitera1996",
      "pmid": "8649569",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8649569/"
    },
    {
      "entry": "Faught1996|https://pubmed.ncbi.nlm.nih.gov/8649570/",
      "label": "Faught1996",
      "pmid": "8649570",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8649570/"
    },
    {
      "entry": "BenMenachem1996|https://pubmed.ncbi.nlm.nih.gov/8641230/",
      "label": "BenMenachem1996",
      "pmid": "8641230",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8641230/"
    }
  ],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "Neurologic: paresthesia 51%, CNS: somnolence 29%, CNS: dizziness 25%, cognitive: psychomotor slowing 21%, constitutional: fatigue 16%, metabolic: weight loss 16%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "19-43 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Zhang2011 topiramate 200 mg/day 40.3%; Yen2000 topiramate 300 mg/day 34.8%; PMID1999 topiramate 600 mg/day 37.7%; Sachdeo1999 topiramate approximately 6 mg/kg/day 25%; Elterman1999 topiramate 6 mg/kg/day 19%; Biton1999 topiramate approximately 6 mg/kg/day 36%; Sharief1996 topiramate 400 mg/day 27%; Tassinari1996 topiramate 600 mg/day 37%; Faught1996 topiramate 400 mg/day 29%; Privitera1996 topiramate 600 mg/day 35%; BenMenachem1996 topiramate up to 800 mg/day 43%)",
    "diff_median_pct_change_maximum_effective_dose": "19.9-58 % (drug minus placebo MPC differential at maximum effective dose/regimen: Guberman2002 topiramate 200 mg/day 24%; PMID1999 topiramate 600 mg/day 42.2%; Sachdeo1999 topiramate approximately 6 mg/kg/day 19.9%; Elterman1999 topiramate 6 mg/kg/day 22.6%; Biton1999 topiramate approximately 6 mg/kg/day 47.7%; Sharief1996 topiramate 400 mg/day 40%; Tassinari1996 topiramate 600 mg/day 58%; Faught1996 topiramate 400 mg/day 35%; Privitera1996 topiramate 600 mg/day 40%; BenMenachem1996 topiramate up to 800 mg/day 54%)",
    "diff_seizure_freedom_maximum_effective_dose": "6.7 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: PMID1999 topiramate 600 mg/day 6.7%)",
    "enzyme_inducing_or_inhibiting": "Weak CYP3A inducer at higher doses; inhibits CYP2C19; weak carbonic anhydrase inhibitor",
    "epilepsy_type": "Focal; Primary generalized tonic-clonic; LGS; Generalized",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=e2a4df59-fead-4a01-9021-9eda02c48010; published=Mar 23, 2026; title=EPRONTIA (TOPIRAMATE) SOLUTION [AZURITY PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e2a4df59-fead-4a01-9021-9eda02c48010",
    "formulations_available": "Tablet; sprinkle capsule; extended-release capsule; oral solution",
    "half_life_range": "19-23 h",
    "major_organ_for_metabolism": "Partial liver metabolism; renal excretion",
    "maximum_approved_daily_dose": "400 mg/day for most adult epilepsy indications; up to 1000 mg/day in older adjunctive labeling",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Precise anticonvulsant mechanism is unknown; preclinical effects include voltage-dependent sodium-channel blockade, GABA-A augmentation, AMPA/kainate antagonism, and carbonic-anhydrase inhibition.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "200 mg/day common adult epilepsy maintenance target",
    "plot_diff_50_responder_maximum_effective_dose": "Zhang2011|40.3|https://pubmed.ncbi.nlm.nih.gov/21672344/|86; Yen2000|34.8|https://pubmed.ncbi.nlm.nih.gov/10999555/|46; Sachdeo1999|25|https://pubmed.ncbi.nlm.nih.gov/10371538/|98; PMID1999|37.7|https://pubmed.ncbi.nlm.nih.gov/10612342/|177; Elterman1999|19|https://pubmed.ncbi.nlm.nih.gov/10227615/|86; Biton1999|36|https://pubmed.ncbi.nlm.nih.gov/10227614/|80; Tassinari1996|37|https://pubmed.ncbi.nlm.nih.gov/8764816/|60; Sharief1996|27|https://pubmed.ncbi.nlm.nih.gov/8956919/|47; Privitera1996|35|https://pubmed.ncbi.nlm.nih.gov/8649569/|190; Faught1996|29|https://pubmed.ncbi.nlm.nih.gov/8649570/|181; BenMenachem1996|43|https://pubmed.ncbi.nlm.nih.gov/8641230/|56",
    "plot_diff_median_pct_change_maximum_effective_dose": "Guberman2002|24|https://pubmed.ncbi.nlm.nih.gov/12225311/|263; Sachdeo1999|19.9|https://pubmed.ncbi.nlm.nih.gov/10371538/|98; PMID1999|42.2|https://pubmed.ncbi.nlm.nih.gov/10612342/|177; Elterman1999|22.6|https://pubmed.ncbi.nlm.nih.gov/10227615/|86; Biton1999|47.7|https://pubmed.ncbi.nlm.nih.gov/10227614/|80; Tassinari1996|58|https://pubmed.ncbi.nlm.nih.gov/8764816/|60; Sharief1996|40|https://pubmed.ncbi.nlm.nih.gov/8956919/|47; Privitera1996|40|https://pubmed.ncbi.nlm.nih.gov/8649569/|190; Faught1996|35|https://pubmed.ncbi.nlm.nih.gov/8649570/|181; BenMenachem1996|54|https://pubmed.ncbi.nlm.nih.gov/8641230/|56",
    "plot_diff_seizure_freedom_maximum_effective_dose": "PMID1999|6.7|https://pubmed.ncbi.nlm.nih.gov/10612342/|177",
    "pubmed_phase_ii_iii_rct_links": "Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/; Novotny2010|https://pubmed.ncbi.nlm.nih.gov/20089937/; Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/; Yen2000|https://pubmed.ncbi.nlm.nih.gov/10999555/; Sachdeo1999|https://pubmed.ncbi.nlm.nih.gov/10371538/; PMID1999|https://pubmed.ncbi.nlm.nih.gov/10612342/; Elterman1999|https://pubmed.ncbi.nlm.nih.gov/10227615/; Biton1999|https://pubmed.ncbi.nlm.nih.gov/10227614/; Faught1997|https://pubmed.ncbi.nlm.nih.gov/9092954/; Tassinari1996|https://pubmed.ncbi.nlm.nih.gov/8764816/; Sharief1996|https://pubmed.ncbi.nlm.nih.gov/8956919/; Privitera1996|https://pubmed.ncbi.nlm.nih.gov/8649569/; Faught1996|https://pubmed.ncbi.nlm.nih.gov/8649570/; BenMenachem1996|https://pubmed.ncbi.nlm.nih.gov/8641230/",
    "pubmed_search_aliases": "",
    "qt_interval_effect": "No clinically meaningful QT effect established",
    "trade_names": "Eprontia; Qudexy XR; Topamax; Topamax Sprinkle; Trokendi XR",
    "typical_doses_per_day": "Adults epilepsy: 200-400 mg/day divided or once daily XR; higher for some adjunctive regimens",
    "year_fda_cleared": "1996"
  },
  "generic_name": "topiramate",
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
      "current_value": "Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/; Novotny2010|https://pubmed.ncbi.nlm.nih.gov/20089937/; Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/; Yen2000|https://pubmed.ncbi.nlm.nih.gov/10999555/; Sachdeo1999|https://pubmed.ncbi.nlm.nih.gov/10371538/; PMID1999|https://pubmed.ncbi.nlm.nih.gov/10612342/; Elterman1999|https://pubmed.ncbi.nlm.nih.gov/10227615/; Biton1999|https://pubmed.ncbi.nlm.nih.gov/10227614/; Faught1997|https://pubmed.ncbi.nlm.nih.gov/9092954/; Tassinari1996|https://pubmed.ncbi.nlm.nih.gov/8764816/; Sharief1996|https://pubmed.ncbi.nlm.nih.gov/8956919/; Privitera1996|https://pubmed.ncbi.nlm.nih.gov/8649569/; Faught1996|https://pubmed.ncbi.nlm.nih.gov/8649570/; BenMenachem1996|https://pubmed.ncbi.nlm.nih.gov/8641230/",
      "details": {
        "article": {
          "abstract": "This randomized, double-blind, placebo-controlled UK trial evaluated the effect of topiramate as add-on therapy on seizure frequency, seizure severity, and quality of life in patients with epilepsy and intellectual disability. There were three phases: 4 weeks baseline, 18 weeks titration to 200-400 mg topiramate/day (adults) or 5-9 mg/kg/day (children), 12 weeks maintenance. Recruitment was low (88/120); analyses were underpowered. Seizure frequency varied enormously (median 17.7, maximum 1706.2). There was no significant difference in reduction in mean total seizure frequency or number of responders between the groups. Topiramate reduced seizure frequency by >30% from baseline (placebo 1%); post hoc analyses showed a trend toward significance (R ratio, P=0.052). There were no significant differences between the groups with respect to mean seizure severity or other outcome measures. Topiramate was generally well tolerated; body weight (P=0.015) and systolic blood pressure (P=0.043) were reduced. The study suggests that topiramate reduces seizure frequency in patients with epilepsy and intellectual disability without the added burden of behavior effects, and was potentially advantageous to physical well-being.",
          "first_author": "Kerr",
          "pmid": "16140593",
          "pub_types": [
            "Journal Article",
            "Multicenter Study",
            "Randomized Controlled Trial",
            "Research Support, Non-U.S. Gov't"
          ],
          "title": "A randomized, double-blind, placebo-controlled trial of topiramate in adults with epilepsy and intellectual disability: impact on seizures, severity, and quality of life.",
          "year": "2005"
        },
        "reason": "qualifying PubMed placebo-controlled randomized ASM trial report"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/16140593/",
      "generic_name": "topiramate",
      "id": "new_pubmed_phase_ii_iii_rct-8b994db9a357",
      "kind": "new_pubmed_phase_ii_iii_rct",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "pubmed_phase_ii_iii_rct_links": "Kerr2005|https://pubmed.ncbi.nlm.nih.gov/16140593/",
        "rct_pubmed_verification_notes": "update_check on 05-19-2026: added PMID 16140593 after PubMed qualification as qualifying PubMed placebo-controlled randomized ASM trial report."
      },
      "proposed_value": "Kerr2005|https://pubmed.ncbi.nlm.nih.gov/16140593/",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "high",
      "source": "PubMed",
      "summary": "New qualifying placebo-controlled randomized phase II/III ASM trial report: A randomized, double-blind, placebo-controlled trial of topiramate in adults with epilepsy and intellectual disability: impact on seizures, severity, and quality of life."
    },
    {
      "column": "pubmed_phase_ii_iii_rct_links",
      "current_value": "Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/",
      "details": {
        "article": {
          "abstract": "This double-blind, placebo-controlled study investigated the efficacy and tolerability of adjunctive topiramate in 86 elderly Chinese patients with refractory partial epilepsy. Patients who had at least four seizures per 4 weeks during an 8-week baseline period, despite medication with up to three standard antiepileptic drugs (AEDs), were randomly assigned to receive topiramate (n = 46) or placebo (n = 40). Topiramate dosages were titrated (target dose 200 mg/day orally) for 8 weeks and maintained at stable levels for another 12 weeks; concomitant AEDs continued at original dosages. All patients completed the study: 47.8% in the topiramate group and 7.5% on placebo reached ≥ 50% reduction in complex partial seizures. In the topiramate group, the most common adverse events were dizziness, somnolence, fatigue, headache and difficulty with memory; most events were transient and mild or moderate in severity. It was concluded that 200 mg/day topiramate was effective and well-tolerated in elderly patients with refractory partial epilepsy.",
          "first_author": "Zhang",
          "pmid": "21672344",
          "pub_types": [
            "Journal Article",
            "Randomized Controlled Trial"
          ],
          "title": "Topiramate as an adjunctive treatment for refractory partial epilepsy in the elderly.",
          "year": "2011"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/21672344/",
      "generic_name": "topiramate",
      "id": "rct_pubmed_concordance_problem-0925c26b8df4",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 21672344 needs manual review for topiramate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 21672344 needs manual review for topiramate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "pubmed_phase_ii_iii_rct_links",
      "current_value": "Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/",
      "details": {
        "article": {
          "abstract": "Based on dose predictions from animal and human volunteer studies, most patients enrolled in initial randomized controlled trials of topiramate as adjunctive therapy in adults with partial-onset seizures were randomized to >or= 600 mg/day topiramate. Subsequent experience suggests that dosage needs were overestimated. This double-blind, placebo-controlled study evaluated 200 mg/day topiramate in adults with treatment-resistant partial-onset seizures receiving a concurrent enzyme-inducing antiepileptic agent (carbamazepine). After a 4-week baseline, 263 adults receiving carbamazepine who had at least three partial-onset seizures during the baseline period were randomized to placebo or one of two topiramate 200 mg/day treatment arms: topiramate escalated weekly 25 mg/day(8-week escalation) or 50 mg/day(4-week escalation). Therapy was then maintained for the remainder of the 12-week double-blind study. Median percent reduction in seizure frequency from baseline to study end was 44% with topiramate and 20% with placebo (P <or= 0.001). A significant therapeutic effect was present at 2 weeks with a dose of 100 mg/day. The most common adverse events (>or=10% incidence in topiramate-treated patients) were somnolence, fatigue, paresthesia, nervousness and anorexia; 8% of topiramate-treated patients and 2% of placebo-treated patients discontinued because of adverse events. As a result of the low incidence of adverse events, differences between titration rates in terms of tolerability were not detected. Topiramate 200 mg/day is an appropriate target dose as adjunctive therapy in adults with treatment-resistant partial-onset seizures, even when receiving an enzyme-inducing agent; 100 mg/day also appears to be effective. A significant therapeutic effect may be seen in the second week of treatment with a dose of 100 mg/day.",
          "first_author": "Guberman",
          "pmid": "12225311",
          "pub_types": [
            "Clinical Trial",
            "Comparative Study",
            "Journal Article",
            "Multicenter Study",
            "Randomized Controlled Trial",
            "Research Support, Non-U.S. Gov't"
          ],
          "title": "Low-dose topiramate in adults with treatment-resistant partial-onset seizures.",
          "year": "2002"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/12225311/",
      "generic_name": "topiramate",
      "id": "rct_pubmed_concordance_problem-10b1ff149415",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 12225311 needs manual review for topiramate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 12225311 needs manual review for topiramate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "year_fda_cleared",
      "current_value": "1996",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1996"
        ],
        "missing_terms": [],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5",
      "generic_name": "topiramate",
      "id": "source_fact_concordance_problem-6cf8c0860d39",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5); review current text before relying on it.",
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
        "brief_summary": "The purpose of this study is to evaluate the tolerability, safety and efficacy of topiramate in infants with refractory partial onset seizures (POS).",
        "interventions": [
          "topiramate",
          "topiramate",
          "topiramate",
          "placebo"
        ],
        "masking": "QUADRUPLE",
        "nct_id": "NCT00113815",
        "new_reference_pmids": [
          "22633629",
          "21673279"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "20089937",
          "22633629",
          "21673279"
        ],
        "title": "Topiramate as Adjunctive Therapy in Infants 1-24 Months for the Control of Partial Onset Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT00113815",
      "generic_name": "topiramate",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-a1a68b34864f",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Topiramate as Adjunctive Therapy in Infants 1-24 Months for the Control of Partial Onset Seizures"
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
      "generic_name": "topiramate",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-e2fa8dd69260",
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
        "brief_summary": "OBJECTIVES:\n\nI. Evaluate the safety and efficacy of oral topiramate in patients with Lennox-Gastaut syndrome.",
        "interventions": [
          "topiramate"
        ],
        "masking": "DOUBLE",
        "nct_id": "NCT00004776",
        "new_reference_pmids": [],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [],
        "title": "Phase III Randomized, Double-Blind, Placebo-Controlled Study of Oral Topiramate for Lennox-Gastaut Syndrome"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT00004776",
      "generic_name": "topiramate",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-1e54776c5774",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Phase III Randomized, Double-Blind, Placebo-Controlled Study of Oral Topiramate for Lennox-Gastaut Syndrome"
    },
    {
      "column": "",
      "current_value": "",
      "details": {
        "allocation": "RANDOMIZED",
        "brief_summary": "The purpose of this study is to examine the safety and effectiveness of USL255 as adjunctive therapy in patients with refractory partial onset-seizures.",
        "interventions": [
          "USL255",
          "Placebo"
        ],
        "masking": "DOUBLE",
        "nct_id": "NCT01142193",
        "new_reference_pmids": [
          "25461205",
          "24902983"
        ],
        "overall_status": "COMPLETED",
        "phases": [
          "PHASE3"
        ],
        "pmids": [
          "25461205",
          "24902983"
        ],
        "title": "Study to Evaluate the Safety and Effectiveness of USL255 in Patients With Refractory Partial-onset Seizures"
      },
      "evidence_url": "https://clinicaltrials.gov/study/NCT01142193",
      "generic_name": "topiramate",
      "id": "nih_clinicaltrial_phase_ii_iii_rct-b8de731a3d50",
      "kind": "nih_clinicaltrial_phase_ii_iii_rct",
      "proposed_updates": {},
      "proposed_value": "",
      "requires_approval": false,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "NIH ClinicalTrials.gov",
      "summary": "NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Evaluate the Safety and Effectiveness of USL255 in Patients With Refractory Partial-onset Seizures"
    },
    {
      "column": "trade_names",
      "current_value": "Eprontia; Qudexy XR; Topamax; Topamax Sprinkle; Trokendi XR",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100",
      "generic_name": "topiramate",
      "id": "trade_name_addition-c2f2f0a16dd3",
      "kind": "trade_name_addition",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA",
        "trade_names": "Topiramate"
      },
      "proposed_value": "Topiramate",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "Source labels mention trade name(s) not present in CSV: Topiramate."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=e2a4df59-fead-4a01-9021-9eda02c48010; published=Mar 23, 2026; title=EPRONTIA (TOPIRAMATE) SOLUTION [AZURITY PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e2a4df59-fead-4a01-9021-9eda02c48010",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5",
      "generic_name": "topiramate",
      "id": "fda_warning_metadata_refresh-b2e5f394b9ec",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "No FDA boxed warning identified in selected current FDA/openFDA label.",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=e2a4df59-fead-4a01-9021-9eda02c48010; effective_time=20251113; title=Eprontia / TOPIRAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=e2a4df59-fead-4a01-9021-9eda02c48010; effective_time=20251113; title=Eprontia / TOPIRAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [
    {
      "audit_note": "Abstract reports responder rates for the 200 mg/day elderly trial.",
      "dose_or_regimen": "topiramate 200 mg/day",
      "endpoint": "elderly refractory partial epilepsy",
      "generic_name": "topiramate",
      "label": "Zhang2011",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "21672344",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/21672344/",
      "rr50_active_percent": "47.8",
      "rr50_differential_percent": "40.3",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "7.5",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Topiramate as an adjunctive treatment for refractory partial epilepsy in the elderly."
    },
    {
      "audit_note": "Infant partial-onset seizure trial found no significant difference for 25 mg/kg/day versus placebo; not included as a maximum effective regimen.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "topiramate",
      "label": "Novotny2010",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "20089937",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/20089937/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Randomized trial of adjunctive topiramate therapy in infants with refractory partial seizures."
    },
    {
      "audit_note": "Abstract reports 200 mg/day median seizure-frequency reduction values; responder rate was not extractable.",
      "dose_or_regimen": "topiramate 200 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "topiramate",
      "label": "Guberman2002",
      "mpc_active_percent": "44.0",
      "mpc_differential_percent": "24.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "20.0",
      "pmid": "12225311",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/12225311/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Low-dose topiramate in adults with treatment-resistant partial-onset seizures."
    },
    {
      "audit_note": "Abstract reports responder rates for topiramate 300 mg/day and placebo.",
      "dose_or_regimen": "topiramate 300 mg/day",
      "endpoint": "adult refractory partial epilepsy",
      "generic_name": "topiramate",
      "label": "Yen2000",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "10999555",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/10999555/",
      "rr50_active_percent": "47.8",
      "rr50_differential_percent": "34.8",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "13.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "A double-blind, placebo-controlled study of topiramate in adult patients with refractory partial epilepsy."
    },
    {
      "audit_note": "Abstract reports target 600 mg/day responder, median seizure-frequency reduction, and seizure-free rates.",
      "dose_or_regimen": "topiramate 600 mg/day",
      "endpoint": "partial epilepsy",
      "generic_name": "topiramate",
      "label": "PMID1999",
      "mpc_active_percent": "51.3",
      "mpc_differential_percent": "42.2",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "9.1",
      "pmid": "10612342",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/10612342/",
      "rr50_active_percent": "50.6",
      "rr50_differential_percent": "37.7",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "12.9",
      "sf_active_percent": "7.9",
      "sf_differential_percent": "6.7",
      "sf_included_in_csv_summary": "yes",
      "sf_placebo_percent": "1.2",
      "title": "Topiramate in medically intractable partial epilepsies: double-blind placebo-controlled randomized parallel group trial. Korean Topiramate Study Group."
    },
    {
      "audit_note": "Abstract reports major-seizure responder rates and drop-attack median reduction values.",
      "dose_or_regimen": "topiramate approximately 6 mg/kg/day",
      "endpoint": "LGS drop attacks and major seizures",
      "generic_name": "topiramate",
      "label": "Sachdeo1999",
      "mpc_active_percent": "14.8",
      "mpc_differential_percent": "19.9",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "-5.1",
      "pmid": "10371538",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/10371538/",
      "rr50_active_percent": "33.0",
      "rr50_differential_percent": "25.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "8.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "A double-blind, randomized trial of topiramate in Lennox-Gastaut syndrome. Topiramate YL Study Group."
    },
    {
      "audit_note": "Abstract reports pediatric responder and median seizure-frequency reduction values.",
      "dose_or_regimen": "topiramate 6 mg/kg/day",
      "endpoint": "pediatric partial-onset seizures",
      "generic_name": "topiramate",
      "label": "Elterman1999",
      "mpc_active_percent": "33.1",
      "mpc_differential_percent": "22.6",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "10.5",
      "pmid": "10227615",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/10227615/",
      "rr50_active_percent": "39.0",
      "rr50_differential_percent": "19.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "20.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "A double-blind, randomized trial of topiramate as adjunctive therapy for partial-onset seizures in children. Topiramate YP Study Group."
    },
    {
      "audit_note": "Abstract reports target-dose PGTC responder and median reduction values.",
      "dose_or_regimen": "topiramate approximately 6 mg/kg/day",
      "endpoint": "primary generalized tonic-clonic seizures",
      "generic_name": "topiramate",
      "label": "Biton1999",
      "mpc_active_percent": "56.7",
      "mpc_differential_percent": "47.7",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "9.0",
      "pmid": "10227614",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/10227614/",
      "rr50_active_percent": "56.0",
      "rr50_differential_percent": "36.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "20.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "A randomized, placebo-controlled study of topiramate in primary generalized tonic-clonic seizures. Topiramate YTC Study Group."
    },
    {
      "audit_note": "Companion summary of topiramate U.S. dose-ranging trials; source study values are captured from the primary trial reports.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "topiramate",
      "label": "Faught1997",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "9092954",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/9092954/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy of topiramate as adjunctive therapy in refractory partial seizures: United States trial experience."
    },
    {
      "audit_note": "Abstract reports 400 mg/day responder and median reduction values.",
      "dose_or_regimen": "topiramate 400 mg/day",
      "endpoint": "partial seizures",
      "generic_name": "topiramate",
      "label": "Sharief1996",
      "mpc_active_percent": "41.0",
      "mpc_differential_percent": "40.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "1.0",
      "pmid": "8956919",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8956919/",
      "rr50_active_percent": "35.0",
      "rr50_differential_percent": "27.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "8.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Double-blind, placebo-controlled study of topiramate in patients with refractory partial epilepsy."
    },
    {
      "audit_note": "Abstract reports responder and median seizure-frequency reduction values for topiramate 600 mg/day.",
      "dose_or_regimen": "topiramate 600 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "topiramate",
      "label": "Tassinari1996",
      "mpc_active_percent": "46.0",
      "mpc_differential_percent": "58.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "-12.0",
      "pmid": "8764816",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8764816/",
      "rr50_active_percent": "47.0",
      "rr50_differential_percent": "37.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "10.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Double-blind, placebo-controlled trial of topiramate (600 mg daily) for the treatment of refractory partial epilepsy."
    },
    {
      "audit_note": "Abstract reports 400 mg/day responder and median reduction values. Higher 600 mg/day arm was not used because incremental efficacy above 400 mg/day is not the selected maximum effective dose.",
      "dose_or_regimen": "topiramate 400 mg/day",
      "endpoint": "partial-onset seizures",
      "generic_name": "topiramate",
      "label": "Faught1996",
      "mpc_active_percent": "48.0",
      "mpc_differential_percent": "35.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "13.0",
      "pmid": "8649570",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8649570/",
      "rr50_active_percent": "47.0",
      "rr50_differential_percent": "29.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "18.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Topiramate placebo-controlled dose-ranging trial in refractory partial epilepsy using 200-, 400-, and 600-mg daily dosages. Topiramate YD Study Group."
    },
    {
      "audit_note": "Abstract reports 600 mg/day responder and median seizure-frequency reduction values; higher doses did not add group-level efficacy.",
      "dose_or_regimen": "topiramate 600 mg/day",
      "endpoint": "refractory partial epilepsy",
      "generic_name": "topiramate",
      "label": "Privitera1996",
      "mpc_active_percent": "41.0",
      "mpc_differential_percent": "40.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "1.0",
      "pmid": "8649569",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8649569/",
      "rr50_active_percent": "44.0",
      "rr50_differential_percent": "35.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "9.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Topiramate placebo-controlled dose-ranging trial in refractory partial epilepsy using 600-, 800-, and 1,000-mg daily dosages. Topiramate YE Study Group."
    },
    {
      "audit_note": "Abstract reports placebo-adjusted median reduction and responder rates for the titrated 800 mg/day/max-tolerated regimen.",
      "dose_or_regimen": "topiramate up to 800 mg/day",
      "endpoint": "refractory partial epilepsy",
      "generic_name": "topiramate",
      "label": "BenMenachem1996",
      "mpc_active_percent": "",
      "mpc_differential_percent": "54.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "",
      "pmid": "8641230",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8641230/",
      "rr50_active_percent": "43.0",
      "rr50_differential_percent": "43.0",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "0.0",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Double-blind, placebo-controlled trial of topiramate as add-on therapy in patients with refractory partial seizures."
    }
  ],
  "local_rct_audit_rows": [
    {
      "first_author": "Zhang",
      "generic_name": "topiramate",
      "label": "Zhang2011",
      "pmid": "21672344",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Topiramate as an adjunctive treatment for refractory partial epilepsy in the elderly.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/21672344/",
      "year": "2011"
    },
    {
      "first_author": "Novotny",
      "generic_name": "topiramate",
      "label": "Novotny2010",
      "pmid": "20089937",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Randomized trial of adjunctive topiramate therapy in infants with refractory partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/20089937/",
      "year": "2010"
    },
    {
      "first_author": "Guberman",
      "generic_name": "topiramate",
      "label": "Guberman2002",
      "pmid": "12225311",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Low-dose topiramate in adults with treatment-resistant partial-onset seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/12225311/",
      "year": "2002"
    },
    {
      "first_author": "Yen",
      "generic_name": "topiramate",
      "label": "Yen2000",
      "pmid": "10999555",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "A double-blind, placebo-controlled study of topiramate in adult patients with refractory partial epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10999555/",
      "year": "2000"
    },
    {
      "first_author": "PMID",
      "generic_name": "topiramate",
      "label": "PMID1999",
      "pmid": "10612342",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Topiramate in medically intractable partial epilepsies: double-blind placebo-controlled randomized parallel group trial. Korean Topiramate Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10612342/",
      "year": "1999"
    },
    {
      "first_author": "Sachdeo",
      "generic_name": "topiramate",
      "label": "Sachdeo1999",
      "pmid": "10371538",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't; Research Support, U.S. Gov't, P.H.S.",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "A double-blind, randomized trial of topiramate in Lennox-Gastaut syndrome. Topiramate YL Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10371538/",
      "year": "1999"
    },
    {
      "first_author": "Elterman",
      "generic_name": "topiramate",
      "label": "Elterman1999",
      "pmid": "10227615",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "A double-blind, randomized trial of topiramate as adjunctive therapy for partial-onset seizures in children. Topiramate YP Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10227615/",
      "year": "1999"
    },
    {
      "first_author": "Biton",
      "generic_name": "topiramate",
      "label": "Biton1999",
      "pmid": "10227614",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "A randomized, placebo-controlled study of topiramate in primary generalized tonic-clonic seizures. Topiramate YTC Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10227614/",
      "year": "1999"
    },
    {
      "first_author": "Faught",
      "generic_name": "topiramate",
      "label": "Faught1997",
      "pmid": "9092954",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy of topiramate as adjunctive therapy in refractory partial seizures: United States trial experience.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9092954/",
      "year": "1997"
    },
    {
      "first_author": "Sharief",
      "generic_name": "topiramate",
      "label": "Sharief1996",
      "pmid": "8956919",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Double-blind, placebo-controlled study of topiramate in patients with refractory partial epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8956919/",
      "year": "1996"
    },
    {
      "first_author": "Tassinari",
      "generic_name": "topiramate",
      "label": "Tassinari1996",
      "pmid": "8764816",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Double-blind, placebo-controlled trial of topiramate (600 mg daily) for the treatment of refractory partial epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8764816/",
      "year": "1996"
    },
    {
      "first_author": "Faught",
      "generic_name": "topiramate",
      "label": "Faught1996",
      "pmid": "8649570",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Topiramate placebo-controlled dose-ranging trial in refractory partial epilepsy using 200-, 400-, and 600-mg daily dosages. Topiramate YD Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8649570/",
      "year": "1996"
    },
    {
      "first_author": "Privitera",
      "generic_name": "topiramate",
      "label": "Privitera1996",
      "pmid": "8649569",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Topiramate placebo-controlled dose-ranging trial in refractory partial epilepsy using 600-, 800-, and 1,000-mg daily dosages. Topiramate YE Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8649569/",
      "year": "1996"
    },
    {
      "first_author": "Ben-Menachem",
      "generic_name": "topiramate",
      "label": "BenMenachem1996",
      "pmid": "8641230",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Double-blind, placebo-controlled trial of topiramate as add-on therapy in patients with refractory partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8641230/",
      "year": "1996"
    },
    {
      "first_author": "Kerr",
      "generic_name": "topiramate",
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
      "generic_name": "topiramate",
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
      "first_author": "VanLandingham",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "32652616",
      "pub_types": "Clinical Trial, Phase II; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "A Phase 2, Double-Blind, Placebo-Controlled Trial to Investigate Potential Drug-Drug Interactions Between Cannabidiol and Clobazam.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/32652616/",
      "year": "2020"
    },
    {
      "first_author": "Moseley",
      "generic_name": "topiramate",
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
      "first_author": "Perry",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "30955420",
      "pub_types": "Journal Article; Comment",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Don't Fear the Reefer-Evidence Mounts for Plant-Based Cannabidiol as Treatment for Epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/30955420/",
      "year": "2019"
    },
    {
      "first_author": "Nuñez-Ramiro",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "31091527",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Topiramate plus Cooling for Hypoxic-Ischemic Encephalopathy: A Randomized, Controlled, Multicenter, Double-Blinded Trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/31091527/",
      "year": "2019"
    },
    {
      "first_author": "Devinsky",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "29540584",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Randomized, dose-ranging safety trial of cannabidiol in Dravet syndrome.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/29540584/",
      "year": "2018"
    },
    {
      "first_author": "Benbadis",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "29414542",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Efficacy, safety, and tolerability of brivaracetam with concomitant lamotrigine or concomitant topiramate in pooled Phase III randomized, double-blind trials: A post-hoc analysis.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/29414542/",
      "year": "2018"
    },
    {
      "first_author": "Chung",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "27084978",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Long-term safety and sustained efficacy of USL255 (topiramate extended-release capsules) in patients with refractory partial-onset seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/27084978/",
      "year": "2016"
    },
    {
      "first_author": "Meador",
      "generic_name": "topiramate",
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
      "first_author": "Kälviäinen",
      "generic_name": "topiramate",
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
      "first_author": "Hogan",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "25461205",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Efficacy of once-daily extended-release topiramate (USL255): a subgroup analysis based on the level of treatment resistance.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/25461205/",
      "year": "2014"
    },
    {
      "first_author": "Chung",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "24902983",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Once-daily USL255 as adjunctive treatment of partial-onset seizures: randomized phase III study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/24902983/",
      "year": "2014"
    },
    {
      "first_author": "Bitton",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "22889307",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "A randomized controlled trial of flunarizine as add-on therapy and effect on cognitive outcome in children with infantile spasms.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/22889307/",
      "year": "2012"
    },
    {
      "first_author": "Loring",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "21148119",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, N.I.H., Extramural; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Topiramate dose effects on cognition: a randomized double-blind study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/21148119/",
      "year": "2010"
    },
    {
      "first_author": "Cady",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "19222595",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Evaluation of carisbamate for the treatment of migraine in a randomized, double-blind trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/19222595/",
      "year": "2009"
    },
    {
      "first_author": "Otoul",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "17651416",
      "pub_types": "Comparative Study; Journal Article; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Lack of pharmacokinetic interaction of levetiracetam on carbamazepine, valproic acid, topiramate, and lamotrigine in children with epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17651416/",
      "year": "2007"
    },
    {
      "first_author": "Wroe",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "17594758",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Zonisamide and renal calculi in patients with epilepsy: how big an issue?",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17594758/",
      "year": "2007"
    },
    {
      "first_author": "Gazzola",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "17521343",
      "pub_types": "Comparative Study; Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Seizure-free outcome in randomized add-on trials of the new antiepileptic drugs.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17521343/",
      "year": "2007"
    },
    {
      "first_author": "PMID",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "17582922",
      "pub_types": "Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Zonisamide: new drug. No advantage in refractory partial epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17582922/",
      "year": "2007"
    },
    {
      "first_author": "Biton",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "16286543",
      "pub_types": "Comparative Study; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Topiramate in patients with juvenile myoclonic epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/16286543/",
      "year": "2005"
    },
    {
      "first_author": "Kerr",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "16140593",
      "pub_types": "Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "A randomized, double-blind, placebo-controlled trial of topiramate in adults with epilepsy and intellectual disability: impact on seizures, severity, and quality of life.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/16140593/",
      "year": "2005"
    },
    {
      "first_author": "Fröscher",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "16162434",
      "pub_types": "Clinical Trial; Journal Article",
      "reason": "no randomized language",
      "status": "rejected",
      "title": "Topiramate: a prospective study on the relationship between concentration, dosage and adverse events in epileptic patients on combination therapy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/16162434/",
      "year": "2005"
    },
    {
      "first_author": "Majkowski",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "15857429",
      "pub_types": "Comparative Study; Journal Article",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Time course of adverse events in patients with localization-related epilepsy receiving topiramate added to carbamazepine.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/15857429/",
      "year": "2005"
    },
    {
      "first_author": "Hardan",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "15650499",
      "pub_types": "Journal Article; Research Support, U.S. Gov't, P.H.S.",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "A retrospective assessment of topiramate in children and adolescents with pervasive developmental disorders.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/15650499/",
      "year": "2004"
    },
    {
      "first_author": "Meador",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "12743236",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Differential cognitive and behavioral effects of topiramate and valproate.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/12743236/",
      "year": "2003"
    },
    {
      "first_author": "Maltoni",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "17535035",
      "pub_types": "Journal Article",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Lifetime cost-utility analysis of patients with refractory epilepsy treated with adjunctive topiramate therapy : cost-effectiveness in refractory epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/17535035/",
      "year": "2003"
    },
    {
      "first_author": "PMID",
      "generic_name": "topiramate",
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
      "first_author": "Storey",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "11903524",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Topiramate in migraine prevention: a double-blind, placebo-controlled study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/11903524/",
      "year": "2001"
    },
    {
      "first_author": "Glauser",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "10768308",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Topiramate in Lennox-Gastaut syndrome: open-label treatment of patients completing a randomized controlled trial. Topiramate YL Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10768308/",
      "year": "2000"
    },
    {
      "first_author": "Ritter",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "10768307",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Effectiveness, tolerability, and safety of topiramate in children with partial-onset seizures. Topiramate YP Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10768307/",
      "year": "2000"
    },
    {
      "first_author": "Montouris",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "10768306",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Nonfocal generalized tonic-clonic seizures: response during long-term topiramate treatment. Topiramate YTC/YTCE Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10768306/",
      "year": "2000"
    },
    {
      "first_author": "PMID",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "11503838",
      "pub_types": "Comparative Study; Journal Article",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Topiramate: new indication. A bulkier assessment file.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/11503838/",
      "year": "1999"
    },
    {
      "first_author": "Biton",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "9092959",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Preliminary open-label experience with topiramate in primary generalized seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9092959/",
      "year": "1997"
    },
    {
      "first_author": "Glauser",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "9092958",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article; Multicenter Study",
      "reason": "no randomized language",
      "status": "rejected",
      "title": "Preliminary observations on topiramate in pediatric epilepsies.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9092958/",
      "year": "1997"
    },
    {
      "first_author": "Reife",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "9092956",
      "pub_types": "Clinical Trial; Journal Article",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Topiramate as adjunctive therapy in refractory partial epilepsy: pooled analysis of data from five double-blind, placebo-controlled trials.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9092956/",
      "year": "1997"
    },
    {
      "first_author": "Ben-Menachem",
      "generic_name": "topiramate",
      "label": "",
      "pmid": "9092955",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Clinical efficacy of topiramate as add-on therapy in refractory partial epilepsy: the European experience.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9092955/",
      "year": "1997"
    }
  ],
  "possible_duplicate_name_hits": []
}
