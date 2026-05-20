# ASM update_check summary

Generated: 2026-05-19
CSV: /Users/dgoldenh/Documents/GitHub/ASM-master/ASM-list.csv

## Counts

- critical: 3
- high: 130
- medium: 188
- warning: 1
- info: 45

## Findings

### CRITICAL fda_warning_contradiction-67bcc8d4c339
- Kind: fda_warning_contradiction
- Medication: diazepam
- Source: FDA/openFDA
- Column: fda_black_box_warning
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22diazepam%22+OR+openfda.brand_name%3A%22diazepam%22+OR+openfda.substance_name%3A%22diazepam%22&limit=10
- Summary: Current FDA/openFDA boxed-warning extraction differs from the CSV. This is a direct contradiction and will not be applied without approval.
- Current: WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation [see Warnings and Precautions ( 5.1 ), Drug Interactions ( 7.1 )]. LIBERVANT is approved for use in pediatric patients 2 to 5 years of age. The unapproved use of LIBERVANT exposes users to risks of abuse, misuse...
- Proposed: WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation [see Warnings and Precautions (5.1) and Drug Interactions (7.1) ] . The use of benzodiazepines, including VALTOCO, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Ab...

### CRITICAL fda_warning_contradiction-7c4911e7c162
- Kind: fda_warning_contradiction
- Medication: lorazepam
- Source: FDA/openFDA
- Column: fda_black_box_warning
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Ativan%22+OR+openfda.brand_name%3A%22Ativan%22+OR+openfda.substance_name%3A%22Ativan%22&limit=10
- Summary: Current FDA/openFDA boxed-warning extraction differs from the CSV. This is a direct contradiction and will not be applied without approval.
- Current: WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS ; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs in patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation (see WARNINGS and PRECAUTIONS ). The use of benzodiazepines, including ATIVAN Injection, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of benzodia...
- Proposed: WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; and DEPENDENCE AND WITHDRAWAL REACTIONS • Concomitant use of benzodiazepines and opioids may result in profound sedation, respiratory depression, coma, and death. Reserve concomitant prescribing of these drugs for patients for whom alternative treatment options are inadequate. Limit dosages and durations to the minimum required. Follow patients for signs and symptoms of respiratory depression and sedation (see WARNINGS and PRECAUTIONS ). • The use of benzodiazepines, including Ativan, exposes users to risks of abuse, misuse, and addiction, which can lead to overdose or death. Abuse and misuse of benzodiazepine...

### CRITICAL rct_outcome_summary_mismatch-7882a6792154
- Kind: rct_outcome_summary_mismatch
- Medication: valproic acid
- Source: Local outcome validation
- Column: diff_50_responder_maximum_effective_dose
- Apply: safe=False; approval_required=True
- Evidence: /Users/dgoldenh/Documents/GitHub/ASM-master/pubmed_cache/reports/efficacy_outcome_audit.csv
- Summary: diff_50_responder_maximum_effective_dose does not match efficacy_outcome_audit.csv included rows.
- Current: 19 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Willmore1996 add-on divalproex sodium/valproate 19%)
- Proposed: 19 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Willmore1996 add-on divalproex sodium 19%)

### HIGH source_fact_concordance_problem-2f249df2d78f
- Kind: source_fact_concordance_problem
- Medication: acetazolamide
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-36dac3217b6d
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: brivaracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/41175011/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: A randomized, double-blind, placebo-controlled, time-to-event study of the efficacy and safety of JNJ-40411813 in combination with levetiracetam or brivaracetam in patients with focal onset seizures.
- Current: Yu2026|https://pubmed.ncbi.nlm.nih.gov/42092987/; Inoue2024|https://pubmed.ncbi.nlm.nih.gov/38576178/; Bast2022|https://pubmed.ncbi.nlm.nih.gov/35844134/; Kalviainen2015|https://pubmed.ncbi.nlm.nih.gov/26666500/; Klein2015|https://pubmed.ncbi.nlm.nih.gov/26471380/; Ryvlin2013|https://pubmed.ncbi.nlm.nih.gov/24256083/; Kwan2013|https://pubmed.ncbi.nlm.nih.gov/24116853/; Biton2013|https://pubmed.ncbi.nlm.nih.gov/24446953/; VanPaesschen2012|https://pubmed.ncbi.nlm.nih.gov/22813235/; French2010|https://pubmed.ncbi.nlm.nih.gov/20592253/
- Proposed: French2025|https://pubmed.ncbi.nlm.nih.gov/41175011/

### HIGH new_pubmed_phase_ii_iii_rct-7dcd25e54640
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: brivaracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/35582748/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Tolerability and efficacy of adjunctive brivaracetam in adults with focal seizures by concomitant antiseizure medication use: Pooled results from three phase 3 trials.
- Current: Yu2026|https://pubmed.ncbi.nlm.nih.gov/42092987/; Inoue2024|https://pubmed.ncbi.nlm.nih.gov/38576178/; Bast2022|https://pubmed.ncbi.nlm.nih.gov/35844134/; Kalviainen2015|https://pubmed.ncbi.nlm.nih.gov/26666500/; Klein2015|https://pubmed.ncbi.nlm.nih.gov/26471380/; Ryvlin2013|https://pubmed.ncbi.nlm.nih.gov/24256083/; Kwan2013|https://pubmed.ncbi.nlm.nih.gov/24116853/; Biton2013|https://pubmed.ncbi.nlm.nih.gov/24446953/; VanPaesschen2012|https://pubmed.ncbi.nlm.nih.gov/22813235/; French2010|https://pubmed.ncbi.nlm.nih.gov/20592253/
- Proposed: Ryvlin2022|https://pubmed.ncbi.nlm.nih.gov/35582748/

### HIGH new_pubmed_phase_ii_iii_rct-0e04ac73a88c
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: brivaracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/27988967/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Time to onset of sustained ≥50% responder status in patients with focal (partial-onset) seizures in three phase III studies of adjunctive brivaracetam treatment.
- Current: Yu2026|https://pubmed.ncbi.nlm.nih.gov/42092987/; Inoue2024|https://pubmed.ncbi.nlm.nih.gov/38576178/; Bast2022|https://pubmed.ncbi.nlm.nih.gov/35844134/; Kalviainen2015|https://pubmed.ncbi.nlm.nih.gov/26666500/; Klein2015|https://pubmed.ncbi.nlm.nih.gov/26471380/; Ryvlin2013|https://pubmed.ncbi.nlm.nih.gov/24256083/; Kwan2013|https://pubmed.ncbi.nlm.nih.gov/24116853/; Biton2013|https://pubmed.ncbi.nlm.nih.gov/24446953/; VanPaesschen2012|https://pubmed.ncbi.nlm.nih.gov/22813235/; French2010|https://pubmed.ncbi.nlm.nih.gov/20592253/
- Proposed: Klein2016|https://pubmed.ncbi.nlm.nih.gov/27988967/

### HIGH new_pubmed_phase_ii_iii_rct-bf86fd5eeede
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: brivaracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/27608437/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Efficacy, safety, and tolerability of adjunctive brivaracetam for secondarily generalized tonic-clonic seizures: Pooled results from three Phase III studies.
- Current: Yu2026|https://pubmed.ncbi.nlm.nih.gov/42092987/; Inoue2024|https://pubmed.ncbi.nlm.nih.gov/38576178/; Bast2022|https://pubmed.ncbi.nlm.nih.gov/35844134/; Kalviainen2015|https://pubmed.ncbi.nlm.nih.gov/26666500/; Klein2015|https://pubmed.ncbi.nlm.nih.gov/26471380/; Ryvlin2013|https://pubmed.ncbi.nlm.nih.gov/24256083/; Kwan2013|https://pubmed.ncbi.nlm.nih.gov/24116853/; Biton2013|https://pubmed.ncbi.nlm.nih.gov/24446953/; VanPaesschen2012|https://pubmed.ncbi.nlm.nih.gov/22813235/; French2010|https://pubmed.ncbi.nlm.nih.gov/20592253/
- Proposed: Moseley2016|https://pubmed.ncbi.nlm.nih.gov/27608437/

### HIGH rct_pubmed_concordance_problem-18fa79ea7aec
- Kind: rct_pubmed_concordance_problem
- Medication: brivaracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/26666500/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks seizure/epilepsy context.
- Current: Kalviainen2015|https://pubmed.ncbi.nlm.nih.gov/26666500/
- Proposed: update_check on 05-19-2026: PMID 26666500 needs manual review for brivaracetam; PubMed validation reason: title lacks seizure/epilepsy context.

### HIGH source_fact_concordance_problem-c2fb020359ab
- Kind: source_fact_concordance_problem
- Medication: brivaracetam
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2016
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-d91d47f056de
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: cannabidiol
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/33797076/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Time to onset of cannabidiol (CBD) treatment effect in Lennox-Gastaut syndrome: Analysis from two randomized controlled trials.
- Current: OBrien2022|https://pubmed.ncbi.nlm.nih.gov/35802375/; Thiele2021|https://pubmed.ncbi.nlm.nih.gov/33346789/; Miller2020|https://pubmed.ncbi.nlm.nih.gov/32119035/; Thiele2018|https://pubmed.ncbi.nlm.nih.gov/29395273/; Devinsky2018b|https://pubmed.ncbi.nlm.nih.gov/29768152/; Devinsky2018|https://pubmed.ncbi.nlm.nih.gov/29540584/; Devinsky2017|https://pubmed.ncbi.nlm.nih.gov/28538134/
- Proposed: Privitera2021|https://pubmed.ncbi.nlm.nih.gov/33797076/

### HIGH rct_pubmed_concordance_problem-54012593d620
- Kind: rct_pubmed_concordance_problem
- Medication: cannabidiol
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/32119035/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: drug appears in title but not as primary intervention.
- Current: Miller2020|https://pubmed.ncbi.nlm.nih.gov/32119035/
- Proposed: update_check on 05-19-2026: PMID 32119035 needs manual review for cannabidiol; PubMed validation reason: drug appears in title but not as primary intervention.

### HIGH source_fact_concordance_problem-a4fbeb9084a8
- Kind: source_fact_concordance_problem
- Medication: cannabidiol
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2018
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-303d9d3df1b8
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: carbamazepine
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/20955400/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Improvement in verbal memory after withdrawal of carbamazepine and valproate in patients with well-controlled epilepsy: a randomized, double-blind study.
- Current: Sobaniec2004|https://pubmed.ncbi.nlm.nih.gov/15156070/
- Proposed: Hessen2010|https://pubmed.ncbi.nlm.nih.gov/20955400/

### HIGH source_fact_concordance_problem-9539087d4802
- Kind: source_fact_concordance_problem
- Medication: carbamazepine
- Source: FDA/openFDA
- Column: half_life_range
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=5
- Summary: half_life_range could not be verified against the selected FDA/openFDA label.
- Current: 25-65 h initially; 12-17 h after autoinduction
- Proposed: update_check on 05-19-2026: half_life_range was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-3bca4dce071f
- Kind: source_fact_concordance_problem
- Medication: carbamazepine
- Source: FDA/openFDA
- Column: adverse_symptoms_percentages
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=5
- Summary: adverse_symptoms_percentages could not be verified against the selected FDA/openFDA label.
- Current: CNS: dizziness 44%, CNS: drowsiness 32%, GI: nausea 29%, GI: vomiting 18%, neurologic: ataxia 15%, dermatologic: rash 7%
- Proposed: update_check on 05-19-2026: adverse_symptoms_percentages was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-cc7fddc7000f
- Kind: source_fact_concordance_problem
- Medication: carbamazepine
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1968
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=5); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-a1968776c0bf
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: cenobamate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/41230998/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Early response rates with adjunctive cenobamate in uncontrolled focal seizures: Prospective analysis of a randomized, double-blind, placebo-controlled study in a multinational Asian population.
- Current: Lee2025|https://pubmed.ncbi.nlm.nih.gov/41144696/; Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32313503/; Chung2020|https://pubmed.ncbi.nlm.nih.gov/32409485/; Krauss2019|https://pubmed.ncbi.nlm.nih.gov/31734103/; KasteleijnNolstTrenite2019|https://pubmed.ncbi.nlm.nih.gov/31292226/
- Proposed: Kawai2025|https://pubmed.ncbi.nlm.nih.gov/41230998/

### HIGH new_pubmed_phase_ii_iii_rct-ed4728049b06
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: cenobamate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/41101116/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Efficacy of adjunctive cenobamate by focal seizure subtypes: a randomized, double-blind, placebo-controlled, multicenter study in a multinational Asian population.
- Current: Lee2025|https://pubmed.ncbi.nlm.nih.gov/41144696/; Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32313503/; Chung2020|https://pubmed.ncbi.nlm.nih.gov/32409485/; Krauss2019|https://pubmed.ncbi.nlm.nih.gov/31734103/; KasteleijnNolstTrenite2019|https://pubmed.ncbi.nlm.nih.gov/31292226/
- Proposed: Wu2025|https://pubmed.ncbi.nlm.nih.gov/41101116/

### HIGH rct_pubmed_concordance_problem-90a2a62ab0cd
- Kind: rct_pubmed_concordance_problem
- Medication: cenobamate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/31292226/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: KasteleijnNolstTrenite2019|https://pubmed.ncbi.nlm.nih.gov/31292226/
- Proposed: update_check on 05-19-2026: PMID 31292226 needs manual review for cenobamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH new_or_missing_approved_asm-6bd09ca4211e
- Kind: new_or_missing_approved_asm
- Medication: ciclopirox
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100
- Summary: Medication candidate 'ciclopirox' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'epilepsy'; effective_time=20230124
- Proposed: ciclopirox

### HIGH source_fact_concordance_problem-6a1132e86913
- Kind: source_fact_concordance_problem
- Medication: clobazam
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22de03bd69-2dca-459c-93b4-541fd3e9571c%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2011
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22de03bd69-2dca-459c-93b4-541fd3e9571c%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-df92260130b2
- Kind: source_fact_concordance_problem
- Medication: clonazepam
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1975
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-efaa2b79f8e9
- Kind: source_fact_concordance_problem
- Medication: clorazepate dipotassium
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.

### HIGH new_or_missing_approved_asm-c0b2237a85c4
- Kind: new_or_missing_approved_asm
- Medication: clozapine
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22seizure%22&limit=100
- Summary: Medication candidate 'clozapine' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'seizure'; effective_time=20260313
- Proposed: clozapine

### HIGH source_fact_concordance_problem-24270435ebe1
- Kind: source_fact_concordance_problem
- Medication: diazepam
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22diazepam%22+OR+openfda.brand_name%3A%22diazepam%22+OR+openfda.substance_name%3A%22diazepam%22&limit=10
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1963
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22diazepam%22+OR+openfda.brand_name%3A%22diazepam%22+OR+openfda.substance_name%3A%22diazepam%22&limit=10); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-4f97f15211c4
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/35908275/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Psychiatric adverse events in three phase III trials of eslicarbazepine acetate for focal seizures.
- Current: Koepp2026|https://pubmed.ncbi.nlm.nih.gov/41722592/; Kirkham2020|https://pubmed.ncbi.nlm.nih.gov/32151803/; Mintzer2018|https://pubmed.ncbi.nlm.nih.gov/29499473/; Sperling2014|https://pubmed.ncbi.nlm.nih.gov/25528898/; BenMenachem2010|https://pubmed.ncbi.nlm.nih.gov/20299189/; GilNagel2009|https://pubmed.ncbi.nlm.nih.gov/19832771/; Elger2009|https://pubmed.ncbi.nlm.nih.gov/19243424/; Elger2007|https://pubmed.ncbi.nlm.nih.gov/17319919/
- Proposed: Altalib2022|https://pubmed.ncbi.nlm.nih.gov/35908275/

### HIGH new_pubmed_phase_ii_iii_rct-7c89be073150
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/29454255/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Effects of adjunctive eslicarbazepine acetate on neurocognitive functioning in children with refractory focal-onset seizures.
- Current: Koepp2026|https://pubmed.ncbi.nlm.nih.gov/41722592/; Kirkham2020|https://pubmed.ncbi.nlm.nih.gov/32151803/; Mintzer2018|https://pubmed.ncbi.nlm.nih.gov/29499473/; Sperling2014|https://pubmed.ncbi.nlm.nih.gov/25528898/; BenMenachem2010|https://pubmed.ncbi.nlm.nih.gov/20299189/; GilNagel2009|https://pubmed.ncbi.nlm.nih.gov/19832771/; Elger2009|https://pubmed.ncbi.nlm.nih.gov/19243424/; Elger2007|https://pubmed.ncbi.nlm.nih.gov/17319919/
- Proposed: Jozwiak2018|https://pubmed.ncbi.nlm.nih.gov/29454255/

