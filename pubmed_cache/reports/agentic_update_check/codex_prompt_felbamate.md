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
    "adverse_symptoms_percentages": "GI: anorexia 19%, GI: vomiting 17%, CNS: insomnia 16%, GI: nausea 12%, CNS: headache 12%, hematologic/hepatic: aplastic anemia/hepatic failure <1%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "data_most_recently_refreshed": "05-20-2026",
    "diff_50_responder_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo RR50 differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_median_pct_change_maximum_effective_dose": "23 % (drug minus placebo MPC differential at maximum effective dose/regimen: FelbamateStudyGroupinLennoxGastautSyndrome1993 felbamate up to 45 mg/kg/day or 3600 mg/day 23%)",
    "diff_seizure_freedom_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "enzyme_inducing_or_inhibiting": "Inhibits CYP2C19; induces CYP3A4",
    "epilepsy_type": "Focal; LGS; Generalized",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Wikipedia anticonvulsant drug-class list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review",
    "fda_black_box_warning": "WARNING 1. APLASTIC ANEMIA THE USE OF FELBATOL ® (felbamate) IS ASSOCIATED WITH A MARKED INCREASE IN THE INCIDENCE OF APLASTIC ANEMIA. ACCORDINGLY, FELBATOL ® SHOULD ONLY BE USED IN PATIENTS WHOSE EPILEPSY IS SO SEVERE THAT THE RISK OF APLASTIC ANEMIA IS DEEMED ACCEPTABLE IN LIGHT OF THE BENEFITS CONFERRED BY ITS USE (SEE INDICATIONS ). ORDINARILY, A PATIENT SHOULD NOT BE PLACED ON AND/OR CONTINUED ON FELBATOL ® WITHOUT CONSIDERATION OF APPROPRIATE EXPERT HEMATOLOGIC CONSULTATION. AMONG FELBATOL ® TREATED PATIENTS, APLASTIC ANEMIA (PANCYTOPENIA IN THE PRESENCE OF A BONE MARROW LARGELY DEPLETED OF HEMATOPOIETIC PRECURSORS) OCCURS AT AN INCIDENCE THAT MAY BE MORE THAN A 100 FOLD GREATER THAN THAT SEEN IN THE UNTREATED POPULATION (I.E., 2 TO 5 PER MILLION PERSONS PER YEAR). THE RISK OF DEATH IN PATIENTS WITH APLASTIC ANEMIA GENERALLY VARIES AS A FUNCTION OF ITS SEVERITY AND ETIOLOGY; CURRENT ESTIMATES OF THE OVERALL CASE FATALITY RATE ARE IN THE RANGE OF 20 TO 30%, BUT RATES AS HIGH AS 70% HAVE BEEN REPORTED IN THE PAST. THERE ARE TOO FEW FELBATOL ® ASSOCIATED CASES, AND TOO LITTLE KNOWN ABOUT THEM TO PROVIDE A RELIABLE ESTIMATE OF THE SYNDROME’S INCIDENCE OR ITS CASE FATALITY RATE OR TO IDENTIFY THE FACTORS, IF ANY, THAT MIGHT CONCEIVABLY BE USED TO PREDICT WHO IS AT GREATER OR LESSER RISK. IN MANAGING PATIENTS ON FELBATOL ® , IT SHOULD BE BORNE IN MIND THAT THE CLINICAL MANIFESTATION OF APLASTIC ANEMIA MAY NOT BE SEEN UNTIL AFTER A PATIENT HAS BEEN ON FELBATOL ® FOR SEVERAL MONTHS (E.G., ONSET OF APLASTIC ANEMIA AMONG FELBATOL ® EXPOSED PATIENTS FOR WHOM DATA ARE AVAILABLE HAS RANGED FROM 5 TO 30 WEEKS). HOWEVER, THE INJURY TO BONE MARROW STEM CELLS THAT IS HELD TO BE ULTIMATELY RESPONSIBLE FOR THE ANEMIA MAY OCCUR WEEKS TO MONTHS EARLIER. ACCORDINGLY, PATIENTS WHO ARE DISCONTINUED FROM FELBATOL ® REMAIN AT RISK FOR DEVELOPING ANEMIA FOR A VARIABLE, AND UNKNOWN, PERIOD AFTERWARDS. IT IS NOT KNOWN WHETHER OR NOT THE RISK OF DEVELOPING APLASTIC ANEMIA CHANGES WITH DURATION OF EXPOSURE. CONSEQUENTLY, IT IS NOT SAFE TO ASSUME THAT A PATIENT WHO HAS BEEN ON FELBATOL ® WITHOUT SIGNS OF HEMATOLOGIC ABNORMALITY FOR LONG PERIODS OF TIME IS WITHOUT RISK. IT IS NOT KNOWN WHETHER OR NOT THE DOSE OF FELBATOL ® AFFECTS THE INCIDENCE OF APLASTIC ANEMIA. IT IS NOT KNOWN WHETHER OR NOT CONCOMITANT USE OF ANTIEPILEPTIC DRUGS AND/OR OTHER DRUGS AFFECTS THE INCIDENCE OF APLASTIC ANEMIA. APLASTIC ANEMIA TYPICALLY DEVELOPS WITHOUT PREMONITORY CLINICAL OR LABORATORY SIGNS, THE FULL BLOWN SYNDROME PRESENTING WITH SIGNS OF INFECTION, BLEEDING, OR ANEMIA. ACCORDINGLY, ROUTINE BLOOD TESTING CANNOT BE RELIABLY USED TO REDUCE THE INCIDENCE OF APLASTIC ANEMIA, BUT, IT WILL, IN SOME CASES, ALLOW THE DETECTION OF THE HEMATOLOGIC CHANGES BEFORE THE SYNDROME DECLARES ITSELF CLINICALLY. FELBATOL ® SHOULD BE DISCONTINUED IF ANY EVIDENCE OF BONE MARROW DEPRESSION OCCURS. 2. HEPATIC FAILURE EVALUATION OF POSTMARKETING EXPERIENCE SUGGESTS THAT ACUTE LIVER FAILURE IS ASSOCIATED WITH THE USE OF FELBATOL ® . THE REPORTED RATE IN THE U.S. HAS BEEN ABOUT 6 CASES OF LIVER FAILURE LEADING TO DEATH OR TRANSPLANT PER 75,000 PATIENT YEARS OF USE. THIS RATE IS AN UNDERESTIMATE BECAUSE OF UNDER REPORTING, AND THE TRUE RATE COULD BE CONSIDERABLY GREATER THAN THIS. FOR EXAMPLE, IF THE REPORTING RATE IS 10%, THE TRUE RATE WOULD BE ONE CASE PER 1,250 PATIENT YEARS OF USE. OF THE CASES REPORTED, ABOUT 67% RESULTED IN DEATH OR LIVER TRANSPLANTATION, USUALLY WITHIN 5 WEEKS OF THE ONSET OF SIGNS AND SYMPTOMS OF LIVER FAILURE. THE EARLIEST ONSET OF SEVERE HEPATIC DYSFUNCTION FOLLOWED SUBSEQUENTLY BY LIVER FAILURE WAS 3 WEEKS AFTER INITIATION OF FELBATOL ® . ALTHOUGH SOME REPORTS DESCRIBED DARK URINE AND NONSPECIFIC PRODROMAL SYMPTOMS (E.G., ANOREXIA, MALAISE, AND GASTROINTESTINAL SYMPTOMS), IN OTHER REPORTS IT WAS NOT CLEAR IF ANY PRODROMAL SYMPTOMS PRECEDED THE ONSET OF JAUNDICE. IT IS NOT KNOWN WHETHER OR NOT THE RISK OF DEVELOPING HEPATIC FAILURE CHANGES WITH DURATION OF EXPOSURE. IT IS NOT KNOWN WHETHER OR NOT THE DOSAGE OF FELBATOL ® AFFECTS THE INCIDENCE OF HEPATIC FAILURE. IT IS NOT KNOWN WHETHER CONCOMITANT USE OF OTHER ANTIEPILEPTIC DRUGS AND/OR OTHER DRUGS AFFECT THE INCIDENCE OF HEPATIC FAILURE. FELBATOL ® SHOULD NOT BE PRESCRIBED FOR ANYONE WITH A HISTORY OF HEPATIC DYSFUNCTION. TREATMENT WITH FELBATOL ® SHOULD BE INITIATED ONLY IN INDIVIDUALS WITHOUT ACTIVE LIVER DISEASE AND WITH NORMAL BASELINE SERUM TRANSAMINASES. IT HAS NOT BEEN PROVED THAT PERIODIC SERUM TRANSAMINASE TESTING WILL PREVENT SERIOUS INJURY BUT IT IS GENERALLY BELIEVED THAT EARLY DETECTION OF DRUG-INDUCED HEPATIC INJURY ALONG WITH IMMEDIATE WITHDRAWAL OF THE SUSPECT DRUG ENHANCES THE LIKELIHOOD FOR RECOVERY. THERE IS NO INFORMATION AVAILABLE THAT DOCUMENTS HOW RAPIDLY PATIENTS CAN PROGRESS FROM NORMAL LIVER FUNCTION TO LIVER FAILURE, BUT OTHER DRUGS KNOWN TO BE HEPATOTOXINS CAN CAUSE LIVER FAILURE RAPIDLY (E.G., FROM NORMAL ENZYMES TO LIVER FAILURE IN 2-4 WEEKS). ACCORDINGLY, MONITORING OF SERUM TRANSAMINASE LEVELS (AST AND ALT) IS RECOMMENDED AT BASELINE AND PERIODICALLY THEREAFTER. WHILE THE MORE FREQUENT THE MONITORING THE GREATER THE CHANCES OF EARLY DETECTION, THE PRECISE SCHEDULE FOR MONITORING IS A MATTER OF CLINICAL JUDGEMENT. FELBATOL ® SHOULD BE DISCONTINUED IF EITHER SERUM AST OR SERUM ALT LEVELS BECOME INCREASED ≥ 2 TIMES THE UPPER LIMIT OF NORMAL, OR IF CLINICAL SIGNS AND SYMPTOMS SUGGEST LIVER FAILURE (SEE PRECAUTIONS ). PATIENTS WHO DEVELOP EVIDENCE OF HEPATOCELLULAR INJURY WHILE ON FELBATOL ® AND ARE WITHDRAWN FROM THE DRUG FOR ANY REASON SHOULD BE PRESUMED TO BE AT INCREASED RISK FOR LIVER INJURY IF FELBATOL ® IS REINTRODUCED. ACCORDINGLY, SUCH PATIENTS SHOULD NOT BE CONSIDERED FOR RE-TREATMENT.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=boxed_warning_found; setid=2f522701-397a-11de-8a39-0800200c9a66; published=Dec 31, 2025; title=FELBATOL (FELBAMATE) TABLET FELBATOL (FELBAMATE) SUSPENSION [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2f522701-397a-11de-8a39-0800200c9a66",
    "fda_black_box_warning_verified": "05-20-2026",
    "filter_availability": "Available in US",
    "filter_enzyme_effect": "Inhibitor",
    "filter_epilepsy_type": "Focal; Generalized; LGS",
    "filter_formulation": "Liquid; Tablet",
    "filter_mechanism": "GABA; Glutamate receptor",
    "filter_metabolism": "Liver/hepatic",
    "filter_qt_effect": "No known meaningful QT effect",
    "filter_symptom_category": "CNS; GI; Hematologic/hepatic",
    "formulations_available": "Tablet; oral suspension",
    "generic_name": "felbamate",
    "half_life_range": "14-23 h",
    "major_organ_for_metabolism": "Liver",
    "maximum_approved_daily_dose": "3600 mg/day",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Anticonvulsant mechanism is unknown in labeling; proposed mechanisms include reduced seizure spread with NMDA receptor inhibition and GABA-A receptor modulation.",
    "mechanism_source": "FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "1200 mg/day",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "FelbamateStudyGroupinLennoxGastautSyndrome1993|23|https://pubmed.ncbi.nlm.nih.gov/8347179/|73",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "Siegel1999|https://pubmed.ncbi.nlm.nih.gov/10210023/; Devinsky1995|https://pubmed.ncbi.nlm.nih.gov/7796796/; FelbamateStudyGroupinLennoxGastautSyndrome1993|https://pubmed.ncbi.nlm.nih.gov/8347179/; Bourgeois1993|https://pubmed.ncbi.nlm.nih.gov/8469324/; Theodore1991|https://pubmed.ncbi.nlm.nih.gov/2044501/; Leppik1991|https://pubmed.ncbi.nlm.nih.gov/1944909/",
    "pubmed_search_aliases": "",
    "qt_interval_effect": "No clinically meaningful QT effect established",
    "rct_pubmed_verification_notes": "PubMed loop 21/65 on 2026-05-15: 6 qualifying placebo-controlled randomized clinical trial report(s) retained from 12 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.",
    "status_or_notes": "Restricted-use ASM for severe/refractory epilepsy because of serious aplastic anemia and hepatic failure risks.",
    "trade_names": "Felbatol; Taloxa",
    "typical_doses_per_day": "Adults: 1200-3600 mg/day divided TID/QID",
    "year_fda_cleared": "1993"
  },
  "existing_pubmed_links": [
    {
      "entry": "Siegel1999|https://pubmed.ncbi.nlm.nih.gov/10210023/",
      "label": "Siegel1999",
      "pmid": "10210023",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10210023/"
    },
    {
      "entry": "Devinsky1995|https://pubmed.ncbi.nlm.nih.gov/7796796/",
      "label": "Devinsky1995",
      "pmid": "7796796",
      "url": "https://pubmed.ncbi.nlm.nih.gov/7796796/"
    },
    {
      "entry": "FelbamateStudyGroupinLennoxGastautSyndrome1993|https://pubmed.ncbi.nlm.nih.gov/8347179/",
      "label": "FelbamateStudyGroupinLennoxGastautSyndrome1993",
      "pmid": "8347179",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8347179/"
    },
    {
      "entry": "Bourgeois1993|https://pubmed.ncbi.nlm.nih.gov/8469324/",
      "label": "Bourgeois1993",
      "pmid": "8469324",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8469324/"
    },
    {
      "entry": "Theodore1991|https://pubmed.ncbi.nlm.nih.gov/2044501/",
      "label": "Theodore1991",
      "pmid": "2044501",
      "url": "https://pubmed.ncbi.nlm.nih.gov/2044501/"
    },
    {
      "entry": "Leppik1991|https://pubmed.ncbi.nlm.nih.gov/1944909/",
      "label": "Leppik1991",
      "pmid": "1944909",
      "url": "https://pubmed.ncbi.nlm.nih.gov/1944909/"
    }
  ],
  "fact_fields_to_check": {
    "adverse_symptoms_percentages": "GI: anorexia 19%, GI: vomiting 17%, CNS: insomnia 16%, GI: nausea 12%, CNS: headache 12%, hematologic/hepatic: aplastic anemia/hepatic failure <1%",
    "alternate_generic_names": "",
    "available_in_us": "Yes",
    "diff_50_responder_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo RR50 differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "diff_median_pct_change_maximum_effective_dose": "23 % (drug minus placebo MPC differential at maximum effective dose/regimen: FelbamateStudyGroupinLennoxGastautSyndrome1993 felbamate up to 45 mg/kg/day or 3600 mg/day 23%)",
    "diff_seizure_freedom_maximum_effective_dose": "NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records",
    "enzyme_inducing_or_inhibiting": "Inhibits CYP2C19; induces CYP3A4",
    "epilepsy_type": "Focal; LGS; Generalized",
    "evidence_sources": "NCBI LiverTox anticonvulsants table; Wikipedia anticonvulsant drug-class list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review",
    "fda_black_box_warning": "WARNING 1. APLASTIC ANEMIA THE USE OF FELBATOL ® (felbamate) IS ASSOCIATED WITH A MARKED INCREASE IN THE INCIDENCE OF APLASTIC ANEMIA. ACCORDINGLY, FELBATOL ® SHOULD ONLY BE USED IN PATIENTS WHOSE EPILEPSY IS SO SEVERE THAT THE RISK OF APLASTIC ANEMIA IS DEEMED ACCEPTABLE IN LIGHT OF THE BENEFITS CONFERRED BY ITS USE (SEE INDICATIONS ). ORDINARILY, A PATIENT SHOULD NOT BE PLACED ON AND/OR CONTINUED ON FELBATOL ® WITHOUT CONSIDERATION OF APPROPRIATE EXPERT HEMATOLOGIC CONSULTATION. AMONG FELBATOL ® TREATED PATIENTS, APLASTIC ANEMIA (PANCYTOPENIA IN THE PRESENCE OF A BONE MARROW LARGELY DEPLETED OF HEMATOPOIETIC PRECURSORS) OCCURS AT AN INCIDENCE THAT MAY BE MORE THAN A 100 FOLD GREATER THAN THAT SEEN IN THE UNTREATED POPULATION (I.E., 2 TO 5 PER MILLION PERSONS PER YEAR). THE RISK OF DEATH IN PATIENTS WITH APLASTIC ANEMIA GENERALLY VARIES AS A FUNCTION OF ITS SEVERITY AND ETIOLOGY; CURRENT ESTIMATES OF THE OVERALL CASE FATALITY RATE ARE IN THE RANGE OF 20 TO 30%, BUT RATES AS HIGH AS 70% HAVE BEEN REPORTED IN THE PAST. THERE ARE TOO FEW FELBATOL ® ASSOCIATED CASES, AND TOO LITTLE KNOWN ABOUT THEM TO PROVIDE A RELIABLE ESTIMATE OF THE SYNDROME’S INCIDENCE OR ITS CASE FATALITY RATE OR TO IDENTIFY THE FACTORS, IF ANY, THAT MIGHT CONCEIVABLY BE USED TO PREDICT WHO IS AT GREATER OR LESSER RISK. IN MANAGING PATIENTS ON FELBATOL ® , IT SHOULD BE BORNE IN MIND THAT THE CLINICAL MANIFESTATION OF APLASTIC ANEMIA MAY NOT BE SEEN UNTIL AFTER A PATIENT HAS BEEN ON FELBATOL ® FOR SEVERAL MONTHS (E.G., ONSET OF APLASTIC ANEMIA AMONG FELBATOL ® EXPOSED PATIENTS FOR WHOM DATA ARE AVAILABLE HAS RANGED FROM 5 TO 30 WEEKS). HOWEVER, THE INJURY TO BONE MARROW STEM CELLS THAT IS HELD TO BE ULTIMATELY RESPONSIBLE FOR THE ANEMIA MAY OCCUR WEEKS TO MONTHS EARLIER. ACCORDINGLY, PATIENTS WHO ARE DISCONTINUED FROM FELBATOL ® REMAIN AT RISK FOR DEVELOPING ANEMIA FOR A VARIABLE, AND UNKNOWN, PERIOD AFTERWARDS. IT IS NOT KNOWN WHETHER OR NOT THE RISK OF DEVELOPING APLASTIC ANEMIA CHANGES WITH DURATION OF EXPOSURE. CONSEQUENTLY, IT IS NOT SAFE TO ASSUME THAT A PATIENT WHO HAS BEEN ON FELBATOL ® WITHOUT SIGNS OF HEMATOLOGIC ABNORMALITY FOR LONG PERIODS OF TIME IS WITHOUT RISK. IT IS NOT KNOWN WHETHER OR NOT THE DOSE OF FELBATOL ® AFFECTS THE INCIDENCE OF APLASTIC ANEMIA. IT IS NOT KNOWN WHETHER OR NOT CONCOMITANT USE OF ANTIEPILEPTIC DRUGS AND/OR OTHER DRUGS AFFECTS THE INCIDENCE OF APLASTIC ANEMIA. APLASTIC ANEMIA TYPICALLY DEVELOPS WITHOUT PREMONITORY CLINICAL OR LABORATORY SIGNS, THE FULL BLOWN SYNDROME PRESENTING WITH SIGNS OF INFECTION, BLEEDING, OR ANEMIA. ACCORDINGLY, ROUTINE BLOOD TESTING CANNOT BE RELIABLY USED TO REDUCE THE INCIDENCE OF APLASTIC ANEMIA, BUT, IT WILL, IN SOME CASES, ALLOW THE DETECTION OF THE HEMATOLOGIC CHANGES BEFORE THE SYNDROME DECLARES ITSELF CLINICALLY. FELBATOL ® SHOULD BE DISCONTINUED IF ANY EVIDENCE OF BONE MARROW DEPRESSION OCCURS. 2. HEPATIC FAILURE EVALUATION OF POSTMARKETING EXPERIENCE SUGGESTS THAT ACUTE LIVER FAILURE IS ASSOCIATED WITH THE USE OF FELBATOL ® . THE REPORTED RATE IN THE U.S. HAS BEEN ABOUT 6 CASES OF LIVER FAILURE LEADING TO DEATH OR TRANSPLANT PER 75,000 PATIENT YEARS OF USE. THIS RATE IS AN UNDERESTIMATE BECAUSE OF UNDER REPORTING, AND THE TRUE RATE COULD BE CONSIDERABLY GREATER THAN THIS. FOR EXAMPLE, IF THE REPORTING RATE IS 10%, THE TRUE RATE WOULD BE ONE CASE PER 1,250 PATIENT YEARS OF USE. OF THE CASES REPORTED, ABOUT 67% RESULTED IN DEATH OR LIVER TRANSPLANTATION, USUALLY WITHIN 5 WEEKS OF THE ONSET OF SIGNS AND SYMPTOMS OF LIVER FAILURE. THE EARLIEST ONSET OF SEVERE HEPATIC DYSFUNCTION FOLLOWED SUBSEQUENTLY BY LIVER FAILURE WAS 3 WEEKS AFTER INITIATION OF FELBATOL ® . ALTHOUGH SOME REPORTS DESCRIBED DARK URINE AND NONSPECIFIC PRODROMAL SYMPTOMS (E.G., ANOREXIA, MALAISE, AND GASTROINTESTINAL SYMPTOMS), IN OTHER REPORTS IT WAS NOT CLEAR IF ANY PRODROMAL SYMPTOMS PRECEDED THE ONSET OF JAUNDICE. IT IS NOT KNOWN WHETHER OR NOT THE RISK OF DEVELOPING HEPATIC FAILURE CHANGES WITH DURATION OF EXPOSURE. IT IS NOT KNOWN WHETHER OR NOT THE DOSAGE OF FELBATOL ® AFFECTS THE INCIDENCE OF HEPATIC FAILURE. IT IS NOT KNOWN WHETHER CONCOMITANT USE OF OTHER ANTIEPILEPTIC DRUGS AND/OR OTHER DRUGS AFFECT THE INCIDENCE OF HEPATIC FAILURE. FELBATOL ® SHOULD NOT BE PRESCRIBED FOR ANYONE WITH A HISTORY OF HEPATIC DYSFUNCTION. TREATMENT WITH FELBATOL ® SHOULD BE INITIATED ONLY IN INDIVIDUALS WITHOUT ACTIVE LIVER DISEASE AND WITH NORMAL BASELINE SERUM TRANSAMINASES. IT HAS NOT BEEN PROVED THAT PERIODIC SERUM TRANSAMINASE TESTING WILL PREVENT SERIOUS INJURY BUT IT IS GENERALLY BELIEVED THAT EARLY DETECTION OF DRUG-INDUCED HEPATIC INJURY ALONG WITH IMMEDIATE WITHDRAWAL OF THE SUSPECT DRUG ENHANCES THE LIKELIHOOD FOR RECOVERY. THERE IS NO INFORMATION AVAILABLE THAT DOCUMENTS HOW RAPIDLY PATIENTS CAN PROGRESS FROM NORMAL LIVER FUNCTION TO LIVER FAILURE, BUT OTHER DRUGS KNOWN TO BE HEPATOTOXINS CAN CAUSE LIVER FAILURE RAPIDLY (E.G., FROM NORMAL ENZYMES TO LIVER FAILURE IN 2-4 WEEKS). ACCORDINGLY, MONITORING OF SERUM TRANSAMINASE LEVELS (AST AND ALT) IS RECOMMENDED AT BASELINE AND PERIODICALLY THEREAFTER. WHILE THE MORE FREQUENT THE MONITORING THE GREATER THE CHANCES OF EARLY DETECTION, THE PRECISE SCHEDULE FOR MONITORING IS A MATTER OF CLINICAL JUDGEMENT. FELBATOL ® SHOULD BE DISCONTINUED IF EITHER SERUM AST OR SERUM ALT LEVELS BECOME INCREASED ≥ 2 TIMES THE UPPER LIMIT OF NORMAL, OR IF CLINICAL SIGNS AND SYMPTOMS SUGGEST LIVER FAILURE (SEE PRECAUTIONS ). PATIENTS WHO DEVELOP EVIDENCE OF HEPATOCELLULAR INJURY WHILE ON FELBATOL ® AND ARE WITHDRAWN FROM THE DRUG FOR ANY REASON SHOULD BE PRESUMED TO BE AT INCREASED RISK FOR LIVER INJURY IF FELBATOL ® IS REINTRODUCED. ACCORDINGLY, SUCH PATIENTS SHOULD NOT BE CONSIDERED FOR RE-TREATMENT.",
    "fda_black_box_warning_source": "FDA/DailyMed SPL; status=boxed_warning_found; setid=2f522701-397a-11de-8a39-0800200c9a66; published=Dec 31, 2025; title=FELBATOL (FELBAMATE) TABLET FELBATOL (FELBAMATE) SUSPENSION [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2f522701-397a-11de-8a39-0800200c9a66",
    "formulations_available": "Tablet; oral suspension",
    "half_life_range": "14-23 h",
    "major_organ_for_metabolism": "Liver",
    "maximum_approved_daily_dose": "3600 mg/day",
    "mechanism_confidence": "Moderate",
    "mechanism_of_action": "Anticonvulsant mechanism is unknown in labeling; proposed mechanisms include reduced seizure spread with NMDA receptor inhibition and GABA-A receptor modulation.",
    "mechanism_source": "FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review",
    "mechanism_source_tier": "FDA label",
    "minimum_effective_dose": "1200 mg/day",
    "plot_diff_50_responder_maximum_effective_dose": "",
    "plot_diff_median_pct_change_maximum_effective_dose": "FelbamateStudyGroupinLennoxGastautSyndrome1993|23|https://pubmed.ncbi.nlm.nih.gov/8347179/|73",
    "plot_diff_seizure_freedom_maximum_effective_dose": "",
    "pubmed_phase_ii_iii_rct_links": "Siegel1999|https://pubmed.ncbi.nlm.nih.gov/10210023/; Devinsky1995|https://pubmed.ncbi.nlm.nih.gov/7796796/; FelbamateStudyGroupinLennoxGastautSyndrome1993|https://pubmed.ncbi.nlm.nih.gov/8347179/; Bourgeois1993|https://pubmed.ncbi.nlm.nih.gov/8469324/; Theodore1991|https://pubmed.ncbi.nlm.nih.gov/2044501/; Leppik1991|https://pubmed.ncbi.nlm.nih.gov/1944909/",
    "pubmed_search_aliases": "",
    "qt_interval_effect": "No clinically meaningful QT effect established",
    "trade_names": "Felbatol; Taloxa",
    "typical_doses_per_day": "Adults: 1200-3600 mg/day divided TID/QID",
    "year_fda_cleared": "1993"
  },
  "generic_name": "felbamate",
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
      "current_value": "Siegel1999|https://pubmed.ncbi.nlm.nih.gov/10210023/",
      "details": {
        "article": {
          "abstract": "We studied the efficacy of felbamate (FBM) in combination with valproic acid (VPA) in 13 patients with the Lennox-Gastaut syndrome and evaluated the contribution of each drug. Following stabilization on VPA monotherapy, FBM or placebo titration was performed for two observation periods lasting 7 weeks with a washout period between them. 6-h video-electroencephalography was recorded following each observation period. In addition to examining the effects of the drugs with parental reports and video-EEG, we compared video-EEG data with families' seizure reports. Based on parental counts for the 7-week observation periods, patients had 40% fewer drop attacks (p < 0.03, Wilcoxon rank sum test) and 60% fewer total seizures (p < 0.02) on VPA and FBM. VPA level rose by 12.7% when FBM was added (p < 0.01). When the effect of FBM was factored out, VPA had a significant effect on drop attack frequency, although not total number of seizures. FBM's therapeutic effect on drop attacks is due in part to increased VPA levels, although the combination may be synergistic for the effect on total seizure number.",
          "first_author": "Siegel",
          "pmid": "10210023",
          "pub_types": [
            "Clinical Trial",
            "Controlled Clinical Trial",
            "Journal Article",
            "Randomized Controlled Trial"
          ],
          "title": "The efficacy of felbamate as add-on therapy to valproic acid in the Lennox-Gastaut syndrome.",
          "year": "1999"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/10210023/",
      "generic_name": "felbamate",
      "id": "rct_pubmed_concordance_problem-55ba540ee506",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 10210023 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 10210023 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "pubmed_phase_ii_iii_rct_links",
      "current_value": "Devinsky1995|https://pubmed.ncbi.nlm.nih.gov/7796796/",
      "details": {
        "article": {
          "abstract": "The efficacy and safety of felbamate monotherapy were evaluated in 52 patients with refractory partial seizures with or without secondary generalization in a double-blind, randomized, placebo-controlled trial. Each patient completed a routine evaluation for epilepsy surgery and was randomized to receive either felbamate, titrated to a maximum daily dose of 3600 mg over 2 days, or placebo during the 10-day, inpatient, treatment phase. An intent-to-treat analysis was performed on the data of all 52 patients who received study medication, while a separate efficacy analysis also was performed on the data of 43 evaluable patients, which excluded protocol violators. The endpoint of the trial was completing 10 days of treatment or the occurrence of a fourth seizure. The primary efficacy variable was the average daily seizure frequency during the treatment phase for each patient. For the intent-to-treat analysis based on all 52 patients who received study medications, the mean rank of the daily seizure frequency for patients treated with felbamate was 21.6 compared to 29.6 for patients treated with placebo (P = 0.065). In the analysis based on the 43 evaluable patients, the mean rank of the daily seizure frequency for felbamate-treated patients was 17.0 compared to 25.4 for placebo-treated patients. This difference was statistically significant (P = 0.032) in favor of felbamate. Seizure frequency was decreased by 89.5% compared to baseline in nine patients who completed 10 days of felbamate therapy. This study permitted the rapid determination of the anticonvulsant activity of felbamate and demonstrated that felbamate is effective as monotherapy for the treatment of partial seizures.",
          "first_author": "Devinsky",
          "pmid": "7796796",
          "pub_types": [
            "Clinical Trial",
            "Journal Article",
            "Randomized Controlled Trial",
            "Research Support, Non-U.S. Gov't"
          ],
          "title": "Efficacy of felbamate monotherapy in patients undergoing presurgical evaluation of partial seizures.",
          "year": "1995"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/7796796/",
      "generic_name": "felbamate",
      "id": "rct_pubmed_concordance_problem-88586dee4303",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 7796796 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 7796796 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
    },
    {
      "column": "pubmed_phase_ii_iii_rct_links",
      "current_value": "FelbamateStudyGroupinLennoxGastautSyndrome1993|https://pubmed.ncbi.nlm.nih.gov/8347179/",
      "details": {
        "article": {
          "abstract": "The Lennox-Gastaut syndrome is a childhood disorder characterized by multiple types of seizures, mental retardation, characteristic electroencephalographic abnormalities, and resistance to standard antiepileptic drugs. Felbamate is an investigational antiepileptic drug with a preclinical profile that suggests it would be effective in patients with multiple types of seizures. In controlled clinical trials, felbamate was superior to placebo in reducing the frequency of refractory partial-onset seizures. We studied the efficacy of felbamate in 73 patients ranging in age from 4 to 36 years who had the Lennox-Gastaut syndrome. During a 28-day base-line phase, the patients received their usual antiepileptic therapies. At the end of this phase, felbamate or placebo was administered for 70 days in addition to the current antiepileptic medications. The dosage of felbamate was titrated during the first 14 days of the treatment phase to a maximum of 45 mg per kilogram of body weight per day or 3600 mg per day, whichever was less. The primary efficacy variables were the total number of seizures counted during a four-hour period of video recording, parents' or guardians' global evaluations of the patients' quality of life, and the total number of atonic seizures, as reported by parents or guardians. The patients treated with felbamate had a 34 percent decrease in the frequency of atonic seizures, as compared with a 9 percent decrease in the patients who received placebo (P = 0.01). The felbamate-treated patients had a 19 percent decrease in the total frequency of seizures, as compared with a 4 percent increase in the placebo group (P = 0.002). The global-evaluation scores were significantly higher in the felbamate group than in the placebo group from day 49 to the end of the study. There were no significant differences in the frequency of seizures occurring during video monitoring, but there was a significant reduction (P = 0.017) in the number of tonic-clonic seizures during the maintenance period in the felbamate group. The types and frequency of side effects were similar in the two treatment groups. Felbamate is beneficial in patients with the Lennox-Gastaut syndrome.",
          "first_author": "Felbamate Study Group in Lennox-Gastaut Syndrome",
          "pmid": "8347179",
          "pub_types": [
            "Clinical Trial",
            "Journal Article",
            "Randomized Controlled Trial"
          ],
          "title": "Efficacy of felbamate in childhood epileptic encephalopathy (Lennox-Gastaut syndrome).",
          "year": "1993"
        },
        "reason": "title lacks primary randomized/placebo/phase trial language"
      },
      "evidence_url": "https://pubmed.ncbi.nlm.nih.gov/8347179/",
      "generic_name": "felbamate",
      "id": "rct_pubmed_concordance_problem-a5aa5e426454",
      "kind": "rct_pubmed_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"rct_pubmed_verification_notes\": \"update_check on 05-19-2026: PMID 8347179 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: PMID 8347179 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "PubMed",
      "summary": "Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language."
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
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5",
      "generic_name": "felbamate",
      "id": "source_fact_concordance_problem-84969f3cdb08",
      "kind": "source_fact_concordance_problem",
      "proposed_updates": {
        "__append_fields__": "{\"status_or_notes\": \"update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5); review current text before relying on it.\"}"
      },
      "proposed_value": "update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5); review current text before relying on it.",
      "requires_approval": true,
      "safe_to_apply": false,
      "severity": "high",
      "source": "FDA/openFDA",
      "summary": "year_fda_cleared could not be verified against the selected FDA/openFDA label."
    },
    {
      "column": "trade_names",
      "current_value": "Felbatol; Taloxa",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22lennox-gastaut%22&limit=100",
      "generic_name": "felbamate",
      "id": "trade_name_addition-51c562e53f69",
      "kind": "trade_name_addition",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA",
        "trade_names": "Felbamate"
      },
      "proposed_value": "Felbamate",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "medium",
      "source": "FDA/openFDA",
      "summary": "Source labels mention trade name(s) not present in CSV: Felbamate."
    },
    {
      "column": "fda_black_box_warning_source",
      "current_value": "FDA/DailyMed SPL; status=boxed_warning_found; setid=2f522701-397a-11de-8a39-0800200c9a66; published=Dec 31, 2025; title=FELBATOL (FELBAMATE) TABLET FELBATOL (FELBAMATE) SUSPENSION [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2f522701-397a-11de-8a39-0800200c9a66",
      "details": {},
      "evidence_url": "https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5",
      "generic_name": "felbamate",
      "id": "fda_warning_metadata_refresh-1fef5bcc9e9c",
      "kind": "fda_warning_metadata_refresh",
      "proposed_updates": {
        "data_most_recently_refreshed": "05-19-2026",
        "evidence_sources": "FDA/openFDA labeling",
        "fda_black_box_warning": "WARNING 1. APLASTIC ANEMIA THE USE OF FELBATOL ® (felbamate) IS ASSOCIATED WITH A MARKED INCREASE IN THE INCIDENCE OF APLASTIC ANEMIA. ACCORDINGLY, FELBATOL ® SHOULD ONLY BE USED IN PATIENTS WHOSE EPILEPSY IS SO SEVERE THAT THE RISK OF APLASTIC ANEMIA IS DEEMED ACCEPTABLE IN LIGHT OF THE BENEFITS CONFERRED BY ITS USE (SEE INDICATIONS ). ORDINARILY, A PATIENT SHOULD NOT BE PLACED ON AND/OR CONTINUED ON FELBATOL ® WITHOUT CONSIDERATION OF APPROPRIATE EXPERT HEMATOLOGIC CONSULTATION. AMONG FELBATOL ® TREATED PATIENTS, APLASTIC ANEMIA (PANCYTOPENIA IN THE PRESENCE OF A BONE MARROW LARGELY DEPLETED OF HEMATOPOIETIC PRECURSORS) OCCURS AT AN INCIDENCE THAT MAY BE MORE THAN A 100 FOLD GREATER THAN THAT SEEN IN THE UNTREATED POPULATION (I.E., 2 TO 5 PER MILLION PERSONS PER YEAR). THE RISK OF DEATH IN PATIENTS WITH APLASTIC ANEMIA GENERALLY VARIES AS A FUNCTION OF ITS SEVERITY AND ETIOLOGY; CURRENT ESTIMATES OF THE OVERALL CASE FATALITY RATE ARE IN THE RANGE OF 20 TO 30%, BUT RATES AS HIGH AS 70% HAVE BEEN REPORTED IN THE PAST. THERE ARE TOO FEW FELBATOL ® ASSOCIATED CASES, AND TOO LITTLE KNOWN ABOUT THEM TO PROVIDE A RELIABLE ESTIMATE OF THE SYNDROME’S INCIDENCE OR ITS CASE FATALITY RATE OR TO IDENTIFY THE FACTORS, IF ANY, THAT MIGHT CONCEIVABLY BE USED TO PREDICT WHO IS AT GREATER OR LESSER RISK. IN MANAGING PATIENTS ON FELBATOL ® , IT SHOULD BE BORNE IN MIND THAT THE CLINICAL MANIFESTATION OF APLASTIC ANEMIA MAY NOT BE SEEN UNTIL AFTER A PATIENT HAS BEEN ON FELBATOL ® FOR SEVERAL MONTHS (E.G., ONSET OF APLASTIC ANEMIA AMONG FELBATOL ® EXPOSED PATIENTS FOR WHOM DATA ARE AVAILABLE HAS RANGED FROM 5 TO 30 WEEKS). HOWEVER, THE INJURY TO BONE MARROW STEM CELLS THAT IS HELD TO BE ULTIMATELY RESPONSIBLE FOR THE ANEMIA MAY OCCUR WEEKS TO MONTHS EARLIER. ACCORDINGLY, PATIENTS WHO ARE DISCONTINUED FROM FELBATOL ® REMAIN AT RISK FOR DEVELOPING ANEMIA FOR A VARIABLE, AND UNKNOWN, PERIOD AFTERWARDS. IT IS NOT KNOWN WHETHER OR NOT THE RISK OF DEVELOPING APLASTIC ANEMIA CHANGES WITH DURATION OF EXPOSURE. CONSEQUENTLY, IT IS NOT SAFE TO ASSUME THAT A PATIENT WHO HAS BEEN ON FELBATOL ® WITHOUT SIGNS OF HEMATOLOGIC ABNORMALITY FOR LONG PERIODS OF TIME IS WITHOUT RISK. IT IS NOT KNOWN WHETHER OR NOT THE DOSE OF FELBATOL ® AFFECTS THE INCIDENCE OF APLASTIC ANEMIA. IT IS NOT KNOWN WHETHER OR NOT CONCOMITANT USE OF ANTIEPILEPTIC DRUGS AND/OR OTHER DRUGS AFFECTS THE INCIDENCE OF APLASTIC ANEMIA. APLASTIC ANEMIA TYPICALLY DEVELOPS WITHOUT PREMONITORY CLINICAL OR LABORATORY SIGNS, THE FULL BLOWN SYNDROME PRESENTING WITH SIGNS OF INFECTION, BLEEDING, OR ANEMIA. ACCORDINGLY, ROUTINE BLOOD TESTING CANNOT BE RELIABLY USED TO REDUCE THE INCIDENCE OF APLASTIC ANEMIA, BUT, IT WILL, IN SOME CASES, ALLOW THE DETECTION OF THE HEMATOLOGIC CHANGES BEFORE THE SYNDROME DECLARES ITSELF CLINICALLY. FELBATOL ® SHOULD BE DISCONTINUED IF ANY EVIDENCE OF BONE MARROW DEPRESSION OCCURS. 2. HEPATIC FAILURE EVALUATION OF POSTMARKETING EXPERIENCE SUGGESTS THAT ACUTE LIVER FAILURE IS ASSOCIATED WITH THE USE OF FELBATOL ® . THE REPORTED RATE IN THE U.S. HAS BEEN ABOUT 6 CASES OF LIVER FAILURE LEADING TO DEATH OR TRANSPLANT PER 75,000 PATIENT YEARS OF USE. THIS RATE IS AN UNDERESTIMATE BECAUSE OF UNDER REPORTING, AND THE TRUE RATE COULD BE CONSIDERABLY GREATER THAN THIS. FOR EXAMPLE, IF THE REPORTING RATE IS 10%, THE TRUE RATE WOULD BE ONE CASE PER 1,250 PATIENT YEARS OF USE. OF THE CASES REPORTED, ABOUT 67% RESULTED IN DEATH OR LIVER TRANSPLANTATION, USUALLY WITHIN 5 WEEKS OF THE ONSET OF SIGNS AND SYMPTOMS OF LIVER FAILURE. THE EARLIEST ONSET OF SEVERE HEPATIC DYSFUNCTION FOLLOWED SUBSEQUENTLY BY LIVER FAILURE WAS 3 WEEKS AFTER INITIATION OF FELBATOL ® . ALTHOUGH SOME REPORTS DESCRIBED DARK URINE AND NONSPECIFIC PRODROMAL SYMPTOMS (E.G., ANOREXIA, MALAISE, AND GASTROINTESTINAL SYMPTOMS), IN OTHER REPORTS IT WAS NOT CLEAR IF ANY PRODROMAL SYMPTOMS PRECEDED THE ONSET OF JAUNDICE. IT IS NOT KNOWN WHETHER OR NOT THE RISK OF DEVELOPING HEPATIC FAILURE CHANGES WITH DURATION OF EXPOSURE. IT IS NOT KNOWN WHETHER OR NOT THE DOSAGE OF FELBATOL ® AFFECTS THE INCIDENCE OF HEPATIC FAILURE. IT IS NOT KNOWN WHETHER CONCOMITANT USE OF OTHER ANTIEPILEPTIC DRUGS AND/OR OTHER DRUGS AFFECT THE INCIDENCE OF HEPATIC FAILURE. FELBATOL ® SHOULD NOT BE PRESCRIBED FOR ANYONE WITH A HISTORY OF HEPATIC DYSFUNCTION. TREATMENT WITH FELBATOL ® SHOULD BE INITIATED ONLY IN INDIVIDUALS WITHOUT ACTIVE LIVER DISEASE AND WITH NORMAL BASELINE SERUM TRANSAMINASES. IT HAS NOT BEEN PROVED THAT PERIODIC SERUM TRANSAMINASE TESTING WILL PREVENT SERIOUS INJURY BUT IT IS GENERALLY BELIEVED THAT EARLY DETECTION OF DRUG-INDUCED HEPATIC INJURY ALONG WITH IMMEDIATE WITHDRAWAL OF THE SUSPECT DRUG ENHANCES THE LIKELIHOOD FOR RECOVERY. THERE IS NO INFORMATION AVAILABLE THAT DOCUMENTS HOW RAPIDLY PATIENTS CAN PROGRESS FROM NORMAL LIVER FUNCTION TO LIVER FAILURE, BUT OTHER DRUGS KNOWN TO BE HEPATOTOXINS CAN CAUSE LIVER FAILURE RAPIDLY (E.G., FROM NORMAL ENZYMES TO LIVER FAILURE IN 2-4 WEEKS). ACCORDINGLY, MONITORING OF SERUM TRANSAMINASE LEVELS (AST AND ALT) IS RECOMMENDED AT BASELINE AND PERIODICALLY THEREAFTER. WHILE THE MORE FREQUENT THE MONITORING THE GREATER THE CHANCES OF EARLY DETECTION, THE PRECISE SCHEDULE FOR MONITORING IS A MATTER OF CLINICAL JUDGEMENT. FELBATOL ® SHOULD BE DISCONTINUED IF EITHER SERUM AST OR SERUM ALT LEVELS BECOME INCREASED ≥ 2 TIMES THE UPPER LIMIT OF NORMAL, OR IF CLINICAL SIGNS AND SYMPTOMS SUGGEST LIVER FAILURE (SEE PRECAUTIONS ). PATIENTS WHO DEVELOP EVIDENCE OF HEPATOCELLULAR INJURY WHILE ON FELBATOL ® AND ARE WITHDRAWN FROM THE DRUG FOR ANY REASON SHOULD BE PRESUMED TO BE AT INCREASED RISK FOR LIVER INJURY IF FELBATOL ® IS REINTRODUCED. ACCORDINGLY, SUCH PATIENTS SHOULD NOT BE CONSIDERED FOR RE-TREATMENT.",
        "fda_black_box_warning_source": "FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2f522701-397a-11de-8a39-0800200c9a66; effective_time=20250815; title=Felbatol / FELBAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5",
        "fda_black_box_warning_verified": "05-19-2026"
      },
      "proposed_value": "FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2f522701-397a-11de-8a39-0800200c9a66; effective_time=20250815; title=Felbatol / FELBAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5",
      "requires_approval": false,
      "safe_to_apply": true,
      "severity": "info",
      "source": "FDA/openFDA",
      "summary": "FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed."
    }
  ],
  "local_outcome_audit_rows": [
    {
      "audit_note": "Small crossover add-on study reports fewer seizures on felbamate plus valproate, but not an extractable arm-specific RR50/MPC/seizure-freedom differential.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "felbamate",
      "label": "Siegel1999",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "10210023",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/10210023/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "The efficacy of felbamate as add-on therapy to valproic acid in the Lennox-Gastaut syndrome."
    },
    {
      "audit_note": "Presurgical monotherapy trial reports daily seizure frequency ranks and completer seizure reductions, but no extractable active/placebo RR50, MPC, or seizure-freedom differential.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "felbamate",
      "label": "Devinsky1995",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "7796796",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/7796796/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy of felbamate monotherapy in patients undergoing presurgical evaluation of partial seizures."
    },
    {
      "audit_note": "Presurgical-evaluation trial reports time-to-fourth-seizure and fourth-seizure event proportions, not RR50, MPC, or seizure-freedom patient rates.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "felbamate",
      "label": "Bourgeois1993",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "8469324",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8469324/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Felbamate: a double-blind controlled trial in patients undergoing presurgical evaluation of partial seizures."
    },
    {
      "audit_note": "Abstract reports total seizure frequency decreased 19% with felbamate versus a 4% increase with placebo.",
      "dose_or_regimen": "felbamate up to 45 mg/kg/day or 3600 mg/day",
      "endpoint": "LGS seizures",
      "generic_name": "felbamate",
      "label": "FelbamateStudyGroupinLennoxGastautSyndrome1993",
      "mpc_active_percent": "",
      "mpc_differential_percent": "23.0",
      "mpc_included_in_csv_summary": "yes",
      "mpc_placebo_percent": "",
      "pmid": "8347179",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/8347179/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Efficacy of felbamate in childhood epileptic encephalopathy (Lennox-Gastaut syndrome)."
    },
    {
      "audit_note": "Abstract reports mean seizure frequencies and significant percent seizure reduction, but not extractable active/placebo percentage reductions.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "felbamate",
      "label": "Leppik1991",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "1944909",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/1944909/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Felbamate for partial seizures: results of a controlled clinical trial."
    },
    {
      "audit_note": "Crossover abstract reports no significant seizure-frequency difference and no extractable active/placebo percentages.",
      "dose_or_regimen": "",
      "endpoint": "",
      "generic_name": "felbamate",
      "label": "Theodore1991",
      "mpc_active_percent": "",
      "mpc_differential_percent": "",
      "mpc_included_in_csv_summary": "no",
      "mpc_placebo_percent": "",
      "pmid": "2044501",
      "pubmed_url": "https://pubmed.ncbi.nlm.nih.gov/2044501/",
      "rr50_active_percent": "",
      "rr50_differential_percent": "",
      "rr50_included_in_csv_summary": "no",
      "rr50_placebo_percent": "",
      "sf_active_percent": "",
      "sf_differential_percent": "",
      "sf_included_in_csv_summary": "no",
      "sf_placebo_percent": "",
      "title": "Felbamate: a clinical trial for complex partial seizures."
    }
  ],
  "local_rct_audit_rows": [
    {
      "first_author": "Siegel",
      "generic_name": "felbamate",
      "label": "Siegel1999",
      "pmid": "10210023",
      "pub_types": "Clinical Trial; Controlled Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "The efficacy of felbamate as add-on therapy to valproic acid in the Lennox-Gastaut syndrome.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/10210023/",
      "year": "1999"
    },
    {
      "first_author": "Devinsky",
      "generic_name": "felbamate",
      "label": "Devinsky1995",
      "pmid": "7796796",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy of felbamate monotherapy in patients undergoing presurgical evaluation of partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/7796796/",
      "year": "1995"
    },
    {
      "first_author": "Bourgeois",
      "generic_name": "felbamate",
      "label": "Bourgeois1993",
      "pmid": "8469324",
      "pub_types": "Clinical Trial; Journal Article; Multicenter Study; Randomized Controlled Trial; Research Support, Non-U.S. Gov't",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Felbamate: a double-blind controlled trial in patients undergoing presurgical evaluation of partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8469324/",
      "year": "1993"
    },
    {
      "first_author": "Felbamate Study Group in Lennox-Gastaut Syndrome",
      "generic_name": "felbamate",
      "label": "FelbamateStudyGroupinLennoxGastautSyndrome1993",
      "pmid": "8347179",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Efficacy of felbamate in childhood epileptic encephalopathy (Lennox-Gastaut syndrome).",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8347179/",
      "year": "1993"
    },
    {
      "first_author": "Leppik",
      "generic_name": "felbamate",
      "label": "Leppik1991",
      "pmid": "1944909",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial; Research Support, U.S. Gov't, P.H.S.",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Felbamate for partial seizures: results of a controlled clinical trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/1944909/",
      "year": "1991"
    },
    {
      "first_author": "Theodore",
      "generic_name": "felbamate",
      "label": "Theodore1991",
      "pmid": "2044501",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "qualifying placebo-controlled randomized clinical trial report",
      "status": "included",
      "title": "Felbamate: a clinical trial for complex partial seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/2044501/",
      "year": "1991"
    },
    {
      "first_author": "Ketter",
      "generic_name": "felbamate",
      "label": "",
      "pmid": "8964274",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Felbamate monotherapy has stimulant-like effects in patients with epilepsy.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8964274/",
      "year": "1996"
    },
    {
      "first_author": "Theodore",
      "generic_name": "felbamate",
      "label": "",
      "pmid": "7588454",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Felbamate monotherapy: implications for antiepileptic drug development.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/7588454/",
      "year": "1995"
    },
    {
      "first_author": "Sahlroot",
      "generic_name": "felbamate",
      "label": "",
      "pmid": "8019586",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial",
      "reason": "drug term not in title",
      "status": "rejected",
      "title": "Dosage adjustments in response to monitored plasma concentrations: can unblinded staff adhere to objective criteria?",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8019586/",
      "year": "1994"
    },
    {
      "first_author": "Jensen",
      "generic_name": "felbamate",
      "label": "",
      "pmid": "8039473",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Felbamate in the treatment of Lennox-Gastaut syndrome.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8039473/",
      "year": "1994"
    },
    {
      "first_author": "Jensen",
      "generic_name": "felbamate",
      "label": "",
      "pmid": "8243375",
      "pub_types": "Clinical Trial; Comparative Study; Journal Article; Randomized Controlled Trial",
      "reason": "title lacks primary randomized/placebo/phase trial language",
      "status": "rejected",
      "title": "Felbamate in the treatment of refractory partial-onset seizures.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8243375/",
      "year": "1993"
    },
    {
      "first_author": "Dodson",
      "generic_name": "felbamate",
      "label": "",
      "pmid": "8243374",
      "pub_types": "Clinical Trial; Journal Article; Randomized Controlled Trial",
      "reason": "excluded secondary/non-primary title",
      "status": "rejected",
      "title": "Felbamate in the treatment of Lennox-Gastaut syndrome: results of a 12-month open-label study following a randomized clinical trial.",
      "url": "https://pubmed.ncbi.nlm.nih.gov/8243374/",
      "year": "1993"
    }
  ],
  "possible_duplicate_name_hits": []
}
