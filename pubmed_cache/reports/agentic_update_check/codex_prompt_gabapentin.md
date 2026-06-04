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
    "adverse_symptoms_percentages": "CNS: somnolence 19%, CNS: dizziness 17%, neurologic: ataxia 13%, constitutional: fatigue 11%, neurologic: nystagmus 8%, infectious: viral infection 11%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "15.2-17.9 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Anhut1994 gabapentin 1200 mg/day 17.9%; PMID1990 gabapentin 1200 mg/day 15.2%)",
    "diff_median_pct_change_maximum_effective_dose": "10.5-16.7 % (drug minus placebo MPC differential at maximum effective dose/regimen: Appleton1999 gabapentin 23-35 mg/kg/day 10.5%; PMID1990 gabapentin 1200 mg/day 16.7%)",
    "diff_seizure_freedom_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "enzyme_inducing_or_inhibiting": "Not metabolized; not an enzyme inducer/inhibitor",
    "epilepsy_type": "Focal",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd; published=May 07, 2025; title=HORIZANT (GABAPENTIN ENACARBIL) TABLET, EXTENDED RELEASE [AZURITY PHARMACEUTICALS, INC. (FORMERLY ARBOR PHARMACEUTICALS)]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "Inducer; No major enzyme effect",
    "filter_epilepsy_type": "Focal",
    "filter_formulation": "Capsule; Liquid; Tablet",
    "filter_mechanism": "Calcium channel / alpha-2-delta",
    "filter_metabolism": "Renal/no major metabolism",
    "filter_qt_effect": "No known meaningful QT effect",
    "filter_symptom_category": "CNS; Constitutional; Infectious; Neurologic",
    "formulations_available": "Capsule; tablet; oral solution",
    "generic_name": "gabapentin",
    "half_life_range": "5-7 h",
    "major_organ_for_metabolism": "Not metabolized; renal excretion",
    "maximum_approved_daily_dose": "1800 mg/day labeled for epilepsy; higher doses used in practice",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Precise antiepileptic mechanism is unknown; gabapentin binds the alpha-2-delta subunit of voltage-activated calcium channels, but the relationship of this binding to efficacy is not fully established.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "900 mg/day",
    "plot_diff_50_responder_maximum_effective_dose": "Anhut1994|17.9|https://pubmed.ncbi.nlm.nih.gov/8082624/|272; PMID1990|15.2|https://pubmed.ncbi.nlm.nih.gov/1971862/|127",
    "plot_diff_median_pct_change_maximum_effective_dose": "Appleton1999|10.5|https://pubmed.ncbi.nlm.nih.gov/10448830/|247; PMID1990|16.7|https://pubmed.ncbi.nlm.nih.gov/1971862/|127",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "Yamauchi2006|https://pubmed.ncbi.nlm.nih.gov/16884455/; Zhu2005|https://pubmed.ncbi.nlm.nih.gov/15774213/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10448830/; Leach1997|https://pubmed.ncbi.nlm.nih.gov/9120451/; Trudeau1996|https://pubmed.ncbi.nlm.nih.gov/9120226/; Dimond1996|https://pubmed.ncbi.nlm.nih.gov/8771597/; BenMenachem1995|https://pubmed.ncbi.nlm.nih.gov/8536677/; Anhut1994|https://pubmed.ncbi.nlm.nih.gov/8082624/; PMID1993|https://pubmed.ncbi.nlm.nih.gov/8232945/; Sivenius1991|https://pubmed.ncbi.nlm.nih.gov/1907907/; PMID1990|https://pubmed.ncbi.nlm.nih.gov/1971862/",
    "pubmed_search_aliases": "",
    "qt_interval_effect": "No clinically meaningful QT effect established",
    "rct_pubmed_verification_notes": "PubMed loop 24/65 on 2026-05-15: 11 qualifying placebo-controlled randomized clinical trial report(s) retained from 30 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.",
    "status_or_notes": "Current ASM for focal/partial seizures; also used for postherpetic neuralgia, neuropathic pain, restless legs syndrome, and other off-label uses.",
    "trade_names": "Gralise; Horizant; Neurontin",
    "typical_doses_per_day": "Adjunctive focal seizures: 900-1800 mg/day divided TID; up to 3600 mg/day used",
    "year_fda_cleared": "1993"
  },
  "existing_pubmed_links": [
    {
      "entry": "Yamauchi2006|https://pubmed.ncbi.nlm.nih.gov/16884455/",
      "label": "Yamauchi2006",
      "pmid": "16884455",
      "url": "https://pubmed.ncbi.nlm.nih.gov/16884455/"
    },
    {
      "entry": "Zhu2005|https://pubmed.ncbi.nlm.nih.gov/15774213/",
      "label": "Zhu2005",
      "pmid": "15774213",
      "url": "https://pubmed.ncbi.nlm.nih.gov/15774213/"
    },
    {
      "entry": "Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10448830/",
      "label": "Appleton1999",
      "pmid": "10448830",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10448830/"
    },
    {
      "entry": "Leach1997|https://pubmed.ncbi.nlm.nih.gov/9120451/",
      "label": "Leach1997",
      "pmid": "9120451",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9120451/"
    },
    {
      "entry": "Trudeau1996|https://pubmed.ncbi.nlm.nih.gov/9120226/",
      "label": "Trudeau1996",
      "pmid": "9120226",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9120226/"
    },
    {
      "entry": "Dimond1996|https://pubmed.ncbi.nlm.nih.gov/8771597/",
      "label": "Dimond1996",
      "pmid": "8771597",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8771597/"
    },
    {
      "entry": "BenMenachem1995|https://pubmed.ncbi.nlm.nih.gov/8536677/",
      "label": "BenMenachem1995",
      "pmid": "8536677",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8536677/"
    },
    {
      "entry": "Anhut1994|https://pubmed.ncbi.nlm.nih.gov/8082624/",
      "label": "Anhut1994",
      "pmid": "8082624",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8082624/"
    },
    {
      "entry": "PMID1993|https://pubmed.ncbi.nlm.nih.gov/8232945/",
      "label": "PMID1993",
      "pmid": "8232945",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8232945/"
    },
    {
      "entry": "Sivenius1991|https://pubmed.ncbi.nlm.nih.gov/1907907/",
      "label": "Sivenius1991",
      "pmid": "1907907",
      "url": "https://pubmed.ncbi.nlm.nih.gov/1907907/"
    },
    {
      "entry": "PMID1990|https://pubmed.ncbi.nlm.nih.gov/1971862/",
      "label": "PMID1990",
      "pmid": "1971862",
      "url": "https://pubmed.ncbi.nlm.nih.gov/1971862/"
    }
  ],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "CNS: somnolence 19%, CNS: dizziness 17%, neurologic: ataxia 13%, constitutional: fatigue 11%, neurologic: nystagmus 8%, infectious: viral infection 11%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "15.2-17.9 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Anhut1994 gabapentin 1200 mg/day 17.9%; PMID1990 gabapentin 1200 mg/day 15.2%)",
    "diff_median_pct_change_maximum_effective_dose": "10.5-16.7 % (drug minus placebo MPC differential at maximum effective dose/regimen: Appleton1999 gabapentin 23-35 mg/kg/day 10.5%; PMID1990 gabapentin 1200 mg/day 16.7%)",
    "diff_seizure_freedom_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "enzyme_inducing_or_inhibiting": "Not metabolized; not an enzyme inducer/inhibitor",
    "epilepsy_type": "Focal",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling",
    "fda_black_box_warning": "No FDA boxed warning identified in selected current DailyMed label.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd; published=May 07, 2025; title=HORIZANT (GABAPENTIN ENACARBIL) TABLET, EXTENDED RELEASE [AZURITY PHARMACEUTICALS, INC. (FORMERLY ARBOR PHARMACEUTICALS)]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd",
    "formulations_available": "Capsule; tablet; oral solution",
    "half_life_range": "5-7 h",
    "major_organ_for_metabolism": "Not metabolized; renal excretion",
    "maximum_approved_daily_dose": "1800 mg/day labeled for epilepsy; higher doses used in practice",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Precise antiepileptic mechanism is unknown; gabapentin binds the alpha-2-delta subunit of voltage-activated calcium channels, but the relationship of this binding to efficacy is not fully established.",
    "mechanism_source": "FDA/DailyMed labeling",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "900 mg/day",
    "plot_diff_50_responder_maximum_effective_dose": "Anhut1994|17.9|https://pubmed.ncbi.nlm.nih.gov/8082624/|272; PMID1990|15.2|https://pubmed.ncbi.nlm.nih.gov/1971862/|127",
    "plot_diff_median_pct_change_maximum_effective_dose": "Appleton1999|10.5|https://pubmed.ncbi.nlm.nih.gov/10448830/|247; PMID1990|16.7|https://pubmed.ncbi.nlm.nih.gov/1971862/|127",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "Yamauchi2006|https://pubmed.ncbi.nlm.nih.gov/16884455/; Zhu2005|https://pubmed.ncbi.nlm.nih.gov/15774213/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10448830/; Leach1997|https://pubmed.ncbi.nlm.nih.gov/9120451/; Trudeau1996|https://pubmed.ncbi.nlm.nih.gov/9120226/; Dimond1996|https://pubmed.ncbi.nlm.nih.gov/8771597/; BenMenachem1995|https://pubmed.ncbi.nlm.nih.gov/8536677/; Anhut1994|https://pubmed.ncbi.nlm.nih.gov/8082624/; PMID1993|https://pubmed.ncbi.nlm.nih.gov/8232945/; Sivenius1991|https://pubmed.ncbi.nlm.nih.gov/1907907/; PMID1990|https://pubmed.ncbi.nlm.nih.gov/1971862/",
    "pubmed_search_aliases": "",
    "qt_interval_effect": "No clinically meaningful QT effect established",
    "trade_names": "Gralise; Horizant; Neurontin",
    "typical_doses_per_day": "Adjunctive focal seizures: 900-1800 mg/day divided TID; up to 3600 mg/day used",
    "year_fda_cleared": "1993"
  },
  "generic_name": "gabapentin",
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
      "current_value": "PMID1990|https://pubmed.ncbi.nlm.nih.gov/1971862/",
      "details": {
        "article": {
          "abstract": "Gabapentin is an analogue of gamma aminobutyric acid (GABA) which has anticonvulsant properties in animals. In a multicentre, double-blind, placebo-controlled, parallel-group study of 1200 mg/day gabapentin as additional therapy in 127 patients with drug-resistant partial epilepsy, 25% of patients who received gabapentin had the number of partial seizures at least halved, compared with 9.8% of patients given placebo. The median reduction in partial seizure frequency during 12 weeks' treatment was 29.2% with gabapentin compared with 12.5% with placebo. The mean adjusted response ratio for gabapentin (-0.192) was significantly better than the ratio of -0.060 for placebo by analysis of variance. 62% of patients who received gabapentin reported mostly mild or moderate adverse effects compared with 41% on placebo; no interactions were observed between gabapentin and other standard anticonvulsants. Gabapentin is an effective additional treatment for patients with partial epilepsy refractory to standard therapy, is fairly well tolerated, and appears to have a favourable efficacy-to-toxicity ratio.",
          "first_author": "PMID",
          "pmid": "1971862",
          "pub_types": [
            "Clinical Trial",
            "Journal Article",
            "Multicenter Study",
            "Randomized Controlled Trial"
          ],
          "title": "Gabapentin in partial epilepsy. UK Gabapentin Study Group.",
          "year": "1990"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/1971862/",
      "generic_name": "gabapentin",
      "id": "rct_pubmed_concordance_problem-ebf7f5a01d35",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 1971862 needs manual review for gabapentin; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 1971862 needs manual review for gabapentin; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "typical_doses_per_day",
      "current_value": "Adjunctive focal seizures: 900-1800 mg/day divided TID; up to 3600 mg/day used",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1800",
          "3600"
        ],
        "missing_terms": [
          "adjunctive",
          "focal",
          "divided"
        ],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10",
      "generic_name": "gabapentin",
      "id": "source_fact_concordance_problem-d6e04d0107ac",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "typical_doses_per_day could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "maximum_approved_daily_dose",
      "current_value": "1800 mg/day labeled for epilepsy; higher doses used in practice",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1800"
        ],
        "missing_terms": [],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10",
      "generic_name": "gabapentin",
      "id": "source_fact_concordance_problem-3b0f7959c8fc",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "maximum_approved_daily_dose could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "year_fda_cleared",
      "current_value": "1993",
      "details": {
        "checked": true,
        "missing_numbers": [
          "1993"
        ],
        "missing_terms": [],
        "ok": false
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10",
      "generic_name": "gabapentin",
      "id": "source_fact_concordance_problem-aa8792eb2f8d",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "year_fda_cleared could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "epilepsy_type",
      "current_value": "Focal",
      "details": {
        "checked": true,
        "matched_terms": [],
        "missing_numbers": [],
        "missing_terms": [
          "focal"
        ],
        "numbers": [],
        "ok": false,
        "terms": [
          "focal"
        ]
      },
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10",
      "generic_name": "gabapentin",
      "id": "source_fact_concordance_problem-55d3d60b08fc",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "epilepsy_type could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "trade_names",
      "current_value": "Gralise; Horizant; Neurontin",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100",
      "generic_name": "gabapentin",
      "id": "trade_name_addition-66aae1378305",
      "kind": "trade_name_addition",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA",
        "trade_names": "Gabapentin"
      },
      "proposed_value": "Gabapentin",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "Source labels mention trade name(s) not present in CSV: Gabapentin."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd; published=May 07, 2025; title=HORIZANT (GABAPENTIN ENACARBIL) TABLET, EXTENDED RELEASE [AZURITY PHARMACEUTICALS, INC. (FORMERLY ARBOR PHARMACEUTICALS)]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10",
      "generic_name": "gabapentin",
      "id": "fda_warning_metadata_refresh-e0359b1abc81",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "No FDA boxed warning identified in selected current FDA/openFDA label.",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=466273b1-c9fc-3930-c94b-aa11394d5140; effective_time=20250501; title=Gralise / GABAPENTIN; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=466273b1-c9fc-3930-c94b-aa11394d5140; effective_time=20250501; title=Gralise / GABAPENTIN; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [
    {
      "audit_note": "Abstract reports response-ratio significance for 1200 and 1800 mg/day but not arm-specific RR50/MPC/seizure-freedom percentages.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "gabapentin",
      "label": "Yamauchi2006",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "16884455",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/16884455/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Treatment of partial seizures with gabapentin: double-blind, placebo-controlled, parallel-group study."
    },
    {
      "audit_note": "Abstract reports significant efficacy-rate differences but not extractable active/placebo percentages.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "gabapentin",
      "label": "Zhu2005",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "15774213",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/15774213/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "[Curative effect of gabapentin on refractory epilepsy]."
    },
    {
      "audit_note": "Abstract reports median percentage reduction for all partial seizures. Responder rate favored gabapentin but arm percentages were not reported.",
      "dose_or_regimen": "gabapentin 23-35 mg/kg/day",
      "endpoint": "pediatric refractory partial seizures",
      "generic_name": "gabapentin",
      "label": "Appleton1999",
      "mpc_active_percent": "17.0",
      "mpc_differential_percent": "10.5",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "6.5",
      "pmid": "10448830",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/10448830/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Gabapentin as add-on therapy in children with refractory partial seizures: a 12-week, multicentre, double-blind, placebo-controlled study. Gabapentin Paediatric Study Group."
    },
    {
      "audit_note": "Cognition-focused dose-ranging study; seizure-frequency RR50/MPC/seizure-freedom outcomes are not extractable from the abstract.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "gabapentin",
      "label": "Leach1997",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "9120451",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/9120451/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Gabapentin and cognition: a double blind, dose ranging, placebo controlled study in refractory epilepsy."
    },
    {
      "audit_note": "Absence-epilepsy monotherapy trials did not significantly change seizure frequency versus placebo and do not provide extractable active/placebo percentages.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "gabapentin",
      "label": "Trudeau1996",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "9120226",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/9120226/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Gabapentin in naive childhood absence epilepsy: results from two double-blind, placebo-controlled, multicenter studies."
    },
    {
      "audit_note": "Mood/well-being analysis of gabapentin trials, not a primary seizure-frequency efficacy report.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "gabapentin",
      "label": "Dimond1996",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "8771597",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8771597/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Effect of gabapentin (Neurontin) [corrected] on mood and well-being in patients with epilepsy."
    },
    {
      "audit_note": "CSF/seizure-frequency study abstract does not report extractable active/placebo RR50, MPC, or seizure-freedom percentages.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "gabapentin",
      "label": "BenMenachem1995",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "8536677",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8536677/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Seizure frequency and CSF parameters in a double-blind placebo controlled trial of gabapentin in patients with intractable complex partial seizures."
    },
    {
      "audit_note": "Abstract reports 1200 mg/day responder rate and placebo responder rate; 1200 mg/day median reduction was described as greater than 900 mg/day but not numerically reported.",
      "dose_or_regimen": "gabapentin 1200 mg/day",
      "endpoint": "partial seizures",
      "generic_name": "gabapentin",
      "label": "Anhut1994",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "8082624",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8082624/",
      "rr50_active_percent": "28.0",
      "rr50_differential_percent": "17.9",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "10.1",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Gabapentin (Neurontin) as add-on therapy in patients with partial seizures: a double-blind, placebo-controlled study. The International Gabapentin Study Group."
    },
    {
      "audit_note": "Abstract reports a responder-rate range across gabapentin dose groups, but does not identify the maximum-dose arm-specific responder percentage.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "gabapentin",
      "label": "PMID1993",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "8232945",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8232945/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Gabapentin as add-on therapy in refractory partial epilepsy: a double-blind, placebo-controlled, parallel-group study. The US Gabapentin Study Group No. 5."
    },
    {
      "audit_note": "Abstract reports seizure-frequency decrease for gabapentin 1200 mg/day but not an extractable placebo arm percentage for a drug-minus-placebo differential.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "gabapentin",
      "label": "Sivenius1991",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "1907907",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/1907907/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Double-blind study of Gabapentin in the treatment of partial seizures."
    },
    {
      "audit_note": "Abstract reports 1200 mg/day responder and median partial-seizure reduction values.",
      "dose_or_regimen": "gabapentin 1200 mg/day",
      "endpoint": "partial seizures",
      "generic_name": "gabapentin",
      "label": "PMID1990",
      "mpc_active_percent": "29.2",
      "mpc_differential_percent": "16.7",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "12.5",
      "pmid": "1971862",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/1971862/",
      "rr50_active_percent": "25.0",
      "rr50_differential_percent": "15.2",
      "rr50_included_in_csv_summary": "yes",
      "rr50_placebo_percent": "9.8",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Gabapentin in partial epilepsy. UK Gabapentin Study Group."
    }
  ],
  "local_rct_audit_rows": [
    {
      "first_author": "Yamauchi",
      "generic_name": "gabapentin",
      "label": "Yamauchi2006",
      "pmid": "16884455",
      "pub_types": "Clinical Trial, Phase III; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Treatment of partial seizures with gabapentin: double-blind, placebo-controlled, parallel-group study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/16884455/",
      "year": "2006"
    },
    {
      "first_author": "Zhu",
      "generic_name": "gabapentin",
      "label": "Zhu2005",
      "pmid": "15774213",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "[Curative effect of gabapentin on refractory epilepsy].",
      "url": "https://pubmed.ncbi.nlm.nih.gov/15774213/",
      "year": "2005"
    },
    {
      "first_author": "Appleton",
      "generic_name": "gabapentin",
      "label": "Appleton1999",
      "pmid": "10448830",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Gabapentin as add-on therapy in children with refractory partial seizures: a 12-week, multicentre, double-blind, placebo-controlled study. Gabapentin Paediatric Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10448830/",
      "year": "1999"
    },
    {
      "first_author": "Leach",
      "generic_name": "gabapentin",
      "label": "Leach1997",
      "pmid": "9120451",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Gabapentin and cognition: a double blind, dose ranging, placebo controlled study in refractory epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9120451/",
      "year": "1997"
    },
    {
      "first_author": "Trudeau",
      "generic_name": "gabapentin",
      "label": "Trudeau1996",
      "pmid": "9120226",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Gabapentin in naive childhood absence epilepsy: results from two double-blind, placebo-controlled, multicenter studies.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/9120226/",
      "year": "1996"
    },
    {
      "first_author": "Dimond",
      "generic_name": "gabapentin",
      "label": "Dimond1996",
      "pmid": "8771597",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Effect of gabapentin (Neurontin) [corrected] on mood and well-being in patients with epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8771597/",
      "year": "1996"
    },
    {
      "first_author": "Ben-Menachem",
      "generic_name": "gabapentin",
      "label": "BenMenachem1995",
      "pmid": "8536677",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Seizure frequency and CSF parameters in a double-blind placebo controlled trial of gabapentin in patients with intractable complex partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8536677/",
      "year": "1995"
    },
    {
      "first_author": "Anhut",
      "generic_name": "gabapentin",
      "label": "Anhut1994",
      "pmid": "8082624",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Gabapentin (Neurontin) as add-on therapy in patients with partial seizures: a double-blind, placebo-controlled study. The International Gabapentin Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8082624/",
      "year": "1994"
    },
    {
      "first_author": "PMID",
      "generic_name": "gabapentin",
      "label": "PMID1993",
      "pmid": "8232945",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Gabapentin as add-on therapy in refractory partial epilepsy: a double-blind, placebo-controlled, parallel-group study. The US Gabapentin Study Group No. 5.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8232945/",
      "year": "1993"
    },
    {
      "first_author": "Sivenius",
      "generic_name": "gabapentin",
      "label": "Sivenius1991",
      "pmid": "1907907",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Double-blind study of Gabapentin in the treatment of partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/1907907/",
      "year": "1991"
    },
    {
      "first_author": "PMID",
      "generic_name": "gabapentin",
      "label": "PMID1990",
      "pmid": "1971862",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Gabapentin in partial epilepsy. UK Gabapentin Study Group.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/1971862/",
      "year": "1990"
    },
    {
      "first_author": "Baos",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "41660750",
      "pub_types": "Journal Article; Randomized Controlled Trial; Multicenter Study",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Gabapentin as an adjunct to multimodal pain regimens in surgical patients: the GAP placebo-controlled RCT and economic evaluation.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/41660750/",
      "year": "2026"
    },
    {
      "first_author": "Baos",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "40663783",
      "pub_types": "Clinical Trial, Phase IV; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Gabapentin for Pain Management after Major Surgery: A Placebo-controlled, Double-blinded, Randomized Clinical Trial (the GAP Study).",
      "url": "https://pubmed.ncbi.nlm.nih.gov/40663783/",
      "year": "2025"
    },
    {
      "first_author": "Singh",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "36741623",
      "pub_types": "Journal Article",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Preemptive Levetiracetam Decreases Postoperative Pain: A Double-Blind, Randomised, Control Trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/36741623/",
      "year": "2023"
    },
    {
      "first_author": "Wilson",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "36419530",
      "pub_types": "Journal Article",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Feasibility of gabapentin as an intervention for neurorecovery after an acute spinal cord injury: Protocol.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/36419530/",
      "year": "2022"
    },
    {
      "first_author": "Baos",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "33444208",
      "pub_types": "Clinical Trial Protocol; Journal Article; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Effectiveness, cost-effectiveness and safety of gabapentin versus placebo as an adjunct to multimodal pain regimens in surgical patients: protocol of a placebo controlled randomised controlled trial with blinding (GAP study).",
      "url": "https://pubmed.ncbi.nlm.nih.gov/33444208/",
      "year": "2020"
    },
    {
      "first_author": "Trbolova",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "28927402",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Effects of premedication with oral gabapentin on intraocular pressure changes following tracheal intubation in clinically normal dogs.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/28927402/",
      "year": "2017"
    },
    {
      "first_author": "Ahuja",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "23089176",
      "pub_types": "Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "A four arm, double blind, randomized and placebo controlled study of pregabalin in the management of post-burn pruritus.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/23089176/",
      "year": "2012"
    },
    {
      "first_author": "Clarke",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "20353411",
      "pub_types": "Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Gabapentin does not reduce preoperative anxiety when given prior to total hip arthroplasty.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/20353411/",
      "year": "2010"
    },
    {
      "first_author": "Gazzola",
      "generic_name": "gabapentin",
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
      "generic_name": "gabapentin",
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
      "first_author": "PMID",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "16397976",
      "pub_types": "Comparative Study; Journal Article",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Pregabalin: new drug. Very similar to gabapentin.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/16397976/",
      "year": "2005"
    },
    {
      "first_author": "Gidal",
      "generic_name": "gabapentin",
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
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "11987312",
      "pub_types": "Journal Article",
      "reason": "no randomized language",
      "status": "rejected",
      "title": "Gabapentin: new indication. Little impact on partial epilepsy in children between 3 and 12.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/11987312/",
      "year": "2002"
    },
    {
      "first_author": "Fisher",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "11274308",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Rapid initiation of gabapentin: a randomized, controlled trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/11274308/",
      "year": "2001"
    },
    {
      "first_author": "Dodrill",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "10372564",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "title lacks seizure/epilepsy context",
      "status": "rejected",
      "title": "Cognitive abilities and adjustment with gabapentin: results of a multisite study.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10372564/",
      "year": "1999"
    },
    {
      "first_author": "Chadwick",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "8956916",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Gabapentin in generalized seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8956916/",
      "year": "1996"
    },
    {
      "first_author": "Sivenius",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "7945002",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Long-term study with gabapentin in patients with drug-resistant epileptic seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/7945002/",
      "year": "1994"
    },
    {
      "first_author": "Handforth",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "7925148",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "drug appears in title but not as primary intervention",
      "status": "rejected",
      "title": "Efficacy and tolerance of long-term, high-dose gabapentin: additional observations.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/7925148/",
      "year": "1994"
    },
    {
      "first_author": "Ben-Menachem",
      "generic_name": "gabapentin",
      "label": "",
      "pmid": "1373372",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article",
      "reason": "no randomized language",
      "status": "rejected",
      "title": "Selected CSF biochemistry and gabapentin concentrations in the CSF and plasma in patients with partial seizures after a single oral dose of gabapentin.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/1373372/",
      "year": "1992"
    }
  ],
  "possible_duplicate_name_hits": []
}