### HIGH new_pubmed_phase_ii_iii_rct-f74a46017ce4
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/29030894/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Pooled efficacy and safety of eslicarbazepine acetate as add-on treatment in patients with focal-onset seizures: Data from four double-blind placebo-controlled pivotal phase III clinical studies.
- Current: Koepp2026|https://pubmed.ncbi.nlm.nih.gov/41722592/; Kirkham2020|https://pubmed.ncbi.nlm.nih.gov/32151803/; Mintzer2018|https://pubmed.ncbi.nlm.nih.gov/29499473/; Sperling2014|https://pubmed.ncbi.nlm.nih.gov/25528898/; BenMenachem2010|https://pubmed.ncbi.nlm.nih.gov/20299189/; GilNagel2009|https://pubmed.ncbi.nlm.nih.gov/19832771/; Elger2009|https://pubmed.ncbi.nlm.nih.gov/19243424/; Elger2007|https://pubmed.ncbi.nlm.nih.gov/17319919/
- Proposed: Elger2017|https://pubmed.ncbi.nlm.nih.gov/29030894/

### HIGH new_pubmed_phase_ii_iii_rct-c63a58b1612c
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/26575256/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Severity and burden of partial-onset seizures in a phase III trial of eslicarbazepine acetate.
- Current: Koepp2026|https://pubmed.ncbi.nlm.nih.gov/41722592/; Kirkham2020|https://pubmed.ncbi.nlm.nih.gov/32151803/; Mintzer2018|https://pubmed.ncbi.nlm.nih.gov/29499473/; Sperling2014|https://pubmed.ncbi.nlm.nih.gov/25528898/; BenMenachem2010|https://pubmed.ncbi.nlm.nih.gov/20299189/; GilNagel2009|https://pubmed.ncbi.nlm.nih.gov/19832771/; Elger2009|https://pubmed.ncbi.nlm.nih.gov/19243424/; Elger2007|https://pubmed.ncbi.nlm.nih.gov/17319919/
- Proposed: Cramer2015|https://pubmed.ncbi.nlm.nih.gov/26575256/

### HIGH rct_pubmed_concordance_problem-95fd919173bf
- Kind: rct_pubmed_concordance_problem
- Medication: eslicarbazepine acetate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/20299189/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: BenMenachem2010|https://pubmed.ncbi.nlm.nih.gov/20299189/
- Proposed: update_check on 05-19-2026: PMID 20299189 needs manual review for eslicarbazepine acetate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-52ad12ce2069
- Kind: rct_pubmed_concordance_problem
- Medication: eslicarbazepine acetate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/19832771/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: GilNagel2009|https://pubmed.ncbi.nlm.nih.gov/19832771/
- Proposed: update_check on 05-19-2026: PMID 19832771 needs manual review for eslicarbazepine acetate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-9d346e73f21c
- Kind: source_fact_concordance_problem
- Medication: eslicarbazepine acetate
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2013
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-2cd845e7b7be
- Kind: source_fact_concordance_problem
- Medication: ethosuximide
- Source: FDA/openFDA
- Column: maximum_approved_daily_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5
- Summary: maximum_approved_daily_dose could not be verified against the selected FDA/openFDA label.
- Current: 1500 mg/day; FDA label states doses exceeding 1.5 g/day should be used only under strict physician supervision.
- Proposed: update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-f644fe6180da
- Kind: source_fact_concordance_problem
- Medication: ethosuximide
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-58501fe42c24
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: everolimus
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/31217257/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: A randomized controlled trial with everolimus for IQ and autism in tuberous sclerosis complex.
- Current: French2016|https://pubmed.ncbi.nlm.nih.gov/27613521/
- Proposed: Overwater2019|https://pubmed.ncbi.nlm.nih.gov/31217257/

### HIGH new_pubmed_phase_ii_iii_rct-6c55b29b1d6e
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: everolimus
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/28993887/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: The effect of everolimus on renal angiomyolipoma in pediatric patients with tuberous sclerosis being treated for subependymal giant cell astrocytoma.
- Current: French2016|https://pubmed.ncbi.nlm.nih.gov/27613521/
- Proposed: Bissler2017|https://pubmed.ncbi.nlm.nih.gov/28993887/

### HIGH new_pubmed_phase_ii_iii_rct-afc01cad1b79
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: everolimus
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/24522027/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Re: everolimus for angiomyolipoma associated with tuberous sclerosis complex or sporadic lymphangioleiomyomatosis (EXIST-2): a multicentre, randomised, double-blind, placebo-controlled trial.
- Current: French2016|https://pubmed.ncbi.nlm.nih.gov/27613521/
- Proposed: Laguna2013|https://pubmed.ncbi.nlm.nih.gov/24522027/

### HIGH new_pubmed_phase_ii_iii_rct-68c0c4daa520
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: everolimus
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/23642941/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Commentary on: everolimus for angiomyolipoma associated with tuberous sclerosis complex or sporadic lymphangioleiomyomatosis (EXIST-2): a multicentre, randomised, double-blind, placebo-controlled trial.
- Current: French2016|https://pubmed.ncbi.nlm.nih.gov/27613521/
- Proposed: Black2013|https://pubmed.ncbi.nlm.nih.gov/23642941/

### HIGH new_pubmed_phase_ii_iii_rct-fd8343ffa0c3
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: everolimus
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/23312829/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Everolimus for angiomyolipoma associated with tuberous sclerosis complex or sporadic lymphangioleiomyomatosis (EXIST-2): a multicentre, randomised, double-blind, placebo-controlled trial.
- Current: French2016|https://pubmed.ncbi.nlm.nih.gov/27613521/
- Proposed: Bissler2013|https://pubmed.ncbi.nlm.nih.gov/23312829/

### HIGH new_pubmed_phase_ii_iii_rct-12467f47e0ae
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: everolimus
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/23158522/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Efficacy and safety of everolimus for subependymal giant cell astrocytomas associated with tuberous sclerosis complex (EXIST-1): a multicentre, randomised, placebo-controlled phase 3 trial.
- Current: French2016|https://pubmed.ncbi.nlm.nih.gov/27613521/
- Proposed: Franz2012|https://pubmed.ncbi.nlm.nih.gov/23158522/

### HIGH source_fact_concordance_problem-373fde0ce3de
- Kind: source_fact_concordance_problem
- Medication: everolimus
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2018 for TSC-associated seizures; 2009 original oncology approval
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5); review current text before relying on it.

### HIGH rct_pubmed_concordance_problem-cd4231675472
- Kind: rct_pubmed_concordance_problem
- Medication: ezogabine
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/20944074/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Brodie2010|https://pubmed.ncbi.nlm.nih.gov/20944074/
- Proposed: update_check on 05-19-2026: PMID 20944074 needs manual review for ezogabine; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-55ba540ee506
- Kind: rct_pubmed_concordance_problem
- Medication: felbamate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/10210023/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Siegel1999|https://pubmed.ncbi.nlm.nih.gov/10210023/
- Proposed: update_check on 05-19-2026: PMID 10210023 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-88586dee4303
- Kind: rct_pubmed_concordance_problem
- Medication: felbamate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/7796796/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Devinsky1995|https://pubmed.ncbi.nlm.nih.gov/7796796/
- Proposed: update_check on 05-19-2026: PMID 7796796 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-a5aa5e426454
- Kind: rct_pubmed_concordance_problem
- Medication: felbamate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/8347179/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: FelbamateStudyGroupinLennoxGastautSyndrome1993|https://pubmed.ncbi.nlm.nih.gov/8347179/
- Proposed: update_check on 05-19-2026: PMID 8347179 needs manual review for felbamate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-84969f3cdb08
- Kind: source_fact_concordance_problem
- Medication: felbamate
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1993
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-5476663ac8d8
- Kind: source_fact_concordance_problem
- Medication: fenfluramine
- Source: FDA/openFDA
- Column: typical_doses_per_day
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5
- Summary: typical_doses_per_day could not be verified against the selected FDA/openFDA label.
- Current: Dravet/LGS: 0.2-0.7 mg/kg/day divided BID subject to syndrome/background therapy caps
- Proposed: update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-3e62db6e7a75
- Kind: source_fact_concordance_problem
- Medication: fenfluramine
- Source: FDA/openFDA
- Column: minimum_effective_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5
- Summary: minimum_effective_dose could not be verified against the selected FDA/openFDA label.
- Current: 0.2 mg/kg/day; titrate by syndrome and background therapy
- Proposed: update_check on 05-19-2026: minimum_effective_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-9595b473517f
- Kind: source_fact_concordance_problem
- Medication: fenfluramine
- Source: FDA/openFDA
- Column: maximum_approved_daily_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5
- Summary: maximum_approved_daily_dose could not be verified against the selected FDA/openFDA label.
- Current: 0.7 mg/kg/day; capped by product labeling and lower with stiripentol
- Proposed: update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-cb9b3ae4f657
- Kind: source_fact_concordance_problem
- Medication: fenfluramine
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2020 for Dravet; 2022 LGS; older anorectic approval withdrawn
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5); review current text before relying on it.

### HIGH new_or_missing_approved_asm-9afa902268b6
- Kind: new_or_missing_approved_asm
- Medication: flumazenil
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22status+epilepticus%22&limit=100
- Summary: Medication candidate 'flumazenil' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'status epilepticus'; effective_time=20251020
- Proposed: flumazenil

### HIGH source_fact_concordance_problem-bd14103daa6a
- Kind: source_fact_concordance_problem
- Medication: fosphenytoin
- Source: FDA/openFDA
- Column: half_life_range
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5
- Summary: half_life_range could not be verified against the selected FDA/openFDA label.
- Current: Conversion ~15 min; phenytoin ~7-42 h
- Proposed: update_check on 05-19-2026: half_life_range was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-51eff9b4fdd5
- Kind: source_fact_concordance_problem
- Medication: fosphenytoin
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1996
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5); review current text before relying on it.

### HIGH new_or_missing_approved_asm-8fa04132958f
- Kind: new_or_missing_approved_asm
- Medication: fosphenytoin sodium
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22status+epilepticus%22&limit=100
- Summary: Medication candidate 'fosphenytoin sodium' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'status epilepticus'; effective_time=20231017
- Proposed: fosphenytoin sodium

### HIGH rct_pubmed_concordance_problem-ebf7f5a01d35
- Kind: rct_pubmed_concordance_problem
- Medication: gabapentin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/1971862/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: PMID1990|https://pubmed.ncbi.nlm.nih.gov/1971862/
- Proposed: update_check on 05-19-2026: PMID 1971862 needs manual review for gabapentin; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-d6e04d0107ac
- Kind: source_fact_concordance_problem
- Medication: gabapentin
- Source: FDA/openFDA
- Column: typical_doses_per_day
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10
- Summary: typical_doses_per_day could not be verified against the selected FDA/openFDA label.
- Current: Adjunctive focal seizures: 900-1800 mg/day divided TID; up to 3600 mg/day used
- Proposed: update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.

### HIGH source_fact_concordance_problem-3b0f7959c8fc
- Kind: source_fact_concordance_problem
- Medication: gabapentin
- Source: FDA/openFDA
- Column: maximum_approved_daily_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10
- Summary: maximum_approved_daily_dose could not be verified against the selected FDA/openFDA label.
- Current: 1800 mg/day labeled for epilepsy; higher doses used in practice
- Proposed: update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.

### HIGH source_fact_concordance_problem-aa8792eb2f8d
- Kind: source_fact_concordance_problem
- Medication: gabapentin
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1993
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.

### HIGH rct_pubmed_concordance_problem-dc0596a5aaea
- Kind: rct_pubmed_concordance_problem
- Medication: ganaxolone
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/35429480/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks seizure/epilepsy context.
- Current: Knight2022|https://pubmed.ncbi.nlm.nih.gov/35429480/
- Proposed: update_check on 05-19-2026: PMID 35429480 needs manual review for ganaxolone; PubMed validation reason: title lacks seizure/epilepsy context.

### HIGH source_fact_concordance_problem-19b1d8a7be2f
- Kind: source_fact_concordance_problem
- Medication: ganaxolone
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d91612c4-b03a-4be4-a1ee-6a13e3b83d4e%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2022
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d91612c4-b03a-4be4-a1ee-6a13e3b83d4e%22&limit=5); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-bf8800252922
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: lacosamide
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/26414341/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Safety and tolerability of lacosamide as adjunctive therapy for adults with partial-onset seizures: Analysis of data pooled from three randomized, double-blind, placebo-controlled clinical trials.
- Current: Makedonska2024|https://pubmed.ncbi.nlm.nih.gov/38375995/; Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32817358/; Farkas2019|https://pubmed.ncbi.nlm.nih.gov/31462582/; FoldvarySchaefer2017|https://pubmed.ncbi.nlm.nih.gov/28866338/; Hong2016|https://pubmed.ncbi.nlm.nih.gov/27669155/; Rudd2015|https://pubmed.ncbi.nlm.nih.gov/25933358/; Chung2010|https://pubmed.ncbi.nlm.nih.gov/20132285/; Halasz2009|https://pubmed.ncbi.nlm.nih.gov/19183227/; BenMenachem2007|https://pubmed.ncbi.nlm.nih.gov/17635557/
- Proposed: Biton2015|https://pubmed.ncbi.nlm.nih.gov/26414341/

### HIGH rct_pubmed_concordance_problem-4aece0205e3a
- Kind: rct_pubmed_concordance_problem
- Medication: lacosamide
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/38375995/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Makedonska2024|https://pubmed.ncbi.nlm.nih.gov/38375995/
- Proposed: update_check on 05-19-2026: PMID 38375995 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-fb99b1963c7c
- Kind: rct_pubmed_concordance_problem
- Medication: lacosamide
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/31462582/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Farkas2019|https://pubmed.ncbi.nlm.nih.gov/31462582/
- Proposed: update_check on 05-19-2026: PMID 31462582 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-0a4a476b1dd1
- Kind: rct_pubmed_concordance_problem
- Medication: lacosamide
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/17635557/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: BenMenachem2007|https://pubmed.ncbi.nlm.nih.gov/17635557/
- Proposed: update_check on 05-19-2026: PMID 17635557 needs manual review for lacosamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-ac3493599a74
- Kind: source_fact_concordance_problem
- Medication: lacosamide
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2008
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10); review current text before relying on it.

### HIGH rct_pubmed_concordance_problem-12495c5ed0ce
- Kind: rct_pubmed_concordance_problem
- Medication: lamotrigine
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/17938371/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Naritoku2007|https://pubmed.ncbi.nlm.nih.gov/17938371/
- Proposed: update_check on 05-19-2026: PMID 17938371 needs manual review for lamotrigine; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-b26b4cbd59ef
- Kind: rct_pubmed_concordance_problem
- Medication: lamotrigine
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/16847080/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Trevathan2006|https://pubmed.ncbi.nlm.nih.gov/16847080/
- Proposed: update_check on 05-19-2026: PMID 16847080 needs manual review for lamotrigine; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-be28eb52fc2b
- Kind: rct_pubmed_concordance_problem
- Medication: lamotrigine
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/10403222/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Frank1999|https://pubmed.ncbi.nlm.nih.gov/10403222/
- Proposed: update_check on 05-19-2026: PMID 10403222 needs manual review for lamotrigine; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-fc47d066ac4f
- Kind: rct_pubmed_concordance_problem
- Medication: lamotrigine
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/9400037/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Motte1997|https://pubmed.ncbi.nlm.nih.gov/9400037/
- Proposed: update_check on 05-19-2026: PMID 9400037 needs manual review for lamotrigine; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-e9ae0e750088
- Kind: source_fact_concordance_problem
- Medication: lamotrigine
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d7e3572d-56fe-4727-2bb4-013ccca22678%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1994
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d7e3572d-56fe-4727-2bb4-013ccca22678%22&limit=5); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-8b7ad605cd48
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/41175011/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: A randomized, double-blind, placebo-controlled, time-to-event study of the efficacy and safety of JNJ-40411813 in combination with levetiracetam or brivaracetam in patients with focal onset seizures.
- Current: PeterDerex2022|https://pubmed.ncbi.nlm.nih.gov/35963261/; Wu2018|https://pubmed.ncbi.nlm.nih.gov/30525116/; Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Larsson2012|https://pubmed.ncbi.nlm.nih.gov/22494796/; Fattore2011|https://pubmed.ncbi.nlm.nih.gov/21320119/; Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/; PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/; Peltola2009|https://pubmed.ncbi.nlm.nih.gov/19317886/; Wu2008|https://pubmed.ncbi.nlm.nih.gov/18657175/; Berkovic2007|https://pubmed.ncbi.nlm.nih.gov/17625106/; Tsai2006|https://pubmed.ncbi.nlm.nih.gov/16417534/; Glauser2006|https://pubmed.ncbi.nlm.nih.gov/16641323/; Boon2002|https://pubmed.ncbi.nlm.nih.gov/118231...
- Proposed: French2025|https://pubmed.ncbi.nlm.nih.gov/41175011/

### HIGH new_pubmed_phase_ii_iii_rct-16b3cb361b31
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/39949405/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: High-frequency oscillations in epileptic and non-epileptic Alzheimer's disease patients and the differential effect of levetiracetam on the oscillations.
- Current: PeterDerex2022|https://pubmed.ncbi.nlm.nih.gov/35963261/; Wu2018|https://pubmed.ncbi.nlm.nih.gov/30525116/; Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Larsson2012|https://pubmed.ncbi.nlm.nih.gov/22494796/; Fattore2011|https://pubmed.ncbi.nlm.nih.gov/21320119/; Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/; PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/; Peltola2009|https://pubmed.ncbi.nlm.nih.gov/19317886/; Wu2008|https://pubmed.ncbi.nlm.nih.gov/18657175/; Berkovic2007|https://pubmed.ncbi.nlm.nih.gov/17625106/; Tsai2006|https://pubmed.ncbi.nlm.nih.gov/16417534/; Glauser2006|https://pubmed.ncbi.nlm.nih.gov/16641323/; Boon2002|https://pubmed.ncbi.nlm.nih.gov/118231...
- Proposed: Shandilya2025|https://pubmed.ncbi.nlm.nih.gov/39949405/

### HIGH new_pubmed_phase_ii_iii_rct-fdad5246446e
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/20547106/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Assessment of behavioral and emotional functioning using standardized instruments in children and adolescents with partial-onset seizures treated with adjunctive levetiracetam in a randomized, placebo-controlled trial.
- Current: PeterDerex2022|https://pubmed.ncbi.nlm.nih.gov/35963261/; Wu2018|https://pubmed.ncbi.nlm.nih.gov/30525116/; Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Larsson2012|https://pubmed.ncbi.nlm.nih.gov/22494796/; Fattore2011|https://pubmed.ncbi.nlm.nih.gov/21320119/; Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/; PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/; Peltola2009|https://pubmed.ncbi.nlm.nih.gov/19317886/; Wu2008|https://pubmed.ncbi.nlm.nih.gov/18657175/; Berkovic2007|https://pubmed.ncbi.nlm.nih.gov/17625106/; Tsai2006|https://pubmed.ncbi.nlm.nih.gov/16417534/; Glauser2006|https://pubmed.ncbi.nlm.nih.gov/16641323/; Boon2002|https://pubmed.ncbi.nlm.nih.gov/118231...
- Proposed: delaLoge2010|https://pubmed.ncbi.nlm.nih.gov/20547106/

### HIGH new_pubmed_phase_ii_iii_rct-651ffcb4747d
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/19702752/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Neurocognitive effects of adjunctive levetiracetam in children with partial-onset seizures: a randomized, double-blind, placebo-controlled, noninferiority trial.
- Current: PeterDerex2022|https://pubmed.ncbi.nlm.nih.gov/35963261/; Wu2018|https://pubmed.ncbi.nlm.nih.gov/30525116/; Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Larsson2012|https://pubmed.ncbi.nlm.nih.gov/22494796/; Fattore2011|https://pubmed.ncbi.nlm.nih.gov/21320119/; Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/; PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/; Peltola2009|https://pubmed.ncbi.nlm.nih.gov/19317886/; Wu2008|https://pubmed.ncbi.nlm.nih.gov/18657175/; Berkovic2007|https://pubmed.ncbi.nlm.nih.gov/17625106/; Tsai2006|https://pubmed.ncbi.nlm.nih.gov/16417534/; Glauser2006|https://pubmed.ncbi.nlm.nih.gov/16641323/; Boon2002|https://pubmed.ncbi.nlm.nih.gov/118231...
- Proposed: Levisohn2009|https://pubmed.ncbi.nlm.nih.gov/19702752/

### HIGH new_pubmed_phase_ii_iii_rct-10982ca5dd1f
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/19327967/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Levetiracetam as add-on therapy for idiopathic generalized epilepsy syndromes with onset during adolescence: analysis of two randomized, double-blind, placebo-controlled studies.
- Current: PeterDerex2022|https://pubmed.ncbi.nlm.nih.gov/35963261/; Wu2018|https://pubmed.ncbi.nlm.nih.gov/30525116/; Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Larsson2012|https://pubmed.ncbi.nlm.nih.gov/22494796/; Fattore2011|https://pubmed.ncbi.nlm.nih.gov/21320119/; Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/; PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/; Peltola2009|https://pubmed.ncbi.nlm.nih.gov/19317886/; Wu2008|https://pubmed.ncbi.nlm.nih.gov/18657175/; Berkovic2007|https://pubmed.ncbi.nlm.nih.gov/17625106/; Tsai2006|https://pubmed.ncbi.nlm.nih.gov/16417534/; Glauser2006|https://pubmed.ncbi.nlm.nih.gov/16641323/; Boon2002|https://pubmed.ncbi.nlm.nih.gov/118231...
- Proposed: Rosenfeld2009|https://pubmed.ncbi.nlm.nih.gov/19327967/

### HIGH new_pubmed_phase_ii_iii_rct-5f6244068644
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/18024209/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Effects of levetiracetam as an add-on therapy on cognitive function and quality of life in patients with refractory partial seizures.
- Current: PeterDerex2022|https://pubmed.ncbi.nlm.nih.gov/35963261/; Wu2018|https://pubmed.ncbi.nlm.nih.gov/30525116/; Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Larsson2012|https://pubmed.ncbi.nlm.nih.gov/22494796/; Fattore2011|https://pubmed.ncbi.nlm.nih.gov/21320119/; Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/; PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/; Peltola2009|https://pubmed.ncbi.nlm.nih.gov/19317886/; Wu2008|https://pubmed.ncbi.nlm.nih.gov/18657175/; Berkovic2007|https://pubmed.ncbi.nlm.nih.gov/17625106/; Tsai2006|https://pubmed.ncbi.nlm.nih.gov/16417534/; Glauser2006|https://pubmed.ncbi.nlm.nih.gov/16641323/; Boon2002|https://pubmed.ncbi.nlm.nih.gov/118231...
- Proposed: Zhou2007|https://pubmed.ncbi.nlm.nih.gov/18024209/

### HIGH new_pubmed_phase_ii_iii_rct-5b3658191b8d
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/16529615/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Onset of action of levetiracetam: a RCT trial using therapeutic intensive seizure analysis (TISA).
- Current: PeterDerex2022|https://pubmed.ncbi.nlm.nih.gov/35963261/; Wu2018|https://pubmed.ncbi.nlm.nih.gov/30525116/; Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Larsson2012|https://pubmed.ncbi.nlm.nih.gov/22494796/; Fattore2011|https://pubmed.ncbi.nlm.nih.gov/21320119/; Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/; PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/; Peltola2009|https://pubmed.ncbi.nlm.nih.gov/19317886/; Wu2008|https://pubmed.ncbi.nlm.nih.gov/18657175/; Berkovic2007|https://pubmed.ncbi.nlm.nih.gov/17625106/; Tsai2006|https://pubmed.ncbi.nlm.nih.gov/16417534/; Glauser2006|https://pubmed.ncbi.nlm.nih.gov/16641323/; Boon2002|https://pubmed.ncbi.nlm.nih.gov/118231...
- Proposed: Stefan2006|https://pubmed.ncbi.nlm.nih.gov/16529615/

### HIGH new_pubmed_phase_ii_iii_rct-9fb1d178b578
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/10897159/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Effect of levetiracetam on epilepsy-related quality of life. N132 Study Group.
- Current: PeterDerex2022|https://pubmed.ncbi.nlm.nih.gov/35963261/; Wu2018|https://pubmed.ncbi.nlm.nih.gov/30525116/; Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Larsson2012|https://pubmed.ncbi.nlm.nih.gov/22494796/; Fattore2011|https://pubmed.ncbi.nlm.nih.gov/21320119/; Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/; PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/; Peltola2009|https://pubmed.ncbi.nlm.nih.gov/19317886/; Wu2008|https://pubmed.ncbi.nlm.nih.gov/18657175/; Berkovic2007|https://pubmed.ncbi.nlm.nih.gov/17625106/; Tsai2006|https://pubmed.ncbi.nlm.nih.gov/16417534/; Glauser2006|https://pubmed.ncbi.nlm.nih.gov/16641323/; Boon2002|https://pubmed.ncbi.nlm.nih.gov/118231...
- Proposed: Cramer2000|https://pubmed.ncbi.nlm.nih.gov/10897159/

### HIGH rct_pubmed_concordance_problem-78f82595a4c1
- Kind: rct_pubmed_concordance_problem
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/19176965/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Xiao2009|https://pubmed.ncbi.nlm.nih.gov/19176965/
- Proposed: update_check on 05-19-2026: PMID 19176965 needs manual review for levetiracetam; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-066083ab43dd
- Kind: rct_pubmed_concordance_problem
- Medication: levetiracetam
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/19243423/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: PinaGarza2009|https://pubmed.ncbi.nlm.nih.gov/19243423/
- Proposed: update_check on 05-19-2026: PMID 19243423 needs manual review for levetiracetam; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-ae66a96aad8e
- Kind: source_fact_concordance_problem
- Medication: levetiracetam
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1999
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5); review current text before relying on it.

### HIGH new_or_missing_approved_asm-a88f18de4d91
- Kind: new_or_missing_approved_asm
- Medication: levetiracetam oral
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22partial-onset+seizures%22&limit=100
- Summary: Medication candidate 'levetiracetam oral' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'partial-onset seizures'; effective_time=20240803
- Proposed: levetiracetam oral

### HIGH source_fact_concordance_problem-5236cad63e5b
- Kind: source_fact_concordance_problem
- Medication: lorazepam
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Ativan%22+OR+openfda.brand_name%3A%22Ativan%22+OR+openfda.substance_name%3A%22Ativan%22&limit=10
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1977
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Ativan%22+OR+openfda.brand_name%3A%22Ativan%22+OR+openfda.substance_name%3A%22Ativan%22&limit=10); review current text before relying on it.

### HIGH new_or_missing_approved_asm-e736462ff1bf
- Kind: new_or_missing_approved_asm
- Medication: methadone
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22seizure%22&limit=100
- Summary: Medication candidate 'methadone' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'seizure'; effective_time=20251231
- Proposed: methadone

### HIGH source_fact_concordance_problem-d0f6e190903a
- Kind: source_fact_concordance_problem
- Medication: methsuximide
- Source: FDA/openFDA
- Column: typical_doses_per_day
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Summary: typical_doses_per_day could not be verified against the selected FDA/openFDA label.
- Current: Suggested schedule: 300 mg/day for first week, then increase by 300 mg/day weekly if needed to 1200 mg/day per FDA label.
- Proposed: update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-089c934e9142
- Kind: source_fact_concordance_problem
- Medication: methsuximide
- Source: FDA/openFDA
- Column: maximum_approved_daily_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Summary: maximum_approved_daily_dose could not be verified against the selected FDA/openFDA label.
- Current: 1200 mg/day in selected FDA label dosage schedule.
- Proposed: update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-3a95fcba4ff8
- Kind: source_fact_concordance_problem
- Medication: methsuximide
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-a83ae075db9a
- Kind: source_fact_concordance_problem
- Medication: midazolam
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1985 injection; 2019 nasal seizure-cluster product
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-0ecabda8188f
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: perampanel
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/26724782/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Cognitive effects of adjunctive perampanel for partial-onset seizures: A randomized trial.
- Current: Vossler2024|https://pubmed.ncbi.nlm.nih.gov/39576191/; Nishida2017|https://pubmed.ncbi.nlm.nih.gov/29250772/; Lagae2016|https://pubmed.ncbi.nlm.nih.gov/27221398/; French2015|https://pubmed.ncbi.nlm.nih.gov/26296511/; Belousova2014|https://pubmed.ncbi.nlm.nih.gov/25345628/; Krauss2012|https://pubmed.ncbi.nlm.nih.gov/22517103/; French2012b|https://pubmed.ncbi.nlm.nih.gov/22905857/; French2012|https://pubmed.ncbi.nlm.nih.gov/22843280/
- Proposed: Meador2016|https://pubmed.ncbi.nlm.nih.gov/26724782/

### HIGH new_pubmed_phase_ii_iii_rct-1584ae761e3f
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: perampanel
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/26088895/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Lack of effect of perampanel on QT interval duration: Results from a thorough QT analysis and pooled partial seizure Phase III clinical trials.
- Current: Vossler2024|https://pubmed.ncbi.nlm.nih.gov/39576191/; Nishida2017|https://pubmed.ncbi.nlm.nih.gov/29250772/; Lagae2016|https://pubmed.ncbi.nlm.nih.gov/27221398/; French2015|https://pubmed.ncbi.nlm.nih.gov/26296511/; Belousova2014|https://pubmed.ncbi.nlm.nih.gov/25345628/; Krauss2012|https://pubmed.ncbi.nlm.nih.gov/22517103/; French2012b|https://pubmed.ncbi.nlm.nih.gov/22905857/; French2012|https://pubmed.ncbi.nlm.nih.gov/22843280/
- Proposed: Yang2015|https://pubmed.ncbi.nlm.nih.gov/26088895/

### HIGH source_fact_concordance_problem-c16d79125017
- Kind: source_fact_concordance_problem
- Medication: perampanel
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22perampanel%22+OR+openfda.brand_name%3A%22perampanel%22+OR+openfda.substance_name%3A%22perampanel%22&limit=10
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2012
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22perampanel%22+OR+openfda.brand_name%3A%22perampanel%22+OR+openfda.substance_name%3A%22perampanel%22&limit=10); review current text before relying on it.

### HIGH source_fact_concordance_problem-431e2c430787
- Kind: source_fact_concordance_problem
- Medication: phenobarbital
- Source: FDA/openFDA
- Column: half_life_range
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5
- Summary: half_life_range could not be verified against the selected FDA/openFDA label.
- Current: 53-118 h
- Proposed: update_check on 05-19-2026: half_life_range was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-c75a6b5d6c3b
- Kind: source_fact_concordance_problem
- Medication: phenobarbital
- Source: FDA/openFDA
- Column: typical_doses_per_day
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5
- Summary: typical_doses_per_day could not be verified against the selected FDA/openFDA label.
- Current: Adults often 60-200 mg/day once daily or divided; pediatric weight-based
- Proposed: update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-718752a7f920
- Kind: source_fact_concordance_problem
- Medication: phenobarbital
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1912 legacy; predates modern FDA approval system
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.

### HIGH new_or_missing_approved_asm-45ca6bce587b
- Kind: new_or_missing_approved_asm
- Medication: phenobarbital sodium
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22status+epilepticus%22&limit=100
- Summary: Medication candidate 'phenobarbital sodium' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'status epilepticus'; effective_time=20251105
- Proposed: phenobarbital sodium

### HIGH new_pubmed_phase_ii_iii_rct-62aa3a8f4e16
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: phenytoin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/8148215/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: A double-blind, placebo-controlled interaction study between oxcarbazepine and carbamazepine, sodium valproate and phenytoin in epileptic patients.
- Current: Young2004|https://pubmed.ncbi.nlm.nih.gov/15039684/; DeSantis2002|https://pubmed.ncbi.nlm.nih.gov/11903465/; Dikmen1991|https://pubmed.ncbi.nlm.nih.gov/1995974/; Temkin1990|https://pubmed.ncbi.nlm.nih.gov/2115976/; Bacon1981|https://pubmed.ncbi.nlm.nih.gov/6116084/; North1980|https://pubmed.ncbi.nlm.nih.gov/6101843/
- Proposed: McKee1994|https://pubmed.ncbi.nlm.nih.gov/8148215/

### HIGH new_pubmed_phase_ii_iii_rct-27e4f41b19a7
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: phenytoin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/1828561/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: The administration of folic acid to institutionalized epileptic adults with phenytoin-induced gingival hyperplasia. A double-blind, randomized, placebo-controlled, parallel study.
- Current: Young2004|https://pubmed.ncbi.nlm.nih.gov/15039684/; DeSantis2002|https://pubmed.ncbi.nlm.nih.gov/11903465/; Dikmen1991|https://pubmed.ncbi.nlm.nih.gov/1995974/; Temkin1990|https://pubmed.ncbi.nlm.nih.gov/2115976/; Bacon1981|https://pubmed.ncbi.nlm.nih.gov/6116084/; North1980|https://pubmed.ncbi.nlm.nih.gov/6101843/
- Proposed: Brown1991|https://pubmed.ncbi.nlm.nih.gov/1828561/

### HIGH source_fact_concordance_problem-388c2732febe
- Kind: source_fact_concordance_problem
- Medication: phenytoin
- Source: FDA/openFDA
- Column: half_life_range
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Summary: half_life_range could not be verified against the selected FDA/openFDA label.
- Current: 7-42 h; concentration-dependent/nonlinear
- Proposed: update_check on 05-19-2026: half_life_range was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-22292dd7cbcf
- Kind: source_fact_concordance_problem
- Medication: phenytoin
- Source: FDA/openFDA
- Column: typical_doses_per_day
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Summary: typical_doses_per_day could not be verified against the selected FDA/openFDA label.
- Current: Adults maintenance commonly 300-400 mg/day; individualized by levels
- Proposed: update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-204dd8553ed7
- Kind: source_fact_concordance_problem
- Medication: phenytoin
- Source: FDA/openFDA
- Column: minimum_effective_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Summary: minimum_effective_dose could not be verified against the selected FDA/openFDA label.
- Current: 300 mg/day common adult maintenance starting regimen; individualized by levels
- Proposed: update_check on 05-19-2026: minimum_effective_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-61a1bffac48a
- Kind: source_fact_concordance_problem
- Medication: phenytoin
- Source: FDA/openFDA
- Column: maximum_approved_daily_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Summary: maximum_approved_daily_dose could not be verified against the selected FDA/openFDA label.
- Current: Dose individualized by serum level; commonly up to 400-600 mg/day
- Proposed: update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-af4524cc922b
- Kind: source_fact_concordance_problem
- Medication: phenytoin
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1938 legacy approval
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5); review current text before relying on it.

### HIGH new_or_missing_approved_asm-5f652acc7fe2
- Kind: new_or_missing_approved_asm
- Medication: phenytoin sodium
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22status+epilepticus%22&limit=100
- Summary: Medication candidate 'phenytoin sodium' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'status epilepticus'; effective_time=20240409
- Proposed: phenytoin sodium

### HIGH rct_pubmed_concordance_problem-a55a14877293
- Kind: rct_pubmed_concordance_problem
- Medication: pregabalin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/20696552/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Baulac2010|https://pubmed.ncbi.nlm.nih.gov/20696552/
- Proposed: update_check on 05-19-2026: PMID 20696552 needs manual review for pregabalin; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-d00bf38cfd49
- Kind: rct_pubmed_concordance_problem
- Medication: pregabalin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/15699378/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: drug appears in title but not as primary intervention.
- Current: Beydoun2005|https://pubmed.ncbi.nlm.nih.gov/15699378/
- Proposed: update_check on 05-19-2026: PMID 15699378 needs manual review for pregabalin; PubMed validation reason: drug appears in title but not as primary intervention.

### HIGH source_fact_concordance_problem-17122bd43f54
- Kind: source_fact_concordance_problem
- Medication: pregabalin
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2005
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-ea01525ecaed
- Kind: source_fact_concordance_problem
- Medication: primidone
- Source: FDA/openFDA
- Column: typical_doses_per_day
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5
- Summary: typical_doses_per_day could not be verified against the selected FDA/openFDA label.
- Current: Patients 8 years and older: titrate over 10 days to 250 mg three times daily; usual maintenance 750-1000 mg/day divided; FDA label allows increase if required.
- Proposed: update_check on 05-19-2026: typical_doses_per_day was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-6ed5ec099dd1
- Kind: source_fact_concordance_problem
- Medication: primidone
- Source: FDA/openFDA
- Column: minimum_effective_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5
- Summary: minimum_effective_dose could not be verified against the selected FDA/openFDA label.
- Current: 750 mg/day labeled day-10 maintenance target for patients 8 years and older; clinical effective serum level 5-12 mcg/mL.
- Proposed: update_check on 05-19-2026: minimum_effective_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-d8b483c4a197
- Kind: source_fact_concordance_problem
- Medication: primidone
- Source: FDA/openFDA
- Column: maximum_approved_daily_dose
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5
- Summary: maximum_approved_daily_dose could not be verified against the selected FDA/openFDA label.
- Current: 2000 mg/day; FDA label states daily doses should not exceed 500 mg four times daily.
- Proposed: update_check on 05-19-2026: maximum_approved_daily_dose was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-c56b1526a9d2
- Kind: source_fact_concordance_problem
- Medication: primidone
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5); review current text before relying on it.

### HIGH rct_pubmed_concordance_problem-57727f0c08eb
- Kind: rct_pubmed_concordance_problem
- Medication: rufinamide
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/18401024/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Glauser2008|https://pubmed.ncbi.nlm.nih.gov/18401024/
- Proposed: update_check on 05-19-2026: PMID 18401024 needs manual review for rufinamide; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-c5453decaae6
- Kind: source_fact_concordance_problem
- Medication: stiripentol
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2018
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5); review current text before relying on it.

### HIGH rct_pubmed_concordance_problem-706bbf690711
- Kind: rct_pubmed_concordance_problem
- Medication: sultiame
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/14738417/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks seizure/epilepsy context.
- Current: Debus2004|https://pubmed.ncbi.nlm.nih.gov/14738417/
- Proposed: update_check on 05-19-2026: PMID 14738417 needs manual review for sultiame; PubMed validation reason: title lacks seizure/epilepsy context.

### HIGH new_pubmed_phase_ii_iii_rct-314ebce77085
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: tiagabine
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/9109894/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Cognitive and quality of life effects of differing dosages of tiagabine in epilepsy.
- Current: Uthman1998|https://pubmed.ncbi.nlm.nih.gov/9443711/; Kalviainen1998|https://pubmed.ncbi.nlm.nih.gov/9551842/; Sachdeo1997|https://pubmed.ncbi.nlm.nih.gov/9152116/; Richens1995|https://pubmed.ncbi.nlm.nih.gov/7641674/; Sveinbjornsdottir1994|https://pubmed.ncbi.nlm.nih.gov/8044451/
- Proposed: Dodrill1997|https://pubmed.ncbi.nlm.nih.gov/9109894/

### HIGH rct_pubmed_concordance_problem-81db4d92fa56
- Kind: rct_pubmed_concordance_problem
- Medication: tiagabine
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/9152116/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Sachdeo1997|https://pubmed.ncbi.nlm.nih.gov/9152116/
- Proposed: update_check on 05-19-2026: PMID 9152116 needs manual review for tiagabine; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-2d0f9e238a79
- Kind: source_fact_concordance_problem
- Medication: tiagabine
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22tiagabine%22+OR+openfda.brand_name%3A%22tiagabine%22+OR+openfda.substance_name%3A%22tiagabine%22&limit=10
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1997
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22tiagabine%22+OR+openfda.brand_name%3A%22tiagabine%22+OR+openfda.substance_name%3A%22tiagabine%22&limit=10); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-8b994db9a357
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: topiramate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/16140593/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: A randomized, double-blind, placebo-controlled trial of topiramate in adults with epilepsy and intellectual disability: impact on seizures, severity, and quality of life.
- Current: Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/; Novotny2010|https://pubmed.ncbi.nlm.nih.gov/20089937/; Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/; Yen2000|https://pubmed.ncbi.nlm.nih.gov/10999555/; Sachdeo1999|https://pubmed.ncbi.nlm.nih.gov/10371538/; PMID1999|https://pubmed.ncbi.nlm.nih.gov/10612342/; Elterman1999|https://pubmed.ncbi.nlm.nih.gov/10227615/; Biton1999|https://pubmed.ncbi.nlm.nih.gov/10227614/; Faught1997|https://pubmed.ncbi.nlm.nih.gov/9092954/; Tassinari1996|https://pubmed.ncbi.nlm.nih.gov/8764816/; Sharief1996|https://pubmed.ncbi.nlm.nih.gov/8956919/; Privitera1996|https://pubmed.ncbi.nlm.nih.gov/8649569/; Faught1996|https://pubmed.ncbi.nlm.nih.gov/8649...
- Proposed: Kerr2005|https://pubmed.ncbi.nlm.nih.gov/16140593/

### HIGH rct_pubmed_concordance_problem-0925c26b8df4
- Kind: rct_pubmed_concordance_problem
- Medication: topiramate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/21672344/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/
- Proposed: update_check on 05-19-2026: PMID 21672344 needs manual review for topiramate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH rct_pubmed_concordance_problem-10b1ff149415
- Kind: rct_pubmed_concordance_problem
- Medication: topiramate
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/12225311/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/
- Proposed: update_check on 05-19-2026: PMID 12225311 needs manual review for topiramate; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-6cf8c0860d39
- Kind: source_fact_concordance_problem
- Medication: topiramate
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1996
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5); review current text before relying on it.

### HIGH new_or_missing_approved_asm-746f68877bf7
- Kind: new_or_missing_approved_asm
- Medication: topiramate spinkle
- Source: FDA/openFDA
- Column: generic_name
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22lennox-gastaut%22&limit=100
- Summary: Medication candidate 'topiramate spinkle' was found in external source(s) but not in ASM-list.csv. FDA/openFDA confirmation supports adding a skeletal row. Evidence: openFDA label indication text matched 'lennox-gastaut'; effective_time=20251225
- Proposed: topiramate spinkle

### HIGH new_pubmed_phase_ii_iii_rct-f11ebaad61b5
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: valproic acid
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/3130256/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Effects of sodium valproate on haem biosynthesis in man: implications for seizure management in the porphyric patient.
- Current: Willmore1996|https://pubmed.ncbi.nlm.nih.gov/8559420/; Richens1975|https://pubmed.ncbi.nlm.nih.gov/1104059/; Sharshar2023|https://pubmed.ncbi.nlm.nih.gov/36624526/
- Proposed: McGuire1988|https://pubmed.ncbi.nlm.nih.gov/3130256/

### HIGH rct_pubmed_concordance_problem-7fafbc2f590d
- Kind: rct_pubmed_concordance_problem
- Medication: valproic acid
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/8559420/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Willmore1996|https://pubmed.ncbi.nlm.nih.gov/8559420/
- Proposed: update_check on 05-19-2026: PMID 8559420 needs manual review for valproic acid; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-7621437404b9
- Kind: source_fact_concordance_problem
- Medication: valproic acid
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 1978 valproic acid; 1983 divalproex sodium; Dec 30, 1996 valproate sodium injection
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5); review current text before relying on it.

### HIGH new_pubmed_phase_ii_iii_rct-47c09f4139bd
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: vigabatrin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/41864166/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Comment on "Safety and efficacy of vigabatrin add on compared to placebo in Lennox-Gastaut syndrome (LennoVig): A single center randomized double-blind placebo-controlled trial".
- Current: Kalita2025|https://pubmed.ncbi.nlm.nih.gov/41500178/; Bebin2023|https://pubmed.ncbi.nlm.nih.gov/37638552/; Bruni2000|https://pubmed.ncbi.nlm.nih.gov/10777431/; Dean1999|https://pubmed.ncbi.nlm.nih.gov/9924905/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10565592/; Beran1996|https://pubmed.ncbi.nlm.nih.gov/8952010/; Jackson1994|https://pubmed.ncbi.nlm.nih.gov/7957035/; Grunewald1994|https://pubmed.ncbi.nlm.nih.gov/8089668/; Gillham1993|https://pubmed.ncbi.nlm.nih.gov/8270925/; PMID1992|https://pubmed.ncbi.nlm.nih.gov/1483856/; Cosi1989|https://pubmed.ncbi.nlm.nih.gov/2757911/; Cosi1988|https://pubmed.ncbi.nlm.nih.gov/3130253/; Tassinari1987|https://pubmed.ncbi.nlm.nih.gov/2887152/; Tarta...
- Proposed: Mantry2026|https://pubmed.ncbi.nlm.nih.gov/41864166/

### HIGH new_pubmed_phase_ii_iii_rct-fe1cea84b7d2
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: vigabatrin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/41735087/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Comment on "Safety and efficacy of vigabatrin add on compared to placebo in Lennox-Gastaut syndrome (LennoVig): A single center randomized double-blind placebo-controlled trial".
- Current: Kalita2025|https://pubmed.ncbi.nlm.nih.gov/41500178/; Bebin2023|https://pubmed.ncbi.nlm.nih.gov/37638552/; Bruni2000|https://pubmed.ncbi.nlm.nih.gov/10777431/; Dean1999|https://pubmed.ncbi.nlm.nih.gov/9924905/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10565592/; Beran1996|https://pubmed.ncbi.nlm.nih.gov/8952010/; Jackson1994|https://pubmed.ncbi.nlm.nih.gov/7957035/; Grunewald1994|https://pubmed.ncbi.nlm.nih.gov/8089668/; Gillham1993|https://pubmed.ncbi.nlm.nih.gov/8270925/; PMID1992|https://pubmed.ncbi.nlm.nih.gov/1483856/; Cosi1989|https://pubmed.ncbi.nlm.nih.gov/2757911/; Cosi1988|https://pubmed.ncbi.nlm.nih.gov/3130253/; Tassinari1987|https://pubmed.ncbi.nlm.nih.gov/2887152/; Tarta...
- Proposed: Awasthi2026|https://pubmed.ncbi.nlm.nih.gov/41735087/

### HIGH new_pubmed_phase_ii_iii_rct-b072cf5cadf9
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: vigabatrin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/41679982/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Comment on "safety and efficacy of vigabatrin add on compared to placebo in Lennox-Gastaut syndrome (LennoVig): A single center randomized double-blind placebo-controlled trial".
- Current: Kalita2025|https://pubmed.ncbi.nlm.nih.gov/41500178/; Bebin2023|https://pubmed.ncbi.nlm.nih.gov/37638552/; Bruni2000|https://pubmed.ncbi.nlm.nih.gov/10777431/; Dean1999|https://pubmed.ncbi.nlm.nih.gov/9924905/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10565592/; Beran1996|https://pubmed.ncbi.nlm.nih.gov/8952010/; Jackson1994|https://pubmed.ncbi.nlm.nih.gov/7957035/; Grunewald1994|https://pubmed.ncbi.nlm.nih.gov/8089668/; Gillham1993|https://pubmed.ncbi.nlm.nih.gov/8270925/; PMID1992|https://pubmed.ncbi.nlm.nih.gov/1483856/; Cosi1989|https://pubmed.ncbi.nlm.nih.gov/2757911/; Cosi1988|https://pubmed.ncbi.nlm.nih.gov/3130253/; Tassinari1987|https://pubmed.ncbi.nlm.nih.gov/2887152/; Tarta...
- Proposed: Xu2026|https://pubmed.ncbi.nlm.nih.gov/41679982/

### HIGH new_pubmed_phase_ii_iii_rct-efda04b48f2e
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: vigabatrin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/7821274/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Effects of differing dosages of vigabatrin (Sabril) on cognitive abilities and quality of life in epilepsy.
- Current: Kalita2025|https://pubmed.ncbi.nlm.nih.gov/41500178/; Bebin2023|https://pubmed.ncbi.nlm.nih.gov/37638552/; Bruni2000|https://pubmed.ncbi.nlm.nih.gov/10777431/; Dean1999|https://pubmed.ncbi.nlm.nih.gov/9924905/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10565592/; Beran1996|https://pubmed.ncbi.nlm.nih.gov/8952010/; Jackson1994|https://pubmed.ncbi.nlm.nih.gov/7957035/; Grunewald1994|https://pubmed.ncbi.nlm.nih.gov/8089668/; Gillham1993|https://pubmed.ncbi.nlm.nih.gov/8270925/; PMID1992|https://pubmed.ncbi.nlm.nih.gov/1483856/; Cosi1989|https://pubmed.ncbi.nlm.nih.gov/2757911/; Cosi1988|https://pubmed.ncbi.nlm.nih.gov/3130253/; Tassinari1987|https://pubmed.ncbi.nlm.nih.gov/2887152/; Tarta...
- Proposed: Dodrill1995|https://pubmed.ncbi.nlm.nih.gov/7821274/

### HIGH new_pubmed_phase_ii_iii_rct-48da107d2354
- Kind: new_pubmed_phase_ii_iii_rct
- Medication: vigabatrin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=True; approval_required=False
- Evidence: https://pubmed.ncbi.nlm.nih.gov/8255447/
- Summary: New qualifying placebo-controlled randomized phase II/III ASM trial report: Evaluation of the effects of vigabatrin on cognitive abilities and quality of life in epilepsy.
- Current: Kalita2025|https://pubmed.ncbi.nlm.nih.gov/41500178/; Bebin2023|https://pubmed.ncbi.nlm.nih.gov/37638552/; Bruni2000|https://pubmed.ncbi.nlm.nih.gov/10777431/; Dean1999|https://pubmed.ncbi.nlm.nih.gov/9924905/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10565592/; Beran1996|https://pubmed.ncbi.nlm.nih.gov/8952010/; Jackson1994|https://pubmed.ncbi.nlm.nih.gov/7957035/; Grunewald1994|https://pubmed.ncbi.nlm.nih.gov/8089668/; Gillham1993|https://pubmed.ncbi.nlm.nih.gov/8270925/; PMID1992|https://pubmed.ncbi.nlm.nih.gov/1483856/; Cosi1989|https://pubmed.ncbi.nlm.nih.gov/2757911/; Cosi1988|https://pubmed.ncbi.nlm.nih.gov/3130253/; Tassinari1987|https://pubmed.ncbi.nlm.nih.gov/2887152/; Tarta...
- Proposed: Dodrill1993|https://pubmed.ncbi.nlm.nih.gov/8255447/

### HIGH rct_pubmed_concordance_problem-77887223a629
- Kind: rct_pubmed_concordance_problem
- Medication: vigabatrin
- Source: PubMed
- Column: pubmed_phase_ii_iii_rct_links
- Apply: safe=False; approval_required=True
- Evidence: https://pubmed.ncbi.nlm.nih.gov/9924905/
- Summary: Existing RCT link may be assigned to the wrong drug or may not meet the phase II/III placebo-controlled randomized epilepsy criteria: title lacks primary randomized/placebo/phase trial language.
- Current: Dean1999|https://pubmed.ncbi.nlm.nih.gov/9924905/
- Proposed: update_check on 05-19-2026: PMID 9924905 needs manual review for vigabatrin; PubMed validation reason: title lacks primary randomized/placebo/phase trial language.

### HIGH source_fact_concordance_problem-d0f826cfb229
- Kind: source_fact_concordance_problem
- Medication: vigabatrin
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a88ac1b4-e2c9-45c0-b321-4785902172e3%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2009
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a88ac1b4-e2c9-45c0-b321-4785902172e3%22&limit=5); review current text before relying on it.

### HIGH source_fact_concordance_problem-43c289327614
- Kind: source_fact_concordance_problem
- Medication: zonisamide
- Source: FDA/openFDA
- Column: year_fda_cleared
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d12de43e-3ac3-4335-bc85-70d7366a91eb%22&limit=5
- Summary: year_fda_cleared could not be verified against the selected FDA/openFDA label.
- Current: 2000
- Proposed: update_check on 05-19-2026: year_fda_cleared was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d12de43e-3ac3-4335-bc85-70d7366a91eb%22&limit=5); review current text before relying on it.

### MEDIUM source_fact_concordance_problem-5a8dc6782798
- Kind: source_fact_concordance_problem
- Medication: acetazolamide
- Source: FDA/openFDA
- Column: qt_interval_effect
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10
- Summary: qt_interval_effect could not be verified against the selected FDA/openFDA label.
- Current: No QT interval effect described in selected FDA label.
- Proposed: update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-097c40372370
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00175825
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Dose-ranging Study With Brivaracetam in Patients From 16 to 65 Years With Refractory Partial Onset Seizures.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-3cbd588db294
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00464269
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Double-blind, Randomized Study Evaluating the Efficacy and Safety of Brivaracetam in Adults With Partial Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-e05a766f169b
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04666610
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Evaluate the Efficacy, Safety, and Tolerability of Brivaracetam as Monotherapy in Patients 2 to 25 Years of Age With Childhood Absence Epilepsy or Juvenile Absence Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-436f4a259845
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01405508
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Safety and Tolerability of Intravenous Brivaracetam (Infusion or Bolus) as Adjunctive Antiepileptic Therapy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-86cde09ea70b
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00504881
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Brivaracetam as add-on Treatment in Adolescents and Adults Suffering From Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-52961cfa2a10
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00490035
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Double-blind, Randomized Study Evaluating the Efficacy and Safety of Brivaracetam in Adults With Partial Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-53eef9df7f66
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03083665
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Evaluate the Efficacy and Safety of Brivaracetam in Study Participants (>=16 to 80 Years of Age) With Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b9665c9707b4
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04836559
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Investigate JNJ-40411813 in Combination With Levetiracetam or Brivaracetam in Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-14781aa2d08a
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01261325
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Brivaracetam Efficacy and Safety Study in Subjects With Partial Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-7b14a6caf35c
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: brivaracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00175929
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study of Brivaracetam in Subjects With Partial Onset Seizures

### MEDIUM source_fact_concordance_problem-8dbcd7c10ef9
- Kind: source_fact_concordance_problem
- Medication: brivaracetam
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Focal
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-8f5722b05665
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02091375
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Antiepileptic Efficacy Study of GWP42003-P in Children and Young Adults With Dravet Syndrome (GWPCARE1)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-4bb5426d0798
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02544763
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Randomized Controlled Trial of Cannabidiol (GWP42003-P, CBD) for Seizures in Tuberous Sclerosis Complex (GWPCARE6)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b693d1220964
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03421496
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Assess Cannabidiol Oral Solution With Vigabatrin as Initial Therapy in Participants With Infantile Spasms

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c8b54d31b9b9
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02224560
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of GWP42003-P for Seizures Associated With Lennox-Gastaut Syndrome in Children and Adults

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-cc5cc6abb781
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02607891
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study of Possible Drug-drug Interactions Between Stiripentol or Valproate and Cannabidiol in Patients With Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-edf5640b3fab
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02091206
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Dose-ranging Pharmacokinetics and Safety Study of GWP42003-P in Children With Dravet Syndrome (GWPCARE1)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-e76316a67b12
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03808935
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Cannabis Extract in Refractory Epilepsy Study

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b1e218a5bf91
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02224690
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Investigate the Efficacy and Safety of Cannabidiol (GWP42003-P; CBD) as Adjunctive Treatment for Seizures Associated With Lennox-Gastaut Syndrome in Children and Adults

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-75fb607dc1d8
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02783092
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Double-Blind Trial to Evaluate Efficacy and Safety of Cannabidiol as an add-on Therapy for Treatment in Refractory Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-6b38610edad8
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02224703
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: GWPCARE2 A Study to Investigate the Efficacy and Safety of Cannabidiol (GWP42003-P) in Children and Young Adults With Dravet Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-0f1aafb31360
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT06523725
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Trial Investigating the Safety and Efficacy of BRC-003 in Refractory Post-Traumatic Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-11aac5de439c
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT07023744
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: CANnabinoids for Drug Resistant Epilepsy (DRE) in Adults and Children

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-a03e2c99f432
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02318563
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Cannabidiol Oral Solution as an Adjunctive Therapy for Treatment of Participants With Inadequately Controlled Dravet Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-fe8bc81d02c0
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02318537
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Cannabidiol Oral Solution as an Adjunctive Therapy for Treatment of Participants With Inadequately Controlled Lennox-Gastaut Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-681a6f827ed0
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04406948
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study of Safety and Efficacy of MGCND00EP1 as an Add on Treatment in Children and Adolescents With Resistant Epilepsies

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-e7cc65df63ef
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cannabidiol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT05288283
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of GWP42003-P Oral Solution in Children With Epilepsy With Myoclonic-atonic Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-60acbf6a6280
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: carbamazepine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00894010
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Photosensitivity Proof of Concept Trial

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-6dcbf5f6df1e
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: carbamazepine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01713946
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-6886a001dec0
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: carbamazepine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00772603
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Evaluation of Efficacy and Safety of OXC XR as Adjunctive Therapy for Partial Seizures

### MEDIUM trade_name_addition-80b09f4bc87e
- Kind: trade_name_addition
- Medication: carbamazepine
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Carbamazepine.
- Current: Carbatrol; Curatil; Epitol; Equetro; Tegretol; Tegretol Prolonged Release; Tegretol-XR
- Proposed: Carbamazepine

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-03504868be32
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cenobamate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03678753
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Randomized, Double-Blind Study to Evaluate Efficacy and Safety of Cenobamate Adjunctive Therapy in PGTC Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-84d0c5b57e15
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cenobamate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04557085
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Randomized, Double-blind Study to Evaluate Efficacy and Safety of Cenobamate Adjunctive Therapy in POS

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-920a9df8c8a3
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cenobamate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00616148
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy of YKP3089 in Patients With Photosensitive Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-f37875ce0067
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cenobamate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01866111
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Double-Blind, Randomized, Placebo-Controlled, Phase 2 Trial of YKP3089 as Adjunctive Therapy in Subjects With Partial Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-0faa91a003a0
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: cenobamate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01397968
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of YKP3089 in Subjects With Treatment Resistant Partial Onset Seizures

### MEDIUM source_fact_concordance_problem-46a77a978870
- Kind: source_fact_concordance_problem
- Medication: cenobamate
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Focal
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-131c2de5ec6f
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: clobazam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01713946
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-500f1f4b60f1
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: clobazam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00518713
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Clobazam in Patients With Lennox-Gastaut Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-a33340c17bea
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: clobazam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02174094
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Clobazam as Adjunctive Therapy in Paediatric Patients Aged ≥1 to ≤16 Years With Dravet Syndrome

### MEDIUM trade_name_addition-d7fbe265b120
- Kind: trade_name_addition
- Medication: clobazam
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22lennox-gastaut%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Clobazam.
- Current: Frisium; Onfi; Perizam; Sympazan; Tapclob; Zacco
- Proposed: Clobazam

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-9854285a73f2
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: clonazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01150331
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study of Antiepileptic Drug in Generalised Convulsive Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b00678a05078
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: clonazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01870024
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Comparison Between Lorazepam, Clonazepam and Clonazepam + Fosphenytoin for the Treatment of Out-of-hospital Generalized Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-1b84c678b287
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: clonazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01713946
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures

### MEDIUM source_fact_concordance_problem-99dabe45c308
- Kind: source_fact_concordance_problem
- Medication: clonazepam
- Source: FDA/openFDA
- Column: enzyme_inducing_or_inhibiting
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5
- Summary: enzyme_inducing_or_inhibiting could not be verified against the selected FDA/openFDA label.
- Current: Not a CYP inducer/inhibitor
- Proposed: update_check on 05-19-2026: enzyme_inducing_or_inhibiting was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5); review current text before relying on it.

### MEDIUM trade_name_addition-9d9fdd5fe630
- Kind: trade_name_addition
- Medication: clonazepam
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22seizure%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Clonazepam.
- Current: Klonopin; Rivotril
- Proposed: Clonazepam

### MEDIUM source_fact_concordance_problem-345f0268becd
- Kind: source_fact_concordance_problem
- Medication: clorazepate dipotassium
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Focal
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.

### MEDIUM source_fact_concordance_problem-7e0919890a95
- Kind: source_fact_concordance_problem
- Medication: clorazepate dipotassium
- Source: FDA/openFDA
- Column: formulations_available
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5
- Summary: formulations_available could not be verified against the selected FDA/openFDA label.
- Current: Oral tablet currently; oral capsule historical/discontinued in Orange Book
- Proposed: update_check on 05-19-2026: formulations_available was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.

### MEDIUM source_fact_concordance_problem-ddfd8b960c44
- Kind: source_fact_concordance_problem
- Medication: clorazepate dipotassium
- Source: FDA/openFDA
- Column: qt_interval_effect
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5
- Summary: qt_interval_effect could not be verified against the selected FDA/openFDA label.
- Current: No QT interval effect described in selected FDA label.
- Proposed: update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-8be6411ab19f
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: diazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00319501
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Diazepam in the Management of Refractory Epilepsy in Selected Patients Who Require Intermittent Medical Intervention for Acute Repetitive Seizures.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-93fd39790d74
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: diazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00004297
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Phase III Randomized Study of Diazepam Vs Lorazepam Vs Placebo for Prehospital Treatment of Status Epilepticus

### MEDIUM trade_name_addition-380a63bc09f2
- Kind: trade_name_addition
- Medication: diazepam
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22status+epilepticus%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Diazepam.
- Current: Diastat; Diastat AcuDial; Libervant; Valtoco; Valium
- Proposed: Diazepam

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-25d51a89c82d
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00988429
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Eslicarbazepine Acetate (BIA 2-093) as Adjunctive Therapy for Refractory Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-6977900efee8
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00957047
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety Study of BIA 2-093 in Combination With Other Anti-Epileptic Drugs to Treat Partial Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-3915a0c466af
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01527513
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Effects of Eslicarbazepine Acetate (Esl, Bia 2-093) on Cognitive Function in Children With Partial Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-7843548535b2
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00957372
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Eslicarbazepine Acetate as Adjunctive Therapy for Refractory Partial Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-4f944e098296
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00957684
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Eslicarbazepine Acetate as Adjunctive Therapy for Refractory Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-3213094f6319
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT06597084
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Anti-epileptogenic Effects of Eslicarbazepine Acetate

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-a97a33d82f8c
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: eslicarbazepine acetate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02170077
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study to Investigate Safety and Efficacy of BIA 2-093

### MEDIUM source_fact_concordance_problem-85d165e00303
- Kind: source_fact_concordance_problem
- Medication: eslicarbazepine acetate
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Focal
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5); review current text before relying on it.

### MEDIUM source_fact_concordance_problem-48f9a032d9e2
- Kind: source_fact_concordance_problem
- Medication: ethosuximide
- Source: FDA/openFDA
- Column: qt_interval_effect
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5
- Summary: qt_interval_effect could not be verified against the selected FDA/openFDA label.
- Current: No QT interval effect described in selected FDA label.
- Proposed: update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-55f3bda9834e
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: everolimus
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01713946
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-1a897cfafb07
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: everolimus
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00790400
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of RAD001 in Patients Aged 18 and Over With Angiomyolipoma Associated With Either Tuberous Sclerosis Complex (TSC) or Sporadic Lymphangioleiomyomatosis (LAM)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-59bf36a910fc
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: everolimus
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03198949
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study Investigating the Anti-epileptic Efficacy of Afinitor (Everolimus) in Patients With Refractory Seizures Who Have Focal Cortical Dysplasia Type II (FCD II)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-65b41840f8b9
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: everolimus
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT05613166
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Adjunctive Everolimus Treatment of Refractory Epilepsy

### MEDIUM source_fact_concordance_problem-cb50e77aa378
- Kind: source_fact_concordance_problem
- Medication: everolimus
- Source: FDA/openFDA
- Column: formulations_available
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5
- Summary: formulations_available could not be verified against the selected FDA/openFDA label.
- Current: Tablet; tablet for oral suspension
- Proposed: update_check on 05-19-2026: formulations_available was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5); review current text before relying on it.

### MEDIUM trade_name_addition-eecdc77cd0e9
- Kind: trade_name_addition
- Medication: everolimus
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22partial-onset+seizures%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Everolimus.
- Current: Afinitor; Afinitor Disperz; Votubia
- Proposed: Everolimus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-9ee147cafa57
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ezogabine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00235755
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Retigabine Efficacy and Safety Trial for Partial Onset Refractory Seizures in Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-804a4c097573
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ezogabine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00232596
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Retigabine (Adjunctive Therapy) Efficacy and Safety Study for Partial Onset Refractory Seizures in Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-24297109c97d
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ezogabine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04639310
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: XEN496 (Ezogabine) in Children With KCNQ2 Developmental and Epileptic Encephalopathy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-a11753eb757c
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ezogabine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01648101
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Assessment of the Efficacy and Safety of 2 Doses of Retigabine Immediate Release (900 mg/Day and 600 mg/Day) Used as Adjunctive Therapy in Adult Asian Subjects With Drug-resistant Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-3d783a7a5dc5
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ezogabine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00310388
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Open-Label Extension Study of the Phase 3 VRX-RET-E22-302 Double-Blind Trial. 115097

### MEDIUM source_reference_gap-2373830e56b1
- Kind: source_reference_gap
- Medication: ezogabine
- Source: Local source validation
- Column: evidence_sources
- Apply: safe=True; approval_required=False
- Evidence: /Users/dgoldenh/Documents/GitHub/ASM-master/ASM-list.csv
- Summary: mechanism_source is not represented in evidence_sources.
- Current: NCBI LiverTox anticonvulsants table; EMA Trobalt withdrawal page; ILAE/GSK discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling
- Proposed: EMA Trobalt withdrawal page; Sills and Rogawski 2020 ASM mechanism review

### MEDIUM trade_name_addition-51c562e53f69
- Kind: trade_name_addition
- Medication: felbamate
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22lennox-gastaut%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Felbamate.
- Current: Felbatol; Taloxa
- Proposed: Felbamate

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-498413db0305
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: fenfluramine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02926898
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A 2-Part Study to Investigate the Dose-Ranging Safety and Pharmacokinetics, Followed by the Efficacy and Safety of ZX008 (Fenfluramine Hydrochloride) Oral Solution as an Adjunctive Therapy in Children ≥ 2 Years Old and Young Adults With Dravet Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-ac12fc310118
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: fenfluramine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03355209
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Investigate the Efficacy and Safety of ZX008 (Fenfluramine Hydrochloride) as an Adjunctive Therapy in Children and Adults With Lennox-Gastaut Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-56d8642da368
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: fenfluramine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02682927
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Trial of Two Fixed Doses of ZX008 (Fenfluramine HCl) in Children and Young Adults With Dravet Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-dbb795449a00
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: fosphenytoin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01870024
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Comparison Between Lorazepam, Clonazepam and Clonazepam + Fosphenytoin for the Treatment of Out-of-hospital Generalized Status Epilepticus

### MEDIUM source_fact_concordance_problem-55d3d60b08fc
- Kind: source_fact_concordance_problem
- Medication: gabapentin
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Focal
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10); review current text before relying on it.

### MEDIUM trade_name_addition-66aae1378305
- Kind: trade_name_addition
- Medication: gabapentin
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Gabapentin.
- Current: Gralise; Horizant; Neurontin
- Proposed: Gabapentin

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-4ff44d44d474
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01963208
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Phase 3 Study of Adjunctive Ganaxolone in Adults With Drug-resistant Partial Onset Seizures and Open-label Extension

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-933e287c2d71
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT05757544
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Safety and Efficacy Study of IV Ganaxolone as Adjuvant Therapy for Established Status Epilepticus (ESE)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-e6181b95aaac
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03350035
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Intravenous Ganaxolone as Adjunctive Therapy to Treat Subjects With Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-6319c9f46db6
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00441896
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Randomized, Controlled Trial of Ganaxolone in Patients With Infantile Spasms

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c435ce0cd595
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT05814523
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: To Evaluate the Efficacy, Safety, and Tolerability of Intravenous Ganaxolone Added to Standard of Care in Refractory Status Epilepticus (RSE)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-1f56a451132b
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00465517
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Randomized, Controlled Trial of Ganaxolone in Adult Uncontrolled Partial-Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-33c82d2368c0
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03572933
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study of Adjunctive Ganaxolone Treatment in Children and Young Adults With CDKL5 Deficiency Disorder

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c16956a7871c
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04391569
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Randomized Therapy In Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-cc8c48d12ec3
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT05249556
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Double-blind, Randomized, Placebo-controlled Trial of Ganaxolone in CDKL5 Deficiency Patients 6 Months to Less Than 2 Years Old

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-7991afaf963a
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT05323734
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Adjunctive GNX Treatment Compared With Placebo in Children and Adults With TSC-related Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-77b34d730aa9
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: ganaxolone
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03865732
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study of Adjunctive Ganaxolone Treatment in Female Children With Protocadherin 19 (PCDH19)-Related Epilepsy (Violet Study)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-528188ee85a8
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lacosamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00800215
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Trial to Investigate the Safety, Tolerability and Pharmacokinetics of Intravenous SPM 927

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b72a4e8b3b50
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lacosamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01710657
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Trial to Evaluate the Efficacy and Safety of Adjunctive Therapy With Lacosamide in Adults With Partial-Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-e8554c17c8ea
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lacosamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02408523
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Assess the Safety and Efficacy of Lacosamide Versus Placebo (a Pill Without Active Medication) in Patients With Idiopathic Generalised Epilepsy Who Are Already Taking Anti-epileptic Medications

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-5009a84c2973
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lacosamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02477839
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Lacosamide as Adjunctive Therapy in Subjects ≥1 Month to <4 Years With Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-16953c5969f7
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lacosamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01921205
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Investigate Lacosamide as Add-on Therapy in Subjects ≥4 Years to <17 Years of Age With Partial Onset Seizures

### MEDIUM trade_name_addition-d6d72b750501
- Kind: trade_name_addition
- Medication: lacosamide
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22partial-onset+seizures%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: LACOSAMIDE.
- Current: Motpoly XR; Vimpat
- Proposed: LACOSAMIDE

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-a6a6d49e8968
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lamotrigine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00104416
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study Evaluating LAMICTAL Extended-Release Therapy Added To Current Seizure Treatments In Patients With Primary Generalized Tonic-Clonic Seizures (PGTC) Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c678790bab77
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lamotrigine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00266149
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Lamotrigine and Oral Contraceptives

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-941ff9028f75
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lamotrigine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00113165
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study Evaluating LAMICTAL Extended-Release Therapy Added To Current Seizure Treatments In Patients With Partial Seizures

### MEDIUM trade_name_addition-589b0cceb967
- Kind: trade_name_addition
- Medication: lamotrigine
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Lamotrigine.
- Current: Lamictal; Lamictal CD; Lamictal ODT; Lamictal XR; Logem
- Proposed: Lamotrigine

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c4d04e7ee4db
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01150331
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study of Antiepileptic Drug in Generalised Convulsive Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-a8cbf73223fc
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00600509
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Bridging Study of L059 (Levetiracetam) in Patients With Epilepsy by Double Blind Method

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-fbbc3ff660c5
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03489044
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: An Investigation of Levetiracetam in Alzheimer's Disease

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-81f0888b010a
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00894010
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Photosensitivity Proof of Concept Trial

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-17bfc1a58a12
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00603135
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Intravenous Levetiracetam as First-line Anticonvulsive Treatment in Patients With Non-convulsive Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-3e03801ef8a9
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01228747
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Double-blind, Placebo-controlled Study of Levetiracetam in Epilepsy Patients With Generalized Tonic-clonic Seizures (Except Partial Seizures Evolving to Secondarily Generalized Seizures)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-015baeb79327
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00419094
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Conversion to Monotherapy Study With Keppra XR for Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-59245e4a8cc3
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT07234695
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: LEvetiracetam to Prevent Seizures in Symptomatic Alzheimer's Disease in Adults With Down Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-d7692be2e2f4
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04926844
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Effectiveness of Combined Levetiracetam and Midazolam in Generalized Convulsive Status Epilepticus in Children

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-288f6eddd014
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: levetiracetam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00175890
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Levetiracetam In Children (1mo to 4yrs of Age) With Partial Onset Seizures.

### MEDIUM source_fact_concordance_problem-7360fc10d604
- Kind: source_fact_concordance_problem
- Medication: levetiracetam
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Focal; Myoclonic; Primary generalized tonic-clonic
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5); review current text before relying on it.

### MEDIUM source_fact_concordance_problem-c76eb7327b63
- Kind: source_fact_concordance_problem
- Medication: levetiracetam
- Source: FDA/openFDA
- Column: enzyme_inducing_or_inhibiting
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5
- Summary: enzyme_inducing_or_inhibiting could not be verified against the selected FDA/openFDA label.
- Current: Not an enzyme inducer/inhibitor
- Proposed: update_check on 05-19-2026: enzyme_inducing_or_inhibiting was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5); review current text before relying on it.

### MEDIUM trade_name_addition-387ee4518629
- Kind: trade_name_addition
- Medication: levetiracetam
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Levetiracetam.
- Current: Desitrend; Eltam; Elepsia XR; Keppra; Keppra XR; Roweepra; Roweepra XR; Spritam
- Proposed: Levetiracetam

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-477d4b9b267c
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lorazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00603135
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Intravenous Levetiracetam as First-line Anticonvulsive Treatment in Patients With Non-convulsive Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-63bf70a50d0a
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lorazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01870024
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Comparison Between Lorazepam, Clonazepam and Clonazepam + Fosphenytoin for the Treatment of Out-of-hospital Generalized Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-2e08fbd6daf5
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lorazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00004297
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Phase III Randomized Study of Diazepam Vs Lorazepam Vs Placebo for Prehospital Treatment of Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c4fd824c8ee0
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lorazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02564029
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: PF-06372865 in Subjects With Photosensitive Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-3f3799ba4874
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: lorazepam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00465244
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Seizure Therapy With Intravenous Levetiracetam and Lorazepam

### MEDIUM source_fact_concordance_problem-18a40000fd47
- Kind: source_fact_concordance_problem
- Medication: lorazepam
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Ativan%22+OR+openfda.brand_name%3A%22Ativan%22+OR+openfda.substance_name%3A%22Ativan%22&limit=10
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Status epilepticus; Seizure clusters / rescue
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Ativan%22+OR+openfda.brand_name%3A%22Ativan%22+OR+openfda.substance_name%3A%22Ativan%22&limit=10); review current text before relying on it.

### MEDIUM source_fact_concordance_problem-8bae2dfdc701
- Kind: source_fact_concordance_problem
- Medication: lorazepam
- Source: FDA/openFDA
- Column: enzyme_inducing_or_inhibiting
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Ativan%22+OR+openfda.brand_name%3A%22Ativan%22+OR+openfda.substance_name%3A%22Ativan%22&limit=10
- Summary: enzyme_inducing_or_inhibiting could not be verified against the selected FDA/openFDA label.
- Current: Not a CYP inducer/inhibitor; glucuronidated
- Proposed: update_check on 05-19-2026: enzyme_inducing_or_inhibiting was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Ativan%22+OR+openfda.brand_name%3A%22Ativan%22+OR+openfda.substance_name%3A%22Ativan%22&limit=10); review current text before relying on it.

### MEDIUM trade_name_addition-b9b43c47fc78
- Kind: trade_name_addition
- Medication: lorazepam
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22status+epilepticus%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Lorazepam.
- Current: Ativan; Loreev XR
- Proposed: Lorazepam

### MEDIUM source_fact_concordance_problem-9051c2939aa4
- Kind: source_fact_concordance_problem
- Medication: methsuximide
- Source: FDA/openFDA
- Column: qt_interval_effect
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Summary: qt_interval_effect could not be verified against the selected FDA/openFDA label.
- Current: No QT interval effect described in selected FDA label.
- Proposed: update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b6d55568968d
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: midazolam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01999777
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Evaluate the Safety and Efficacy of USL261 in Patients With Increased Bouts of Seizure Activity in the EMU

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-56897abca4e0
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: midazolam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01390220
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Evaluate the Safety and Efficacy of USL261 (Intranasal Midazolam) in Patients With Seizure Clusters

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-5b27e2248d8f
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: midazolam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04926844
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Effectiveness of Combined Levetiracetam and Midazolam in Generalized Convulsive Status Epilepticus in Children

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-03ccb5eab6aa
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: midazolam
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT05779657
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Combined Ketamine and Midazolam for Generalized Convulsive Status Epilepticus

### MEDIUM source_fact_concordance_problem-6b954d326c5f
- Kind: source_fact_concordance_problem
- Medication: midazolam
- Source: FDA/openFDA
- Column: enzyme_inducing_or_inhibiting
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5
- Summary: enzyme_inducing_or_inhibiting could not be verified against the selected FDA/openFDA label.
- Current: Not an inducer/inhibitor; CYP3A substrate
- Proposed: update_check on 05-19-2026: enzyme_inducing_or_inhibiting was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-cf3867c7198a
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: oxcarbazepine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00772603
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Evaluation of Efficacy and Safety of OXC XR as Adjunctive Therapy for Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-239ae1f68cf4
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: oxcarbazepine
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00975715
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy, Safety and Tolerability of TRI476 (Oxcarbazepine) in Children With Inadequately Controlled Partial Onset Seizures

### MEDIUM trade_name_addition-0098785bb658
- Kind: trade_name_addition
- Medication: oxcarbazepine
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22partial-onset+seizures%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Oxcarbazepine.
- Current: Oxtellar XR; Trileptal
- Proposed: Oxcarbazepine

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-78647697e188
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00144690
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: E2007 Given as Adjunctive Therapy in Patients With Refractory Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-704bc530338a
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00699582
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: To Evaluate The Efficacy and Safety of E2007 (Perampanel) Given as Adjunctive Therapy in Subjects With Refractory Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-f3d60c6fec30
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01393743
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Efficacy and Safety Study of Adjunctive Perampanel in Primary Generalized Tonic Clonic Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-d01aa43487fa
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT06401707
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: PeRampanel fOr Status ePilEpticus pRophylaxis Post-cardiac Arrest

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-238e755f0fa3
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00699972
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Evaluating the Efficacy and Safety of E2007 (Perampanel) Given as Adjunctive Therapy in Subjects With Refractory Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c4bd41f361f7
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01618695
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study With an Open-label Extension Phase to Evaluate the Efficacy and Safety of Perampanel (E2007) Administered as an Adjunctive Therapy in Subjects With Refractory Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-98ff5a0d723f
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00700310
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Evaluating Efficacy and Safety of E2007 (Perampanel) Given as Adjunctive Therapy in Subjects With Refractory Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c915501730b9
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03780907
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Safety and Pharmacokinetics Study of E2007 to Treat Partial and Generalised Seizures in People With Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-0db469871592
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00416195
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Exploring the Safety And Tolerability of Doses of E2007 up to a Maximum of 12 mg In Patients With Refractory Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-5ad40793dd5c
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: perampanel
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02834793
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study of Perampanel as Adjunctive Treatment for Inadequately Controlled Seizures Associated With Lennox-Gastaut Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-4e9e485a3e95
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: phenobarbital
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01713946
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b42647f9800a
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: phenobarbital
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03602118
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Evaluate Phenobarbital Sodium Injection for the Treatment of Neonatal Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-8cae19b9ffa9
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: phenobarbital
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01284556
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Evaluation Phenobarbital as Adjunctive Therapy in Participants With Partial Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-47a13d5b4f4d
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: phenobarbital
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04320940
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Intravenous Phenobarbital in Neonatal Seizures

### MEDIUM source_fact_concordance_problem-75185ea3a10c
- Kind: source_fact_concordance_problem
- Medication: phenobarbital
- Source: FDA/openFDA
- Column: qt_interval_effect
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5
- Summary: qt_interval_effect could not be verified against the selected FDA/openFDA label.
- Current: No direct QT effect established
- Proposed: update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-28312e9c6f6f
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: phenytoin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01870024
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Comparison Between Lorazepam, Clonazepam and Clonazepam + Fosphenytoin for the Treatment of Out-of-hospital Generalized Status Epilepticus

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-f12b1fdad1ef
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: phenytoin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01713946
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-2aa81236e60f
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: phenytoin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01730313
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Treatment of Nodding Syndrome - A Randomized Blinded Placebo-Controlled Crossover Trial of Oral Pyridoxine and Conventional Anti-Epileptic Therapy, in Northern Uganda - 2012

### MEDIUM source_fact_concordance_problem-cd863eca6f3f
- Kind: source_fact_concordance_problem
- Medication: phenytoin
- Source: FDA/openFDA
- Column: formulations_available
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Summary: formulations_available could not be verified against the selected FDA/openFDA label.
- Current: Capsule; chewable tablet; oral suspension; IV injection
- Proposed: update_check on 05-19-2026: formulations_available was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-831ced3f8bc7
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: pregabalin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00437281
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Safety, Tolerability, and Pharmacokinetic Study of Pregabalin in Pediatric Patients With Partial Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-59cd766fa5ee
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: pregabalin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01747915
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Safety, Efficacy and Tolerability Trial of Pregabalin as Add-On Treatment in Pediatric and Adult Subjects With Primary Generalized Tonic-Clonic (i.e., Grand Mal) Seizures.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c762239b97cd
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: pregabalin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02072824
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Safety, Efficacy, and Tolerability Trial of Pregabalin as Add-On Treatment in Pediatric Subjects <4 Years of Age With Partial Onset Seizures.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-fbb56d1c5368
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: pregabalin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00141258
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Pregabalin Epilepsy Add-On Trial

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-f5ba764e330d
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: pregabalin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00643136
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study of Lyrica as Treatment for Sleep Problems in Patients With Sleep Problems and Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-3850b7912de2
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: pregabalin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01262677
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Once-A-Day Pregabalin For Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-700a247cd096
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: pregabalin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01389596
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study of the Efficacy and Safety of Pregabalin as Add-On Therapy for Partial Onset Seizures in Children Ages 4-16 Years

### MEDIUM source_fact_concordance_problem-ade8eae67f58
- Kind: source_fact_concordance_problem
- Medication: pregabalin
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Focal
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5); review current text before relying on it.

### MEDIUM source_fact_concordance_problem-8987a56a7909
- Kind: source_fact_concordance_problem
- Medication: pregabalin
- Source: FDA/openFDA
- Column: enzyme_inducing_or_inhibiting
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5
- Summary: enzyme_inducing_or_inhibiting could not be verified against the selected FDA/openFDA label.
- Current: Not metabolized; not an enzyme inducer/inhibitor
- Proposed: update_check on 05-19-2026: enzyme_inducing_or_inhibiting was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5); review current text before relying on it.

### MEDIUM trade_name_addition-38974123d586
- Kind: trade_name_addition
- Medication: pregabalin
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22partial-onset+seizures%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: PREGABALIN.
- Current: Alzain; Lyrica
- Proposed: PREGABALIN

### MEDIUM source_fact_concordance_problem-d651cfd5cb9a
- Kind: source_fact_concordance_problem
- Medication: primidone
- Source: FDA/openFDA
- Column: qt_interval_effect
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5
- Summary: qt_interval_effect could not be verified against the selected FDA/openFDA label.
- Current: No QT interval effect described in selected FDA label.
- Proposed: update_check on 05-19-2026: qt_interval_effect was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-fa9d842bc070
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: rufinamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01146951
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-Controlled, Double-Blind Comparative Study of E2080 in Lennox-Gastaut Syndrome Patients (Study E2080-J081-304)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-a0d421a28032
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: rufinamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00334958
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Rufinamide Given as Adjunctive Therapy in Participants With Refractory Partial Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-0910b4bd2583
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: stiripentol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02926898
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A 2-Part Study to Investigate the Dose-Ranging Safety and Pharmacokinetics, Followed by the Efficacy and Safety of ZX008 (Fenfluramine Hydrochloride) Oral Solution as an Adjunctive Therapy in Children ≥ 2 Years Old and Young Adults With Dravet Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-27dc159cb643
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: stiripentol
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02607891
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study of Possible Drug-drug Interactions Between Stiripentol or Valproate and Cannabidiol in Patients With Epilepsy

### MEDIUM source_reference_gap-040c7479de0f
- Kind: source_reference_gap
- Medication: sultiame
- Source: Local source validation
- Column: evidence_sources
- Apply: safe=True; approval_required=False
- Evidence: /Users/dgoldenh/Documents/GitHub/ASM-master/ASM-list.csv
- Summary: mechanism_source is not represented in evidence_sources.
- Current: Epilepsy Society ASM list; Wikipedia anticonvulsant drug-class list; UK eMC SmPC labeling; Sills and Rogawski 2020 ASM mechanism review; Sulthiame sodium-current mechanism study; FDA/DailyMed labeling
- Proposed: UK eMC SmPC labeling; Sulthiame sodium-current mechanism study

### MEDIUM source_fact_concordance_problem-1fe840e83362
- Kind: source_fact_concordance_problem
- Medication: tiagabine
- Source: FDA/openFDA
- Column: epilepsy_type
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22tiagabine%22+OR+openfda.brand_name%3A%22tiagabine%22+OR+openfda.substance_name%3A%22tiagabine%22&limit=10
- Summary: epilepsy_type could not be verified against the selected FDA/openFDA label.
- Current: Focal
- Proposed: update_check on 05-19-2026: epilepsy_type was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22tiagabine%22+OR+openfda.brand_name%3A%22tiagabine%22+OR+openfda.substance_name%3A%22tiagabine%22&limit=10); review current text before relying on it.

### MEDIUM source_fact_concordance_problem-aa03803572f0
- Kind: source_fact_concordance_problem
- Medication: tiagabine
- Source: FDA/openFDA
- Column: enzyme_inducing_or_inhibiting
- Apply: safe=False; approval_required=True
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22tiagabine%22+OR+openfda.brand_name%3A%22tiagabine%22+OR+openfda.substance_name%3A%22tiagabine%22&limit=10
- Summary: enzyme_inducing_or_inhibiting could not be verified against the selected FDA/openFDA label.
- Current: Not a major inducer/inhibitor; CYP3A substrate
- Proposed: update_check on 05-19-2026: enzyme_inducing_or_inhibiting was not concordant with the selected FDA/openFDA label (https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22tiagabine%22+OR+openfda.brand_name%3A%22tiagabine%22+OR+openfda.substance_name%3A%22tiagabine%22&limit=10); review current text before relying on it.

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-a1a68b34864f
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: topiramate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00113815
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Topiramate as Adjunctive Therapy in Infants 1-24 Months for the Control of Partial Onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-e2fa8dd69260
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: topiramate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01713946
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-1e54776c5774
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: topiramate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00004776
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Phase III Randomized, Double-Blind, Placebo-Controlled Study of Oral Topiramate for Lennox-Gastaut Syndrome

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b8de731a3d50
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: topiramate
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01142193
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Study to Evaluate the Safety and Effectiveness of USL255 in Patients With Refractory Partial-onset Seizures

### MEDIUM trade_name_addition-c2f2f0a16dd3
- Kind: trade_name_addition
- Medication: topiramate
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Topiramate.
- Current: Eprontia; Qudexy XR; Topamax; Topamax Sprinkle; Trokendi XR
- Proposed: Topiramate

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-f0e6bffe07b1
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: valproic acid
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02607891
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study of Possible Drug-drug Interactions Between Stiripentol or Valproate and Cannabidiol in Patients With Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-27acb8b4489c
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: valproic acid
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT05431595
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Managing Agitated Delirium With Neuroleptics and Anti-Epileptics as a Neuroleptic Sparing Strategy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-50c125e89d5f
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: valproic acid
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01730313
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Treatment of Nodding Syndrome - A Randomized Blinded Placebo-Controlled Crossover Trial of Oral Pyridoxine and Conventional Anti-Epileptic Therapy, in Northern Uganda - 2012

### MEDIUM trade_name_addition-a8472b310f45
- Kind: trade_name_addition
- Medication: valproic acid
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Divalproex Sodium.
- Current: Convulex; Depacon; Depakene; Depakine; Depakote; Depakote ER; Depakote Sprinkles; Depakyn; Dyzantil; Epilim Chrono; Epilim Chronosphere; Epival; Stavzor; Valproate Sodium
- Proposed: Divalproex Sodium

### MEDIUM trade_name_addition-f93cdba993e7
- Kind: trade_name_addition
- Medication: valproic acid
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22seizure%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Valproic Acid.
- Current: Convulex; Depacon; Depakene; Depakine; Depakote; Depakote ER; Depakote Sprinkles; Depakyn; Dyzantil; Epilim Chrono; Epilim Chronosphere; Epival; Stavzor; Valproate Sodium
- Proposed: Valproic Acid

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-6b35e2d06cf3
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: vigabatrin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT02849457
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Preventing Epilepsy Using Vigabatrin In Infants With Tuberous Sclerosis Complex

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-9da36ab0e553
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: vigabatrin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT03421496
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Study to Assess Cannabidiol Oral Solution With Vigabatrin as Initial Therapy in Participants With Infantile Spasms

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-60ecc5595533
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: vigabatrin
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT04987463
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Rapamycin Versus Vigabatrin in the Prevention of Tuberous Sclerosis Complex Symptoms in Infants

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-2c1b04dcad6b
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: zonisamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT01713946
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: A Placebo-controlled Study of Efficacy & Safety of 2 Trough-ranges of Everolimus as Adjunctive Therapy in Patients With Tuberous Sclerosis Complex (TSC) & Refractory Partial-onset Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b08eb9e906b5
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: zonisamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00693017
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Adjunctive Zonisamide in Myoclonic Seizures Associated With Idiopathic Generalised Epilepsy

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-b6104c93d190
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: zonisamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00692003
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Adjunctive Zonisamide in Primary Generalised Tonic Clonic Seizures

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-f6f9a8b58484
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: zonisamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00566254
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Efficacy and Safety of Adjunctive Zonisamide in Paediatric Partial Onset Seizures (CATZ Study)

### MEDIUM nih_clinicaltrial_phase_ii_iii_rct-c595b24da4b7
- Kind: nih_clinicaltrial_phase_ii_iii_rct
- Medication: zonisamide
- Source: NIH ClinicalTrials.gov
- Apply: safe=False; approval_required=False
- Evidence: https://clinicaltrials.gov/study/NCT00327717
- Summary: NIH ClinicalTrials.gov lists a phase II/III randomized placebo-controlled epilepsy/seizure trial: Evaluating the Efficacy and Safety of Zonisamide in the Treatment of Partial Seizures

### MEDIUM trade_name_addition-442b609d32cd
- Kind: trade_name_addition
- Medication: zonisamide
- Source: FDA/openFDA
- Column: trade_names
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=indications_and_usage%3A%22epilepsy%22&limit=100
- Summary: Source labels mention trade name(s) not present in CSV: Zonisamide.
- Current: Desizon; Zonegran; Zonisade
- Proposed: Zonisamide

### WARNING source_error-241abdf33577
- Kind: source_error
- Source: Epilepsy Foundation
- Apply: safe=False; approval_required=False
- Evidence: https://www.epilepsy.com/tools-resources/seizure-medication-list
- Summary: HTTP 403 for https://www.epilepsy.com/tools-resources/seizure-medication-list

### INFO fda_warning_metadata_refresh-a5437214f970
- Kind: fda_warning_metadata_refresh
- Medication: acetazolamide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58093032-8480-4d0f-82be-92e643bdbea4; published=Jan 16, 2026; title=ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) INJECTION, POWDER, FOR SOLUTION [SAGENT PHARMACEUTICALS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58093032-8480-4d0f-82be-92e643bdbea4
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=4dd56001-4941-4ff0-9f30-02a1bcc4fe7e; effective_time=20260410; title=Acetazolamide / ACETAZOLAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22acetazolamide+sodium%22+OR+openfda.brand_name%3A%22acetazolamide+sodium%22+OR+openfda.substance_name%3A%22acetazolamide+sodium%22&limit=10

### INFO fda_warning_metadata_refresh-d0a4b8ecc306
- Kind: fda_warning_metadata_refresh
- Medication: brivaracetam
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=3cf2f439-0e97-443e-8e33-25ecef616f6c; published=May 14, 2026; title=BRIVIACT (BRIVARACETAM) TABLET, FILM COATED BRIVIACT (BRIVARACETAM) SOLUTION BRIVIACT (BRIVARACETAM) INJECTION, SUSPENSION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=3cf2f439-0e97-443e-8e33-25ecef616f6c; effective_time=20260513; title=Briviact / BRIVARACETAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5

### INFO fda_warning_metadata_refresh-d25acf3821ce
- Kind: fda_warning_metadata_refresh
- Medication: cannabidiol
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=8bf27097-4870-43fb-94f0-f3d0871d1eec; published=Nov 17, 2025; title=EPIDIOLEX (CANNABIDIOL) SOLUTION [JAZZ PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=8bf27097-4870-43fb-94f0-f3d0871d1eec; effective_time=20250731; title=Epidiolex / CANNABIDIOL; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5

### INFO fda_warning_metadata_refresh-39410ee1ac35
- Kind: fda_warning_metadata_refresh
- Medication: carbamazepine
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=bc03e499-5bac-4293-bff4-6864153a624d; published=Jul 03, 2025; title=CARBATROL (CARBAMAZEPINE) CAPSULE, EXTENDED RELEASE [TAKEDA PHARMACEUTICALS AMERICA, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=bc03e499-5bac-4293-bff4-6864153a624d
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=bc03e499-5bac-4293-bff4-6864153a624d; effective_time=20250627; title=Carbatrol / CARBAMAZEPINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=5

### INFO fda_warning_metadata_refresh-d03652dfeffa
- Kind: fda_warning_metadata_refresh
- Medication: cenobamate
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=565c2126-57ae-4e29-b443-723bbe7e2072; published=Feb 02, 2026; title=XCOPRI TITRATION PACK (CENOBAMATE) KIT XCOPRI (CENOBAMATE) TABLET, FILM COATED XCOPRI MAINTENANCE PACK (CENOBAMATE) KIT XCOPRI (CENOBAMATE) TABLET [SK LIFE SCIENCE, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=565c2126-57ae-4e29-b443-723bbe7e2072
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=565c2126-57ae-4e29-b443-723bbe7e2072; effective_time=20250925; title=Xcopri; Xcopri Maintenance Pack; Xcopri Titration Pack / CENOBAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5

### INFO fda_warning_metadata_refresh-61af11bdf09c
- Kind: fda_warning_metadata_refresh
- Medication: clobazam
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22de03bd69-2dca-459c-93b4-541fd3e9571c%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=de03bd69-2dca-459c-93b4-541fd3e9571c; published=Dec 17, 2025; title=ONFI (CLOBAZAM) TABLET ONFI (CLOBAZAM) SUSPENSION [LUNDBECK PHARMACEUTICALS LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=de03bd69-2dca-459c-93b4-541fd3e9571c
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=de03bd69-2dca-459c-93b4-541fd3e9571c; effective_time=20240312; title=Onfi / CLOBAZAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22de03bd69-2dca-459c-93b4-541fd3e9571c%22&limit=5

### INFO fda_warning_metadata_refresh-3ab158dfb03e
- Kind: fda_warning_metadata_refresh
- Medication: clonazepam
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=cfa0d79a-843c-4b88-95a1-e9511d649ca1; published=Dec 02, 2025; title=KLONOPIN (CLONAZEPAM) TABLET [H2-PHARMA, LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cfa0d79a-843c-4b88-95a1-e9511d649ca1
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=cfa0d79a-843c-4b88-95a1-e9511d649ca1; effective_time=20251201; title=Klonopin / CLONAZEPAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5

### INFO fda_warning_metadata_refresh-9beafe880f5a
- Kind: fda_warning_metadata_refresh
- Medication: clorazepate dipotassium
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=919cbd07-f587-4005-acff-26213dd1d1fb; published=Mar 26, 2026; title=CLORAZEPATE DIPOTASSIUM TABLET [AUROLIFE PHARMA LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=919cbd07-f587-4005-acff-26213dd1d1fb
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=919cbd07-f587-4005-acff-26213dd1d1fb; effective_time=20260325; title=CLORAZEPATE DIPOTASSIUM / CLORAZEPATE DIPOTASSIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5

### INFO fda_warning_metadata_refresh-4b5bf8b4927d
- Kind: fda_warning_metadata_refresh
- Medication: eslicarbazepine acetate
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=3d0c9554-eaeb-4694-8089-00133fcadce3; published=Dec 05, 2023; title=APTIOM (ESLICARBAZEPINE ACETATE) TABLET APTIOM (ESLICARBAZEPINE ACETATE) KIT [SUMITOMO PHARMA AMERICA, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3d0c9554-eaeb-4694-8089-00133fcadce3
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=3d0c9554-eaeb-4694-8089-00133fcadce3; effective_time=20231110; title=Aptiom / ESLICARBAZEPINE ACETATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5

### INFO fda_warning_metadata_refresh-183ee13cd841
- Kind: fda_warning_metadata_refresh
- Medication: ethosuximide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6; published=Jul 16, 2024; title=ZARONTIN (ETHOSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=0e008f33-70a1-4bc6-b3a0-d45214418ab6; effective_time=20240715; title=Zarontin / ETHOSUXIMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5

### INFO fda_warning_metadata_refresh-5a4180a7b11b
- Kind: fda_warning_metadata_refresh
- Medication: ethotoin
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [ethotoin; Peganone].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [ethotoin; Peganone].

### INFO fda_warning_metadata_refresh-62ddf7f4de7d
- Kind: fda_warning_metadata_refresh
- Medication: everolimus
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=43ef3c29-0e25-4fdd-aea1-06a20af9bbab; published=Mar 02, 2026; title=EVEROLIMUS TABLET [AUROBINDO PHARMA LIMITED]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=43ef3c29-0e25-4fdd-aea1-06a20af9bbab
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=43ef3c29-0e25-4fdd-aea1-06a20af9bbab; effective_time=20260226; title=everolimus / EVEROLIMUS; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5

### INFO fda_warning_metadata_refresh-8c970146d582
- Kind: fda_warning_metadata_refresh
- Medication: ezogabine
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [ezogabine; retigabine; Potiga; Trobalt].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [ezogabine; retigabine; Potiga; Trobalt].

### INFO fda_warning_metadata_refresh-1fef5bcc9e9c
- Kind: fda_warning_metadata_refresh
- Medication: felbamate
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=2f522701-397a-11de-8a39-0800200c9a66; published=Dec 31, 2025; title=FELBATOL (FELBAMATE) TABLET FELBATOL (FELBAMATE) SUSPENSION [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2f522701-397a-11de-8a39-0800200c9a66
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2f522701-397a-11de-8a39-0800200c9a66; effective_time=20250815; title=Felbatol / FELBAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5

### INFO fda_warning_metadata_refresh-4b46db3a1844
- Kind: fda_warning_metadata_refresh
- Medication: fenfluramine
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=e88f360e-33ad-4cd6-b2de-5ef885857c5d; published=Nov 17, 2025; title=FINTEPLA (FENFLURAMINE) SOLUTION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e88f360e-33ad-4cd6-b2de-5ef885857c5d
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=e88f360e-33ad-4cd6-b2de-5ef885857c5d; effective_time=20251027; title=Fintepla / FENFLURAMINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5

### INFO fda_warning_metadata_refresh-5f02df31b8a9
- Kind: fda_warning_metadata_refresh
- Medication: fosphenytoin
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a; published=Aug 29, 2025; title=CEREBYX (FOSPHENYTOIN SODIUM) INJECTION, SOLUTION [PFIZER LABORATORIES DIV PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a; effective_time=20250828; title=CEREBYX / FOSPHENYTOIN SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5

### INFO fda_warning_metadata_refresh-e0359b1abc81
- Kind: fda_warning_metadata_refresh
- Medication: gabapentin
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd; published=May 07, 2025; title=HORIZANT (GABAPENTIN ENACARBIL) TABLET, EXTENDED RELEASE [AZURITY PHARMACEUTICALS, INC. (FORMERLY ARBOR PHARMACEUTICALS)]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=466273b1-c9fc-3930-c94b-aa11394d5140; effective_time=20250501; title=Gralise / GABAPENTIN; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Gralise%22+OR+openfda.brand_name%3A%22Gralise%22+OR+openfda.substance_name%3A%22Gralise%22&limit=10

### INFO fda_warning_metadata_refresh-95e876d2b356
- Kind: fda_warning_metadata_refresh
- Medication: ganaxolone
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d91612c4-b03a-4be4-a1ee-6a13e3b83d4e%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=d91612c4-b03a-4be4-a1ee-6a13e3b83d4e; published=Dec 01, 2025; title=ZTALMY (GANAXOLONE) SUSPENSION [IMMEDICA PHARMA US INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d91612c4-b03a-4be4-a1ee-6a13e3b83d4e
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=d91612c4-b03a-4be4-a1ee-6a13e3b83d4e; effective_time=20251128; title=ZTALMY / GANAXOLONE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d91612c4-b03a-4be4-a1ee-6a13e3b83d4e%22&limit=5

### INFO fda_warning_metadata_refresh-141c484d2a9c
- Kind: fda_warning_metadata_refresh
- Medication: lacosamide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2; published=May 13, 2026; title=VIMPAT (LACOSAMIDE) TABLET, FILM COATED VIMPAT (LACOSAMIDE) INJECTION VIMPAT (LACOSAMIDE) SOLUTION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=fb8235b4-4cd3-6f22-e053-6294a90a545c; effective_time=20250716; title=MOTPOLY XR / LACOSAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22Motpoly+XR%22+OR+openfda.brand_name%3A%22Motpoly+XR%22+OR+openfda.substance_name%3A%22Motpoly+XR%22&limit=10

### INFO fda_warning_metadata_refresh-8d5a93e43e00
- Kind: fda_warning_metadata_refresh
- Medication: lamotrigine
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d7e3572d-56fe-4727-2bb4-013ccca22678%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=d7e3572d-56fe-4727-2bb4-013ccca22678; published=Nov 17, 2025; title=LAMICTAL (LAMOTRIGINE) TABLET LAMICTAL (LAMOTRIGINE) TABLET, FOR SUSPENSION LAMICTAL ODT (LAMOTRIGINE) TABLET, ORALLY DISINTEGRATING LAMICTAL (LAMOTRIGINE) KIT [GLAXOSMITHKLINE LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d7e3572d-56fe-4727-2bb4-013ccca22678
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=d7e3572d-56fe-4727-2bb4-013ccca22678; effective_time=20251010; title=LAMICTAL; LAMICTAL ODT / LAMOTRIGINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d7e3572d-56fe-4727-2bb4-013ccca22678%22&limit=5

### INFO fda_warning_metadata_refresh-f896430f401f
- Kind: fda_warning_metadata_refresh
- Medication: levetiracetam
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=2919e43b-69a8-434c-a2d2-1f3ecd7554c0; published=Jun 26, 2025; title=KEPPRA XR (LEVETIRACETAM) TABLET, FILM COATED, EXTENDED RELEASE [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2919e43b-69a8-434c-a2d2-1f3ecd7554c0
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=2919e43b-69a8-434c-a2d2-1f3ecd7554c0; effective_time=20250624; title=Keppra XR / LEVETIRACETAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5

### INFO fda_warning_metadata_refresh-04350c3fbabb
- Kind: fda_warning_metadata_refresh
- Medication: mephenytoin
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [mephenytoin; Mesantoin].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [mephenytoin; Mesantoin].

### INFO fda_warning_metadata_refresh-778d14e046fd
- Kind: fda_warning_metadata_refresh
- Medication: metharbital
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [metharbital; Gemonil].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [metharbital; Gemonil].

### INFO fda_warning_metadata_refresh-396d72324abb
- Kind: fda_warning_metadata_refresh
- Medication: methsuximide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=64a6ee88-c6b1-4e13-8208-b6772ef65a74; published=Apr 09, 2026; title=CELONTIN (METHSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=64a6ee88-c6b1-4e13-8208-b6772ef65a74
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=64a6ee88-c6b1-4e13-8208-b6772ef65a74; effective_time=20260407; title=Celontin / METHSUXIMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5

### INFO fda_warning_metadata_refresh-6d6f723b88fd
- Kind: fda_warning_metadata_refresh
- Medication: midazolam
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=2b29422e-54d5-4a49-8522-e9cf752368c3; published=Jan 31, 2023; title=NAYZILAM (MIDAZOLAM) SPRAY [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b29422e-54d5-4a49-8522-e9cf752368c3
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2b29422e-54d5-4a49-8522-e9cf752368c3; effective_time=20230119; title=Nayzilam / MIDAZOLAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5

### INFO fda_warning_metadata_refresh-c6c6a182ad03
- Kind: fda_warning_metadata_refresh
- Medication: oxcarbazepine
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=aa610e56-1d1d-11e1-8bc2-0800200c9a66; published=Nov 17, 2025; title=OXTELLAR XR (OXCARBAZEPINE) TABLET [SUPERNUS PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aa610e56-1d1d-11e1-8bc2-0800200c9a66
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=aa610e56-1d1d-11e1-8bc2-0800200c9a66; effective_time=20251022; title=OXTELLAR XR / OXCARBAZEPINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5

### INFO fda_warning_metadata_refresh-6bf8fa9e6427
- Kind: fda_warning_metadata_refresh
- Medication: paramethadione
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [paramethadione; Paradione].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [paramethadione; Paradione].

### INFO fda_warning_metadata_refresh-19307f16717b
- Kind: fda_warning_metadata_refresh
- Medication: perampanel
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22perampanel%22+OR+openfda.brand_name%3A%22perampanel%22+OR+openfda.substance_name%3A%22perampanel%22&limit=10
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=71cf3309-e182-473c-8b0b-280cabd0e122; published=Jan 28, 2026; title=FYCOMPA (PERAMPANEL) TABLET FYCOMPA (PERAMPANEL) SUSPENSION [EISAI INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=71cf3309-e182-473c-8b0b-280cabd0e122
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=ec812ea3-de3a-4271-957c-db8f692d1ae3; effective_time=20240105; title=Fycompa / PERAMPANEL; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22perampanel%22+OR+openfda.brand_name%3A%22perampanel%22+OR+openfda.substance_name%3A%22perampanel%22&limit=10

### INFO fda_warning_metadata_refresh-fb184c2cfd32
- Kind: fda_warning_metadata_refresh
- Medication: phenacemide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [phenacemide; Phenurone].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [phenacemide; Phenurone].

### INFO fda_warning_metadata_refresh-b88a4ceff2b0
- Kind: fda_warning_metadata_refresh
- Medication: phenobarbital
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=8c7d0402-4977-4c25-bc4b-11db91339e9a; published=; title=These highlights do not include all the information needed to use SEZABY safely and effectively. See full prescribing information for SEZABY. SEZABY™ (phenobarbital sodium) for injection, for intravenous use, CIV Initial U.S. Approval: 2022; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=8c7d0402-4977-4c25-bc4b-11db91339e9a; effective_time=20251223; title=SEZABY / PHENOBARBITAL SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5

### INFO fda_warning_metadata_refresh-dd89eda17606
- Kind: fda_warning_metadata_refresh
- Medication: phensuximide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [phensuximide; Milontin].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [phensuximide; Milontin].

### INFO fda_warning_metadata_refresh-1321f86509b2
- Kind: fda_warning_metadata_refresh
- Medication: phenytoin
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=a52cf1bd-dc1f-47be-aba8-29066d9a50fb; published=; title=Phenytoin Sodium Injection, USP Rx Only These highlights do not include all the information needed to use PHENYTOIN SODIUM INJECTION safely and effectively. See full prescribing information for PHENYTOIN SODIUM INJECTION. PHENYTOIN Sodium Injection for intravenous or intramuscular use Initial U.S. Approval: 1953; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a52cf1bd-dc1f-47be-aba8-29066d9a50fb
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=a52cf1bd-dc1f-47be-aba8-29066d9a50fb; effective_time=20241226; title=PHENYTOIN SODIUM / PHENYTOIN SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5

### INFO fda_warning_metadata_refresh-b1702f6fb1b6
- Kind: fda_warning_metadata_refresh
- Medication: piracetam
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [piracetam; Nootropil].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [piracetam; Nootropil].

### INFO fda_warning_metadata_refresh-bdc5f477d132
- Kind: fda_warning_metadata_refresh
- Medication: pregabalin
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=f280bbd8-2af2-444a-bd96-e409337ca6dd; published=Apr 15, 2026; title=LYRICA CR (PREGABALIN) TABLET, FILM COATED, EXTENDED RELEASE [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f280bbd8-2af2-444a-bd96-e409337ca6dd
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=f280bbd8-2af2-444a-bd96-e409337ca6dd; effective_time=20260312; title=Lyrica CR / PREGABALIN; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5

### INFO fda_warning_metadata_refresh-859b6fa37d32
- Kind: fda_warning_metadata_refresh
- Medication: primidone
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=af593171-dabb-4ea3-b44c-89ed457b2c46; published=Aug 12, 2020; title=MYSOLINE (PRIMIDONE) TABLET [BAUSCH HEALTH US, LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=af593171-dabb-4ea3-b44c-89ed457b2c46
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=af593171-dabb-4ea3-b44c-89ed457b2c46; effective_time=20200706; title=Mysoline / PRIMIDONE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22af593171-dabb-4ea3-b44c-89ed457b2c46%22&limit=5

### INFO fda_warning_metadata_refresh-eb7ca4da750a
- Kind: fda_warning_metadata_refresh
- Medication: progabide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [progabide; Gabrene].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [progabide; Gabrene].

### INFO fda_warning_metadata_refresh-d4db392dee3b
- Kind: fda_warning_metadata_refresh
- Medication: rufinamide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d; published=Nov 18, 2024; title=BANZEL (RUFINAMIDE) TABLET, FILM COATED BANZEL (RUFINAMIDE) SUSPENSION [EISAI INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=0a3fa925-1abd-458a-bd57-4ae780a1ef2d; effective_time=20221215; title=Banzel / RUFINAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5

### INFO fda_warning_metadata_refresh-471c89f58df3
- Kind: fda_warning_metadata_refresh
- Medication: stiripentol
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58304ba8-9779-4658-811e-94ffe08c3f16; published=Apr 30, 2026; title=DIACOMIT (STIRIPENTOL) CAPSULE DIACOMIT (STIRIPENTOL) POWDER, FOR SUSPENSION [BIOCODEX, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58304ba8-9779-4658-811e-94ffe08c3f16
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=58304ba8-9779-4658-811e-94ffe08c3f16; effective_time=20260427; title=Diacomit / STIRIPENTOL; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5

### INFO fda_warning_metadata_refresh-a687d0ef66a8
- Kind: fda_warning_metadata_refresh
- Medication: sultiame
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [sultiame; sulthiame; Ospolot].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [sultiame; sulthiame; Ospolot].

### INFO fda_warning_metadata_refresh-3a3fc9d51d4d
- Kind: fda_warning_metadata_refresh
- Medication: tiagabine
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22tiagabine%22+OR+openfda.brand_name%3A%22tiagabine%22+OR+openfda.substance_name%3A%22tiagabine%22&limit=10
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=72b7f357-8827-4a8b-b55a-01fbce47ae80; published=Aug 08, 2016; title=GABITRIL (TIAGABINE HYDROCHLORIDE) TABLET, FILM COATED [CARILION MATERIALS MANAGEMENT]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=72b7f357-8827-4a8b-b55a-01fbce47ae80
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=953ef3cc-e3cb-480f-b9ea-256520fd62b8; effective_time=20210930; title=Tiagabine Hydrochloride / TIAGABINE HYDROCHLORIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22tiagabine%22+OR+openfda.brand_name%3A%22tiagabine%22+OR+openfda.substance_name%3A%22tiagabine%22&limit=10

### INFO fda_warning_metadata_refresh-b2e5f394b9ec
- Kind: fda_warning_metadata_refresh
- Medication: topiramate
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=e2a4df59-fead-4a01-9021-9eda02c48010; published=Mar 23, 2026; title=EPRONTIA (TOPIRAMATE) SOLUTION [AZURITY PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e2a4df59-fead-4a01-9021-9eda02c48010
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=e2a4df59-fead-4a01-9021-9eda02c48010; effective_time=20251113; title=Eprontia / TOPIRAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5

### INFO fda_warning_metadata_refresh-ae7a49794db6
- Kind: fda_warning_metadata_refresh
- Medication: trimethadione
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://open.fda.gov/apis/drug/label/
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed search on 05-19-2026: no current label found for terms [trimethadione; Tridione].
- Proposed: FDA/openFDA label API search on 05-19-2026: no current FDA label found for terms [trimethadione; Tridione].

### INFO fda_warning_metadata_refresh-0e998fe32ba1
- Kind: fda_warning_metadata_refresh
- Medication: valproic acid
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=0dc024ce-efc8-4690-7cb5-639c728fccac; published=Apr 13, 2026; title=DEPAKOTE ER (DIVALPROEX SODIUM) TABLET, EXTENDED RELEASE [ABBVIE INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0dc024ce-efc8-4690-7cb5-639c728fccac
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=0dc024ce-efc8-4690-7cb5-639c728fccac; effective_time=20260331; title=Depakote ER / DIVALPROEX SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5

### INFO fda_warning_metadata_refresh-f7d2b9137d94
- Kind: fda_warning_metadata_refresh
- Medication: vigabatrin
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a88ac1b4-e2c9-45c0-b321-4785902172e3%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=a88ac1b4-e2c9-45c0-b321-4785902172e3; published=Dec 17, 2025; title=SABRIL (VIGABATRIN) POWDER, FOR SOLUTION [LUNDBECK PHARMACEUTICALS LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a88ac1b4-e2c9-45c0-b321-4785902172e3
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=a88ac1b4-e2c9-45c0-b321-4785902172e3; effective_time=20211020; title=SABRIL / VIGABATRIN; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a88ac1b4-e2c9-45c0-b321-4785902172e3%22&limit=5

### INFO fda_warning_metadata_refresh-2b721838cbdc
- Kind: fda_warning_metadata_refresh
- Medication: zonisamide
- Source: FDA/openFDA
- Column: fda_black_box_warning_source
- Apply: safe=True; approval_required=False
- Evidence: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d12de43e-3ac3-4335-bc85-70d7366a91eb%22&limit=5
- Summary: FDA boxed-warning text matches current CSV or only the source wording changed; FDA/openFDA metadata can be refreshed.
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=d12de43e-3ac3-4335-bc85-70d7366a91eb; published=Oct 03, 2025; title=ZONEGRAN (ZONISAMIDE) CAPSULE [ADVANZ PHARMA (US) CORP.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d12de43e-3ac3-4335-bc85-70d7366a91eb
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=d12de43e-3ac3-4335-bc85-70d7366a91eb; effective_time=20250912; title=Zonegran / ZONISAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d12de43e-3ac3-4335-bc85-70d7366a91eb%22&limit=5
