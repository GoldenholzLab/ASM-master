# Agentic update_check summary

Generated: 2026-05-20

Rows audited: 51
Findings: 1231

## HIGH acetazolamide / fact_check
- Field: trade_names
- Status: incorrect
- Approval required: False
- Summary: Current value omits DIAMOX SEQUELS, the FDA-labeled extended-release capsule brand. Existing generic product names are not contradicted, so retain and append the missing brand.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf
- Current: Acetazolamide; Acetazolamide Sodium; Diamox
- Proposed: Acetazolamide; Acetazolamide Sodium; Diamox; Diamox Sequels

## HIGH acetazolamide / fact_check
- Field: pubmed_search_aliases
- Status: incorrect
- Approval required: False
- Summary: Add Diamox Sequels so the branded extended-release capsule alias is searchable.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: Diamox; acetazolamide sodium
- Proposed: Diamox; Diamox Sequels; acetazolamide sodium

## CRITICAL acetazolamide / fact_check
- Field: filter_formulation
- Status: incorrect
- Approval required: True
- Summary: FDA labeling says the injection is for intravenous use and intramuscular administration is not recommended.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf
- Current: Capsule; IV/IM injection; Long acting; Tablet
- Proposed: Capsule; IV injection; Long acting; Tablet

## HIGH acetazolamide / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: Mechanism can be supported by FDA label PDFs; remove DailyMed from the named source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA Drugs@FDA/accessdata labeling

## HIGH acetazolamide / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: False
- Summary: The field should not remain N/A when trusted NCBI sources provide half-life values. The current statement is only true for the selected FDA label, not for the fact field overall.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK532282/; https://www.ncbi.nlm.nih.gov/books/NBK2597/
- Current: N/A - selected FDA/DailyMed label does not provide a half-life value.
- Proposed: 6-14 hours; reported values vary by trusted NCBI sources, with StatPearls listing plasma half-life 6-9 hours and an NCBI Bookshelf epilepsy text listing elimination half-life 12-14 hours.

## HIGH acetazolamide / fact_check
- Field: major_organ_for_metabolism
- Status: incorrect
- Approval required: False
- Summary: NCBI sources state acetazolamide does not undergo metabolic alteration and is renally excreted.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK532282/; https://www.ncbi.nlm.nih.gov/books/NBK2597/
- Current: N/A - selected FDA/DailyMed label does not identify a major metabolic organ; renal bicarbonate handling and urinary effects are clinically central.
- Proposed: No major metabolism; renal excretion is the primary route of elimination.

## MEDIUM acetazolamide / fact_check
- Field: qt_interval_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: FDA labels reviewed do not describe QT effects, but label silence is not strong evidence for 'no known meaningful QT effect'.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf
- Current: No QT interval effect described in selected FDA label.
- Proposed: No QT-related warning or effect identified in selected FDA labeling; absence of label language does not establish a proven no-effect finding.

## MEDIUM acetazolamide / fact_check
- Field: filter_qt_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: The stronger 'no known meaningful QT effect' claim is not directly established by the cited FDA label; a label-limited statement is supportable.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf
- Current: No known meaningful QT effect
- Proposed: No QT-related warning/effect identified in selected FDA labeling

## HIGH acetazolamide / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should be removed from the named row sources, and NCBI/PubMed should be added for half-life/metabolism and RCT-gap support.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK532282/; https://pubmed.ncbi.nlm.nih.gov/6797857/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book data files; FDA Drugs@FDA/accessdata labeling; NCBI Bookshelf; PubMed

## HIGH acetazolamide / fact_check
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: Conclusion is supported by FDA label PDFs, but the current wording relies on DailyMed, which is not permissible for this field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA labeling.

## HIGH acetazolamide / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: Replace the impermissible DailyMed SPL source with FDA label sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58093032-8480-4d0f-82be-92e643bdbea4; published=Jan 16, 2026; title=ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) INJECTION, POWDER, FOR SOLUTION [SAGENT PHARMACEUTICALS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58093032-8480-4d0f-82be-92e643bdbea4
- Proposed: FDA Drugs@FDA/accessdata labels; status=no_boxed_warning_identified_in_selected_fda_labels; checked labels: DIAMOX tablets NDA 008943/S-054 (2025), DIAMOX tablets/injection NDA 008943/S-053 and NDA 009388/S-039 (2024), DIAMOX SEQUELS NDA 012945/S-048 (2024); urls=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf | https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf | https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf

## INFO acetazolamide / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot value appropriately remains blank because the corresponding outcome is N/A.

## INFO acetazolamide / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot value appropriately remains blank because the corresponding outcome is N/A.

## INFO acetazolamide / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot value appropriately remains blank because the corresponding outcome is N/A.

## HIGH acetazolamide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supportable from FDA label PDFs that show ordinary WARNINGS sections but no BOXED WARNING section. The current value/source is not compliant because it cites DailyMed for the FDA boxed-warning field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA labeling.

## MEDIUM acetazolamide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: DailyMed should not be used as a named source in this audit bundle, and the row needs NCBI/PubMed sources for non-label facts and RCT-gap verification.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK532282/; https://pubmed.ncbi.nlm.nih.gov/6797857/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book data files; FDA Drugs@FDA/accessdata labeling; NCBI Bookshelf; PubMed

## MEDIUM acetazolamide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism text is supported by FDA label PDFs.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA Drugs@FDA/accessdata labeling

## MEDIUM acetazolamide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box source must be FDA/openFDA/Drugs@FDA, not DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58093032-8480-4d0f-82be-92e643bdbea4; published=Jan 16, 2026; title=ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) INJECTION, POWDER, FOR SOLUTION [SAGENT PHARMACEUTICALS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58093032-8480-4d0f-82be-92e643bdbea4
- Proposed: FDA Drugs@FDA/accessdata labels; status=no_boxed_warning_identified_in_selected_fda_labels; checked labels: DIAMOX tablets NDA 008943/S-054 (2025), DIAMOX tablets/injection NDA 008943/S-053 and NDA 009388/S-039 (2024), DIAMOX SEQUELS NDA 012945/S-048 (2024); urls=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf | https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf | https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf

## MEDIUM acetazolamide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Remove DailyMed from row source naming and add trusted sources used for half-life/metabolism and RCT-gap verification.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK532282/; https://pubmed.ncbi.nlm.nih.gov/6797857/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book data files; FDA Drugs@FDA/accessdata labeling; NCBI Bookshelf; PubMed

## MEDIUM acetazolamide / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Black-box verification must use FDA sources, not DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA labeling.

## MEDIUM acetazolamide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace impermissible DailyMed source with FDA label sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58093032-8480-4d0f-82be-92e643bdbea4; published=Jan 16, 2026; title=ACETAZOLAMIDE (ACETAZOLAMIDE SODIUM) INJECTION, POWDER, FOR SOLUTION [SAGENT PHARMACEUTICALS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58093032-8480-4d0f-82be-92e643bdbea4
- Proposed: FDA Drugs@FDA/accessdata labels; status=no_boxed_warning_identified_in_selected_fda_labels; checked labels: DIAMOX tablets NDA 008943/S-054 (2025), DIAMOX tablets/injection NDA 008943/S-053 and NDA 009388/S-039 (2024), DIAMOX SEQUELS NDA 012945/S-048 (2024); urls=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf | https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf | https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf

## MEDIUM acetazolamide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supportable from FDA labeling; DailyMed is unnecessary and outside the trusted source list supplied for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA Drugs@FDA/accessdata labeling

## MEDIUM acetazolamide / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: Trusted NCBI sources provide half-life values; the row should not leave the pharmacokinetic field as N/A solely because the selected label omits it.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK532282/; https://www.ncbi.nlm.nih.gov/books/NBK2597/
- Current: N/A - selected FDA/DailyMed label does not provide a half-life value.
- Proposed: 6-14 hours; reported values vary by trusted NCBI sources, with StatPearls listing plasma half-life 6-9 hours and an NCBI Bookshelf epilepsy text listing elimination half-life 12-14 hours.

## MEDIUM acetazolamide / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: False
- Summary: NCBI sources state acetazolamide does not undergo metabolic alteration and is primarily renally eliminated.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK532282/; https://www.ncbi.nlm.nih.gov/books/NBK2597/
- Current: N/A - selected FDA/DailyMed label does not identify a major metabolic organ; renal bicarbonate handling and urinary effects are clinically central.
- Proposed: No major metabolism; renal excretion is the primary route of elimination.

## MEDIUM acetazolamide / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Add the missing FDA-labeled Diamox Sequels brand alias without deleting existing names.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: Acetazolamide; Acetazolamide Sodium; Diamox
- Proposed: Acetazolamide; Acetazolamide Sodium; Diamox; Diamox Sequels

## MEDIUM acetazolamide / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add the missing extended-release capsule brand alias for search coverage.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/012945s048lbl.pdf
- Current: Diamox; acetazolamide sodium
- Proposed: Diamox; Diamox Sequels; acetazolamide sodium

## CRITICAL acetazolamide / proposed_row_update
- Field: filter_formulation
- Status: proposed
- Approval required: True
- Summary: FDA labeling identifies the injection for intravenous use and says intramuscular administration is not recommended.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf
- Current: Capsule; IV/IM injection; Long acting; Tablet
- Proposed: Capsule; IV injection; Long acting; Tablet

## MEDIUM acetazolamide / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: False
- Summary: Clarify that the evidence is label silence, not affirmative QT safety evidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/008943s054lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008943s053%2C009388s039lbl.pdf
- Current: No QT interval effect described in selected FDA label.
- Proposed: No QT-related warning or effect identified in selected FDA labeling; absence of label language does not establish a proven no-effect finding.

## MEDIUM acetazolamide / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Refresh audit date and retain the N/A conclusion.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6797857/; https://www.ncbi.nlm.nih.gov/books/NBK581157/
- Current: No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-19-2026; RCT section set to N/A per current scope.
- Proposed: No qualifying phase II/III placebo-controlled randomized epilepsy RCT was found/retained in the PubMed RCT audit/gap review as of 05-20-2026; RCT section remains N/A.

## HIGH barbexaclone / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: A starting titration dose is not the same as an evidence-based minimum effective dose, so the cell should be worded more cautiously.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: Swiss Fachinformation: adult titration begins at 100 mg/day; children may titrate slowly using 25 mg tablets.
- Proposed: No explicit minimum effective dose stated; Swiss Fachinformation dosing starts adults at 100 mg/day and titrates every 2 days to 1 week; children may be titrated slowly using 25 mg dragees/tablets.

## HIGH barbexaclone / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The cited mechanism source is a Swiss Fachinformation page via ODDB, not an EMA EPAR, EMA SmPC, or UK eMC/SmPC.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: EMA/UK SmPC
- Proposed: Swiss Fachinformation / non-U.S. product information (not EMA/UK SmPC)

## HIGH barbexaclone / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: The Swiss source supports the frequency categories and listed events, but the row's phrase '0% exact percentage unavailable' is inaccurate because unestimable frequency is not 0%. The proposed text also captures additional listed events and avoids overstating exact percentages.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: Swiss Fachinformation frequency categories: frequent 1-10% not itemized for all symptoms; occasional 0.1-1% calcium metabolism disorder and weight loss; rare 0.01-0.1% aplastic/megaloblastic anemia, pancytopenia, thrombocytopenia, leukopenia, agranulocytosis, allergic/respiratory hypersensitivity, hallucinations, hemorrhage, constipation, vomiting, gingival hyperplasia, SJS/TEN, exfoliative dermatitis, rash; frequency not reliably estimable 0% exact percentage unavailable for somnolence, ataxia, nystagmus, dizziness, respiratory depression, fatigue.
- Proposed: Swiss Fachinformation frequency categories: frequent >1/100 to <=1/10, occasional >1/1000 to <=1/100, rare >1/10000 to <=1/1000. Occasional: calcium metabolism disorders, weight loss. Rare: aplastic anemia, megaloblastic anemia, pancytopenia, thrombocytopenia, leukopenia, agranulocytosis, allergic reactions/skin and respiratory hypersensitivity, systemic lupus erythematosus, optical hallucinations, hemorrhage, constipation, vomiting, gingival hyperplasia, erythema multiforme, Stevens-Johnson syndrome, Lyell syndrome/TEN, exfoliative dermatitis, nonspecific drug rash, photosensitization, urticaria. Frequency not reliably estimable: restlessness, drowsiness, ataxia, nystagmus, dizziness, respiratory depression, hepatitis, jaundice, increased GGT, irritability, fatigue, high fever.

## MEDIUM barbexaclone / fact_check
- Field: qt_interval_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: The Swiss source supports the cardiac contraindications/cautions. Absence of QT wording in the source should not be treated as evidence of no QT effect.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: No QT interval effect described in Swiss Fachinformation; contraindications/cautions include tachyarrhythmias, severe angina, severe myocardial damage.
- Proposed: QT effect not characterized in located product information; Swiss Fachinformation does not describe a QT-interval effect but lists contraindications/cautions including tachyarrhythmias, severe angina pectoris, and severe myocardial damage.

## MEDIUM barbexaclone / fact_check
- Field: pubmed_search_aliases
- Status: missing_source
- Approval required: False
- Summary: PubChem lists additional aliases and MeSH entry terms that are useful for avoiding duplicate rows and improving literature searches.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Barbexaclone
- Current: barbesaclone; barbexaclonum; Maliasin
- Proposed: barbesaclone; barbexaclonum; barbexaclon; barbexaclona; Maliasin; CHP phenobarbital; phenobarbital propylhexedrine salt

## HIGH barbexaclone / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be used for the boxed-warning field. The row also needs named sources for aliases and RCT-gap claims. Note that ch.oddb.org/AIFA are outside the provided trusted-domain list, although they do support the row's non-U.S. source claims.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862; https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf; https://www.aifa.gov.it/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-; https://www.aifa.gov.it/en/ricerca-aifa?adtCategories=811507&searchKeywords=; https://pubchem.ncbi.nlm.nih.gov/compound/Barbexaclone; https://pubmed.ncbi.nlm.nih.gov/14606/; https://pubmed.ncbi.nlm.nih.gov/3709618/; https://pubmed.ncbi.nlm.nih.gov/23981808/; https://www.ilae.org/files/ilaeGuideline/Guidelines.pdf; https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/
- Current: Swiss Maliasin Fachinformation Swissmedic no. 31862 (https://ch.oddb.org/de/gcc/fachinfo/reg/31862); Swissmedic Journal 07/2006 Maliasin authorization entry (https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf); AIFA Barbesaclone distribution communication (https://www.aifa.gov.it/en/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-); FDA/DailyMed labeling
- Proposed: Swiss Maliasin Fachinformation Swissmedic no. 31862 (https://ch.oddb.org/de/gcc/fachinfo/reg/31862); Swissmedic Journal 07/2006 Maliasin authorization entry (https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf); AIFA Barbesaclone distribution/access communications, including 22-05-2014 and current AIFA search results (https://www.aifa.gov.it/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-; https://www.aifa.gov.it/en/ricerca-aifa?adtCategories=811507&searchKeywords=); PubChem Barbexaclone identity/aliases (https://pubchem.ncbi.nlm.nih.gov/compound/Barbexaclone); PubMed records PMID 14606, 3709618, 23981808; ILAE evidence review (https://www.ilae.org/files/ilaeGuideline/Guidelines.pdf); FDA/openFDA/Drugs@FDA searches for FDA label/applica

## HIGH barbexaclone / fact_check
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for the black-box field. The replacement keeps the no-FDA-label conclusion but ties it to FDA/openFDA/Drugs@FDA only.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/; https://open.fda.gov/apis/drug/drugsfda/how-to-use-the-endpoint/
- Current: No current FDA/DailyMed label identified.
- Proposed: N/A - no FDA-approved labeling or FDA boxed warning identified for barbexaclone/barbesaclone/barbexaclonum/Maliasin.

## HIGH barbexaclone / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is impermissible for this field under the audit instructions.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/; https://open.fda.gov/apis/drug/drugsfda/how-to-use-the-endpoint/
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [barbexaclone; barbesaclone; barbexaclonum; Maliasin].
- Proposed: FDA/openFDA/Drugs@FDA searches on 05-20-2026 for terms [barbexaclone; barbesaclone; barbexaclonum; Maliasin]: no FDA-approved label/application or boxed warning identified. DailyMed was not used for boxed-warning verification.

## HIGH barbexaclone / fact_check
- Field: status_or_notes
- Status: incorrect
- Approval required: False
- Summary: The Swiss statements are supported. AIFA search results show later 2025-2026 Barbesaclone notices, so characterizing the Italian documentation only as historical is incomplete.
- Sources: https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf; https://ch.oddb.org/de/gcc/fachinfo/reg/31862; https://www.aifa.gov.it/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-; https://www.aifa.gov.it/en/ricerca-aifa?adtCategories=811507&searchKeywords=
- Current: Historical European/Swiss/Italian ASM product; Swissmedic Journal lists Maliasin 25 mg/100 mg (barbexaclonum) as an antiepileptic under authorization no. 31862, Swiss Maliasin Fachinformation lists multiple epilepsy indications, and AIFA communications document Barbesaclone 25 mg/100 mg coated-tablet distribution access.
- Proposed: Non-U.S. ASM product: historical Swiss Maliasin authorization no. 31862 for 25 mg/100 mg dragees (barbexaclonum) as an antiepileptic; Swiss Fachinformation lists multiple epilepsy indications; AIFA documents Barbesaclone 25 mg/100 mg coated-tablet access/distribution, with later AIFA search results showing ongoing 2025-2026 Barbesaclone distribution/expiry-extension notices.

## HIGH barbexaclone / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The conclusion is plausible, but the row's wording cites DailyMed for a boxed-warning field; the audit policy permits FDA/openFDA/Drugs@FDA sources only for this field.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/; https://open.fda.gov/apis/drug/drugsfda/how-to-use-the-endpoint/; https://api.fda.gov/drug/label.json?search=%22barbexaclone%22&limit=1; https://api.fda.gov/drug/label.json?search=%22barbesaclone%22&limit=1; https://api.fda.gov/drug/label.json?search=%22barbexaclonum%22&limit=1; https://api.fda.gov/drug/label.json?search=%22Maliasin%22&limit=1
- Current: No current FDA/DailyMed label identified.
- Proposed: N/A - no FDA-approved labeling or FDA boxed warning identified for barbexaclone/barbesaclone/barbexaclonum/Maliasin.

## MEDIUM barbexaclone / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Remove DailyMed for black-box verification and add named sources for alias, RCT-gap, FDA-status, and current AIFA context.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Barbexaclone; https://pubmed.ncbi.nlm.nih.gov/14606/; https://pubmed.ncbi.nlm.nih.gov/3709618/; https://pubmed.ncbi.nlm.nih.gov/23981808/; https://www.ilae.org/files/ilaeGuideline/Guidelines.pdf; https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/
- Current: Swiss Maliasin Fachinformation Swissmedic no. 31862 (https://ch.oddb.org/de/gcc/fachinfo/reg/31862); Swissmedic Journal 07/2006 Maliasin authorization entry (https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf); AIFA Barbesaclone distribution communication (https://www.aifa.gov.it/en/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-); FDA/DailyMed labeling
- Proposed: Swiss Maliasin Fachinformation Swissmedic no. 31862 (https://ch.oddb.org/de/gcc/fachinfo/reg/31862); Swissmedic Journal 07/2006 Maliasin authorization entry (https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf); AIFA Barbesaclone distribution/access communications, including 22-05-2014 and current AIFA search results (https://www.aifa.gov.it/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-; https://www.aifa.gov.it/en/ricerca-aifa?adtCategories=811507&searchKeywords=); PubChem Barbexaclone identity/aliases (https://pubchem.ncbi.nlm.nih.gov/compound/Barbexaclone); PubMed records PMID 14606, 3709618, 23981808; ILAE evidence review (https://www.ilae.org/files/ilaeGuideline/Guidelines.pdf); FDA/openFDA/Drugs@FDA searches for FDA label/applica

## MEDIUM barbexaclone / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permitted for this field.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/; https://open.fda.gov/apis/drug/drugsfda/how-to-use-the-endpoint/
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [barbexaclone; barbesaclone; barbexaclonum; Maliasin].
- Proposed: FDA/openFDA/Drugs@FDA searches on 05-20-2026 for terms [barbexaclone; barbesaclone; barbexaclonum; Maliasin]: no FDA-approved label/application or boxed warning identified. DailyMed was not used for boxed-warning verification.

## MEDIUM barbexaclone / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: The cited source is not EMA or UK eMC/SmPC.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: EMA/UK SmPC
- Proposed: Swiss Fachinformation / non-U.S. product information (not EMA/UK SmPC)

## MEDIUM barbexaclone / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Remove misleading '0%' wording and align event list more closely to Swiss product information.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: Swiss Fachinformation frequency categories: frequent 1-10% not itemized for all symptoms; occasional 0.1-1% calcium metabolism disorder and weight loss; rare 0.01-0.1% aplastic/megaloblastic anemia, pancytopenia, thrombocytopenia, leukopenia, agranulocytosis, allergic/respiratory hypersensitivity, hallucinations, hemorrhage, constipation, vomiting, gingival hyperplasia, SJS/TEN, exfoliative dermatitis, rash; frequency not reliably estimable 0% exact percentage unavailable for somnolence, ataxia, nystagmus, dizziness, respiratory depression, fatigue.
- Proposed: Swiss Fachinformation frequency categories: frequent >1/100 to <=1/10, occasional >1/1000 to <=1/100, rare >1/10000 to <=1/1000. Occasional: calcium metabolism disorders, weight loss. Rare: aplastic anemia, megaloblastic anemia, pancytopenia, thrombocytopenia, leukopenia, agranulocytosis, allergic reactions/skin and respiratory hypersensitivity, systemic lupus erythematosus, optical hallucinations, hemorrhage, constipation, vomiting, gingival hyperplasia, erythema multiforme, Stevens-Johnson syndrome, Lyell syndrome/TEN, exfoliative dermatitis, nonspecific drug rash, photosensitization, urticaria. Frequency not reliably estimable: restlessness, drowsiness, ataxia, nystagmus, dizziness, respiratory depression, hepatitis, jaundice, increased GGT, irritability, fatigue, high fever.

## MEDIUM barbexaclone / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Add additional PubChem-listed aliases to prevent duplicate-row treatment of language variants.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Barbexaclone; https://www.aifa.gov.it/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-
- Current: barbesaclone; barbexaclonum
- Proposed: barbesaclone; barbexaclonum; barbexaclon; barbexaclona

## MEDIUM barbexaclone / proposed_row_update
- Field: available_in_us
- Status: proposed
- Approval required: False
- Summary: Use FDA approval terminology and avoid implying the non-U.S. Italian context is only historical.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/; https://www.aifa.gov.it/en/ricerca-aifa?adtCategories=811507&searchKeywords=
- Current: No - not available in U.S. for seizure control; historical Swiss/Italian European documentation identified.
- Proposed: No - no FDA-approved U.S. label/application identified; non-U.S. Swiss and Italian product/access documentation identified.

## MEDIUM barbexaclone / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is impermissible for boxed-warning verification; use FDA/openFDA/Drugs@FDA only.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/; https://open.fda.gov/apis/drug/drugsfda/how-to-use-the-endpoint/
- Current: No current FDA/DailyMed label identified.
- Proposed: N/A - no FDA-approved labeling or FDA boxed warning identified for barbexaclone/barbesaclone/barbexaclonum/Maliasin.

## MEDIUM barbexaclone / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Complies with FDA-only black-box source policy.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://open.fda.gov/apis/drug/label/example-api-queries/; https://open.fda.gov/apis/drug/drugsfda/how-to-use-the-endpoint/
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [barbexaclone; barbesaclone; barbexaclonum; Maliasin].
- Proposed: FDA/openFDA/Drugs@FDA searches on 05-20-2026 for terms [barbexaclone; barbesaclone; barbexaclonum; Maliasin]: no FDA-approved label/application or boxed warning identified. DailyMed was not used for boxed-warning verification.

## MEDIUM barbexaclone / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: The cited mechanism source is Swiss product information via ODDB, not EMA or UK eMC.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: EMA/UK SmPC
- Proposed: Swiss Fachinformation / non-U.S. product information (not EMA/UK SmPC)

## MEDIUM barbexaclone / proposed_row_update
- Field: minimum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Starting titration dose is not necessarily the minimum effective dose.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: Swiss Fachinformation: adult titration begins at 100 mg/day; children may titrate slowly using 25 mg tablets.
- Proposed: No explicit minimum effective dose stated; Swiss Fachinformation dosing starts adults at 100 mg/day and titrates every 2 days to 1 week; children may be titrated slowly using 25 mg dragees/tablets.

## MEDIUM barbexaclone / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: False
- Summary: Absence of QT language in the product information is not proof of no QT effect.
- Sources: https://ch.oddb.org/de/gcc/fachinfo/reg/31862
- Current: No QT interval effect described in Swiss Fachinformation; contraindications/cautions include tachyarrhythmias, severe angina, severe myocardial damage.
- Proposed: QT effect not characterized in located product information; Swiss Fachinformation does not describe a QT-interval effect but lists contraindications/cautions including tachyarrhythmias, severe angina pectoris, and severe myocardial damage.

## MEDIUM barbexaclone / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add PubChem/MeSH aliases useful for PubMed and duplicate-row avoidance.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Barbexaclone
- Current: barbesaclone; barbexaclonum; Maliasin
- Proposed: barbesaclone; barbexaclonum; barbexaclon; barbexaclona; Maliasin; CHP phenobarbital; phenobarbital propylhexedrine salt

## MEDIUM barbexaclone / proposed_row_update
- Field: status_or_notes
- Status: proposed
- Approval required: False
- Summary: AIFA has later notices, including 2025-2026 search results, so the Italian access documentation is not merely historical.
- Sources: https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf; https://ch.oddb.org/de/gcc/fachinfo/reg/31862; https://www.aifa.gov.it/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-; https://www.aifa.gov.it/en/ricerca-aifa?adtCategories=811507&searchKeywords=
- Current: Historical European/Swiss/Italian ASM product; Swissmedic Journal lists Maliasin 25 mg/100 mg (barbexaclonum) as an antiepileptic under authorization no. 31862, Swiss Maliasin Fachinformation lists multiple epilepsy indications, and AIFA communications document Barbesaclone 25 mg/100 mg coated-tablet distribution access.
- Proposed: Non-U.S. ASM product: historical Swiss Maliasin authorization no. 31862 for 25 mg/100 mg dragees (barbexaclonum) as an antiepileptic; Swiss Fachinformation lists multiple epilepsy indications; AIFA documents Barbesaclone 25 mg/100 mg coated-tablet access/distribution, with later AIFA search results showing ongoing 2025-2026 Barbesaclone distribution/expiry-extension notices.

## MEDIUM barbexaclone / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: Use FDA approval terminology and keep non-U.S. authorization/access context separate.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://www.swissmedic.ch/dam/swissmedic/en/dokumente/stab/journal/swissmedic_journal072006.pdf.download.pdf/swissmedic_journal072006.pdf; https://www.aifa.gov.it/-/comunicazione-sul-medicinale-a-denominazione-generica-barbesaclone-25-mg-e-100-mg-compresse-rivestite-22-05-2014-
- Current: Not FDA-cleared; Swissmedic Journal documents Maliasin authorization no. 31862 as an antiepileptic, and AIFA Barbesaclone 25 mg/100 mg distribution communications are documented.
- Proposed: Not FDA-cleared/approved; no FDA label/application identified. Swissmedic Journal documents Maliasin authorization no. 31862 as an antiepileptic, and AIFA documents Barbesaclone coated-tablet access/distribution communications.

## HIGH brivaracetam / fact_check
- Field: pubmed_search_aliases
- Status: incorrect
- Approval required: False
- Summary: UCB 34714/UCB-34714 is an investigational-code alias for brivaracetam; adding the hyphenated form improves alias coverage without making it a separate drug row.
- Sources: https://pubmed.ncbi.nlm.nih.gov/18321235/; https://pmc.ncbi.nlm.nih.gov/articles/PMC7479692/
- Current: UCB 34714
- Proposed: UCB 34714; UCB-34714

## HIGH brivaracetam / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; DailyMed should not be the named source for this FDA-tier source field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling

## HIGH brivaracetam / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: FDA label supports weak CYP2C19 inhibition, epoxide hydrolase inhibition, and little/no CYP induction; current text omits epoxide hydrolase inhibition.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: Weak CYP2C19 inhibitor; not a broad enzyme inducer
- Proposed: Weak CYP2C19 inhibitor; reversible epoxide hydrolase inhibitor; unlikely to induce CYP enzymes in vivo

## CRITICAL brivaracetam / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: FDA label states brivaracetam is unlikely to induce CYP enzymes in vivo; retaining Inducer is directly contradicted.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: Inducer; Inhibitor
- Proposed: Inhibitor

## CRITICAL brivaracetam / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: True
- Summary: FDA label says brivaracetam is primarily eliminated by metabolism and less than 10% is excreted unchanged in urine; the current 'Renal/no major metabolism' wording is misleading/contradicted.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: Liver/hepatic; Plasma/extrahepatic; Renal/no major metabolism
- Proposed: Liver/hepatic; Plasma/extrahepatic; Renal excretion of metabolites

## HIGH brivaracetam / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for black-box verification. Use FDA/openFDA metadata instead.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=3cf2f439-0e97-443e-8e33-25ecef616f6c; published=May 14, 2026; title=BRIVIACT (BRIVARACETAM) TABLET, FILM COATED BRIVIACT (BRIVARACETAM) SOLUTION BRIVIACT (BRIVARACETAM) INJECTION, SUSPENSION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=3cf2f439-0e97-443e-8e33-25ecef616f6c; effective_time=20260513; title=Briviact / BRIVARACETAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5

## CRITICAL brivaracetam / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: True
- Summary: The row uses non-trusted/non-cited sources and DailyMed wording. The retained facts are supportable from trusted FDA, PubMed/NCBI, and ClinicalTrials.gov sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK548532/; https://www.ncbi.nlm.nih.gov/books/NBK447897/; https://clinicaltrials.gov/study/NCT04666610
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: NCBI LiverTox anticonvulsants table; FDA/Drugs@FDA labeling; FDA/openFDA labeling; PubMed/NCBI Bookshelf; ClinicalTrials.gov

## HIGH brivaracetam / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Current values are supported, but the Klein2015 200 mg/day median percent reduction differential is extractable from NCBI Bookshelf/CADTH data (35.6% active vs 17.6% placebo; table also reports 18.1% median difference). Adding it does not change the range.
- Sources: https://pubmed.ncbi.nlm.nih.gov/38576178/; https://pubmed.ncbi.nlm.nih.gov/26471380/; https://pubmed.ncbi.nlm.nih.gov/24446953/; https://pubmed.ncbi.nlm.nih.gov/24256083/; https://pubmed.ncbi.nlm.nih.gov/24116853/; https://pubmed.ncbi.nlm.nih.gov/22813235/; https://pubmed.ncbi.nlm.nih.gov/20592253/; https://www.ncbi.nlm.nih.gov/books/NBK447897/
- Current: 8-31.4 % (drug minus placebo MPC differential at maximum effective dose/regimen: Inoue2024 BRV 200 mg/day 25.4%; Biton2013 BRV 50 mg/day 12.7%; Ryvlin2013 BRV 100 mg/day 15.5%; Kwan2013 BRV flexible dose up to 150 mg/day 8%; VanPaesschen2012 BRV 150 mg/day 11.1%; French2010 BRV 50 mg/day 31.4%)
- Proposed: 8-31.4 % (drug minus placebo MPC differential at maximum effective dose/regimen: Inoue2024 BRV 200 mg/day 25.4%; Klein2015 BRV 200 mg/day 18.0%; Biton2013 BRV 50 mg/day 12.7%; Ryvlin2013 BRV 100 mg/day 15.5%; Kwan2013 BRV flexible dose up to 150 mg/day 8%; VanPaesschen2012 BRV 150 mg/day 11.1%; French2010 BRV 50 mg/day 31.4%)

## HIGH brivaracetam / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Current listed seizure-freedom entries are supported, but NCBI Bookshelf/CADTH outcome data support additional seizure-freedom differentials for Klein2015, Biton2013, and Kwan2013; including Kwan changes the range minimum to 1.5%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/42092987/; https://pubmed.ncbi.nlm.nih.gov/38576178/; https://pubmed.ncbi.nlm.nih.gov/26471380/; https://pubmed.ncbi.nlm.nih.gov/24446953/; https://pubmed.ncbi.nlm.nih.gov/24256083/; https://pubmed.ncbi.nlm.nih.gov/24116853/; https://pubmed.ncbi.nlm.nih.gov/22813235/; https://pubmed.ncbi.nlm.nih.gov/20592253/; https://www.ncbi.nlm.nih.gov/books/NBK447897/
- Current: 3.9-8.84 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Yu2026 BRV 200 mg/day 8.84%; Inoue2024 BRV 200 mg/day 6.8%; Ryvlin2013 BRV 100 mg/day 4%; VanPaesschen2012 BRV 150 mg/day 3.9%; French2010 BRV 50 mg/day 5.8%)
- Proposed: 1.5-8.84 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Yu2026 BRV 200 mg/day 8.84%; Inoue2024 BRV 200 mg/day 6.8%; Klein2015 BRV 200 mg/day 3.2%; Biton2013 BRV 50 mg/day 4.0%; Ryvlin2013 BRV 100 mg/day 4.0%; Kwan2013 BRV flexible dose up to 150 mg/day 1.5%; VanPaesschen2012 BRV 150 mg/day 3.9%; French2010 BRV 50 mg/day 5.8%)

## HIGH brivaracetam / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Add extractable Klein2015 MPC differential from NCBI Bookshelf/CADTH data.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26471380/; https://www.ncbi.nlm.nih.gov/books/NBK447897/
- Current: Inoue2024|25.4|https://pubmed.ncbi.nlm.nih.gov/38576178/|448; Ryvlin2013|15.5|https://pubmed.ncbi.nlm.nih.gov/24256083/|398; Kwan2013|8|https://pubmed.ncbi.nlm.nih.gov/24116853/|431; Biton2013|12.7|https://pubmed.ncbi.nlm.nih.gov/24446953/|396; VanPaesschen2012|11.1|https://pubmed.ncbi.nlm.nih.gov/22813235/|157; French2010|31.4|https://pubmed.ncbi.nlm.nih.gov/20592253/|208
- Proposed: Inoue2024|25.4|https://pubmed.ncbi.nlm.nih.gov/38576178/|448; Klein2015|18.0|https://pubmed.ncbi.nlm.nih.gov/26471380/|760; Ryvlin2013|15.5|https://pubmed.ncbi.nlm.nih.gov/24256083/|398; Kwan2013|8|https://pubmed.ncbi.nlm.nih.gov/24116853/|431; Biton2013|12.7|https://pubmed.ncbi.nlm.nih.gov/24446953/|396; VanPaesschen2012|11.1|https://pubmed.ncbi.nlm.nih.gov/22813235/|157; French2010|31.4|https://pubmed.ncbi.nlm.nih.gov/20592253/|208

## HIGH brivaracetam / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Add supported seizure-freedom differentials for Klein2015, Biton2013, and Kwan2013 from NCBI Bookshelf/CADTH outcome data.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26471380/; https://pubmed.ncbi.nlm.nih.gov/24446953/; https://pubmed.ncbi.nlm.nih.gov/24116853/; https://www.ncbi.nlm.nih.gov/books/NBK447897/
- Current: Yu2026|8.84|https://pubmed.ncbi.nlm.nih.gov/42092987/|178; Inoue2024|6.8|https://pubmed.ncbi.nlm.nih.gov/38576178/|448; Ryvlin2013|4|https://pubmed.ncbi.nlm.nih.gov/24256083/|398; VanPaesschen2012|3.9|https://pubmed.ncbi.nlm.nih.gov/22813235/|157; French2010|5.8|https://pubmed.ncbi.nlm.nih.gov/20592253/|208
- Proposed: Yu2026|8.84|https://pubmed.ncbi.nlm.nih.gov/42092987/|178; Inoue2024|6.8|https://pubmed.ncbi.nlm.nih.gov/38576178/|448; Klein2015|3.2|https://pubmed.ncbi.nlm.nih.gov/26471380/|760; Biton2013|4.0|https://pubmed.ncbi.nlm.nih.gov/24446953/|396; Ryvlin2013|4.0|https://pubmed.ncbi.nlm.nih.gov/24256083/|398; Kwan2013|1.5|https://pubmed.ncbi.nlm.nih.gov/24116853/|431; VanPaesschen2012|3.9|https://pubmed.ncbi.nlm.nih.gov/22813235/|157; French2010|5.8|https://pubmed.ncbi.nlm.nih.gov/20592253/|208

## HIGH brivaracetam / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supported by FDA/openFDA/FDA label sources, but the row's current wording and source rely on DailyMed, which is not permissible for this field.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM brivaracetam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box warning verification must use FDA/openFDA/Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=3cf2f439-0e97-443e-8e33-25ecef616f6c; published=May 14, 2026; title=BRIVIACT (BRIVARACETAM) TABLET, FILM COATED BRIVIACT (BRIVARACETAM) SOLUTION BRIVIACT (BRIVARACETAM) INJECTION, SUSPENSION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=3cf2f439-0e97-443e-8e33-25ecef616f6c; effective_time=20260513; title=Briviact / BRIVARACETAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5

## MEDIUM brivaracetam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism cell is supported by FDA label language.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling

## CRITICAL brivaracetam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: True
- Summary: Replace/augment unsupported source names with trusted sources that support row facts.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548532/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK447897/; https://clinicaltrials.gov/study/NCT04666610
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: NCBI LiverTox anticonvulsants table; FDA/Drugs@FDA labeling; FDA/openFDA labeling; PubMed/NCBI Bookshelf; ClinicalTrials.gov

## MEDIUM brivaracetam / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add hyphenated investigational-code alias variant.
- Sources: https://pubmed.ncbi.nlm.nih.gov/18321235/; https://pmc.ncbi.nlm.nih.gov/articles/PMC7479692/
- Current: UCB 34714
- Proposed: UCB 34714; UCB-34714

## MEDIUM brivaracetam / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for black-box verification; FDA/openFDA/FDA label support no boxed warning.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM brivaracetam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace impermissible DailyMed black-box source with FDA/openFDA source metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=3cf2f439-0e97-443e-8e33-25ecef616f6c; published=May 14, 2026; title=BRIVIACT (BRIVARACETAM) TABLET, FILM COATED BRIVIACT (BRIVARACETAM) SOLUTION BRIVIACT (BRIVARACETAM) INJECTION, SUSPENSION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3cf2f439-0e97-443e-8e33-25ecef616f6c
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=3cf2f439-0e97-443e-8e33-25ecef616f6c; effective_time=20260513; title=Briviact / BRIVARACETAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223cf2f439-0e97-443e-8e33-25ecef616f6c%22&limit=5

## MEDIUM brivaracetam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supported by FDA labeling; DailyMed is not needed as source text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling

## CRITICAL brivaracetam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: True
- Summary: Use trusted, row-supporting sources and avoid reliance on non-trusted/DailyMed source names.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548532/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK447897/; https://clinicaltrials.gov/study/NCT04666610
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: NCBI LiverTox anticonvulsants table; FDA/Drugs@FDA labeling; FDA/openFDA labeling; PubMed/NCBI Bookshelf; ClinicalTrials.gov

## MEDIUM brivaracetam / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: FDA label supports weak CYP2C19 inhibition, epoxide hydrolase inhibition, and lack of meaningful induction.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: Weak CYP2C19 inhibitor; not a broad enzyme inducer
- Proposed: Weak CYP2C19 inhibitor; reversible epoxide hydrolase inhibitor; unlikely to induce CYP enzymes in vivo

## CRITICAL brivaracetam / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: FDA label directly contradicts inducer classification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: Inducer; Inhibitor
- Proposed: Inhibitor

## CRITICAL brivaracetam / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: True
- Summary: FDA label says brivaracetam is primarily metabolized, with urinary excretion mainly as metabolites; unchanged renal excretion is less than 10%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/205836s017%2C205837s014%2C205838s015lbl.pdf
- Current: Liver/hepatic; Plasma/extrahepatic; Renal/no major metabolism
- Proposed: Liver/hepatic; Plasma/extrahepatic; Renal excretion of metabolites

## MEDIUM brivaracetam / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Add extractable Klein2015 median percent change differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26471380/; https://www.ncbi.nlm.nih.gov/books/NBK447897/
- Current: 8-31.4 % (drug minus placebo MPC differential at maximum effective dose/regimen: Inoue2024 BRV 200 mg/day 25.4%; Biton2013 BRV 50 mg/day 12.7%; Ryvlin2013 BRV 100 mg/day 15.5%; Kwan2013 BRV flexible dose up to 150 mg/day 8%; VanPaesschen2012 BRV 150 mg/day 11.1%; French2010 BRV 50 mg/day 31.4%)
- Proposed: 8-31.4 % (drug minus placebo MPC differential at maximum effective dose/regimen: Inoue2024 BRV 200 mg/day 25.4%; Klein2015 BRV 200 mg/day 18.0%; Biton2013 BRV 50 mg/day 12.7%; Ryvlin2013 BRV 100 mg/day 15.5%; Kwan2013 BRV flexible dose up to 150 mg/day 8%; VanPaesschen2012 BRV 150 mg/day 11.1%; French2010 BRV 50 mg/day 31.4%)

## MEDIUM brivaracetam / proposed_row_update
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Add Klein2015 plot value.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26471380/; https://www.ncbi.nlm.nih.gov/books/NBK447897/
- Current: Inoue2024|25.4|https://pubmed.ncbi.nlm.nih.gov/38576178/|448; Ryvlin2013|15.5|https://pubmed.ncbi.nlm.nih.gov/24256083/|398; Kwan2013|8|https://pubmed.ncbi.nlm.nih.gov/24116853/|431; Biton2013|12.7|https://pubmed.ncbi.nlm.nih.gov/24446953/|396; VanPaesschen2012|11.1|https://pubmed.ncbi.nlm.nih.gov/22813235/|157; French2010|31.4|https://pubmed.ncbi.nlm.nih.gov/20592253/|208
- Proposed: Inoue2024|25.4|https://pubmed.ncbi.nlm.nih.gov/38576178/|448; Klein2015|18.0|https://pubmed.ncbi.nlm.nih.gov/26471380/|760; Ryvlin2013|15.5|https://pubmed.ncbi.nlm.nih.gov/24256083/|398; Kwan2013|8|https://pubmed.ncbi.nlm.nih.gov/24116853/|431; Biton2013|12.7|https://pubmed.ncbi.nlm.nih.gov/24446953/|396; VanPaesschen2012|11.1|https://pubmed.ncbi.nlm.nih.gov/22813235/|157; French2010|31.4|https://pubmed.ncbi.nlm.nih.gov/20592253/|208

## MEDIUM brivaracetam / proposed_row_update
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Add extractable seizure-freedom differentials for Klein2015, Biton2013, and Kwan2013; update range.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26471380/; https://pubmed.ncbi.nlm.nih.gov/24446953/; https://pubmed.ncbi.nlm.nih.gov/24116853/; https://www.ncbi.nlm.nih.gov/books/NBK447897/
- Current: 3.9-8.84 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Yu2026 BRV 200 mg/day 8.84%; Inoue2024 BRV 200 mg/day 6.8%; Ryvlin2013 BRV 100 mg/day 4%; VanPaesschen2012 BRV 150 mg/day 3.9%; French2010 BRV 50 mg/day 5.8%)
- Proposed: 1.5-8.84 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Yu2026 BRV 200 mg/day 8.84%; Inoue2024 BRV 200 mg/day 6.8%; Klein2015 BRV 200 mg/day 3.2%; Biton2013 BRV 50 mg/day 4.0%; Ryvlin2013 BRV 100 mg/day 4.0%; Kwan2013 BRV flexible dose up to 150 mg/day 1.5%; VanPaesschen2012 BRV 150 mg/day 3.9%; French2010 BRV 50 mg/day 5.8%)

## MEDIUM brivaracetam / proposed_row_update
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Add supported seizure-freedom plot values.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26471380/; https://pubmed.ncbi.nlm.nih.gov/24446953/; https://pubmed.ncbi.nlm.nih.gov/24116853/; https://www.ncbi.nlm.nih.gov/books/NBK447897/
- Current: Yu2026|8.84|https://pubmed.ncbi.nlm.nih.gov/42092987/|178; Inoue2024|6.8|https://pubmed.ncbi.nlm.nih.gov/38576178/|448; Ryvlin2013|4|https://pubmed.ncbi.nlm.nih.gov/24256083/|398; VanPaesschen2012|3.9|https://pubmed.ncbi.nlm.nih.gov/22813235/|157; French2010|5.8|https://pubmed.ncbi.nlm.nih.gov/20592253/|208
- Proposed: Yu2026|8.84|https://pubmed.ncbi.nlm.nih.gov/42092987/|178; Inoue2024|6.8|https://pubmed.ncbi.nlm.nih.gov/38576178/|448; Klein2015|3.2|https://pubmed.ncbi.nlm.nih.gov/26471380/|760; Biton2013|4.0|https://pubmed.ncbi.nlm.nih.gov/24446953/|396; Ryvlin2013|4.0|https://pubmed.ncbi.nlm.nih.gov/24256083/|398; Kwan2013|1.5|https://pubmed.ncbi.nlm.nih.gov/24116853/|431; VanPaesschen2012|3.9|https://pubmed.ncbi.nlm.nih.gov/22813235/|157; French2010|5.8|https://pubmed.ncbi.nlm.nih.gov/20592253/|208

## MEDIUM brivaracetam / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Clarify which retained RCT links are outcome-bearing and prevent erroneous addition of secondary/background-drug publications.
- Sources: https://pubmed.ncbi.nlm.nih.gov/35844134/; https://pubmed.ncbi.nlm.nih.gov/26666500/; https://pubmed.ncbi.nlm.nih.gov/41175011/; https://pubmed.ncbi.nlm.nih.gov/35582748/; https://pubmed.ncbi.nlm.nih.gov/27988967/; https://pubmed.ncbi.nlm.nih.gov/27608437/
- Current: PubMed loop 5/65 on 2026-05-15: 10 qualifying placebo-controlled randomized clinical trial report(s) retained from 40 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Verified 2026-05-20: 10 listed links are brivaracetam phase II/III randomized placebo-controlled studies or design reports. Bast2022 is a phase 2/3 adaptive design publication without extractable efficacy-arm results; Kalviainen2015 reports EPM1 action-myoclonus outcomes rather than RR50/MPC/seizure-freedom outcomes. Secondary pooled/post hoc publications and the JNJ-40411813 trial with brivaracetam as background therapy should not be added as separate primary brivaracetam RCT rows.

## HIGH cannabidiol / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: CBD is verified. GWP42003-P is a recurring trial/intervention name in ClinicalTrials.gov records for cannabidiol and should be searchable to prevent missed RCTs.
- Sources: https://clinicaltrials.gov/study/NCT02091375; https://clinicaltrials.gov/study/NCT02224560; https://clinicaltrials.gov/study/NCT02224690; https://clinicaltrials.gov/study/NCT02544763
- Current: CBD
- Proposed: CBD; GWP42003-P

## MEDIUM cannabidiol / fact_check
- Field: half_life_range
- Status: missing_source
- Approval required: True
- Summary: FDA labeling supports terminal plasma half-life of 56-61 h. I did not find a trusted row-cited source supporting the effective half-life value of ~17 h.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: Effective ~17 h; terminal ~56-61 h
- Proposed: Terminal plasma half-life 56-61 h after twice-daily dosing for 7 days

## CRITICAL cannabidiol / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: FDA adverse-reaction tables for LGS/Dravet and TSC support the proposed ranges. The current row misses the TSC diarrhea and transaminase maxima and includes a somnolence maximum not supported by the selected FDA label tables.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: CNS: somnolence 23-32%, GI: decreased appetite 16-22%, GI: diarrhea 9-20%, hepatic: transaminase elevation 8-13%, constitutional: fatigue/malaise 11%
- Proposed: CNS: somnolence 13-25%, GI: decreased appetite 16-22%, GI: diarrhea 9-31%, hepatic: transaminases elevated 8-25%, constitutional: fatigue/malaise/asthenia 5-12%

## MEDIUM cannabidiol / fact_check
- Field: mechanism_of_action
- Status: missing_source
- Approval required: True
- Summary: FDA labeling supports the unknown mechanism and lack of apparent cannabinoid-receptor mediation. A trusted row-cited source was not found for the GPR55, TRPV1, and adenosine-mediated signaling claims.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: Precise human anticonvulsant mechanisms are unknown; effects do not appear to be mediated by CB1/CB2 cannabinoid receptors, with GPR55, TRPV1, and adenosine-mediated signaling proposed.
- Proposed: Precise human anticonvulsant mechanisms are unknown; cannabidiol does not appear to exert its anticonvulsant effects through interaction with cannabinoid receptors.

## CRITICAL cannabidiol / fact_check
- Field: qt_interval_effect
- Status: incorrect
- Approval required: True
- Summary: FDA labeling is more nuanced than the current text: it reports concentration-dependent QTc prolongation but no >10 ms QTc prolongation at recommended monotherapy exposures with a high-fat meal.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: No clinically meaningful QT prolongation established
- Proposed: Concentration-dependent QTc prolongation observed; at recommended monotherapy exposures with a high-fat meal, EPIDIOLEX did not prolong QTc by more than 10 ms; QTc effect at increased exposures from food, concomitant medications, or alcohol is unknown

## HIGH cannabidiol / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The current source list includes DailyMed and sources outside the trusted-domain list. FDA/openFDA/FDA label, NCBI, EMA, PubMed, and ClinicalTrials.gov sources support the retained row facts more directly.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK548890/; https://www.ema.europa.eu/en/medicines/human/EPAR/epidyolex
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary
- Proposed: FDA/openFDA or FDA-approved labeling for Epidiolex; NCBI LiverTox cannabidiol monograph; EMA Epidyolex EPAR; PubMed/ClinicalTrials.gov RCT records listed in pubmed_phase_ii_iii_rct_links

## HIGH cannabidiol / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The current source string includes DailyMed and AES; the FDA label directly supports only the narrower mechanism statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary
- Proposed: FDA-approved labeling for Epidiolex, section 12.1 Clinical Pharmacology / Mechanism of Action

## HIGH cannabidiol / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The retained mechanism should be sourced to FDA labeling only unless a trusted peer-reviewed source is added for the extra mechanistic hypotheses.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: FDA/AES summary
- Proposed: FDA labeling

## MEDIUM cannabidiol / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: insufficient_evidence
- Approval required: True
- Summary: Correct drug and placebo-controlled randomized transdermal cannabidiol focal-epilepsy trial, but PubMed did not clearly verify phase II/III classification, and no significant double-blind efficacy difference was reported.
- Sources: https://pubmed.ncbi.nlm.nih.gov/35802375/
- Current: https://pubmed.ncbi.nlm.nih.gov/35802375/
- Proposed: Retain pending row-policy review; do not use for RR50/MPC/seizure-freedom rollups.

## HIGH cannabidiol / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed metadata and the abstract describe a post hoc analysis of two randomized, placebo-controlled phase 3 cannabidiol trials in LGS. It is not an independent new trial and should be appended only if the CSV intentionally includes secondary/post hoc RCT reports.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33797076/
- Proposed: Privitera2021|https://pubmed.ncbi.nlm.nih.gov/33797076/

## HIGH cannabidiol / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supportable, but the row cites DailyMed for the boxed-warning field. The audit policy requires FDA/openFDA, FDA labels, or Drugs@FDA only for this field.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM cannabidiol / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box warning verification must use FDA/openFDA, FDA labels, or Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=8bf27097-4870-43fb-94f0-f3d0871d1eec; published=Nov 17, 2025; title=EPIDIOLEX (CANNABIDIOL) SOLUTION [JAZZ PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=8bf27097-4870-43fb-94f0-f3d0871d1eec; effective_time=20250731; title=Epidiolex / CANNABIDIOL; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5

## MEDIUM cannabidiol / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Current source does not support all mechanism text and includes non-preferred/non-trusted source naming.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary
- Proposed: FDA-approved labeling for Epidiolex, section 12.1 Clinical Pharmacology / Mechanism of Action

## MEDIUM cannabidiol / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use trusted domains and sources that directly support row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548890/; https://www.ema.europa.eu/en/medicines/human/EPAR/epidyolex; https://clinicaltrials.gov/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary
- Proposed: FDA/openFDA or FDA-approved labeling for Epidiolex; NCBI LiverTox cannabidiol monograph; EMA Epidyolex EPAR; PubMed/ClinicalTrials.gov RCT records listed in pubmed_phase_ii_iii_rct_links

## CRITICAL cannabidiol / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Align adverse-event ranges with FDA label Tables 3 and 4 across LGS/Dravet and TSC.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: CNS: somnolence 23-32%, GI: decreased appetite 16-22%, GI: diarrhea 9-20%, hepatic: transaminase elevation 8-13%, constitutional: fatigue/malaise 11%
- Proposed: CNS: somnolence 13-25%, GI: decreased appetite 16-22%, GI: diarrhea 9-31%, hepatic: transaminases elevated 8-25%, constitutional: fatigue/malaise/asthenia 5-12%

## MEDIUM cannabidiol / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permitted for FDA boxed-warning verification; use FDA/openFDA metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=8bf27097-4870-43fb-94f0-f3d0871d1eec; published=Nov 17, 2025; title=EPIDIOLEX (CANNABIDIOL) SOLUTION [JAZZ PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8bf27097-4870-43fb-94f0-f3d0871d1eec
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=8bf27097-4870-43fb-94f0-f3d0871d1eec; effective_time=20250731; title=Epidiolex / CANNABIDIOL; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5

## MEDIUM cannabidiol / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Same conclusion, corrected source language.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228bf27097-4870-43fb-94f0-f3d0871d1eec%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## CRITICAL cannabidiol / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: FDA label supports terminal half-life only; no trusted source was found for the effective half-life value.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: Effective ~17 h; terminal ~56-61 h
- Proposed: Terminal plasma half-life 56-61 h after twice-daily dosing for 7 days

## CRITICAL cannabidiol / proposed_row_update
- Field: mechanism_of_action
- Status: proposed
- Approval required: True
- Summary: FDA labeling supports the narrower statement; the additional mechanistic hypotheses lack a trusted row-cited source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: Precise human anticonvulsant mechanisms are unknown; effects do not appear to be mediated by CB1/CB2 cannabinoid receptors, with GPR55, TRPV1, and adenosine-mediated signaling proposed.
- Proposed: Precise human anticonvulsant mechanisms are unknown; cannabidiol does not appear to exert its anticonvulsant effects through interaction with cannabinoid receptors.

## MEDIUM cannabidiol / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism statement should cite a trusted source that directly supports it.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary
- Proposed: FDA-approved labeling for Epidiolex, section 12.1 Clinical Pharmacology / Mechanism of Action

## MEDIUM cannabidiol / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: AES summary was not verified from the trusted-domain list and is not needed for the FDA-supported mechanism statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: FDA/AES summary
- Proposed: FDA labeling

## CRITICAL cannabidiol / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: True
- Summary: FDA label supports a more nuanced QT statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: No clinically meaningful QT prolongation established
- Proposed: Concentration-dependent QTc prolongation observed; at recommended monotherapy exposures with a high-fat meal, EPIDIOLEX did not prolong QTc by more than 10 ms; QTc effect at increased exposures from food, concomitant medications, or alcohol is unknown

## MEDIUM cannabidiol / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: More closely matches FDA drug-interaction and pharmacokinetic wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf
- Current: Inhibits CYP2C19 and can inhibit CYP2C9/UGT pathways; affected by CYP3A4/CYP2C19 modulators
- Proposed: Substrate of CYP3A4/CYP2C19; inhibits CYP2C19 and may inhibit CYP2C9, UGT1A9, and UGT2B7; strong CYP3A4/CYP2C19 inducers reduce exposure

## MEDIUM cannabidiol / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: GWP42003-P is an important trial code/intervention name for cannabidiol in ClinicalTrials.gov records.
- Sources: https://clinicaltrials.gov/study/NCT02091375; https://clinicaltrials.gov/study/NCT02224560; https://clinicaltrials.gov/study/NCT02224690; https://clinicaltrials.gov/study/NCT02544763
- Current: CBD
- Proposed: CBD; GWP42003-P

## MEDIUM cannabidiol / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace non-trusted or non-specific row sources with trusted sources that directly support the populated facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210365s021lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548890/; https://www.ema.europa.eu/en/medicines/human/EPAR/epidyolex
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary
- Proposed: FDA/openFDA or FDA-approved labeling for Epidiolex; NCBI LiverTox cannabidiol monograph; EMA Epidyolex EPAR; PubMed/ClinicalTrials.gov RCT records listed in pubmed_phase_ii_iii_rct_links

## CRITICAL cannabidiol / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: Privitera2021 is a post hoc analysis of two randomized placebo-controlled phase 3 LGS cannabidiol trials; append only if secondary RCT analyses are within CSV scope.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33797076/
- Current: OBrien2022|https://pubmed.ncbi.nlm.nih.gov/35802375/; Thiele2021|https://pubmed.ncbi.nlm.nih.gov/33346789/; Miller2020|https://pubmed.ncbi.nlm.nih.gov/32119035/; Thiele2018|https://pubmed.ncbi.nlm.nih.gov/29395273/; Devinsky2018b|https://pubmed.ncbi.nlm.nih.gov/29768152/; Devinsky2018|https://pubmed.ncbi.nlm.nih.gov/29540584/; Devinsky2017|https://pubmed.ncbi.nlm.nih.gov/28538134/
- Proposed: OBrien2022|https://pubmed.ncbi.nlm.nih.gov/35802375/; Thiele2021|https://pubmed.ncbi.nlm.nih.gov/33346789/; Miller2020|https://pubmed.ncbi.nlm.nih.gov/32119035/; Thiele2018|https://pubmed.ncbi.nlm.nih.gov/29395273/; Devinsky2018b|https://pubmed.ncbi.nlm.nih.gov/29768152/; Devinsky2018|https://pubmed.ncbi.nlm.nih.gov/29540584/; Devinsky2017|https://pubmed.ncbi.nlm.nih.gov/28538134/; Privitera2021|https://pubmed.ncbi.nlm.nih.gov/33797076/

## MEDIUM carbamazepine / fact_check
- Field: trade_names
- Status: insufficient_evidence
- Approval required: False
- Summary: Carbatrol, Equetro, Tegretol/Tegretol XR, and Epitol are supported by FDA/NCBI sources. Curatil and Tegretol Prolonged Release were not verified from the available trusted-source evidence in this audit; no direct contradiction found, so no deletion is proposed.
- Sources: https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/information-carbamazepine-marketed-carbatrol-equetro-tegretol-and-generics; https://www.ncbi.nlm.nih.gov/books/NBK548097/
- Current: Carbatrol; Curatil; Epitol; Equetro; Tegretol; Tegretol Prolonged Release; Tegretol-XR
- Proposed: Carbatrol; Curatil; Epitol; Equetro; Tegretol; Tegretol Prolonged Release; Tegretol-XR

## HIGH carbamazepine / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: The empty alias field may miss common abbreviation/brand-title records. FDA/NCBI sources support the listed brand names; CBZ is a standard abbreviation used in PubMed-indexed carbamazepine literature.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548097/; https://pubmed.ncbi.nlm.nih.gov/15156070/
- Proposed: CBZ; Carbatrol; Tegretol; Tegretol-XR; Tegretol XR; Equetro; Epitol

## HIGH carbamazepine / fact_check
- Field: enzyme_inducing_or_inhibiting; filter_enzyme_effect
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports potent/strong CYP3A4 induction and induction of CYP1A2, 2B6, and 2C9/19. UGT induction and autoinduction are supported by peer-reviewed PubMed/PMC evidence; wording should avoid implying every listed pathway is classified as strong.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/31650711/; https://pubmed.ncbi.nlm.nih.gov/14709631/; https://pmc.ncbi.nlm.nih.gov/articles/PMC4865535/
- Current: Strong enzyme inducer: CYP3A4, CYP1A2, CYP2B6, CYP2C9, CYP2C19, UGT; autoinducer
- Proposed: Strong enzyme inducer: CYP3A4; inducer of CYP1A2, CYP2B6, CYP2C9/19 and UGT pathways; autoinducer

## HIGH carbamazepine / fact_check
- Field: adverse_symptoms_percentages; filter_symptom_category
- Status: incorrect
- Approval required: False
- Summary: The percentages match FDA Equetro pooled placebo-controlled bipolar-disorder trials. FDA term is somnolence, not drowsiness; the data are not epilepsy-trial-specific.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf
- Current: CNS: dizziness 44%, CNS: drowsiness 32%, GI: nausea 29%, GI: vomiting 18%, neurologic: ataxia 15%, dermatologic: rash 7%
- Proposed: CNS: dizziness 44%, CNS: somnolence/drowsiness 32%, neurologic: ataxia 15%, GI: nausea 29%, GI: vomiting 18%, dermatologic: rash 7%

## HIGH carbamazepine / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed should be replaced with FDA/accessdata for a trusted FDA label citation; the Sills/Rogawski PubMed record supports the sodium-channel mechanism.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; Sills and Rogawski 2020 ASM mechanism review (PMID 32120063)

## HIGH carbamazepine / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The FDA label supports mechanism uncertainty but not the full sodium-channel wording; the mechanistic classification relies on peer-reviewed review evidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: FDA label
- Proposed: FDA label + peer-reviewed review

## MEDIUM carbamazepine / fact_check
- Field: qt_interval_effect
- Status: missing_source
- Approval required: True
- Summary: FDA labeling supports AV heart block and overdose conduction disorders. The current QRS-specific wording and broad 'no typical QT prolongation' statement were not directly supported by the cited row sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf
- Current: No typical QT prolongation; can cause conduction abnormalities/AV block and QRS effects in toxicity
- Proposed: No FDA-label evidence of typical QT prolongation; conduction/arrhythmia caution including reported AV heart block and overdose conduction disorders.

## CRITICAL carbamazepine / fact_check
- Field: filter_qt_effect
- Status: incorrect
- Approval required: True
- Summary: The row's narrative QT field says no typical QT prolongation, and FDA labeling supports conduction/AV-block caution rather than a QT-prolongation classification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf
- Current: Conduction/arrhythmia caution; QT prolongation
- Proposed: Conduction/arrhythmia caution

## HIGH carbamazepine / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The named Epilepsy Society and Epilepsy Foundation Australia sources are outside the requested trusted domains, and DailyMed is not acceptable for black-box verification. The proposed sources are trusted and map to the checked facts.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548097/; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://pubmed.ncbi.nlm.nih.gov/15156070/; https://www.ncbi.nlm.nih.gov/books/n/niceng217er26/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling; NCBI LiverTox; Sills and Rogawski 2020 ASM mechanism review (PMID 32120063); PubMed RCT metadata (PMID 15156070); NCBI Bookshelf NICE epilepsy evidence review

## HIGH carbamazepine / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: This is a randomized double-blind withdrawal/neuropsychological study in well-controlled epilepsy; the abstract states medication choice was not randomized to placebo, and it is not a phase II/III placebo-controlled carbamazepine seizure-efficacy RCT for RR50/MPC/seizure-freedom extraction.
- Sources: https://pubmed.ncbi.nlm.nih.gov/20955400/
- Current: https://pubmed.ncbi.nlm.nih.gov/20955400/
- Proposed: do_not_add

## HIGH carbamazepine / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The boxed-warning content is concordant with FDA labeling, but the row's black-box source cites DailyMed, which is not permissible for this field under the audit rules.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf
- Current: Boxed warning text present for serious dermatologic reactions/HLA-B*1502 plus aplastic anemia/agranulocytosis; current source is DailyMed-based.
- Proposed: Keep current boxed-warning text; replace source metadata with: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=bc03e499-5bac-4293-bff4-6864153a624d; effective_time=20250627; title=Carbatrol / CARBAMAZEPINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1

## MEDIUM carbamazepine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box field must use FDA/openFDA/accessdata, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=bc03e499-5bac-4293-bff4-6864153a624d; published=Jul 03, 2025; title=CARBATROL (CARBAMAZEPINE) CAPSULE, EXTENDED RELEASE [TAKEDA PHARMACEUTICALS AMERICA, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=bc03e499-5bac-4293-bff4-6864153a624d
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=bc03e499-5bac-4293-bff4-6864153a624d; effective_time=20250627; title=Carbatrol / CARBAMAZEPINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1

## MEDIUM carbamazepine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Clarifies trusted source and PubMed identifier.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; Sills and Rogawski 2020 ASM mechanism review (PMID 32120063)

## MEDIUM carbamazepine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces non-trusted/overbroad named sources with trusted sources that support the row facts.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548097/; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://pubmed.ncbi.nlm.nih.gov/15156070/; https://www.ncbi.nlm.nih.gov/books/n/niceng217er26/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling; NCBI LiverTox; Sills and Rogawski 2020 ASM mechanism review (PMID 32120063); PubMed RCT metadata (PMID 15156070); NCBI Bookshelf NICE epilepsy evidence review

## MEDIUM carbamazepine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for black-box warning verification; FDA/openFDA is permissible.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=bc03e499-5bac-4293-bff4-6864153a624d; published=Jul 03, 2025; title=CARBATROL (CARBAMAZEPINE) CAPSULE, EXTENDED RELEASE [TAKEDA PHARMACEUTICALS AMERICA, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=bc03e499-5bac-4293-bff4-6864153a624d
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=bc03e499-5bac-4293-bff4-6864153a624d; effective_time=20250627; title=Carbatrol / CARBAMAZEPINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1

## MEDIUM carbamazepine / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: FDA label specifically calls CYP3A4 strong/potent and lists CYP1A2, 2B6, 2C9/19 induction; UGT support comes from PubMed evidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/31650711/; https://pubmed.ncbi.nlm.nih.gov/14709631/
- Current: Strong enzyme inducer: CYP3A4, CYP1A2, CYP2B6, CYP2C9, CYP2C19, UGT; autoinducer
- Proposed: Strong enzyme inducer: CYP3A4; inducer of CYP1A2, CYP2B6, CYP2C9/19 and UGT pathways; autoinducer

## MEDIUM carbamazepine / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Uses the FDA label term somnolence and keeps the same verified percentages.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf
- Current: CNS: dizziness 44%, CNS: drowsiness 32%, GI: nausea 29%, GI: vomiting 18%, neurologic: ataxia 15%, dermatologic: rash 7%
- Proposed: CNS: dizziness 44%, CNS: somnolence/drowsiness 32%, neurologic: ataxia 15%, GI: nausea 29%, GI: vomiting 18%, dermatologic: rash 7%

## MEDIUM carbamazepine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Replaces DailyMed wording with FDA/accessdata and adds PMID for the peer-reviewed mechanism source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; Sills and Rogawski 2020 ASM mechanism review (PMID 32120063)

## MEDIUM carbamazepine / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: The sodium-channel mechanism is supported by peer-reviewed review evidence; FDA label mainly supports uncertainty.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: FDA label
- Proposed: FDA label + peer-reviewed review

## CRITICAL carbamazepine / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: True
- Summary: Aligns the field with FDA label-supported conduction warnings and avoids unsupported QRS-specific wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf
- Current: No typical QT prolongation; can cause conduction abnormalities/AV block and QRS effects in toxicity
- Proposed: No FDA-label evidence of typical QT prolongation; conduction/arrhythmia caution including reported AV heart block and overdose conduction disorders.

## CRITICAL carbamazepine / proposed_row_update
- Field: filter_qt_effect
- Status: proposed
- Approval required: True
- Summary: The QT-prolongation filter conflicts with the row narrative and was not supported by the FDA label evidence used in this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf
- Current: Conduction/arrhythmia caution; QT prolongation
- Proposed: Conduction/arrhythmia caution

## MEDIUM carbamazepine / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Adds supported aliases/brand names likely to improve PubMed retrieval without creating duplicate drug rows.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548097/; https://pubmed.ncbi.nlm.nih.gov/15156070/
- Proposed: CBZ; Carbatrol; Tegretol; Tegretol-XR; Tegretol XR; Equetro; Epitol

## MEDIUM carbamazepine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Uses trusted domains and sources that actually support the populated cells audited here.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id:%22bc03e499-5bac-4293-bff4-6864153a624d%22&limit=1; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/020712s038lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/021710s018lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548097/; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://pubmed.ncbi.nlm.nih.gov/15156070/; https://www.ncbi.nlm.nih.gov/books/n/niceng217er26/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling; NCBI LiverTox; Sills and Rogawski 2020 ASM mechanism review (PMID 32120063); PubMed RCT metadata (PMID 15156070); NCBI Bookshelf NICE epilepsy evidence review

## CRITICAL cenobamate / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: True
- Summary: FDA clinical interaction data support increased CYP2C19 substrate exposure and decreased CYP3A/CYP2B6 substrate exposure. Current FDA label also lists in vitro CYP2B6/CYP2C8/CYP3A4 induction and CYP2B6/CYP2C19/CYP3A inhibition, but I did not find FDA-label support for UGT induction.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: Inhibits CYP2C19; induces CYP3A4, CYP2B6, and UGT pathways
- Proposed: Inhibits CYP2C19; induces CYP3A4 and CYP2B6

## HIGH cenobamate / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: False
- Summary: The row's own enzyme text and FDA label both indicate clinically relevant induction and inhibition effects, so a filter containing only Inhibitor is incomplete.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: Inhibitor
- Proposed: Inducer; Inhibitor

## INFO cenobamate / fact_check
- Field: mechanism_confidence
- Status: not_applicable
- Approval required: False
- Summary: This is a curator confidence classification, not a directly source-verifiable drug fact. It is consistent with the FDA label statement that the precise therapeutic mechanism is unknown.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: Moderate
- Proposed: Moderate

## HIGH cenobamate / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; removing DailyMed from the source text makes the row align with the trusted-domain source policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA label (Xcopri Prescribing Information)

## HIGH cenobamate / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: FDA label Table 4 lists active-dose rates of somnolence 19/22/37%, dizziness 18/22/33%, fatigue 12/14/24%, and diplopia 6/7/15%; FDA QT warning lists QT shortening >20 ms in 31% at 200 mg and 66% at 500 mg.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: CNS: somnolence 19-37%, CNS: dizziness 18-33%, constitutional: fatigue 11-24%, ophthalmologic: diplopia 4-15%, cardiac: QT shortening >20 ms 31-66%
- Proposed: CNS: somnolence 19-37%, CNS: dizziness 18-33%, constitutional: fatigue 12-24%, ophthalmologic: diplopia 6-15%, cardiac: QT shortening >20 ms 31-66%

## HIGH cenobamate / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The current source list includes DailyMed and Epilepsy Society, which are not in the allowed trusted-source list for this audit, and it omits the PubMed/ClinicalTrials/EMA/eMC sources needed for RCTs and non-US brand/indication facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2019/212839Orig1s000ltr.pdf; https://pubmed.ncbi.nlm.nih.gov/41144696/; https://clinicaltrials.gov/study/NCT04557085; https://www.ema.europa.eu/en/medicines/human/EPAR/ontozry; https://www.medicines.org.uk/emc/product/13008/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA label (Xcopri Prescribing Information, accessdata.fda.gov); Drugs@FDA approval letter; FDA/openFDA label API for boxed-warning status; PubMed and ClinicalTrials.gov RCT records; EMA EPAR and eMC SmPC for Ontozry

## INFO cenobamate / fact_check
- Field: data_most_recently_refreshed
- Status: not_applicable
- Approval required: False
- Summary: Refresh date is row metadata rather than a drug fact; it matches the supplied audit date.
- Current: 05-20-2026
- Proposed: 05-20-2026

## INFO cenobamate / fact_check
- Field: fda_black_box_warning_verified
- Status: not_applicable
- Approval required: False
- Summary: Verification date is row metadata; the FDA source text should be updated, but the date itself matches the audit date.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: 05-20-2026
- Proposed: 05-20-2026

## HIGH cenobamate / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_placebo_rct
- Approval required: True
- Summary: PMID 32313503 is a Comment/editorial article discussing the Krauss trial, not the original randomized placebo-controlled trial report. It should not be counted as a phase II/III placebo-controlled RCT link.
- Sources: https://pubmed.ncbi.nlm.nih.gov/32313503/
- Current: https://pubmed.ncbi.nlm.nih.gov/32313503/
- Proposed: Remove from pubmed_phase_ii_iii_rct_links or move to non-RCT commentary notes; requires user approval because it removes an existing entry.

## HIGH cenobamate / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed-listed randomized controlled trial report from NCT04557085 with placebo comparison during early titration. It is a secondary/prospective analysis of an already listed trial, not a new unique trial; include only if the CSV field captures secondary RCT reports.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41230998/
- Proposed: Kawai2025|https://pubmed.ncbi.nlm.nih.gov/41230998/

## HIGH cenobamate / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: RCT-labeled seizure-subtype analysis of NCT04557085 with placebo comparison. It is not a separate trial from Lee2025; include only if secondary RCT reports are in scope.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41101116/
- Proposed: Wu2025|https://pubmed.ncbi.nlm.nih.gov/41101116/

## HIGH cenobamate / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Post hoc Chinese subgroup analysis from randomized, double-blind, placebo-controlled NCT04557085. It provides RR50/MPC/seizure-freedom values for a subgroup but should not be treated as a separate unique RCT.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41428177/
- Proposed: Yu2025|https://pubmed.ncbi.nlm.nih.gov/41428177/

## HIGH cenobamate / outcome_check
- Field: diff_50_responder_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Chung2020 and Krauss2019 differentials are correct. Lee2025/NCT04557085 reports an overall maintenance-phase >=50% responder rate for 400 mg/day of 81.6% versus 28.2% placebo, a 53.4 percentage-point differential, so the current maximum RR50 differential is too low if Lee2025 outcomes are included.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41144696/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12927683/; https://pubmed.ncbi.nlm.nih.gov/32409485/; https://pubmed.ncbi.nlm.nih.gov/31734103/
- Current: 28.2-39 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Chung2020 cenobamate 200 mg/day 28.2%; Krauss2019 cenobamate 400 mg/day 39%)
- Proposed: 28.2-53.4 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Lee2025 cenobamate 400 mg/day 53.4%; Chung2020 cenobamate 200 mg/day 28.2%; Krauss2019 cenobamate 400 mg/day 39%)

## HIGH cenobamate / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Plot values should include Lee2025 RR50 differential if the row includes Lee2025 as outcome evidence.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41144696/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12927683/; https://pubmed.ncbi.nlm.nih.gov/32409485/; https://pubmed.ncbi.nlm.nih.gov/31734103/
- Current: Chung2020|28.2|https://pubmed.ncbi.nlm.nih.gov/32409485/|222; Krauss2019|39|https://pubmed.ncbi.nlm.nih.gov/31734103/|437
- Proposed: Lee2025|53.4|https://pubmed.ncbi.nlm.nih.gov/41144696/|519; Chung2020|28.2|https://pubmed.ncbi.nlm.nih.gov/32409485/|222; Krauss2019|39|https://pubmed.ncbi.nlm.nih.gov/31734103/|437

## HIGH cenobamate / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Lee2025 and Chung2020 values are correct. FDA label also reports Study 2 seizure-free maintenance counts for 400 mg/day and placebo, yielding about a 20.1 percentage-point differential; adding Krauss2019 improves completeness but does not change the displayed range.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41144696/; https://pubmed.ncbi.nlm.nih.gov/32409485/; https://pubmed.ncbi.nlm.nih.gov/31734103/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: 19.5-49.8 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Lee2025 cenobamate 400 mg/day 49.8%; Chung2020 cenobamate 200 mg/day 19.5%)
- Proposed: 19.5-49.8 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Lee2025 cenobamate 400 mg/day 49.8%; Chung2020 cenobamate 200 mg/day 19.5%; Krauss2019 cenobamate 400 mg/day 20.1%)

## HIGH cenobamate / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Current plotted Lee2025 and Chung2020 values are supported; Krauss2019 seizure-freedom differential is extractable from FDA Study 2 maintenance-phase seizure-free counts.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41144696/; https://pubmed.ncbi.nlm.nih.gov/32409485/; https://pubmed.ncbi.nlm.nih.gov/31734103/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: Lee2025|49.8|https://pubmed.ncbi.nlm.nih.gov/41144696/|519; Chung2020|19.5|https://pubmed.ncbi.nlm.nih.gov/32409485/|222
- Proposed: Lee2025|49.8|https://pubmed.ncbi.nlm.nih.gov/41144696/|519; Chung2020|19.5|https://pubmed.ncbi.nlm.nih.gov/32409485/|222; Krauss2019|20.1|https://pubmed.ncbi.nlm.nih.gov/31734103/|437

## HIGH cenobamate / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supported by FDA/openFDA/FDA label sources, but the current cell explicitly relies on DailyMed, which is not permissible for this field under the audit instructions.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM cenobamate / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current sources do not meet the trusted-source policy for all row facts and omit RCT/non-US brand sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2019/212839Orig1s000ltr.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; https://www.ema.europa.eu/en/medicines/human/EPAR/ontozry; https://www.medicines.org.uk/emc/product/13008/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA label (Xcopri Prescribing Information, accessdata.fda.gov); Drugs@FDA approval letter; FDA/openFDA label API for boxed-warning status; PubMed and ClinicalTrials.gov RCT records; EMA EPAR and eMC SmPC for Ontozry

## MEDIUM cenobamate / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Use the FDA label URL directly for mechanism support.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA label (Xcopri Prescribing Information)

## MEDIUM cenobamate / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: FDA boxed-warning field must be verified from FDA/openFDA/FDA label/Drugs@FDA only.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=565c2126-57ae-4e29-b443-723bbe7e2072; published=Feb 02, 2026; title=XCOPRI TITRATION PACK (CENOBAMATE) KIT XCOPRI (CENOBAMATE) TABLET, FILM COATED XCOPRI MAINTENANCE PACK (CENOBAMATE) KIT XCOPRI (CENOBAMATE) TABLET [SK LIFE SCIENCE, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=565c2126-57ae-4e29-b443-723bbe7e2072
- Proposed: FDA/openFDA drug label API and FDA Xcopri Prescribing Information; status=no_boxed_warning_in_selected_fda_label; spl_set_id=565c2126-57ae-4e29-b443-723bbe7e2072; effective_time=20250925; title=Xcopri; Xcopri Maintenance Pack; Xcopri Titration Pack / CENOBAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; fda_label_url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf

## MEDIUM cenobamate / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Correct FDA-label fatigue and diplopia percentages.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: CNS: somnolence 19-37%, CNS: dizziness 18-33%, constitutional: fatigue 11-24%, ophthalmologic: diplopia 4-15%, cardiac: QT shortening >20 ms 31-66%
- Proposed: CNS: somnolence 19-37%, CNS: dizziness 18-33%, constitutional: fatigue 12-24%, ophthalmologic: diplopia 6-15%, cardiac: QT shortening >20 ms 31-66%

## CRITICAL cenobamate / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: True
- Summary: FDA label supports CYP2C19 inhibition and CYP3A4/CYP2B6 induction; UGT induction was not supported by the checked FDA label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: Inhibits CYP2C19; induces CYP3A4, CYP2B6, and UGT pathways
- Proposed: Inhibits CYP2C19; induces CYP3A4 and CYP2B6

## MEDIUM cenobamate / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: False
- Summary: Cenobamate has both inducing and inhibiting interaction effects.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: Inhibitor
- Proposed: Inducer; Inhibitor

## MEDIUM cenobamate / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use only trusted/allowed sources and include sources that support brand, indication, RCT, outcome, and FDA warning facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2019/212839Orig1s000ltr.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; https://pubmed.ncbi.nlm.nih.gov/41144696/; https://clinicaltrials.gov/study/NCT04557085; https://www.ema.europa.eu/en/medicines/human/EPAR/ontozry; https://www.medicines.org.uk/emc/product/13008/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA label (Xcopri Prescribing Information, accessdata.fda.gov); Drugs@FDA approval letter; FDA/openFDA label API for boxed-warning status; PubMed and ClinicalTrials.gov RCT records; EMA EPAR and eMC SmPC for Ontozry

## MEDIUM cenobamate / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism wording is supported by FDA labeling; DailyMed is unnecessary and outside the trusted-domain list supplied for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA label (Xcopri Prescribing Information)

## MEDIUM cenobamate / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Black-box verification must use FDA/openFDA/FDA label/Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM cenobamate / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace impermissible DailyMed boxed-warning source with FDA/openFDA/FDA label sources.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=565c2126-57ae-4e29-b443-723bbe7e2072; published=Feb 02, 2026; title=XCOPRI TITRATION PACK (CENOBAMATE) KIT XCOPRI (CENOBAMATE) TABLET, FILM COATED XCOPRI MAINTENANCE PACK (CENOBAMATE) KIT XCOPRI (CENOBAMATE) TABLET [SK LIFE SCIENCE, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=565c2126-57ae-4e29-b443-723bbe7e2072
- Proposed: FDA/openFDA drug label API and FDA Xcopri Prescribing Information; status=no_boxed_warning_in_selected_fda_label; spl_set_id=565c2126-57ae-4e29-b443-723bbe7e2072; effective_time=20250925; title=Xcopri; Xcopri Maintenance Pack; Xcopri Titration Pack / CENOBAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22565c2126-57ae-4e29-b443-723bbe7e2072%22&limit=5; fda_label_url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf

## MEDIUM cenobamate / proposed_row_update
- Field: diff_50_responder_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Add Lee2025 RR50 maximum-dose differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41144696/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12927683/
- Current: 28.2-39 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Chung2020 cenobamate 200 mg/day 28.2%; Krauss2019 cenobamate 400 mg/day 39%)
- Proposed: 28.2-53.4 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Lee2025 cenobamate 400 mg/day 53.4%; Chung2020 cenobamate 200 mg/day 28.2%; Krauss2019 cenobamate 400 mg/day 39%)

## MEDIUM cenobamate / proposed_row_update
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Add Lee2025 RR50 plot point.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41144696/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12927683/
- Current: Chung2020|28.2|https://pubmed.ncbi.nlm.nih.gov/32409485/|222; Krauss2019|39|https://pubmed.ncbi.nlm.nih.gov/31734103/|437
- Proposed: Lee2025|53.4|https://pubmed.ncbi.nlm.nih.gov/41144696/|519; Chung2020|28.2|https://pubmed.ncbi.nlm.nih.gov/32409485/|222; Krauss2019|39|https://pubmed.ncbi.nlm.nih.gov/31734103/|437

## MEDIUM cenobamate / proposed_row_update
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Add Krauss2019 seizure-freedom differential from Study 2 maintenance-phase seizure-free counts; range is unchanged.
- Sources: https://pubmed.ncbi.nlm.nih.gov/31734103/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: 19.5-49.8 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Lee2025 cenobamate 400 mg/day 49.8%; Chung2020 cenobamate 200 mg/day 19.5%)
- Proposed: 19.5-49.8 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Lee2025 cenobamate 400 mg/day 49.8%; Chung2020 cenobamate 200 mg/day 19.5%; Krauss2019 cenobamate 400 mg/day 20.1%)

## MEDIUM cenobamate / proposed_row_update
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Add Krauss2019 seizure-freedom plot point.
- Sources: https://pubmed.ncbi.nlm.nih.gov/31734103/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212839s013lbl.pdf
- Current: Lee2025|49.8|https://pubmed.ncbi.nlm.nih.gov/41144696/|519; Chung2020|19.5|https://pubmed.ncbi.nlm.nih.gov/32409485/|222
- Proposed: Lee2025|49.8|https://pubmed.ncbi.nlm.nih.gov/41144696/|519; Chung2020|19.5|https://pubmed.ncbi.nlm.nih.gov/32409485/|222; Krauss2019|20.1|https://pubmed.ncbi.nlm.nih.gov/31734103/|437

## CRITICAL cenobamate / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: Vossler2020 is a Comment/editorial about a trial, not a placebo-controlled RCT report. Removal of an existing entry requires user approval.
- Sources: https://pubmed.ncbi.nlm.nih.gov/32313503/; https://pubmed.ncbi.nlm.nih.gov/31734103/
- Current: Lee2025|https://pubmed.ncbi.nlm.nih.gov/41144696/; Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32313503/; Chung2020|https://pubmed.ncbi.nlm.nih.gov/32409485/; Krauss2019|https://pubmed.ncbi.nlm.nih.gov/31734103/; KasteleijnNolstTrenite2019|https://pubmed.ncbi.nlm.nih.gov/31292226/
- Proposed: Lee2025|https://pubmed.ncbi.nlm.nih.gov/41144696/; Chung2020|https://pubmed.ncbi.nlm.nih.gov/32409485/; Krauss2019|https://pubmed.ncbi.nlm.nih.gov/31734103/; KasteleijnNolstTrenite2019|https://pubmed.ncbi.nlm.nih.gov/31292226/

## CRITICAL cenobamate / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: True
- Summary: Update verification notes to reflect RCT concordance and secondary-report status.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41144696/; https://pubmed.ncbi.nlm.nih.gov/32313503/; https://pubmed.ncbi.nlm.nih.gov/32409485/; https://pubmed.ncbi.nlm.nih.gov/31734103/; https://pubmed.ncbi.nlm.nih.gov/31292226/; https://pubmed.ncbi.nlm.nih.gov/41230998/; https://pubmed.ncbi.nlm.nih.gov/41101116/; https://pubmed.ncbi.nlm.nih.gov/41428177/
- Current: PubMed loop 8/65 on 2026-05-15: 5 qualifying placebo-controlled randomized clinical trial report(s) retained from 22 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit 05-20-2026: PubMed links verified for cenobamate/YKP3089. Lee2025, Chung2020, Krauss2019, and KasteleijnNolstTrenite2019 are qualifying placebo-controlled phase II/III randomized trial reports or proof-of-principle reports; Vossler2020 PMID 32313503 is a Comment/editorial and should not be counted as an RCT report. KasteleijnNolstTrenite2019 is a phase 2 photosensitivity/PPR proof-of-principle study and should not be used for focal-seizure RR50/MPC/seizure-freedom outcomes. Secondary reports from NCT04557085 include Kawai2025 PMID 41230998, Wu2025 PMID 41101116, and Yu2025 PMID 41428177; include only if secondary RCT reports are in scope.

## HIGH clobazam / fact_check
- Field: trade_names
- Status: missing
- Approval required: False
- Summary: All listed trade names were supported by FDA/eMC/NCBI sources. NCBI LiverTox also lists Urbanol as a clobazam trade name. The deterministic suggestion to add 'Clobazam' as a trade name should not be applied because clobazam is the generic name, not a trade name.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210833s006lbl.pdf; https://www.medicines.org.uk/emc/product/100006/smpc; https://www.medicines.org.uk/emc/product/6913/smpc; https://www.medicines.org.uk/emc/product/8950/smpc; https://www.medicines.org.uk/emc/product/14934/smpc; https://www.ncbi.nlm.nih.gov/books/NBK548865/
- Current: Frisium; Onfi; Perizam; Sympazan; Tapclob; Zacco
- Proposed: Frisium; Onfi; Perizam; Sympazan; Tapclob; Urbanol; Zacco

## HIGH clobazam / fact_check
- Field: typical_doses_per_day
- Status: incorrect
- Approval required: False
- Summary: FDA labeling says a 5 mg/day dose can be given once daily, while daily doses greater than 5 mg should be divided twice daily.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: LGS: 5-40 mg/day divided BID depending on weight
- Proposed: LGS: 5-40 mg/day by weight; doses above 5 mg/day administered BID

## HIGH clobazam / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports CYP3A4/CYP2C19 metabolism and CYP2D6 inhibition, but the current text omits FDA-labeled weak CYP3A4 induction and CYP2B6 contribution.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: Not a major inducer; substrate of CYP3A4/CYP2C19; weak CYP2D6 inhibition reported
- Proposed: Weak CYP3A4 inducer; CYP2D6 inhibitor; clobazam is metabolized primarily by CYP3A4 and to a lesser extent by CYP2C19/CYP2B6; N-desmethylclobazam is mainly metabolized by CYP2C19

## HIGH clobazam / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; DailyMed should be removed from the named source because the audit trusted-source list does not include DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA accessdata labeling

## CRITICAL clobazam / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The FDA adverse-reaction table supports somnolence/sedation 26% overall/32% high dose, constipation 5% overall/10% high dose, pyrexia 13% overall/12% high dose, upper respiratory tract infection 12% overall/14% high dose, drooling 9% overall/14% high dose, aggression 8% overall/14% high dose, and cough 5% overall/7% high dose. The current row mixes dose-specific and all-ONFI rates and misclassifies pyrexia as infectious.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: CNS: somnolence/sedation 26-32%, infectious: pyrexia 10%, GI: constipation 10%, psychiatric: aggression 8%, respiratory: cough 7%, neurologic: drooling 7%
- Proposed: CNS: somnolence/sedation 26% overall (32% high dose); GI: constipation 5% overall (10% high dose); general: pyrexia 13% overall (12% high dose); infectious: upper respiratory tract infection 12% overall (14% high dose); neurologic: drooling 9% overall (14% high dose); psychiatric: aggression 8% overall (14% high dose); respiratory: cough 5% overall (7% high dose)

## HIGH clobazam / fact_check
- Field: filter_symptom_category
- Status: missing
- Approval required: False
- Summary: After correcting the adverse-symptom text, pyrexia belongs under a general/systemic category while upper respiratory tract infection supports retaining Infectious.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: CNS; GI; Infectious; Neurologic; Psychiatric; Respiratory
- Proposed: CNS; GI; General; Infectious; Neurologic; Psychiatric; Respiratory

## HIGH clobazam / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for FDA black-box-warning verification. FDA accessdata labeling verifies the boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22de03bd69-2dca-459c-93b4-541fd3e9571c%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=de03bd69-2dca-459c-93b4-541fd3e9571c; published=Dec 17, 2025; title=ONFI (CLOBAZAM) TABLET ONFI (CLOBAZAM) SUSPENSION [LUNDBECK PHARMACEUTICALS LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=de03bd69-2dca-459c-93b4-541fd3e9571c
- Proposed: FDA accessdata drug label; status=boxed_warning_found; product=ONFI (clobazam) tablets and oral suspension; NDA=202067/203993; revised=03/2024; reference_id=5344696; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf

## HIGH clobazam / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Epilepsy Society and Epilepsy Foundation Australia are not in the trusted-source domain list, and DailyMed should be replaced by FDA accessdata/openFDA sources. The proposed sources support the row facts more specifically.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210833s006lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548865/; https://www.ncbi.nlm.nih.gov/books/NBK552057/; https://clinicaltrials.gov/study/NCT00518713; https://www.medicines.org.uk/emc/product/100006/smpc; https://www.medicines.org.uk/emc/product/6913/smpc; https://www.medicines.org.uk/emc/product/8950/smpc; https://www.medicines.org.uk/emc/product/14934/smpc; https://www.epilepsy.com/what-is-epilepsy/syndromes/lennox-gastaut-syndrome
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA accessdata labeling (ONFI; SYMPAZAN); NCBI Bookshelf/LiverTox; NCBI Bookshelf NICE evidence update for Ng2011 outcomes; ClinicalTrials.gov NCT00518713; eMC SmPCs (Frisium, Perizam, Tapclob, Zacco); Epilepsy Foundation LGS/clobazam pages

## HIGH clobazam / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: The 56.2-point differential is correct: 68.3% high-dose clobazam minus 12.1% placebo. However, the trusted evidence describes mean reduction from baseline in average weekly drop-seizure rate, not a patient-level median percent change.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK552057/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/21956725/
- Current: 56.2 % (drug minus placebo MPC differential at maximum effective dose/regimen: Ng2011 clobazam 1.0 mg/kg/day 56.2%)
- Proposed: 56.2 % (drug minus placebo mean percent drop-seizure-rate reduction differential at maximum effective dose/regimen: Ng2011 clobazam 1.0 mg/kg/day 56.2%)

## MEDIUM clobazam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box-warning verification must use FDA/openFDA/Drugs@FDA sources, not DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22de03bd69-2dca-459c-93b4-541fd3e9571c%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=de03bd69-2dca-459c-93b4-541fd3e9571c; published=Dec 17, 2025; title=ONFI (CLOBAZAM) TABLET ONFI (CLOBAZAM) SUSPENSION [LUNDBECK PHARMACEUTICALS LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=de03bd69-2dca-459c-93b4-541fd3e9571c
- Proposed: FDA accessdata drug label; status=boxed_warning_found; product=ONFI (clobazam) tablets and oral suspension; NDA=202067/203993; revised=03/2024; reference_id=5344696; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf

## MEDIUM clobazam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace untrusted/non-permitted source names with trusted sources that directly support the populated facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/210833s006lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548865/; https://www.ncbi.nlm.nih.gov/books/NBK552057/; https://clinicaltrials.gov/study/NCT00518713; https://www.medicines.org.uk/emc/product/100006/smpc; https://www.medicines.org.uk/emc/product/6913/smpc; https://www.medicines.org.uk/emc/product/8950/smpc; https://www.medicines.org.uk/emc/product/14934/smpc; https://www.epilepsy.com/what-is-epilepsy/syndromes/lennox-gastaut-syndrome
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA accessdata labeling (ONFI; SYMPAZAN); NCBI Bookshelf/LiverTox; NCBI Bookshelf NICE evidence update for Ng2011 outcomes; ClinicalTrials.gov NCT00518713; eMC SmPCs (Frisium, Perizam, Tapclob, Zacco); Epilepsy Foundation LGS/clobazam pages

## MEDIUM clobazam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA label supports the mechanism; DailyMed is not in the trusted-source list for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA accessdata labeling

## MEDIUM clobazam / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Add Urbanol, supported by NCBI LiverTox; do not add generic 'Clobazam' as a trade name.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548865/
- Current: Frisium; Onfi; Perizam; Sympazan; Tapclob; Zacco
- Proposed: Frisium; Onfi; Perizam; Sympazan; Tapclob; Urbanol; Zacco

## CRITICAL clobazam / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Align adverse-event percentages and categories with the FDA ONFI adverse-reaction table.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: CNS: somnolence/sedation 26-32%, infectious: pyrexia 10%, GI: constipation 10%, psychiatric: aggression 8%, respiratory: cough 7%, neurologic: drooling 7%
- Proposed: CNS: somnolence/sedation 26% overall (32% high dose); GI: constipation 5% overall (10% high dose); general: pyrexia 13% overall (12% high dose); infectious: upper respiratory tract infection 12% overall (14% high dose); neurologic: drooling 9% overall (14% high dose); psychiatric: aggression 8% overall (14% high dose); respiratory: cough 5% overall (7% high dose)

## MEDIUM clobazam / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: FDA label supports the added CYP3A4 induction and CYP2B6 details.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: Not a major inducer; substrate of CYP3A4/CYP2C19; weak CYP2D6 inhibition reported
- Proposed: Weak CYP3A4 inducer; CYP2D6 inhibitor; clobazam is metabolized primarily by CYP3A4 and to a lesser extent by CYP2C19/CYP2B6; N-desmethylclobazam is mainly metabolized by CYP2C19

## MEDIUM clobazam / proposed_row_update
- Field: typical_doses_per_day
- Status: proposed
- Approval required: False
- Summary: FDA label permits 5 mg/day as a single daily dose and requires BID division only above 5 mg/day.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: LGS: 5-40 mg/day divided BID depending on weight
- Proposed: LGS: 5-40 mg/day by weight; doses above 5 mg/day administered BID

## MEDIUM clobazam / proposed_row_update
- Field: filter_symptom_category
- Status: proposed
- Approval required: False
- Summary: Corrected adverse text includes pyrexia as general/systemic and upper respiratory tract infection as infectious.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202067s008%2C203993s010lbl.pdf
- Current: CNS; GI; Infectious; Neurologic; Psychiatric; Respiratory
- Proposed: CNS; GI; General; Infectious; Neurologic; Psychiatric; Respiratory

## MEDIUM clobazam / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: The numeric value is correct, but the cited evidence reports mean reduction in average weekly drop-seizure rate, not median percent change.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK552057/; https://pubmed.ncbi.nlm.nih.gov/21956725/
- Current: 56.2 % (drug minus placebo MPC differential at maximum effective dose/regimen: Ng2011 clobazam 1.0 mg/kg/day 56.2%)
- Proposed: 56.2 % (drug minus placebo mean percent drop-seizure-rate reduction differential at maximum effective dose/regimen: Ng2011 clobazam 1.0 mg/kg/day 56.2%)

## HIGH clonazepam / fact_check
- Field: epilepsy_type; filter_epilepsy_type
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports Lennox-Gastaut/petit mal variant, akinetic, myoclonic, and refractory absence seizures. 'Adjunctive nonspecific epilepsy' is overbroad; the label says useful alone or as adjunct only for the specified seizure disorders.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: Absence; Myoclonic; Akinetic/atonic; Adjunctive nonspecific epilepsy
- Proposed: Lennox-Gastaut syndrome (petit mal variant); Akinetic; Myoclonic; Absence seizures after failure to respond to succinimides

## MEDIUM clonazepam / fact_check
- Field: mechanism_source
- Status: missing_source
- Approval required: False
- Summary: The current mechanism statement is supportable, but the retained source list should use trusted/cited domains. AES is not in the provided trusted domain list; FDA, PubMed, and NCBI sources are sufficient.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://www.ncbi.nlm.nih.gov/books/NBK556010/
- Current: American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA Klonopin label; Sills and Rogawski 2020 ASM mechanism review; NCBI Bookshelf StatPearls clonazepam

## HIGH clonazepam / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The current tier names FDA but the mechanism_source field does not cite FDA; use a tier matching the actual trusted sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: AES/FDA summary
- Proposed: FDA label/PubMed/NCBI

## HIGH clonazepam / fact_check
- Field: enzyme_inducing_or_inhibiting; filter_enzyme_effect
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports no evidence that clonazepam induces its own metabolism or that of other drugs, but it does not establish a blanket 'not an inhibitor' statement and notes CYP3A involvement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: Not a CYP inducer/inhibitor
- Proposed: No major enzyme induction established; CYP3A may play an important role in clonazepam metabolism; effect on metabolism of other drugs has not been fully investigated

## HIGH clonazepam / fact_check
- Field: minimum_effective_dose; maximum_approved_daily_dose; typical_doses_per_day
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports the initial dose, titration increments, individualized maintenance, and 20 mg/day maximum. It does not support 'maintenance often 1.5-20 mg/day' as written.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: Adults seizure disorders: 1.5 mg/day initial; titrate to effect; maximum 20 mg/day; maintenance often 1.5-20 mg/day divided TID
- Proposed: Adults seizure disorders: initial dose should not exceed 1.5 mg/day divided TID; increase by 0.5 to 1 mg every 3 days until controlled or limited by adverse effects; maintenance individualized; maximum recommended daily dose 20 mg/day

## CRITICAL clonazepam / fact_check
- Field: adverse_symptoms_percentages; filter_symptom_category
- Status: incorrect
- Approval required: True
- Summary: FDA labeling supports drowsiness about 50%, ataxia about 30%, and behavior problems about 25% in seizure-disorder experience. The FDA label supports hypersalivation/increased salivation and upper-respiratory hypersecretion but not a 7% frequency.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: CNS: drowsiness 50%, neurologic: ataxia 30%, behavioral: behavior problems 25%, respiratory: increased salivation 7%
- Proposed: CNS: drowsiness approximately 50%; neurologic: ataxia approximately 30%; behavioral: behavior problems approximately 25%; respiratory: hypersecretion in upper respiratory passages and hypersalivation/increased salivation warning, frequency not stated in FDA label

## MEDIUM clonazepam / fact_check
- Field: qt_interval_effect; filter_qt_effect
- Status: missing_source
- Approval required: False
- Summary: No QT warning was identified in the FDA label reviewed, but the current row lacks a direct trusted source proving absence of a clinically meaningful QT effect.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: No clinically meaningful QT effect established; No known meaningful QT effect
- Proposed: No QT warning identified in FDA labeling; clinically meaningful QT effect not established from reviewed trusted sources

## HIGH clonazepam / fact_check
- Field: status_or_notes
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports specified seizure disorders and panic disorder. 'Panic/anxiety disorders' is broader than the FDA-labeled psychiatric indication.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: Current benzodiazepine used for seizure types including absence/myoclonic seizures; also used for panic/anxiety disorders.
- Proposed: Current benzodiazepine used for specified seizure disorders including Lennox-Gastaut/petit mal variant, akinetic, myoclonic, and refractory absence seizures; also FDA-approved for panic disorder.

## HIGH clonazepam / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Wikipedia and Epilepsy Foundation Australia are outside the supplied trusted domains; DailyMed cannot be used for black-box verification. Use FDA, PubMed, NCBI, and ClinicalTrials.gov sources that support the specific cells.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5; https://www.fda.gov/drugs/drug-safety-and-availability/fda-requiring-boxed-warning-updated-improve-safe-use-benzodiazepine-drug-class; https://www.ncbi.nlm.nih.gov/books/NBK556010/; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://clinicaltrials.gov/study/NCT01150331
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA; FDA benzodiazepine Drug Safety Communication; FDA/accessdata Klonopin label; NCBI Bookshelf StatPearls clonazepam; PubMed Sills and Rogawski 2020 mechanism review; PubMed/ClinicalTrials.gov records for cited RCTs; FDA warning letter noting non-U.S. Rivotril clonazepam product naming

## HIGH clonazepam / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: ClinicalTrials.gov and secondary PubMed/NCBI records identify this as a randomized, double-blind phase 3 placebo-controlled trial of levetiracetam added to clonazepam versus placebo added to clonazepam. Clonazepam was given in both arms, so no clonazepam-placebo effect is tested.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26627366/
- Current: https://pubmed.ncbi.nlm.nih.gov/26627366/
- Proposed: Do not count as a qualifying clonazepam placebo-controlled efficacy RCT; remove from pubmed_phase_ii_iii_rct_links or move to notes with user approval.

## HIGH clonazepam / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: The record is a randomized double-blind low-dose clonazepam study in children with epilepsy, but evidence reviews describe it as a crossover/EEG epileptiform-activity study rather than a phase II/III seizure-frequency RCT with RR50, MPC, or seizure-freedom outcomes.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10714402/
- Current: https://pubmed.ncbi.nlm.nih.gov/10714402/
- Proposed: Do not count as a qualifying phase II/III placebo-controlled clonazepam seizure-frequency efficacy RCT; remove from the qualifying RCT field or move to notes with user approval.

## MEDIUM clonazepam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box warnings must be verified from FDA/openFDA, FDA labels, or Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=cfa0d79a-843c-4b88-95a1-e9511d649ca1; published=Dec 02, 2025; title=KLONOPIN (CLONAZEPAM) TABLET [H2-PHARMA, LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cfa0d79a-843c-4b88-95a1-e9511d649ca1
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=cfa0d79a-843c-4b88-95a1-e9511d649ca1; effective_time=20251201; title=Klonopin / CLONAZEPAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5

## MEDIUM clonazepam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Several current sources are not in the trusted domain list or do not support specific cells. DailyMed is not acceptable for black-box verification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf; https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-data-files; https://www.fda.gov/drugs/drug-safety-and-availability/fda-requiring-boxed-warning-updated-improve-safe-use-benzodiazepine-drug-class; https://www.ncbi.nlm.nih.gov/books/NBK556010/; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://clinicaltrials.gov/study/NCT01150331
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA; FDA benzodiazepine Drug Safety Communication; FDA/accessdata Klonopin label; NCBI Bookshelf StatPearls clonazepam; PubMed Sills and Rogawski 2020 mechanism review; PubMed/ClinicalTrials.gov records for cited RCTs; FDA warning letter noting non-U.S. Rivotril clonazepam product naming

## MEDIUM clonazepam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for black-box warning verification; FDA/openFDA or Drugs@FDA/accessdata is required.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=cfa0d79a-843c-4b88-95a1-e9511d649ca1; published=Dec 02, 2025; title=KLONOPIN (CLONAZEPAM) TABLET [H2-PHARMA, LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=cfa0d79a-843c-4b88-95a1-e9511d649ca1
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=cfa0d79a-843c-4b88-95a1-e9511d649ca1; effective_time=20251201; title=Klonopin / CLONAZEPAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22cfa0d79a-843c-4b88-95a1-e9511d649ca1%22&limit=5; FDA label fallback=https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf

## MEDIUM clonazepam / proposed_row_update
- Field: epilepsy_type
- Status: proposed
- Approval required: False
- Summary: FDA indication is specific and does not support broad 'adjunctive nonspecific epilepsy'.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: Absence; Myoclonic; Akinetic/atonic; Adjunctive nonspecific epilepsy
- Proposed: Lennox-Gastaut syndrome (petit mal variant); Akinetic; Myoclonic; Absence seizures after failure to respond to succinimides

## MEDIUM clonazepam / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: Current wording overstates the FDA label evidence regarding inhibition.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: Not a CYP inducer/inhibitor
- Proposed: No major enzyme induction established; CYP3A may play an important role in clonazepam metabolism; effect on metabolism of other drugs has not been fully investigated

## CRITICAL clonazepam / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: The 7% salivation value was not verified in the FDA label; the other percentages were verified.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: CNS: drowsiness 50%, neurologic: ataxia 30%, behavioral: behavior problems 25%, respiratory: increased salivation 7%
- Proposed: CNS: drowsiness approximately 50%; neurologic: ataxia approximately 30%; behavioral: behavior problems approximately 25%; respiratory: hypersecretion in upper respiratory passages and hypersalivation/increased salivation warning, frequency not stated in FDA label

## MEDIUM clonazepam / proposed_row_update
- Field: typical_doses_per_day
- Status: proposed
- Approval required: False
- Summary: FDA label supports individualized maintenance and maximum 20 mg/day, not 'maintenance often 1.5-20 mg/day'.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017533s062lbl.pdf
- Current: Adults seizure disorders: maintenance often 1.5-20 mg/day divided TID
- Proposed: Adults seizure disorders: initial dose should not exceed 1.5 mg/day divided TID; increase by 0.5 to 1 mg every 3 days until controlled or limited by adverse effects; maintenance individualized; maximum recommended daily dose 20 mg/day

## CRITICAL clonazepam / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: The cited records do not qualify as phase II/III placebo-controlled clonazepam-vs-placebo seizure-frequency efficacy RCTs for this row. Navarro is a levetiracetam add-on trial with clonazepam in both arms; Dahlin is a low-dose EEG crossover study, not phase II/III RR50/MPC/seizure-freedom evidence.
- Sources: https://clinicaltrials.gov/study/NCT01150331; https://pubmed.ncbi.nlm.nih.gov/26627366/; https://pubmed.ncbi.nlm.nih.gov/10714402/; https://www.ncbi.nlm.nih.gov/books/NBK581157/
- Current: Navarro2015|https://pubmed.ncbi.nlm.nih.gov/26627366/; Dahlin2000|https://pubmed.ncbi.nlm.nih.gov/10714402/

## CRITICAL clonazepam / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: True
- Summary: Current notes incorrectly describe both records as qualifying clonazepam placebo-controlled RCT reports for extractable effectiveness summaries.
- Sources: https://clinicaltrials.gov/study/NCT01150331; https://pubmed.ncbi.nlm.nih.gov/26627366/; https://pubmed.ncbi.nlm.nih.gov/10714402/; https://www.ncbi.nlm.nih.gov/books/NBK579009/; https://www.ncbi.nlm.nih.gov/books/NBK581157/
- Current: PubMed loop 10/65 on 2026-05-15: 2 qualifying placebo-controlled randomized clinical trial report(s) retained from 11 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit 2026-05-20: The cited records do not provide clonazepam-vs-placebo RR50, median percent seizure-frequency change, or seizure-freedom outcomes. Navarro2015/SAMUKeppra is a phase 3 levetiracetam add-on trial in which both arms received clonazepam; placebo controls levetiracetam, not clonazepam. Dahlin2000 is a randomized double-blind low-dose clonazepam EEG study measuring epileptiform activity, not phase II/III seizure-frequency RR50/MPC/seizure-freedom outcomes.

## HIGH clorazepate dipotassium / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: The FDA label lists these adverse reactions qualitatively. It does not support an incidence of 0%; removing the 0% notation avoids implying no adverse-event incidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017105s085lbl.pdf
- Current: N/A 0%: FDA label lists drowsiness, dizziness, GI complaints, nervousness, blurred vision, dry mouth, headache, mental confusion, insomnia, skin rashes, fatigue, ataxia, irritability, diplopia, depression, tremor, and slurred speech without quantified incidence percentages.
- Proposed: N/A: FDA label lists drowsiness, dizziness, GI complaints, nervousness, blurred vision, dry mouth, headache, mental confusion, insomnia, skin rashes, fatigue, ataxia, irritability, diplopia, depression, tremor, and slurred speech without quantified incidence percentages.

## MEDIUM clorazepate dipotassium / fact_check
- Field: filter_qt_effect
- Status: insufficient_evidence
- Approval required: True
- Summary: The detailed row text only establishes that QT interval effects are not described in the selected FDA label; it does not directly establish a clinically verified 'no known meaningful QT effect' category.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017105s085lbl.pdf
- Current: No known meaningful QT effect
- Proposed: Unknown/limited

## HIGH clorazepate dipotassium / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be used for black-box verification and is not in the requested trusted-source list. The retained row facts are better supported by FDA Orange Book, FDA Drugs@FDA/accessdata/openFDA labeling, and NCBI alias sources.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.fda.gov/media/71474/download; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017105s085lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5; https://www.ncbi.nlm.nih.gov/mesh/68003009
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book data files/annual edition; FDA Drugs@FDA/accessdata labeling; FDA/openFDA drug label API; NCBI MeSH/PubChem for aliases

## MEDIUM clorazepate dipotassium / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for the black-box-warning field; FDA/openFDA is permissible.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017105s085lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=919cbd07-f587-4005-acff-26213dd1d1fb; published=Mar 26, 2026; title=CLORAZEPATE DIPOTASSIUM TABLET [AUROLIFE PHARMA LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=919cbd07-f587-4005-acff-26213dd1d1fb
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=919cbd07-f587-4005-acff-26213dd1d1fb; effective_time=20260325; title=CLORAZEPATE DIPOTASSIUM / CLORAZEPATE DIPOTASSIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5

## MEDIUM clorazepate dipotassium / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces the DailyMed reference with trusted FDA/NCBI sources that actually support the retained cells.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.fda.gov/media/71474/download; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017105s085lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22919cbd07-f587-4005-acff-26213dd1d1fb%22&limit=5; https://www.ncbi.nlm.nih.gov/mesh/68003009
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book data files/annual edition; FDA Drugs@FDA/accessdata labeling; FDA/openFDA drug label API; NCBI MeSH/PubChem for aliases

## MEDIUM clorazepate dipotassium / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism facts are supported by FDA labeling and NCBI MeSH without relying on DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017105s085lbl.pdf; https://www.ncbi.nlm.nih.gov/mesh/68003009
- Current: FDA/DailyMed labeling
- Proposed: FDA Drugs@FDA/accessdata labeling; NCBI MeSH

## MEDIUM clorazepate dipotassium / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: FDA labeling provides a qualitative adverse-reaction list but no 0% incidence value.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017105s085lbl.pdf
- Current: N/A 0%: FDA label lists drowsiness, dizziness, GI complaints, nervousness, blurred vision, dry mouth, headache, mental confusion, insomnia, skin rashes, fatigue, ataxia, irritability, diplopia, depression, tremor, and slurred speech without quantified incidence percentages.
- Proposed: N/A: FDA label lists drowsiness, dizziness, GI complaints, nervousness, blurred vision, dry mouth, headache, mental confusion, insomnia, skin rashes, fatigue, ataxia, irritability, diplopia, depression, tremor, and slurred speech without quantified incidence percentages.

## MEDIUM clorazepate dipotassium / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Adds NCBI MeSH entry terms for the same drug/substance to avoid alias-driven duplicate rows.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68003009
- Current: clorazepate
- Proposed: clorazepate; dipotassium chlorazepate; chlorazepate; clorazepic acid

## MEDIUM clorazepate dipotassium / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Adds verified PubMed-relevant entry terms and brand aliases.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68003009; https://pubchem.ncbi.nlm.nih.gov/compound/167305
- Current: clorazepate; Tranxene; Tranxene SD; Gen-Xene
- Proposed: clorazepate; clorazepate dipotassium; dipotassium chlorazepate; chlorazepate; Tranxene; Tranxene SD; Gen-Xene; Tranxilium

## CRITICAL clorazepate dipotassium / proposed_row_update
- Field: filter_qt_effect
- Status: proposed
- Approval required: True
- Summary: The cited FDA label only supports that QT effects are not described; it does not directly support a broader no-known-meaningful-effect category.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017105s085lbl.pdf
- Current: No known meaningful QT effect
- Proposed: Unknown/limited

## MEDIUM clorazepate dipotassium / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: Clarifies the Orange Book application context; no substantive change.
- Sources: https://www.fda.gov/media/71474/download; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: Approved prior to Jan 1, 1982 (FDA Orange Book; NDA 017105).

## HIGH diazepam / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Search aliases are missing. Several RCTs and FDA labels use formulation/trade-name terms such as Diastat, VALTOCO, LIBERVANT, and diazepam auto-injector.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/24111974/; https://pubmed.ncbi.nlm.nih.gov/9818845/
- Proposed: Valium; Diastat; Diastat AcuDial; Valtoco; Libervant; diazepam rectal gel; diazepam nasal spray; diazepam buccal film; diazepam auto-injector

## CRITICAL diazepam / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The current ataxia 15%, dizziness 12%, nasal discomfort 6%, and nausea 5% values were not supported by the FDA VALTOCO/LIBERVANT label tables reviewed. FDA label data support rectal-gel trial rates of somnolence 23%, headache 5%, diarrhea 4%, ataxia 3%, dizziness 3%, and VALTOCO local nasal discomfort 5%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf
- Current: CNS: somnolence 23%, neurologic: ataxia 15%, CNS: dizziness 12%, respiratory: nasal discomfort 6% for nasal product, GI: nausea 5%
- Proposed: CNS: somnolence 23%; CNS: headache 5%; GI: diarrhea 4%; neurologic: ataxia 3%; CNS: dizziness 3%; respiratory/local: nasal discomfort 5% for nasal spray

## HIGH diazepam / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Wikipedia and Epilepsy Foundation Australia are not in the trusted-source list for this audit, and DailyMed is not permissible for black-box verification. Replace with trusted FDA, NCBI, epilepsy.com, PubMed, and ClinicalTrials.gov sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK547871/; https://www.epilepsy.com/treatment/seizure-rescue-therapies/oral-rescue-medicines; https://clinicaltrials.gov/study/NCT00319501
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; FDA/DailyMed labeling
- Proposed: FDA/accessdata prescribing information and approval records; NCBI Bookshelf/LiverTox; Epilepsy Foundation (epilepsy.com); PubMed RCT records; ClinicalTrials.gov records

## CRITICAL diazepam / fact_check
- Field: formulations_available
- Status: incorrect
- Approval required: True
- Summary: FDA/NCBI sources support tablets, oral solution, rectal gel, nasal spray, injection, and LIBERVANT buccal film. Diazepam auto-injector is supported as an investigational/clinical-trial formulation, not as a current approved/available formulation in the reviewed FDA sources.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK547871/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/24111974/
- Current: Tablet; oral solution; rectal gel; nasal spray; IV injection; autoinjector in some settings
- Proposed: Tablet; oral solution; rectal gel; nasal spray; IV/IM injection; buccal film

## CRITICAL diazepam / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: True
- Summary: Current text is partly supported for typical diazepam half-life, but FDA labels document a wider age-related diazepam range and a desmethyldiazepam half-life around 147 h, which contradicts 'active metabolites up to ~100 h'.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf
- Current: Diazepam 20-50 h; active metabolites up to ~100 h
- Proposed: Diazepam half-life is formulation/population dependent: about 49.2 h after a 10 mg VALTOCO dose, about 15-100 h across adult age range after IV dosing, and desmethyldiazepam about 147 h in LIBERVANT labeling

## MEDIUM diazepam / fact_check
- Field: mechanism_source
- Status: missing_source
- Approval required: False
- Summary: DailyMed is not in the trusted source list supplied for this audit; FDA/accessdata labels support the mechanism statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM diazepam / fact_check
- Field: qt_interval_effect
- Status: missing_source
- Approval required: False
- Summary: No cited row source specifically supports this QT statement. Absence of a QT warning in reviewed labels is not strong enough to verify the cell as written.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: No change proposed without a specific trusted QT source

## HIGH diazepam / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Placebo-controlled randomized acute repetitive seizure trial of diazepam rectal gel. FDA labeling reports the corresponding 91-patient study and seizure-free rates of 62% vs 20%, which materially changes the seizure-freedom differential maximum to 42%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9637805/
- Proposed: Dreifuss1998|https://pubmed.ncbi.nlm.nih.gov/9637805/

## HIGH diazepam / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Phase III randomized double-blind placebo-controlled multicenter diazepam auto-injector trial for acute repetitive seizures; ClinicalTrials.gov NCT00319501 links this study to a completed Phase 3 trial.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24111974/
- Proposed: AbouKhalil2013|https://pubmed.ncbi.nlm.nih.gov/24111974/

## HIGH diazepam / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Randomized placebo-controlled diazepam-arm trial for status epilepticus; ClinicalTrials.gov NCT00004297 identifies the study as Phase 3 randomized diazepam vs lorazepam vs placebo for prehospital status epilepticus.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11547716/
- Proposed: Alldredge2001|https://pubmed.ncbi.nlm.nih.gov/11547716/

## CRITICAL diazepam / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: The cited values for vanTuijl2021, Cereghino1998, and Autret1990 are supported by the respective abstract/label evidence. However, the current range omits a qualifying rectal diazepam gel placebo-controlled RCT summarized in FDA labeling with 62% vs 20% seizure-free patients, a 42% differential; therefore the maximum is not 21%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33465768/; https://pubmed.ncbi.nlm.nih.gov/9818845/; https://pubmed.ncbi.nlm.nih.gov/2202804/; https://pubmed.ncbi.nlm.nih.gov/9637805/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: 1.8-21 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: vanTuijl2021 diazepam for 3 days after acute stroke 1.8%; Cereghino1998 single caregiver-administered rectal diazepam dose 21%; Autret1990 intermittent oral diazepam during fever 3.5%)
- Proposed: 1.8-42% (drug minus placebo seizure-free or recurrence-free differential from placebo-controlled RCTs with extractable rates: vanTuijl2021 diazepam for 3 days after acute stroke 1.8%; Dreifuss1998 diazepam rectal gel acute repetitive seizure study 42%; Cereghino1998 single caregiver-administered rectal diazepam dose 21%; Autret1990 intermittent oral diazepam during fever 3.5%)

## CRITICAL diazepam / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: Add the missing Dreifuss/FDA-labeled 91-patient rectal diazepam placebo-controlled trial result, 62% vs 20% seizure-free.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9637805/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: vanTuijl2021|1.8|https://pubmed.ncbi.nlm.nih.gov/33465768/|784; Cereghino1998|21|https://pubmed.ncbi.nlm.nih.gov/9818845/|114; Autret1990|3.5|https://pubmed.ncbi.nlm.nih.gov/2202804/|185
- Proposed: vanTuijl2021|1.8|https://pubmed.ncbi.nlm.nih.gov/33465768/|784; Dreifuss1998|42|https://pubmed.ncbi.nlm.nih.gov/9637805/|91; Cereghino1998|21|https://pubmed.ncbi.nlm.nih.gov/9818845/|114; Autret1990|3.5|https://pubmed.ncbi.nlm.nih.gov/2202804/|185

## CRITICAL diazepam / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: True
- Summary: Current source is DailyMed, which is not permissible for the black-box field. FDA accessdata VALTOCO and LIBERVANT labels confirm a boxed warning, but the CSV text is duplicated and product-specific to LIBERVANT; the broader current FDA diazepam rescue product label wording is better represented by a concise FDA-sourced warning summary.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-requiring-boxed-warning-updated-improve-safe-use-benzodiazepine-drug-class
- Current: WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION and DEPENDENCE AND WITHDRAWAL REACTIONS ... FDA/DailyMed SPL ... url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=12527569-8eb3-4624-b3c0-5c0e0c5f88c9
- Proposed: WARNING: RISKS FROM CONCOMITANT USE WITH OPIOIDS; ABUSE, MISUSE, AND ADDICTION; AND DEPENDENCE AND WITHDRAWAL REACTIONS. Boxed warning present for diazepam benzodiazepine products: opioid co-use can cause profound sedation, respiratory depression, coma, and death; benzodiazepine use exposes users to abuse, misuse, addiction, overdose, and death; use more frequently than recommended can cause physical dependence and potentially life-threatening withdrawal reactions.

## MEDIUM diazepam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current sources include non-trusted or disallowed sources for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK547871/; https://www.epilepsy.com/treatment/seizure-rescue-therapies/oral-rescue-medicines; https://clinicaltrials.gov/study/NCT00319501
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; FDA/DailyMed labeling
- Proposed: FDA/accessdata prescribing information and approval records; NCBI Bookshelf/LiverTox; Epilepsy Foundation (epilepsy.com); PubMed RCT records; ClinicalTrials.gov records

## CRITICAL diazepam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: True
- Summary: Black-box verification must use FDA/openFDA, FDA labels, or Drugs@FDA only; DailyMed is not permissible.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=12527569-8eb3-4624-b3c0-5c0e0c5f88c9; published=Nov 15, 2024; title=LIBERVANT (DIAZEPAM) FILM [AQUESTIVE THERAPEUTICS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=12527569-8eb3-4624-b3c0-5c0e0c5f88c9
- Proposed: FDA/accessdata prescribing information; status=boxed_warning_found; Reference ID=5681158; title=VALTOCO (diazepam) nasal spray; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf

## MEDIUM diazepam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supported directly by FDA/accessdata labels; source text should avoid DailyMed because it is outside the trusted source list supplied for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## CRITICAL diazepam / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: FDA label percentages contradict several current adverse-event values.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: CNS: somnolence 23%, neurologic: ataxia 15%, CNS: dizziness 12%, respiratory: nasal discomfort 6% for nasal product, GI: nausea 5%
- Proposed: CNS: somnolence 23%; CNS: headache 5%; GI: diarrhea 4%; neurologic: ataxia 3%; CNS: dizziness 3%; respiratory/local: nasal discomfort 5% for nasal spray

## MEDIUM diazepam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace untrusted/inapplicable sources with trusted sources specified by audit instructions.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK547871/; https://www.epilepsy.com/treatment/seizure-rescue-therapies/oral-rescue-medicines; https://clinicaltrials.gov/study/NCT00319501
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; FDA/DailyMed labeling
- Proposed: FDA/accessdata prescribing information and approval records; NCBI Bookshelf/LiverTox; Epilepsy Foundation (epilepsy.com); PubMed RCT records; ClinicalTrials.gov records

## CRITICAL diazepam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: True
- Summary: DailyMed is not permissible for black-box verification; FDA/accessdata label is permissible.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=12527569-8eb3-4624-b3c0-5c0e0c5f88c9; published=Nov 15, 2024; title=LIBERVANT (DIAZEPAM) FILM [AQUESTIVE THERAPEUTICS]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=12527569-8eb3-4624-b3c0-5c0e0c5f88c9
- Proposed: FDA/accessdata prescribing information; status=boxed_warning_found; Reference ID=5681158; title=VALTOCO (diazepam) nasal spray; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf

## MEDIUM diazepam / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Verification should be tied to FDA/accessdata rather than DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: 05-20-2026
- Proposed: 05-20-2026

## CRITICAL diazepam / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: True
- Summary: Add FDA-approved buccal film and remove unsupported currently available auto-injector wording.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK547871/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf
- Current: Tablet; oral solution; rectal gel; nasal spray; IV injection; autoinjector in some settings
- Proposed: Tablet; oral solution; rectal gel; nasal spray; IV/IM injection; buccal film

## CRITICAL diazepam / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: FDA labels support a broader range and longer desmethyldiazepam half-life than the current text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf
- Current: Diazepam 20-50 h; active metabolites up to ~100 h
- Proposed: Diazepam half-life is formulation/population dependent: about 49.2 h after a 10 mg VALTOCO dose, about 15-100 h across adult age range after IV dosing, and desmethyldiazepam about 147 h in LIBERVANT labeling

## MEDIUM diazepam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Use trusted FDA/accessdata source naming instead of DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/218623s000lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM diazepam / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Alias/search field is empty despite important trade names and formulation names used in labels and RCT titles.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24111974/; https://pubmed.ncbi.nlm.nih.gov/9818845/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Proposed: Valium; Diastat; Diastat AcuDial; Valtoco; Libervant; diazepam rectal gel; diazepam nasal spray; diazepam buccal film; diazepam auto-injector

## MEDIUM diazepam / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: False
- Summary: Existing links are valid but incomplete; at least three relevant placebo-controlled diazepam seizure/status epilepticus RCTs are missing.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9637805/; https://pubmed.ncbi.nlm.nih.gov/24111974/; https://pubmed.ncbi.nlm.nih.gov/11547716/; https://clinicaltrials.gov/study/NCT00319501; https://clinicaltrials.gov/study/NCT00004297
- Current: vanTuijl2021|https://pubmed.ncbi.nlm.nih.gov/33465768/; Cereghino1998|https://pubmed.ncbi.nlm.nih.gov/9818845/; Uhari1995|https://pubmed.ncbi.nlm.nih.gov/7776115/; Rosman1993|https://pubmed.ncbi.nlm.nih.gov/8510706/; Autret1990|https://pubmed.ncbi.nlm.nih.gov/2202804/
- Proposed: vanTuijl2021|https://pubmed.ncbi.nlm.nih.gov/33465768/; Cereghino1998|https://pubmed.ncbi.nlm.nih.gov/9818845/; Uhari1995|https://pubmed.ncbi.nlm.nih.gov/7776115/; Rosman1993|https://pubmed.ncbi.nlm.nih.gov/8510706/; Autret1990|https://pubmed.ncbi.nlm.nih.gov/2202804/; Dreifuss1998|https://pubmed.ncbi.nlm.nih.gov/9637805/; AbouKhalil2013|https://pubmed.ncbi.nlm.nih.gov/24111974/; Alldredge2001|https://pubmed.ncbi.nlm.nih.gov/11547716/

## CRITICAL diazepam / proposed_row_update
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Omitted FDA-labeled 91-patient rectal diazepam gel placebo RCT result changes the maximum differential from 21% to 42%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9637805/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: 1.8-21 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: vanTuijl2021 diazepam for 3 days after acute stroke 1.8%; Cereghino1998 single caregiver-administered rectal diazepam dose 21%; Autret1990 intermittent oral diazepam during fever 3.5%)
- Proposed: 1.8-42% (drug minus placebo seizure-free or recurrence-free differential from placebo-controlled RCTs with extractable rates: vanTuijl2021 diazepam for 3 days after acute stroke 1.8%; Dreifuss1998 diazepam rectal gel acute repetitive seizure study 42%; Cereghino1998 single caregiver-administered rectal diazepam dose 21%; Autret1990 intermittent oral diazepam during fever 3.5%)

## CRITICAL diazepam / proposed_row_update
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Add missing 42% placebo differential from the rectal diazepam gel study summarized in FDA labeling.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9637805/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/211635Orig1s012corrected_lbl.pdf
- Current: vanTuijl2021|1.8|https://pubmed.ncbi.nlm.nih.gov/33465768/|784; Cereghino1998|21|https://pubmed.ncbi.nlm.nih.gov/9818845/|114; Autret1990|3.5|https://pubmed.ncbi.nlm.nih.gov/2202804/|185
- Proposed: vanTuijl2021|1.8|https://pubmed.ncbi.nlm.nih.gov/33465768/|784; Dreifuss1998|42|https://pubmed.ncbi.nlm.nih.gov/9637805/|91; Cereghino1998|21|https://pubmed.ncbi.nlm.nih.gov/9818845/|114; Autret1990|3.5|https://pubmed.ncbi.nlm.nih.gov/2202804/|185

## HIGH eslicarbazepine acetate / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; DailyMed is unnecessary and is not in the trusted source list for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## CRITICAL eslicarbazepine acetate / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: FDA adult adjunctive placebo-controlled trial table for Aptiom 800 mg and 1200 mg reports dizziness 20/28%, somnolence 11/18%, nausea 10/16%, diplopia 9/11%, and ataxia 4/6%. Current values appear to mix or understate several active-dose percentages.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf
- Current: CNS: dizziness 21-28%, CNS: somnolence 8-18%, GI: nausea 7-10%, neurologic: diplopia 6-11%, neurologic: ataxia 4-6%
- Proposed: CNS: dizziness 20-28%, CNS: somnolence 11-18%, GI: nausea 10-16%, neurologic: diplopia 9-11%, neurologic: ataxia 4-6%

## HIGH eslicarbazepine acetate / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed and Epilepsy Society are not in the trusted source list for this audit, and DailyMed is explicitly impermissible for boxed-warning verification. The proposed sources cover the populated row facts with trusted domains.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK548939/; https://www.ema.europa.eu/en/medicines/human/EPAR/zebinix; https://www.medicines.org.uk/emc/product/7872/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling; FDA/openFDA labeling; NCBI LiverTox; EMA Zebinix EPAR; eMC Zebinix SmPC; PubMed RCT records; ClinicalTrials.gov records

## HIGH eslicarbazepine acetate / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: False
- Summary: The drug has both induction and inhibition effects: CYP3A4/UGT induction and CYP2C19 inhibition.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf; https://www.medicines.org.uk/emc/product/7872/smpc
- Current: Inhibitor
- Proposed: Inducer; Inhibitor

## HIGH eslicarbazepine acetate / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Phase II randomized, double-blind, placebo-controlled pediatric adjunctive eslicarbazepine acetate study in refractory focal-onset seizures; it is a qualifying phase II placebo-controlled ASM trial report but is absent from the current PubMed RCT link field.
- Sources: https://pubmed.ncbi.nlm.nih.gov/29454255/
- Proposed: Jozwiak2018|https://pubmed.ncbi.nlm.nih.gov/29454255/

## HIGH eslicarbazepine acetate / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supported by FDA/openFDA/FDA label sources, but the current row uses DailyMed wording/source for the boxed-warning field, which violates the row policy.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Boxed-warning verification must use FDA/openFDA/FDA labeling, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=3d0c9554-eaeb-4694-8089-00133fcadce3; published=Dec 05, 2023; title=APTIOM (ESLICARBAZEPINE ACETATE) TABLET APTIOM (ESLICARBAZEPINE ACETATE) KIT [SUMITOMO PHARMA AMERICA, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3d0c9554-eaeb-4694-8089-00133fcadce3
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=3d0c9554-eaeb-4694-8089-00133fcadce3; effective_time=20231110; title=Aptiom / ESLICARBAZEPINE ACETATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism source should cite FDA labeling on a trusted FDA domain rather than DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace non-trusted and policy-problem sources with trusted sources actually supporting the row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK548939/; https://www.ema.europa.eu/en/medicines/human/EPAR/zebinix; https://www.medicines.org.uk/emc/product/7872/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling; FDA/openFDA labeling; NCBI LiverTox; EMA Zebinix EPAR; eMC Zebinix SmPC; PubMed RCT records; ClinicalTrials.gov records

## CRITICAL eslicarbazepine acetate / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Align adult adjunctive adverse-event percentages to FDA labeling for Aptiom 800 and 1200 mg.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf
- Current: CNS: dizziness 21-28%, CNS: somnolence 8-18%, GI: nausea 7-10%, neurologic: diplopia 6-11%, neurologic: ataxia 4-6%
- Proposed: CNS: dizziness 20-28%, CNS: somnolence 11-18%, GI: nausea 10-16%, neurologic: diplopia 9-11%, neurologic: ataxia 4-6%

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace non-trusted or policy-problem source wording with trusted sources used for the row.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK548939/; https://www.ema.europa.eu/en/medicines/human/EPAR/zebinix; https://www.medicines.org.uk/emc/product/7872/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling; FDA/openFDA labeling; NCBI LiverTox; EMA Zebinix EPAR; eMC Zebinix SmPC; PubMed RCT records; ClinicalTrials.gov records

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; FDA/openFDA/FDA label sources support the no-boxed-warning conclusion.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Use FDA/openFDA rather than DailyMed for boxed-warning source metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=3d0c9554-eaeb-4694-8089-00133fcadce3; published=Dec 05, 2023; title=APTIOM (ESLICARBAZEPINE ACETATE) TABLET APTIOM (ESLICARBAZEPINE ACETATE) KIT [SUMITOMO PHARMA AMERICA, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=3d0c9554-eaeb-4694-8089-00133fcadce3
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=3d0c9554-eaeb-4694-8089-00133fcadce3; effective_time=20231110; title=Aptiom / ESLICARBAZEPINE ACETATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Keep audit-date verification after switching source text to FDA/openFDA.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%223d0c9554-eaeb-4694-8089-00133fcadce3%22&limit=5
- Current: 05-20-2026
- Proposed: 05-20-2026

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supported by FDA label; DailyMed wording is unnecessary for this trusted-source audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: False
- Summary: Eslicarbazepine acetate has both induction and inhibition effects.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/022416s009lbl.pdf; https://www.medicines.org.uk/emc/product/7872/smpc
- Current: Inhibitor
- Proposed: Inducer; Inhibitor

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: False
- Summary: Add missing phase II randomized double-blind placebo-controlled pediatric focal-onset seizure study report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/29454255/; https://clinicaltrials.gov/study/NCT01527513
- Current: Koepp2026|https://pubmed.ncbi.nlm.nih.gov/41722592/; Kirkham2020|https://pubmed.ncbi.nlm.nih.gov/32151803/; Mintzer2018|https://pubmed.ncbi.nlm.nih.gov/29499473/; Sperling2014|https://pubmed.ncbi.nlm.nih.gov/25528898/; BenMenachem2010|https://pubmed.ncbi.nlm.nih.gov/20299189/; GilNagel2009|https://pubmed.ncbi.nlm.nih.gov/19832771/; Elger2009|https://pubmed.ncbi.nlm.nih.gov/19243424/; Elger2007|https://pubmed.ncbi.nlm.nih.gov/17319919/
- Proposed: Koepp2026|https://pubmed.ncbi.nlm.nih.gov/41722592/; Kirkham2020|https://pubmed.ncbi.nlm.nih.gov/32151803/; Mintzer2018|https://pubmed.ncbi.nlm.nih.gov/29499473/; Jozwiak2018|https://pubmed.ncbi.nlm.nih.gov/29454255/; Sperling2014|https://pubmed.ncbi.nlm.nih.gov/25528898/; BenMenachem2010|https://pubmed.ncbi.nlm.nih.gov/20299189/; GilNagel2009|https://pubmed.ncbi.nlm.nih.gov/19832771/; Elger2009|https://pubmed.ncbi.nlm.nih.gov/19243424/; Elger2007|https://pubmed.ncbi.nlm.nih.gov/17319919/

## MEDIUM eslicarbazepine acetate / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Update RCT notes to reflect manual audit and the added missing trial report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/29454255/; https://pubmed.ncbi.nlm.nih.gov/25528898/; https://pubmed.ncbi.nlm.nih.gov/20299189/; https://pubmed.ncbi.nlm.nih.gov/19832771/; https://pubmed.ncbi.nlm.nih.gov/19243424/; https://pubmed.ncbi.nlm.nih.gov/17319919/
- Current: PubMed loop 14/65 on 2026-05-15: 8 qualifying placebo-controlled randomized clinical trial report(s) retained from 33 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit 2026-05-20: existing PubMed links verified as eslicarbazepine acetate phase II/III placebo-controlled randomized trial reports or secondary reports of such trials; added Jozwiak2018 (PMID 29454255) as a qualifying phase II randomized double-blind placebo-controlled pediatric study. Differential effectiveness columns retain extractable adult maximum effective-dose/regimen RR50/MPC values from Sperling2014, BenMenachem2010, GilNagel2009, Elger2009, and Elger2007; seizure-freedom differential remains not extractable.

## CRITICAL ethosuximide / fact_check
- Field: trade_names
- Status: incorrect
- Approval required: True
- Summary: Zarontin is the FDA-labeled proprietary/brand name; ethosuximide is already the generic name and should not be repeated as a trade name unless the row intentionally stores generic-labeled product names in this field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5
- Current: Ethosuximide; Zarontin
- Proposed: Zarontin

## HIGH ethosuximide / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be used for the boxed-warning field, and the row needs NIH/NCBI/PubMed sources for pharmacokinetic and enzyme-effect facts not present in FDA labeling.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK544244/; https://pubmed.ncbi.nlm.nih.gov/9606477/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling; FDA-approved labeling PDFs; NIH/NCBI Bookshelf; PubMed

## HIGH ethosuximide / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: A PubMed review states ethosuximide is neither an inducer nor inhibitor of drug metabolism, while FDA labeling supports the phenytoin/valproate interaction wording.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9606477/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf
- Current: N/A - selected FDA label does not define clinically meaningful enzyme induction or inhibition; label notes interactions with other antiepileptic drug serum levels.
- Proposed: Neither enzyme-inducing nor enzyme-inhibiting; ethosuximide may increase phenytoin levels, and valproic acid has been reported to both increase and decrease ethosuximide levels.

## HIGH ethosuximide / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: False
- Summary: The selected FDA label may omit half-life, but a trusted NIH/NCBI source provides the half-life range, so N/A is incomplete for the data field.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK544244/
- Current: N/A - selected FDA/DailyMed label does not provide a half-life value.
- Proposed: 30 hours in children; 50-60 hours in adults.

## HIGH ethosuximide / fact_check
- Field: major_organ_for_metabolism
- Status: incorrect
- Approval required: False
- Summary: NIH/NCBI sources identify hepatic metabolism and CYP3A4 involvement; LiverTox also describes liver metabolism via cytochrome P450.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK544244/; https://www.ncbi.nlm.nih.gov/books/NBK547870/; https://pubmed.ncbi.nlm.nih.gov/12637244/
- Current: N/A - selected FDA/DailyMed label does not identify a major metabolic organ; label advises caution and monitoring with liver or renal disease.
- Proposed: Hepatic metabolism; about 80% metabolized to inactive metabolites, primarily by CYP3A4.

## HIGH ethosuximide / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism statement is supportable from FDA-approved labeling PDFs, so the source should not depend on DailyMed wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA-approved labeling

## HIGH ethosuximide / fact_check
- Field: filter_mechanism
- Status: incorrect
- Approval required: False
- Summary: NIH/NCBI describes ethosuximide as disrupting thalamocortical absence seizure circuitry by blocking/reducing T-type calcium currents; the current filter is less accurate.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK544244/
- Current: Other / unclear
- Proposed: T-type calcium channel blocker

## HIGH ethosuximide / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: False
- Summary: Trusted NIH/NCBI and PubMed sources identify hepatic/CYP metabolism, so the filter should not remain limited/unknown.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK544244/; https://pubmed.ncbi.nlm.nih.gov/12637244/
- Current: Limited/unknown
- Proposed: Hepatic; CYP3A4

## HIGH ethosuximide / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: False
- Summary: PubMed review evidence supports ethosuximide as neither an inducer nor inhibitor of drug metabolism.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9606477/
- Current: Unknown/limited
- Proposed: None / not clinically meaningful

## MEDIUM ethosuximide / fact_check
- Field: filter_qt_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: Absence of QT wording in the FDA label supports label silence, not a positive no-effect finding from a QT study.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf
- Current: No known meaningful QT effect
- Proposed: No QT effect described in FDA label

## HIGH ethosuximide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning finding is supported when checked against FDA/openFDA and FDA labeling, but the current row wording and source rely on DailyMed, which is not permissible for this field under the audit policy.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM ethosuximide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Needed to comply with the boxed-warning source policy and to support half-life, metabolism, enzyme-effect, and RCT-scope checks.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK544244/; https://pubmed.ncbi.nlm.nih.gov/20200383/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling; FDA-approved labeling PDFs; NIH/NCBI Bookshelf; PubMed

## MEDIUM ethosuximide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed-dependent source wording and add sources needed for pharmacokinetics/enzyme-effect fields.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK544244/; https://pubmed.ncbi.nlm.nih.gov/9606477/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling; FDA-approved labeling PDFs; NIH/NCBI Bookshelf; PubMed

## MEDIUM ethosuximide / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; FDA/openFDA supports the finding.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM ethosuximide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Use FDA/openFDA metadata instead of DailyMed for boxed-warning source.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6; published=Jul 16, 2024; title=ZARONTIN (ETHOSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0e008f33-70a1-4bc6-b3a0-d45214418ab6
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=0e008f33-70a1-4bc6-b3a0-d45214418ab6; effective_time=20240715; title=Zarontin / ETHOSUXIMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220e008f33-70a1-4bc6-b3a0-d45214418ab6%22&limit=5

## MEDIUM ethosuximide / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: PubMed supports neither inducer nor inhibitor; FDA labeling supports specific phenytoin/valproate interaction wording.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9606477/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf
- Current: N/A - selected FDA label does not define clinically meaningful enzyme induction or inhibition; label notes interactions with other antiepileptic drug serum levels.
- Proposed: Neither enzyme-inducing nor enzyme-inhibiting; ethosuximide may increase phenytoin levels, and valproic acid has been reported to both increase and decrease ethosuximide levels.

## MEDIUM ethosuximide / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: False
- Summary: Ethosuximide is not a meaningful inducer or inhibitor of drug metabolism in the cited PubMed review.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9606477/
- Current: Unknown/limited
- Proposed: None / not clinically meaningful

## MEDIUM ethosuximide / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: NIH/NCBI provides a half-life range; N/A is incomplete.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK544244/
- Current: N/A - selected FDA/DailyMed label does not provide a half-life value.
- Proposed: 30 hours in children; 50-60 hours in adults.

## MEDIUM ethosuximide / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: False
- Summary: NIH/NCBI and PubMed identify hepatic/CYP metabolism.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK544244/; https://pubmed.ncbi.nlm.nih.gov/12637244/
- Current: N/A - selected FDA/DailyMed label does not identify a major metabolic organ; label advises caution and monitoring with liver or renal disease.
- Proposed: Hepatic metabolism; about 80% metabolized to inactive metabolites, primarily by CYP3A4.

## MEDIUM ethosuximide / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: False
- Summary: Trusted sources identify hepatic/CYP metabolism.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK544244/; https://pubmed.ncbi.nlm.nih.gov/12637244/
- Current: Limited/unknown
- Proposed: Hepatic; CYP3A4

## MEDIUM ethosuximide / proposed_row_update
- Field: filter_mechanism
- Status: proposed
- Approval required: False
- Summary: NIH/NCBI describes the anti-absence mechanism through low-threshold T-type calcium current/channel effects.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK544244/
- Current: Other / unclear
- Proposed: T-type calcium channel blocker

## MEDIUM ethosuximide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The current mechanism wording is supported directly by FDA labeling PDFs, without needing DailyMed as a cited source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA-approved labeling

## CRITICAL ethosuximide / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: True
- Summary: Ethosuximide is the generic name, not a distinct trade name; removing it from trade_names requires user approval because it removes existing CSV text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf
- Current: Ethosuximide; Zarontin
- Proposed: Zarontin

## MEDIUM ethosuximide / proposed_row_update
- Field: filter_qt_effect
- Status: proposed
- Approval required: False
- Summary: FDA label silence supports the narrower label-based statement, not a definitive no-effect claim from QT-specific evidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/012380s037lbl.pdf
- Current: No known meaningful QT effect
- Proposed: No QT effect described in FDA label

## MEDIUM ethosuximide / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Refresh audit date and clarify why the major ethosuximide CAE RCT is excluded from placebo-differential outcome fields.
- Sources: https://pubmed.ncbi.nlm.nih.gov/20200383/
- Current: No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-19-2026; RCT section set to N/A per current scope.
- Proposed: No qualifying phase II/III placebo-controlled randomized epilepsy RCT identified as of 05-20-2026; active-controlled CAE trial PMID 20200383 is not placebo-controlled and was not retained for placebo-differential outcomes.

## HIGH ethotoin / fact_check
- Field: epilepsy_type
- Status: incorrect
- Approval required: False
- Summary: FDA Peganone labeling states these labeled seizure indications; the row should not remain unspecified.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)
- Proposed: Tonic-clonic (grand mal) and complex partial (psychomotor) seizures

## HIGH ethotoin / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: False
- Summary: FDA Peganone labeling provides half-life information; the no-label rationale is contradicted by FDA labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: 3-9 hours at plasma concentrations below about 8 mcg/mL; FDA label also notes a reported half-life of 6-9 hours with 4-6 hour dosing intervals.

## HIGH ethotoin / fact_check
- Field: major_organ_for_metabolism
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports hepatic metabolism/biotransformation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Liver; FDA label states ethotoin is apparently biotransformed by the liver.

## HIGH ethotoin / fact_check
- Field: mechanism_of_action
- Status: incorrect
- Approval required: False
- Summary: FDA Peganone labeling provides a limited, phenytoin-like mechanism statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Hydantoin antiepileptic; mechanism probably similar to phenytoin: stabilizes rather than raises seizure threshold and prevents spread of seizure activity.

## HIGH ethotoin / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The Orange Book/Drugs@FDA product listing supports product status, not mechanism. The mechanism statement is supported by FDA labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: FDA Orange Book products file
- Proposed: FDA Peganone (ethotoin) labeling (accessdata.fda.gov; NDA010841/S-022)

## HIGH ethotoin / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The mechanism source should be the FDA label, not the Orange Book product listing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Historical/limited
- Proposed: FDA labeling

## HIGH ethotoin / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: FDA labeling exists and includes metabolism/drug-interaction discussion, but it does not establish a clear enzyme induction/inhibition classification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe enzyme induction or inhibition.
- Proposed: Limited/unknown: FDA label does not document ethotoin enzyme induction/inhibition; it notes saturable metabolism and cautions that a phenytoin-like coumarin anticoagulant interaction may occur without documentation.

## HIGH ethotoin / fact_check
- Field: maximum_approved_daily_dose
- Status: incorrect
- Approval required: False
- Summary: FDA labeling gives usual adult maintenance dosing of 2 to 3 g daily.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a maximum approved daily dose.
- Proposed: 3 g/day (upper end of usual adult maintenance dose; label does not state a separate maximum)

## HIGH ethotoin / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: FDA labeling provides an adult lower effective threshold statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a minimum effective dose.
- Proposed: Adults: 2 g/day; FDA label states less than 2 g/day has been ineffective in most adults.

## HIGH ethotoin / fact_check
- Field: typical_doses_per_day
- Status: incorrect
- Approval required: False
- Summary: FDA Peganone labeling specifies administration in 4 to 6 divided daily doses after food.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide dosing.
- Proposed: 4 to 6 divided doses daily, after food.

## HIGH ethotoin / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: FDA labeling exists and lists adverse reactions without percentages; the Orange Book/product listing does not provide AE incidence data.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A: FDA Peganone label lists adverse reactions qualitatively and does not provide adverse-event incidence percentages.

## HIGH ethotoin / fact_check
- Field: qt_interval_effect
- Status: incorrect
- Approval required: False
- Summary: The QT fact remains limited/unknown, but the source rationale should use FDA labeling rather than no-label wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe QT effect.
- Proposed: N/A - FDA Peganone label does not describe a QT-interval effect.

## HIGH ethotoin / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be used for boxed-warning verification, and Orange Book/product files do not support mechanism, dosing, half-life, metabolism, or adverse-reaction details. FDA label and PubMed sources should be named.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22ETHOTOIN%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/?term=%28ethotoin%5BTitle%2FAbstract%5D+OR+Peganone%5BTitle%2FAbstract%5D%29+AND+%28randomized+OR+randomised+OR+placebo+OR+trial%29
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA/openFDA Drugs@FDA; FDA Peganone labeling (accessdata.fda.gov); PubMed

## HIGH ethotoin / fact_check
- Field: filter_epilepsy_type
- Status: incorrect
- Approval required: False
- Summary: FDA labeling identifies specific seizure categories.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Historical/unspecified epilepsy
- Proposed: Tonic-clonic and complex partial seizures

## HIGH ethotoin / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: False
- Summary: FDA labeling states ethotoin is apparently biotransformed by the liver.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Limited/unknown
- Proposed: Hepatic

## HIGH ethotoin / fact_check
- Field: filter_mechanism
- Status: incorrect
- Approval required: False
- Summary: FDA labeling identifies ethotoin as a hydantoin antiepileptic with probable phenytoin-like mechanism.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Other / unclear
- Proposed: Hydantoin / phenytoin-like (limited confidence)

## INFO ethotoin / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is not applicable because the outcome is N/A.

## INFO ethotoin / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is not applicable because the outcome is N/A.

## INFO ethotoin / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is not applicable because the outcome is N/A.

## HIGH ethotoin / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for this field. The FDA/openFDA label API query returned no current openFDA SPL label for ethotoin/Peganone, but FDA accessdata labeling for Peganone exists and contains Warnings/Medication Guide content without a boxed-warning section.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22ETHOTOIN%22+OR+openfda.brand_name:%22PEGANONE%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: No current FDA/DailyMed label identified.
- Proposed: No FDA boxed warning identified in FDA Peganone (ethotoin) labeling reviewed.

## MEDIUM ethotoin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: DailyMed is not allowed for boxed-warning verification, and the FDA label/PubMed are needed to support retained pharmacology, dosing, adverse-reaction, and RCT-gap facts.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22ETHOTOIN%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/?term=%28ethotoin%5BTitle%2FAbstract%5D+OR+Peganone%5BTitle%2FAbstract%5D%29+AND+%28randomized+OR+randomised+OR+placebo+OR+trial%29
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA/openFDA Drugs@FDA; FDA Peganone labeling (accessdata.fda.gov); PubMed

## MEDIUM ethotoin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Boxed-warning verification must use FDA/openFDA/FDA label sources only.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22ETHOTOIN%22+OR+openfda.brand_name:%22PEGANONE%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [ethotoin; Peganone].
- Proposed: FDA/openFDA label API search on 05-20-2026 found no current openFDA SPL label for openfda.generic_name="ETHOTOIN" or openfda.brand_name="PEGANONE"; FDA accessdata Peganone label (NDA010841/S-022, May 2010) reviewed and no boxed-warning section/text was identified.

## MEDIUM ethotoin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The mechanism statement is present in FDA labeling, not in the Orange Book/product listing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: FDA Orange Book products file
- Proposed: FDA Peganone (ethotoin) labeling (accessdata.fda.gov; NDA010841/S-022)

## MEDIUM ethotoin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Existing named sources do not support multiple retained clinical pharmacology/dosing facts, and DailyMed is not permissible for boxed-warning verification.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22ETHOTOIN%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/?term=%28ethotoin%5BTitle%2FAbstract%5D+OR+Peganone%5BTitle%2FAbstract%5D%29+AND+%28randomized+OR+randomised+OR+placebo+OR+trial%29
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA/openFDA Drugs@FDA; FDA Peganone labeling (accessdata.fda.gov); PubMed

## MEDIUM ethotoin / proposed_row_update
- Field: available_in_us
- Status: proposed
- Approval required: False
- Summary: FDA/openFDA directly verifies discontinued Peganone oral tablet products.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22ETHOTOIN%22&limit=5
- Current: No - discontinued FDA Orange Book product
- Proposed: No - discontinued FDA/openFDA Drugs@FDA product

## MEDIUM ethotoin / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: FDA accessdata labeling exists; boxed-warning field should state FDA-label boxed-warning status and avoid DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22ETHOTOIN%22+OR+openfda.brand_name:%22PEGANONE%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: No current FDA/DailyMed label identified.
- Proposed: No FDA boxed warning identified in FDA Peganone (ethotoin) labeling reviewed.

## MEDIUM ethotoin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Use FDA/openFDA and FDA accessdata only for boxed-warning verification.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22ETHOTOIN%22+OR+openfda.brand_name:%22PEGANONE%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [ethotoin; Peganone].
- Proposed: FDA/openFDA label API search on 05-20-2026 found no current openFDA SPL label for openfda.generic_name="ETHOTOIN" or openfda.brand_name="PEGANONE"; FDA accessdata Peganone label (NDA010841/S-022, May 2010) reviewed and no boxed-warning section/text was identified.

## MEDIUM ethotoin / proposed_row_update
- Field: epilepsy_type
- Status: proposed
- Approval required: False
- Summary: FDA label provides the labeled seizure categories.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)
- Proposed: Tonic-clonic (grand mal) and complex partial (psychomotor) seizures

## MEDIUM ethotoin / proposed_row_update
- Field: filter_epilepsy_type
- Status: proposed
- Approval required: False
- Summary: Align filter with FDA-labeled seizure categories.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Historical/unspecified epilepsy
- Proposed: Tonic-clonic and complex partial seizures

## MEDIUM ethotoin / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: False
- Summary: FDA sources support tablet formulation and historical strengths.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf; https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22ETHOTOIN%22&limit=5
- Current: Historical oral tablet (not marketed in U.S.)
- Proposed: Historical oral tablets: Peganone 250 mg in FDA label; FDA/openFDA Drugs@FDA lists discontinued Peganone oral tablet products at 250 mg and 500 mg.

## MEDIUM ethotoin / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: FDA Peganone label provides half-life data.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: 3-9 hours at plasma concentrations below about 8 mcg/mL; FDA label also notes a reported half-life of 6-9 hours with 4-6 hour dosing intervals.

## MEDIUM ethotoin / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: False
- Summary: FDA Peganone label supports hepatic metabolism.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Liver; FDA label states ethotoin is apparently biotransformed by the liver.

## MEDIUM ethotoin / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: False
- Summary: FDA label supports liver biotransformation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Limited/unknown
- Proposed: Hepatic

## MEDIUM ethotoin / proposed_row_update
- Field: mechanism_of_action
- Status: proposed
- Approval required: False
- Summary: FDA Peganone label supports a limited phenytoin-like mechanism statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Hydantoin antiepileptic; mechanism probably similar to phenytoin: stabilizes rather than raises seizure threshold and prevents spread of seizure activity.

## MEDIUM ethotoin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supported by FDA label, not Orange Book/product listing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: FDA Orange Book products file
- Proposed: FDA Peganone (ethotoin) labeling (accessdata.fda.gov; NDA010841/S-022)

## MEDIUM ethotoin / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: Correct source tier for the mechanism statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Historical/limited
- Proposed: FDA labeling

## MEDIUM ethotoin / proposed_row_update
- Field: filter_mechanism
- Status: proposed
- Approval required: False
- Summary: FDA label identifies ethotoin as a hydantoin with probable phenytoin-like mechanism.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: Other / unclear
- Proposed: Hydantoin / phenytoin-like (limited confidence)

## MEDIUM ethotoin / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: FDA label exists and gives limited metabolism/interaction information.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe enzyme induction or inhibition.
- Proposed: Limited/unknown: FDA label does not document ethotoin enzyme induction/inhibition; it notes saturable metabolism and cautions that a phenytoin-like coumarin anticoagulant interaction may occur without documentation.

## MEDIUM ethotoin / proposed_row_update
- Field: maximum_approved_daily_dose
- Status: proposed
- Approval required: False
- Summary: FDA label provides usual adult maintenance dose of 2 to 3 g daily.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a maximum approved daily dose.
- Proposed: 3 g/day (upper end of usual adult maintenance dose; label does not state a separate maximum)

## MEDIUM ethotoin / proposed_row_update
- Field: minimum_effective_dose
- Status: proposed
- Approval required: False
- Summary: FDA label supports adult minimum-effective threshold wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a minimum effective dose.
- Proposed: Adults: 2 g/day; FDA label states less than 2 g/day has been ineffective in most adults.

## MEDIUM ethotoin / proposed_row_update
- Field: typical_doses_per_day
- Status: proposed
- Approval required: False
- Summary: FDA label provides dosing frequency.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide dosing.
- Proposed: 4 to 6 divided doses daily, after food.

## MEDIUM ethotoin / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: FDA label exists but adverse reactions are qualitative, not percentage-based.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A: FDA Peganone label lists adverse reactions qualitatively and does not provide adverse-event incidence percentages.

## MEDIUM ethotoin / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: False
- Summary: Retain unknown QT effect but correct source rationale.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010841s022lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe QT effect.
- Proposed: N/A - FDA Peganone label does not describe a QT-interval effect.

## MEDIUM ethotoin / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: FDA/openFDA provides a more precise original approval date.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22ETHOTOIN%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2010/010841s022ltr.pdf
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: 1957 (FDA/openFDA Drugs@FDA original approval Apr 22, 1957; Orange Book may display Approved prior to Jan 1, 1982)

## MEDIUM ethotoin / proposed_row_update
- Field: status_or_notes
- Status: proposed
- Approval required: False
- Summary: FDA/openFDA supports exact NDA, approval date, and discontinued status.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=products.active_ingredients.name:%22ETHOTOIN%22&limit=5
- Current: FDA Orange Book pre-1982 legacy ASM product (Peganone); discontinued U.S. product listing.
- Proposed: FDA/openFDA Drugs@FDA legacy ASM product (Peganone; NDA010841; original approval Apr 22, 1957); discontinued U.S. product listing.

## MEDIUM ethotoin / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Refresh date and document non-qualifying PubMed hits.
- Sources: https://pubmed.ncbi.nlm.nih.gov/?term=%28ethotoin%5BTitle%2FAbstract%5D+OR+Peganone%5BTitle%2FAbstract%5D%29+AND+%28randomized+OR+randomised+OR+placebo+OR+trial%29; https://pubmed.ncbi.nlm.nih.gov/1973383/; https://pubmed.ncbi.nlm.nih.gov/7194443/
- Current: No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-19-2026; RCT section set to N/A per current scope.
- Proposed: No qualifying phase II/III placebo-controlled randomized epilepsy RCT found in PubMed search as of 05-20-2026; PMID 1973383 is retrospective adjunctive ethotoin therapy and PMID 7194443 is not an ethotoin efficacy RCT.

## HIGH everolimus / fact_check
- Field: trade_names
- Status: missing
- Approval required: False
- Summary: Current names are valid. Zortress is also an FDA everolimus trade name and is relevant because the boxed warning applies to transplant-label everolimus products. Do not add "Everolimus" as a trade name; that is the generic name.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf; https://www.ema.europa.eu/en/medicines/human/EPAR/votubia; https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/021560s021lbl.pdf
- Current: Afinitor; Afinitor Disperz; Votubia
- Proposed: Afinitor; Afinitor Disperz; Votubia; Zortress

## HIGH everolimus / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; replace DailyMed wording with an FDA/accessdata source for trusted-source concordance.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata AFINITOR/AFINITOR DISPERZ labeling

## CRITICAL everolimus / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: The row text and FDA label support substrate/affected-by-modulators classification. The "Inhibitor" filter is not supported as clinically meaningful.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf
- Current: Inhibitor; Substrate / affected by modulators
- Proposed: Substrate / affected by modulators

## CRITICAL everolimus / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The current row mixes or misstates percentages for TSC-associated seizure use. FDA EXIST-3 high-trough AFINITOR DISPERZ data support stomatitis 64%, diarrhea 22%, vomiting 10%, nasopharyngitis 16%, upper respiratory tract infection 15%, pyrexia 14%, cough 10%, and rash 10%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf
- Current: GI/oral: stomatitis 64%, infectious: infection 50%, GI: diarrhea 24%, dermatologic: rash 21%, respiratory: cough 20%, constitutional: fatigue 14%
- Proposed: GI/oral: stomatitis 64%; GI: diarrhea 22%, vomiting 10%; infectious: nasopharyngitis 16%, upper respiratory tract infection 15%; constitutional: pyrexia 14%; respiratory: cough 10%; dermatologic: rash 10%

## HIGH everolimus / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Healthline is outside the requested trusted domains, and DailyMed should not be used for boxed-warning verification. FDA, PubMed, ClinicalTrials.gov, and EMA sources support the retained facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5; https://pubmed.ncbi.nlm.nih.gov/27613521/; https://clinicaltrials.gov/study/NCT01713946; https://www.ema.europa.eu/en/medicines/human/EPAR/votubia
- Current: Epilepsy Society ASM list; Healthline ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata AFINITOR/AFINITOR DISPERZ labeling; FDA/openFDA labeling; PubMed; ClinicalTrials.gov; EMA Votubia EPAR

## HIGH everolimus / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for the FDA boxed-warning field; the FDA/openFDA API URL is the appropriate source.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=43ef3c29-0e25-4fdd-aea1-06a20af9bbab; published=Mar 02, 2026; title=EVEROLIMUS TABLET [AUROBINDO PHARMA LIMITED]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=43ef3c29-0e25-4fdd-aea1-06a20af9bbab
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=43ef3c29-0e25-4fdd-aea1-06a20af9bbab; effective_time=20260226; title=everolimus / EVEROLIMUS; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5

## HIGH everolimus / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed/ClinicalTrials.gov identify this as a phase II randomized, double-blind, placebo-controlled crossover everolimus trial in refractory seizures with focal cortical dysplasia type II (NCT03198949). Add if the CSV tracks all placebo-controlled seizure RCTs for the drug, with caveat that it is outside the FDA-approved TSC seizure indication.
- Sources: https://pubmed.ncbi.nlm.nih.gov/39607729/
- Proposed: Kim2024|https://pubmed.ncbi.nlm.nih.gov/39607729/

## MEDIUM everolimus / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box warning field must use FDA/openFDA, FDA label, or Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=43ef3c29-0e25-4fdd-aea1-06a20af9bbab; published=Mar 02, 2026; title=EVEROLIMUS TABLET [AUROBINDO PHARMA LIMITED]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=43ef3c29-0e25-4fdd-aea1-06a20af9bbab
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=43ef3c29-0e25-4fdd-aea1-06a20af9bbab; effective_time=20260226; title=everolimus / EVEROLIMUS; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5

## MEDIUM everolimus / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism source should cite FDA accessdata label rather than DailyMed wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata AFINITOR/AFINITOR DISPERZ labeling

## MEDIUM everolimus / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current evidence_sources includes non-trusted or non-preferred sources for this audit; replacement sources support the row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5; https://pubmed.ncbi.nlm.nih.gov/27613521/; https://clinicaltrials.gov/study/NCT01713946; https://www.ema.europa.eu/en/medicines/human/EPAR/votubia
- Current: Epilepsy Society ASM list; Healthline ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata AFINITOR/AFINITOR DISPERZ labeling; FDA/openFDA labeling; PubMed; ClinicalTrials.gov; EMA Votubia EPAR

## CRITICAL everolimus / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Corrects TSC-associated seizure EXIST-3 high-trough adverse-event percentages from FDA labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf
- Current: GI/oral: stomatitis 64%, infectious: infection 50%, GI: diarrhea 24%, dermatologic: rash 21%, respiratory: cough 20%, constitutional: fatigue 14%
- Proposed: GI/oral: stomatitis 64%; GI: diarrhea 22%, vomiting 10%; infectious: nasopharyngitis 16%, upper respiratory tract infection 15%; constitutional: pyrexia 14%; respiratory: cough 10%; dermatologic: rash 10%

## MEDIUM everolimus / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Adds an FDA-recognized everolimus trade name relevant to the boxed-warning/transplant labeling; current listed names remain valid.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/021560s021lbl.pdf; https://www.ema.europa.eu/en/medicines/human/EPAR/votubia
- Current: Afinitor; Afinitor Disperz; Votubia
- Proposed: Afinitor; Afinitor Disperz; Votubia; Zortress

## MEDIUM everolimus / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: False
- Summary: French2016 is verified. Kim2024 appears to be an additional phase II randomized placebo-controlled everolimus seizure trial in FCD II, outside the FDA-approved TSC seizure indication.
- Sources: https://pubmed.ncbi.nlm.nih.gov/27613521/; https://pubmed.ncbi.nlm.nih.gov/39607729/; https://clinicaltrials.gov/study/NCT03198949
- Current: French2016|https://pubmed.ncbi.nlm.nih.gov/27613521/
- Proposed: French2016|https://pubmed.ncbi.nlm.nih.gov/27613521/; Kim2024|https://pubmed.ncbi.nlm.nih.gov/39607729/

## MEDIUM everolimus / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Updates RCT audit notes and rejects deterministic false positives such as TSC tumor/cognition/commentary papers.
- Sources: https://pubmed.ncbi.nlm.nih.gov/27613521/; https://clinicaltrials.gov/study/NCT01713946; https://pubmed.ncbi.nlm.nih.gov/39607729/; https://clinicaltrials.gov/study/NCT03198949
- Current: PubMed loop 19/65 on 2026-05-15: 1 qualifying placebo-controlled randomized clinical trial report(s) retained from 9 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit 2026-05-20: French2016 (PMID 27613521) verified as phase 3 randomized double-blind placebo-controlled EXIST-3 everolimus/RAD001 adjunctive seizure trial in TSC-associated treatment-resistant focal-onset seizures. Kim2024 (PMID 39607729; NCT03198949) identified as an additional phase 2 randomized double-blind placebo-controlled crossover seizure trial in focal cortical dysplasia type II, outside the FDA-approved TSC seizure indication. Non-seizure TSC tumor/cognition/commentary reports should not be retained as ASM seizure-efficacy RCTs.

## MEDIUM everolimus / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces non-trusted/unsupported source names with trusted domains used for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5; https://pubmed.ncbi.nlm.nih.gov/27613521/; https://clinicaltrials.gov/study/NCT01713946; https://www.ema.europa.eu/en/medicines/human/EPAR/votubia
- Current: Epilepsy Society ASM list; Healthline ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata AFINITOR/AFINITOR DISPERZ labeling; FDA/openFDA labeling; PubMed; ClinicalTrials.gov; EMA Votubia EPAR

## MEDIUM everolimus / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supported by FDA accessdata labeling; DailyMed wording should be removed from the cited source text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata AFINITOR/AFINITOR DISPERZ labeling

## MEDIUM everolimus / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed cannot be used for FDA boxed-warning verification; FDA/openFDA source is required.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=43ef3c29-0e25-4fdd-aea1-06a20af9bbab; published=Mar 02, 2026; title=EVEROLIMUS TABLET [AUROBINDO PHARMA LIMITED]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=43ef3c29-0e25-4fdd-aea1-06a20af9bbab
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=43ef3c29-0e25-4fdd-aea1-06a20af9bbab; effective_time=20260226; title=everolimus / EVEROLIMUS; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2243ef3c29-0e25-4fdd-aea1-06a20af9bbab%22&limit=5

## CRITICAL everolimus / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: FDA labeling supports CYP3A4/P-gp substrate/affected-by-modulators status, not clinically meaningful inhibitor status.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/203985s023%2C022334s051lbl.pdf
- Current: Inhibitor; Substrate / affected by modulators
- Proposed: Substrate / affected by modulators

## CRITICAL ezogabine / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: The row's filter conflicts with the populated enzyme fact and FDA/NCBI sources; ezogabine is not a major CYP inhibitor.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548304/
- Current: Inhibitor
- Proposed: None/Not a major inducer or inhibitor

## HIGH ezogabine / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The EMA withdrawal page supports authorization withdrawal but not mechanism. EMA's EPAR summary, Sills/Rogawski, and LiverTox support the potassium-channel mechanism.
- Sources: https://www.ema.europa.eu/en/documents/overview/trobalt-epar-summary-public_en.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://www.ncbi.nlm.nih.gov/books/NBK548304/
- Current: EMA Trobalt withdrawal page; Sills and Rogawski 2020 ASM mechanism review
- Proposed: EMA Trobalt EPAR summary; Sills and Rogawski 2020 ASM mechanism review; NCBI LiverTox Ezogabine

## HIGH ezogabine / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The row cites an EMA EPAR-type source and a peer-reviewed mechanism review, not a UK SmPC located during audit.
- Sources: https://www.ema.europa.eu/en/documents/overview/trobalt-epar-summary-public_en.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: EMA/UK SmPC
- Proposed: EMA EPAR/peer-reviewed review

## CRITICAL ezogabine / fact_check
- Field: qt_interval_effect
- Status: incorrect
- Approval required: True
- Summary: FDA labeling documents a QT interval effect. The withdrawal-causation statement is contradicted by ILAE/GSK and EMA withdrawal notices, which state permanent discontinuation/withdrawal was for limited usage/commercial reasons.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.ilae.org/files/dmfile/GSK_RetigabineTrobalt-Reminder.pdf; https://www.ema.europa.eu/en/documents/public-statement/public-statement-trobalt-withdrawal-marketing-authorisation-european-union_en.pdf
- Current: QT prolongation not typical; urinary/retinal toxicity drove withdrawal
- Proposed: QT prolongation possible; FDA label reports mean 7.7-msec QT prolongation at 400 mg TID and recommends monitoring in at-risk patients. Global discontinuation was attributed by GSK/EMA to limited use/commercial reasons, not efficacy or safety.

## HIGH ezogabine / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be used for black-box verification, and the mechanism is supported by EMA EPAR rather than the EMA withdrawal page. FDA labeling and FDA safety communication should be named explicitly.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-determines-2013-labeling-adequate-manage-risk-retinal; https://www.ncbi.nlm.nih.gov/books/NBK548304/; https://www.ema.europa.eu/en/documents/overview/trobalt-epar-summary-public_en.pdf; https://www.ema.europa.eu/en/documents/public-statement/public-statement-trobalt-withdrawal-marketing-authorisation-european-union_en.pdf; https://www.ilae.org/files/dmfile/GSK_RetigabineTrobalt-Reminder.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: NCBI LiverTox anticonvulsants table; EMA Trobalt withdrawal page; ILAE/GSK discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling
- Proposed: FDA Potiga prescribing information; FDA Potiga Drug Safety Communication; NCBI LiverTox Ezogabine; EMA Trobalt EPAR summary and withdrawal statement; ILAE/GSK Trobalt/Potiga discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; cited PubMed RCTs

## INFO ezogabine / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: No plotted seizure-freedom differential is present; this is consistent with the NR seizure-freedom summary.
- Sources: https://pubmed.ncbi.nlm.nih.gov/27376872/; https://pubmed.ncbi.nlm.nih.gov/21451152/; https://pubmed.ncbi.nlm.nih.gov/20944074/; https://pubmed.ncbi.nlm.nih.gov/17420403/

## CRITICAL ezogabine / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: True
- Summary: The 2016 FDA Potiga label contains a boxed warning for retinal abnormalities and potential vision loss, and FDA's 2015 Drug Safety Communication explicitly refers to recommendations in the Boxed Warning. DailyMed should not be cited for this field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-determines-2013-labeling-adequate-manage-risk-retinal
- Current: No current FDA/DailyMed label identified.
- Proposed: Boxed warning in last FDA-approved Potiga label: retinal abnormalities and potential vision loss.

## CRITICAL ezogabine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: True
- Summary: FDA sources directly support a boxed warning; DailyMed is not permissible for this field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-determines-2013-labeling-adequate-manage-risk-retinal
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [ezogabine; retigabine; Potiga; Trobalt].
- Proposed: FDA Potiga prescribing information, May 2016, and FDA Drug Safety Communication, 06-16-2015: boxed warning for retinal abnormalities and potential vision loss identified for Potiga (ezogabine).

## MEDIUM ezogabine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Improves source specificity and removes DailyMed for black-box support.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-determines-2013-labeling-adequate-manage-risk-retinal; https://www.ncbi.nlm.nih.gov/books/NBK548304/; https://www.ema.europa.eu/en/documents/overview/trobalt-epar-summary-public_en.pdf; https://www.ema.europa.eu/en/documents/public-statement/public-statement-trobalt-withdrawal-marketing-authorisation-european-union_en.pdf; https://www.ilae.org/files/dmfile/GSK_RetigabineTrobalt-Reminder.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: NCBI LiverTox anticonvulsants table; EMA Trobalt withdrawal page; ILAE/GSK discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling
- Proposed: FDA Potiga prescribing information; FDA Potiga Drug Safety Communication; NCBI LiverTox Ezogabine; EMA Trobalt EPAR summary and withdrawal statement; ILAE/GSK Trobalt/Potiga discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; cited PubMed RCTs

## MEDIUM ezogabine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: EMA EPAR, not EMA withdrawal page, supports the mechanism cell.
- Sources: https://www.ema.europa.eu/en/documents/overview/trobalt-epar-summary-public_en.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://www.ncbi.nlm.nih.gov/books/NBK548304/
- Current: EMA Trobalt withdrawal page; Sills and Rogawski 2020 ASM mechanism review
- Proposed: EMA Trobalt EPAR summary; Sills and Rogawski 2020 ASM mechanism review; NCBI LiverTox Ezogabine

## CRITICAL ezogabine / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: True
- Summary: Directly contradicted by the 2016 FDA Potiga label and FDA safety communication.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-determines-2013-labeling-adequate-manage-risk-retinal
- Current: No current FDA/DailyMed label identified.
- Proposed: Boxed warning in last FDA-approved Potiga label: retinal abnormalities and potential vision loss.

## CRITICAL ezogabine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: True
- Summary: DailyMed is not permissible for black-box verification and FDA sources identify a boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-determines-2013-labeling-adequate-manage-risk-retinal
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [ezogabine; retigabine; Potiga; Trobalt].
- Proposed: FDA Potiga prescribing information, May 2016, and FDA Drug Safety Communication, 06-16-2015: boxed warning for retinal abnormalities and potential vision loss identified for Potiga (ezogabine).

## MEDIUM ezogabine / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Use the actual audit verification date for the corrected FDA boxed-warning finding.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## CRITICAL ezogabine / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: FDA/NCBI sources contradict CYP inhibitor classification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548304/
- Current: Inhibitor
- Proposed: None/Not a major inducer or inhibitor

## CRITICAL ezogabine / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: True
- Summary: FDA label supports QT effect; ILAE/GSK and EMA contradict safety-driven withdrawal wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.ilae.org/files/dmfile/GSK_RetigabineTrobalt-Reminder.pdf; https://www.ema.europa.eu/en/documents/public-statement/public-statement-trobalt-withdrawal-marketing-authorisation-european-union_en.pdf
- Current: QT prolongation not typical; urinary/retinal toxicity drove withdrawal
- Proposed: QT prolongation possible; FDA label reports mean 7.7-msec QT prolongation at 400 mg TID and recommends monitoring in at-risk patients. Global discontinuation was attributed by GSK/EMA to limited use/commercial reasons, not efficacy or safety.

## MEDIUM ezogabine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The withdrawal page supports market withdrawal, not mechanism; EMA EPAR and NCBI LiverTox support the mechanism.
- Sources: https://www.ema.europa.eu/en/documents/overview/trobalt-epar-summary-public_en.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/; https://www.ncbi.nlm.nih.gov/books/NBK548304/
- Current: EMA Trobalt withdrawal page; Sills and Rogawski 2020 ASM mechanism review
- Proposed: EMA Trobalt EPAR summary; Sills and Rogawski 2020 ASM mechanism review; NCBI LiverTox Ezogabine

## MEDIUM ezogabine / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: No UK SmPC source was verified in the cited row sources; the verified source tier is EMA EPAR plus peer-reviewed/NCBI evidence.
- Sources: https://www.ema.europa.eu/en/documents/overview/trobalt-epar-summary-public_en.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: EMA/UK SmPC
- Proposed: EMA EPAR/peer-reviewed review

## MEDIUM ezogabine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Names trusted sources that actually support the populated cells and removes DailyMed as a black-box source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-drug-safety-communication-fda-determines-2013-labeling-adequate-manage-risk-retinal; https://www.ncbi.nlm.nih.gov/books/NBK548304/; https://www.ema.europa.eu/en/documents/overview/trobalt-epar-summary-public_en.pdf; https://www.ema.europa.eu/en/documents/public-statement/public-statement-trobalt-withdrawal-marketing-authorisation-european-union_en.pdf; https://www.ilae.org/files/dmfile/GSK_RetigabineTrobalt-Reminder.pdf; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: NCBI LiverTox anticonvulsants table; EMA Trobalt withdrawal page; ILAE/GSK discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling
- Proposed: FDA Potiga prescribing information; FDA Potiga Drug Safety Communication; NCBI LiverTox Ezogabine; EMA Trobalt EPAR summary and withdrawal statement; ILAE/GSK Trobalt/Potiga discontinuation notice; Sills and Rogawski 2020 ASM mechanism review; cited PubMed RCTs

## MEDIUM ezogabine / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: Adds exact EMA authorization and withdrawal dates from EMA withdrawal statement.
- Sources: https://www.ema.europa.eu/en/documents/public-statement/public-statement-trobalt-withdrawal-marketing-authorisation-european-union_en.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/022345s011lbl.pdf
- Current: 2011 FDA approval; EMA Trobalt/retigabine marketing authorisation granted 2011 and withdrawn 2018
- Proposed: 2011 FDA approval; EMA Trobalt/retigabine marketing authorisation granted 28 Mar 2011 and withdrawn 19 Jul 2018

## MEDIUM felbamate / fact_check
- Field: minimum_effective_dose
- Status: missing_source
- Approval required: False
- Summary: The FDA label supports 1200 mg/day as the recommended adult starting dose. It does not establish this as a formal minimum effective dose.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf
- Current: 1200 mg/day
- Proposed: 1200 mg/day (recommended adult initial dose; not independently established as a minimum effective dose)

## CRITICAL felbamate / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: True
- Summary: FDA labeling states a terminal half-life of 20-23 hours in subjects with normal renal function. The label separately notes renal impairment prolongs half-life by 9-15 hours, but does not support 14-23 h as the normal range.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf
- Current: 14-23 h
- Proposed: 20-23 h

## MEDIUM felbamate / fact_check
- Field: mechanism_source_tier
- Status: missing_source
- Approval required: False
- Summary: The FDA label supports the 'unknown mechanism' and preclinical NMDA/GABA statements; the Sills and Rogawski review supports broader ASM mechanism classification. Current tier omits the peer-reviewed component used by the cell.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32165193/
- Current: FDA label
- Proposed: FDA label; peer-reviewed review

## MEDIUM felbamate / fact_check
- Field: qt_interval_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: The FDA label describes no clinically significant mean blood-pressure or heart-rate changes, but it does not provide a dedicated QT/QTc study statement. The current value is plausible but stronger than the located source support.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: No QT/QTc warning or clinically meaningful QT effect identified in reviewed FDA labeling

## CRITICAL felbamate / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The current row mixes or rounds unsupported percentages. FDA adult add-on controlled-trial table gives headache 36.8%, nausea 34.2%, anorexia 19.3%, vomiting 16.7%, insomnia 17.5%. The boxed warning states aplastic anemia/hepatic failure risks are serious and not reliably quantified, so '<1%' is not source-supported.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf
- Current: GI: anorexia 19%, GI: vomiting 17%, CNS: insomnia 16%, GI: nausea 12%, CNS: headache 12%, hematologic/hepatic: aplastic anemia/hepatic failure <1%
- Proposed: Adult controlled add-on trials: CNS: headache 36.8%, somnolence 19.3%, dizziness 18.4%, insomnia 17.5%; GI: nausea 34.2%, anorexia 19.3%, vomiting 16.7%, dyspepsia 12.3%; hematologic/hepatic: aplastic anemia and hepatic failure are boxed-warning risks and incidence is not reliably quantified in labeling.

## HIGH felbamate / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Wikipedia is not a trusted source for this audit, and DailyMed is not permissible for FDA boxed-warning verification. The proposed source list uses trusted domains and matches the row facts more directly.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548256/; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=33488; https://pubmed.ncbi.nlm.nih.gov/32165193/; https://www.ema.europa.eu/en/medicines/human/EPAR/taloxa
- Current: NCBI LiverTox anticonvulsants table; Wikipedia anticonvulsant drug-class list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling; NCBI LiverTox felbamate; FDA orphan drug approval record; PubMed RCT records; Sills and Rogawski 2020 ASM mechanism review; EMA Taloxa EPAR for non-US trade name

## CRITICAL felbamate / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: PMID 8347179 verifies the 23 percentage-point differential from 19% decrease versus 4% increase in total seizure frequency. However, the cited PubMed abstract does not describe this as a median percent change, so the current MPC wording overstates the metric specificity.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8347179/; https://www.fda.gov/media/158280/download
- Current: 23 % (drug minus placebo MPC differential at maximum effective dose/regimen: FelbamateStudyGroupinLennoxGastautSyndrome1993 felbamate up to 45 mg/kg/day or 3600 mg/day 23%)
- Proposed: 23 percentage points (felbamate 19% decrease in total seizure frequency vs placebo 4% increase; FelbamateStudyGroupinLennoxGastautSyndrome1993, felbamate up to 45 mg/kg/day or 3600 mg/day; not confirmed as a median percent change in the PubMed abstract)

## MEDIUM felbamate / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed source is not permitted for boxed-warning verification by the audit instructions.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=2f522701-397a-11de-8a39-0800200c9a66; published=Dec 31, 2025; title=FELBATOL (FELBAMATE) TABLET FELBATOL (FELBAMATE) SUSPENSION [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2f522701-397a-11de-8a39-0800200c9a66
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2f522701-397a-11de-8a39-0800200c9a66; effective_time=20250815; title=Felbatol / FELBAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5

## MEDIUM felbamate / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current source list includes Wikipedia and DailyMed; trusted row support should use FDA/openFDA/accessdata, NCBI/PubMed, and EMA sources.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548256/; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=33488; https://pubmed.ncbi.nlm.nih.gov/32165193/; https://www.ema.europa.eu/en/medicines/human/EPAR/taloxa
- Current: NCBI LiverTox anticonvulsants table; Wikipedia anticonvulsant drug-class list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling; NCBI LiverTox felbamate; FDA orphan drug approval record; PubMed RCT records; Sills and Rogawski 2020 ASM mechanism review; EMA Taloxa EPAR for non-US trade name

## MEDIUM felbamate / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed naming with FDA/openFDA or accessdata FDA labeling while retaining the peer-reviewed review source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32165193/
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/openFDA or FDA/accessdata labeling; Sills and Rogawski 2020 ASM mechanism review

## MEDIUM felbamate / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification in this audit; use FDA/openFDA metadata instead.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=2f522701-397a-11de-8a39-0800200c9a66; published=Dec 31, 2025; title=FELBATOL (FELBAMATE) TABLET FELBATOL (FELBAMATE) SUSPENSION [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2f522701-397a-11de-8a39-0800200c9a66
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2f522701-397a-11de-8a39-0800200c9a66; effective_time=20250815; title=Felbatol / FELBAMATE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5

## CRITICAL felbamate / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: FDA labeling supports terminal half-life 20-23 hours in normal renal function; 14-23 h was not verified against FDA label text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf
- Current: 14-23 h
- Proposed: 20-23 h

## CRITICAL felbamate / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Current percentages conflict with FDA adverse-event tables and '<1%' for aplastic anemia/hepatic failure is not supported by labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf
- Current: GI: anorexia 19%, GI: vomiting 17%, CNS: insomnia 16%, GI: nausea 12%, CNS: headache 12%, hematologic/hepatic: aplastic anemia/hepatic failure <1%
- Proposed: Adult controlled add-on trials: CNS: headache 36.8%, somnolence 19.3%, dizziness 18.4%, insomnia 17.5%; GI: nausea 34.2%, anorexia 19.3%, vomiting 16.7%, dyspepsia 12.3%; hematologic/hepatic: aplastic anemia and hepatic failure are boxed-warning risks and incidence is not reliably quantified in labeling.

## CRITICAL felbamate / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: 23 is verified, but the cited abstract supports a total seizure-frequency percent-change differential, not explicitly a median percent-change differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8347179/
- Current: 23 % (drug minus placebo MPC differential at maximum effective dose/regimen: FelbamateStudyGroupinLennoxGastautSyndrome1993 felbamate up to 45 mg/kg/day or 3600 mg/day 23%)
- Proposed: 23 percentage points (felbamate 19% decrease in total seizure frequency vs placebo 4% increase; FelbamateStudyGroupinLennoxGastautSyndrome1993, felbamate up to 45 mg/kg/day or 3600 mg/day; not confirmed as a median percent change in the PubMed abstract)

## MEDIUM felbamate / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use trusted audit sources and remove Wikipedia/DailyMed dependency.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222f522701-397a-11de-8a39-0800200c9a66%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548256/; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=33488; https://pubmed.ncbi.nlm.nih.gov/32165193/; https://www.ema.europa.eu/en/medicines/human/EPAR/taloxa
- Current: NCBI LiverTox anticonvulsants table; Wikipedia anticonvulsant drug-class list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling; NCBI LiverTox felbamate; FDA orphan drug approval record; PubMed RCT records; Sills and Rogawski 2020 ASM mechanism review; EMA Taloxa EPAR for non-US trade name

## MEDIUM felbamate / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: DailyMed should not be relied on where FDA/openFDA or FDA label sources are available; mechanism claims are supported by FDA labeling and peer-reviewed review.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/32165193/
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/openFDA or FDA/accessdata labeling; Sills and Rogawski 2020 ASM mechanism review

## MEDIUM felbamate / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: False
- Summary: The row's stronger negative QT claim is not directly established in located FDA labeling; the proposed text is limited to reviewed source evidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/020189s027lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: No QT/QTc warning or clinically meaningful QT effect identified in reviewed FDA labeling

## HIGH fenfluramine / fact_check
- Field: generic_name / trade_names / alternate_generic_names / pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Generic name fenfluramine, Fintepla, and ZX008 are supported. FDA clinical review also identifies historical Pondimin/Ponderex and fenfluramine HCl, so the empty alternate_generic_names field and current trade_names omit important aliases. Dexfenfluramine/Redux is a distinct d-enantiomer, not a fenfluramine alias.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; https://www.fda.gov/media/158280/download; https://clinicaltrials.gov/study/NCT02682927; https://clinicaltrials.gov/study/NCT03355209
- Current: fenfluramine; trade_names=Fintepla; alternate_generic_names blank; pubmed_search_aliases=ZX008
- Proposed: alternate_generic_names: fenfluramine hydrochloride; fenfluramine HCl. trade_names: Fintepla; Pondimin (historical/withdrawn anorectic); Ponderex (historical/withdrawn anorectic). Keep pubmed_search_aliases: ZX008.

## CRITICAL fenfluramine / fact_check
- Field: metabolism_enzyme_fields
- Status: incorrect
- Approval required: True
- Summary: FDA labeling supports 20-hour half-life, metabolism primarily by CYP1A2/CYP2B6/CYP2D6, and no clinically relevant CYP induction or inhibition by fenfluramine/norfenfluramine. The filter_enzyme_effect value contradicts this.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: half_life_range=~20 h; major_organ_for_metabolism=Liver; enzyme_inducing_or_inhibiting=Not a major enzyme inducer/inhibitor; CYP2D6/1A2/2B6 metabolism; filter_enzyme_effect=Inducer; Inhibitor
- Proposed: enzyme_inducing_or_inhibiting: Not a major enzyme inducer/inhibitor; primarily metabolized by CYP1A2, CYP2B6, and CYP2D6. filter_enzyme_effect: Neither inducer nor inhibitor.

## MEDIUM fenfluramine / fact_check
- Field: mechanism_fields
- Status: missing_source
- Approval required: True
- Summary: FDA labeling supports unknown mechanism and serotonin 5-HT2 receptor agonist activity, but not sigma-1 modulation. DailyMed and AES are not acceptable trusted source entries for this audit bundle as written.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: mechanism_of_action includes unknown seizure mechanism, serotonin 5-HT2 agonist activity, and proposed sigma-1 modulation; mechanism_source=FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary; mechanism_source_tier=FDA label; filter_mechanism=Serotonin / sigma
- Proposed: If using FDA-only support: Precise seizure mechanism is unknown; fenfluramine and norfenfluramine exhibit agonist activity at serotonin 5-HT2 receptors. If retaining sigma-1 modulation, add a trusted PubMed/NCBI peer-reviewed mechanism source and change mechanism_source_tier away from FDA-only.

## CRITICAL fenfluramine / fact_check
- Field: qt_fields
- Status: incorrect
- Approval required: True
- Summary: FDA labeling states FINTEPLA did not prolong QT at 4 times the maximum recommended dose. The filter value should not include QT prolongation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: qt_interval_effect=No clinically meaningful QT prolongation in labeling; cardiac valvulopathy/pulmonary hypertension monitoring required; filter_qt_effect=No known meaningful QT effect; QT prolongation
- Proposed: qt_interval_effect: No clinically meaningful QT prolongation in labeling; cardiac valvulopathy/pulmonary hypertension monitoring required. filter_qt_effect: No known meaningful QT effect.

## CRITICAL fenfluramine / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: FDA adverse-reaction tables do not support fatigue/lethargy 16% or somnolence 13% for the maximum labeled dose arms. VHD/PAH absence in controlled/extension trial monitoring is supported, with postmarketing cases noted in labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: GI: decreased appetite 38%, constitutional: fatigue/lethargy 16%, GI: diarrhea 15%, CNS: somnolence 13%, cardiac: valvular heart disease 0% in controlled trials
- Proposed: At labeled 0.7 mg/kg/day arms: decreased appetite 38% (DS) / 36% (LGS); somnolence/sedation/lethargy 25% (DS) / 22% (LGS); diarrhea 15% (DS) / 13% (LGS); fatigue/malaise/asthenia 10% (DS) / 24% (LGS). No VHD/PAH occurred in DS/LGS clinical trials up to 3 years, but postmarketing VHD/PAH cases have been reported.

## HIGH fenfluramine / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The named Epilepsy Society and AES sources are not in the trusted-source domain list provided for this audit, and DailyMed is not permissible for boxed-warning verification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5; https://clinicaltrials.gov/study/NCT02682927; https://clinicaltrials.gov/study/NCT02926898; https://clinicaltrials.gov/study/NCT03355209
- Current: evidence_sources=Epilepsy Society ASM list; FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary
- Proposed: FDA/accessdata prescribing information; FDA/openFDA drug label API; FDA approval letters and clinical review; ClinicalTrials.gov; PubMed RCT records

## HIGH fenfluramine / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_placebo_rct
- Approval required: True
- Summary: The article analyzes responder thresholds and NNT from existing fenfluramine RCT data. It is useful secondary evidence but is not itself a primary placebo-controlled phase II/III RCT report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33540241/
- Current: https://pubmed.ncbi.nlm.nih.gov/33540241/
- Proposed: Reclassify as secondary responder/NNT analysis; remove from pubmed_phase_ii_iii_rct_links if that field is reserved for primary RCT reports.

## CRITICAL fenfluramine / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose / plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: The numeric values are supported by the cited RCT/outcome evidence, but the current wording overstates them as uniform drug-minus-placebo median percent-change differentials. Sullivan2023 and Nabbout2020 are placebo-adjusted/model-based greater reductions; Knupp2022 is an estimated median difference; Lagae2019 is the arithmetic median reduction difference.
- Sources: https://pubmed.ncbi.nlm.nih.gov/37543865/; https://pubmed.ncbi.nlm.nih.gov/35499850/; https://pubmed.ncbi.nlm.nih.gov/31790543/; https://pubmed.ncbi.nlm.nih.gov/31862249/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: 19.9-64.8 % described as drug-minus-placebo MPC differential for Sullivan2023, Knupp2022, Nabbout2020, Lagae2019
- Proposed: 19.9-64.8 % (reported placebo-adjusted or drug-minus-placebo seizure-frequency change at maximum effective dose/regimen: Sullivan2023 fenfluramine 0.7 mg/kg/day placebo-adjusted greater reduction in MCSF 64.8%; Knupp2022 fenfluramine 0.7 mg/kg/day estimated median difference vs placebo 19.9 percentage points; Nabbout2020 fenfluramine 0.4 mg/kg/day with stiripentol placebo-adjusted greater reduction in MCSF 54.0%; Lagae2019 fenfluramine 0.7 mg/kg/day median reduction 74.9% vs placebo 19.2%, arithmetic differential 55.7%).

## CRITICAL fenfluramine / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose / plot_diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: FDA labeling explicitly reports no-convulsive-seizure patient rates for the Dravet Study 1/2 maximum regimens, and Knupp2022 reports LGS seizure freedom by group. Therefore the blanket NR/not extractable value is not correct for all included RCT evidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/35499850/; https://pubmed.ncbi.nlm.nih.gov/31790543/; https://pubmed.ncbi.nlm.nih.gov/31862249/
- Current: NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen
- Proposed: -1 to 8 percentage points among extractable maximum-dose/regimen RCT sources: Lagae2019/Study 1 fenfluramine 0.7 mg/kg/day 8% vs 0% placebo, diff 8%; Nabbout2020/Study 2 fenfluramine 0.4 mg/kg/day with stiripentol 2% vs 0% placebo, diff 2%; Knupp2022/LGS fenfluramine 0.7 mg/kg/day 0% vs 1% placebo, diff -1 percentage point. Sullivan2023 complete seizure-freedom differential was not verified from a trusted accessible abstract in this audit.

## MEDIUM fenfluramine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for black-box warning verification; FDA/accessdata and openFDA are permissible.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=e88f360e-33ad-4cd6-b2de-5ef885857c5d; published=Nov 17, 2025; title=FINTEPLA (FENFLURAMINE) SOLUTION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e88f360e-33ad-4cd6-b2de-5ef885857c5d
- Proposed: FDA/accessdata prescribing information; status=boxed_warning_found; NDA=212102; label=212102s016; revised=04/2025; title=FINTEPLA (fenfluramine) oral solution; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; FDA/openFDA API url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e88f360e-33ad-4cd6-b2de-5ef885857c5d%22&limit=5

## MEDIUM fenfluramine / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: FDA source was rechecked during this audit on the current system date.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## MEDIUM fenfluramine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use only trusted domains and avoid DailyMed for boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; https://www.fda.gov/media/158280/download; https://clinicaltrials.gov/study/NCT02682927; https://clinicaltrials.gov/study/NCT02926898; https://clinicaltrials.gov/study/NCT03355209
- Current: Epilepsy Society ASM list; FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary
- Proposed: FDA/accessdata prescribing information; FDA/openFDA drug label API; FDA approval letters and clinical review; ClinicalTrials.gov; PubMed RCT records

## MEDIUM fenfluramine / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Important salt/alias names are used in FDA and trial records.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; https://clinicaltrials.gov/study/NCT02682927
- Proposed: fenfluramine hydrochloride; fenfluramine HCl

## MEDIUM fenfluramine / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: FDA clinical review identifies historical fenfluramine trade names; adding them reduces duplicate-row risk.
- Sources: https://www.fda.gov/media/158280/download
- Current: Fintepla
- Proposed: Fintepla; Pondimin (historical/withdrawn anorectic); Ponderex (historical/withdrawn anorectic)

## CRITICAL fenfluramine / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: FDA label states fenfluramine/norfenfluramine are not CYP inhibitors or inducers at clinically relevant concentrations.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: Inducer; Inhibitor
- Proposed: Neither inducer nor inhibitor

## CRITICAL fenfluramine / proposed_row_update
- Field: filter_qt_effect
- Status: proposed
- Approval required: True
- Summary: FDA label states FINTEPLA did not prolong QT at 4 times the maximum recommended dose.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: No known meaningful QT effect; QT prolongation
- Proposed: No known meaningful QT effect

## CRITICAL fenfluramine / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Current adverse-event percentages mix unsupported values with supported maximum-dose values.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf
- Current: GI: decreased appetite 38%, constitutional: fatigue/lethargy 16%, GI: diarrhea 15%, CNS: somnolence 13%, cardiac: valvular heart disease 0% in controlled trials
- Proposed: At labeled 0.7 mg/kg/day arms: decreased appetite 38% (DS) / 36% (LGS); somnolence/sedation/lethargy 25% (DS) / 22% (LGS); diarrhea 15% (DS) / 13% (LGS); fatigue/malaise/asthenia 10% (DS) / 24% (LGS). No VHD/PAH occurred in DS/LGS clinical trials up to 3 years, but postmarketing VHD/PAH cases have been reported.

## CRITICAL fenfluramine / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Numbers are supported, but current wording incorrectly treats all as the same median percent-change differential type.
- Sources: https://pubmed.ncbi.nlm.nih.gov/37543865/; https://pubmed.ncbi.nlm.nih.gov/35499850/; https://pubmed.ncbi.nlm.nih.gov/31790543/; https://pubmed.ncbi.nlm.nih.gov/31862249/
- Current: 19.9-64.8 % (drug minus placebo MPC differential at maximum effective dose/regimen: Sullivan2023 fenfluramine 0.7 mg/kg/day 64.8%; Knupp2022 fenfluramine 0.7 mg/kg/day 19.9%; Nabbout2020 fenfluramine 0.4 mg/kg/day with stiripentol 54%; Lagae2019 fenfluramine 0.7 mg/kg/day 55.7%)
- Proposed: 19.9-64.8 % (reported placebo-adjusted or drug-minus-placebo seizure-frequency change at maximum effective dose/regimen: Sullivan2023 fenfluramine 0.7 mg/kg/day placebo-adjusted greater reduction in MCSF 64.8%; Knupp2022 fenfluramine 0.7 mg/kg/day estimated median difference vs placebo 19.9 percentage points; Nabbout2020 fenfluramine 0.4 mg/kg/day with stiripentol placebo-adjusted greater reduction in MCSF 54.0%; Lagae2019 fenfluramine 0.7 mg/kg/day median reduction 74.9% vs placebo 19.2%, arithmetic differential 55.7%).

## CRITICAL fenfluramine / proposed_row_update
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Seizure-freedom/no-convulsive-seizure values are extractable for several maximum-dose/regimen RCTs.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/35499850/
- Current: NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records
- Proposed: -1 to 8 percentage points among extractable maximum-dose/regimen RCT sources: Lagae2019/Study 1 fenfluramine 0.7 mg/kg/day 8% vs 0% placebo, diff 8%; Nabbout2020/Study 2 fenfluramine 0.4 mg/kg/day with stiripentol 2% vs 0% placebo, diff 2%; Knupp2022/LGS fenfluramine 0.7 mg/kg/day 0% vs 1% placebo, diff -1 percentage point. Sullivan2023 complete seizure-freedom differential not verified from a trusted accessible abstract in this audit.

## CRITICAL fenfluramine / proposed_row_update
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Plot field is empty despite extractable study-level seizure-freedom/no-convulsive-seizure differentials.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/212102s016lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/35499850/
- Proposed: Lagae2019|8|https://pubmed.ncbi.nlm.nih.gov/31862249/|119; Nabbout2020|2|https://pubmed.ncbi.nlm.nih.gov/31790543/|87; Knupp2022|-1|https://pubmed.ncbi.nlm.nih.gov/35499850/|263

## CRITICAL fenfluramine / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: Sullivan2021 is a responder/NNT secondary analysis of trial data, not a primary phase II/III placebo-controlled RCT report. Reclassify rather than treat as a primary RCT link.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33540241/; https://clinicaltrials.gov/study/NCT02682927; https://clinicaltrials.gov/study/NCT02926898
- Current: Sullivan2023|https://pubmed.ncbi.nlm.nih.gov/37543865/; Knupp2022|https://pubmed.ncbi.nlm.nih.gov/35499850/; Sullivan2021|https://pubmed.ncbi.nlm.nih.gov/33540241/; Nabbout2020|https://pubmed.ncbi.nlm.nih.gov/31790543/; Lagae2019|https://pubmed.ncbi.nlm.nih.gov/31862249/
- Proposed: Sullivan2023|https://pubmed.ncbi.nlm.nih.gov/37543865/; Knupp2022|https://pubmed.ncbi.nlm.nih.gov/35499850/; Nabbout2020|https://pubmed.ncbi.nlm.nih.gov/31790543/; Lagae2019|https://pubmed.ncbi.nlm.nih.gov/31862249/

## CRITICAL fenfluramine / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: True
- Summary: Current note counts Sullivan2021 as a qualifying primary RCT report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33540241/
- Current: PubMed loop 22/65 on 2026-05-15: 5 qualifying placebo-controlled randomized clinical trial report(s) retained from 13 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit 2026-05-21: 4 primary phase II/III placebo-controlled randomized trial reports retained (Sullivan2023, Knupp2022, Nabbout2020, Lagae2019). Sullivan2021 is a responder/NNT secondary analysis of phase 3 trial data and should be reclassified if this field is reserved for primary RCT reports. Differential effectiveness columns summarize extractable maximum effective dose/regimen values from cited RCT/outcome sources.

## HIGH fosphenytoin / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: FDA label Table 1 supports nystagmus 44%, dizziness 31%, somnolence 20%, ataxia 11%, pruritus 49%, and hypotension 8% for IV CEREBYX at maximum dose/rate; current pruritus, ataxia, and somnolence percentages do not match.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: Neurologic: nystagmus 44%, CNS: dizziness 31%, dermatologic: pruritus 27%, neurologic: ataxia 25%, CNS: somnolence 17%, cardiovascular: hypotension 8%
- Proposed: Neurologic: nystagmus 44%, CNS: dizziness 31%, dermatologic: pruritus 49%, CNS: somnolence 20%, neurologic: ataxia 11%, cardiovascular: hypotension 8%

## HIGH fosphenytoin / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: FDA and eMC sources use fosphenytoin sodium as the active/generic salt name; it should be listed as an alias of fosphenytoin, not as a separate drug row.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf; https://www.medicines.org.uk/emc/medicine/13310/SPC/pro-epanutin%20concentrate%20for%20infusion%20~%20solution%20for%20injection
- Proposed: fosphenytoin sodium

## MEDIUM fosphenytoin / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: missing_source
- Approval required: False
- Summary: FDA labeling supports that phenytoin/CEREBYX is a potent inducer of hepatic drug-metabolizing enzymes, but the row's specific CYP/UGT wording is not directly supported by the cited FDA label text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: Phenytoin prodrug; strong CYP/UGT enzyme inducer after conversion
- Proposed: Phenytoin prodrug; potent inducer of hepatic drug-metabolizing enzymes after conversion

## HIGH fosphenytoin / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Current source text uses DailyMed and omits eMC for Pro-Epanutin and trial sources for RCT-specific fields.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK547879/; https://www.ncbi.nlm.nih.gov/books/NBK548889/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf; https://www.medicines.org.uk/emc/medicine/13310/SPC/pro-epanutin%20concentrate%20for%20infusion%20~%20solution%20for%20injection; https://pubmed.ncbi.nlm.nih.gov/24135012/; https://clinicaltrials.gov/study/NCT01870024
- Current: NCBI LiverTox anticonvulsants table; FDA/DailyMed labeling
- Proposed: NCBI LiverTox fosphenytoin/phenytoin records; FDA/accessdata CEREBYX prescribing information; eMC Pro-Epanutin SmPC; PubMed and ClinicalTrials.gov records for RCT/trial fields

## HIGH fosphenytoin / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification under the audit rules; use FDA/openFDA or FDA label metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a; published=Aug 29, 2025; title=CEREBYX (FOSPHENYTOIN SODIUM) INJECTION, SOLUTION [PFIZER LABORATORIES DIV PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a; effective_time=20250828; title=CEREBYX / FOSPHENYTOIN SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5

## CRITICAL fosphenytoin / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: True
- Summary: FDA CEREBYX labeling supports fosphenytoin conversion half-life of about 15 minutes and mean total phenytoin half-life values of 12.0-28.9 hours after CEREBYX. The 7-42 hour range is a general oral phenytoin range, not concordant with the cited CEREBYX FDA label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: Conversion ~15 min; phenytoin ~7-42 h
- Proposed: Conversion ~15 min; derived phenytoin mean total half-life 12.0-28.9 h after CEREBYX at studied doses

## HIGH fosphenytoin / fact_check
- Field: major_organ_for_metabolism
- Status: incorrect
- Approval required: False
- Summary: FDA label says the conversion mechanism has not been determined but phosphatases probably play a major role, and derived phenytoin is extensively metabolized in the liver by CYP2C9/CYP2C19. The current 'plasma phosphatases' wording is too specific for the cited label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: Plasma phosphatases convert prodrug; phenytoin metabolized in liver
- Proposed: Phosphatases convert fosphenytoin to phenytoin; derived phenytoin is extensively metabolized in the liver by CYP2C9 and CYP2C19

## HIGH fosphenytoin / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not in the trusted source list provided for this audit; the same mechanism is supported by FDA/accessdata labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata CEREBYX prescribing information

## HIGH fosphenytoin / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Search aliases should include the salt name and major trade names so alias rows are not created separately.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf; https://www.medicines.org.uk/emc/medicine/13310/SPC/pro-epanutin%20concentrate%20for%20infusion%20~%20solution%20for%20injection; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2021/210864Orig1s000OtherR.pdf
- Proposed: fosphenytoin sodium; Cerebyx; Pro-Epanutin; Sesquient

## HIGH fosphenytoin / fact_check
- Field: qt_interval_effect
- Status: incorrect
- Approval required: False
- Summary: FDA labeling lists QT interval prolongation as an infrequent cardiovascular adverse event and carries a boxed warning for hypotension/cardiac arrhythmias with rapid IV infusion. The current 'No typical QT prolongation' wording is not directly supported by the cited label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: No typical QT prolongation; IV administration can cause hypotension/arrhythmias
- Proposed: QT interval prolongation has been reported infrequently; IV administration can cause hypotension and cardiac arrhythmias, especially with rapid infusion

## HIGH fosphenytoin / fact_check
- Field: trade_names
- Status: missing
- Approval required: False
- Summary: Cerebyx is FDA-labeled, Pro-Epanutin is an eMC/UK SmPC trade name, and FDA review material identifies Sesquient as a fosphenytoin sodium product; all should be aliases of fosphenytoin, not separate generic rows.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf; https://www.medicines.org.uk/emc/medicine/13310/SPC/pro-epanutin%20concentrate%20for%20infusion%20~%20solution%20for%20injection; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2021/210864Orig1s000OtherR.pdf
- Current: Cerebyx; Pro-Epanutin
- Proposed: Cerebyx; Pro-Epanutin; Sesquient

## MEDIUM fosphenytoin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: insufficient_evidence
- Approval required: True
- Summary: The cited article is for fosphenytoin, randomized, double-blind, and placebo-controlled, but phase II/III status is not explicit in the PubMed-level evidence available. It reports seizure occurrence in childhood coma prophylaxis rather than chronic epilepsy responder outcomes.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24135012/
- Current: https://pubmed.ncbi.nlm.nih.gov/24135012/
- Proposed: Retain as a placebo-controlled randomized fosphenytoin seizure-prevention trial, but update notes because PubMed does not explicitly verify phase II/III and the trial does not report standard RR50/MPC/seizure-freedom endpoints.

## HIGH fosphenytoin / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Potential missing PubMed RCT: PubMed abstract verifies randomized double-dummy/placebo-controlled fosphenytoin substitution in epilepsy/neurosurgery patients. Phase II/III status is not explicit and it is safety/tolerability/PK, not RR50/MPC/seizure-freedom efficacy, so addition requires user scope approval.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8759983/
- Proposed: Wilder1996|https://pubmed.ncbi.nlm.nih.gov/8759983/

## HIGH fosphenytoin / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: ClinicalTrials.gov verifies a completed phase 3 randomized double-blind trial with placebo infusion arms and a fosphenytoin arm. No linked PubMed publication/results were identified, so it should not be added to the PubMed PMID field without a publication.
- Sources: https://clinicaltrials.gov/study/NCT01870024
- Proposed: NCT01870024|https://clinicaltrials.gov/study/NCT01870024

## MEDIUM fosphenytoin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Boxed warning source must be FDA/openFDA/FDA label/Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a; published=Aug 29, 2025; title=CEREBYX (FOSPHENYTOIN SODIUM) INJECTION, SOLUTION [PFIZER LABORATORIES DIV PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a; effective_time=20250828; title=CEREBYX / FOSPHENYTOIN SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5

## MEDIUM fosphenytoin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Use trusted FDA label source naming.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata CEREBYX prescribing information

## MEDIUM fosphenytoin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current named sources do not support all trade-name and RCT-specific facts and include DailyMed wording.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK547879/; https://www.ncbi.nlm.nih.gov/books/NBK548889/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf; https://www.medicines.org.uk/emc/medicine/13310/SPC/pro-epanutin%20concentrate%20for%20infusion%20~%20solution%20for%20injection; https://pubmed.ncbi.nlm.nih.gov/24135012/; https://clinicaltrials.gov/study/NCT01870024
- Current: NCBI LiverTox anticonvulsants table; FDA/DailyMed labeling
- Proposed: NCBI LiverTox fosphenytoin/phenytoin records; FDA/accessdata CEREBYX prescribing information; eMC Pro-Epanutin SmPC; PubMed and ClinicalTrials.gov records for RCT/trial fields

## MEDIUM fosphenytoin / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Correct percentages to FDA label Table 1.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: Neurologic: nystagmus 44%, CNS: dizziness 31%, dermatologic: pruritus 27%, neurologic: ataxia 25%, CNS: somnolence 17%, cardiovascular: hypotension 8%
- Proposed: Neurologic: nystagmus 44%, CNS: dizziness 31%, dermatologic: pruritus 49%, CNS: somnolence 20%, neurologic: ataxia 11%, cardiovascular: hypotension 8%

## MEDIUM fosphenytoin / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Add salt-name alias.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Proposed: fosphenytoin sodium

## MEDIUM fosphenytoin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use trusted named sources and add sources for trade names/RCT facts.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK547879/; https://www.ncbi.nlm.nih.gov/books/NBK548889/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf; https://www.medicines.org.uk/emc/medicine/13310/SPC/pro-epanutin%20concentrate%20for%20infusion%20~%20solution%20for%20injection; https://pubmed.ncbi.nlm.nih.gov/24135012/; https://clinicaltrials.gov/study/NCT01870024
- Current: NCBI LiverTox anticonvulsants table; FDA/DailyMed labeling
- Proposed: NCBI LiverTox fosphenytoin/phenytoin records; FDA/accessdata CEREBYX prescribing information; eMC Pro-Epanutin SmPC; PubMed and ClinicalTrials.gov records for RCT/trial fields

## MEDIUM fosphenytoin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not allowed for boxed-warning verification.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a; published=Aug 29, 2025; title=CEREBYX (FOSPHENYTOIN SODIUM) INJECTION, SOLUTION [PFIZER LABORATORIES DIV PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a; effective_time=20250828; title=CEREBYX / FOSPHENYTOIN SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d4c36fad-0ba2-4cd4-9c5e-dcf843f38a5a%22&limit=5

## CRITICAL fosphenytoin / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: Align PK range with FDA CEREBYX label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: Conversion ~15 min; phenytoin ~7-42 h
- Proposed: Conversion ~15 min; derived phenytoin mean total half-life 12.0-28.9 h after CEREBYX at studied doses

## MEDIUM fosphenytoin / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: False
- Summary: FDA label supports phosphatases generally and hepatic CYP2C9/CYP2C19 metabolism of derived phenytoin.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: Plasma phosphatases convert prodrug; phenytoin metabolized in liver
- Proposed: Phosphatases convert fosphenytoin to phenytoin; derived phenytoin is extensively metabolized in the liver by CYP2C9 and CYP2C19

## MEDIUM fosphenytoin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed with FDA/accessdata source wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata CEREBYX prescribing information

## MEDIUM fosphenytoin / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add search aliases/trade names to prevent duplicate alias rows.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf; https://www.medicines.org.uk/emc/medicine/13310/SPC/pro-epanutin%20concentrate%20for%20infusion%20~%20solution%20for%20injection; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2021/210864Orig1s000OtherR.pdf
- Proposed: fosphenytoin sodium; Cerebyx; Pro-Epanutin; Sesquient

## MEDIUM fosphenytoin / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: False
- Summary: FDA label reports QT interval prolongation as infrequent and includes cardiovascular boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf
- Current: No typical QT prolongation; IV administration can cause hypotension/arrhythmias
- Proposed: QT interval prolongation has been reported infrequently; IV administration can cause hypotension and cardiac arrhythmias, especially with rapid infusion

## MEDIUM fosphenytoin / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Add FDA-identified Sesquient trade alias while retaining Cerebyx and Pro-Epanutin.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2019/020450s039lbl.pdf; https://www.medicines.org.uk/emc/medicine/13310/SPC/pro-epanutin%20concentrate%20for%20infusion%20~%20solution%20for%20injection; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2021/210864Orig1s000OtherR.pdf
- Current: Cerebyx; Pro-Epanutin
- Proposed: Cerebyx; Pro-Epanutin; Sesquient

## CRITICAL fosphenytoin / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: Wilder1996 was not merely a title-only drug hit; PubMed abstract describes randomized double-dummy/placebo-controlled IM fosphenytoin substitution. Add only if non-efficacy safety/substitution placebo RCTs are in this field's scope because phase is not explicit.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8759983/
- Current: Gwer2013|https://pubmed.ncbi.nlm.nih.gov/24135012/
- Proposed: Gwer2013|https://pubmed.ncbi.nlm.nih.gov/24135012/; Wilder1996|https://pubmed.ncbi.nlm.nih.gov/8759983/

## MEDIUM fosphenytoin / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Clarify RCT scope, phase uncertainty, non-extractable outcomes, and trial registry finding.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24135012/; https://pubmed.ncbi.nlm.nih.gov/8759983/; https://clinicaltrials.gov/study/NCT01870024
- Current: PubMed loop 23/65 on 2026-05-15: 1 qualifying placebo-controlled randomized clinical trial report(s) retained from 3 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit 2026-05-20: Gwer2013 (PMID 24135012) is a randomized double-blind placebo-controlled fosphenytoin 20 mg PE/kg IM seizure-prevention trial in childhood acute coma; PubMed phase is not explicit and it does not report RR50/MPC/seizure-freedom efficacy endpoints. Wilder1996 (PMID 8759983) is a randomized double-dummy placebo-controlled safety/tolerability/PK substitution trial of IM fosphenytoin in epilepsy/neurosurgery; include only if non-efficacy safety/substitution RCTs are in scope. ClinicalTrials.gov NCT01870024 is a completed phase 3 randomized double-blind status-epilepticus trial with placebo infusion arms and a fosphenytoin arm but no linked PubMed results identified.

## HIGH gabapentin / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Several PubMed abstracts use GBP as an abbreviation for gabapentin; this is useful as a search alias rather than an alternate generic name.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10448830/; https://pubmed.ncbi.nlm.nih.gov/1907907/
- Proposed: GBP

## CRITICAL gabapentin / fact_check
- Field: trade_names
- Status: incorrect
- Approval required: True
- Summary: Neurontin and Gralise are gabapentin products. Horizant is gabapentin enacarbil, a prodrug, and the FDA label states it is not the same medicine as gabapentin products such as Neurontin or Gralise and should not be used in their place.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/022544s029lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/022399s010lbl.pdf
- Current: Gralise; Horizant; Neurontin
- Proposed: Gralise; Neurontin

## CRITICAL gabapentin / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: The 'Inducer' value contradicts the row's own enzyme statement and FDA/NCBI sources. Gabapentin is not a hepatic enzyme inducer.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/7693432/
- Current: Inducer; No major enzyme effect
- Proposed: No major enzyme effect

## HIGH gabapentin / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism statement is supported by FDA labeling; DailyMed should not be named as the source under the trusted-domain policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA-approved Neurontin prescribing information (accessdata.fda.gov)

## MEDIUM gabapentin / fact_check
- Field: qt_interval_effect
- Status: missing_source
- Approval required: False
- Summary: The current wording is plausible, but no direct QT-specific trusted source was identified in the cited row sources. FDA gabapentin labeling does not provide a direct QT claim.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: No QT warning or clinically meaningful QT effect described in FDA gabapentin labeling

## MEDIUM gabapentin / fact_check
- Field: filter_qt_effect
- Status: missing_source
- Approval required: False
- Summary: No direct QT-specific source was cited; this should be worded as a label-based absence of warning unless a direct QT study/source is added.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: No known meaningful QT effect
- Proposed: No QT warning identified in FDA labeling

## HIGH gabapentin / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Current evidence_sources includes DailyMed and non-whitelisted organizations. The proposed source list uses trusted domains and better maps to the row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/022544s029lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/022399s010lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548252/; https://www.ncbi.nlm.nih.gov/books/NBK493228/; https://www.fda.gov/safety/medical-product-safety-information/neurontin-gralise-horizant-gabapentin-and-lyrica-lyrica-cr-pregabalin-drug-safety-communication
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA-approved Neurontin labeling (accessdata.fda.gov); FDA Gralise and Horizant labels for trade-name disambiguation; NCBI Bookshelf LiverTox/StatPearls; PubMed placebo-controlled gabapentin RCT records; FDA drug safety communication

## HIGH gabapentin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: The abstract describes a review/secondary analysis of global improvement data from five double-blind clinical trials, not an independent primary phase II/III seizure-efficacy RCT report. It should not be used for RR50/MPC/SF outcomes.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8771597/
- Current: https://pubmed.ncbi.nlm.nih.gov/8771597/
- Proposed: flag for user review before retaining as a phase II/III RCT link

## CRITICAL gabapentin / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: Appleton1999 reports three gabapentin patients and one placebo patient were seizure-free during double-blind treatment. FDA Neurontin pediatric trial tables provide the gabapentin/placebo denominators of 119 and 128, allowing an approximate patient-rate differential of 1.7 percentage points.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10448830/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records
- Proposed: 1.7 % (drug minus placebo seizure-freedom patient-rate differential: Appleton1999 gabapentin 23-35 mg/kg/day, 3/119 [2.5%] vs placebo 1/128 [0.8%])

## CRITICAL gabapentin / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: This plot entry follows from the Appleton1999 seizure-free counts and FDA label denominators. User approval is appropriate because it changes an NR field to an extracted value.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10448830/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Proposed: Appleton1999|1.7|https://pubmed.ncbi.nlm.nih.gov/10448830/|247

## HIGH gabapentin / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supported by the FDA-approved Neurontin label, but the current row uses DailyMed and a Horizant (gabapentin enacarbil) label. DailyMed is not permissible for this field, and Horizant is not the same product as gabapentin.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in current FDA-approved Neurontin (gabapentin) prescribing information.

## MEDIUM gabapentin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: FDA-only boxed warning policy and correct gabapentin product source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd; published=May 07, 2025; title=HORIZANT (GABAPENTIN ENACARBIL) TABLET, EXTENDED RELEASE [AZURITY PHARMACEUTICALS, INC. (FORMERLY ARBOR PHARMACEUTICALS)]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd
- Proposed: FDA-approved Neurontin prescribing information; status=no_boxed_warning_identified_in_fda_label; revised=07/2024; title=NEURONTIN (gabapentin) capsules/tablets/oral solution; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf

## MEDIUM gabapentin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism text is supported by FDA label; DailyMed is not a trusted-domain citation in this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA-approved Neurontin prescribing information (accessdata.fda.gov)

## MEDIUM gabapentin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces non-trusted or nonspecific source names with sources that support the populated cells.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/022544s029lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/022399s010lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548252/; https://www.ncbi.nlm.nih.gov/books/NBK493228/; https://www.fda.gov/safety/medical-product-safety-information/neurontin-gralise-horizant-gabapentin-and-lyrica-lyrica-cr-pregabalin-drug-safety-communication
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA-approved Neurontin labeling (accessdata.fda.gov); FDA Gralise and Horizant labels for trade-name disambiguation; NCBI Bookshelf LiverTox/StatPearls; PubMed placebo-controlled gabapentin RCT records; FDA drug safety communication

## CRITICAL gabapentin / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: True
- Summary: Horizant is gabapentin enacarbil, not gabapentin, and FDA labeling states it is not the same medicine as Neurontin/Gralise and should not be used in their place.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/022399s010lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/022544s029lbl.pdf
- Current: Gralise; Horizant; Neurontin
- Proposed: Gralise; Neurontin

## MEDIUM gabapentin / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: GBP is used as an abbreviation for gabapentin in PubMed RCT abstracts and should be captured as a search alias.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10448830/; https://pubmed.ncbi.nlm.nih.gov/1907907/
- Proposed: GBP

## MEDIUM gabapentin / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: FDA-source-only policy for boxed warnings; current text cites DailyMed and a Horizant label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in current FDA-approved Neurontin (gabapentin) prescribing information.

## MEDIUM gabapentin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replaces nonpermissible DailyMed/Horizant source with FDA accessdata gabapentin labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd; published=May 07, 2025; title=HORIZANT (GABAPENTIN ENACARBIL) TABLET, EXTENDED RELEASE [AZURITY PHARMACEUTICALS, INC. (FORMERLY ARBOR PHARMACEUTICALS)]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=4c486fc7-c8c4-4c6c-b30c-366dabaeaadd
- Proposed: FDA-approved Neurontin prescribing information; status=no_boxed_warning_identified_in_fda_label; revised=07/2024; title=NEURONTIN (gabapentin) capsules/tablets/oral solution; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf

## MEDIUM gabapentin / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Audit verification was performed against FDA labeling on the current audit date.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## CRITICAL gabapentin / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: Gabapentin is not a hepatic enzyme inducer; current filter contains a direct contradiction.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/7693432/
- Current: Inducer; No major enzyme effect
- Proposed: No major enzyme effect

## CRITICAL gabapentin / proposed_row_update
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Appleton1999 reports seizure-free counts, and FDA label denominators allow rate calculation.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10448830/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records
- Proposed: 1.7 % (drug minus placebo seizure-freedom patient-rate differential: Appleton1999 gabapentin 23-35 mg/kg/day, 3/119 [2.5%] vs placebo 1/128 [0.8%])

## CRITICAL gabapentin / proposed_row_update
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Adds the extractable Appleton1999 seizure-freedom differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10448830/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Proposed: Appleton1999|1.7|https://pubmed.ncbi.nlm.nih.gov/10448830/|247

## MEDIUM gabapentin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; the row should cite the FDA label rather than DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA-approved Neurontin prescribing information (accessdata.fda.gov)

## MEDIUM gabapentin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Uses trusted-domain sources that actually support the populated cells and removes DailyMed/non-whitelisted source names.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/022544s029lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/022399s010lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548252/; https://www.ncbi.nlm.nih.gov/books/NBK493228/; https://www.fda.gov/safety/medical-product-safety-information/neurontin-gralise-horizant-gabapentin-and-lyrica-lyrica-cr-pregabalin-drug-safety-communication
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA-approved Neurontin labeling (accessdata.fda.gov); FDA Gralise and Horizant labels for trade-name disambiguation; NCBI Bookshelf LiverTox/StatPearls; PubMed placebo-controlled gabapentin RCT records; FDA drug safety communication

## CRITICAL gabapentin / proposed_row_update
- Field: status_or_notes
- Status: proposed
- Approval required: True
- Summary: Clarifies the Horizant/gabapentin-enacarbil distinction while preserving the clinically relevant notes.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021129s056%2C020882s057%2C020235s076lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/022399s010lbl.pdf
- Current: Current ASM for focal/partial seizures; also used for postherpetic neuralgia, neuropathic pain, restless legs syndrome, and other off-label uses.
- Proposed: Current ASM for adjunctive treatment of focal/partial-onset seizures; also indicated for postherpetic neuralgia. Gabapentin enacarbil (Horizant) is a distinct prodrug indicated for RLS/PHN and should not be treated as an interchangeable gabapentin trade name.

## HIGH ganaxolone / fact_check
- Field: pubmed_search_aliases
- Status: incorrect
- Approval required: False
- Summary: CCD 1042 is verified in PubMed; FDA pharmacology review/search metadata also uses GNX. Current value is not wrong, but it is missing common spacing/hyphenation and GNX aliases useful for PubMed searches.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9067315/; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2022/215904Orig1s000PharmR.pdf
- Current: CCD1042
- Proposed: CCD 1042; CCD-1042; CCD1042; GNX

## MEDIUM ganaxolone / fact_check
- Field: mechanism_source
- Status: missing_source
- Approval required: False
- Summary: The mechanism is supported by FDA labeling, but the named source should not include DailyMed under the trusted-source policy for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA prescribing information (Drugs@FDA/accessdata)

## HIGH ganaxolone / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not in the requested trusted-source list, and the outcome/RCT fields are supported by PubMed and ClinicalTrials.gov rather than FDA label alone.
- Sources: https://www.fda.gov/drugs/drug-trials-snapshots/drug-trials-snapshots-ztalmy; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/35429480/; https://pubmed.ncbi.nlm.nih.gov/36870093/; https://pubmed.ncbi.nlm.nih.gov/28230252/; https://clinicaltrials.gov/study/NCT03572933
- Current: FDA Ztalmy approval/snapshot pages; FDA/DailyMed labeling
- Proposed: FDA Ztalmy approval/snapshot pages; FDA prescribing information (Drugs@FDA/accessdata); PubMed RCT abstracts/metadata; ClinicalTrials.gov records for trial design where needed

## CRITICAL ganaxolone / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: Sullivan and Knight support median/Hodges-Lehmann values. Sperling supports a 19.6 percentage-point difference, but it is a mean percent change, not a median percent change.
- Sources: https://pubmed.ncbi.nlm.nih.gov/36870093/; https://pubmed.ncbi.nlm.nih.gov/35429480/; https://pubmed.ncbi.nlm.nih.gov/28230252/
- Current: 19.6-37.5 % (drug minus placebo MPC differential at maximum effective dose/regimen: Sullivan2023 ganaxolone up to 63 mg/kg/day or 1800 mg/day 37.5%; Knight2022 ganaxolone up to 63 mg/kg/day or 1800 mg/day 27.1%; Sperling2017 ganaxolone 1500 mg/day 19.6%)
- Proposed: 19.6-37.5 % (drug-minus-placebo seizure-frequency percent-change differential at maximum effective dose/regimen: Sullivan2023 ganaxolone up to 63 mg/kg/day or 1800 mg/day median reduction 61.5% vs 24.0%, differential 37.5%; Knight2022 ganaxolone up to 63 mg/kg/day or 1800 mg/day Hodges-Lehmann median difference 27.1%; Sperling2017 ganaxolone 1500 mg/day reported mean percent change, not median: -17.6% vs 2.0%, differential 19.6%)

## CRITICAL ganaxolone / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: The plotted median-percent-change field should not include Sperling2017 unless the plot can explicitly label that value as mean percent change rather than median. Removing or relocating that value changes existing CSV data, so approval is required.
- Sources: https://pubmed.ncbi.nlm.nih.gov/36870093/; https://pubmed.ncbi.nlm.nih.gov/35429480/; https://pubmed.ncbi.nlm.nih.gov/28230252/
- Current: Sullivan2023|37.5|https://pubmed.ncbi.nlm.nih.gov/36870093/|21; Knight2022|27.1|https://pubmed.ncbi.nlm.nih.gov/35429480/|100; Sperling2017|19.6|https://pubmed.ncbi.nlm.nih.gov/28230252/|147
- Proposed: Sullivan2023|37.5|https://pubmed.ncbi.nlm.nih.gov/36870093/|21; Knight2022|27.1|https://pubmed.ncbi.nlm.nih.gov/35429480/|100

## INFO ganaxolone / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: No plot value is expected because seizure-freedom differential is not extractable from the cited RCT records.
- Sources: https://pubmed.ncbi.nlm.nih.gov/36870093/; https://pubmed.ncbi.nlm.nih.gov/35429480/; https://pubmed.ncbi.nlm.nih.gov/28230252/; https://pubmed.ncbi.nlm.nih.gov/38959712/

## HIGH ganaxolone / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The current FDA label has warnings/precautions but no boxed-warning section. The row's conclusion is supported, but DailyMed is not permissible for this field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in current FDA prescribing information.

## MEDIUM ganaxolone / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed with FDA label source and name PubMed/ClinicalTrials.gov support for RCT and outcome fields.
- Sources: https://www.fda.gov/drugs/drug-trials-snapshots/drug-trials-snapshots-ztalmy; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/35429480/; https://pubmed.ncbi.nlm.nih.gov/36870093/; https://pubmed.ncbi.nlm.nih.gov/28230252/; https://clinicaltrials.gov/study/NCT03572933
- Current: FDA Ztalmy approval/snapshot pages; FDA/DailyMed labeling
- Proposed: FDA Ztalmy approval/snapshot pages; FDA prescribing information (Drugs@FDA/accessdata); PubMed RCT abstracts/metadata; ClinicalTrials.gov records for trial design where needed

## MEDIUM ganaxolone / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism wording is supported by FDA label; DailyMed is not needed and is outside the requested trusted-source list.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA prescribing information (Drugs@FDA/accessdata)

## MEDIUM ganaxolone / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box warning verification must use FDA/openFDA/FDA label/Drugs@FDA sources, not DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=d91612c4-b03a-4be4-a1ee-6a13e3b83d4e; published=Dec 01, 2025; title=ZTALMY (GANAXOLONE) SUSPENSION [IMMEDICA PHARMA US INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d91612c4-b03a-4be4-a1ee-6a13e3b83d4e
- Proposed: FDA prescribing information (Drugs@FDA/accessdata); status=no_boxed_warning_identified_in_current_fda_label; NDA=215904; revised=10/2025; title=ZTALMY (ganaxolone) oral suspension; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf

## MEDIUM ganaxolone / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for black-box verification; the FDA accessdata label supports no boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in current FDA prescribing information.

## MEDIUM ganaxolone / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Adds verified development-code and abbreviation variants useful for PubMed searching.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9067315/; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2022/215904Orig1s000PharmR.pdf
- Current: CCD1042
- Proposed: CCD 1042; CCD-1042; CCD1042; GNX

## CRITICAL ganaxolone / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Sperling2017 reports mean percent change, not median percent change; annotate before relying on it in a median field.
- Sources: https://pubmed.ncbi.nlm.nih.gov/36870093/; https://pubmed.ncbi.nlm.nih.gov/35429480/; https://pubmed.ncbi.nlm.nih.gov/28230252/
- Current: 19.6-37.5 % (drug minus placebo MPC differential at maximum effective dose/regimen: Sullivan2023 ganaxolone up to 63 mg/kg/day or 1800 mg/day 37.5%; Knight2022 ganaxolone up to 63 mg/kg/day or 1800 mg/day 27.1%; Sperling2017 ganaxolone 1500 mg/day 19.6%)
- Proposed: 19.6-37.5 % (drug-minus-placebo seizure-frequency percent-change differential at maximum effective dose/regimen: Sullivan2023 ganaxolone up to 63 mg/kg/day or 1800 mg/day median reduction 61.5% vs 24.0%, differential 37.5%; Knight2022 ganaxolone up to 63 mg/kg/day or 1800 mg/day Hodges-Lehmann median difference 27.1%; Sperling2017 ganaxolone 1500 mg/day reported mean percent change, not median: -17.6% vs 2.0%, differential 19.6%)

## CRITICAL ganaxolone / proposed_row_update
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Sperling2017 value is mean percent change and should not be plotted as median percent change unless the plot parser supports an explicit mean label.
- Sources: https://pubmed.ncbi.nlm.nih.gov/36870093/; https://pubmed.ncbi.nlm.nih.gov/35429480/; https://pubmed.ncbi.nlm.nih.gov/28230252/
- Current: Sullivan2023|37.5|https://pubmed.ncbi.nlm.nih.gov/36870093/|21; Knight2022|27.1|https://pubmed.ncbi.nlm.nih.gov/35429480/|100; Sperling2017|19.6|https://pubmed.ncbi.nlm.nih.gov/28230252/|147
- Proposed: Sullivan2023|37.5|https://pubmed.ncbi.nlm.nih.gov/36870093/|21; Knight2022|27.1|https://pubmed.ncbi.nlm.nih.gov/35429480/|100

## MEDIUM ganaxolone / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: Current FDA label contains UGT interaction and broader metabolism language not captured in the row.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/215904s011s013lbl.pdf
- Current: CYP3A4 substrate; not a major inducer/inhibitor
- Proposed: Metabolized by CYP3A4/5 and other CYP/UGT enzymes; UGT inhibitors may increase exposure and strong/moderate CYP3A4 inducers decrease exposure; not a clinically relevant CYP inhibitor or inducer

## HIGH lacosamide / fact_check
- Field: names_and_aliases
- Status: missing
- Approval required: False
- Summary: Lacosamide and the US trade names Vimpat and Motpoly XR are verified. LACOSAMIDE should not be added as a trade name because it is the generic name. PubMed/NCBI literature identifies SPM 927, harkoseride, and ADD 234037 as prior/development aliases; SPM 927 is present but harkoseride and ADD 234037 are missing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/?term=17461888
- Current: generic_name=lacosamide; trade_names=Motpoly XR; Vimpat; alternate_generic_names=; pubmed_search_aliases=SPM 927
- Proposed: generic_name=lacosamide; trade_names=Motpoly XR; Vimpat; alternate_generic_names=; pubmed_search_aliases=SPM 927; harkoseride; ADD 234037

## CRITICAL lacosamide / fact_check
- Field: formulations_available/filter_formulation
- Status: incorrect
- Approval required: True
- Summary: FDA labeling supports tablets, oral solution, IV injection, and extended-release capsules. The detailed formulation is IV only; IM injection is not supported by the FDA label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22VIMPAT%22&limit=10
- Current: formulations_available=Tablet; oral solution; IV injection; extended-release capsule; filter_formulation=Capsule; IV/IM injection; Liquid; Long acting; Tablet
- Proposed: formulations_available=Tablet; oral solution; IV injection; extended-release capsule; filter_formulation=Capsule; IV injection; Liquid; Long acting; Tablet

## HIGH lacosamide / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: The CNS/GI/ophthalmologic percentages are supported across FDA-labeled adult partial-onset and PGTC trial data. The cardiac percentage is specifically asymptomatic first-degree AV block 0.4%; PR interval prolongation is a pharmacodynamic effect, not an adverse-event percentage of <1%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf
- Current: adverse_symptoms_percentages=CNS: dizziness 23-25%, CNS: somnolence 17%, CNS: headache 14%, GI: nausea 10%, ophthalmologic: diplopia 10%, cardiac: PR prolongation <1%
- Proposed: CNS: dizziness 23-25%, CNS: somnolence 17%, CNS: headache 14%, GI: nausea 10%, ophthalmologic: diplopia 10%, cardiac: first-degree AV block 0.4%; dose-dependent PR interval prolongation

## CRITICAL lacosamide / fact_check
- Field: qt_interval_effect/filter_qt_effect
- Status: incorrect
- Approval required: True
- Summary: FDA labeling states lacosamide did not prolong QTc and produced a small dose-related PR interval increase. The filter value QT prolongation directly contradicts the label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf
- Current: qt_interval_effect=No QT prolongation; can prolong PR interval; filter_qt_effect=PR interval effect; QT prolongation
- Proposed: qt_interval_effect=No QT prolongation; can prolong PR interval; filter_qt_effect=PR interval effect

## CRITICAL lacosamide / fact_check
- Field: enzyme_inducing_or_inhibiting/filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: FDA labeling and NCBI sources support no clinically meaningful induction/inhibition. The filter value Inducer; Inhibitor directly contradicts the row fact and source evidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK547940/; https://www.ncbi.nlm.nih.gov/books/NBK493589/
- Current: enzyme_inducing_or_inhibiting=Not a clinically meaningful enzyme inducer/inhibitor; filter_enzyme_effect=Inducer; Inhibitor
- Proposed: enzyme_inducing_or_inhibiting=Not a clinically meaningful enzyme inducer/inhibitor; filter_enzyme_effect=None

## CRITICAL lacosamide / fact_check
- Field: metabolism_half_life
- Status: incorrect
- Approval required: True
- Summary: FDA labeling verifies renal excretion plus biotransformation, CYP3A4/CYP2C9/CYP2C19 involvement, and half-life about 13 hours. The phrase Renal/no major metabolism is misleading because lacosamide undergoes hepatic biotransformation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK547940/
- Current: major_organ_for_metabolism=Liver and renal excretion; half_life_range=13 h; filter_metabolism=Liver/hepatic; Renal/no major metabolism
- Proposed: major_organ_for_metabolism=Liver metabolism and renal excretion; half_life_range=13 h; filter_metabolism=Liver/hepatic; Renal excretion

## HIGH lacosamide / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The current evidence_sources field names DailyMed and non-trusted epilepsy-list sources. Retained facts can be supported by FDA/openFDA/accessdata, NCBI, PubMed, and ClinicalTrials.gov sources instead.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22LACOSAMIDE%22&limit=10; https://www.ncbi.nlm.nih.gov/books/NBK547940/; https://www.ncbi.nlm.nih.gov/books/NBK493589/
- Current: evidence_sources=NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata FDA labeling; FDA/openFDA drug label API; NCBI LiverTox; NCBI Medical Genetics Summaries; PubMed RCT abstracts; ClinicalTrials.gov trial records

## HIGH lacosamide / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: PubMed identifies this as Clinical Trial, Phase IV. The endpoint was daytime sleepiness/noninferiority, not a phase II/III placebo-controlled seizure-efficacy RCT.
- Sources: https://pubmed.ncbi.nlm.nih.gov/28866338/
- Current: https://pubmed.ncbi.nlm.nih.gov/28866338/
- Proposed: Remove from pubmed_phase_ii_iii_rct_links with user approval; optionally retain only as a sleep/cognition tolerability reference elsewhere.

## HIGH lacosamide / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: This is a pooled cardiac safety analysis of clinical-trial data, not a primary phase II/III placebo-controlled seizure-efficacy RCT report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/25933358/
- Current: https://pubmed.ncbi.nlm.nih.gov/25933358/
- Proposed: Remove from pubmed_phase_ii_iii_rct_links with user approval; retain as cardiac-safety support if a separate safety-source field exists.

## CRITICAL lacosamide / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose / plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: Farkas, Chung, Halasz, and Ben-Menachem values are true active-minus-placebo median percent-change differentials. Makedonska2024 reports a placebo-adjusted percentage reduction in electrographic focal-seizure ADF, not an arm-specific median percent-change value, so it should not be in a median-percent-change field.
- Sources: https://pubmed.ncbi.nlm.nih.gov/38375995/; https://pubmed.ncbi.nlm.nih.gov/31462582/; https://pubmed.ncbi.nlm.nih.gov/20132285/; https://pubmed.ncbi.nlm.nih.gov/19183227/; https://pubmed.ncbi.nlm.nih.gov/17635557/
- Current: 3.2-30 % (Makedonska2024 3.2%; Farkas2019 30%; Chung2010 16.5%; Halasz2009 15.9%; BenMenachem2007 29%)
- Proposed: 15.9-30 % (drug minus placebo median percent-change differential at maximum effective dose/regimen: Farkas2019 lacosamide target weight-based pediatric regimen 30%; Chung2010 lacosamide 400 mg/day 16.5%; Halasz2009 lacosamide 400 mg/day 15.9%; BenMenachem2007 lacosamide 400 mg/day 29%)

## HIGH lacosamide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is plausible, but the current row relies on DailyMed, which is not permissible for this field. FDA/openFDA or Drugs@FDA/FDA label sources should be used instead.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22VIMPAT%22&limit=10; https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22MOTPOLY%20XR%22&limit=10; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA labels for lacosamide (Vimpat/Motpoly XR).

## MEDIUM lacosamide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supported by FDA labeling; DailyMed wording should be avoided in source fields when trusted FDA/accessdata/openFDA sources are available.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA labeling

## MEDIUM lacosamide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box warning verification must use FDA/openFDA/Drugs@FDA/accessdata, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22VIMPAT%22&limit=10; https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22MOTPOLY%20XR%22&limit=10
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label...
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_identified_in_selected_current_fda_labeling; api_urls=https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22VIMPAT%22&limit=10 and https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22MOTPOLY%20XR%22&limit=10

## CRITICAL lacosamide / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: True
- Summary: Updates automated notes after manual concordance review.
- Sources: https://pubmed.ncbi.nlm.nih.gov/28866338/; https://pubmed.ncbi.nlm.nih.gov/25933358/; https://pubmed.ncbi.nlm.nih.gov/26414341/
- Current: PubMed loop 26/65 on 2026-05-15: 9 qualifying placebo-controlled randomized clinical trial report(s) retained from 26 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Manual audit on 2026-05-20: retained Makedonska2024, Vossler2020, Farkas2019, Hong2016, Chung2010, Halasz2009, and BenMenachem2007 as qualifying lacosamide placebo-controlled phase II/III seizure-efficacy RCT reports. FoldvarySchaefer2017 is Phase IV sleepiness/cognition and Rudd2015 is pooled cardiac safety, so both require user approval before removal from the phase II/III RCT link field. Do not add Biton2015 as a missing RCT because it is a pooled safety/tolerability analysis of already represented trials, not an independent primary efficacy RCT.

## MEDIUM lacosamide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22VIMPAT%22&limit=10; https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22MOTPOLY%20XR%22&limit=10; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2; published=May 13, 2026; title=VIMPAT (LACOSAMIDE) TABLET, FILM COATED VIMPAT (LACOSAMIDE) INJECTION VIMPAT (LACOSAMIDE) SOLUTION [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=9e79b42c-38a3-4b2c-a196-a5a1948250e2
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_identified_in_selected_current_fda_labeling; api_urls=https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22VIMPAT%22&limit=10 and https://api.fda.gov/drug/label.json?search=openfda.brand_name%3A%22MOTPOLY%20XR%22&limit=10; FDA label reference=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf

## MEDIUM lacosamide / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: NCBI/PubMed review identifies harkoseride and ADD 234037 as prior names/aliases for lacosamide; aliases should not become separate drug rows.
- Sources: https://pubmed.ncbi.nlm.nih.gov/?term=17461888
- Current: SPM 927
- Proposed: SPM 927; harkoseride; ADD 234037

## CRITICAL lacosamide / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: FoldvarySchaefer2017 is Phase IV sleepiness/cognition, not phase II/III seizure-efficacy RCT. Rudd2015 is a pooled cardiac safety analysis, not a primary phase II/III placebo-controlled seizure-efficacy RCT report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/28866338/; https://pubmed.ncbi.nlm.nih.gov/25933358/
- Current: FoldvarySchaefer2017 and Rudd2015 included in pubmed_phase_ii_iii_rct_links
- Proposed: Makedonska2024|https://pubmed.ncbi.nlm.nih.gov/38375995/; Vossler2020|https://pubmed.ncbi.nlm.nih.gov/32817358/; Farkas2019|https://pubmed.ncbi.nlm.nih.gov/31462582/; Hong2016|https://pubmed.ncbi.nlm.nih.gov/27669155/; Chung2010|https://pubmed.ncbi.nlm.nih.gov/20132285/; Halasz2009|https://pubmed.ncbi.nlm.nih.gov/19183227/; BenMenachem2007|https://pubmed.ncbi.nlm.nih.gov/17635557/

## CRITICAL lacosamide / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Makedonska2024 3.2% is placebo-adjusted electrographic ADF percent reduction, not a median percent-change differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/38375995/; https://pubmed.ncbi.nlm.nih.gov/31462582/; https://pubmed.ncbi.nlm.nih.gov/20132285/; https://pubmed.ncbi.nlm.nih.gov/19183227/; https://pubmed.ncbi.nlm.nih.gov/17635557/
- Current: 3.2-30 % (includes Makedonska2024 3.2%)
- Proposed: 15.9-30 % (drug minus placebo median percent-change differential at maximum effective dose/regimen: Farkas2019 lacosamide target weight-based pediatric regimen 30%; Chung2010 lacosamide 400 mg/day 16.5%; Halasz2009 lacosamide 400 mg/day 15.9%; BenMenachem2007 lacosamide 400 mg/day 29%)

## CRITICAL lacosamide / proposed_row_update
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Remove Makedonska2024 from the median-percent-change plot for the same reason as above.
- Sources: https://pubmed.ncbi.nlm.nih.gov/38375995/
- Current: Makedonska2024|3.2|https://pubmed.ncbi.nlm.nih.gov/38375995/|255; Farkas2019|30|https://pubmed.ncbi.nlm.nih.gov/31462582/|338; Chung2010|16.5|https://pubmed.ncbi.nlm.nih.gov/20132285/|405; Halasz2009|15.9|https://pubmed.ncbi.nlm.nih.gov/19183227/|485; BenMenachem2007|29|https://pubmed.ncbi.nlm.nih.gov/17635557/|418
- Proposed: Farkas2019|30|https://pubmed.ncbi.nlm.nih.gov/31462582/|338; Chung2010|16.5|https://pubmed.ncbi.nlm.nih.gov/20132285/|405; Halasz2009|15.9|https://pubmed.ncbi.nlm.nih.gov/19183227/|485; BenMenachem2007|29|https://pubmed.ncbi.nlm.nih.gov/17635557/|418

## CRITICAL lacosamide / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: FDA labeling supports no clinically meaningful enzyme induction/inhibition; current filter contradicts the fact field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf
- Current: Inducer; Inhibitor
- Proposed: None

## CRITICAL lacosamide / proposed_row_update
- Field: filter_qt_effect
- Status: proposed
- Approval required: True
- Summary: FDA labeling states lacosamide did not prolong QTc and can increase PR interval.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf
- Current: PR interval effect; QT prolongation
- Proposed: PR interval effect

## CRITICAL lacosamide / proposed_row_update
- Field: filter_formulation
- Status: proposed
- Approval required: True
- Summary: FDA labeling supports IV injection only, not IM injection.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf
- Current: Capsule; IV/IM injection; Liquid; Long acting; Tablet
- Proposed: Capsule; IV injection; Liquid; Long acting; Tablet

## MEDIUM lacosamide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces DailyMed/non-trusted list sources with trusted domains that support the retained facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/216185s001lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK547940/; https://www.ncbi.nlm.nih.gov/books/NBK493589/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata FDA labeling; FDA/openFDA drug label API; NCBI LiverTox; NCBI Medical Genetics Summaries; PubMed RCT abstracts; ClinicalTrials.gov trial records

## MEDIUM lamotrigine / fact_check
- Field: trade_names
- Status: insufficient_evidence
- Approval required: True
- Summary: Lamictal/ODT/XR are supported by FDA labeling. I could not verify Lamictal CD and Logem from the trusted domains available in this audit; Lamotrigine should not be added as a trade name because it is the generic name.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/022115s031s032lbl.pdf; https://www.medicines.org.uk/emc/product/8052/smpc
- Current: Lamictal; Lamictal CD; Lamictal ODT; Lamictal XR; Logem
- Proposed: No automatic change. FDA sources verify Lamictal, Lamictal ODT, and Lamictal XR; add trusted-source support for Lamictal CD and Logem, or user-approve narrowing to: Lamictal; Lamictal ODT; Lamictal XR

## HIGH lamotrigine / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: LTG and Lamictal appear in lamotrigine trial literature and would improve alias capture without creating duplicate drug rows.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10403222/; https://pubmed.ncbi.nlm.nih.gov/2498073/
- Proposed: LTG; Lamictal

## CRITICAL lamotrigine / fact_check
- Field: maximum_approved_daily_dose
- Status: incorrect
- Approval required: True
- Summary: Immediate-release dosing supports up to 500 mg/day in some adjunctive regimens; FDA XR labeling lists an adjunctive target therapeutic range up to 600 mg/day.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/022115s031s032lbl.pdf
- Current: Up to 500 mg/day for adjunctive therapy depending on interacting ASMs
- Proposed: Up to 500 mg/day for immediate-release adjunctive epilepsy depending on interacting ASMs; up to 600 mg/day for Lamictal XR adjunctive therapy depending on concomitant AEDs

## HIGH lamotrigine / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: Use FDA/accessdata rather than DailyMed as the named FDA-label source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; Sills and Rogawski 2020 ASM mechanism review

## CRITICAL lamotrigine / fact_check
- Field: filter_mechanism
- Status: incorrect
- Approval required: True
- Summary: The label supports voltage-sensitive sodium-channel inhibition with modulation of glutamate/aspartate release, and specifically reports no NMDA receptor inhibition at tested concentrations. A glutamate receptor filter is misleading.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: Glutamate receptor
- Proposed: Sodium channel; Reduced excitatory amino acid release

## CRITICAL lamotrigine / fact_check
- Field: filter_qt_effect
- Status: incorrect
- Approval required: True
- Summary: FDA evidence supports conduction/arrhythmia caution, not QT prolongation as a clinically meaningful effect.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/studies-show-increased-risk-heart-rhythm-problems-seizure-and-mental-health-medicine-lamotrigine
- Current: Conduction/arrhythmia caution; No known meaningful QT effect; QT prolongation
- Proposed: Conduction/arrhythmia caution; No known meaningful QT effect

## MEDIUM lamotrigine / fact_check
- Field: evidence_sources
- Status: missing_source
- Approval required: False
- Summary: Current evidence_sources includes non-trusted-domain sources for this audit and cites DailyMed. FDA/accessdata, eMC, PubMed/NCBI, and ClinicalTrials.gov better match the row-source policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf; https://www.medicines.org.uk/emc/product/8052/smpc; https://pmc.ncbi.nlm.nih.gov/articles/PMC10712213/; https://clinicaltrials.gov/study/NCT00104416; https://clinicaltrials.gov/study/NCT00113165
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; eMC SmPC; NCBI/PubMed reviews; PubMed randomized placebo-controlled trial reports; ClinicalTrials.gov trial records; Sills and Rogawski 2020 ASM mechanism review

## HIGH lamotrigine / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for FDA black-box-warning verification under the audit rules; FDA/accessdata is permissible and supports the warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=d7e3572d-56fe-4727-2bb4-013ccca22678; published=Nov 17, 2025; title=LAMICTAL...; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d7e3572d-56fe-4727-2bb4-013ccca22678
- Proposed: FDA/accessdata drug label; status=boxed_warning_found; application=NDA 020241/020764/022251; revised=10/2025; reference_id=5675542; title=LAMICTAL (lamotrigine) tablets/tablets for oral suspension/LAMICTAL ODT; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf

## HIGH lamotrigine / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: Lamotrigine vs placebo randomized double-blind crossover in children with epilepsy, but primary endpoint is cognition and seizure frequency was similar; it does not support seizure efficacy outcomes.
- Sources: https://pubmed.ncbi.nlm.nih.gov/16717207/
- Current: https://pubmed.ncbi.nlm.nih.gov/16717207/
- Proposed: User review before retaining in phase II/III efficacy list.

## HIGH lamotrigine / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: Secondary mood-symptom analysis of a randomized placebo-controlled PGTC study; does not provide independent seizure-efficacy outcomes for this row.
- Sources: https://pubmed.ncbi.nlm.nih.gov/17071141/
- Current: https://pubmed.ncbi.nlm.nih.gov/17071141/
- Proposed: User review before retaining as a separate phase II/III efficacy RCT.

## HIGH lamotrigine / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: Lamotrigine pharmacodynamic/interictal spike-count study, not a seizure-frequency phase II/III efficacy outcome report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/3530305/
- Current: https://pubmed.ncbi.nlm.nih.gov/3530305/
- Proposed: User review before retaining in phase II/III clinical efficacy list.

## HIGH lamotrigine / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Multicenter randomized double-blind parallel-group placebo-controlled adjunctive lamotrigine trial in refractory partial seizures; FDA label describes n=216 and median seizure-frequency reductions of 8% placebo, 20% at 300 mg/day, and 36% at 500 mg/day.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8232944/
- Proposed: Matsuo1993|https://pubmed.ncbi.nlm.nih.gov/8232944/

## HIGH lamotrigine / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Randomized double-blind placebo-controlled infant partial-seizure trial; relevant as a negative/young-pediatric study if the CSV retains negative placebo-controlled lamotrigine epilepsy trials.
- Sources: https://pubmed.ncbi.nlm.nih.gov/18077797/
- Proposed: PinaGarza2007|https://pubmed.ncbi.nlm.nih.gov/18077797/

## HIGH lamotrigine / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Existing values are supported; Matsuo1993 is a missing randomized placebo-controlled partial-seizure efficacy trial with 36% median reduction at 500 mg/day vs 8% placebo, differential 28%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/20937567/; https://pubmed.ncbi.nlm.nih.gov/17938371/; https://pubmed.ncbi.nlm.nih.gov/16847080/; https://pubmed.ncbi.nlm.nih.gov/16344515/; https://pubmed.ncbi.nlm.nih.gov/9400037/; https://pubmed.ncbi.nlm.nih.gov/8937535/; https://pubmed.ncbi.nlm.nih.gov/8112232/; https://pubmed.ncbi.nlm.nih.gov/8232944/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: 22.1-44.8 % (Biton2010 43.3%; Naritoku2007 22.1%; Trevathan2006 37%; Biton2005 32.3%; Motte1997 44.8%; Boas1996 30.3%; Messenheimer1994 25%)
- Proposed: 22.1-44.8 % (drug minus placebo MPC differential at maximum effective dose/regimen: Biton2010 lamotrigine XR individualized adjunctive dose 43.3%; Naritoku2007 lamotrigine XR individualized adjunctive dose 22.1%; Trevathan2006 lamotrigine individualized adjunctive dose 37%; Biton2005 lamotrigine individualized adjunctive dose 32.3%; Motte1997 lamotrigine individualized adjunctive dose 44.8%; Boas1996 lamotrigine 75-400 mg/day 30.3%; Messenheimer1994 lamotrigine mostly 400 mg/day 25%; Matsuo1993 lamotrigine 500 mg/day 28%)

## HIGH lamotrigine / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Add missing Matsuo1993 MPC differential; existing plot entries are concordant with cited outcomes.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8232944/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: Biton2010|43.3|https://pubmed.ncbi.nlm.nih.gov/20937567/|153; Naritoku2007|22.1|https://pubmed.ncbi.nlm.nih.gov/17938371/|239; Trevathan2006|37|https://pubmed.ncbi.nlm.nih.gov/16847080/|45; Biton2005|32.3|https://pubmed.ncbi.nlm.nih.gov/16344515/|117; Motte1997|44.8|https://pubmed.ncbi.nlm.nih.gov/9400037/|169; Boas1996|30.3|https://pubmed.ncbi.nlm.nih.gov/8937535/|56; Messenheimer1994|25|https://pubmed.ncbi.nlm.nih.gov/8112232/|98
- Proposed: Biton2010|43.3|https://pubmed.ncbi.nlm.nih.gov/20937567/|153; Naritoku2007|22.1|https://pubmed.ncbi.nlm.nih.gov/17938371/|239; Trevathan2006|37|https://pubmed.ncbi.nlm.nih.gov/16847080/|45; Biton2005|32.3|https://pubmed.ncbi.nlm.nih.gov/16344515/|117; Motte1997|44.8|https://pubmed.ncbi.nlm.nih.gov/9400037/|169; Boas1996|30.3|https://pubmed.ncbi.nlm.nih.gov/8937535/|56; Messenheimer1994|25|https://pubmed.ncbi.nlm.nih.gov/8112232/|98; Matsuo1993|28|https://pubmed.ncbi.nlm.nih.gov/8232944/|216

## MEDIUM lamotrigine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box-warning verification must use FDA/openFDA/accessdata/Drugs@FDA sources, not DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=d7e3572d-56fe-4727-2bb4-013ccca22678; published=Nov 17, 2025; title=LAMICTAL...; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d7e3572d-56fe-4727-2bb4-013ccca22678
- Proposed: FDA/accessdata drug label; status=boxed_warning_found; application=NDA 020241/020764/022251; revised=10/2025; reference_id=5675542; title=LAMICTAL (lamotrigine) tablets/tablets for oral suspension/LAMICTAL ODT; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf

## MEDIUM lamotrigine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces non-trusted or overbroad source names with trusted-domain sources that support the row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf; https://www.medicines.org.uk/emc/product/8052/smpc; https://pmc.ncbi.nlm.nih.gov/articles/PMC10712213/; https://clinicaltrials.gov/study/NCT00104416; https://clinicaltrials.gov/study/NCT00113165
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; eMC SmPC; NCBI/PubMed reviews; PubMed randomized placebo-controlled trial reports; ClinicalTrials.gov trial records; Sills and Rogawski 2020 ASM mechanism review

## MEDIUM lamotrigine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: DailyMed should be replaced by FDA/accessdata labeling in named row sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; Sills and Rogawski 2020 ASM mechanism review

## MEDIUM lamotrigine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for black-box-warning verification; FDA/accessdata supports the field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=d7e3572d-56fe-4727-2bb4-013ccca22678; published=Nov 17, 2025; title=LAMICTAL...; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d7e3572d-56fe-4727-2bb4-013ccca22678
- Proposed: FDA/accessdata drug label; status=boxed_warning_found; application=NDA 020241/020764/022251; revised=10/2025; reference_id=5675542; title=LAMICTAL (lamotrigine) tablets/tablets for oral suspension/LAMICTAL ODT; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf

## CRITICAL lamotrigine / proposed_row_update
- Field: maximum_approved_daily_dose
- Status: proposed
- Approval required: True
- Summary: Current value omits FDA-approved XR adjunctive dosing up to 600 mg/day.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/022115s031s032lbl.pdf
- Current: Up to 500 mg/day for adjunctive therapy depending on interacting ASMs
- Proposed: Up to 500 mg/day for immediate-release adjunctive epilepsy depending on interacting ASMs; up to 600 mg/day for Lamictal XR adjunctive therapy depending on concomitant AEDs

## CRITICAL lamotrigine / proposed_row_update
- Field: filter_mechanism
- Status: proposed
- Approval required: True
- Summary: FDA label supports sodium-channel inhibition and reduced glutamate/aspartate release, not glutamate-receptor antagonism.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: Glutamate receptor
- Proposed: Sodium channel; Reduced excitatory amino acid release

## CRITICAL lamotrigine / proposed_row_update
- Field: filter_qt_effect
- Status: proposed
- Approval required: True
- Summary: QT prolongation is not supported as a meaningful lamotrigine effect; conduction/arrhythmia caution is supported.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/studies-show-increased-risk-heart-rhythm-problems-seizure-and-mental-health-medicine-lamotrigine
- Current: Conduction/arrhythmia caution; No known meaningful QT effect; QT prolongation
- Proposed: Conduction/arrhythmia caution; No known meaningful QT effect

## MEDIUM lamotrigine / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Important literature aliases are missing; adding aliases avoids duplicate rows and improves search recall.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10403222/; https://pubmed.ncbi.nlm.nih.gov/2498073/
- Proposed: LTG; Lamictal

## MEDIUM lamotrigine / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: False
- Summary: Matsuo1993 is a missing pivotal randomized placebo-controlled adjunctive partial-seizure efficacy trial; PinaGarza2007 is a negative infant placebo-controlled trial relevant if the dataset keeps negative pediatric studies.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8232944/; https://pubmed.ncbi.nlm.nih.gov/18077797/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: Biton2010|https://pubmed.ncbi.nlm.nih.gov/20937567/; Naritoku2007|https://pubmed.ncbi.nlm.nih.gov/17938371/; Trevathan2006|https://pubmed.ncbi.nlm.nih.gov/16847080/; Pressler2006|https://pubmed.ncbi.nlm.nih.gov/16717207/; Ettinger2006|https://pubmed.ncbi.nlm.nih.gov/17071141/; Biton2005|https://pubmed.ncbi.nlm.nih.gov/16344515/; Frank1999|https://pubmed.ncbi.nlm.nih.gov/10403222/; Duchowny1999|https://pubmed.ncbi.nlm.nih.gov/10563619/; Eriksson1998|https://pubmed.ncbi.nlm.nih.gov/9596201/; Beran1998|https://pubmed.ncbi.nlm.nih.gov/9860069/; Motte1997|https://pubmed.ncbi.nlm.nih.gov/9400037/; Matsuo1996|https://pubmed.ncbi.nlm.nih.gov/8814098/; Boas1996|https://pubmed.ncbi.nlm.nih.gov/8937535/; Messenheimer1994|https://pubmed.ncbi.nlm.nih.gov/8112232/; Schapel1993|https://pubmed.ncbi.nlm.nih.gov/8505632/; Sander1990|https://pubmed.ncbi.nlm.nih.gov/2272345/; Loiseau1990|https://pubmed.ncbi
- Proposed: Append Matsuo1993|https://pubmed.ncbi.nlm.nih.gov/8232944/; consider PinaGarza2007|https://pubmed.ncbi.nlm.nih.gov/18077797/ if negative infant placebo-controlled trials are retained.

## MEDIUM lamotrigine / proposed_row_update
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Adds missing placebo-adjusted median percent reduction from the omitted Matsuo1993 randomized placebo-controlled trial.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8232944/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2025/020241s068s069%2C020764s061s062%2C022251s032s033lbl.pdf
- Current: Biton2010|43.3|https://pubmed.ncbi.nlm.nih.gov/20937567/|153; Naritoku2007|22.1|https://pubmed.ncbi.nlm.nih.gov/17938371/|239; Trevathan2006|37|https://pubmed.ncbi.nlm.nih.gov/16847080/|45; Biton2005|32.3|https://pubmed.ncbi.nlm.nih.gov/16344515/|117; Motte1997|44.8|https://pubmed.ncbi.nlm.nih.gov/9400037/|169; Boas1996|30.3|https://pubmed.ncbi.nlm.nih.gov/8937535/|56; Messenheimer1994|25|https://pubmed.ncbi.nlm.nih.gov/8112232/|98
- Proposed: Biton2010|43.3|https://pubmed.ncbi.nlm.nih.gov/20937567/|153; Naritoku2007|22.1|https://pubmed.ncbi.nlm.nih.gov/17938371/|239; Trevathan2006|37|https://pubmed.ncbi.nlm.nih.gov/16847080/|45; Biton2005|32.3|https://pubmed.ncbi.nlm.nih.gov/16344515/|117; Motte1997|44.8|https://pubmed.ncbi.nlm.nih.gov/9400037/|169; Boas1996|30.3|https://pubmed.ncbi.nlm.nih.gov/8937535/|56; Messenheimer1994|25|https://pubmed.ncbi.nlm.nih.gov/8112232/|98; Matsuo1993|28|https://pubmed.ncbi.nlm.nih.gov/8232944/|216

## HIGH levetiracetam / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Important PubMed/search aliases are missing; older RCT abstracts and labels use LEV/UCB L059 and Keppra.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10897159/; https://pubmed.ncbi.nlm.nih.gov/30525116/
- Proposed: LEV; UCB L059; Keppra

## HIGH levetiracetam / fact_check
- Field: formulations_available
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports tablets, oral solution, IV injection, extended-release tablets, and Spritam tablets for oral suspension. 'Dissolvable tablet' is imprecise.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021035s115%2C021505s053lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2014/021872s016lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/022285s036lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/207958s025lbl.pdf
- Current: Immediate-release tablet; oral solution; IV injection; extended-release tablet; dissolvable tablet
- Proposed: Immediate-release tablet; oral solution; IV injection; extended-release tablet; tablet for oral suspension

## CRITICAL levetiracetam / fact_check
- Field: filter_formulation
- Status: incorrect
- Approval required: True
- Summary: Levetiracetam injection labeling supports intravenous use only; no IM formulation was verified.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2014/021872s016lbl.pdf
- Current: Film/ODT; IV/IM injection; Liquid; Long acting; Tablet
- Proposed: Film/ODT; IV injection; Liquid; Long acting; Tablet

## CRITICAL levetiracetam / fact_check
- Field: enzyme_inducing_or_inhibiting; filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: FDA labeling states levetiracetam is neither an inhibitor nor high-affinity substrate for CYP/epoxide hydrolase/UGT enzymes and does not influence other AED plasma concentrations. The 'Inducer' filter is directly contradicted.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021035s115%2C021505s053lbl.pdf
- Current: Not an enzyme inducer/inhibitor; filter_enzyme_effect=Inducer; No major enzyme effect
- Proposed: Not an enzyme inducer/inhibitor; filter_enzyme_effect=No major enzyme effect

## CRITICAL levetiracetam / fact_check
- Field: adverse_symptoms_percentages; filter_symptom_category
- Status: incorrect
- Approval required: True
- Summary: FDA adult placebo-controlled partial-onset seizure table supports somnolence 15%, asthenia 15%, infection 13%, dizziness 9%, nervousness 4%, and hostility 2%; the 10-13% hostility/nervousness value is not supported as written. Pediatric labeling supports irritability 12%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021035s115%2C021505s053lbl.pdf
- Current: CNS: somnolence 15%, constitutional: asthenia 15%, infectious: infection 13%, CNS: dizziness 9%, behavioral: hostility/nervousness 10-13%
- Proposed: CNS: somnolence 15%, constitutional: asthenia 15%, infectious: infection 13%, CNS: dizziness 9%, behavioral: adult partial-onset trial nervousness 4% and hostility 2%; pediatric 1 month to <4 years irritability 12%

## HIGH levetiracetam / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Primary intervention is JNJ-40411813; levetiracetam/brivaracetam are background concomitant ASMs, so this is not a levetiracetam efficacy RCT.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41175011/
- Current: https://pubmed.ncbi.nlm.nih.gov/41175011/
- Proposed: Do not add to the levetiracetam RCT list.

## HIGH levetiracetam / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: This is a secondary biomarker/Alzheimer's disease report, not a phase II/III placebo-controlled epilepsy efficacy trial for levetiracetam.
- Sources: https://pubmed.ncbi.nlm.nih.gov/39949405/
- Current: https://pubmed.ncbi.nlm.nih.gov/39949405/
- Proposed: Do not add to the epilepsy levetiracetam RCT list.

## HIGH levetiracetam / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Randomized double-blind placebo-controlled pediatric partial-onset seizure trial of adjunctive levetiracetam; abstract reports RR50, median seizure-frequency reduction, and seizure freedom values that alter MPC and seizure-freedom rollups if all qualifying placebo-controlled levetiracetam RCT reports are included.
- Sources: https://pubmed.ncbi.nlm.nih.gov/19702752/
- Proposed: Levisohn2009|https://pubmed.ncbi.nlm.nih.gov/19702752/

## HIGH levetiracetam / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Primary placebo-controlled levetiracetam trial supporting the myoclonic/JME indication; eMC/FDA efficacy summaries report 58.3% versus 23.3% myoclonic seizure-day responder rates.
- Sources: https://pubmed.ncbi.nlm.nih.gov/18285535/
- Proposed: Noachtar2008|https://pubmed.ncbi.nlm.nih.gov/18285535/

## HIGH levetiracetam / outcome_check
- Field: diff_50_responder_maximum_effective_dose; plot_diff_50_responder_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Arithmetic in the currently cited RR50 entries is consistent with active minus placebo. Missing Noachtar2008 and Levisohn2009 add intermediate RR50 values and do not change the min/max range.
- Sources: https://pubmed.ncbi.nlm.nih.gov/30525116/; https://pubmed.ncbi.nlm.nih.gov/18285535/; https://pubmed.ncbi.nlm.nih.gov/19702752/; https://pubmed.ncbi.nlm.nih.gov/19243423/; https://pubmed.ncbi.nlm.nih.gov/19317886/; https://pubmed.ncbi.nlm.nih.gov/18657175/; https://pubmed.ncbi.nlm.nih.gov/19176965/; https://pubmed.ncbi.nlm.nih.gov/17625106/; https://pubmed.ncbi.nlm.nih.gov/16641323/; https://pubmed.ncbi.nlm.nih.gov/16417534/; https://pubmed.ncbi.nlm.nih.gov/11051122/; https://pubmed.ncbi.nlm.nih.gov/10999557/; https://pubmed.ncbi.nlm.nih.gov/10908898/; https://pubmed.ncbi.nlm.nih.gov/10845730/
- Current: 7.1-49.4 % with listed cited RR50 differentials
- Proposed: 7.1-49.4 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Wu2018 LEV 1000-3000 mg/day 49.4%; Noachtar2008 LEV 3000 mg/day 35.0%; PinaGarza2009 LEV 40-50 mg/kg/day 23.5%; Peltola2009 LEV XR 1000 mg/day 13.9%; Wu2008 LEV 1000-3000 mg/day 29.9%; Xiao2009 LEV 3000 mg/day 7.1%; Berkovic2007 LEV target 3000 mg/day adults or 60 mg/kg/day children 27%; Glauser2006 LEV target 60 mg/kg/day 25%; Tsai2006 LEV up to 2000 mg/day 32.9%; Levisohn2009 LEV 20-60 mg/kg/day 21.3%; BenMenachem2000 LEV 3000 mg/day 25.4%; Shorvon2000 LEV 2000 mg/day 21.2%; Cereghino2000 LEV 3000 mg/day 29%; Betts2000 LEV 2000 mg/day 32%)

## HIGH levetiracetam / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose; plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Current cited MPC arithmetic is consistent, but missing Levisohn2009 reports median reductions of 91.5% versus 26.5%, changing the maximum differential to 65.0%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/19702752/; https://pubmed.ncbi.nlm.nih.gov/30525116/; https://pubmed.ncbi.nlm.nih.gov/19243423/; https://pubmed.ncbi.nlm.nih.gov/19317886/; https://pubmed.ncbi.nlm.nih.gov/18657175/; https://pubmed.ncbi.nlm.nih.gov/17625106/; https://pubmed.ncbi.nlm.nih.gov/16641323/; https://pubmed.ncbi.nlm.nih.gov/16417534/
- Current: 12.7-56.2 % with listed cited MPC differentials
- Proposed: 12.7-65.0 % (drug minus placebo MPC differential at maximum effective dose/regimen: Levisohn2009 LEV 20-60 mg/kg/day 65.0%; Wu2018 LEV 1000-3000 mg/day 56.2%; PinaGarza2009 LEV 40-50 mg/kg/day 36.5%; Peltola2009 LEV XR 1000 mg/day 12.7%; Wu2008 LEV 1000-3000 mg/day 42.2%; Berkovic2007 LEV target 3000 mg/day adults or 60 mg/kg/day children 28.3%; Glauser2006 LEV target 60 mg/kg/day 26.8%; Tsai2006 LEV up to 2000 mg/day 23.8%)

## HIGH levetiracetam / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose; plot_diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Current cited seizure-freedom arithmetic is consistent, but missing Levisohn2009 reports seizure freedom of 46.9% versus 8.8%, changing the maximum differential to 38.1%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/19702752/; https://pubmed.ncbi.nlm.nih.gov/30525116/; https://pubmed.ncbi.nlm.nih.gov/19317886/; https://pubmed.ncbi.nlm.nih.gov/18657175/; https://pubmed.ncbi.nlm.nih.gov/17625106/; https://pubmed.ncbi.nlm.nih.gov/16641323/; https://pubmed.ncbi.nlm.nih.gov/11823112/
- Current: 5.1-26.5 % with listed cited seizure-freedom differentials
- Proposed: 5.1-38.1 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Levisohn2009 LEV 20-60 mg/kg/day 38.1%; Wu2018 LEV 1000-3000 mg/day 26.5%; Peltola2009 LEV XR 1000 mg/day 8.8%; Wu2008 LEV 1000-3000 mg/day 8.8%; Berkovic2007 LEV target 3000 mg/day adults or 60 mg/kg/day children 23.5%; Glauser2006 LEV target 60 mg/kg/day 5.9%; Boon2002 LEV 2000 mg/day 5.1%)

## HIGH levetiracetam / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supported by FDA labeling, but DailyMed is not permissible for this field. FDA has required DRESS warnings in Warnings and Precautions, not a boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/022285s036lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5; https://www.fda.gov/drugs/drug-safety-and-availability/fda-warns-rare-serious-drug-reaction-antiseizure-medicines-levetiracetam-keppra-keppra-xr-elepsia-xr
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM levetiracetam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current evidence_sources includes non-trusted/unverified sources and DailyMed wording; replace with trusted source families actually used for the audited cells.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021035s115%2C021505s053lbl.pdf; https://www.fda.gov/drugs/drug-safety-and-availability/fda-warns-rare-serious-drug-reaction-antiseizure-medicines-levetiracetam-keppra-keppra-xr-elepsia-xr; https://www.ncbi.nlm.nih.gov/books/NBK548785/; https://www.ema.europa.eu/en/medicines/human/EPAR/keppra; https://www.medicines.org.uk/emc/product/5166/smpc; https://www.medicines.org.uk/emc/product/15730/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labels and Drugs@FDA; FDA Drug Safety Communication; NCBI LiverTox/Bookshelf; EMA Keppra EPAR; eMC SmPCs for Desitrend and Eltam; PubMed and ClinicalTrials.gov RCT records

## MEDIUM levetiracetam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supported by FDA labeling; DailyMed should not be named as the mechanism source when the source policy prefers FDA/accessdata.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021035s115%2C021505s053lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM levetiracetam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box verification must use FDA/openFDA, FDA labels, or Drugs@FDA; DailyMed is not permissible for this field.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/022285s036lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=2919e43b-69a8-434c-a2d2-1f3ecd7554c0; published=Jun 26, 2025; title=KEPPRA XR (LEVETIRACETAM) TABLET, FILM COATED, EXTENDED RELEASE [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2919e43b-69a8-434c-a2d2-1f3ecd7554c0
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=2919e43b-69a8-434c-a2d2-1f3ecd7554c0; effective_time=20250624; title=Keppra XR / LEVETIRACETAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5

## MEDIUM levetiracetam / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; FDA labeling supports no boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/022285s036lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM levetiracetam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace impermissible DailyMed source with FDA/openFDA metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=2919e43b-69a8-434c-a2d2-1f3ecd7554c0; published=Jun 26, 2025; title=KEPPRA XR (LEVETIRACETAM) TABLET, FILM COATED, EXTENDED RELEASE [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2919e43b-69a8-434c-a2d2-1f3ecd7554c0
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=2919e43b-69a8-434c-a2d2-1f3ecd7554c0; effective_time=20250624; title=Keppra XR / LEVETIRACETAM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222919e43b-69a8-434c-a2d2-1f3ecd7554c0%22&limit=5

## MEDIUM levetiracetam / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Important search aliases are missing.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10897159/; https://pubmed.ncbi.nlm.nih.gov/30525116/
- Proposed: LEV; UCB L059; Keppra

## CRITICAL levetiracetam / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: The behavioral 10-13% wording is not supported by the FDA adverse-reaction table.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021035s115%2C021505s053lbl.pdf
- Current: CNS: somnolence 15%, constitutional: asthenia 15%, infectious: infection 13%, CNS: dizziness 9%, behavioral: hostility/nervousness 10-13%
- Proposed: CNS: somnolence 15%, constitutional: asthenia 15%, infectious: infection 13%, CNS: dizziness 9%, behavioral: adult partial-onset trial nervousness 4% and hostility 2%; pediatric 1 month to <4 years irritability 12%

## MEDIUM levetiracetam / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: False
- Summary: Use the FDA dosage-form wording for Spritam.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/207958s025lbl.pdf
- Current: Immediate-release tablet; oral solution; IV injection; extended-release tablet; dissolvable tablet
- Proposed: Immediate-release tablet; oral solution; IV injection; extended-release tablet; tablet for oral suspension

## CRITICAL levetiracetam / proposed_row_update
- Field: filter_formulation
- Status: proposed
- Approval required: True
- Summary: FDA labeling supports IV injection only, not IM injection.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2014/021872s016lbl.pdf
- Current: Film/ODT; IV/IM injection; Liquid; Long acting; Tablet
- Proposed: Film/ODT; IV injection; Liquid; Long acting; Tablet

## CRITICAL levetiracetam / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: Levetiracetam is not an enzyme inducer/inhibitor; the Inducer filter is contradicted by FDA labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021035s115%2C021505s053lbl.pdf
- Current: Inducer; No major enzyme effect
- Proposed: No major enzyme effect

## HIGH lorazepam / fact_check
- Field: formulations_available
- Status: incorrect
- Approval required: False
- Summary: The current value is incomplete because FDA approved Loreev XR lorazepam extended-release capsules. Tablet, oral concentrate, and IV/IM injection are supported by FDA labels.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017794s049lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2009/079244lbl.PDF; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/214826s003lbl.pdf
- Current: Tablet; oral concentrate; IV/IM injection
- Proposed: Tablet; oral concentrate; IV/IM injection; extended-release capsule

## CRITICAL lorazepam / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: FDA tablet/oral concentrate labeling gives sedation 15.9%, dizziness 6.9%, weakness 4.2%, and unsteadiness 3.4%. Respiratory depression is listed as an adverse reaction/warning but not as a 3% event in the cited labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017794s049lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2009/079244lbl.PDF
- Current: CNS: sedation 16%, CNS: dizziness 7%, constitutional: weakness 4%, respiratory: respiratory depression 3%
- Proposed: CNS: sedation 15.9%, CNS: dizziness 6.9%, constitutional: weakness 4.2%, CNS: unsteadiness 3.4%

## MEDIUM lorazepam / fact_check
- Field: epilepsy_type
- Status: missing_source
- Approval required: False
- Summary: FDA injection labeling supports status epilepticus. The seizure-clusters/rescue portion is plausible clinically but needs a named trusted source in the row; the cited FDA label does not specifically support seizure clusters.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf
- Current: Status epilepticus; Seizure clusters / rescue
- Proposed: Status epilepticus; Seizure clusters / rescue

## HIGH lorazepam / fact_check
- Field: maximum_approved_daily_dose
- Status: incorrect
- Approval required: False
- Summary: The current text is too vague for a maximum-dose field. FDA labeling gives the adult status epilepticus regimen and oral daily dosage range.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017794s049lbl.pdf
- Current: Acute seizure dosing individualized
- Proposed: Status epilepticus: 4 mg IV slowly; may repeat 4 mg IV once after 10-15 minutes if seizures continue or recur; experience with further doses is very limited. Oral anxiety labeling: 1-10 mg/day.

## HIGH lorazepam / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: The row's value is directionally correct that this is acute/intermittent treatment, but FDA labeling supports a more precise status epilepticus regimen.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf
- Current: Acute seizure/status dosing individualized
- Proposed: No chronic epilepsy minimum effective dose; status epilepticus adult FDA-labeled regimen is 4 mg IV slowly, with one repeat 4 mg dose after 10-15 minutes if needed.

## MEDIUM lorazepam / fact_check
- Field: qt_interval_effect
- Status: missing_source
- Approval required: False
- Summary: No contradiction was found in the reviewed FDA labels, but the row lacks a named source specifically supporting the QT statement.
- Current: No clinically meaningful QT effect established
- Proposed: No clinically meaningful QT effect established

## HIGH lorazepam / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Wikipedia is not in the trusted source list, and DailyMed must not be used for FDA boxed-warning verification. The proposed source text names trusted FDA, PubMed/NCBI, and ClinicalTrials.gov sources actually used for the checked facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017794s049lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/6378615/; https://pubmed.ncbi.nlm.nih.gov/11547716/; https://clinicaltrials.gov/study/NCT00004297
- Current: Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling (Ativan tablets NDA 017794; Ativan injection NDA 018140; Loreev XR NDA 214826; lorazepam oral concentrate ANDA 079244); PubMed/NCBI RCT records; ClinicalTrials.gov NCT00004297

## HIGH lorazepam / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: PubMed verifies lorazepam, randomized assignment, double-blind placebo-controlled crossover design, and PMID 6378615. PubMed publication type is Clinical Trial, not Phase II/III, and the trial had only eight patients.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6378615/
- Current: https://pubmed.ncbi.nlm.nih.gov/6378615/
- Proposed: Do not count as a phase II/III RCT unless the dataset permits historical non-phase placebo-controlled trials; otherwise replace with Alldredge2001 for the phase II/III field.

## HIGH lorazepam / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed verifies a randomized double-blind trial of IV lorazepam, diazepam, and placebo for out-of-hospital status epilepticus; ClinicalTrials.gov NCT00004297 identifies the study as phase III. Lorazepam 59.1% vs placebo 21.1% termination of status epilepticus on ED arrival is extractable as an acute seizure-termination endpoint, not RR50/MPC.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11547716/
- Proposed: Alldredge2001|https://pubmed.ncbi.nlm.nih.gov/11547716/

## MEDIUM lorazepam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for the FDA black-box-warning field; the FDA accessdata label supports the current warning text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=5fc0e987-61c9-40c4-b0d5-fcea07c8733e; published=Apr 10, 2023; title=ATIVAN (LORAZEPAM) INJECTION [HIKMA PHARMACEUTICALS USA INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=5fc0e987-61c9-40c4-b0d5-fcea07c8733e
- Proposed: FDA/Drugs@FDA label; status=boxed_warning_found; NDA=018140; Reference ID=5109772; title=ATIVAN Injection (lorazepam injection, USP); revised=Jan 2023; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf

## MEDIUM lorazepam / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Boxed warning was rechecked against an FDA label source during this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## MEDIUM lorazepam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces non-trusted/impermissible source names with trusted source categories that support the checked cells.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017794s049lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2009/079244lbl.PDF; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/214826s003lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/11547716/; https://clinicaltrials.gov/study/NCT00004297
- Current: Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review; FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling (Ativan tablets NDA 017794; Ativan injection NDA 018140; Loreev XR NDA 214826; lorazepam oral concentrate ANDA 079244); PubMed/NCBI RCT records; ClinicalTrials.gov NCT00004297

## MEDIUM lorazepam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA labeling directly supports the GABA-benzodiazepine receptor mechanism used in the row; AES was not verified from a trusted URL in this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf
- Current: American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA Ativan Injection label

## CRITICAL lorazepam / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Corrects the FDA-labeled common adverse event percentages and replaces unsupported respiratory depression 3%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017794s049lbl.pdf
- Current: CNS: sedation 16%, CNS: dizziness 7%, constitutional: weakness 4%, respiratory: respiratory depression 3%
- Proposed: CNS: sedation 15.9%, CNS: dizziness 6.9%, constitutional: weakness 4.2%, CNS: unsteadiness 3.4%

## MEDIUM lorazepam / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: False
- Summary: Adds FDA-approved Loreev XR extended-release capsule formulation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/214826s003lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2022/214826Orig1s000Approv.pdf
- Current: Tablet; oral concentrate; IV/IM injection
- Proposed: Tablet; oral concentrate; IV/IM injection; extended-release capsule

## MEDIUM lorazepam / proposed_row_update
- Field: filter_formulation
- Status: proposed
- Approval required: False
- Summary: Derived filter should include the FDA-approved Loreev XR extended-release capsule formulation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/214826s003lbl.pdf
- Current: IV/IM injection; Liquid; Tablet
- Proposed: Capsule; IV/IM injection; Liquid; Tablet

## MEDIUM lorazepam / proposed_row_update
- Field: maximum_approved_daily_dose
- Status: proposed
- Approval required: False
- Summary: FDA labels provide more precise acute status epilepticus and oral dosing limits than the current vague wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/017794s049lbl.pdf
- Current: Acute seizure dosing individualized
- Proposed: Status epilepticus: 4 mg IV slowly; may repeat 4 mg IV once after 10-15 minutes if seizures continue or recur; experience with further doses is very limited. Oral anxiety labeling: 1-10 mg/day.

## MEDIUM lorazepam / proposed_row_update
- Field: minimum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Clarifies that lorazepam does not have a chronic epilepsy minimum effective dose and cites the FDA status epilepticus regimen.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf
- Current: Acute seizure/status dosing individualized
- Proposed: No chronic epilepsy minimum effective dose; status epilepticus adult FDA-labeled regimen is 4 mg IV slowly, with one repeat 4 mg dose after 10-15 minutes if needed.

## CRITICAL lorazepam / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: Walker1984 is placebo-controlled and randomized but not verified as phase II/III. Alldredge2001 is the missing placebo-controlled lorazepam status epilepticus RCT associated with phase III NCT00004297.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6378615/; https://pubmed.ncbi.nlm.nih.gov/11547716/; https://clinicaltrials.gov/study/NCT00004297
- Current: Walker1984|https://pubmed.ncbi.nlm.nih.gov/6378615/
- Proposed: Alldredge2001|https://pubmed.ncbi.nlm.nih.gov/11547716/

## CRITICAL lorazepam / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: True
- Summary: Corrects the retained/rejected RCT interpretation and documents the extractable acute endpoint separately from RR50/MPC/seizure freedom.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6378615/; https://pubmed.ncbi.nlm.nih.gov/11547716/; https://clinicaltrials.gov/study/NCT00004297
- Current: PubMed loop 29/65 on 2026-05-15: 1 qualifying placebo-controlled randomized clinical trial report(s) retained from 11 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit 2026-05-21: Walker1984 PMID 6378615 is a lorazepam double-blind placebo-controlled crossover clinical trial but is not verified as phase II/III. Alldredge2001 PMID 11547716 is a randomized double-blind lorazepam/diazepam/placebo out-of-hospital status epilepticus trial associated with phase III NCT00004297 and should be included if this field is restricted to phase II/III placebo-controlled RCTs. RR50, MPC, and standard seizure-freedom endpoints remain not extractable; Alldredge2001 reports acute status-termination 59.1% lorazepam vs 21.1% placebo.

## MEDIUM lorazepam / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: The reviewed trusted source directly supporting the mechanism is FDA labeling; AES was not cited from a trusted source URL in this audit bundle.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/018140s051lbl.pdf
- Current: AES/FDA summary
- Proposed: FDA labeling

## HIGH mephenytoin / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: NCBI MeSH lists these as Mephenytoin entry terms. They should be captured as aliases rather than separate drug rows.
- Sources: https://www.ncbi.nlm.nih.gov/mesh?Cmd=DetailsSearch&Db=mesh&Term=%22Mephenytoin%22%5BMeSH%20Terms%5D
- Proposed: Methoin; methyl phenetoin; mefenetoin; 5-ethyl-3-methyl-5-phenylhydantoin; Phenantoin

## HIGH mephenytoin / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: The PubMed search alias list should include the NCBI MeSH entry terms so alias-only literature is not missed.
- Sources: https://www.ncbi.nlm.nih.gov/mesh?Cmd=DetailsSearch&Db=mesh&Term=%22Mephenytoin%22%5BMeSH%20Terms%5D
- Current: Mesantoin
- Proposed: Mesantoin; Methoin; methyl phenetoin; mefenetoin; Phenantoin; 5-ethyl-3-methyl-5-phenylhydantoin

## HIGH mephenytoin / fact_check
- Field: mechanism_of_action
- Status: missing
- Approval required: False
- Summary: The current FDA/Orange Book source does not provide a mechanism, but NCBI/PubMed sources support a limited non-label mechanism entry rather than N/A.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Hydantoin-class antiseizure drug; exact drug-specific mechanism is limited, but mephenytoin/hydantoin sources describe reduced high-frequency neuronal firing through voltage-gated sodium-channel effects.

## HIGH mephenytoin / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: Orange Book supports product identity, not mechanism. Mechanism should cite the NCBI/PubMed pharmacology sources if populated.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: FDA Orange Book products file
- Proposed: NCBI PubChem pharmacology records; Sills and Rogawski 2020 ASM mechanism review

## HIGH mephenytoin / fact_check
- Field: half_life_range
- Status: missing
- Approval required: False
- Summary: The FDA label is unavailable, but NCBI/PubMed-indexed pharmacokinetic evidence and PubChem report half-life values; the N/A value is missing available evidence.
- Sources: https://pubmed.ncbi.nlm.nih.gov/42344/; https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: Mephenytoin approximately 7 hours; active metabolite 5-ethyl-5-phenylhydantoin/nirvanol approximately 96 hours (reported range about 95-144 hours).

## HIGH mephenytoin / fact_check
- Field: major_organ_for_metabolism
- Status: missing
- Approval required: False
- Summary: PubMed/PMC literature identifies CYP2C19-mediated mephenytoin metabolism, so the metabolism field should not remain N/A solely because a current FDA label is unavailable.
- Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC2014478/; https://pubmed.ncbi.nlm.nih.gov/9435198/; https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Hepatic CYP metabolism, especially CYP2C19-mediated S-mephenytoin hydroxylation; additional CYP enzymes are reported in NCBI/PubChem records.

## MEDIUM mephenytoin / fact_check
- Field: adverse_symptoms_percentages
- Status: missing_source
- Approval required: True
- Summary: No adverse-event percentages are supported by the cited FDA sources. The embedded '0%' is not an evidence-based adverse-event percentage and should be removed if the field is intended to contain sourced percentages.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A: no current FDA/openFDA label identified; FDA Orange Book product listing does not provide adverse-event percentages.

## HIGH mephenytoin / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be used for the boxed-warning field, and the row needs NCBI/PubMed sources for aliases, mechanism, half-life, metabolism, and RCT absence.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://open.fda.gov/apis/drug/label/; https://www.ncbi.nlm.nih.gov/mesh?Cmd=DetailsSearch&Db=mesh&Term=%22Mephenytoin%22%5BMeSH%20Terms%5D; https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/?term=%28mephenytoin%20OR%20Mesantoin%29%20epilepsy%20placebo%20randomized
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling; NCBI MeSH; NCBI PubChem; PubMed/NCBI literature search

## HIGH mephenytoin / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: Underlying no-current-label conclusion is consistent with the provided FDA/openFDA audit finding, but DailyMed is not permissible for the boxed-warning field. Use FDA/openFDA wording only.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22MEPHENYTOIN%22&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22MESANTOIN%22&limit=1
- Current: No current FDA/DailyMed label identified. Source: FDA/DailyMed search on 05-20-2026: no current label found for terms [mephenytoin; Mesantoin].
- Proposed: No current FDA/openFDA label identified. Source: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [mephenytoin; Mesantoin].

## MEDIUM mephenytoin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: DailyMed is not allowed for the boxed-warning field, and additional NCBI/PubMed sources are needed for aliases, mechanism, PK/metabolism, and RCT absence.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://open.fda.gov/apis/drug/label/; https://www.ncbi.nlm.nih.gov/mesh?Cmd=DetailsSearch&Db=mesh&Term=%22Mephenytoin%22%5BMeSH%20Terms%5D; https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/?term=%28mephenytoin%20OR%20Mesantoin%29%20epilepsy%20placebo%20randomized
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling; NCBI MeSH; NCBI PubChem; PubMed/NCBI literature search

## MEDIUM mephenytoin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: FDA boxed-warning verification must use FDA/openFDA, FDA label, or Drugs@FDA sources only.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22MEPHENYTOIN%22&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22MESANTOIN%22&limit=1
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [mephenytoin; Mesantoin].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [mephenytoin; Mesantoin].

## MEDIUM mephenytoin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA Orange Book product data do not support mechanism of action.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: FDA Orange Book products file
- Proposed: NCBI PubChem pharmacology records; Sills and Rogawski 2020 ASM mechanism review

## MEDIUM mephenytoin / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Important NCBI MeSH aliases are missing.
- Sources: https://www.ncbi.nlm.nih.gov/mesh?Cmd=DetailsSearch&Db=mesh&Term=%22Mephenytoin%22%5BMeSH%20Terms%5D
- Proposed: Methoin; methyl phenetoin; mefenetoin; 5-ethyl-3-methyl-5-phenylhydantoin; Phenantoin

## MEDIUM mephenytoin / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add MeSH entry terms to improve PubMed retrieval.
- Sources: https://www.ncbi.nlm.nih.gov/mesh?Cmd=DetailsSearch&Db=mesh&Term=%22Mephenytoin%22%5BMeSH%20Terms%5D
- Current: Mesantoin
- Proposed: Mesantoin; Methoin; methyl phenetoin; mefenetoin; Phenantoin; 5-ethyl-3-methyl-5-phenylhydantoin

## MEDIUM mephenytoin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed wording for FDA boxed-warning compliance and add sources that support aliases, mechanism, PK/metabolism, and RCT absence.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://open.fda.gov/apis/drug/label/; https://www.ncbi.nlm.nih.gov/mesh?Cmd=DetailsSearch&Db=mesh&Term=%22Mephenytoin%22%5BMeSH%20Terms%5D; https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/?term=%28mephenytoin%20OR%20Mesantoin%29%20epilepsy%20placebo%20randomized
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling; NCBI MeSH; NCBI PubChem; PubMed/NCBI literature search

## MEDIUM mephenytoin / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification in this audit.
- Sources: https://open.fda.gov/apis/drug/label/
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM mephenytoin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Use FDA/openFDA source wording only for boxed-warning metadata.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22MEPHENYTOIN%22&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22MESANTOIN%22&limit=1
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [mephenytoin; Mesantoin].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [mephenytoin; Mesantoin].

## MEDIUM mephenytoin / proposed_row_update
- Field: mechanism_of_action
- Status: proposed
- Approval required: False
- Summary: NCBI/PubMed sources support a limited mechanism entry.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Hydantoin-class antiseizure drug; exact drug-specific mechanism is limited, but mephenytoin/hydantoin sources describe reduced high-frequency neuronal firing through voltage-gated sodium-channel effects.

## MEDIUM mephenytoin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Orange Book does not support mechanism.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: FDA Orange Book products file
- Proposed: NCBI PubChem pharmacology records; Sills and Rogawski 2020 ASM mechanism review

## MEDIUM mephenytoin / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: Reflects historical/non-label mechanism support.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin; https://pubmed.ncbi.nlm.nih.gov/32120063/
- Current: Historical/limited
- Proposed: Historical/limited; NCBI/PubMed secondary pharmacology

## MEDIUM mephenytoin / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: PK evidence is available from PubMed-indexed/PubChem sources.
- Sources: https://pubmed.ncbi.nlm.nih.gov/42344/; https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: Mephenytoin approximately 7 hours; active metabolite 5-ethyl-5-phenylhydantoin/nirvanol approximately 96 hours (reported range about 95-144 hours).

## MEDIUM mephenytoin / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: False
- Summary: Mephenytoin is a CYP2C19 phenotype probe with documented CYP metabolism.
- Sources: https://pmc.ncbi.nlm.nih.gov/articles/PMC2014478/; https://pubmed.ncbi.nlm.nih.gov/9435198/; https://pubchem.ncbi.nlm.nih.gov/compound/Mephenytoin
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Hepatic CYP metabolism, especially CYP2C19-mediated S-mephenytoin hydroxylation; additional CYP enzymes are reported in NCBI/PubChem records.

## MEDIUM mephenytoin / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: False
- Summary: FDA Orange Book product data support tablet/oral and 100 mg strength.
- Sources: https://www.accessdata.fda.gov/scripts/cder/ob/results_product.cfm?Appl_Type=N&Appl_No=006008; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: Historical oral tablet (not marketed in U.S.)
- Proposed: Historical oral tablet, 100 mg (Mesantoin; discontinued/not marketed in U.S.)

## CRITICAL mephenytoin / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: No sourced adverse-event percentages were found; '0%' is unsupported as a percentage fact.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A: no current FDA/openFDA label identified; FDA Orange Book product listing does not provide adverse-event percentages.

## MEDIUM mephenytoin / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: False
- Summary: Source wording should use FDA/openFDA rather than DailyMed.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe QT effect.
- Proposed: N/A - no current FDA/openFDA label located and FDA Orange Book product listing does not describe QT effect.

## MEDIUM mephenytoin / proposed_row_update
- Field: typical_doses_per_day
- Status: proposed
- Approval required: False
- Summary: Source wording should use FDA/openFDA rather than DailyMed.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide dosing.
- Proposed: N/A - no current FDA/openFDA label located and FDA Orange Book product listing does not provide dosing.

## MEDIUM mephenytoin / proposed_row_update
- Field: minimum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Source wording should use FDA/openFDA rather than DailyMed.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a minimum effective dose.
- Proposed: N/A - no current FDA/openFDA label located and FDA Orange Book product listing does not provide a minimum effective dose.

## MEDIUM mephenytoin / proposed_row_update
- Field: maximum_approved_daily_dose
- Status: proposed
- Approval required: False
- Summary: Source wording should use FDA/openFDA rather than DailyMed.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a maximum approved daily dose.
- Proposed: N/A - no current FDA/openFDA label located and FDA Orange Book product listing does not provide a maximum approved daily dose.

## HIGH metharbital / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: Important aliases are missing. PubChem/MeSH lists endiemal, metharbitone, and methobarbitone, and PubChem depositor synonyms include metarbital. These should be captured to avoid alias-based duplicate rows/search misses.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Metharbital
- Proposed: Endiemal; metharbitone; methobarbitone; metarbital

## HIGH metharbital / fact_check
- Field: pubmed_search_aliases
- Status: incorrect
- Approval required: False
- Summary: Current value is incomplete for literature search. Adding common NCBI/PubChem/MeSH aliases improves PubMed recall without creating a separate drug row.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Metharbital
- Current: Gemonil
- Proposed: Gemonil; Endiemal; metharbitone; methobarbitone; metarbital

## HIGH metharbital / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be used for boxed-warning verification, and the row now needs an explicit NCBI/PubChem alias source. openFDA is the appropriate FDA label-search source for the no-current-label finding.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://open.fda.gov/apis/drug/label/; https://pubchem.ncbi.nlm.nih.gov/compound/Metharbital
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling API; NCBI PubChem/MeSH aliases

## HIGH metharbital / fact_check
- Field: mechanism_of_action
- Status: incorrect
- Approval required: False
- Summary: The substantive N/A mechanism conclusion is supported by absence of a current FDA label and Orange Book field limitations, but source wording should be FDA/openFDA rather than FDA/DailyMed.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: N/A - no current FDA/openFDA label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.

## HIGH metharbital / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: Substantive no-current-FDA-label finding is plausible, but boxed-warning verification must cite FDA/openFDA, FDA label, or Drugs@FDA only. DailyMed should not appear in this boxed-warning field.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM metharbital / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current source list cites DailyMed despite boxed-warning policy and omits alias source coverage.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://open.fda.gov/apis/drug/label/; https://pubchem.ncbi.nlm.nih.gov/compound/Metharbital
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling API; NCBI PubChem/MeSH aliases

## MEDIUM metharbital / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: FDA-only source wording required for boxed-warning verification.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [metharbital; Gemonil].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [metharbital; Gemonil].

## MEDIUM metharbital / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Add important aliases supported by NCBI/PubChem/MeSH.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Metharbital
- Proposed: Endiemal; metharbitone; methobarbitone; metarbital

## MEDIUM metharbital / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Improve PubMed recall and alias deduplication.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Metharbital
- Current: Gemonil
- Proposed: Gemonil; Endiemal; metharbitone; methobarbitone; metarbital

## MEDIUM metharbital / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed boxed-warning source dependency and add alias source coverage.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://open.fda.gov/apis/drug/label/; https://pubchem.ncbi.nlm.nih.gov/compound/Metharbital
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA/openFDA labeling API; NCBI PubChem/MeSH aliases

## MEDIUM metharbital / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Boxed-warning field must use FDA/openFDA, FDA labels, or Drugs@FDA only.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM metharbital / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; use FDA/openFDA source wording.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [metharbital; Gemonil].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [metharbital; Gemonil].

## HIGH methsuximide / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: NCBI LiverTox states methsuximide is also called mesuximide. This alias should be captured to avoid duplicate-row treatment.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548535/
- Proposed: mesuximide

## CRITICAL methsuximide / fact_check
- Field: trade_names
- Status: incorrect
- Approval required: True
- Summary: Celontin is the proprietary/brand name; methsuximide is the established generic name already captured in generic_name, not a separate trade name.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548535/
- Current: Celontin; Methsuximide
- Proposed: Celontin

## HIGH methsuximide / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Mesuximide is a documented alternate name and should be included as a search alias.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548535/
- Current: Celontin
- Proposed: Celontin; mesuximide

## MEDIUM methsuximide / fact_check
- Field: mechanism_source
- Status: missing_source
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; DailyMed should not be the named source when FDA/accessdata and openFDA sources are available.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Current: FDA/DailyMed labeling
- Proposed: FDA Drugs@FDA/accessdata labeling; FDA/openFDA labeling

## CRITICAL methsuximide / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The current statement is directionally supported but the '0%' prefix is misleading and the list omits several labeled adverse reactions.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: N/A 0%: FDA label lists nausea/vomiting, anorexia, diarrhea, weight loss, epigastric/abdominal pain, constipation, drowsiness, ataxia/dizziness, irritability/nervousness, headache, blurred vision, photophobia, hiccups, insomnia, confusion, depression, psychosis, urticaria, SJS, rash, and blood dyscrasias without quantified incidence percentages.
- Proposed: N/A: FDA labeling reports adverse reactions without incidence percentages. Listed reactions include GI symptoms, hematologic abnormalities/blood dyscrasias, neurologic and sensory symptoms, psychiatric abnormalities including rare psychosis/suicidal behavior/auditory hallucinations, dermatologic reactions including Stevens-Johnson syndrome, hyperemia, proteinuria/microscopic hematuria, and periorbital edema.

## HIGH methsuximide / fact_check
- Field: filter_symptom_category
- Status: missing
- Approval required: False
- Summary: FDA labeling also lists hyperemia, proteinuria/microscopic hematuria, and periorbital edema.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: CNS; Dermatologic; GI; Hematologic; Neurologic; Psychiatric
- Proposed: CNS; Dermatologic; GI; Hematologic; Neurologic; Psychiatric; Cardiovascular; Genitourinary; General/Other

## HIGH methsuximide / fact_check
- Field: half_life_range
- Status: missing
- Approval required: False
- Summary: The FDA label caveat is true, but a trusted PubMed pharmacology source provides half-life values for the principal plasma substance/active metabolite, so N/A is incomplete.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6403891/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: N/A - selected FDA/DailyMed label does not provide a half-life value; label notes an active N-desmethylmethsuximide metabolite in overdose.
- Proposed: Active metabolite N-desmethylmethsuximide: accumulation half-life 49.7 hours and elimination half-life 72.2 hours in PubMed PMID 6403891; FDA labeling notes active N-desmethylmethsuximide in overdose but does not provide half-life.

## CRITICAL methsuximide / fact_check
- Field: major_organ_for_metabolism
- Status: missing
- Approval required: True
- Summary: The label-only limitation is true, but NCBI provides a trusted source for hepatic metabolism.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548535/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: N/A - selected FDA/DailyMed label does not identify a major metabolic organ; label notes active N-desmethylmethsuximide metabolite and advises liver/renal caution.
- Proposed: Hepatic/liver; NCBI LiverTox states methsuximide is metabolized in the liver via the cytochrome P450 system (CYP3A4). FDA labeling notes active N-desmethylmethsuximide in overdose and advises liver/renal caution.

## CRITICAL methsuximide / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: True
- Summary: NCBI LiverTox identifies liver metabolism via CYP3A4, so the filter should not remain limited/unknown.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548535/
- Current: Limited/unknown
- Proposed: Hepatic

## MEDIUM methsuximide / fact_check
- Field: evidence_sources
- Status: missing_source
- Approval required: False
- Summary: DailyMed should not be used as the named FDA source for the boxed-warning field, and additional trusted sources are needed for aliases, metabolism, and half-life.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2010/010596s022ltr.pdf; https://www.fda.gov/drugs/generic-drugs/competitive-generic-therapy-approvals; https://www.ncbi.nlm.nih.gov/books/NBK548535/; https://pubmed.ncbi.nlm.nih.gov/6403891/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling and approval correspondence; FDA CGT approvals list; NCBI LiverTox; PubMed PMID 6403891

## HIGH methsuximide / fact_check
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The warning conclusion is supported, but the source wording must be changed from DailyMed to FDA/openFDA.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## HIGH methsuximide / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is impermissible for black-box verification under the row audit policy; FDA/openFDA is acceptable.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=64a6ee88-c6b1-4e13-8208-b6772ef65a74; published=Apr 09, 2026; title=CELONTIN (METHSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=64a6ee88-c6b1-4e13-8208-b6772ef65a74
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=64a6ee88-c6b1-4e13-8208-b6772ef65a74; effective_time=20260407; title=Celontin / METHSUXIMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5

## HIGH methsuximide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supported, but the current row cites DailyMed for the boxed-warning field, which is not permissible under the audit policy. Use the FDA/openFDA label API metadata instead.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM methsuximide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box verification must use FDA/openFDA, FDA labels, or Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=64a6ee88-c6b1-4e13-8208-b6772ef65a74; published=Apr 09, 2026; title=CELONTIN (METHSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=64a6ee88-c6b1-4e13-8208-b6772ef65a74
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=64a6ee88-c6b1-4e13-8208-b6772ef65a74; effective_time=20260407; title=Celontin / METHSUXIMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5

## MEDIUM methsuximide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: The retained facts now need explicit trusted-source support for label, approval/availability, alias, metabolism, and half-life claims.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2010/010596s022ltr.pdf; https://www.fda.gov/drugs/generic-drugs/competitive-generic-therapy-approvals; https://www.ncbi.nlm.nih.gov/books/NBK548535/; https://pubmed.ncbi.nlm.nih.gov/6403891/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling and approval correspondence; FDA CGT approvals list; NCBI LiverTox; PubMed PMID 6403891

## MEDIUM methsuximide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Use FDA-accessible labeling directly for mechanism support.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Current: FDA/DailyMed labeling
- Proposed: FDA Drugs@FDA/accessdata labeling; FDA/openFDA labeling

## MEDIUM methsuximide / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Documented NCBI alias.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548535/
- Proposed: mesuximide

## CRITICAL methsuximide / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: True
- Summary: Methsuximide is the generic name, not a separate trade name.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548535/
- Current: Celontin; Methsuximide
- Proposed: Celontin

## MEDIUM methsuximide / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add documented alternate name for literature searches.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548535/
- Current: Celontin
- Proposed: Celontin; mesuximide

## MEDIUM methsuximide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Use trusted FDA sources directly rather than DailyMed wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Current: FDA/DailyMed labeling
- Proposed: FDA Drugs@FDA/accessdata labeling; FDA/openFDA labeling

## CRITICAL methsuximide / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Avoid misleading '0%' wording and include omitted labeled adverse reactions.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: N/A 0%: FDA label lists nausea/vomiting, anorexia, diarrhea, weight loss, epigastric/abdominal pain, constipation, drowsiness, ataxia/dizziness, irritability/nervousness, headache, blurred vision, photophobia, hiccups, insomnia, confusion, depression, psychosis, urticaria, SJS, rash, and blood dyscrasias without quantified incidence percentages.
- Proposed: N/A: FDA labeling reports adverse reactions without incidence percentages. Listed reactions include GI symptoms, hematologic abnormalities/blood dyscrasias, neurologic and sensory symptoms, psychiatric abnormalities including rare psychosis/suicidal behavior/auditory hallucinations, dermatologic reactions including Stevens-Johnson syndrome, hyperemia, proteinuria/microscopic hematuria, and periorbital edema.

## MEDIUM methsuximide / proposed_row_update
- Field: filter_symptom_category
- Status: proposed
- Approval required: False
- Summary: FDA labeling includes hyperemia, urinary findings, and periorbital edema.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: CNS; Dermatologic; GI; Hematologic; Neurologic; Psychiatric
- Proposed: CNS; Dermatologic; GI; Hematologic; Neurologic; Psychiatric; Cardiovascular; Genitourinary; General/Other

## MEDIUM methsuximide / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: Trusted PubMed source provides active-metabolite half-life values.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6403891/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: N/A - selected FDA/DailyMed label does not provide a half-life value; label notes an active N-desmethylmethsuximide metabolite in overdose.
- Proposed: Active metabolite N-desmethylmethsuximide: accumulation half-life 49.7 hours and elimination half-life 72.2 hours in PubMed PMID 6403891; FDA labeling notes active N-desmethylmethsuximide in overdose but does not provide half-life.

## CRITICAL methsuximide / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: True
- Summary: NCBI source identifies hepatic metabolism.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548535/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf
- Current: N/A - selected FDA/DailyMed label does not identify a major metabolic organ; label notes active N-desmethylmethsuximide metabolite and advises liver/renal caution.
- Proposed: Hepatic/liver; NCBI LiverTox states methsuximide is metabolized in the liver via the cytochrome P450 system (CYP3A4). FDA labeling notes active N-desmethylmethsuximide in overdose and advises liver/renal caution.

## CRITICAL methsuximide / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: True
- Summary: NCBI LiverTox supports hepatic metabolism.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548535/
- Current: Limited/unknown
- Proposed: Hepatic

## MEDIUM methsuximide / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: FDA accessdata approval correspondence provides the exact original approval date.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2010/010596s022ltr.pdf
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: Approved February 8, 1957 (NDA 010596; predates Jan 1, 1982).

## MEDIUM methsuximide / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; FDA/openFDA is.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM methsuximide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace impermissible DailyMed boxed-warning source with FDA/openFDA source.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=64a6ee88-c6b1-4e13-8208-b6772ef65a74; published=Apr 09, 2026; title=CELONTIN (METHSUXIMIDE) CAPSULE [PARKE-DAVIS DIV OF PFIZER INC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=64a6ee88-c6b1-4e13-8208-b6772ef65a74
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=64a6ee88-c6b1-4e13-8208-b6772ef65a74; effective_time=20260407; title=Celontin / METHSUXIMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5

## MEDIUM methsuximide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Add trusted sources for FDA label facts, FDA approval/availability, alias/metabolism, and half-life; remove DailyMed as named source.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2264a6ee88-c6b1-4e13-8208-b6772ef65a74%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/010596s22lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2010/010596s022ltr.pdf; https://www.fda.gov/drugs/generic-drugs/competitive-generic-therapy-approvals; https://www.ncbi.nlm.nih.gov/books/NBK548535/; https://pubmed.ncbi.nlm.nih.gov/6403891/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA/openFDA labeling; FDA Drugs@FDA/accessdata labeling and approval correspondence; FDA CGT approvals list; NCBI LiverTox; PubMed PMID 6403891

## HIGH methylphenobarbital / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The mechanism source is a Croatian HALMED SmPC, not an EMA SmPC or UK/eMC SmPC. EMA PSUSA supports national authorization but not the mechanism wording.
- Sources: https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf; https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf
- Current: EMA/UK SmPC
- Proposed: National SmPC (HALMED/Croatia)

## HIGH methylphenobarbital / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: The current phrase 'unknown frequency 0%' is wrong: unknown frequency means cannot be estimated from available data, not 0%. The replacement also adds adverse events listed in the SmPC but omitted from the row.
- Sources: https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf
- Current: HALMED SmPC frequency categories: very rare events <0.01% include megaloblastic anemia; unknown frequency 0% exact percentage unavailable for CNS depression, mood changes/depression, dependence, nervousness, dizziness, somnolence, nystagmus, ataxia, headache, nausea, vomiting, constipation, bradycardia, respiratory insufficiency, SJS/TEN, rash, angioedema, osteomalacia/rickets.
- Proposed: HALMED SmPC frequency categories: very rare (<0.01%) includes megaloblastic anemia; frequency unknown (cannot be estimated from available data; exact percentages unavailable) includes folate deficiency, CNS depression, mood changes/depression, psychological and physical dependence, nervousness, dizziness, somnolence/drowsiness, nystagmus, ataxia, neuralgia, headache, tics, bradycardia, syncope/circulatory disorder, respiratory insufficiency/hypoventilation, nausea, vomiting, constipation, hepatitis/liver dysfunction, SJS/TEN, hypersensitivity rash, angioedema, exfoliative dermatitis, myalgia/arthralgia, rickets/osteomalacia, restlessness/confusion/paradoxical excitation, hyperexcitability/irritability in children, tolerance, reduced blood pressure, and pyrexia.

## HIGH methylphenobarbital / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The vague 'FDA/DailyMed labeling' source is not adequate, and DailyMed is impermissible for boxed-warning verification. Add specific trusted sources that support aliases, U.S. availability, enzyme induction, and FDA-search context.
- Sources: https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm; https://pubchem.ncbi.nlm.nih.gov/compound/Mephobarbital; https://www.ncbi.nlm.nih.gov/books/NBK548260/
- Current: HALMED Phemiton 200 mg SmPC (https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf); EMA methylphenobarbital nationally authorised products PSUSA/00002025/202303 (https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf); FDA/DailyMed labeling
- Proposed: HALMED Phemiton 200 mg SmPC (https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf); EMA methylphenobarbital nationally authorised products PSUSA/00002025/202303 (https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf); PubChem Mephobarbital CID 8271 (https://pubchem.ncbi.nlm.nih.gov/compound/Mephobarbital); NCBI LiverTox Barbiturates (https://www.ncbi.nlm.nih.gov/books/NBK548260/); FDA Label Search and Drugs@FDA searches (https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm)

## HIGH methylphenobarbital / fact_check
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not appear in this field. FDA Label Search warns submitted labels may be unapproved/not FDA-verified, and Drugs@FDA is the FDA-approved-drug source. FDA web searches did not identify a current FDA-approved mephobarbital label.
- Sources: https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm
- Current: No current FDA/DailyMed label identified.
- Proposed: No FDA-approved label or FDA boxed warning identified; DailyMed should not be used for boxed-warning verification.

## HIGH methylphenobarbital / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is impermissible for boxed-warning verification; source wording should be FDA-only and should not imply a DailyMed-based conclusion.
- Sources: https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [methylphenobarbital; mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal].
- Proposed: FDA-only search on 05-20-2026/05-21-2026: FDA Label Search and Drugs@FDA searches did not identify a current FDA-approved mephobarbital/methylphenobarbital label or boxed warning; searched terms [methylphenobarbital; mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal].

## HIGH methylphenobarbital / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Current aliases are valid, but PubChem supports additional important synonyms/trade-name-like aliases, and Mephyltaletten is already in trade_names but absent from PubMed search aliases.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephobarbital; https://www.ncbi.nlm.nih.gov/books/NBK591157/bin/niceng217er6-appb-et1.pdf
- Current: mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Phemiton; Prominal
- Proposed: mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Metylfenemal; N-methylphenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal; Prominaletten; Phemetone; Isonal

## HIGH methylphenobarbital / fact_check
- Field: year_fda_cleared
- Status: incorrect
- Approval required: False
- Summary: 'FDA-cleared' is device terminology and should be avoided for this drug row. The Croatia authorization dates are supported by HALMED; EMA supports nationally authorised methylphenobarbital products; NCBI supports U.S. non-availability.
- Sources: https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm; https://www.ncbi.nlm.nih.gov/books/NBK548260/; https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf; https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf
- Current: Not FDA-cleared/currently available in U.S.; Croatia Phemiton first authorization 06 Apr 1994 and renewal 30 Mar 2020 per HALMED; EMA PSUSA lists Croatia and Slovenia nationally authorized products.
- Proposed: No FDA-approved methylphenobarbital/mephobarbital drug product identified; mephobarbital is no longer available in the United States. Croatia Phemiton first authorization 06 Apr 1994 and renewal 30 Mar 2020 per HALMED; EMA PSUSA lists methylphenobarbital nationally authorised products.

## HIGH methylphenobarbital / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The row's source text cites FDA/DailyMed, but DailyMed is not permissible for this field. FDA Label Search also warns that submitted labels may be unapproved and not FDA-verified, while Drugs@FDA is the FDA-approved-drug database. I did not identify a Drugs@FDA approved mephobarbital/methylphenobarbital product record in FDA web searches.
- Sources: https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm
- Current: No current FDA/DailyMed label identified.
- Proposed: No FDA-approved label or FDA boxed warning identified; DailyMed should not be used for boxed-warning verification.

## MEDIUM methylphenobarbital / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Adds source coverage for aliases and U.S. availability, and replaces vague FDA/DailyMed wording with FDA-only sources for boxed-warning context.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephobarbital; https://www.ncbi.nlm.nih.gov/books/NBK548260/; https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm
- Current: HALMED Phemiton 200 mg SmPC (https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf); EMA methylphenobarbital nationally authorised products PSUSA/00002025/202303 (https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf); FDA/DailyMed labeling
- Proposed: HALMED Phemiton 200 mg SmPC (https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf); EMA methylphenobarbital nationally authorised products PSUSA/00002025/202303 (https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf); PubChem Mephobarbital CID 8271 (https://pubchem.ncbi.nlm.nih.gov/compound/Mephobarbital); NCBI LiverTox Barbiturates (https://www.ncbi.nlm.nih.gov/books/NBK548260/); FDA Label Search and Drugs@FDA searches (https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm)

## MEDIUM methylphenobarbital / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not an acceptable boxed-warning source under the audit policy.
- Sources: https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [methylphenobarbital; mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal].
- Proposed: FDA-only search on 05-20-2026/05-21-2026: FDA Label Search and Drugs@FDA searches did not identify a current FDA-approved mephobarbital/methylphenobarbital label or boxed warning; searched terms [methylphenobarbital; mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal].

## MEDIUM methylphenobarbital / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Corrects the misleading 'unknown frequency 0%' wording and aligns the adverse-event list to the SmPC table.
- Sources: https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf
- Current: HALMED SmPC frequency categories: very rare events <0.01% include megaloblastic anemia; unknown frequency 0% exact percentage unavailable for CNS depression, mood changes/depression, dependence, nervousness, dizziness, somnolence, nystagmus, ataxia, headache, nausea, vomiting, constipation, bradycardia, respiratory insufficiency, SJS/TEN, rash, angioedema, osteomalacia/rickets.
- Proposed: HALMED SmPC frequency categories: very rare (<0.01%) includes megaloblastic anemia; frequency unknown (cannot be estimated from available data; exact percentages unavailable) includes folate deficiency, CNS depression, mood changes/depression, psychological and physical dependence, nervousness, dizziness, somnolence/drowsiness, nystagmus, ataxia, neuralgia, headache, tics, bradycardia, syncope/circulatory disorder, respiratory insufficiency/hypoventilation, nausea, vomiting, constipation, hepatitis/liver dysfunction, SJS/TEN, hypersensitivity rash, angioedema, exfoliative dermatitis, myalgia/arthralgia, rickets/osteomalacia, restlessness/confusion/paradoxical excitation, hyperexcitability/irritability in children, tolerance, reduced blood pressure, and pyrexia.

## MEDIUM methylphenobarbital / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: The mechanism source is HALMED's Croatian national SmPC, not an EMA or UK SmPC.
- Sources: https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf
- Current: EMA/UK SmPC
- Proposed: National SmPC (HALMED/Croatia)

## MEDIUM methylphenobarbital / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Prominaletten is explicitly listed by PubChem for the same compound.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephobarbital
- Current: Mebaral; Mephyltaletten; Phemiton; Prominal
- Proposed: Mebaral; Mephyltaletten; Phemiton; Prominal; Prominaletten

## MEDIUM methylphenobarbital / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Adds supported aliases and includes Mephyltaletten, which is already listed as a trade name.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Mephobarbital; https://www.ncbi.nlm.nih.gov/books/NBK591157/bin/niceng217er6-appb-et1.pdf
- Current: mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Phemiton; Prominal
- Proposed: mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Metylfenemal; N-methylphenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal; Prominaletten; Phemetone; Isonal

## MEDIUM methylphenobarbital / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification, and FDA approved-label sources did not identify an approved product label.
- Sources: https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm
- Current: No current FDA/DailyMed label identified.
- Proposed: No FDA-approved label or FDA boxed warning identified; DailyMed should not be used for boxed-warning verification.

## MEDIUM methylphenobarbital / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Removes impermissible DailyMed reliance for the boxed-warning field.
- Sources: https://labels.fda.gov/; https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [methylphenobarbital; mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal].
- Proposed: FDA-only search on 05-20-2026/05-21-2026: FDA Label Search and Drugs@FDA searches did not identify a current FDA-approved mephobarbital/methylphenobarbital label or boxed warning; searched terms [methylphenobarbital; mephobarbital; mephobarbitone; methylphenobarbitone; metilfenobarbital; Mebaral; Mephyltaletten; Phemiton; Prominal].

## MEDIUM methylphenobarbital / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: Avoids drug-inappropriate 'FDA-cleared' wording and cites U.S. non-availability plus European authorization support.
- Sources: https://www.accessdata.fda.gov/scripts/cder/daf/index.cfm; https://www.ncbi.nlm.nih.gov/books/NBK548260/; https://halmed.hr/upl/lijekovi/SPC/Phemiton-200-mg-tablete-SPC.pdf; https://www.ema.europa.eu/en/documents/psusa/methylphenobarbital-list-nationally-authorised-medicinal-products-psusa-00002025-202303_en.pdf
- Current: Not FDA-cleared/currently available in U.S.; Croatia Phemiton first authorization 06 Apr 1994 and renewal 30 Mar 2020 per HALMED; EMA PSUSA lists Croatia and Slovenia nationally authorized products.
- Proposed: No FDA-approved methylphenobarbital/mephobarbital drug product identified; mephobarbital is no longer available in the United States. Croatia Phemiton first authorization 06 Apr 1994 and renewal 30 Mar 2020 per HALMED; EMA PSUSA lists methylphenobarbital nationally authorised products.

## MEDIUM midazolam / fact_check
- Field: trade_names
- Status: missing_source
- Approval required: False
- Summary: Nayzilam and Seizalam are verified from FDA sources. Versed is plausible as a historical midazolam trade name, but this row bundle does not provide a trusted source directly supporting it.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=508215
- Current: Nayzilam; Seizalam; Versed
- Proposed: Nayzilam; Seizalam; Versed

## HIGH midazolam / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: The phase III RCT and ClinicalTrials.gov records use USL261 for the intranasal midazolam product; adding it improves search recall without creating a duplicate drug row.
- Sources: https://pubmed.ncbi.nlm.nih.gov/31140596/; https://clinicaltrials.gov/study/NCT01390220
- Current: Nayzilam; midazolam nasal spray
- Proposed: Nayzilam; midazolam nasal spray; USL261

## HIGH midazolam / fact_check
- Field: year_fda_cleared
- Status: incorrect
- Approval required: False
- Summary: The current value is directionally correct but omits the FDA-approved SEIZALAM status-epilepticus product approved in 2018.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=508215; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf
- Current: 1985 injection; 2019 nasal seizure-cluster product
- Proposed: 1985 initial U.S. approval for midazolam injection/sedation; 2018 SEIZALAM IM injection for status epilepticus; 2019 NAYZILAM nasal spray for seizure clusters

## MEDIUM midazolam / fact_check
- Field: formulations_available
- Status: missing_source
- Approval required: False
- Summary: Nasal spray and IM/IV injection are supported by FDA labels; buccal/oromucosal midazolam is supported by EMA/eMC sources. Oral syrup is plausible but needs a trusted row source if retained.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf; https://www.ema.europa.eu/en/medicines/human/EPAR/buccolam; https://www.medicines.org.uk/emc/search?q=buccolam
- Current: Nasal spray; buccal/oromucosal solution in some markets; IV/IM injection; oral syrup for sedation
- Proposed: Nasal spray; buccal/oromucosal solution in some non-US markets; IV/IM injection; oral syrup for procedural sedation

## HIGH midazolam / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: FDA labels give product-specific approved dosing; the current wording is too vague for U.S. products.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.ema.europa.eu/en/medicines/human/EPAR/buccolam
- Current: Rescue dosing individualized by product/age/weight
- Proposed: NAYZILAM: 5 mg intranasal initial dose for patients 12 years and older; SEIZALAM: 10 mg IM for adults with status epilepticus; non-US buccal/oromucosal dosing varies by age/weight and product

## HIGH midazolam / fact_check
- Field: maximum_approved_daily_dose
- Status: incorrect
- Approval required: False
- Summary: The NAYZILAM label provides explicit maximum treatment frequency, and SEIZALAM provides a 10 mg IM recommended adult dose.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf
- Current: Rescue dosing individualized by product/age/weight
- Proposed: NAYZILAM: do not use more than 2 doses to treat a single seizure-cluster episode; recommended no more than 1 episode every 3 days and no more than 5 episodes per month. SEIZALAM: recommended dose 10 mg IM once for adults with status epilepticus.

## HIGH midazolam / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: False
- Summary: Checked FDA labels support 1.8-6.4 h for IV studies and 2.1-6.2 h for NAYZILAM; the row's 1.5 h lower bound was not verified.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf
- Current: 1.5-6 h
- Proposed: 1.8-6.4 h in healthy adult IV studies; 2.1-6.2 h following NAYZILAM in clinical trials

## MEDIUM midazolam / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: missing_source
- Approval required: False
- Summary: FDA labels support CYP3A4 metabolism and clinically relevant CYP3A inhibitor/inducer effects. The exact negative claim 'not an inducer/inhibitor' is not directly stated in the checked label text, so the proposed wording is more source-concordant.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf
- Current: Not an inducer/inhibitor; CYP3A substrate
- Proposed: CYP3A4 substrate; exposure is increased by CYP3A4 inhibitors and decreased by CYP3A4 inducers; not classified as an enzyme-inducing antiseizure medication

## CRITICAL midazolam / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: The row's 'Inhibitor' filter describes CYP3A inhibitors that affect midazolam, not midazolam itself. FDA labeling supports midazolam as a CYP3A4 substrate affected by inhibitors/inducers.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf
- Current: Inhibitor; Substrate / affected by modulators
- Proposed: Substrate / affected by modulators

## HIGH midazolam / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The checked FDA labels directly support mechanism. DailyMed is not in the trusted source list for this audit, and AES was not needed to support the mechanism cell.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf
- Current: American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling
- Proposed: FDA NAYZILAM label; FDA SEIZALAM label; FDA midazolam injection label

## HIGH midazolam / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: FDA labeling directly supports the mechanism field and is the trusted source tier actually used here.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf
- Current: AES/FDA summary
- Proposed: FDA label

## CRITICAL midazolam / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: Nasal discomfort is an application-site adverse reaction, not a respiratory category. The checked FDA labels did not verify 'respiratory depression 2%' or 'nausea 2%' as written; FDA labeling supports different adverse-event terms and percentages.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf
- Current: CNS: somnolence/sedation 10%, respiratory: nasal discomfort 16% for nasal product, throat irritation 3%, respiratory depression 2%, GI: nausea 2%
- Proposed: Clinical-trial adverse reactions (selected): NAYZILAM comparative phase: somnolence 10%, nasal discomfort 9% overall (16% in 5 mg + 5 mg subgroup), throat irritation 3%, rhinorrhea 3%; SEIZALAM status-epilepticus trial: upper airway obstruction 5%, agitation 4%, pyrexia 4%, mental status changes 3%, postictal state 3%, acute renal failure 2%; IV midazolam single-agent sedation: nausea 2.8%; pediatric IV literature: apnea 2.8%.

## HIGH midazolam / fact_check
- Field: filter_symptom_category
- Status: missing
- Approval required: False
- Summary: NAYZILAM adverse reactions include somnolence/CNS and nasal discomfort/throat irritation/rhinorrhea; the nasal discomfort item is best captured as application site/local as well as not purely respiratory.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf
- Current: CNS; GI; Respiratory
- Proposed: CNS; GI; Respiratory; Application site

## MEDIUM midazolam / fact_check
- Field: qt_interval_effect
- Status: missing_source
- Approval required: False
- Summary: This is plausible, but the row bundle does not cite a trusted source that directly evaluates QT effect. FDA labels checked for other facts do not establish a clinically meaningful QT signal.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: No clinically meaningful QT effect established

## MEDIUM midazolam / fact_check
- Field: filter_qt_effect
- Status: missing_source
- Approval required: False
- Summary: Same source limitation as qt_interval_effect; no direct trusted QT-specific source was supplied in the row.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf
- Current: No known meaningful QT effect
- Proposed: No known meaningful QT effect

## HIGH midazolam / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Wikipedia, Epilepsy Foundation Australia, AES, and DailyMed are not in the provided trusted-source domain list for this audit. The proposed sources directly support the row's regulatory, formulation, indication, mechanism, and RCT facts.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=508215; https://pubmed.ncbi.nlm.nih.gov/33140403/; https://pubmed.ncbi.nlm.nih.gov/31140596/
- Current: Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling
- Proposed: FDA/openFDA and FDA AccessData labels for NAYZILAM, SEIZALAM, and midazolam injection; FDA Orphan Drug Designations and Approvals for SEIZALAM; EMA/eMC SmPC for buccal/oromucosal midazolam; PubMed RCT records; ClinicalTrials.gov records

## HIGH midazolam / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is explicitly not permissible for the FDA black-box warning field; openFDA and FDA AccessData are permissible FDA sources.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=2b29422e-54d5-4a49-8522-e9cf752368c3; published=Jan 31, 2023; title=NAYZILAM (MIDAZOLAM) SPRAY [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b29422e-54d5-4a49-8522-e9cf752368c3
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2b29422e-54d5-4a49-8522-e9cf752368c3; effective_time=20230119; title=NAYZILAM (MIDAZOLAM) nasal spray; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; fda_label_pdf=https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf

## HIGH midazolam / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: The numeric differentials are supported, but Detyniecki2019 reports treatment success, not a pure seizure-freedom endpoint. The wording should distinguish the endpoints.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33140403/; https://pubmed.ncbi.nlm.nih.gov/31140596/
- Current: 16.1-19.3 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Spencer2020 midazolam nasal spray 5 mg 16.1%; Detyniecki2019 midazolam nasal spray 5 mg 19.3%)
- Proposed: 16.1-19.3% drug-minus-placebo acute seizure-control differential at 5 mg intranasal midazolam: Spencer2020 6-hour seizure freedom 54.8% vs 38.7%, difference 16.1%; Detyniecki2019 treatment success/no recurrence through 6 hours 53.7% vs 34.4%, difference 19.3%.

## INFO midazolam / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Blank is appropriate because no RR50 differential was extractable from the retained acute rescue RCTs.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33140403/; https://pubmed.ncbi.nlm.nih.gov/31140596/

## INFO midazolam / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Blank is appropriate because no median percent change differential was extractable from the retained acute rescue RCTs.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33140403/; https://pubmed.ncbi.nlm.nih.gov/31140596/

## MEDIUM midazolam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box warning verification must use FDA/openFDA, FDA labels, or Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=2b29422e-54d5-4a49-8522-e9cf752368c3; published=Jan 31, 2023; title=NAYZILAM (MIDAZOLAM) SPRAY [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b29422e-54d5-4a49-8522-e9cf752368c3
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2b29422e-54d5-4a49-8522-e9cf752368c3; effective_time=20230119; title=NAYZILAM (MIDAZOLAM) nasal spray; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; fda_label_pdf=https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf

## MEDIUM midazolam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current source list includes non-trusted or non-specific sources; proposed list maps to the facts being retained.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=508215; https://pubmed.ncbi.nlm.nih.gov/33140403/; https://pubmed.ncbi.nlm.nih.gov/31140596/
- Current: Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling
- Proposed: FDA/openFDA and FDA AccessData labels for NAYZILAM, SEIZALAM, and midazolam injection; FDA Orphan Drug Designations and Approvals for SEIZALAM; EMA/eMC SmPC for buccal/oromucosal midazolam; PubMed RCT records; ClinicalTrials.gov records

## MEDIUM midazolam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA labels directly support mechanism and are trusted sources for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf
- Current: American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling
- Proposed: FDA NAYZILAM label; FDA SEIZALAM label; FDA midazolam injection label

## MEDIUM midazolam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace prohibited DailyMed source with FDA/openFDA/FDA label source.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=2b29422e-54d5-4a49-8522-e9cf752368c3; published=Jan 31, 2023; title=NAYZILAM (MIDAZOLAM) SPRAY [UCB, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=2b29422e-54d5-4a49-8522-e9cf752368c3
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=2b29422e-54d5-4a49-8522-e9cf752368c3; effective_time=20230119; title=NAYZILAM (MIDAZOLAM) nasal spray; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; fda_label_pdf=https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf

## MEDIUM midazolam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use trusted source domains that support the specific retained cell facts.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%222b29422e-54d5-4a49-8522-e9cf752368c3%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.ema.europa.eu/en/medicines/human/EPAR/buccolam; https://pubmed.ncbi.nlm.nih.gov/33140403/; https://pubmed.ncbi.nlm.nih.gov/31140596/
- Current: Epilepsy Foundation Australia ASM list; Wikipedia anticonvulsant drug-class list; American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling
- Proposed: FDA/openFDA and FDA AccessData labels for NAYZILAM, SEIZALAM, and midazolam injection; FDA Orphan Drug Designations and Approvals for SEIZALAM; EMA/eMC SmPC for buccal/oromucosal midazolam; PubMed RCT records; ClinicalTrials.gov records

## MEDIUM midazolam / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA labeling directly supports mechanism and avoids non-trusted/unneeded source names.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf
- Current: American Epilepsy Society 2024 U.S. ASM summary; FDA/DailyMed labeling
- Proposed: FDA NAYZILAM label; FDA SEIZALAM label; FDA midazolam injection label

## MEDIUM midazolam / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: FDA labeling is the source tier actually supporting the mechanism fact.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf
- Current: AES/FDA summary
- Proposed: FDA label

## MEDIUM midazolam / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: USL261 is used in the placebo-controlled phase III trial records and should be searchable as an alias/code.
- Sources: https://pubmed.ncbi.nlm.nih.gov/31140596/; https://clinicaltrials.gov/study/NCT01390220
- Current: Nayzilam; midazolam nasal spray
- Proposed: Nayzilam; midazolam nasal spray; USL261

## MEDIUM midazolam / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: Adds FDA-approved SEIZALAM status-epilepticus product year omitted by the row.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=508215; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf
- Current: 1985 injection; 2019 nasal seizure-cluster product
- Proposed: 1985 initial U.S. approval for midazolam injection/sedation; 2018 SEIZALAM IM injection for status epilepticus; 2019 NAYZILAM nasal spray for seizure clusters

## CRITICAL midazolam / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: Midazolam is affected by CYP3A inhibitors/inducers; it is not itself supported as an inhibitor in the checked sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf
- Current: Inhibitor; Substrate / affected by modulators
- Proposed: Substrate / affected by modulators

## MEDIUM midazolam / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: FDA labels support these exact ranges, not the row's 1.5 h lower bound.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf
- Current: 1.5-6 h
- Proposed: 1.8-6.4 h in healthy adult IV studies; 2.1-6.2 h following NAYZILAM in clinical trials

## CRITICAL midazolam / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Corrects unsupported percentages and categorization from FDA labels.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/211321s008lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209566s003lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215868s000lbl.pdf
- Current: CNS: somnolence/sedation 10%, respiratory: nasal discomfort 16% for nasal product, throat irritation 3%, respiratory depression 2%, GI: nausea 2%
- Proposed: Clinical-trial adverse reactions (selected): NAYZILAM comparative phase: somnolence 10%, nasal discomfort 9% overall (16% in 5 mg + 5 mg subgroup), throat irritation 3%, rhinorrhea 3%; SEIZALAM status-epilepticus trial: upper airway obstruction 5%, agitation 4%, pyrexia 4%, mental status changes 3%, postictal state 3%, acute renal failure 2%; IV midazolam single-agent sedation: nausea 2.8%; pediatric IV literature: apnea 2.8%.

## MEDIUM midazolam / proposed_row_update
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Preserves verified numbers while correcting endpoint wording for Detyniecki2019.
- Sources: https://pubmed.ncbi.nlm.nih.gov/33140403/; https://pubmed.ncbi.nlm.nih.gov/31140596/
- Current: 16.1-19.3 % (drug minus placebo seizure-freedom differential at maximum effective dose/regimen: Spencer2020 midazolam nasal spray 5 mg 16.1%; Detyniecki2019 midazolam nasal spray 5 mg 19.3%)
- Proposed: 16.1-19.3% drug-minus-placebo acute seizure-control differential at 5 mg intranasal midazolam: Spencer2020 6-hour seizure freedom 54.8% vs 38.7%, difference 16.1%; Detyniecki2019 treatment success/no recurrence through 6 hours 53.7% vs 34.4%, difference 19.3%.

## HIGH oxcarbazepine / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Barcs2000 explicitly reports 600 mg/day as the minimum effective dosage in adjunctive therapy; FDA labeling supports 1200 mg/day as a common recommended/effective adult dose.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11114219/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf
- Current: 1200 mg/day common adult maintenance target
- Proposed: 600 mg/day adjunctive minimum effective dosage in Barcs2000; 1200 mg/day common adult target/maintenance dose in FDA labeling

## CRITICAL oxcarbazepine / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: Current values understate several FDA-label active-dose adverse-reaction ranges, especially somnolence, nausea, vomiting, and diplopia. Oxtellar XR and Trileptal labels support the proposed active-dose ranges.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/202810s010lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf
- Current: CNS: dizziness 22-49%, CNS: somnolence 19-28%, GI: nausea 15%, GI: vomiting 13%, neurologic: diplopia 14%, metabolic: hyponatremia 2-3%
- Proposed: CNS: dizziness 20-49%, CNS: somnolence 12-36%, GI: nausea 15-29%, GI: vomiting 6-36%, neurologic/eye: diplopia 10-40%, metabolic: hyponatremia 1-5% (clinically significant sodium <125 mmol/L 2.5% in controlled epilepsy studies)

## CRITICAL oxcarbazepine / fact_check
- Field: filter_mechanism
- Status: incorrect
- Approval required: True
- Summary: FDA labeling supports voltage-sensitive sodium-channel blockade as the primary described mechanism and possible high-voltage calcium-channel modulation; it does not support alpha-2-delta binding.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK482313/
- Current: Calcium channel / alpha-2-delta; Potassium channel
- Proposed: Sodium channel; Potassium channel; Calcium channel

## CRITICAL oxcarbazepine / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: True
- Summary: FDA labeling states oxcarbazepine is extensively metabolized and then predominantly excreted by the kidneys; the phrase "Renal/no major metabolism" is misleading for oxcarbazepine.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK482313/
- Current: Liver/hepatic; Renal/no major metabolism
- Proposed: Liver/hepatic; Renal excretion

## MEDIUM oxcarbazepine / fact_check
- Field: qt_interval_effect; filter_qt_effect
- Status: missing_source
- Approval required: False
- Summary: Reviewed FDA labeling does not establish a therapeutic clinically meaningful QT effect, but Oxtellar XR labeling lists QT prolongation among isolated overdose events, so the current wording needs a source-qualified caveat.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/202810s010lbl.pdf
- Current: No clinically meaningful QT effect established; filter_qt_effect=No known meaningful QT effect
- Proposed: No dedicated therapeutic QT-effect statement found in reviewed FDA labeling; QT prolongation is listed among overdose events.

## HIGH oxcarbazepine / fact_check
- Field: alternate_generic_names; pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: No separate alternate generic name is needed, but PubMed/trial search aliases should include OXC/OXC XR and development codes SPN-804 and TRI476 to prevent missed oxcarbazepine trial records.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24359313/; https://clinicaltrials.gov/study/NCT00772603; https://clinicaltrials.gov/study/NCT00975715
- Current: alternate_generic_names=; pubmed_search_aliases=
- Proposed: alternate_generic_names: ""; pubmed_search_aliases: "OXC; OXC XR; SPN-804; TRI476"

## HIGH oxcarbazepine / fact_check
- Field: evidence_sources; mechanism_source
- Status: incorrect
- Approval required: False
- Summary: Epilepsy Society and Epilepsy Foundation Australia are not in the requested trusted-source domain list, and DailyMed is not acceptable for the black-box source. Row facts are better supported by FDA/accessdata/openFDA, NCBI, PubMed, and ClinicalTrials.gov.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK548414/; https://www.ncbi.nlm.nih.gov/books/NBK482313/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling; FDA/openFDA labeling; NCBI LiverTox; NCBI StatPearls; PubMed RCT abstracts; ClinicalTrials.gov

## HIGH oxcarbazepine / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: PubMed lists this as a comment/letter on the Schachter monotherapy trial with no abstract, not an independent phase II/III placebo-controlled RCT report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10599816/
- Current: https://pubmed.ncbi.nlm.nih.gov/10599816/
- Proposed: Remove from pubmed_phase_ii_iii_rct_links or move to notes; requires user approval because it removes an existing link.

## HIGH oxcarbazepine / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: PubMed lists this as a comment/letter on the Schachter monotherapy trial with no abstract, not an independent phase II/III placebo-controlled RCT report.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10599817/
- Current: https://pubmed.ncbi.nlm.nih.gov/10599817/
- Proposed: Remove from pubmed_phase_ii_iii_rct_links or move to notes; requires user approval because it removes an existing link.

## HIGH oxcarbazepine / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed abstract reports a multicenter randomized placebo-controlled pediatric adjunctive oxcarbazepine trial with extractable median percent reduction (35% vs 9%) and RR50 (41% vs 22%).
- Sources: https://pubmed.ncbi.nlm.nih.gov/10881246/
- Proposed: Glauser2000|https://pubmed.ncbi.nlm.nih.gov/10881246/

## HIGH oxcarbazepine / outcome_check
- Field: diff_50_responder_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: French and Barcs calculations are correct. Glauser2000 is a missing placebo-controlled RCT and adds an in-range RR50 differential of 19%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24359313/; https://pubmed.ncbi.nlm.nih.gov/11114219/; https://pubmed.ncbi.nlm.nih.gov/10881246/
- Current: 12.6-37 % (drug minus placebo RR50 differential at maximum effective dose/regimen: French2013 extended-release oxcarbazepine 2400 mg/day 12.6%; Barcs2000 oxcarbazepine 2400 mg/day 37%)
- Proposed: 12.6-37 % (drug minus placebo RR50 differential at maximum effective dose/regimen: French2013 extended-release oxcarbazepine 2400 mg/day 12.6%; Barcs2000 oxcarbazepine 2400 mg/day 37%; Glauser2000 oxcarbazepine 30-46 mg/kg/day 19%)

## HIGH oxcarbazepine / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: French and Barcs calculations are correct. Glauser2000 adds an in-range median-percent-change differential of 26%.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24359313/; https://pubmed.ncbi.nlm.nih.gov/11114219/; https://pubmed.ncbi.nlm.nih.gov/10881246/
- Current: 14.2-42 % (drug minus placebo MPC differential at maximum effective dose/regimen: French2013 extended-release oxcarbazepine 2400 mg/day 14.2%; Barcs2000 oxcarbazepine 2400 mg/day 42%)
- Proposed: 14.2-42 % (drug minus placebo MPC differential at maximum effective dose/regimen: French2013 extended-release oxcarbazepine 2400 mg/day 14.2%; Barcs2000 oxcarbazepine 2400 mg/day 42%; Glauser2000 oxcarbazepine 30-46 mg/kg/day 26%)

## HIGH oxcarbazepine / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Existing plot values match cited abstracts; add Glauser2000 because it is a qualifying placebo-controlled RCT with extractable RR50 differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24359313/; https://pubmed.ncbi.nlm.nih.gov/11114219/; https://pubmed.ncbi.nlm.nih.gov/10881246/
- Current: French2013|12.6|https://pubmed.ncbi.nlm.nih.gov/24359313/|366; Barcs2000|37|https://pubmed.ncbi.nlm.nih.gov/11114219/|694
- Proposed: French2013|12.6|https://pubmed.ncbi.nlm.nih.gov/24359313/|366; Barcs2000|37|https://pubmed.ncbi.nlm.nih.gov/11114219/|694; Glauser2000|19|https://pubmed.ncbi.nlm.nih.gov/10881246/|267

## HIGH oxcarbazepine / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Existing plot values match cited abstracts; add Glauser2000 because it is a qualifying placebo-controlled RCT with extractable median-percent-change differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24359313/; https://pubmed.ncbi.nlm.nih.gov/11114219/; https://pubmed.ncbi.nlm.nih.gov/10881246/
- Current: French2013|14.2|https://pubmed.ncbi.nlm.nih.gov/24359313/|366; Barcs2000|42|https://pubmed.ncbi.nlm.nih.gov/11114219/|694
- Proposed: French2013|14.2|https://pubmed.ncbi.nlm.nih.gov/24359313/|366; Barcs2000|42|https://pubmed.ncbi.nlm.nih.gov/11114219/|694; Glauser2000|26|https://pubmed.ncbi.nlm.nih.gov/10881246/|267

## HIGH oxcarbazepine / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supportable from FDA labeling/openFDA, but the current value and source rely on DailyMed, which is not permissible for this field.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2018/202810s010lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM oxcarbazepine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box-warning verification must use FDA/openFDA, FDA labels, or Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=aa610e56-1d1d-11e1-8bc2-0800200c9a66; published=Nov 17, 2025; title=OXTELLAR XR (OXCARBAZEPINE) TABLET [SUPERNUS PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aa610e56-1d1d-11e1-8bc2-0800200c9a66
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=aa610e56-1d1d-11e1-8bc2-0800200c9a66; effective_time=20251022; title=OXTELLAR XR / OXCARBAZEPINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5

## MEDIUM oxcarbazepine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current row source list includes non-trusted domains and does not name PubMed/ClinicalTrials.gov sources supporting RCT/outcome cells.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548414/; https://www.ncbi.nlm.nih.gov/books/NBK482313/; https://pubmed.ncbi.nlm.nih.gov/24359313/; https://clinicaltrials.gov/study/NCT00772603
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling; FDA/openFDA labeling; NCBI LiverTox; NCBI StatPearls; PubMed RCT abstracts; ClinicalTrials.gov

## MEDIUM oxcarbazepine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism wording is supported by FDA labeling; use an allowed FDA source URL rather than DailyMed wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM oxcarbazepine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification; use FDA/openFDA metadata instead.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=aa610e56-1d1d-11e1-8bc2-0800200c9a66; published=Nov 17, 2025; title=OXTELLAR XR (OXCARBAZEPINE) TABLET [SUPERNUS PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=aa610e56-1d1d-11e1-8bc2-0800200c9a66
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=aa610e56-1d1d-11e1-8bc2-0800200c9a66; effective_time=20251022; title=OXTELLAR XR / OXCARBAZEPINE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5

## MEDIUM oxcarbazepine / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Substantive no-boxed-warning conclusion is supportable, but the source wording must be FDA/openFDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22aa610e56-1d1d-11e1-8bc2-0800200c9a66%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM oxcarbazepine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace non-trusted and DailyMed source wording with the trusted sources actually used for row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548414/; https://www.ncbi.nlm.nih.gov/books/NBK482313/; https://pubmed.ncbi.nlm.nih.gov/24359313/; https://clinicaltrials.gov/study/NCT00772603
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling; FDA/openFDA labeling; NCBI LiverTox; NCBI StatPearls; PubMed RCT abstracts; ClinicalTrials.gov

## MEDIUM oxcarbazepine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The mechanism facts are supported by FDA labeling; avoid DailyMed wording under the trusted-source policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM oxcarbazepine / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Adds trial and PubMed aliases without treating them as alternate generic names.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24359313/; https://clinicaltrials.gov/study/NCT00772603; https://clinicaltrials.gov/study/NCT00975715
- Proposed: OXC; OXC XR; SPN-804; TRI476

## CRITICAL oxcarbazepine / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: Adds a missed randomized placebo-controlled pediatric adjunctive RCT and removes two comment/letter records that are not independent primary trial reports.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24359313/; https://pubmed.ncbi.nlm.nih.gov/11114219/; https://pubmed.ncbi.nlm.nih.gov/10078718/; https://pubmed.ncbi.nlm.nih.gov/10881246/
- Current: French2013|https://pubmed.ncbi.nlm.nih.gov/24359313/; Barcs2000|https://pubmed.ncbi.nlm.nih.gov/11114219/; Schachter1999b|https://pubmed.ncbi.nlm.nih.gov/10599816/; Schachter1999|https://pubmed.ncbi.nlm.nih.gov/10078718/; Cramer1999|https://pubmed.ncbi.nlm.nih.gov/10599817/
- Proposed: French2013|https://pubmed.ncbi.nlm.nih.gov/24359313/; Barcs2000|https://pubmed.ncbi.nlm.nih.gov/11114219/; Schachter1999|https://pubmed.ncbi.nlm.nih.gov/10078718/; Glauser2000|https://pubmed.ncbi.nlm.nih.gov/10881246/

## CRITICAL oxcarbazepine / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: True
- Summary: Updates RCT verification notes to match PubMed evidence.
- Sources: https://pubmed.ncbi.nlm.nih.gov/10078718/; https://pubmed.ncbi.nlm.nih.gov/10881246/
- Current: PubMed loop 37/65 on 2026-05-15: 5 qualifying placebo-controlled randomized clinical trial report(s) retained from 24 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit on 2026-05-20: French2013, Barcs2000, Schachter1999, and Glauser2000 are qualifying placebo-controlled randomized oxcarbazepine seizure trial reports. Schachter1999b (PMID 10599816) and Cramer1999 (PMID 10599817) are comment/letter records on the Schachter monotherapy trial and should not be counted as independent RCT reports. Differential effectiveness columns summarize extractable maximum effective dose/regimen values from French2013, Barcs2000, and Glauser2000; Schachter1999 reports exit/time-to-event outcomes but not extractable RR50, MPC, or seizure-freedom percentages.

## CRITICAL oxcarbazepine / proposed_row_update
- Field: filter_mechanism
- Status: proposed
- Approval required: True
- Summary: FDA labeling supports sodium-channel blockade and possible potassium/high-voltage calcium effects, not alpha-2-delta.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf
- Current: Calcium channel / alpha-2-delta; Potassium channel
- Proposed: Sodium channel; Potassium channel; Calcium channel

## CRITICAL oxcarbazepine / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: True
- Summary: Oxcarbazepine is extensively metabolized; renal excretion is of metabolites.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/021014s050lbl.pdf
- Current: Liver/hepatic; Renal/no major metabolism
- Proposed: Liver/hepatic; Renal excretion

## HIGH paramethadione / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: Important aliases are present in NCBI/PubChem synonym data and should be captured to avoid duplicate-row handling under alternate names.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Proposed: Parametadione; isoethadione

## HIGH paramethadione / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Paradione is correct but search aliases are incomplete because parametadione and isoethadione are documented synonyms.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: Paradione
- Proposed: Paradione; parametadione; isoethadione

## HIGH paramethadione / fact_check
- Field: epilepsy_type
- Status: incorrect
- Approval required: False
- Summary: NCBI/PubChem/HSDB describes paramethadione and trimethadione as indicated for absence/petit mal seizures refractory to other medications and notes older use for petit mal and atypical spike-and-wave absence attacks. Orange Book alone does not supply the indication.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://pubmed.ncbi.nlm.nih.gov/14394344/
- Current: Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)
- Proposed: Historical absence (petit mal) epilepsy / atypical spike-and-wave absence attacks; no current FDA label identified.

## HIGH paramethadione / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: False
- Summary: NCBI/PubChem reports a 12-24 hour half-life for paramethadione and notes the active-metabolite half-life is not known. The current N/A is too conservative if non-label NCBI evidence is allowed.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: 12 to 24 hours for parent paramethadione; active-metabolite half-life not known.

## HIGH paramethadione / fact_check
- Field: major_organ_for_metabolism
- Status: incorrect
- Approval required: False
- Summary: NCBI/PubChem and PubMed metabolism literature support hepatic N-demethylation. Orange Book alone does not provide this cell fact.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://pubmed.ncbi.nlm.nih.gov/13234040/
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Primarily hepatic; paramethadione is N-demethylated to 5-ethyl-5-methyl-2,4-oxazolidinedione, an active metabolite, with renal excretion described.

## HIGH paramethadione / fact_check
- Field: mechanism_of_action
- Status: incorrect
- Approval required: False
- Summary: FDA Orange Book is not a mechanism source. NCBI/PubChem provides a pharmacology summary supporting a limited T-type calcium-channel mechanism.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Limited historical evidence: dione anticonvulsants such as paramethadione reduce T-type calcium currents in thalamic neurons, inhibiting corticothalamic transmission and dampening absence-seizure spike-wave rhythmicity.

## HIGH paramethadione / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: Orange Book product files do not support mechanism-of-action statements.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: FDA Orange Book products file
- Proposed: NCBI PubChem pharmacology summary; historical biomedical literature

## HIGH paramethadione / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: No FDA-label percentage table was found, but DailyMed should not be used as the named source here and '0%' can be misread as zero adverse events.
- Sources: https://api.fda.gov/drug/label.json?limit=1; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A: no current FDA/openFDA label identified; available historical/secondary sources do not provide FDA-label adverse-event percentages for the current dataset scope.

## HIGH paramethadione / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Current row facts rely on more than Orange Book, and DailyMed is not an allowed FDA boxed-warning source. Add NCBI/PubMed for aliases, historical indication, formulation, metabolism, half-life, and mechanism.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://api.fda.gov/drug/label.json?limit=1; https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://pubmed.ncbi.nlm.nih.gov/14394344/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book/Drugs@FDA; FDA/openFDA label API; NCBI PubChem/HSDB; PubMed

## HIGH paramethadione / fact_check
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: FDA boxed-warning verification must use FDA/openFDA, FDA labels, or Drugs@FDA only; remove DailyMed wording.
- Sources: https://api.fda.gov/drug/label.json?limit=1; https://open.fda.gov/apis/drug/label/
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## HIGH paramethadione / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for this field under the audit policy.
- Sources: https://api.fda.gov/drug/label.json?limit=1; https://open.fda.gov/apis/drug/label/
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [paramethadione; Paradione].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [paramethadione; Paradione].

## HIGH paramethadione / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification. Use FDA/openFDA wording only. I did not identify a current FDA label record for paramethadione/Paradione in the available FDA/openFDA sources.
- Sources: https://api.fda.gov/drug/label.json?limit=1; https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM paramethadione / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: The current source list is incomplete and includes DailyMed wording where FDA/openFDA should be used for boxed-warning verification.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://api.fda.gov/drug/label.json?limit=1; https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://pubmed.ncbi.nlm.nih.gov/14394344/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book/Drugs@FDA; FDA/openFDA label API; NCBI PubChem/HSDB; PubMed

## MEDIUM paramethadione / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA Orange Book product files do not support mechanism-of-action content.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: FDA Orange Book products file
- Proposed: NCBI PubChem pharmacology summary; historical biomedical literature

## MEDIUM paramethadione / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for the boxed-warning source field.
- Sources: https://api.fda.gov/drug/label.json?limit=1; https://open.fda.gov/apis/drug/label/
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [paramethadione; Paradione].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [paramethadione; Paradione].

## MEDIUM paramethadione / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Documented aliases are missing.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Proposed: Parametadione; isoethadione

## MEDIUM paramethadione / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add documented aliases for search coverage and duplicate prevention.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: Paradione
- Proposed: Paradione; parametadione; isoethadione

## MEDIUM paramethadione / proposed_row_update
- Field: available_in_us
- Status: proposed
- Approval required: False
- Summary: FDA review material provides more precise discontinued/withdrawn status.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/204442Orig1s000NameR.pdf
- Current: No - discontinued FDA Orange Book product
- Proposed: No - Paradione discontinued; NDA 006800 withdrawn effective 06/04/2004.

## MEDIUM paramethadione / proposed_row_update
- Field: epilepsy_type
- Status: proposed
- Approval required: False
- Summary: NCBI/PubChem/HSDB and PubMed support historical use in absence/petit mal epilepsy.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://pubmed.ncbi.nlm.nih.gov/14394344/
- Current: Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)
- Proposed: Historical absence (petit mal) epilepsy / atypical spike-and-wave absence attacks; no current FDA label identified.

## MEDIUM paramethadione / proposed_row_update
- Field: filter_epilepsy_type
- Status: proposed
- Approval required: False
- Summary: Filter should match the supported historical seizure type.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: Historical/unspecified epilepsy
- Proposed: Absence/petit mal epilepsy (historical)

## MEDIUM paramethadione / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: False
- Summary: Adds historically documented strengths and clarifies current U.S. marketing status.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/204442Orig1s000NameR.pdf
- Current: Historical oral capsule; historical oral solution (not marketed in U.S.)
- Proposed: Historical oral capsules (150 mg and 300 mg) and oral solution (1.5 g/5 mL); not currently marketed in the U.S.

## MEDIUM paramethadione / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: NCBI/PubChem provides half-life information.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: 12 to 24 hours for parent paramethadione; active-metabolite half-life not known.

## MEDIUM paramethadione / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: False
- Summary: NCBI/PubChem and PubMed metabolism evidence support hepatic metabolism.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://pubmed.ncbi.nlm.nih.gov/13234040/
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Primarily hepatic; N-demethylated to 5-ethyl-5-methyl-2,4-oxazolidinedione, an active metabolite; renal excretion described.

## MEDIUM paramethadione / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: False
- Summary: Filter should reflect the supported hepatic metabolism evidence while retaining the limited-data qualifier.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: Limited/unknown
- Proposed: Hepatic metabolism; limited/legacy data

## MEDIUM paramethadione / proposed_row_update
- Field: mechanism_of_action
- Status: proposed
- Approval required: False
- Summary: Orange Book is not a mechanism source; NCBI/PubChem supports a limited T-type calcium-channel mechanism.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Limited historical evidence: dione anticonvulsants such as paramethadione reduce T-type calcium currents in thalamic neurons, inhibiting corticothalamic transmission and dampening absence-seizure spike-wave rhythmicity.

## MEDIUM paramethadione / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is not supported by Orange Book product files.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: FDA Orange Book products file
- Proposed: NCBI PubChem pharmacology summary; historical biomedical literature

## MEDIUM paramethadione / proposed_row_update
- Field: filter_mechanism
- Status: proposed
- Approval required: False
- Summary: Mechanism filter should reflect the supported limited/historical mechanism.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione
- Current: Other / unclear
- Proposed: T-type calcium channel inhibition (limited/historical)

## MEDIUM paramethadione / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current sources do not support all retained facts and DailyMed should not be named for boxed-warning verification.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.fda.gov/drugs/drug-approvals-and-databases/about-drugsfda; https://api.fda.gov/drug/label.json?limit=1; https://pubchem.ncbi.nlm.nih.gov/compound/Paramethadione; https://pubmed.ncbi.nlm.nih.gov/14394344/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book/Drugs@FDA; FDA/openFDA label API; NCBI PubChem/HSDB; PubMed

## MEDIUM paramethadione / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification.
- Sources: https://api.fda.gov/drug/label.json?limit=1; https://open.fda.gov/apis/drug/label/
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM paramethadione / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for this field.
- Sources: https://api.fda.gov/drug/label.json?limit=1; https://open.fda.gov/apis/drug/label/
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [paramethadione; Paradione].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [paramethadione; Paradione].

## MEDIUM paramethadione / proposed_row_update
- Field: status_or_notes
- Status: proposed
- Approval required: False
- Summary: FDA review material supports the more precise discontinued/withdrawn status.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2016/204442Orig1s000NameR.pdf
- Current: FDA Orange Book pre-1982 legacy ASM product (Paradione); discontinued U.S. product listing.
- Proposed: FDA/legacy ASM product (Paradione/paramethadione); discontinued with no generic equivalent; NDA 006800 withdrawn effective 06/04/2004.

## HIGH perampanel / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; DailyMed should be removed from the named source to keep sources within the trusted-source policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling

## HIGH perampanel / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification under the audit policy. FDA accessdata label supports the boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.generic_name%3A%22perampanel%22+OR+openfda.brand_name%3A%22perampanel%22+OR+openfda.substance_name%3A%22perampanel%22&limit=10
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=71cf3309-e182-473c-8b0b-280cabd0e122; published=Jan 28, 2026; title=FYCOMPA (PERAMPANEL) TABLET FYCOMPA (PERAMPANEL) SUSPENSION [EISAI INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=71cf3309-e182-473c-8b0b-280cabd0e122
- Proposed: FDA/Drugs@FDA label; status=boxed_warning_found; application=NDA 202834; label=2024/202834Orig1s019lbl.pdf; title=FYCOMPA (perampanel) tablets/oral suspension; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf

## HIGH perampanel / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The current field includes non-trusted or non-preferred sources for this audit and does not name PubMed/ClinicalTrials sources supporting RCT and outcome cells. DailyMed should not be used for boxed-warning verification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/39576191/; https://pubmed.ncbi.nlm.nih.gov/29250772/; https://pubmed.ncbi.nlm.nih.gov/27221398/; https://pubmed.ncbi.nlm.nih.gov/26296511/; https://clinicaltrials.gov/study/NCT00144690
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling; NCBI LiverTox; PubMed placebo-controlled RCTs; ClinicalTrials.gov trial records

## HIGH perampanel / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed-indexed Phase II randomized placebo-controlled perampanel trial report in adolescents with partial-onset seizures. It supports RCT coverage but should not change RR50/MPC/seizure-freedom outcome fields.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26724782/
- Proposed: Meador2016|https://pubmed.ncbi.nlm.nih.gov/26724782/

## HIGH perampanel / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Randomized double-blind placebo-controlled perampanel dose-escalation studies in refractory partial-onset seizures; ClinicalTrials.gov identifies related phase II study NCT00144690. Include only if the CSV field is intended to capture phase II safety/tolerability RCT reports as well as pivotal efficacy RCTs.
- Sources: https://pubmed.ncbi.nlm.nih.gov/21883097/
- Proposed: Krauss2012a|https://pubmed.ncbi.nlm.nih.gov/21883097/

## MEDIUM perampanel / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for this field; FDA accessdata label is permissible.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=71cf3309-e182-473c-8b0b-280cabd0e122; published=Jan 28, 2026; title=FYCOMPA (PERAMPANEL) TABLET FYCOMPA (PERAMPANEL) SUSPENSION [EISAI INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=71cf3309-e182-473c-8b0b-280cabd0e122
- Proposed: FDA/Drugs@FDA label; status=boxed_warning_found; application=NDA 202834; label=2024/202834Orig1s019lbl.pdf; title=FYCOMPA (perampanel) tablets/oral suspension; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf

## MEDIUM perampanel / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Use the FDA label source directly.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling

## MEDIUM perampanel / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Align source list with trusted-source policy and actual support for row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/39576191/; https://clinicaltrials.gov/study/NCT00144690
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling; NCBI LiverTox; PubMed placebo-controlled RCTs; ClinicalTrials.gov trial records

## MEDIUM perampanel / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; FDA accessdata label supports the boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=71cf3309-e182-473c-8b0b-280cabd0e122; published=Jan 28, 2026; title=FYCOMPA (PERAMPANEL) TABLET FYCOMPA (PERAMPANEL) SUSPENSION [EISAI INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=71cf3309-e182-473c-8b0b-280cabd0e122
- Proposed: FDA/Drugs@FDA label; status=boxed_warning_found; application=NDA 202834; label=2024/202834Orig1s019lbl.pdf; title=FYCOMPA (perampanel) tablets/oral suspension; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf

## MEDIUM perampanel / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Refresh the verification date if the FDA source update is applied.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## MEDIUM perampanel / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace non-trusted/non-preferred source names and add sources that support the RCT/outcome cells.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/39576191/; https://clinicaltrials.gov/study/NCT00144690
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling; NCBI LiverTox; PubMed placebo-controlled RCTs; ClinicalTrials.gov trial records

## MEDIUM perampanel / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is supported by FDA labeling; remove DailyMed from the named source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/202834Orig1s019lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling

## MEDIUM perampanel / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: False
- Summary: Meador2016 is a PubMed-indexed Phase II randomized placebo-controlled perampanel trial report. It should not alter outcome differentials.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26724782/
- Current: Vossler2024|https://pubmed.ncbi.nlm.nih.gov/39576191/; Nishida2017|https://pubmed.ncbi.nlm.nih.gov/29250772/; Lagae2016|https://pubmed.ncbi.nlm.nih.gov/27221398/; French2015|https://pubmed.ncbi.nlm.nih.gov/26296511/; Belousova2014|https://pubmed.ncbi.nlm.nih.gov/25345628/; Krauss2012|https://pubmed.ncbi.nlm.nih.gov/22517103/; French2012b|https://pubmed.ncbi.nlm.nih.gov/22905857/; French2012|https://pubmed.ncbi.nlm.nih.gov/22843280/
- Proposed: Vossler2024|https://pubmed.ncbi.nlm.nih.gov/39576191/; Nishida2017|https://pubmed.ncbi.nlm.nih.gov/29250772/; Lagae2016|https://pubmed.ncbi.nlm.nih.gov/27221398/; Meador2016|https://pubmed.ncbi.nlm.nih.gov/26724782/; French2015|https://pubmed.ncbi.nlm.nih.gov/26296511/; Belousova2014|https://pubmed.ncbi.nlm.nih.gov/25345628/; Krauss2012|https://pubmed.ncbi.nlm.nih.gov/22517103/; French2012b|https://pubmed.ncbi.nlm.nih.gov/22905857/; French2012|https://pubmed.ncbi.nlm.nih.gov/22843280/

## MEDIUM perampanel / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Clarifies missing RCT coverage and rejects the Yang2015 add-to-RCT-link finding for this row’s seizure-efficacy RCT field.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26724782/; https://pubmed.ncbi.nlm.nih.gov/26088895/
- Current: PubMed loop 40/65 on 2026-05-15: 8 qualifying placebo-controlled randomized clinical trial report(s) retained from 50 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Audit on 2026-05-21: existing efficacy/outcome RCT links and outcome differentials verified. Meador2016 (PMID 26724782) is an additional Phase II randomized placebo-controlled perampanel trial report but does not change RR50/MPC/seizure-freedom summaries. Yang2015 (PMID 26088895) supports QT assessment but should not be added as a seizure-efficacy RCT link.

## HIGH phenacemide / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: NIH/PubChem lists phenylacetylurea and phenacetylurea as synonyms for phenacemide. Phenurone is a trade name and should remain in trade_names/pubmed_search_aliases, not as a separate drug row.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Proposed: phenylacetylurea; phenacetylurea

## HIGH phenacemide / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Current alias list omits nonproprietary synonyms that may retrieve older literature.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: Phenurone
- Proposed: Phenurone; phenylacetylurea; phenacetylurea

## HIGH phenacemide / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should be removed from boxed-warning support. Current row also needs NIH/NCBI/PubMed sources for aliases and any retained non-FDA pharmacology facts.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phenacemide%22; https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide; https://pubmed.ncbi.nlm.nih.gov/?term=phenacemide+epilepsy+placebo+randomized+trial
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products/data files; FDA/openFDA labeling; NIH/NCBI PubChem; PubMed search/audit

## CRITICAL phenacemide / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: True
- Summary: NIH/PubChem lists phenacemide biological half-life as 22-25 hours. This contradicts retaining N/A if non-FDA pharmacokinetic sources are in scope.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: 22-25 hours (limited historical data)

## CRITICAL phenacemide / fact_check
- Field: major_organ_for_metabolism
- Status: incorrect
- Approval required: True
- Summary: NIH/PubChem states phenacemide is metabolized in the liver by hepatic microsomal enzymes and inactivated by p-hydroxylation.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Liver (hepatic microsomal metabolism; p-hydroxylation; limited historical data)

## CRITICAL phenacemide / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: True
- Summary: If the PubChem metabolism statement is accepted, the filter should not remain fully unknown.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: Limited/unknown
- Proposed: Hepatic (limited historical data)

## CRITICAL phenacemide / fact_check
- Field: mechanism_of_action
- Status: incorrect
- Approval required: True
- Summary: Orange Book does not support mechanism, but NIH/PubChem provides limited secondary pharmacology/mechanism summaries. Current N/A is incomplete if non-FDA sources are allowed.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Limited/uncertain: elevates seizure threshold and may prevent spread of seizure discharge; NIH/PubChem secondary summaries also describe neuronal sodium-channel or voltage-sensitive calcium-channel blockade.

## HIGH phenacemide / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: Orange Book data fields do not provide mechanism of action; it should not be cited as the mechanism source.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: FDA Orange Book products file
- Proposed: NIH/NCBI PubChem secondary pharmacology summaries

## MEDIUM phenacemide / fact_check
- Field: mechanism_source_tier
- Status: missing_source
- Approval required: False
- Summary: The confidence tier is directionally correct but should identify that the supporting mechanism source is not Orange Book/FDA labeling.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: Historical/limited
- Proposed: Historical/limited; NIH/NCBI secondary pharmacology

## INFO phenacemide / fact_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is appropriately blank because the corresponding RCT outcome is N/A.

## INFO phenacemide / fact_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is appropriately blank because the corresponding RCT outcome is N/A.

## INFO phenacemide / fact_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is appropriately blank because the corresponding RCT outcome is N/A.

## HIGH phenacemide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The boxed-warning field must not rely on DailyMed. The row bundle's deterministic FDA/openFDA check found no current FDA label for phenacemide/Phenurone; update the wording and source to FDA/openFDA only.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phenacemide%22; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22PHENURONE%22; https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-database
- Current: No current FDA/DailyMed label identified. Source cites FDA/DailyMed search.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM phenacemide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current source list uses DailyMed wording and omits NIH/NCBI/PubMed support for aliases and non-FDA pharmacology facts.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phenacemide%22; https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide; https://pubmed.ncbi.nlm.nih.gov/?term=phenacemide+epilepsy+placebo+randomized+trial
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products/data files; FDA/openFDA labeling; NIH/NCBI PubChem; PubMed search/audit

## MEDIUM phenacemide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box verification must be FDA/openFDA, FDA labels, or Drugs@FDA only.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phenacemide%22; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22PHENURONE%22
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [phenacemide; Phenurone].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [phenacemide; Phenurone].

## MEDIUM phenacemide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA Orange Book does not support mechanism of action details.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: FDA Orange Book products file
- Proposed: NIH/NCBI PubChem secondary pharmacology summaries

## MEDIUM phenacemide / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Important NIH/PubChem synonyms are missing; Phenurone should remain trade name/search alias, not a separate row.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Proposed: phenylacetylurea; phenacetylurea

## MEDIUM phenacemide / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Adds nonproprietary/chemical synonyms likely to retrieve older literature.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: Phenurone
- Proposed: Phenurone; phenylacetylurea; phenacetylurea

## MEDIUM phenacemide / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for black-box verification; row bundle supports FDA/openFDA-only wording.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phenacemide%22; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22PHENURONE%22
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM phenacemide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Source wording must use FDA/openFDA only for boxed-warning status.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phenacemide%22; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22PHENURONE%22
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [phenacemide; Phenurone].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [phenacemide; Phenurone].

## MEDIUM phenacemide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Removes DailyMed from black-box support and adds sources needed for aliases/pharmacology/RCT audit.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phenacemide%22; https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide; https://pubmed.ncbi.nlm.nih.gov/?term=phenacemide+epilepsy+placebo+randomized+trial
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products/data files; FDA/openFDA labeling; NIH/NCBI PubChem; PubMed search/audit

## CRITICAL phenacemide / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: NIH/PubChem provides a phenacemide half-life value.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: 22-25 hours (limited historical data)

## CRITICAL phenacemide / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: True
- Summary: NIH/PubChem provides hepatic metabolism information.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Liver (hepatic microsomal metabolism; p-hydroxylation; limited historical data)

## CRITICAL phenacemide / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: True
- Summary: Should align with the proposed hepatic metabolism update if accepted.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: Limited/unknown
- Proposed: Hepatic (limited historical data)

## CRITICAL phenacemide / proposed_row_update
- Field: mechanism_of_action
- Status: proposed
- Approval required: True
- Summary: Orange Book is not a mechanism source, but NIH/PubChem provides limited secondary mechanism/pharmacology summaries.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Limited/uncertain: elevates seizure threshold and may prevent spread of seizure discharge; NIH/PubChem secondary summaries also describe neuronal sodium-channel or voltage-sensitive calcium-channel blockade.

## MEDIUM phenacemide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Orange Book data fields do not support the mechanism cell.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: FDA Orange Book products file
- Proposed: NIH/NCBI PubChem secondary pharmacology summaries

## MEDIUM phenacemide / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: Clarifies source tier for the proposed mechanism value.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Phenacemide
- Current: Historical/limited
- Proposed: Historical/limited; NIH/NCBI secondary pharmacology

## HIGH phenobarbital / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Important PubMed records, including Bacon1981, use phenobarbitone. Leaving this blank risks missing same-drug records and should not create a duplicate drug row.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6116084/
- Proposed: phenobarbitone

## MEDIUM phenobarbital / fact_check
- Field: trade_names
- Status: missing_source
- Approval required: False
- Summary: FDA review supports historical Luminal and FDA approval/orphan records support current SEZABY. Phenobarb/Solfoton were not confirmed from FDA sources in this audit, but no direct contradiction was found, so do not delete them without user approval.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2023/215910Orig1s000MedR.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=703819; https://www.epilepsy.com/stories/summary-anti-seizure-medications
- Current: Luminal; Phenobarb; Solfoton
- Proposed: Luminal; Phenobarb; Solfoton; Sezaby

## CRITICAL phenobarbital / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: True
- Summary: The selected FDA label does not support 53-118 h; FDA labeling states neonatal t1/2 is about 1 week, and eMC SmPC reports adult half-life about 75-120 h and pediatric about 21-75 h. Current value should be replaced or separately sourced if retained.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf; https://www.medicines.org.uk/emc/product/3607/smpc
- Current: 53-118 h
- Proposed: Adults about 75-120 h; children about 21-75 h; neonates approximately 1 week

## CRITICAL phenobarbital / fact_check
- Field: maximum_approved_daily_dose
- Status: incorrect
- Approval required: True
- Summary: The current text is too vague for approved/labelled dosing. FDA SEZABY label provides a maximum loading dose and maintenance regimen; eMC provides usual oral adult and pediatric dosing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf; https://www.medicines.org.uk/emc/product/4920/smpc
- Current: Individualized by serum level/tolerability; no single fixed max
- Proposed: Depends on indication/formulation: SEZABY neonatal regimen maximum total loading dose 40 mg/kg and maintenance 4.5 mg/kg/day for up to 5 days; oral epilepsy SmPC usual adult daily dose 60-200 mg and pediatric 3-6 mg/kg/day

## CRITICAL phenobarbital / fact_check
- Field: qt_interval_effect
- Status: incorrect
- Approval required: True
- Summary: FDA label has a QT Prolongation warning and states SEZABY's QTc effect has not been adequately characterized, with nonclinical hERG signal and QTc prolongation reported in adult literature. Current wording is misleading.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf
- Current: No direct QT effect established
- Proposed: QTc effect not adequately characterized; FDA label warns to avoid concomitant use in patients at significant torsade de pointes risk and with drugs/products that may increase QTc-prolongation risk

## CRITICAL phenobarbital / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: FDA label provides specific neonatal trial percentages that do not match the row. eMC supports behavioral and dermatologic categories but not the row's percentages. The respiratory '<1%' statement is not supported and conflicts with FDA neonatal abnormal-respiration incidence.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf; https://www.medicines.org.uk/emc/product/4920/smpc
- Current: CNS: drowsiness/sedation 20-60%, behavioral: hyperactivity/irritability 5-15%, dermatologic: rash 1-3%, respiratory: respiratory depression <1% at therapeutic doses
- Proposed: CNS: sedation 16% in neonatal Study 1; respiratory: abnormal respiration 25% in neonatal Study 1 and respiratory depression reported/warned; GI/feeding: feeding disorder 16%; cardiovascular: hypotension 16%; behavioral/psychiatric symptoms including abnormal behavior, aggression, hyperactivity, agitation and irritability reported, frequency not reliably estimable; dermatologic reactions including rash, SJS/TEN and DRESS reported, frequency not reliably estimable

## HIGH phenobarbital / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Current evidence_sources includes DailyMed for FDA labeling and non-whitelisted sources. Replace with trusted domains actually used to support row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK548269/; https://www.medicines.org.uk/emc/product/4920/smpc; https://www.medicines.org.uk/emc/product/3607/smpc; https://www.epilepsy.com/stories/summary-anti-seizure-medications
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/Drugs@FDA SEZABY label and approval review; FDA/openFDA SEZABY label API; NCBI Bookshelf LiverTox phenobarbital; NCBI Bookshelf StatPearls phenobarbital/barbiturates; eMC/medicines.org.uk Phenobarbital Elixir BP and Phenobarbital Sodium Injection SmPCs; Epilepsy Foundation ASM summary; PubMed RCT records for Takami2019, Crawley2000 and Bacon1981

## MEDIUM phenobarbital / fact_check
- Field: mechanism_source
- Status: missing_source
- Approval required: False
- Summary: Mechanism is supportable from FDA labeling and NCBI. DailyMed should be removed from the source wording; AES/Sills-Rogawski were not independently verified in this audit from whitelisted source URLs.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK532277/
- Current: FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/Drugs@FDA SEZABY label; NCBI Bookshelf Phenobarbital StatPearls

## HIGH phenobarbital / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: ClinicalTrials.gov describes a completed phase 3 randomized quadruple-masked placebo-controlled phenobarbital adjunctive trial, but no PMID was identified in the provided bundle.
- Sources: https://clinicaltrials.gov/study/NCT01284556
- Proposed: Do not add to pubmed_phase_ii_iii_rct_links unless a PMID/publication is identified; consider a separate ClinicalTrials.gov evidence field if unpublished trials are tracked.

## MEDIUM phenobarbital / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification; use FDA/openFDA or accessdata FDA labeling.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=8c7d0402-4977-4c25-bc4b-11db91339e9a; published=; title=These highlights do not include all the information needed to use SEZABY safely and effectively. See full prescribing information for SEZABY. SEZABY™ (phenobarbital sodium) for injection, for intravenous use, CIV Initial U.S. Approval: 2022; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=8c7d0402-4977-4c25-bc4b-11db91339e9a
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=8c7d0402-4977-4c25-bc4b-11db91339e9a; effective_time=20251223; title=SEZABY / PHENOBARBITAL SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%228c7d0402-4977-4c25-bc4b-11db91339e9a%22&limit=5

## MEDIUM phenobarbital / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The mechanism fact is supported by FDA and NCBI sources; DailyMed and unverified non-whitelisted sources should not be the named support.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK532277/
- Current: FDA/DailyMed labeling; American Epilepsy Society 2024 U.S. ASM summary; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/Drugs@FDA SEZABY label; NCBI Bookshelf Phenobarbital StatPearls

## MEDIUM phenobarbital / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Important same-drug PubMed literature uses the non-US spelling.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6116084/
- Proposed: phenobarbitone

## MEDIUM phenobarbital / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: SEZABY is an FDA-approved phenobarbital sodium trade name; no deletion proposed for unverified names without direct contradiction.
- Sources: https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=703819
- Current: Luminal; Phenobarb; Solfoton
- Proposed: Luminal; Phenobarb; Solfoton; Sezaby

## CRITICAL phenobarbital / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: True
- Summary: FDA label contains QT Prolongation warning and contradicts the current reassuring wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf
- Current: No direct QT effect established
- Proposed: QTc effect not adequately characterized; FDA label warns to avoid concomitant use in patients at significant torsade de pointes risk and with drugs/products that may increase QTc-prolongation risk

## CRITICAL phenobarbital / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: Current numeric range was not supported by the selected FDA/openFDA source; trusted FDA/eMC sources support different population-specific values.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf; https://www.medicines.org.uk/emc/product/3607/smpc
- Current: 53-118 h
- Proposed: Adults about 75-120 h; children about 21-75 h; neonates approximately 1 week

## CRITICAL phenobarbital / proposed_row_update
- Field: maximum_approved_daily_dose
- Status: proposed
- Approval required: True
- Summary: FDA/eMC labeling provides labelled regimen limits and usual dose ranges.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/215910s000lbl.pdf; https://www.medicines.org.uk/emc/product/4920/smpc
- Current: Individualized by serum level/tolerability; no single fixed max
- Proposed: Depends on indication/formulation: SEZABY neonatal regimen maximum total loading dose 40 mg/kg and maintenance 4.5 mg/kg/day for up to 5 days; oral epilepsy SmPC usual adult daily dose 60-200 mg and pediatric 3-6 mg/kg/day

## HIGH phensuximide / fact_check
- Field: alternate_generic_names
- Status: incorrect
- Approval required: False
- Summary: The blank value is missing important aliases. NCBI MeSH lists phensuccimide as an entry term for phensuximide; PubMed PMID 13244795 identifies methylphenylsuccinimide (Milontin) and indexes phensuximide as the substance.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/67100129; https://pubmed.ncbi.nlm.nih.gov/13244795/
- Proposed: phensuccimide; methylphenylsuccinimide

## HIGH phensuximide / fact_check
- Field: pubmed_search_aliases
- Status: incorrect
- Approval required: False
- Summary: Milontin is verified, but PubMed/NCBI aliases useful for literature retrieval are missing.
- Sources: https://pubmed.ncbi.nlm.nih.gov/13244795/; https://www.ncbi.nlm.nih.gov/mesh/67100129
- Current: Milontin
- Proposed: Milontin; methylphenylsuccinimide; phensuccimide

## HIGH phensuximide / fact_check
- Field: year_fda_cleared
- Status: incorrect
- Approval required: False
- Summary: The current value is an Orange Book legacy placeholder; FDA/openFDA Drugs@FDA gives the exact original approval date for NDA008855.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=application_number:%22NDA008855%22&limit=5; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: 1953-09-08 (FDA/openFDA Drugs@FDA NDA008855 ORIG 1 approval date)

## HIGH phensuximide / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be cited for boxed-warning verification, and PubMed/NCBI sources are needed for aliases, epilepsy type, and half-life facts.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=application_number:%22NDA008855%22&limit=5; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phensuximide%22&limit=1; https://pubmed.ncbi.nlm.nih.gov/116142/; https://www.ncbi.nlm.nih.gov/books/NBK2597/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA/openFDA Drugs@FDA application endpoint; FDA/openFDA label API; FDA Orange Book data files; PubMed/NCBI Bookshelf

## HIGH phensuximide / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: The 0% wording is not supported by absence of a label and should not imply zero adverse events. FDA/openFDA label searches found no current phensuximide/Milontin label.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phensuximide%22&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22MILONTIN%22&limit=1; https://api.fda.gov/drug/drugsfda.json?search=application_number:%22NDA008855%22&limit=5
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A: no current FDA/openFDA label identified; FDA/openFDA Drugs@FDA and Orange Book product listings do not provide adverse-event percentages.

## HIGH phensuximide / fact_check
- Field: epilepsy_type
- Status: incorrect
- Approval required: False
- Summary: FDA/openFDA product data do not provide the labeled seizure category, but PubMed evidence specifically indexes phensuximide under absence epilepsy and older Milontin literature refers to petit mal epilepsy.
- Sources: https://pubmed.ncbi.nlm.nih.gov/116142/; https://pubmed.ncbi.nlm.nih.gov/13422710/; https://api.fda.gov/drug/drugsfda.json?search=application_number:%22NDA008855%22&limit=5
- Current: Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)
- Proposed: Historical absence/petit mal epilepsy evidence; specific FDA-labeled seizure category not available from FDA/openFDA product listing.

## HIGH phensuximide / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: False
- Summary: PubMed PMID 116142 reports a mean phensuximide half-life of 7.8 hours in single- and chronic-dose studies in five patients with intractable seizures.
- Sources: https://pubmed.ncbi.nlm.nih.gov/116142/
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: Mean 7.8 hours for phensuximide; desmethylphensuximide had a similar half-life (small 5-patient clinical pharmacokinetic study).

## MEDIUM phensuximide / fact_check
- Field: mechanism_of_action
- Status: missing_source
- Approval required: False
- Summary: FDA product data do not provide mechanism. NCBI Bookshelf lists phensuximide as an older succinimide and describes the succinimide anti-absence class mechanism; this is a class inference, not a phensuximide-specific FDA label claim.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK2597/; https://www.ncbi.nlm.nih.gov/books/NBK544244/; https://pubmed.ncbi.nlm.nih.gov/116142/
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Succinimide anticonvulsant; anti-absence mechanism is limited/inferred from the succinimide class, which reduces thalamic low-threshold calcium currents and suppresses 3-Hz spike-wave activity. Phensuximide-specific mechanism evidence remains limited.

## MEDIUM phensuximide / fact_check
- Field: mechanism_source
- Status: missing_source
- Approval required: False
- Summary: Orange Book/product data verify identity and approval status but do not support mechanism text.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK2597/; https://pubmed.ncbi.nlm.nih.gov/116142/
- Current: FDA Orange Book products file
- Proposed: NCBI Bookshelf succinimide class discussion; PubMed PMID 116142; FDA/openFDA Drugs@FDA for product identity

## HIGH phensuximide / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: If the mechanism cell is updated, the source tier should reflect NCBI secondary evidence and older peer-reviewed clinical pharmacology rather than Orange Book alone.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK2597/; https://pubmed.ncbi.nlm.nih.gov/116142/
- Current: Historical/limited
- Proposed: NCBI/peer-reviewed limited

## INFO phensuximide / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is not applicable because the corresponding outcome value is N/A.

## INFO phensuximide / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is not applicable because the corresponding outcome value is N/A.

## INFO phensuximide / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field is not applicable because the corresponding outcome value is N/A.

## HIGH phensuximide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: FDA/openFDA label searches for generic name phensuximide and brand name MILONTIN returned no matching current FDA label. DailyMed should not be used or named for the boxed-warning field under the audit policy.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phensuximide%22&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22MILONTIN%22&limit=1
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM phensuximide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification, and non-FDA trusted sources are needed for aliases, epilepsy type, and half-life.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=application_number:%22NDA008855%22&limit=5; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phensuximide%22&limit=1; https://pubmed.ncbi.nlm.nih.gov/116142/; https://www.ncbi.nlm.nih.gov/books/NBK2597/
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA/openFDA Drugs@FDA application endpoint; FDA/openFDA label API; FDA Orange Book data files; PubMed/NCBI Bookshelf

## MEDIUM phensuximide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed wording with FDA/openFDA-only boxed-warning source wording.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phensuximide%22&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22MILONTIN%22&limit=1
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [phensuximide; Milontin].
- Proposed: FDA/openFDA label API searches on 2026-05-21: no current FDA label found for openfda.generic_name:"phensuximide" or openfda.brand_name:"MILONTIN".

## MEDIUM phensuximide / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Reflects the FDA/openFDA label API verification date used in this audit.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phensuximide%22&limit=1
- Current: 05-20-2026
- Proposed: 05-21-2026

## MEDIUM phensuximide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Orange Book/product data do not support mechanism text; NCBI/PubMed support only a limited class-level mechanism.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK2597/; https://pubmed.ncbi.nlm.nih.gov/116142/
- Current: FDA Orange Book products file
- Proposed: NCBI Bookshelf succinimide class discussion; PubMed PMID 116142; FDA/openFDA Drugs@FDA for product identity

## MEDIUM phensuximide / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Missing important aliases for the same drug.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/67100129; https://pubmed.ncbi.nlm.nih.gov/13244795/
- Proposed: phensuccimide; methylphenylsuccinimide

## MEDIUM phensuximide / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add literature-search aliases without creating a duplicate drug row.
- Sources: https://pubmed.ncbi.nlm.nih.gov/13244795/; https://www.ncbi.nlm.nih.gov/mesh/67100129
- Current: Milontin
- Proposed: Milontin; methylphenylsuccinimide; phensuccimide

## MEDIUM phensuximide / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: FDA/openFDA Drugs@FDA provides the exact original approval date.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=application_number:%22NDA008855%22&limit=5
- Current: Approved Prior to Jan 1, 1982 (FDA Orange Book)
- Proposed: 1953-09-08 (FDA/openFDA Drugs@FDA NDA008855 ORIG 1 approval date)

## MEDIUM phensuximide / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Remove unsupported 0% implication and DailyMed wording.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phensuximide%22&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22MILONTIN%22&limit=1
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A: no current FDA/openFDA label identified; FDA/openFDA Drugs@FDA and Orange Book product listings do not provide adverse-event percentages.

## MEDIUM phensuximide / proposed_row_update
- Field: epilepsy_type
- Status: proposed
- Approval required: False
- Summary: PubMed evidence supports absence/petit mal historical use while FDA/openFDA product data do not expose a labeled seizure category.
- Sources: https://pubmed.ncbi.nlm.nih.gov/116142/; https://pubmed.ncbi.nlm.nih.gov/13422710/
- Current: Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)
- Proposed: Historical absence/petit mal epilepsy evidence; specific FDA-labeled seizure category not available from FDA/openFDA product listing.

## MEDIUM phensuximide / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: PubMed PMID 116142 provides phensuximide-specific half-life evidence.
- Sources: https://pubmed.ncbi.nlm.nih.gov/116142/
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: Mean 7.8 hours for phensuximide; desmethylphensuximide had a similar half-life (small 5-patient clinical pharmacokinetic study).

## MEDIUM phensuximide / proposed_row_update
- Field: mechanism_of_action
- Status: proposed
- Approval required: False
- Summary: Current source does not support a mechanism; NCBI supports a limited class-level mechanism and phensuximide as an older succinimide.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK2597/; https://www.ncbi.nlm.nih.gov/books/NBK544244/
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Succinimide anticonvulsant; anti-absence mechanism is limited/inferred from the succinimide class, which reduces thalamic low-threshold calcium currents and suppresses 3-Hz spike-wave activity. Phensuximide-specific mechanism evidence remains limited.

## MEDIUM phensuximide / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Boxed-warning verification must use FDA/openFDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22phensuximide%22&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:%22MILONTIN%22&limit=1
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## HIGH phenytoin / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: Diphenylhydantoin is an established phenytoin alias in PubMed RCT records, and phenytoin sodium is the labeled salt form used for capsules/injection.
- Sources: https://pubmed.ncbi.nlm.nih.gov/4610196/; https://pubmed.ncbi.nlm.nih.gov/2686433/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf
- Proposed: diphenylhydantoin; phenytoin sodium

## HIGH phenytoin / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Missing diphenylhydantoin aliases can cause phenytoin RCTs to be missed or misclassified.
- Sources: https://pubmed.ncbi.nlm.nih.gov/4610196/; https://pubmed.ncbi.nlm.nih.gov/2686433/
- Proposed: diphenylhydantoin; diphenylhydantoin sodium; phenytoin sodium

## HIGH phenytoin / fact_check
- Field: formulations_available
- Status: incorrect
- Approval required: False
- Summary: US FDA labeling supports extended capsules, chewable tablets, oral suspension, and parenteral phenytoin sodium injection for intravenous or intramuscular use.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2015/084427Orig1s032lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2013/008762s047lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/010151s047s048lbl.pdf
- Current: Capsule; chewable tablet; oral suspension; IV injection
- Proposed: Capsule; chewable tablet; oral suspension; IV/IM injection

## CRITICAL phenytoin / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: True
- Summary: FDA supports phenytoin as a strong CYP3A inducer and potent hepatic enzyme inducer. PubMed review supports CYP/UGT induction. FDA/eMC labeling supports CYP2C9/CYP2C19 metabolism and saturable metabolism, but the current wording overstates CYP2C9/19 as strong induced enzymes.
- Sources: https://www.fda.gov/drugs/drug-interactions-labeling/drug-development-and-drug-interactions-table-substrates-inhibitors-and-inducers; https://pubmed.ncbi.nlm.nih.gov/9606477/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf; https://www.medicines.org.uk/emc/product/7558/smpc
- Current: Strong enzyme inducer: CYP3A4, CYP2C9/19, and UGT; nonlinear metabolism
- Proposed: Strong CYP3A inducer and broad/potent hepatic enzyme inducer of CYP/UGT pathways; primarily metabolized by CYP2C9 and CYP2C19; saturable/nonlinear metabolism

## HIGH phenytoin / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not in the trusted source list supplied for this audit. FDA accessdata labeling supports the mechanism cell.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA accessdata labeling; Sills and Rogawski 2020 ASM mechanism review

## CRITICAL phenytoin / fact_check
- Field: year_fda_cleared
- Status: incorrect
- Approval required: True
- Summary: FDA labeling lists Initial U.S. Approval as 1953; 1938 may refer to historical introduction/use but is not supported as the FDA clearance/approval year in the checked FDA labels.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/010151s047s048lbl.pdf
- Current: 1938 legacy approval
- Proposed: 1953 (Initial U.S. Approval)

## MEDIUM phenytoin / fact_check
- Field: adverse_symptoms_percentages
- Status: insufficient_evidence
- Approval required: True
- Summary: Checked sources support the adverse event types but not the current exact nystagmus/ataxia/dizziness percentages. NCBI sources give different gingival/rash estimates and describe SJS/TEN as rare serious reactions.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548889/; https://www.ncbi.nlm.nih.gov/books/NBK423938/; https://www.ncbi.nlm.nih.gov/books/NBK482444/
- Current: Neurologic: nystagmus 20-40%, neurologic: ataxia 10-30%, CNS: dizziness 10-20%, gingival: gingival hyperplasia 20%, dermatologic: rash 5-10%, dermatologic: SJS/TEN <1%
- Proposed: Neurologic/CNS: nystagmus, ataxia, slurred speech/decreased coordination, somnolence/mental confusion, dizziness/vertigo (common or dose-related; exact percentages not consistently quantified in checked FDA/NCBI sources); gingival: gingival hyperplasia/overgrowth reported (13% clinically significant in one community study; estimates up to 50% in reviews); dermatologic: rash reported (morbilliform rash 2-5% in IARC review; LiverTox notes rash can occur in 10%); severe dermatologic: SJS/TEN rare serious reactions

## HIGH phenytoin / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Several current named sources are not in the trusted-source domain list or do not support the specific FDA boxed-warning field. Replace with sources actually used for checked cells.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK548889/; https://www.ncbi.nlm.nih.gov/books/NBK423938/; https://www.medicines.org.uk/emc/product/7558/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA accessdata labeling; FDA/openFDA drug label API for boxed warning; NCBI Bookshelf LiverTox/StatPearls/IARC phenytoin monographs; PubMed RCT records; eMC SmPC records for UK trade names; FDA drug-interaction table

## HIGH phenytoin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_placebo_rct
- Approval required: True
- Summary: PubMed abstract states the design was prospective open-label controlled; the control group did not receive phenytoin, so this is not a placebo-controlled trial despite randomization.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11903465/
- Current: https://pubmed.ncbi.nlm.nih.gov/11903465/
- Proposed: Remove from placebo-controlled RCT list or move to a non-placebo randomized-control field; user approval required because this deletes an existing link.

## HIGH phenytoin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: The randomized intervention is oxcarbazepine vs placebo in patients receiving background carbamazepine/valproate/phenytoin; phenytoin is not the randomized study drug.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8148215/
- Current: https://pubmed.ncbi.nlm.nih.gov/8148215/
- Proposed: Do not add to the phenytoin row's placebo-controlled phenytoin RCT list.

## HIGH phenytoin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: The randomized intervention is folic acid vs lactose for phenytoin-induced gingival hyperplasia; phenytoin is background exposure/adverse-effect cause, not the trial drug for seizure efficacy.
- Sources: https://pubmed.ncbi.nlm.nih.gov/1828561/
- Current: https://pubmed.ncbi.nlm.nih.gov/1828561/
- Proposed: Do not add to the phenytoin ASM RCT list.

## HIGH phenytoin / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Diphenylhydantoin is a phenytoin alias. PubMed classifies the report as Clinical Trial and Randomized Controlled Trial with placebo and seizure-prevention MeSH terms; include if alcohol-withdrawal seizure trials are in row scope.
- Sources: https://pubmed.ncbi.nlm.nih.gov/4610196/
- Proposed: Sampliner1974|https://pubmed.ncbi.nlm.nih.gov/4610196/

## HIGH phenytoin / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Prospective randomized double-blind placebo-controlled IV diphenylhydantoin/phenytoin trial for recurrent alcohol-withdrawal seizures; include if provoked seizure trials are in scope.
- Sources: https://pubmed.ncbi.nlm.nih.gov/2686433/
- Proposed: Alldredge1989|https://pubmed.ncbi.nlm.nih.gov/2686433/

## HIGH phenytoin / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: Prospective randomized placebo-controlled double-blind phenytoin trial for recurrence of alcohol-withdrawal seizures; include if provoked seizure trials are in scope.
- Sources: https://pubmed.ncbi.nlm.nih.gov/2024792/
- Proposed: Chance1991|https://pubmed.ncbi.nlm.nih.gov/2024792/

## CRITICAL phenytoin / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: True
- Summary: FDA/openFDA confirms a boxed warning for IV phenytoin rapid infusion. DailyMed is not permissible for this field, and the current cell should use FDA/openFDA or accessdata FDA labeling metadata instead.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/010151s047s048lbl.pdf
- Current: Boxed warning text is populated but uses a DailyMed source, contains duplicated heading text, and includes internally inconsistent/typographic wording such as CARIOVASCULAR, per minutes, and pediatric 1 to 3 mg/min in part of the text.
- Proposed: WARNING: CARDIOVASCULAR RISK ASSOCIATED WITH RAPID INFUSION. Do not exceed IV phenytoin administration rates of 50 mg/min in adults or 1 to 3 mg/kg/min (or 50 mg/min, whichever is slower) in pediatric patients because rapid infusion can cause severe hypotension and cardiac arrhythmias. Monitor cardiac status during and after administration; reduce the rate or stop dosing if needed.

## MEDIUM phenytoin / proposed_row_update
- Field: FDA/DailyMed source usage
- Status: proposed
- Approval required: False
- Summary: The audit policy forbids DailyMed for FDA boxed-warning verification and trusted-source list does not include DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/010151s047s048lbl.pdf
- Current: FDA/DailyMed labeling in evidence_sources and mechanism_source; DailyMed URL in fda_black_box_warning_source
- Proposed: Use FDA accessdata labeling and FDA/openFDA drug label API for FDA facts; remove DailyMed as black-box-warning support

## MEDIUM phenytoin / proposed_row_update
- Field: latest_deterministic_update_check_findings_for_row
- Status: proposed
- Approval required: False
- Summary: McKee1994 randomizes oxcarbazepine, not phenytoin; Brown1991 randomizes folic acid, not phenytoin.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8148215/; https://pubmed.ncbi.nlm.nih.gov/1828561/
- Current: update_check proposed McKee1994 and Brown1991 as new qualifying phenytoin RCTs
- Proposed: Reject McKee1994 and Brown1991 for this row's phenytoin placebo-controlled ASM RCT list

## MEDIUM phenytoin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification; use FDA/openFDA metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=a52cf1bd-dc1f-47be-aba8-29066d9a50fb; ... url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a52cf1bd-dc1f-47be-aba8-29066d9a50fb
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=a52cf1bd-dc1f-47be-aba8-29066d9a50fb; effective_time=20241226; title=PHENYTOIN SODIUM / PHENYTOIN SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5

## CRITICAL phenytoin / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: True
- Summary: Normalizes the boxed warning to FDA-supported content and removes duplicated/erroneous wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/010151s047s048lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22a52cf1bd-dc1f-47be-aba8-29066d9a50fb%22&limit=5
- Current: Current long boxed-warning text with duplicated heading and DailyMed-derived typographic inconsistencies
- Proposed: WARNING: CARDIOVASCULAR RISK ASSOCIATED WITH RAPID INFUSION. Do not exceed IV phenytoin administration rates of 50 mg/min in adults or 1 to 3 mg/kg/min (or 50 mg/min, whichever is slower) in pediatric patients because rapid infusion can cause severe hypotension and cardiac arrhythmias. Monitor cardiac status during and after administration; reduce the rate or stop dosing if needed.

## CRITICAL phenytoin / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: True
- Summary: Checked FDA labels list 1953 as Initial U.S. Approval.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/010151s047s048lbl.pdf
- Current: 1938 legacy approval
- Proposed: 1953 (Initial U.S. Approval)

## MEDIUM phenytoin / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Adds important alias/salt names to prevent duplicate-row or PubMed-search misses.
- Sources: https://pubmed.ncbi.nlm.nih.gov/4610196/; https://pubmed.ncbi.nlm.nih.gov/2686433/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf
- Proposed: diphenylhydantoin; phenytoin sodium

## MEDIUM phenytoin / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Diphenylhydantoin appears in placebo-controlled phenytoin RCT titles/records.
- Sources: https://pubmed.ncbi.nlm.nih.gov/4610196/; https://pubmed.ncbi.nlm.nih.gov/2686433/
- Proposed: diphenylhydantoin; diphenylhydantoin sodium; phenytoin sodium

## MEDIUM phenytoin / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: False
- Summary: Parenteral phenytoin sodium injection labeling includes IV or IM use.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/010151s047s048lbl.pdf
- Current: Capsule; chewable tablet; oral suspension; IV injection
- Proposed: Capsule; chewable tablet; oral suspension; IV/IM injection

## CRITICAL phenytoin / proposed_row_update
- Field: filter_mechanism
- Status: proposed
- Approval required: True
- Summary: FDA labeling supports voltage-dependent sodium channel blockade as the thought mechanism, while noting the precise mechanism is not established.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf
- Current: Other / unclear
- Proposed: Sodium channel blocker

## CRITICAL phenytoin / proposed_row_update
- Field: filter_qt_effect
- Status: proposed
- Approval required: True
- Summary: Checked FDA labeling supports arrhythmia/conduction risk but not a QT-prolongation classification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2017/010151s047s048lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/084349s088lbl.pdf
- Current: Conduction/arrhythmia caution; QT prolongation
- Proposed: Conduction/arrhythmia caution

## CRITICAL phenytoin / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: DeSantis2002 is randomized open-label/no-treatment control rather than placebo-controlled. The three added records are phenytoin/diphenylhydantoin placebo-controlled RCTs if alcohol-withdrawal seizure trials are in scope.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11903465/; https://pubmed.ncbi.nlm.nih.gov/4610196/; https://pubmed.ncbi.nlm.nih.gov/2686433/; https://pubmed.ncbi.nlm.nih.gov/2024792/
- Current: Young2004|https://pubmed.ncbi.nlm.nih.gov/15039684/; DeSantis2002|https://pubmed.ncbi.nlm.nih.gov/11903465/; Dikmen1991|https://pubmed.ncbi.nlm.nih.gov/1995974/; Temkin1990|https://pubmed.ncbi.nlm.nih.gov/2115976/; Bacon1981|https://pubmed.ncbi.nlm.nih.gov/6116084/; North1980|https://pubmed.ncbi.nlm.nih.gov/6101843/
- Proposed: Young2004|https://pubmed.ncbi.nlm.nih.gov/15039684/; Dikmen1991|https://pubmed.ncbi.nlm.nih.gov/1995974/; Temkin1990|https://pubmed.ncbi.nlm.nih.gov/2115976/; Bacon1981|https://pubmed.ncbi.nlm.nih.gov/6116084/; North1980|https://pubmed.ncbi.nlm.nih.gov/6101843/; Sampliner1974|https://pubmed.ncbi.nlm.nih.gov/4610196/; Alldredge1989|https://pubmed.ncbi.nlm.nih.gov/2686433/; Chance1991|https://pubmed.ncbi.nlm.nih.gov/2024792/

## HIGH piracetam / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: NCBI MeSH lists these entry terms for Piracetam; leaving aliases blank risks duplicate-row creation or missed searches.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68010889
- Proposed: Pyracetam; Pirazetam; 2-Pyrrolidone-N-Acetamide

## HIGH piracetam / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: NCBI MeSH lists these entry terms for Piracetam; adding them helps prevent alias-driven duplicate rows and missed PubMed retrievals.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68010889
- Proposed: Nootropil; Nootropyl; Nootrop; Normabrain; UCB-6215; UCB6215; Pyramem

## HIGH piracetam / fact_check
- Field: year_fda_cleared
- Status: incorrect
- Approval required: False
- Summary: Drug products are FDA-approved, not FDA-cleared. FDA/openFDA and Drugs@FDA/NDC searches support no current FDA approval/marketing record found for these terms.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=piracetam&limit=1; https://api.fda.gov/drug/ndc.json?search=generic_name:%22PIRACETAM%22&limit=1; https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-database
- Current: Not FDA-cleared for epilepsy or not marketed in U.S.
- Proposed: Not FDA-approved for epilepsy; no current FDA/openFDA label, Drugs@FDA record, or NDC listing found for piracetam/Nootropil.

## CRITICAL piracetam / fact_check
- Field: formulations_available
- Status: incorrect
- Approval required: True
- Summary: UK eMC verifies 800/1200 mg film-coated tablets and 33% oral solution. EMA nationally authorised product list verifies injection/infusion products in some EU member states. Capsule is not supported by the reviewed trusted sources.
- Sources: https://www.medicines.org.uk/emc/ingredient/813; https://www.medicines.org.uk/emc/product/101132/smpc; https://www.ema.europa.eu/en/documents/psusa/piracetam-list-nationally-authorised-medicinal-products-psusa00002429202204_en.pdf
- Current: Tablet/capsule; oral solution; injection in some markets
- Proposed: Film-coated tablets; oral solution; solution for injection/infusion in some EU markets

## CRITICAL piracetam / fact_check
- Field: filter_formulation
- Status: incorrect
- Approval required: True
- Summary: Trusted sources support oral solution, film-coated tablets, and injection/infusion products, but not capsule or specifically IV/IM route wording.
- Sources: https://www.medicines.org.uk/emc/ingredient/813; https://www.ema.europa.eu/en/documents/psusa/piracetam-list-nationally-authorised-medicinal-products-psusa00002429202204_en.pdf
- Current: Capsule; IV/IM injection; Liquid; Tablet
- Proposed: Injection/infusion solution; Liquid/oral solution; Tablet

## HIGH piracetam / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: False
- Summary: The UK SmPC states plasma half-life is 5.0 hours in young adult men; the 4 h lower bound was not supported by reviewed trusted sources.
- Sources: https://www.medicines.org.uk/emc/product/101132/smpc
- Current: 4-5 h
- Proposed: Approximately 5 h (plasma half-life in young adult men)

## HIGH piracetam / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: SmPC supports low interaction potential and no inhibition of major CYP isoforms at tested concentrations, with only minor high-concentration CYP2A6/CYP3A4/5 effects. It does not directly prove absence of CYP induction.
- Sources: https://www.medicines.org.uk/emc/product/101132/smpc
- Current: Not a CYP inducer/inhibitor
- Proposed: No clinically meaningful CYP inhibition expected; metabolic interaction with other drugs is unlikely

## CRITICAL piracetam / fact_check
- Field: filter_mechanism
- Status: incorrect
- Approval required: True
- Summary: The SmPC says piracetam's mode of action in cortical myoclonus is unknown. A GABA filter implies a direct GABAergic mechanism that the row itself warns against.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc
- Current: GABA
- Proposed: Unknown/Other

## HIGH piracetam / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The cited mechanism source is UK eMC SmPC. EMA product-list evidence supports formulations but is not the mechanism source.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc
- Current: EMA/UK SmPC
- Proposed: UK SmPC

## CRITICAL piracetam / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: Current trusted SmPC supports adverse reaction frequency categories, not the exact percentages. It lists diarrhea/diarrhoea as frequency not known, which conflicts with an exact 0.8% value.
- Sources: https://www.medicines.org.uk/emc/product/101132/smpc
- Current: CNS: hyperkinesia 1.7%, metabolic: weight gain 1.3%, psychiatric: nervousness 1.1%, CNS: somnolence 0.9%, GI: diarrhea 0.8%
- Proposed: CNS: hyperkinesia (common); CNS: somnolence (uncommon); psychiatric: nervousness (common); weight increased (common, investigations); GI: diarrhea/diarrhoea (frequency not known)

## MEDIUM piracetam / fact_check
- Field: qt_interval_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: No trusted source reviewed established a clinically meaningful QT effect, but the row also lacks a positive source explicitly supporting this negative statement. Treat as insufficiently sourced rather than contradicted.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc
- Current: No clinically meaningful QT effect established
- Proposed: No clinically meaningful QT effect established

## MEDIUM piracetam / fact_check
- Field: filter_qt_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: No QT warning/effect was identified in reviewed trusted labeling, but the exact filter claim is not directly supported by a dedicated QT source.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc
- Current: No known meaningful QT effect
- Proposed: No known meaningful QT effect

## HIGH piracetam / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Epilepsy Society is outside the requested trusted-source domains, and FDA/DailyMed labeling is misleading because no FDA label was found and DailyMed is not permissible for boxed-warning verification.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc; https://www.ema.europa.eu/en/documents/psusa/piracetam-list-nationally-authorised-medicinal-products-psusa00002429202204_en.pdf; https://open.fda.gov/apis/drug/label/; https://www.ncbi.nlm.nih.gov/mesh/68010889; https://www.ilae.org/index.cfm?objectid=6C4D71BD-EE34-B816-27EB767D97DE334A
- Current: Epilepsy Society ASM list; UK eMC SmPC labeling; FDA/DailyMed labeling
- Proposed: UK eMC SmPC/PIL labeling; EMA PSUSA nationally authorised product list; FDA/openFDA label, Drugs@FDA, and NDC APIs; PubMed/NCBI MeSH and RCT records; ILAE guidance

## MEDIUM piracetam / fact_check
- Field: status_or_notes
- Status: missing_source
- Approval required: False
- Summary: Cortical/progressive myoclonic epilepsy use is supported by eMC/ILAE. The reviewed trusted sources support nootropic classification, but not the broader cognitive-indication marketing claim.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc; https://www.ilae.org/index.cfm?objectid=6C4D71BD-EE34-B816-27EB767D97DE334A
- Current: Used for cortical myoclonus/myoclonic seizures in some jurisdictions; also marketed as nootropic/for cognitive indications in some markets.
- Proposed: Used for cortical myoclonus/progressive myoclonic epilepsies in some jurisdictions; pharmacotherapeutic group: nootropics (ATC N06BX03).

## HIGH piracetam / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed abstract identifies a placebo-controlled, double-blind crossover trial in which patients were randomly allocated to piracetam 2.4-16.8 g/day or placebo for cortical myoclonus. It is not phase-tagged, but is relevant placebo-controlled randomized piracetam evidence for the row's cortical myoclonus indication.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8419809/
- Proposed: Brown1993|https://pubmed.ncbi.nlm.nih.gov/8419809/

## INFO piracetam / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Blank plot value is consistent with non-extractable RR50 differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9527146/

## INFO piracetam / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Blank plot value is consistent with non-extractable seizure-frequency MPC differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9527146/

## INFO piracetam / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Blank plot value is consistent with non-extractable seizure-freedom differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9527146/

## HIGH piracetam / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: openFDA label API searches for piracetam and Nootropil returned no matches. DailyMed should not be named for boxed-warning verification under the audit policy.
- Sources: https://api.fda.gov/drug/label.json?search=piracetam&limit=1; https://api.fda.gov/drug/label.json?search=Nootropil&limit=1; https://open.fda.gov/apis/drug/label/
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM piracetam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Boxed-warning verification must use FDA sources only; DailyMed should be removed.
- Sources: https://api.fda.gov/drug/label.json?search=piracetam&limit=1; https://api.fda.gov/drug/label.json?search=Nootropil&limit=1; https://open.fda.gov/apis/drug/label/
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [piracetam; Nootropil].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [piracetam; Nootropil].

## MEDIUM piracetam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces unsupported/non-policy sources with trusted sources that support the row facts.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc; https://www.medicines.org.uk/emc/product/101131/pil; https://www.ema.europa.eu/en/documents/psusa/piracetam-list-nationally-authorised-medicinal-products-psusa00002429202204_en.pdf; https://www.ncbi.nlm.nih.gov/mesh/68010889; https://www.ilae.org/index.cfm?objectid=6C4D71BD-EE34-B816-27EB767D97DE334A
- Current: Epilepsy Society ASM list; UK eMC SmPC labeling; FDA/DailyMed labeling
- Proposed: UK eMC SmPC/PIL labeling; EMA PSUSA nationally authorised product list; FDA/openFDA label, Drugs@FDA, and NDC APIs; PubMed/NCBI MeSH and RCT records; ILAE guidance

## CRITICAL piracetam / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: True
- Summary: Updates notes to reflect verified PubMed metadata and the additional relevant placebo-controlled RCT candidate.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9527146/; https://pubmed.ncbi.nlm.nih.gov/8419809/
- Current: PubMed loop 46/65 on 2026-05-15: 1 qualifying placebo-controlled randomized clinical trial report(s) retained from 64 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: PubMed/NCBI audit: Koskiniemi1998 (PMID 9527146) verified as a randomized, double-blind, placebo-controlled crossover piracetam trial in progressive myoclonus epilepsy; Brown1993 (PMID 8419809) is a relevant placebo-controlled randomized crossover piracetam trial in cortical myoclonus to consider for inclusion. RR50/MPC/seizure-freedom differentials are not extractable because outcomes use myoclonus rating scales rather than seizure-frequency endpoints.

## MEDIUM piracetam / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: NCBI MeSH entry terms are missing.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68010889
- Proposed: Pyracetam; Pirazetam; 2-Pyrrolidone-N-Acetamide

## MEDIUM piracetam / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: NCBI MeSH entry terms should be searchable aliases and help avoid duplicate alias rows.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68010889
- Proposed: Nootropil; Nootropyl; Nootrop; Normabrain; UCB-6215; UCB6215; Pyramem

## MEDIUM piracetam / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; FDA/openFDA searches found no label.
- Sources: https://api.fda.gov/drug/label.json?search=piracetam&limit=1; https://api.fda.gov/drug/label.json?search=Nootropil&limit=1; https://open.fda.gov/apis/drug/label/
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM piracetam / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Remove DailyMed from boxed-warning source wording and use FDA/openFDA only.
- Sources: https://api.fda.gov/drug/label.json?search=piracetam&limit=1; https://api.fda.gov/drug/label.json?search=Nootropil&limit=1
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [piracetam; Nootropil].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [piracetam; Nootropil].

## MEDIUM piracetam / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use only trusted-source families actually used for the row; remove DailyMed and unsupported Epilepsy Society citation.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc; https://www.ema.europa.eu/en/documents/psusa/piracetam-list-nationally-authorised-medicinal-products-psusa00002429202204_en.pdf; https://www.ncbi.nlm.nih.gov/mesh/68010889; https://www.ilae.org/index.cfm?objectid=6C4D71BD-EE34-B816-27EB767D97DE334A
- Current: Epilepsy Society ASM list; UK eMC SmPC labeling; FDA/DailyMed labeling
- Proposed: UK eMC SmPC/PIL labeling; EMA PSUSA nationally authorised product list; FDA/openFDA label, Drugs@FDA, and NDC APIs; PubMed/NCBI MeSH and RCT records; ILAE guidance

## CRITICAL piracetam / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Current trusted SmPC supports frequency categories, not exact percentages; diarrhea is listed as frequency not known.
- Sources: https://www.medicines.org.uk/emc/product/101132/smpc
- Current: CNS: hyperkinesia 1.7%, metabolic: weight gain 1.3%, psychiatric: nervousness 1.1%, CNS: somnolence 0.9%, GI: diarrhea 0.8%
- Proposed: CNS: hyperkinesia (common); CNS: somnolence (uncommon); psychiatric: nervousness (common); weight increased (common, investigations); GI: diarrhea/diarrhoea (frequency not known)

## CRITICAL piracetam / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: True
- Summary: eMC and EMA support these formulations; capsule was not supported in reviewed trusted sources.
- Sources: https://www.medicines.org.uk/emc/ingredient/813; https://www.ema.europa.eu/en/documents/psusa/piracetam-list-nationally-authorised-medicinal-products-psusa00002429202204_en.pdf
- Current: Tablet/capsule; oral solution; injection in some markets
- Proposed: Film-coated tablets; oral solution; solution for injection/infusion in some EU markets

## CRITICAL piracetam / proposed_row_update
- Field: filter_formulation
- Status: proposed
- Approval required: True
- Summary: Remove unsupported capsule and overly specific IV/IM wording.
- Sources: https://www.medicines.org.uk/emc/ingredient/813; https://www.ema.europa.eu/en/documents/psusa/piracetam-list-nationally-authorised-medicinal-products-psusa00002429202204_en.pdf
- Current: Capsule; IV/IM injection; Liquid; Tablet
- Proposed: Injection/infusion solution; Liquid/oral solution; Tablet

## MEDIUM piracetam / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: UK SmPC supports 5.0 h, not a 4-5 h range.
- Sources: https://www.medicines.org.uk/emc/product/101132/smpc
- Current: 4-5 h
- Proposed: Approximately 5 h (plasma half-life in young adult men)

## MEDIUM piracetam / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: SmPC supports low CYP inhibition/interaction potential but does not directly establish no induction.
- Sources: https://www.medicines.org.uk/emc/product/101132/smpc
- Current: Not a CYP inducer/inhibitor
- Proposed: No clinically meaningful CYP inhibition expected; metabolic interaction with other drugs is unlikely

## CRITICAL piracetam / proposed_row_update
- Field: filter_mechanism
- Status: proposed
- Approval required: True
- Summary: SmPC says mechanism in cortical myoclonus is unknown; direct GABA classification is misleading.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc
- Current: GABA
- Proposed: Unknown/Other

## MEDIUM piracetam / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: The mechanism source is UK eMC SmPC; EMA source used here is a product-list/formulation source, not a mechanism SmPC.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc
- Current: EMA/UK SmPC
- Proposed: UK SmPC

## MEDIUM piracetam / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: False
- Summary: Use FDA drug-approval terminology and reflect FDA/openFDA findings.
- Sources: https://api.fda.gov/drug/drugsfda.json?search=piracetam&limit=1; https://api.fda.gov/drug/ndc.json?search=generic_name:%22PIRACETAM%22&limit=1
- Current: Not FDA-cleared for epilepsy or not marketed in U.S.
- Proposed: Not FDA-approved for epilepsy; no current FDA/openFDA label, Drugs@FDA record, or NDC listing found for piracetam/Nootropil.

## CRITICAL piracetam / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: Brown1993 is a relevant placebo-controlled randomized crossover piracetam trial in cortical myoclonus, though not phase-tagged; curator review recommended before applying.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9527146/; https://pubmed.ncbi.nlm.nih.gov/8419809/
- Current: Koskiniemi1998|https://pubmed.ncbi.nlm.nih.gov/9527146/
- Proposed: Koskiniemi1998|https://pubmed.ncbi.nlm.nih.gov/9527146/; Brown1993|https://pubmed.ncbi.nlm.nih.gov/8419809/

## MEDIUM piracetam / proposed_row_update
- Field: status_or_notes
- Status: proposed
- Approval required: False
- Summary: Reviewed trusted sources support cortical/progressive myoclonic epilepsy use and nootropic classification, but not the cognitive-indication marketing claim.
- Sources: https://www.medicines.org.uk/emc/product/101131/smpc; https://www.ilae.org/index.cfm?objectid=6C4D71BD-EE34-B816-27EB767D97DE334A
- Current: Used for cortical myoclonus/myoclonic seizures in some jurisdictions; also marketed as nootropic/for cognitive indications in some markets.
- Proposed: Used for cortical myoclonus/progressive myoclonic epilepsies in some jurisdictions; pharmacotherapeutic group: nootropics (ATC N06BX03).

## HIGH potassium bromide / fact_check
- Field: alternate_generic_names
- Status: incorrect
- Approval required: False
- Summary: Kaliumbromid, KBr, kalii bromidum, and kali bromatum are supported synonyms. 'bromide' is broader than potassium bromide and is better kept only as a search alias.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Potassium-Bromide
- Current: bromide; kaliumbromid
- Proposed: kaliumbromid; KBr; kalii bromidum; kali bromatum

## MEDIUM potassium bromide / fact_check
- Field: trade_names
- Status: missing_source
- Approval required: False
- Summary: Kaliumbromid DESITIN is verified from the German Fachinformation. FDA sources verify KBroVet/KBroVet-CA1 as potassium bromide chewable tablets for dogs. DIBRO-BE mono appears plausible but lacks a trusted named source in the current row.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf; https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867
- Current: DIBRO-BE mono; Kaliumbromid DESITIN
- Proposed: DIBRO-BE mono; Kaliumbromid DESITIN; KBroVet; KBroVet-CA1 (veterinary, US)

## HIGH potassium bromide / fact_check
- Field: pubmed_search_aliases
- Status: incorrect
- Approval required: False
- Summary: Add exact chemical abbreviation and newly verified US veterinary brand aliases; retain broad 'bromide' only for search sensitivity.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Potassium-Bromide; https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy
- Current: kaliumbromid; bromide; DIBRO-BE mono; Kaliumbromid DESITIN
- Proposed: potassium bromide; KBr; kaliumbromid; bromide; DIBRO-BE mono; Kaliumbromid DESITIN; KBroVet; KBroVet-CA1

## CRITICAL potassium bromide / fact_check
- Field: available_in_us
- Status: incorrect
- Approval required: True
- Summary: The current wording is too broad after FDA's 2026 full approval of KBroVet for dogs. Human-vs-veterinary scope should be explicit.
- Sources: https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867; https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: No - not available in U.S. for seizure control; German nationally authorized product information identified.
- Proposed: No for FDA-approved human seizure control; however, FDA granted full approval to veterinary KBroVet (potassium bromide chewable tablets) for control of seizures associated with idiopathic epilepsy in dogs on January 21, 2026. German nationally authorized human product information is identified.

## HIGH potassium bromide / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: Bromacne, GI categories, and respiratory events are supported. The CNS '1-10% category' and '0%' respiratory wording are not directly supported and should be removed.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: Dermatologic: bromacne about 25%; CNS: fatigue rare at low bromide levels and more common with higher levels (1-10% category); GI: coated tongue/mouth odor/aphthae/constipation/diarrhea rare (0.01-0.1% category); GI: gastritis/ulcer/pancreatitis very rare (<0.01% category); respiratory: rhinitis/bronchitis/sinusitis frequency not estimable (0% exact percentage unavailable).
- Proposed: Dermatologic: papulopustular skin changes/bromacne very common, about 25%; CNS: fatigue and psychomotor slowing are serum-level related, with fatigue rare at low bromide levels and more frequent at middle/high levels, but exact percentages are not provided; GI: coated tongue, mouth odor, aphthae, constipation, or diarrhea rare (>=0.01% to <0.1%); GI: gastritis, ulcers/perforation, and pancreatitis very rare (<0.01%); Respiratory: serous rhinitis, mucus hypersecretion, bronchitis, sinusitis, and asthma exacerbation can occur, frequency not estimable from available data.

## HIGH potassium bromide / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: The Fachinformation supports no pharmacological interaction with other ASMs, no metabolism, renal excretion, and salt/diuretic effects. It does not specifically state CYP induction/inhibition.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: No pharmacologic interaction with other ASMs described; not a CYP inducer/inhibitor; bromide clearance affected by chloride/salt balance and diuretics.
- Proposed: No pharmacological interactions with other antiseizure medications are described in the German Fachinformation; bromide is not metabolized and is excreted unchanged, mainly renally; bromide levels/half-life are affected by chloride/salt balance and diuretics.

## HIGH potassium bromide / fact_check
- Field: mechanism_source_tier
- Status: incorrect
- Approval required: False
- Summary: The URL is a Desitin German Fachinformation PDF, not EMA or UK eMC/SmPC.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: EMA/UK SmPC
- Proposed: German national Fachinformation / manufacturer product information (not EMA/UK SmPC)

## CRITICAL potassium bromide / fact_check
- Field: year_fda_cleared
- Status: incorrect
- Approval required: True
- Summary: The German authorization date is supported. The broad 'Not FDA-cleared' statement is contradicted in the veterinary context by FDA's 2026 KBroVet full approval, so human/veterinary scope must be explicit.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf; https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867
- Current: Not FDA-cleared; German Kaliumbromid DESITIN authorization 07.01.2019 in Fachinformation.
- Proposed: Not FDA-approved for human seizure control; FDA granted full approval to veterinary KBroVet (potassium bromide chewable tablets) for dogs on January 21, 2026; German Kaliumbromid DESITIN authorization date 07.01.2019.

## HIGH potassium bromide / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be used for the boxed-warning field and the AX powder label is an animal bulk ingredient, not a human antiseizure label. Add FDA veterinary and PubMed sources that support row status/aliases/clinical context. Note that Desitin is not EMA/eMC and is outside the listed trusted domains, although it supports many label-specific German facts.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf; https://pubmed.ncbi.nlm.nih.gov/31111774/; https://pubmed.ncbi.nlm.nih.gov/22430156/; https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867
- Current: Desitin Kaliumbromid DESITIN 850 mg Fachinformation (https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf); FDA/DailyMed labeling
- Proposed: Kaliumbromid DESITIN 850 mg Fachinformation (German national Fachinformation; https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf); PubMed PMID 31111774; PubMed PMID 22430156; FDA CVM KBroVet update (https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy); FDA Animal Drugs@FDA FOI Summary NADA 141-615 (https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867)

## HIGH potassium bromide / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Dog hemp extract study, not potassium bromide epilepsy RCT for this row.
- Sources: https://pubmed.ncbi.nlm.nih.gov/35967998/
- Current: https://pubmed.ncbi.nlm.nih.gov/35967998/
- Proposed: Keep rejected; do not add to pubmed_phase_ii_iii_rct_links.

## HIGH potassium bromide / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Canine medium-chain TAG diet trial, not potassium bromide placebo-controlled RCT.
- Sources: https://pubmed.ncbi.nlm.nih.gov/26337751/
- Current: https://pubmed.ncbi.nlm.nih.gov/26337751/
- Proposed: Keep rejected; do not add to pubmed_phase_ii_iii_rct_links.

## HIGH potassium bromide / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: Potassium bromide/methimazole Graves' disease study, not epilepsy and not placebo-controlled phase II/III ASM evidence.
- Sources: https://pubmed.ncbi.nlm.nih.gov/22186223/
- Current: https://pubmed.ncbi.nlm.nih.gov/22186223/
- Proposed: Keep rejected; do not add to pubmed_phase_ii_iii_rct_links.

## HIGH potassium bromide / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Levetiracetam adjunctive canine epilepsy RCT, not potassium bromide.
- Sources: https://pubmed.ncbi.nlm.nih.gov/22295869/
- Current: https://pubmed.ncbi.nlm.nih.gov/22295869/
- Proposed: Keep rejected; do not add to pubmed_phase_ii_iii_rct_links.

## HIGH potassium bromide / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Asthma study, not epilepsy and not potassium bromide ASM evidence.
- Sources: https://pubmed.ncbi.nlm.nih.gov/21434340/
- Current: https://pubmed.ncbi.nlm.nih.gov/21434340/
- Proposed: Keep rejected; do not add to pubmed_phase_ii_iii_rct_links.

## INFO potassium bromide / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field should remain blank when the differential RCT value is N/A.

## INFO potassium bromide / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field should remain blank when the differential RCT value is N/A.

## INFO potassium bromide / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Plot field should remain blank when the differential RCT value is N/A.

## HIGH potassium bromide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The current source is DailyMed, which is disallowed by the audit rule for boxed-warning verification. FDA sources support veterinary approval for dogs and the FDA FOI summary states the product is not for human use; they do not support a human FDA boxed-warning claim for potassium bromide.
- Sources: https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867; https://www.fda.gov/animal-veterinary/unapproved-animal-drugs/how-can-i-use-fda-online-label-repository-tell-if-drug-legally-marketed
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: Not applicable/no FDA human antiseizure boxed-warning verification: no FDA-approved human potassium bromide antiseizure label was identified; FDA has approved veterinary KBroVet (potassium bromide chewable tablets) for dogs. Do not use DailyMed for this field.

## MEDIUM potassium bromide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is impermissible for this field, and the cited AX product is a bulk ingredient for animal drug compounding rather than a human antiseizure FDA label.
- Sources: https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=c77c8feb-0240-4ea3-9c89-3b972feb0538; published=May 07, 2026; title=POTASSIUM BROMIDE POWDER [AX PHARMACEUTICAL CORP]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=c77c8feb-0240-4ea3-9c89-3b972feb0538
- Proposed: FDA CVM KBroVet update and FDA Animal Drugs@FDA FOI Summary NADA 141-615 for veterinary FDA status; no DailyMed source for boxed-warning verification.

## MEDIUM potassium bromide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace the vague/disallowed DailyMed reference and add trusted FDA/PubMed sources for availability, aliases, and clinical context. Desitin supports many label facts but is not EMA/eMC/UK SmPC.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf; https://pubmed.ncbi.nlm.nih.gov/31111774/; https://pubmed.ncbi.nlm.nih.gov/22430156/; https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867
- Current: Desitin Kaliumbromid DESITIN 850 mg Fachinformation (https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf); FDA/DailyMed labeling
- Proposed: Kaliumbromid DESITIN 850 mg Fachinformation (German national Fachinformation; https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf); PubMed PMID 31111774; PubMed PMID 22430156; FDA CVM KBroVet update; FDA Animal Drugs@FDA FOI Summary NADA 141-615

## MEDIUM potassium bromide / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: Corrects source-tier misclassification.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: EMA/UK SmPC
- Proposed: German national Fachinformation / manufacturer product information (not EMA/UK SmPC)

## MEDIUM potassium bromide / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Use exact synonyms; move broad 'bromide' to search aliases only.
- Sources: https://pubchem.ncbi.nlm.nih.gov/compound/Potassium-Bromide
- Current: bromide; kaliumbromid
- Proposed: kaliumbromid; KBr; kalii bromidum; kali bromatum

## MEDIUM potassium bromide / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: FDA sources verify KBroVet/KBroVet-CA1 as same active ingredient in a US veterinary seizure product; retaining DIBRO-BE mono pending a trusted source avoids unsupported deletion.
- Sources: https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867
- Current: DIBRO-BE mono; Kaliumbromid DESITIN
- Proposed: DIBRO-BE mono; Kaliumbromid DESITIN; KBroVet; KBroVet-CA1 (veterinary, US)

## CRITICAL potassium bromide / proposed_row_update
- Field: available_in_us
- Status: proposed
- Approval required: True
- Summary: Current text is overbroad after 2026 FDA veterinary approval.
- Sources: https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867
- Current: No - not available in U.S. for seizure control; German nationally authorized product information identified.
- Proposed: No for FDA-approved human seizure control; however, FDA granted full approval to veterinary KBroVet (potassium bromide chewable tablets) for control of seizures associated with idiopathic epilepsy in dogs on January 21, 2026. German nationally authorized human product information is identified.

## MEDIUM potassium bromide / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Removes unsupported CNS 1-10% category and confusing 0% respiratory wording.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: Dermatologic: bromacne about 25%; CNS: fatigue rare at low bromide levels and more common with higher levels (1-10% category); GI: coated tongue/mouth odor/aphthae/constipation/diarrhea rare (0.01-0.1% category); GI: gastritis/ulcer/pancreatitis very rare (<0.01% category); respiratory: rhinitis/bronchitis/sinusitis frequency not estimable (0% exact percentage unavailable).
- Proposed: Dermatologic: papulopustular skin changes/bromacne very common, about 25%; CNS: fatigue and psychomotor slowing are serum-level related, with fatigue rare at low bromide levels and more frequent at middle/high levels, but exact percentages are not provided; GI: coated tongue, mouth odor, aphthae, constipation, or diarrhea rare (>=0.01% to <0.1%); GI: gastritis, ulcers/perforation, and pancreatitis very rare (<0.01%); Respiratory: serous rhinitis, mucus hypersecretion, bronchitis, sinusitis, and asthma exacerbation can occur, frequency not estimable from available data.

## MEDIUM potassium bromide / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: CYP-specific statement is not directly supported by the cited source.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: No pharmacologic interaction with other ASMs described; not a CYP inducer/inhibitor; bromide clearance affected by chloride/salt balance and diuretics.
- Proposed: No pharmacological interactions with other antiseizure medications are described in the German Fachinformation; bromide is not metabolized and is excreted unchanged, mainly renally; bromide levels/half-life are affected by chloride/salt balance and diuretics.

## MEDIUM potassium bromide / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: False
- Summary: The mechanism source is a German Desitin Fachinformation PDF, not EMA/eMC/UK SmPC.
- Sources: https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: EMA/UK SmPC
- Proposed: German national Fachinformation / manufacturer product information (not EMA/UK SmPC)

## CRITICAL potassium bromide / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: True
- Summary: Clarifies human versus veterinary FDA approval status and preserves German authorization date.
- Sources: https://www.fda.gov/animal-veterinary/cvm-updates/fda-grants-full-approval-drug-control-seizures-dogs-idiopathic-epilepsy; https://animaldrugsatfda.fda.gov/adafda/app/search/public/document/downloadFoi/17867; https://www.desitin.de/wp-content/uploads/2020/01/Kaliumbromid-DESITIN-850-mg-Tabletten.pdf
- Current: Not FDA-cleared; German Kaliumbromid DESITIN authorization 07.01.2019 in Fachinformation.
- Proposed: Not FDA-approved for human seizure control; FDA granted full approval to veterinary KBroVet (potassium bromide chewable tablets) for dogs on January 21, 2026; German Kaliumbromid DESITIN authorization date 07.01.2019.

## CRITICAL pregabalin / fact_check
- Field: year_fda_cleared
- Status: incorrect
- Approval required: True
- Summary: FDA labeling states Initial U.S. Approval: 2004, and the original approval letter is dated December 30, 2004. The row value 2005 is not supported as the initial FDA approval year.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2004/021446_Lyrica%20Capsules_approv.PDF
- Current: 2005
- Proposed: 2004

## CRITICAL pregabalin / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: The row incorrectly includes Inducer. FDA labeling says pregabalin does not inhibit major CYP enzymes and does not induce CYP1A2 or CYP3A4 activity.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf
- Current: Inducer; No major enzyme effect
- Proposed: No major enzyme effect

## CRITICAL pregabalin / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The current values mix unsupported dose/indication strata. FDA Table 5 for controlled adult adjunctive partial-onset seizure trials gives the all-pregabalin rates listed in the proposed value.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf
- Current: CNS: dizziness 29%, CNS: somnolence 22%, neurologic: ataxia 13%, ophthalmologic: blurred vision 6%, metabolic: weight gain 5%, peripheral: edema 6%
- Proposed: CNS: dizziness 32%, CNS: somnolence 22%, neurologic: ataxia 15%, ophthalmologic: blurred vision 10%, metabolic: weight gain 12%, peripheral: edema 5%

## CRITICAL pregabalin / fact_check
- Field: qt_interval_effect
- Status: incorrect
- Approval required: True
- Summary: The eMC SmPC lists QT prolongation as a rare cardiac adverse reaction, so the current 'No known meaningful QT effect' wording is too absolute.
- Sources: https://www.medicines.org.uk/emc/product/1757/smpc; https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: Rare QT prolongation reported in SmPC; no quantified clinically meaningful QTc effect established from FDA labeling reviewed.

## CRITICAL pregabalin / fact_check
- Field: filter_qt_effect
- Status: incorrect
- Approval required: True
- Summary: The filter should reflect the SmPC-listed rare QT prolongation rather than categorizing pregabalin as having no known QT effect.
- Sources: https://www.medicines.org.uk/emc/product/1757/smpc
- Current: No known meaningful QT effect
- Proposed: QT prolongation reported/rare

## HIGH pregabalin / fact_check
- Field: trade_names
- Status: missing
- Approval required: False
- Summary: Alzain and Lyrica are verified. Lyrica CR is an FDA-labeled pregabalin extended-release product, and Misabri PR is an eMC-listed pregabalin prolonged-release product. Do not add 'PREGABALIN' as a trade name because it is the generic name, not a distinct trade name.
- Sources: https://www.medicines.org.uk/emc/product/1757/smpc; https://www.ema.europa.eu/en/medicines/human/EPAR/lyrica; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209501s005lbl.pdf; https://www.medicines.org.uk/emc/product/100373/smpc
- Current: Alzain; Lyrica
- Proposed: Alzain; Lyrica; Lyrica CR; Misabri PR

## MEDIUM pregabalin / fact_check
- Field: pubmed_search_aliases
- Status: missing_source
- Approval required: False
- Summary: The alias is plausible as a development/search alias, but the row's named evidence sources do not specifically support it.
- Current: CI-1008
- Proposed: CI-1008

## HIGH pregabalin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_placebo_rct
- Approval required: True
- Summary: The title and outcome audit identify this as a historical-controlled pregabalin monotherapy trial, not a concurrent placebo-controlled RCT; it cannot support drug-minus-placebo outcome differentials.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24415567/
- Current: https://pubmed.ncbi.nlm.nih.gov/24415567/
- Proposed: Remove from pubmed_phase_ii_iii_rct_links or move to a non-placebo/historical-control notes field.

## CRITICAL pregabalin / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: Mann2020 reports a 35% placebo-relative reduction in log-transformed video-EEG seizure rate, not a median percent-change differential. The remaining entries are supported as active-minus-placebo median percent-change/seizure-frequency reduction differentials.
- Sources: https://pubmed.ncbi.nlm.nih.gov/32189338/; https://pubmed.ncbi.nlm.nih.gov/30688135/; https://pubmed.ncbi.nlm.nih.gov/20696552/; https://pubmed.ncbi.nlm.nih.gov/16393158/; https://pubmed.ncbi.nlm.nih.gov/15699378/; https://pubmed.ncbi.nlm.nih.gov/14692903/; https://pubmed.ncbi.nlm.nih.gov/12771254/
- Current: Mann2020|35|https://pubmed.ncbi.nlm.nih.gov/32189338/|175; Antinew2019|19.9|https://pubmed.ncbi.nlm.nih.gov/30688135/|295; Baulac2010|20|https://pubmed.ncbi.nlm.nih.gov/20696552/|434; Elger2005|38.7|https://pubmed.ncbi.nlm.nih.gov/16393158/|341; Beydoun2005|54|https://pubmed.ncbi.nlm.nih.gov/15699378/|312; Arroyo2004|49.6|https://pubmed.ncbi.nlm.nih.gov/14692903/|287; French2003|47|https://pubmed.ncbi.nlm.nih.gov/12771254/|453
- Proposed: Antinew2019|19.9|https://pubmed.ncbi.nlm.nih.gov/30688135/|295; Baulac2010|20|https://pubmed.ncbi.nlm.nih.gov/20696552/|434; Elger2005|38.7|https://pubmed.ncbi.nlm.nih.gov/16393158/|341; Beydoun2005|54|https://pubmed.ncbi.nlm.nih.gov/15699378/|312; Arroyo2004|49.6|https://pubmed.ncbi.nlm.nih.gov/14692903/|287; French2003|47|https://pubmed.ncbi.nlm.nih.gov/12771254/|453

## CRITICAL pregabalin / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: The range remains 19.9-54 after removing Mann2020 from the MPC rollup. Mann2020's 35% is a different modeled endpoint and should not be labeled median percent change.
- Sources: https://pubmed.ncbi.nlm.nih.gov/32189338/; https://pubmed.ncbi.nlm.nih.gov/30688135/; https://pubmed.ncbi.nlm.nih.gov/20696552/; https://pubmed.ncbi.nlm.nih.gov/16393158/; https://pubmed.ncbi.nlm.nih.gov/15699378/; https://pubmed.ncbi.nlm.nih.gov/14692903/; https://pubmed.ncbi.nlm.nih.gov/12771254/
- Current: 19.9-54 % (drug minus placebo MPC differential at maximum effective dose/regimen: Mann2020 pregabalin 14 mg/kg/day 35%; Antinew2019 pregabalin 10 mg/kg/day or 14 mg/kg/day if <30 kg 19.9%; Baulac2010 pregabalin up to 600 mg/day 20%; Elger2005 pregabalin 600 mg/day BID fixed dose 38.7%; Beydoun2005 pregabalin 600 mg/day TID 54%; Arroyo2004 pregabalin 600 mg/day TID 49.6%; French2003 pregabalin 600 mg/day BID 47%)
- Proposed: 19.9-54 % (drug minus placebo MPC differential at maximum effective dose/regimen: Antinew2019 pregabalin 10 mg/kg/day or 14 mg/kg/day if <30 kg 19.9%; Baulac2010 pregabalin up to 600 mg/day 20%; Elger2005 pregabalin 600 mg/day BID fixed dose 38.7%; Beydoun2005 pregabalin 600 mg/day TID 54%; Arroyo2004 pregabalin 600 mg/day TID 49.6%; French2003 pregabalin 600 mg/day BID 47%). Note: Mann2020 reported a 35% placebo-relative reduction in log-transformed video-EEG seizure rate, not an MPC differential.

## HIGH pregabalin / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supportable only with FDA/openFDA or FDA label sources. The current wording and source rely on DailyMed, which is not permissible for this field.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209501s005lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM pregabalin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use named trusted sources that directly support row facts; remove non-trusted/nonspecific list sources for this audit policy and avoid DailyMed for boxed-warning verification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5; https://www.ncbi.nlm.nih.gov/books/n/livertox/Pregabalin/; https://www.ncbi.nlm.nih.gov/books/NBK548365/table/Anticonvulsants.Tc/; https://www.ema.europa.eu/en/medicines/human/EPAR/lyrica; https://www.medicines.org.uk/emc/product/1757/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling; FDA/openFDA labeling; FDA Drugs@FDA approval documents; PubMed RCT abstracts; ClinicalTrials.gov trial records; NCBI LiverTox pregabalin page and anticonvulsants table; EMA EPAR/eMC SmPC

## MEDIUM pregabalin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism text is supported by FDA label text; DailyMed is unnecessary and not in the trusted-source list supplied for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM pregabalin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: FDA boxed-warning verification must use FDA/openFDA, FDA labels, or Drugs@FDA; DailyMed is not permissible for this field.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=f280bbd8-2af2-444a-bd96-e409337ca6dd; published=Apr 15, 2026; title=LYRICA CR (PREGABALIN) TABLET, FILM COATED, EXTENDED RELEASE [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f280bbd8-2af2-444a-bd96-e409337ca6dd
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=f280bbd8-2af2-444a-bd96-e409337ca6dd; effective_time=20260312; title=Lyrica CR / PREGABALIN; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5

## CRITICAL pregabalin / proposed_row_update
- Field: year_fda_cleared
- Status: proposed
- Approval required: True
- Summary: FDA label and original approval documentation support Initial U.S. Approval in 2004, not 2005.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/nda/2004/021446_Lyrica%20Capsules_approv.PDF
- Current: 2005
- Proposed: 2004

## CRITICAL pregabalin / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Use a single FDA-supported adverse-event stratum: all pregabalin-treated patients in controlled adult adjunctive partial-onset seizure trials.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf
- Current: CNS: dizziness 29%, CNS: somnolence 22%, neurologic: ataxia 13%, ophthalmologic: blurred vision 6%, metabolic: weight gain 5%, peripheral: edema 6%
- Proposed: CNS: dizziness 32%, CNS: somnolence 22%, neurologic: ataxia 15%, ophthalmologic: blurred vision 10%, metabolic: weight gain 12%, peripheral: edema 5%

## CRITICAL pregabalin / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: Pregabalin is not a CYP enzyme inducer in FDA labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf
- Current: Inducer; No major enzyme effect
- Proposed: No major enzyme effect

## CRITICAL pregabalin / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: True
- Summary: eMC SmPC lists QT prolongation as a rare cardiac adverse reaction.
- Sources: https://www.medicines.org.uk/emc/product/1757/smpc
- Current: No clinically meaningful QT effect established
- Proposed: Rare QT prolongation reported in SmPC; no quantified clinically meaningful QTc effect established from FDA labeling reviewed.

## CRITICAL pregabalin / proposed_row_update
- Field: filter_qt_effect
- Status: proposed
- Approval required: True
- Summary: The existing filter is too absolute in light of SmPC-listed rare QT prolongation.
- Sources: https://www.medicines.org.uk/emc/product/1757/smpc
- Current: No known meaningful QT effect
- Proposed: QT prolongation reported/rare

## MEDIUM pregabalin / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Adds verified pregabalin brand/formulation names and avoids treating aliases as separate drugs. Do not add PREGABALIN as a trade name.
- Sources: https://www.medicines.org.uk/emc/product/1757/smpc; https://www.ema.europa.eu/en/medicines/human/EPAR/lyrica; https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/209501s005lbl.pdf; https://www.medicines.org.uk/emc/product/100373/smpc
- Current: Alzain; Lyrica
- Proposed: Alzain; Lyrica; Lyrica CR; Misabri PR

## MEDIUM pregabalin / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; use FDA/openFDA wording.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM pregabalin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replaces the nonpermissible DailyMed boxed-warning source with FDA/openFDA metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=f280bbd8-2af2-444a-bd96-e409337ca6dd; published=Apr 15, 2026; title=LYRICA CR (PREGABALIN) TABLET, FILM COATED, EXTENDED RELEASE [VIATRIS SPECIALTY LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=f280bbd8-2af2-444a-bd96-e409337ca6dd
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=f280bbd8-2af2-444a-bd96-e409337ca6dd; effective_time=20260312; title=Lyrica CR / PREGABALIN; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5

## MEDIUM pregabalin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The mechanism is supported by FDA label text; cite FDA/accessdata rather than DailyMed under the row's trusted-source policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling

## MEDIUM pregabalin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current row sources include non-trusted or nonspecific sources for this audit policy, and DailyMed should not be used for the FDA boxed-warning field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2016/021446s030%2C022488s010lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22f280bbd8-2af2-444a-bd96-e409337ca6dd%22&limit=5; https://www.ncbi.nlm.nih.gov/books/n/livertox/Pregabalin/; https://www.ncbi.nlm.nih.gov/books/NBK548365/table/Anticonvulsants.Tc/; https://www.ema.europa.eu/en/medicines/human/EPAR/lyrica; https://www.medicines.org.uk/emc/product/1757/smpc
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/accessdata labeling; FDA/openFDA labeling; FDA Drugs@FDA approval documents; PubMed RCT abstracts; ClinicalTrials.gov trial records; NCBI LiverTox pregabalin page and anticonvulsants table; EMA EPAR/eMC SmPC

## CRITICAL pregabalin / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: French2014 is a historical-controlled monotherapy trial and does not have a concurrent placebo arm, so it should not be retained in a placebo-controlled RCT link field.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24415567/
- Current: Driscoll2021|https://pubmed.ncbi.nlm.nih.gov/34033265/; Mann2020|https://pubmed.ncbi.nlm.nih.gov/32189338/; Antinew2019|https://pubmed.ncbi.nlm.nih.gov/30688135/; French2014b|https://pubmed.ncbi.nlm.nih.gov/24962242/; French2014|https://pubmed.ncbi.nlm.nih.gov/24415567/; Baulac2010|https://pubmed.ncbi.nlm.nih.gov/20696552/; Lee2009|https://pubmed.ncbi.nlm.nih.gov/19222545/; Elger2005|https://pubmed.ncbi.nlm.nih.gov/16393158/; Beydoun2005|https://pubmed.ncbi.nlm.nih.gov/15699378/; Arroyo2004|https://pubmed.ncbi.nlm.nih.gov/14692903/; French2003|https://pubmed.ncbi.nlm.nih.gov/12771254/
- Proposed: Driscoll2021|https://pubmed.ncbi.nlm.nih.gov/34033265/; Mann2020|https://pubmed.ncbi.nlm.nih.gov/32189338/; Antinew2019|https://pubmed.ncbi.nlm.nih.gov/30688135/; French2014b|https://pubmed.ncbi.nlm.nih.gov/24962242/; Baulac2010|https://pubmed.ncbi.nlm.nih.gov/20696552/; Lee2009|https://pubmed.ncbi.nlm.nih.gov/19222545/; Elger2005|https://pubmed.ncbi.nlm.nih.gov/16393158/; Beydoun2005|https://pubmed.ncbi.nlm.nih.gov/15699378/; Arroyo2004|https://pubmed.ncbi.nlm.nih.gov/14692903/; French2003|https://pubmed.ncbi.nlm.nih.gov/12771254/

## CRITICAL pregabalin / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Mann2020's endpoint is not a median percent-change differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/32189338/
- Current: 19.9-54 % (drug minus placebo MPC differential at maximum effective dose/regimen: Mann2020 pregabalin 14 mg/kg/day 35%; Antinew2019 pregabalin 10 mg/kg/day or 14 mg/kg/day if <30 kg 19.9%; Baulac2010 pregabalin up to 600 mg/day 20%; Elger2005 pregabalin 600 mg/day BID fixed dose 38.7%; Beydoun2005 pregabalin 600 mg/day TID 54%; Arroyo2004 pregabalin 600 mg/day TID 49.6%; French2003 pregabalin 600 mg/day BID 47%)
- Proposed: 19.9-54 % (drug minus placebo MPC differential at maximum effective dose/regimen: Antinew2019 pregabalin 10 mg/kg/day or 14 mg/kg/day if <30 kg 19.9%; Baulac2010 pregabalin up to 600 mg/day 20%; Elger2005 pregabalin 600 mg/day BID fixed dose 38.7%; Beydoun2005 pregabalin 600 mg/day TID 54%; Arroyo2004 pregabalin 600 mg/day TID 49.6%; French2003 pregabalin 600 mg/day BID 47%). Note: Mann2020 reported a 35% placebo-relative reduction in log-transformed video-EEG seizure rate, not an MPC differential.

## CRITICAL pregabalin / proposed_row_update
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: True
- Summary: Remove Mann2020 from the median percent-change plot because its 35% value is a different endpoint type.
- Sources: https://pubmed.ncbi.nlm.nih.gov/32189338/
- Current: Mann2020|35|https://pubmed.ncbi.nlm.nih.gov/32189338/|175; Antinew2019|19.9|https://pubmed.ncbi.nlm.nih.gov/30688135/|295; Baulac2010|20|https://pubmed.ncbi.nlm.nih.gov/20696552/|434; Elger2005|38.7|https://pubmed.ncbi.nlm.nih.gov/16393158/|341; Beydoun2005|54|https://pubmed.ncbi.nlm.nih.gov/15699378/|312; Arroyo2004|49.6|https://pubmed.ncbi.nlm.nih.gov/14692903/|287; French2003|47|https://pubmed.ncbi.nlm.nih.gov/12771254/|453
- Proposed: Antinew2019|19.9|https://pubmed.ncbi.nlm.nih.gov/30688135/|295; Baulac2010|20|https://pubmed.ncbi.nlm.nih.gov/20696552/|434; Elger2005|38.7|https://pubmed.ncbi.nlm.nih.gov/16393158/|341; Beydoun2005|54|https://pubmed.ncbi.nlm.nih.gov/15699378/|312; Arroyo2004|49.6|https://pubmed.ncbi.nlm.nih.gov/14692903/|287; French2003|47|https://pubmed.ncbi.nlm.nih.gov/12771254/|453

## HIGH primidone / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: The adverse reaction list is supported by the FDA label, but the '0%' wording is not supported and could be misread as an incidence value.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/009170Orig1s040lbl.pdf
- Current: N/A 0%: FDA label lists ataxia, vertigo, nausea, anorexia, vomiting, fatigue, hyperirritability, emotional disturbances, sexual impotency, diplopia, nystagmus, drowsiness, skin eruptions, granulocytopenia, agranulocytosis, red-cell hypoplasia/aplasia, and megaloblastic anemia without quantified incidence percentages.
- Proposed: N/A: FDA label lists ataxia, vertigo, nausea, anorexia, vomiting, fatigue, hyperirritability, emotional disturbances, sexual impotency, diplopia, nystagmus, drowsiness, morbilliform skin eruptions, granulocytopenia, agranulocytosis, red-cell hypoplasia/aplasia, and megaloblastic anemia without quantified incidence percentages.

## HIGH primidone / fact_check
- Field: trade_names
- Status: missing
- Approval required: False
- Summary: Mysoline and Primidone/generic product names are supported by FDA sources. NCBI LiverTox also lists Myidone, Sertan, and Apo-Primidone as brand names, so the current alias list is incomplete.
- Sources: https://www.fda.gov/media/71494/download?attachment=; https://www.ncbi.nlm.nih.gov/books/NBK548512/
- Current: Mysoline; Primidone
- Proposed: Mysoline; Myidone; Sertan; Apo-Primidone; Primidone (generic product name)

## HIGH primidone / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Mysoline is supported; additional brand aliases listed by NCBI should be included to avoid duplicate-name misses in literature searches.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/
- Current: Mysoline
- Proposed: Mysoline; Myidone; Sertan; Apo-Primidone

## HIGH primidone / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: False
- Summary: The FDA label may omit half-life, but trusted NCBI StatPearls provides a primidone half-life of approximately 10-15 hours.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: N/A - selected FDA/DailyMed label does not provide a half-life value.
- Proposed: 10-15 hours for primidone; may increase in patients older than 75 years.

## CRITICAL primidone / fact_check
- Field: major_organ_for_metabolism
- Status: incorrect
- Approval required: True
- Summary: NCBI LiverTox states primidone is extensively metabolized by the liver; StatPearls identifies phenobarbital and PEMA formation and unchanged urinary excretion.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: N/A - selected FDA/DailyMed label does not identify a major metabolic organ; label identifies phenobarbital and PEMA metabolites.
- Proposed: Liver; primidone is extensively metabolized by the liver to phenobarbital and PEMA, with substantial unchanged urinary excretion.

## CRITICAL primidone / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: True
- Summary: The source-limited FDA-label statement misses a clinically meaningful enzyme-induction fact supported by NCBI sources.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: N/A - selected FDA label does not define clinically meaningful enzyme induction or inhibition.
- Proposed: Enzyme inducer: NCBI LiverTox states primidone can induce CYP450 enzyme activities; StatPearls notes hepatic metabolism and phenobarbital-related induction of UGT/CYP2C/CYP3A pathways.

## CRITICAL primidone / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: NCBI sources support clinically meaningful enzyme induction, so the filter should not remain unknown/limited.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: Unknown/limited
- Proposed: Enzyme inducer

## CRITICAL primidone / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: True
- Summary: NCBI sources identify liver metabolism and unchanged urinary excretion.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: Limited/unknown
- Proposed: Hepatic; renal excretion of unchanged drug

## MEDIUM primidone / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification; accessdata FDA label is permissible.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/009170Orig1s040lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=af593171-dabb-4ea3-b44c-89ed457b2c46; published=Aug 12, 2020; title=MYSOLINE (PRIMIDONE) TABLET [BAUSCH HEALTH US, LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=af593171-dabb-4ea3-b44c-89ed457b2c46
- Proposed: FDA-approved label (Drugs@FDA/accessdata); status=no_boxed_warning_identified_in_fda_label; NDA=009170/S-040; label=2020/009170Orig1s040lbl.pdf; checked=2026-05-21; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/009170Orig1s040lbl.pdf

## MEDIUM primidone / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: DailyMed is outside the provided trusted-source list, and NCBI/PubMed sources are needed for half-life, metabolism, enzyme effects, aliases, and RCT absence checks.
- Sources: https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.fda.gov/media/71494/download?attachment=; https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/009170Orig1s040lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK562297/; https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://pubmed.ncbi.nlm.nih.gov/?term=primidone+placebo+controlled+randomized+epilepsy
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book / March 2026 Approved Drug Product List; FDA-approved Mysoline label (Drugs@FDA/accessdata, NDA 009170/S-040); NCBI Bookshelf StatPearls Primidone; NCBI LiverTox Primidone; PubMed search/audit for primidone epilepsy RCTs

## MEDIUM primidone / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism text is supported by FDA labeling, but the named source should point to an FDA/accessdata label rather than DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/009170Orig1s040lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA-approved Mysoline label (Drugs@FDA/accessdata, NDA 009170/S-040)

## MEDIUM primidone / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Remove unsupported '0%' wording while retaining FDA-label adverse reaction facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/009170Orig1s040lbl.pdf
- Current: N/A 0%: FDA label lists ataxia, vertigo, nausea, anorexia, vomiting, fatigue, hyperirritability, emotional disturbances, sexual impotency, diplopia, nystagmus, drowsiness, skin eruptions, granulocytopenia, agranulocytosis, red-cell hypoplasia/aplasia, and megaloblastic anemia without quantified incidence percentages.
- Proposed: N/A: FDA label lists ataxia, vertigo, nausea, anorexia, vomiting, fatigue, hyperirritability, emotional disturbances, sexual impotency, diplopia, nystagmus, drowsiness, morbilliform skin eruptions, granulocytopenia, agranulocytosis, red-cell hypoplasia/aplasia, and megaloblastic anemia without quantified incidence percentages.

## MEDIUM primidone / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: False
- Summary: Trusted NCBI source provides a half-life value.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: N/A - selected FDA/DailyMed label does not provide a half-life value.
- Proposed: 10-15 hours for primidone; may increase in patients older than 75 years.

## CRITICAL primidone / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: True
- Summary: Trusted NCBI sources contradict the limited/unknown metabolism wording.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: N/A - selected FDA/DailyMed label does not identify a major metabolic organ; label identifies phenobarbital and PEMA metabolites.
- Proposed: Liver; primidone is extensively metabolized by the liver to phenobarbital and PEMA, with substantial unchanged urinary excretion.

## CRITICAL primidone / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: True
- Summary: Trusted NCBI sources support enzyme induction.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: N/A - selected FDA label does not define clinically meaningful enzyme induction or inhibition.
- Proposed: Enzyme inducer: NCBI LiverTox states primidone can induce CYP450 enzyme activities; StatPearls notes hepatic metabolism and phenobarbital-related induction of UGT/CYP2C/CYP3A pathways.

## CRITICAL primidone / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: Align filter with NCBI-supported induction evidence.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: Unknown/limited
- Proposed: Enzyme inducer

## CRITICAL primidone / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: True
- Summary: Align filter with NCBI-supported metabolism and excretion evidence.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/; https://www.ncbi.nlm.nih.gov/books/NBK562297/
- Current: Limited/unknown
- Proposed: Hepatic; renal excretion of unchanged drug

## MEDIUM primidone / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Add NCBI-listed brand aliases and clarify Primidone as generic product name.
- Sources: https://www.fda.gov/media/71494/download?attachment=; https://www.ncbi.nlm.nih.gov/books/NBK548512/
- Current: Mysoline; Primidone
- Proposed: Mysoline; Myidone; Sertan; Apo-Primidone; Primidone (generic product name)

## MEDIUM primidone / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add source-supported aliases for literature search coverage.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK548512/
- Current: Mysoline
- Proposed: Mysoline; Myidone; Sertan; Apo-Primidone

## MEDIUM primidone / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Fact is confirmed, but wording should cite FDA/accessdata rather than DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/009170Orig1s040lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in FDA-approved Mysoline (primidone) label (NDA 009170/S-040).

## MEDIUM primidone / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Refresh date to the FDA-source verification date for this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2020/009170Orig1s040lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## HIGH progabide / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: Important aliases/development codes are missing. NLM MeSH lists SL 76002 as an entry term; PubChem lists Halogabide and related SL code variants.
- Sources: https://meshb.nlm.nih.gov/record/ui?ui=C017985; https://pubchem.ncbi.nlm.nih.gov/compound/44115
- Proposed: halogabide; SL 76002; SL-76002; SL-76.002

## HIGH progabide / fact_check
- Field: trade_names
- Status: missing
- Approval required: False
- Summary: Gabrene is verified. PubChem also lists Gabren as a synonym; if the CSV treats brand/trade synonyms broadly, add Gabren to prevent duplicate-row creation under that alias.
- Sources: https://meshb.nlm.nih.gov/record/ui?ui=C017985; https://pubchem.ncbi.nlm.nih.gov/compound/44115
- Current: Gabrene
- Proposed: Gabrene; Gabren

## HIGH progabide / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Search aliases should include trade names and development-code aliases seen in NLM MeSH/PubChem so the same drug is not missed or duplicated.
- Sources: https://meshb.nlm.nih.gov/record/ui?ui=C017985; https://pubchem.ncbi.nlm.nih.gov/compound/44115
- Proposed: Gabrene; Gabren; halogabide; SL 76002; SL-76002; SL-76.002

## MEDIUM progabide / fact_check
- Field: available_in_us
- Status: missing_source
- Approval required: True
- Summary: No current FDA/openFDA label was identified, supporting non-US availability. The exact French authorization/revocation statement is plausible from the row bundle but lacks an allowed-domain source in this audit.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-database
- Current: No - formerly authorized in France; authorization revoked/withdrawn
- Proposed: No - not FDA-approved/currently marketed in the US; historical French authorization/revocation requires ANSM source verification if retained.

## MEDIUM progabide / fact_check
- Field: year_fda_cleared
- Status: missing_source
- Approval required: True
- Summary: The FDA portion is supported by no FDA/openFDA label. The exact French dates are not verifiable from the allowed source domains supplied for this audit.
- Sources: https://open.fda.gov/apis/drug/label/; https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-database
- Current: Not FDA-cleared; ANSM France authorization 19/04/1984, revoked 21/07/2014
- Proposed: Not FDA-cleared/approved; retain the French authorization/revocation dates only with the cited ANSM/public medicines-directory source.

## HIGH progabide / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: The Martinez-Lage RCT reports adverse-event counts during treatment periods, so '0% usable quantified current data' is misleading if read as no RCT safety counts. However, these data are small historical crossover counts, not current FDA-label percentages.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6383790/; https://pubmed.ncbi.nlm.nih.gov/6403342/; https://pubmed.ncbi.nlm.nih.gov/3098923/
- Current: Evidence availability: no reliable FDA/RCT symptom percentages found (0% usable quantified current data located)
- Proposed: Evidence availability: limited historical RCT adverse-event counts exist, but no current FDA-label or harmonized placebo-adjusted symptom-percentage table was identified.

## HIGH progabide / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed should not be cited for FDA boxed-warning verification. The row also uses PubMed RCT evidence and should name it. Exact ANSM date facts remain source-limited under this audit's allowed-domain list.
- Sources: https://open.fda.gov/apis/drug/label/; https://pubmed.ncbi.nlm.nih.gov/6121050/; https://pubmed.ncbi.nlm.nih.gov/6383790/; https://pubmed.ncbi.nlm.nih.gov/6357772/; https://pubmed.ncbi.nlm.nih.gov/6403342/
- Current: NCBI PubChem pharmacology records; FDA/DailyMed labeling; ANSM French medicines directory
- Proposed: NCBI/PubMed and NCBI PubChem pharmacology records; FDA/openFDA labeling; PubMed placebo-controlled trial reports; ANSM French medicines directory for French authorization facts only if an allowed source URL is retained.

## HIGH progabide / fact_check
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: DailyMed wording violates the audit rule for boxed warnings. Use FDA/openFDA only.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=progabide&limit=1; https://api.fda.gov/drug/label.json?search=Gabrene&limit=1
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## HIGH progabide / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: Source wording should use FDA/openFDA and include key aliases. DailyMed is not permissible for this field.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=progabide&limit=1; https://api.fda.gov/drug/label.json?search=Gabrene&limit=1
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [progabide; Gabrene].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [progabide; Gabrene; Gabren; SL 76002].

## MEDIUM progabide / fact_check
- Field: status_or_notes
- Status: missing_source
- Approval required: True
- Summary: GABA-ergic mechanism and Gabrene alias are supported. The French authorization/revocation statement needs the specific ANSM source, which is outside the allowed-domain list supplied for this audit.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6121050/; https://meshb.nlm.nih.gov/record/ui?ui=C017985
- Current: Former French-authorized GABA-ergic anticonvulsant (Gabrene); ANSM authorization later revoked/withdrawn.
- Proposed: Former French-authorized GABA-ergic anticonvulsant (Gabrene); ANSM authorization later revoked/withdrawn. Exact French authorization details require the ANSM/public medicines-directory source URL.

## INFO progabide / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Blank plotting field is consistent with NR/not-extractable RR50 differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6383790/; https://pubmed.ncbi.nlm.nih.gov/6357772/; https://pubmed.ncbi.nlm.nih.gov/6403342/

## INFO progabide / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Blank plotting field is consistent with NR/not-extractable MPC differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6383790/; https://pubmed.ncbi.nlm.nih.gov/6357772/; https://pubmed.ncbi.nlm.nih.gov/6403342/

## INFO progabide / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: Blank plotting field is consistent with NR/not-extractable seizure-freedom differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6383790/; https://pubmed.ncbi.nlm.nih.gov/6357772/; https://pubmed.ncbi.nlm.nih.gov/6403342/

## HIGH progabide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The substantive finding of no current FDA label is consistent with the FDA/openFDA no-label result supplied in the row bundle, but DailyMed is not permissible for boxed-warning verification. Use FDA/openFDA wording only.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=progabide&limit=1; https://api.fda.gov/drug/label.json?search=Gabrene&limit=1; https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-database
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM progabide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not an allowed source for boxed-warning verification; FDA/openFDA is allowed.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=progabide&limit=1; https://api.fda.gov/drug/label.json?search=Gabrene&limit=1
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [progabide; Gabrene].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [progabide; Gabrene; Gabren; SL 76002].

## MEDIUM progabide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Correct FDA source wording and add PubMed RCT/outcome support. French authorization facts still need a specific acceptable source decision.
- Sources: https://open.fda.gov/apis/drug/label/; https://pubmed.ncbi.nlm.nih.gov/6121050/; https://pubmed.ncbi.nlm.nih.gov/6383790/; https://pubmed.ncbi.nlm.nih.gov/6357772/; https://pubmed.ncbi.nlm.nih.gov/6403342/
- Current: NCBI PubChem pharmacology records; FDA/DailyMed labeling; ANSM French medicines directory
- Proposed: NCBI/PubMed and NCBI PubChem pharmacology records; FDA/openFDA labeling; PubMed placebo-controlled trial reports; ANSM French medicines directory for French authorization facts only if an allowed source URL is retained.

## MEDIUM progabide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Primary PubMed pharmacology evidence better supports the mechanism cell.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6121050/; https://pubchem.ncbi.nlm.nih.gov/compound/44115
- Current: NCBI PubChem pharmacology records
- Proposed: NCBI PubChem pharmacology records; PubMed Lloyd 1982 GABA receptor pharmacology study

## MEDIUM progabide / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Important aliases/development codes are missing.
- Sources: https://meshb.nlm.nih.gov/record/ui?ui=C017985; https://pubchem.ncbi.nlm.nih.gov/compound/44115
- Proposed: halogabide; SL 76002; SL-76002; SL-76.002

## MEDIUM progabide / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Gabrene is verified; Gabren is also listed as a synonym/brand-like alias in NCBI/PubChem records.
- Sources: https://meshb.nlm.nih.gov/record/ui?ui=C017985; https://pubchem.ncbi.nlm.nih.gov/compound/44115
- Current: Gabrene
- Proposed: Gabrene; Gabren

## MEDIUM progabide / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add search aliases to prevent duplicate rows and improve PubMed retrieval.
- Sources: https://meshb.nlm.nih.gov/record/ui?ui=C017985; https://pubchem.ncbi.nlm.nih.gov/compound/44115
- Proposed: Gabrene; Gabren; halogabide; SL 76002; SL-76002; SL-76.002

## MEDIUM progabide / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=progabide&limit=1; https://api.fda.gov/drug/label.json?search=Gabrene&limit=1
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM progabide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Use FDA/openFDA source wording and include key aliases.
- Sources: https://open.fda.gov/apis/drug/label/; https://api.fda.gov/drug/label.json?search=progabide&limit=1; https://api.fda.gov/drug/label.json?search=Gabrene&limit=1
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [progabide; Gabrene].
- Proposed: FDA/openFDA label API search on 05-20-2026: no current FDA label found for terms [progabide; Gabrene; Gabren; SL 76002].

## MEDIUM progabide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed with FDA/openFDA and name PubMed RCT evidence. French authorization facts remain source-limited under the allowed-domain list.
- Sources: https://open.fda.gov/apis/drug/label/; https://pubmed.ncbi.nlm.nih.gov/6121050/; https://pubmed.ncbi.nlm.nih.gov/6383790/; https://pubmed.ncbi.nlm.nih.gov/6357772/; https://pubmed.ncbi.nlm.nih.gov/6403342/
- Current: NCBI PubChem pharmacology records; FDA/DailyMed labeling; ANSM French medicines directory
- Proposed: NCBI/PubMed and NCBI PubChem pharmacology records; FDA/openFDA labeling; PubMed placebo-controlled trial reports; ANSM French medicines directory for French authorization facts only if an allowed source URL is retained.

## MEDIUM progabide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Add primary PubMed pharmacology evidence for GABA receptor agonist activity.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6121050/; https://pubchem.ncbi.nlm.nih.gov/compound/44115
- Current: NCBI PubChem pharmacology records
- Proposed: NCBI PubChem pharmacology records; PubMed Lloyd 1982 GABA receptor pharmacology study

## MEDIUM progabide / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: False
- Summary: Historical RCT adverse-event counts exist, so the current wording is too absolute and the '0%' phrasing is potentially misleading.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6383790/; https://pubmed.ncbi.nlm.nih.gov/6403342/; https://pubmed.ncbi.nlm.nih.gov/3098923/
- Current: Evidence availability: no reliable FDA/RCT symptom percentages found (0% usable quantified current data located)
- Proposed: Evidence availability: limited historical RCT adverse-event counts exist, but no current FDA-label or harmonized placebo-adjusted symptom-percentage table was identified.

## MEDIUM progabide / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: More specific wording is supported by PubMed evidence.
- Sources: https://pubmed.ncbi.nlm.nih.gov/3098923/; https://pmc.ncbi.nlm.nih.gov/articles/PMC1029073/; https://pubmed.ncbi.nlm.nih.gov/3191894/; https://pubmed.ncbi.nlm.nih.gov/8222491/
- Current: Limited data; hepatic metabolism and interaction concerns reported
- Proposed: Limited data; hepatic-enzyme elevations and clinically relevant interaction concerns reported, including effects on phenytoin/carbamazepine metabolism and microsomal epoxide hydrolase inhibition.

## MEDIUM repository corticotropin / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: missing_source
- Approval required: True
- Summary: The FDA label supports the diuretic/electrolyte interaction and states formal drug-drug interaction studies have not been performed. I did not find FDA-label support for the stronger statement that it is not a CYP inducer/inhibitor.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: Not a CYP inducer/inhibitor; FDA label notes steroidogenic/electrolyte effects and that Acthar Gel may accentuate electrolyte loss associated with diuretics.
- Proposed: Formal drug-drug interaction studies have not been performed; FDA label states Acthar Gel may accentuate the electrolyte loss associated with diuretic therapy. No FDA-label CYP induction/inhibition interaction was identified.

## HIGH repository corticotropin / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The current source field relies on DailyMed and duplicates FDA/DailyMed labeling. Replace with trusted FDA/NCBI/PubMed sources that support the row facts and RCT context.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=168103; https://www.ncbi.nlm.nih.gov/sites/entrez?Cmd=DetailsSearch&Db=mesh&Term=%22Adrenocorticotropic+Hormone%22%5BMeSH+Terms%5D; https://pubmed.ncbi.nlm.nih.gov/34902005/
- Current: FDA/DailyMed Acthar Gel label (https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7b48ddec-e815-45f4-9ca0-5c0daaf56f30); FDA orphan drug designation/approval record for repository corticotropin/adrenocorticotropic hormone (https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=168103); FDA/DailyMed labeling
- Proposed: FDA Acthar Gel label, NDA 008372/S-074, revised 02/2024 (https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf); FDA orphan drug designation/approval record for repository corticotropin/adrenocorticotropic hormone, H.P. Acthar Gel, infantile spasms marketing approval 10/15/2010 (https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=168103); NCBI MeSH Adrenocorticotropic Hormone entry terms for ACTH/corticotropin aliases (https://www.ncbi.nlm.nih.gov/sites/entrez?Cmd=DetailsSearch&Db=mesh&Term=%22Adrenocorticotropic+Hormone%22%5BMeSH+Terms%5D); Tran et al. 2022 scoping review, PMID 34902005, for corticotropin RCT context (https://pubmed.ncbi.nlm.nih.gov/34902005/).

## MEDIUM repository corticotropin / fact_check
- Field: major_organ_for_metabolism
- Status: missing_source
- Approval required: True
- Summary: The label supports limited/unknown pharmacokinetics and adrenal cortical effects. The comparison to a conventional hepatic/renal ASM metabolism profile is an inference not directly sourced in the row.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: Limited/unknown; peptide hormone mixture with adrenal cortical target effects rather than a conventional hepatic/renal ASM metabolism profile
- Proposed: Limited/unknown; FDA label states pharmacokinetics of Acthar Gel have not been adequately characterized and describes Acthar Gel as a naturally sourced complex mixture of adrenocorticotropic hormone analogs and other pituitary peptides with adrenal cortical effects.

## HIGH repository corticotropin / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed should be replaced with the FDA accessdata label source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: FDA/DailyMed Acthar Gel label (https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7b48ddec-e815-45f4-9ca0-5c0daaf56f30)
- Proposed: FDA Acthar Gel label, NDA 008372/S-074, section 12.1 Mechanism of Action (https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf)

## HIGH repository corticotropin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: The trial intervention is melatonin supplementation for infantile epileptic spasms syndrome, not repository corticotropin/ACTH.
- Sources: https://pubmed.ncbi.nlm.nih.gov/37909654/
- Current: https://pubmed.ncbi.nlm.nih.gov/37909654/
- Proposed: Do not add to repository corticotropin placebo-controlled RCT links.

## HIGH repository corticotropin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: This is a melatonin protocol, not repository corticotropin/ACTH efficacy evidence.
- Sources: https://pubmed.ncbi.nlm.nih.gov/35788069/
- Current: https://pubmed.ncbi.nlm.nih.gov/35788069/
- Proposed: Do not add to repository corticotropin placebo-controlled RCT links.

## HIGH repository corticotropin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Primary intervention is flunarizine add-on therapy in children with infantile spasms, not repository corticotropin/ACTH.
- Sources: https://pubmed.ncbi.nlm.nih.gov/22889307/
- Current: https://pubmed.ncbi.nlm.nih.gov/22889307/
- Proposed: Do not add to repository corticotropin placebo-controlled RCT links.

## HIGH repository corticotropin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Study concerns magnesium effects on endogenous ACTH secretion and sleep physiology in men, not repository corticotropin treatment for seizures.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9683002/
- Current: https://pubmed.ncbi.nlm.nih.gov/9683002/
- Proposed: Do not add to repository corticotropin placebo-controlled RCT links.

## HIGH repository corticotropin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Trial is about valproate, not repository corticotropin/ACTH as the tested intervention.
- Sources: https://pubmed.ncbi.nlm.nih.gov/3939740/
- Current: https://pubmed.ncbi.nlm.nih.gov/3939740/
- Proposed: Do not add to repository corticotropin placebo-controlled RCT links.

## HIGH repository corticotropin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_placebo_rct
- Approval required: True
- Summary: This is a randomized double-blind comparison of ACTH versus prednisone with placebo/double-dummy elements, but it lacks a placebo-only efficacy control arm and is outside the row's placebo-controlled RCT outcome section.
- Sources: https://pubmed.ncbi.nlm.nih.gov/6312008/
- Current: https://pubmed.ncbi.nlm.nih.gov/6312008/
- Proposed: Do not add to placebo-controlled epilepsy RCT links; may be cited only as non-qualifying active-comparator evidence if project scope allows.

## HIGH repository corticotropin / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: Study uses an ACTH fragment in an ECT memory context, not repository corticotropin/Acthar for epilepsy or infantile spasms.
- Sources: https://pubmed.ncbi.nlm.nih.gov/193359/
- Current: https://pubmed.ncbi.nlm.nih.gov/193359/
- Proposed: Do not add to repository corticotropin placebo-controlled RCT links.

## INFO repository corticotropin / outcome_check
- Field: diff_50_responder_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: No qualifying placebo-controlled epilepsy RCT with an RR50 endpoint was identified for repository corticotropin/ACTH in infantile spasms. FDA-labeled infantile-spasms trials use active comparator or dose comparison and responder definitions based on spasm cessation plus hypsarrhythmia resolution, not RR50 versus placebo.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/34902005/
- Current: N/A
- Proposed: N/A

## INFO repository corticotropin / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: No qualifying placebo-controlled epilepsy RCT with median percent seizure-change outcome was identified for this row. Retain N/A.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/34902005/
- Current: N/A
- Proposed: N/A

## INFO repository corticotropin / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: not_applicable
- Approval required: False
- Summary: No qualifying placebo-controlled epilepsy RCT with placebo-differential seizure freedom was identified. FDA-labeled response data are from ACTH-vs-prednisone and dose-comparison infantile-spasms studies, not placebo-controlled epilepsy studies.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/34902005/
- Current: N/A
- Proposed: N/A

## HIGH repository corticotropin / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supported by the FDA accessdata label for Acthar Gel, which contains warnings and precautions but no boxed-warning section or boxed-warning text. The current row wording and source rely on DailyMed, which is not permissible for this field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in FDA Acthar Gel prescribing information.

## MEDIUM repository corticotropin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use trusted FDA/NCBI/PubMed sources and remove DailyMed from the source list.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=168103; https://www.ncbi.nlm.nih.gov/sites/entrez?Cmd=DetailsSearch&Db=mesh&Term=%22Adrenocorticotropic+Hormone%22%5BMeSH+Terms%5D; https://pubmed.ncbi.nlm.nih.gov/34902005/
- Current: FDA/DailyMed Acthar Gel label (https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7b48ddec-e815-45f4-9ca0-5c0daaf56f30); FDA orphan drug designation/approval record for repository corticotropin/adrenocorticotropic hormone (https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=168103); FDA/DailyMed labeling
- Proposed: FDA Acthar Gel label, NDA 008372/S-074, revised 02/2024 (https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf); FDA orphan drug designation/approval record for repository corticotropin/adrenocorticotropic hormone, H.P. Acthar Gel, infantile spasms marketing approval 10/15/2010 (https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=168103); NCBI MeSH Adrenocorticotropic Hormone entry terms for ACTH/corticotropin aliases (https://www.ncbi.nlm.nih.gov/sites/entrez?Cmd=DetailsSearch&Db=mesh&Term=%22Adrenocorticotropic+Hormone%22%5BMeSH+Terms%5D); Tran et al. 2022 scoping review, PMID 34902005, for corticotropin RCT context (https://pubmed.ncbi.nlm.nih.gov/34902005/).

## MEDIUM repository corticotropin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification; use FDA accessdata labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=7b48ddec-e815-45f4-9ca0-5c0daaf56f30; published=Dec 08, 2025; title=ACTHAR (REPOSITORY CORTICOTROPIN) INJECTION ACTHAR (REPOSITORY CORTICOTROPIN) INJECTION [MALLINCKRODT ARD LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7b48ddec-e815-45f4-9ca0-5c0daaf56f30
- Proposed: FDA Acthar Gel label, NDA 008372/S-074, revised 02/2024; status=no_boxed_warning_identified_in_fda_label; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf

## MEDIUM repository corticotropin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed with the FDA accessdata label source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: FDA/DailyMed Acthar Gel label (https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=7b48ddec-e815-45f4-9ca0-5c0daaf56f30)
- Proposed: FDA Acthar Gel label, NDA 008372/S-074, section 12.1 Mechanism of Action (https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf)

## MEDIUM repository corticotropin / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Black-box warning verification must use FDA sources, not DailyMed. FDA accessdata label contains no boxed-warning section/text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in FDA Acthar Gel prescribing information.

## CRITICAL repository corticotropin / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: True
- Summary: The diuretic/electrolyte statement is supported; the stronger CYP statement lacks a named supporting source in the row.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: Not a CYP inducer/inhibitor; FDA label notes steroidogenic/electrolyte effects and that Acthar Gel may accentuate electrolyte loss associated with diuretics.
- Proposed: Formal drug-drug interaction studies have not been performed; FDA label states Acthar Gel may accentuate the electrolyte loss associated with diuretic therapy. No FDA-label CYP induction/inhibition interaction was identified.

## CRITICAL repository corticotropin / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: True
- Summary: Keeps the limited/unknown classification but replaces an unsourced metabolism-profile inference with FDA-label wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/008372s074lbl.pdf
- Current: Limited/unknown; peptide hormone mixture with adrenal cortical target effects rather than a conventional hepatic/renal ASM metabolism profile
- Proposed: Limited/unknown; FDA label states pharmacokinetics of Acthar Gel have not been adequately characterized and describes Acthar Gel as a naturally sourced complex mixture of adrenocorticotropic hormone analogs and other pituitary peptides with adrenal cortical effects.

## MEDIUM rufinamide / fact_check
- Field: pubmed_search_aliases
- Status: missing_source
- Approval required: False
- Summary: The alias is plausible, but the row's named sources do not document it and this audit did not confirm it in an allowed trusted source page.
- Current: CGP 33101
- Proposed: CGP 33101

## HIGH rufinamide / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports 400-800 mg/day as the adult starting dose and 3200 mg/day as the adult target/max. The 'minimum effective' wording is better supported by the Elger Phase II dose-ranging RCT for partial seizures, not by the labeled LGS adult dose statement alone.
- Sources: https://www.fda.gov/media/169593/download; https://pubmed.ncbi.nlm.nih.gov/20061123/
- Current: 400 mg/day adult starting dose; titrate to 3200 mg/day target/max
- Proposed: Adults: start 400-800 mg/day in two divided doses and titrate by 400-800 mg every other day to 3200 mg/day maximum; Elger2010 dose-ranging partial-seizure study reported a minimally efficacious dose of 400 mg/day.

## CRITICAL rufinamide / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: True
- Summary: FDA labeling states most elimination is via metabolism and that the primary pathway is carboxylesterase-mediated hydrolysis; therefore 'Renal/no major metabolism' is too broad and partly contradicted.
- Sources: https://www.fda.gov/media/169593/download
- Current: Renal/no major metabolism
- Proposed: Carboxylesterase hydrolysis/no major CYP metabolism

## CRITICAL rufinamide / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: True
- Summary: The filter conflicts with the row fact and FDA label; the clinically relevant direction is weak CYP3A4 induction, not inhibitor.
- Sources: https://www.fda.gov/media/169593/download
- Current: Inhibitor
- Proposed: Inducer

## HIGH rufinamide / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; DailyMed should not be named as the source when trusted source policy can be satisfied directly with FDA labeling.
- Sources: https://www.fda.gov/media/169593/download
- Current: FDA/DailyMed labeling
- Proposed: FDA Banzel prescribing information

## CRITICAL rufinamide / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: Somnolence 24% and vomiting 22% are supported by Glauser2008/FDA LGS trial data. Headache 16%, nausea 12%, and rash near 4% are supported in FDA pooled tables, but dizziness 14% and QT shortening 14% were not supported; FDA label gives dizziness 8% pediatric or 19% adult and QT shortening >20 msec in 46% at 3200 mg.
- Sources: https://pubmed.ncbi.nlm.nih.gov/18401024/; https://www.fda.gov/media/169593/download
- Current: CNS: somnolence 24%, GI: vomiting 22%, CNS: headache 16%, CNS: dizziness 14%, GI: nausea 12%, dermatologic: rash 5%, cardiac: QT shortening 14%
- Proposed: CNS: somnolence 24.3% in LGS RCT; GI: vomiting 21.6% in LGS RCT; CNS: headache 16% pediatric pooled / 27% adult pooled; CNS: dizziness 8% pediatric pooled / 19% adult pooled; GI: nausea 7% pediatric pooled / 12% adult pooled; dermatologic: rash 4% pediatric pooled; cardiac: QT shortening >20 msec at Tmax in 46% at 3200 mg vs 5-10% placebo in QT study.

## HIGH rufinamide / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The named LiverTox anticonvulsants table is not a good support for LGS-specific row facts, Epilepsy Foundation Australia is outside the requested trusted-source domains, and DailyMed should not be used for FDA boxed-warning verification. FDA, NCBI, EMA, and PubMed sources support the retained facts.
- Sources: https://www.fda.gov/media/169593/download; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=193504; https://www.ncbi.nlm.nih.gov/books/NBK548457/; https://www.ncbi.nlm.nih.gov/books/NBK557595/; https://www.ema.europa.eu/en/medicines/human/EPAR/inovelon
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA Banzel prescribing information; FDA/openFDA drug label API; FDA Orphan Drug Designations and Approvals; NCBI Bookshelf LiverTox rufinamide monograph; NCBI Bookshelf StatPearls rufinamide; EMA Inovelon EPAR; PubMed RCT records.

## HIGH rufinamide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supportable only with an FDA source. DailyMed is not permissible for this field under the audit rules.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM rufinamide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Current source list includes non-trusted or non-specific sources and does not reliably support each row fact.
- Sources: https://www.fda.gov/media/169593/download; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=193504; https://www.ncbi.nlm.nih.gov/books/NBK548457/; https://www.ncbi.nlm.nih.gov/books/NBK557595/; https://www.ema.europa.eu/en/medicines/human/EPAR/inovelon
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA Banzel prescribing information; FDA/openFDA drug label API; FDA Orphan Drug Designations and Approvals; NCBI Bookshelf LiverTox rufinamide monograph; NCBI Bookshelf StatPearls rufinamide; EMA Inovelon EPAR; PubMed RCT records.

## MEDIUM rufinamide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box warning verification must use FDA/openFDA, FDA labels, or Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d; published=Nov 18, 2024; title=BANZEL (RUFINAMIDE) TABLET, FILM COATED BANZEL (RUFINAMIDE) SUSPENSION [EISAI INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=0a3fa925-1abd-458a-bd57-4ae780a1ef2d; effective_time=20221215; title=Banzel / RUFINAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5

## MEDIUM rufinamide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The mechanism text is supported by FDA label lines describing sodium-channel modulation; DailyMed does not need to be cited.
- Sources: https://www.fda.gov/media/169593/download
- Current: FDA/DailyMed labeling
- Proposed: FDA Banzel prescribing information

## MEDIUM rufinamide / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permitted for boxed-warning verification; openFDA/FDA source should be named.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## MEDIUM rufinamide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace non-permitted DailyMed boxed-warning source with FDA/openFDA metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d; published=Nov 18, 2024; title=BANZEL (RUFINAMIDE) TABLET, FILM COATED BANZEL (RUFINAMIDE) SUSPENSION [EISAI INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0a3fa925-1abd-458a-bd57-4ae780a1ef2d
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=0a3fa925-1abd-458a-bd57-4ae780a1ef2d; effective_time=20221215; title=Banzel / RUFINAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5

## CRITICAL rufinamide / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Correct unsupported dizziness, rash, and QT-shortening percentages while preserving supported somnolence/vomiting values.
- Sources: https://pubmed.ncbi.nlm.nih.gov/18401024/; https://www.fda.gov/media/169593/download
- Current: CNS: somnolence 24%, GI: vomiting 22%, CNS: headache 16%, CNS: dizziness 14%, GI: nausea 12%, dermatologic: rash 5%, cardiac: QT shortening 14%
- Proposed: CNS: somnolence 24.3% in LGS RCT; GI: vomiting 21.6% in LGS RCT; CNS: headache 16% pediatric pooled / 27% adult pooled; CNS: dizziness 8% pediatric pooled / 19% adult pooled; GI: nausea 7% pediatric pooled / 12% adult pooled; dermatologic: rash 4% pediatric pooled; cardiac: QT shortening >20 msec at Tmax in 46% at 3200 mg vs 5-10% placebo in QT study.

## CRITICAL rufinamide / proposed_row_update
- Field: filter_enzyme_effect
- Status: proposed
- Approval required: True
- Summary: FDA label supports weak CYP3A4 induction, not a clinically meaningful inhibitor classification.
- Sources: https://www.fda.gov/media/169593/download
- Current: Inhibitor
- Proposed: Inducer

## CRITICAL rufinamide / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: True
- Summary: FDA label states most elimination is via carboxylesterase-mediated metabolism; unchanged renal excretion is less than 2%.
- Sources: https://www.fda.gov/media/169593/download
- Current: Renal/no major metabolism
- Proposed: Carboxylesterase hydrolysis/no major CYP metabolism

## MEDIUM rufinamide / proposed_row_update
- Field: minimum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Clarifies that 400 mg/day is FDA starting-dose language for adults and the minimum-efficacious-dose claim comes from a partial-seizure dose-ranging RCT.
- Sources: https://www.fda.gov/media/169593/download; https://pubmed.ncbi.nlm.nih.gov/20061123/
- Current: 400 mg/day adult starting dose; titrate to 3200 mg/day target/max
- Proposed: Adults: start 400-800 mg/day in two divided doses and titrate by 400-800 mg every other day to 3200 mg/day maximum; Elger2010 dose-ranging partial-seizure study reported a minimally efficacious dose of 400 mg/day.

## MEDIUM rufinamide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Use the FDA label directly as the trusted source.
- Sources: https://www.fda.gov/media/169593/download
- Current: FDA/DailyMed labeling
- Proposed: FDA Banzel prescribing information

## MEDIUM rufinamide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace unsupported/non-trusted source labels with sources that actually support row facts.
- Sources: https://www.fda.gov/media/169593/download; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220a3fa925-1abd-458a-bd57-4ae780a1ef2d%22&limit=5; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=193504; https://www.ncbi.nlm.nih.gov/books/NBK548457/; https://www.ncbi.nlm.nih.gov/books/NBK557595/; https://www.ema.europa.eu/en/medicines/human/EPAR/inovelon
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA Banzel prescribing information; FDA/openFDA drug label API; FDA Orphan Drug Designations and Approvals; NCBI Bookshelf LiverTox rufinamide monograph; NCBI Bookshelf StatPearls rufinamide; EMA Inovelon EPAR; PubMed RCT records.

## HIGH stiripentol / fact_check
- Field: filter_formulation
- Status: incorrect
- Approval required: False
- Summary: The marketed product is not a ready-made liquid; FDA labeling lists capsules and powder for oral suspension.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: Capsule; Liquid; Sprinkle/powder
- Proposed: Capsule; Powder for oral suspension

## HIGH stiripentol / fact_check
- Field: typical_doses_per_day
- Status: incorrect
- Approval required: False
- Summary: Current U.S. labeling requires concomitant clobazam, while the pivotal studies enrolled patients inadequately controlled on clobazam and valproate.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: Dravet: 50 mg/kg/day divided BID/TID with clobazam/valproate
- Proposed: Dravet: 50 mg/kg/day divided BID/TID with clobazam; pivotal trials used clobazam and valproate background therapy

## HIGH stiripentol / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: The 50 mg/kg/day regimen is label-supported, but valproate is trial background therapy rather than a current U.S. labeled requirement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://pubmed.ncbi.nlm.nih.gov/11089822/
- Current: 50 mg/kg/day target regimen with clobazam/valproate
- Proposed: 50 mg/kg/day target regimen; current U.S. indication is with clobazam, and pivotal trials used clobazam plus valproate background therapy

## HIGH stiripentol / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: The current wording overstates potency and omits FDA-labeled induction effects. FDA labeling supports CYP3A4/CYP2C19 inhibition and additional CYP/transporter effects, but not the exact current phrasing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC7358047/
- Current: Potent inhibitor of CYP3A4, CYP2C19, CYP2D6 and other pathways
- Proposed: Mixed CYP/transporter inhibitor and inducer: FDA label states stiripentol inhibits and induces CYP1A2, CYP2B6, and CYP3A4, and inhibits CYP2C8, CYP2C19, P-gp, and BCRP; CYP2D6 inhibition is literature-reported but not listed in the FDA label.

## HIGH stiripentol / fact_check
- Field: filter_enzyme_effect
- Status: incorrect
- Approval required: False
- Summary: FDA label describes both inhibition and induction for selected CYP enzymes; a pure inhibitor filter is incomplete.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: Inhibitor
- Proposed: Mixed inhibitor/inducer

## HIGH stiripentol / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is FDA-label supported, but the source should not be named as DailyMed when a direct FDA label URL is available.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov label 207223s006lbl, revised 04/2026)

## MEDIUM stiripentol / fact_check
- Field: qt_interval_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: The FDA label states there are no relevant pharmacodynamic data, but I did not find a QT-specific statement establishing no meaningful QT effect.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: No QT-specific effect statement identified in current FDA prescribing information.

## MEDIUM stiripentol / fact_check
- Field: filter_qt_effect
- Status: insufficient_evidence
- Approval required: False
- Summary: The current FDA label does not support a specific no-meaningful-QT-effect classification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: No known meaningful QT effect
- Proposed: No QT-specific FDA-label statement identified

## HIGH stiripentol / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed is impermissible for boxed-warning verification and Epilepsy Society is not in the trusted-source allowlist. FDA/NCBI/PubMed sources support the retained row facts more directly.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=266108; https://www.ncbi.nlm.nih.gov/books/NBK548951/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov label 207223s006lbl, revised 04/2026); FDA Orphan Drug Designations and Approvals; NCBI LiverTox Stiripentol; PubMed RCT records

## HIGH stiripentol / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: wrong_drug
- Approval required: True
- Summary: This was a randomized trial of fenfluramine 0.4 mg/kg/day vs placebo in patients receiving stiripentol-inclusive regimens. Stiripentol was not the randomized active treatment.
- Sources: https://pubmed.ncbi.nlm.nih.gov/31790543/
- Current: https://pubmed.ncbi.nlm.nih.gov/31790543/
- Proposed: remove from stiripentol active-drug RCT list or move to background-therapy notes; requires user approval

## MEDIUM stiripentol / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: insufficient_evidence
- Approval required: True
- Summary: PubMed verifies a randomized placebo-controlled enrichment/withdrawal trial of stiripentol in childhood partial epilepsy, but the abstract does not state phase II/III and it is not a Dravet maximum-dose outcome source.
- Sources: https://pubmed.ncbi.nlm.nih.gov/16948934/
- Current: https://pubmed.ncbi.nlm.nih.gov/16948934/
- Proposed: retain only if the CSV field allows placebo-controlled stiripentol seizure RCTs beyond Dravet and without explicit PubMed phase tagging; otherwise review field scope

## HIGH stiripentol / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: The 76% value matches the mean percentage-change contrast in the Chiron2000/FDA data (-69% vs about +7%), not the median percentage-change contrast. FDA Table 5 lists median -91% for stiripentol and +7.4% for placebo in Study 1.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11089822/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: 76 % (drug minus placebo MPC differential at maximum effective dose/regimen: Chiron2000 stiripentol add-on to valproate and clobazam 76%)
- Proposed: 98.4 % (drug minus placebo median percentage-change differential at maximum effective dose/regimen: Chiron2000/STICLO France stiripentol add-on to valproate and clobazam, computed from median -91% on stiripentol vs +7.4% on placebo)

## HIGH stiripentol / outcome_check
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: The plotted value should match median percentage-change differential, not mean percentage-change differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11089822/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: Chiron2000|76|https://pubmed.ncbi.nlm.nih.gov/11089822/|41
- Proposed: Chiron2000|98.4|https://pubmed.ncbi.nlm.nih.gov/11089822/|41

## HIGH stiripentol / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The FDA accessdata label has no Boxed Warning section. The current cell uses DailyMed for boxed-warning verification, which is not permissible for this audit field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in current FDA prescribing information.

## MEDIUM stiripentol / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Use FDA/openFDA, not DailyMed, for the boxed-warning field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58304ba8-9779-4658-811e-94ffe08c3f16; published=Apr 30, 2026; title=DIACOMIT (STIRIPENTOL) CAPSULE DIACOMIT (STIRIPENTOL) POWDER, FOR SUSPENSION [BIOCODEX, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58304ba8-9779-4658-811e-94ffe08c3f16
- Proposed: FDA prescribing information; status=no_boxed_warning_identified_in_current_fda_label; application=NDA 207223; label=207223s006lbl; revised=04/2026; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; openFDA_api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5

## MEDIUM stiripentol / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Align row evidence with trusted-source policy and direct support for facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=266108; https://www.ncbi.nlm.nih.gov/books/NBK548951/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov label 207223s006lbl, revised 04/2026); FDA Orphan Drug Designations and Approvals; NCBI LiverTox Stiripentol; PubMed RCT records

## MEDIUM stiripentol / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for the boxed-warning field; FDA label/openFDA should be used.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=58304ba8-9779-4658-811e-94ffe08c3f16; published=Apr 30, 2026; title=DIACOMIT (STIRIPENTOL) CAPSULE DIACOMIT (STIRIPENTOL) POWDER, FOR SUSPENSION [BIOCODEX, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=58304ba8-9779-4658-811e-94ffe08c3f16
- Proposed: FDA prescribing information; status=no_boxed_warning_identified_in_current_fda_label; application=NDA 207223; label=207223s006lbl; revised=04/2026; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; openFDA_api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%2258304ba8-9779-4658-811e-94ffe08c3f16%22&limit=5

## MEDIUM stiripentol / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Fact is supportable, but the current wording cites an impermissible DailyMed check.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in current FDA prescribing information.

## MEDIUM stiripentol / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Refresh date should reflect this FDA-source audit date.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## MEDIUM stiripentol / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces non-allowlisted/impermissible source naming with trusted sources that directly support row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=266108; https://www.ncbi.nlm.nih.gov/books/NBK548951/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov label 207223s006lbl, revised 04/2026); FDA Orphan Drug Designations and Approvals; NCBI LiverTox Stiripentol; PubMed RCT records

## MEDIUM stiripentol / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism is FDA-label supported; use the direct FDA source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov label 207223s006lbl, revised 04/2026)

## MEDIUM stiripentol / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: Current wording is oversimplified and not fully FDA-label concordant.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf; https://pmc.ncbi.nlm.nih.gov/articles/PMC7358047/
- Current: Potent inhibitor of CYP3A4, CYP2C19, CYP2D6 and other pathways
- Proposed: Mixed CYP/transporter inhibitor and inducer: FDA label states stiripentol inhibits and induces CYP1A2, CYP2B6, and CYP3A4, and inhibits CYP2C8, CYP2C19, P-gp, and BCRP; CYP2D6 inhibition is literature-reported but not listed in the FDA label.

## MEDIUM stiripentol / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: The current 76% is a mean percentage-change contrast, not the median contrast requested by the field name.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11089822/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: 76 % (drug minus placebo MPC differential at maximum effective dose/regimen: Chiron2000 stiripentol add-on to valproate and clobazam 76%)
- Proposed: 98.4 % (drug minus placebo median percentage-change differential at maximum effective dose/regimen: Chiron2000/STICLO France stiripentol add-on to valproate and clobazam, computed from median -91% on stiripentol vs +7.4% on placebo)

## MEDIUM stiripentol / proposed_row_update
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Plot value should match median percentage-change differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/11089822/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: Chiron2000|76|https://pubmed.ncbi.nlm.nih.gov/11089822/|41
- Proposed: Chiron2000|98.4|https://pubmed.ncbi.nlm.nih.gov/11089822/|41

## CRITICAL stiripentol / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: True
- Summary: Nabbout2020 randomized fenfluramine vs placebo; stiripentol was background therapy, so it is the wrong active drug for this stiripentol RCT list. This is a direct contradiction and needs user approval before removal.
- Sources: https://pubmed.ncbi.nlm.nih.gov/31790543/; https://clinicaltrials.gov/study/NCT02926898
- Current: Guerrini2024|https://pubmed.ncbi.nlm.nih.gov/38722572/; Nabbout2020|https://pubmed.ncbi.nlm.nih.gov/31790543/; Chiron2006|https://pubmed.ncbi.nlm.nih.gov/16948934/; Chiron2000|https://pubmed.ncbi.nlm.nih.gov/11089822/
- Proposed: Guerrini2024|https://pubmed.ncbi.nlm.nih.gov/38722572/; Chiron2006|https://pubmed.ncbi.nlm.nih.gov/16948934/; Chiron2000|https://pubmed.ncbi.nlm.nih.gov/11089822/

## MEDIUM stiripentol / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: False
- Summary: FDA label does not provide a QT-specific no-effect statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: No QT-specific effect statement identified in current FDA prescribing information.

## MEDIUM stiripentol / proposed_row_update
- Field: filter_formulation
- Status: proposed
- Approval required: False
- Summary: FDA label supports capsules and powder for oral suspension, not a ready-made liquid formulation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/207223s006lbl.pdf
- Current: Capsule; Liquid; Sprinkle/powder
- Proposed: Capsule; Powder for oral suspension

## HIGH sultiame / fact_check
- Field: names_and_aliases
- Status: missing
- Approval required: False
- Summary: Sulthiame and Ospolot are verified by eMC/PubMed. NCBI/NICE search strategies include additional alias terms useful to prevent duplicate rows and improve PubMed retrieval.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://pubmed.ncbi.nlm.nih.gov/14738417/; https://www.ncbi.nlm.nih.gov/books/NBK581162/bin/niceng217er36-appb-et1.pdf
- Current: sultiame; alternate_generic_names=sulthiame; trade_names=Ospolot; pubmed_search_aliases empty
- Proposed: generic_name=sultiame; alternate_generic_names=sulthiame; trade_names=Ospolot; pubmed_search_aliases=sulthiame; sultiam; sulphenytame; Ospolot; Conadil; Contravul; Elisal; Riker; Trolone

## HIGH sultiame / fact_check
- Field: formulations_available/filter_formulation
- Status: incorrect
- Approval required: False
- Summary: eMC currently lists Ospolot 20 mg/ml oral suspension; NCBI/Cochrane text also describes sulthiame as usually taken in tablet form in some non-US settings. The filter omits oral suspension.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://www.medicines.org.uk/emc/ingredient/10084; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8459749/
- Current: Tablet/oral formulation in non-U.S. markets; filter_formulation=Tablet
- Proposed: Tablet/oral formulation in non-U.S. markets; filter_formulation=Tablet; Oral suspension

## MEDIUM sultiame / fact_check
- Field: epilepsy_type/filter_epilepsy_type
- Status: missing_source
- Approval required: True
- Summary: Trusted sources support Rolandic/BECTS, focal epilepsy, and West syndrome/infantile spasms. I did not find trusted row evidence supporting an Absence epilepsy entry for sulthiame.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://pubmed.ncbi.nlm.nih.gov/14738417/; https://pubmed.ncbi.nlm.nih.gov/12027906/; https://pubmed.ncbi.nlm.nih.gov/16930943/
- Current: Focal; Self-limited epilepsy with centrotemporal spikes; Absence
- Proposed: Focal; Self-limited epilepsy with centrotemporal spikes/Rolandic epilepsy; West syndrome/infantile spasms (placebo-controlled add-on RCT evidence)

## HIGH sultiame / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: The UK SmPC states there is evidence sulthiame inhibits CYP2C19 enzyme activity. The current wording incorrectly implies no CYP inhibition.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc
- Current: Carbonic anhydrase inhibitor; not a major CYP inducer/inhibitor
- Proposed: Carbonic anhydrase inhibitor; inhibits CYP2C19; no evidence identified for CYP induction.

## MEDIUM sultiame / fact_check
- Field: half_life_range
- Status: missing_source
- Approval required: True
- Summary: The trusted eMC SmPC gives an adult half-life of approximately 12 h and says a shorter half-life is assumed in children; I did not find trusted support for the exact 2-16 h range.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://pubmed.ncbi.nlm.nih.gov/31990440/
- Current: 2-16 h
- Proposed: Approximately 12 h in healthy adults; shorter half-life assumed in children.

## CRITICAL sultiame / fact_check
- Field: major_organ_for_metabolism/filter_metabolism
- Status: incorrect
- Approval required: True
- Summary: The SmPC states 80-90% is eliminated in urine, 10-20% in feces after biliary secretion, and 32% unchanged via kidneys within 24 h. It does not support 'liver/hepatic' as a major metabolism route.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc
- Current: Liver and renal excretion; filter_metabolism=Liver/hepatic; Renal/no major metabolism
- Proposed: Predominantly renal excretion with secondary fecal excretion after biliary secretion; no major metabolism characterized in the UK SmPC. filter_metabolism=Renal/no major metabolism; Biliary/fecal excretion

## MEDIUM sultiame / fact_check
- Field: adverse_symptoms_percentages
- Status: missing_source
- Approval required: True
- Summary: The exact percentages in the row are not supported by the UK SmPC. The SmPC gives frequency categories and only quantifies nausea/vomiting at about 10%.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8459749/
- Current: GI: anorexia 15%, neurologic: paresthesia 10%, CNS: fatigue 10%, respiratory: hyperpnea 5%, dermatologic: rash 2%
- Proposed: GI/metabolic: lack of appetite, weight loss, nausea/vomiting about 10%; neurologic: paresthesias in extremities/face, dizziness, headache; respiratory: tachypnoea/hyperpnoea/dyspnoea/hiccups; CNS/general: tiredness/exhaustion may occur with carbonic anhydrase inhibition; dermatologic/hypersensitivity: allergic skin reactions and severe reactions including Stevens-Johnson syndrome/TEN reported, frequency not known.

## MEDIUM sultiame / fact_check
- Field: qt_interval_effect/filter_qt_effect
- Status: missing_source
- Approval required: False
- Summary: The current negative QT wording is plausible but not directly sourced as written. The SmPC supports a narrower statement that QT prolongation is not identified in the label text reviewed.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc
- Current: No established clinically meaningful QT effect
- Proposed: No QT-prolongation warning identified in the UK SmPC; cardiac adverse reactions listed include stenocardia and tachycardia.

## HIGH sultiame / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Wikipedia is not in the trusted source list, and DailyMed cannot support boxed-warning verification. Several retained facts need PubMed/NCBI and FDA/openFDA sources named explicitly.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://pubmed.ncbi.nlm.nih.gov/14738417/; https://pubmed.ncbi.nlm.nih.gov/11051123/; https://pubmed.ncbi.nlm.nih.gov/12027906/; https://pubmed.ncbi.nlm.nih.gov/11325350/; https://pubmed.ncbi.nlm.nih.gov/23543577/; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=401213
- Current: Epilepsy Society ASM list; Wikipedia anticonvulsant drug-class list; UK eMC SmPC labeling; Sills and Rogawski 2020 ASM mechanism review; Sulthiame sodium-current mechanism study; FDA/DailyMed labeling
- Proposed: UK eMC SmPC labeling; PubMed/NCBI sulthiame monotherapy and add-on reviews; Debus2004 and Rating2000 PubMed RCT abstracts; Leniger2002 carbonic anhydrase mechanism study; Madeja2001 sodium-current mechanism study; FDA/openFDA labeling and FDA orphan designation search

## HIGH sultiame / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed abstract describes candidates for a prospective multicenter randomized double-blind placebo-controlled sulthiame study, and the NCBI/Cochrane monotherapy review treats Basnec 2005 as a sulthiame-versus-placebo BECTS study. No RR50, median percent change, or seizure-freedom differential was extractable from the abstract.
- Sources: https://pubmed.ncbi.nlm.nih.gov/15813357/
- Proposed: Basnec2005|https://pubmed.ncbi.nlm.nih.gov/15813357/

## HIGH sultiame / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The warning fact should not cite DailyMed under the audit rule. FDA/openFDA label searches for sultiame/sulthiame/Ospolot are the correct FDA-only basis; FDA orphan designation lists sulthiame for BECTS as not FDA approved for the orphan indication.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:sultiame&limit=1; https://api.fda.gov/drug/label.json?search=openfda.generic_name:sulthiame&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:Ospolot&limit=1; https://www.fda.gov/drugs/drug-approvals-and-databases/drugsfda-database; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=401213
- Current: No current FDA/DailyMed label identified.; source says FDA/DailyMed search.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM sultiame / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace non-trusted/prohibited sources and name sources that actually support retained cell facts.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8459749/; https://pubmed.ncbi.nlm.nih.gov/23543577/; https://pubmed.ncbi.nlm.nih.gov/14738417/; https://pubmed.ncbi.nlm.nih.gov/11051123/; https://pubmed.ncbi.nlm.nih.gov/12027906/; https://pubmed.ncbi.nlm.nih.gov/11325350/; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=401213
- Current: Epilepsy Society ASM list; Wikipedia anticonvulsant drug-class list; UK eMC SmPC labeling; Sills and Rogawski 2020 ASM mechanism review; Sulthiame sodium-current mechanism study; FDA/DailyMed labeling
- Proposed: UK eMC SmPC labeling; PubMed/NCBI sulthiame monotherapy and add-on reviews; Debus2004 and Rating2000 PubMed RCT abstracts; Leniger2002 carbonic anhydrase mechanism study; Madeja2001 sodium-current mechanism study; FDA/openFDA labeling and FDA orphan designation search

## MEDIUM sultiame / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Adds the PubMed carbonic anhydrase mechanism source supporting the primary mechanism and clarifies the sodium-current source.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://pubmed.ncbi.nlm.nih.gov/12027906/; https://pubmed.ncbi.nlm.nih.gov/11325350/
- Current: UK eMC SmPC labeling; Sulthiame sodium-current mechanism study
- Proposed: UK eMC SmPC labeling; Leniger2002 carbonic anhydrase/intracellular pH mechanism study; Madeja2001 sodium-current mechanism study

## MEDIUM sultiame / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Boxed-warning source must be FDA/openFDA/Drugs@FDA, not DailyMed.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:sultiame&limit=1; https://api.fda.gov/drug/label.json?search=openfda.generic_name:sulthiame&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:Ospolot&limit=1; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=401213
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [sultiame; sulthiame; Ospolot].
- Proposed: FDA/openFDA label API searches on 05-21-2026 found no current FDA label for terms [sultiame; sulthiame; Ospolot]; FDA orphan designation record for sulthiame in BECTS lists the orphan indication as not FDA approved.

## MEDIUM sultiame / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; use FDA/openFDA/Drugs@FDA/FDA sources only.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:sultiame&limit=1; https://api.fda.gov/drug/label.json?search=openfda.generic_name:sulthiame&limit=1; https://api.fda.gov/drug/label.json?search=openfda.brand_name:Ospolot&limit=1; https://www.accessdata.fda.gov/scripts/opdlisting/oopd/detailedIndex.cfm?cfgridkey=401213
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [sultiame; sulthiame; Ospolot].
- Proposed: FDA/openFDA label API searches on 05-21-2026 found no current FDA label for terms [sultiame; sulthiame; Ospolot]; FDA orphan designation record for sulthiame in BECTS lists the orphan indication as not FDA approved.

## MEDIUM sultiame / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: Remove DailyMed wording from the boxed-warning field.
- Sources: https://open.fda.gov/apis/drug/label/understanding-the-api-results/
- Current: No current FDA/DailyMed label identified.
- Proposed: No current FDA/openFDA label identified.

## MEDIUM sultiame / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Audit was refreshed against FDA/openFDA policy on 05-21-2026.
- Sources: https://open.fda.gov/apis/drug/label/understanding-the-api-results/
- Current: 05-20-2026
- Proposed: 05-21-2026

## MEDIUM sultiame / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: NCBI/NICE search strategies include these aliases; adding them reduces duplicate-row risk and improves literature retrieval.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK581162/bin/niceng217er36-appb-et1.pdf
- Proposed: sulthiame; sultiam; sulphenytame; Ospolot; Conadil; Contravul; Elisal; Riker; Trolone

## MEDIUM sultiame / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: False
- Summary: Basnec2005 is identified by PubMed/NCBI review evidence as a sulthiame-versus-placebo BECTS study, although no outcome differential is extractable from its abstract.
- Sources: https://pubmed.ncbi.nlm.nih.gov/15813357/; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8459749/
- Current: Debus2004|https://pubmed.ncbi.nlm.nih.gov/14738417/; Rating2000|https://pubmed.ncbi.nlm.nih.gov/11051123/
- Proposed: Debus2004|https://pubmed.ncbi.nlm.nih.gov/14738417/; Rating2000|https://pubmed.ncbi.nlm.nih.gov/11051123/; Basnec2005|https://pubmed.ncbi.nlm.nih.gov/15813357/

## MEDIUM sultiame / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Updates notes for the manually verified RCT set and missing Basnec candidate.
- Sources: https://pubmed.ncbi.nlm.nih.gov/14738417/; https://pubmed.ncbi.nlm.nih.gov/11051123/; https://pubmed.ncbi.nlm.nih.gov/15813357/; https://pubmed.ncbi.nlm.nih.gov/12558577/
- Current: PubMed loop 56/65 on 2026-05-15: 2 qualifying placebo-controlled randomized clinical trial report(s) retained from 4 PubMed candidate(s). Links were rebuilt from fetched PubMed PMID metadata and named FirstAuthorYear. Differential effectiveness columns summarize extractable maximum effective dose/regimen values within qualifying RCT reports.
- Proposed: Manual audit on 2026-05-21: Debus2004 and Rating2000 are verified placebo-controlled randomized sulthiame clinical trial reports with extractable seizure-freedom/complete-response differentials. Basnec2005 should be considered for the RCT link field as a sulthiame-versus-placebo BECTS report, but no RR50, MPC, or seizure-freedom differential was extractable from its abstract. Bast2003 is an EEG companion report of the Rating study and is not a separate efficacy RCT.

## MEDIUM sultiame / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: False
- Summary: UK SmPC states evidence of CYP2C19 inhibition.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc
- Current: Carbonic anhydrase inhibitor; not a major CYP inducer/inhibitor
- Proposed: Carbonic anhydrase inhibitor; inhibits CYP2C19; no evidence identified for CYP induction.

## MEDIUM sultiame / proposed_row_update
- Field: filter_formulation
- Status: proposed
- Approval required: False
- Summary: Oral suspension is a verified current eMC formulation; tablet use is supported in NCBI review text/non-US context.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc; https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8459749/
- Current: Tablet
- Proposed: Tablet; Oral suspension

## CRITICAL sultiame / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: The trusted SmPC supports approximately 12 h, not the exact 2-16 h range.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc
- Current: 2-16 h
- Proposed: Approximately 12 h in healthy adults; shorter half-life assumed in children.

## CRITICAL sultiame / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: True
- Summary: Current wording overstates hepatic metabolism relative to SmPC elimination text.
- Sources: https://www.medicines.org.uk/emc/product/100433/smpc
- Current: Liver and renal excretion
- Proposed: Predominantly renal excretion with secondary fecal excretion after biliary secretion; no major metabolism characterized in the UK SmPC.

## HIGH tiagabine / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: FDA labeling and Drugs@FDA use the salt name tiagabine hydrochloride/tiagabine HCl. This should be captured as an alias so the salt name is not treated as a separate drug row.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/97/020646_gabitril_toc.cfm; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Proposed: tiagabine hydrochloride; tiagabine HCl

## CRITICAL tiagabine / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The FDA label pooled placebo-controlled add-on trial adverse-event table supports dizziness 27%, nausea 11%, tremor 9%, but lists asthenia 20%, somnolence 18%, and nervousness 10%, not 23%, 21%, and 8%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: CNS: dizziness 27%, CNS: asthenia 23%, CNS: somnolence 21%, GI: nausea 11%, neurologic: tremor 9%, psychiatric: nervousness 8%
- Proposed: CNS: dizziness 27%, CNS: asthenia 20%, CNS: somnolence 18%, GI: nausea 11%, neurologic: tremor 9%, psychiatric: nervousness 10%

## HIGH tiagabine / fact_check
- Field: mechanism_of_action
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports GABA uptake-carrier blockade and increased GABA availability, but the cited FDA label wording does not specifically name GAT-1.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: Precise antiseizure mechanism is unknown, but tiagabine blocks GABA uptake by the GAT-1 GABA transporter, increasing synaptic GABA availability.
- Proposed: Precise antiseizure mechanism is unknown; tiagabine enhances GABA activity by binding to GABA uptake-carrier recognition sites and blocking GABA uptake into presynaptic neurons, increasing GABA available for postsynaptic receptor binding.

## HIGH tiagabine / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports the mechanism. DailyMed should not be needed as the named source when an FDA label URL is available.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA labeling

## CRITICAL tiagabine / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: FDA labeling supports initiation at 4 mg once daily and usual adult maintenance of 32-56 mg/day in induced patients; it does not support 16 mg/day as a common lower maintenance dose.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: 16 mg/day common lower maintenance; titrate to 32-56 mg/day depending on enzyme-inducing ASMs
- Proposed: Start 4 mg once daily; titrate by 4-8 mg/week. Usual adult maintenance in enzyme-induced patients: 32-56 mg/day in 2-4 divided doses; lower/slower dosing is required in non-induced patients.

## MEDIUM tiagabine / fact_check
- Field: qt_interval_effect
- Status: missing_source
- Approval required: True
- Summary: The row gives no named trusted source for a QT assessment, and reviewed FDA labeling did not provide a dedicated QT-effect statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: NR/no trusted source cited for clinically meaningful QT-effect assessment.

## MEDIUM tiagabine / fact_check
- Field: status_or_notes
- Status: missing_source
- Approval required: False
- Summary: FDA labeling supports adjunctive use for partial seizures in patients 12 years and older. The row's limited-use characterization is not specifically sourced.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: Current/limited-use ASM for focal/partial seizures.
- Proposed: Current adjunctive ASM for focal/partial seizures in adults and children 12 years and older.

## HIGH tiagabine / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: The current evidence_sources include DailyMed and non-listed external organizations. The proposed source list uses trusted sources that actually support the retained facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/97/020646_gabitril_toc.cfm; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548376/; https://www.ncbi.nlm.nih.gov/books/NBK2597/?report=reader
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling; FDA/openFDA labeling; NCBI Bookshelf LiverTox; NCBI Bookshelf The Epilepsies; PubMed RCT records

## HIGH tiagabine / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: PubMed abstract describes a randomized, double-blind, add-on, placebo-controlled, parallel, multicenter dose-response tiagabine study, but it appears to be a secondary cognitive/quality-of-life report of the same dose-response trial rather than a primary efficacy report. Add only if the CSV intends to track all RCT reports, including secondary reports.
- Sources: https://pubmed.ncbi.nlm.nih.gov/9109894/
- Proposed: Dodrill1997|https://pubmed.ncbi.nlm.nih.gov/9109894/

## HIGH tiagabine / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is plausible, but the row cites DailyMed for the boxed-warning field, which violates the audit policy. Use FDA/openFDA or FDA label metadata instead.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22tiagabine%22+OR+openfda.brand_name:%22tiagabine%22+OR+openfda.substance_name:%22tiagabine%22&limit=10
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in reviewed FDA label/openFDA labeling.

## MEDIUM tiagabine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22tiagabine%22+OR+openfda.brand_name:%22tiagabine%22+OR+openfda.substance_name:%22tiagabine%22&limit=10
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=72b7f357-8827-4a8b-b55a-01fbce47ae80; published=Aug 08, 2016; title=GABITRIL (TIAGABINE HYDROCHLORIDE) TABLET, FILM COATED [CARILION MATERIALS MANAGEMENT]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=72b7f357-8827-4a8b-b55a-01fbce47ae80
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=953ef3cc-e3cb-480f-b9ea-256520fd62b8; effective_time=20210930; title=Tiagabine Hydrochloride / TIAGABINE HYDROCHLORIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22tiagabine%22+OR+openfda.brand_name:%22tiagabine%22+OR+openfda.substance_name:%22tiagabine%22&limit=10

## MEDIUM tiagabine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Use the FDA label source that directly supports the proposed mechanism text.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA labeling

## MEDIUM tiagabine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace unsupported/non-trusted source names with trusted sources used in the audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/97/020646_gabitril_toc.cfm; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548376/; https://www.ncbi.nlm.nih.gov/books/NBK2597/?report=reader
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling; FDA/openFDA labeling; NCBI Bookshelf LiverTox; NCBI Bookshelf The Epilepsies; PubMed RCT records

## CRITICAL tiagabine / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: FDA label pooled placebo-controlled add-on trial adverse-event table contradicts three percentages.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: CNS: dizziness 27%, CNS: asthenia 23%, CNS: somnolence 21%, GI: nausea 11%, neurologic: tremor 9%, psychiatric: nervousness 8%
- Proposed: CNS: dizziness 27%, CNS: asthenia 20%, CNS: somnolence 18%, GI: nausea 11%, neurologic: tremor 9%, psychiatric: nervousness 10%

## MEDIUM tiagabine / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: Important FDA salt-name aliases are missing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/97/020646_gabitril_toc.cfm; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Proposed: tiagabine hydrochloride; tiagabine HCl

## MEDIUM tiagabine / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification; use FDA/openFDA/FDA label wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22tiagabine%22+OR+openfda.brand_name:%22tiagabine%22+OR+openfda.substance_name:%22tiagabine%22&limit=10
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in reviewed FDA label/openFDA labeling.

## MEDIUM tiagabine / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Replace DailyMed boxed-warning source with FDA/openFDA metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22tiagabine%22+OR+openfda.brand_name:%22tiagabine%22+OR+openfda.substance_name:%22tiagabine%22&limit=10
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=72b7f357-8827-4a8b-b55a-01fbce47ae80; published=Aug 08, 2016; title=GABITRIL (TIAGABINE HYDROCHLORIDE) TABLET, FILM COATED [CARILION MATERIALS MANAGEMENT]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=72b7f357-8827-4a8b-b55a-01fbce47ae80
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=953ef3cc-e3cb-480f-b9ea-256520fd62b8; effective_time=20210930; title=Tiagabine Hydrochloride / TIAGABINE HYDROCHLORIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.generic_name:%22tiagabine%22+OR+openfda.brand_name:%22tiagabine%22+OR+openfda.substance_name:%22tiagabine%22&limit=10

## MEDIUM tiagabine / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: Audit verification was performed on 2026-05-21 using FDA/openFDA/FDA-label sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## MEDIUM tiagabine / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use named trusted sources that support the retained cell facts; remove DailyMed and non-trusted list sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/97/020646_gabitril_toc.cfm; https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548376/; https://www.ncbi.nlm.nih.gov/books/NBK2597/?report=reader
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA/Drugs@FDA labeling; FDA/openFDA labeling; NCBI Bookshelf LiverTox; NCBI Bookshelf The Epilepsies; PubMed RCT records

## MEDIUM tiagabine / proposed_row_update
- Field: mechanism_of_action
- Status: proposed
- Approval required: False
- Summary: Align mechanism text with FDA labeling; GAT-1-specific wording is not supported by the named FDA label source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: Precise antiseizure mechanism is unknown, but tiagabine blocks GABA uptake by the GAT-1 GABA transporter, increasing synaptic GABA availability.
- Proposed: Precise antiseizure mechanism is unknown; tiagabine enhances GABA activity by binding to GABA uptake-carrier recognition sites and blocking GABA uptake into presynaptic neurons, increasing GABA available for postsynaptic receptor binding.

## MEDIUM tiagabine / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA label alone supports the proposed mechanism wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA labeling

## CRITICAL tiagabine / proposed_row_update
- Field: minimum_effective_dose
- Status: proposed
- Approval required: True
- Summary: FDA dosing text supports 4 mg initiation and usual adult maintenance of 32-56 mg/day in induced patients, not 16 mg/day as common lower maintenance.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: 16 mg/day common lower maintenance; titrate to 32-56 mg/day depending on enzyme-inducing ASMs
- Proposed: Start 4 mg once daily; titrate by 4-8 mg/week. Usual adult maintenance in enzyme-induced patients: 32-56 mg/day in 2-4 divided doses; lower/slower dosing is required in non-induced patients.

## CRITICAL tiagabine / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: True
- Summary: No trusted row source was cited for the QT claim.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: NR/no trusted source cited for clinically meaningful QT-effect assessment.

## MEDIUM tiagabine / proposed_row_update
- Field: status_or_notes
- Status: proposed
- Approval required: False
- Summary: FDA label supports current adjunctive partial-seizure use in patients 12 years and older; limited-use wording is not specifically sourced.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2010/020646s017lbl.pdf
- Current: Current/limited-use ASM for focal/partial seizures.
- Proposed: Current adjunctive ASM for focal/partial seizures in adults and children 12 years and older.

## HIGH topiramate / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: USL255 is the development/formulation name used for Qudexy XR/topiramate extended-release in phase III epilepsy trial literature; without this alias, the row misses relevant RCT evidence for the same active drug.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24902983/; https://clinicaltrials.gov/study/NCT01142193
- Proposed: USL255; topiramate extended-release

## HIGH topiramate / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism is supported by FDA labeling; the row should cite the FDA label directly rather than mixed FDA/DailyMed wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA TOPAMAX prescribing information (Drugs@FDA label)

## CRITICAL topiramate / fact_check
- Field: maximum_approved_daily_dose
- Status: incorrect
- Approval required: True
- Summary: Current FDA labeling supports 400 mg/day as the adult epilepsy dose ceiling for labeled use. The "up to 1000 mg/day" phrase reflects older trial dose-ranging, not a current approved daily dose statement in the cited current FDA label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf
- Current: 400 mg/day for most adult epilepsy indications; up to 1000 mg/day in older adjunctive labeling
- Proposed: 400 mg/day for current FDA-approved adult epilepsy indications; adult adjunctive partial-onset/LGS dosing is 200-400 mg/day, adult adjunctive PGTC and monotherapy dosing is 400 mg/day, and doses above 400 mg/day have not been shown to improve adult partial-onset responses.

## CRITICAL topiramate / fact_check
- Field: typical_doses_per_day
- Status: incorrect
- Approval required: True
- Summary: The current FDA label supports 200-400 mg/day adult adjunctive partial-onset/LGS dosing and 400 mg/day adult PGTC/monotherapy dosing. The "higher" phrase is not supported as current typical approved dosing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf
- Current: Adults epilepsy: 200-400 mg/day divided or once daily XR; higher for some adjunctive regimens
- Proposed: Adults epilepsy: 200-400 mg/day; immediate-release products are generally given in two divided doses and extended-release products once daily.

## CRITICAL topiramate / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The current values mix percentages from different dose/indication contexts and are not supported as a coherent set by the current FDA label table for adult adjunctive epilepsy at 200-400 mg/day.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf
- Current: Neurologic: paresthesia 51%, CNS: somnolence 29%, CNS: dizziness 25%, cognitive: psychomotor slowing 21%, constitutional: fatigue 16%, metabolic: weight loss 16%
- Proposed: Adult adjunctive epilepsy, FDA recommended-dose pooled trials: CNS: somnolence 29%, CNS: dizziness 25%, constitutional: fatigue 15%, cognitive: psychomotor slowing 13%, neurologic: paresthesia 11%, metabolic: weight loss 9%

## HIGH topiramate / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: Epilepsy Society and Epilepsy Foundation Australia are not in the provided trusted-domain list, and DailyMed is impermissible for boxed-warning verification. The retained facts can be supported by FDA, NCBI, PubMed, and ClinicalTrials.gov sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548632/; https://clinicaltrials.gov/study/NCT01142193
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA TOPAMAX prescribing information; FDA/openFDA labeling; NCBI LiverTox topiramate; PubMed RCT abstracts; ClinicalTrials.gov records

## HIGH topiramate / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: USL255 is Qudexy XR/topiramate extended-release. PREVAIL was a global phase III randomized, double-blind, placebo-controlled adjunctive trial in refractory partial-onset seizures, so it is same-active-drug RCT evidence and should not be omitted because the alias differs from generic topiramate.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24902983/
- Proposed: Chung2014|https://pubmed.ncbi.nlm.nih.gov/24902983/

## HIGH topiramate / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: This is a randomized, double-blind, placebo-controlled adjunctive topiramate epilepsy trial. It appears underpowered/negative and does not add extractable maximum-effective-dose outcome values, but it qualifies for the PubMed RCT link list.
- Sources: https://pubmed.ncbi.nlm.nih.gov/16140593/
- Proposed: Kerr2005|https://pubmed.ncbi.nlm.nih.gov/16140593/

## HIGH topiramate / outcome_check
- Field: diff_50_responder_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Existing immediate-release topiramate RR50 differentials are supported by the cited RCT abstracts/tables, but the same-drug USL255/Qudexy XR phase III RCT reports an extractable placebo-adjusted RR50 differential of 37.9% minus 23.2% = 14.7%, which changes the minimum of the range.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24902983/; https://clinicaltrials.gov/study/NCT01142193; https://pubmed.ncbi.nlm.nih.gov/21672344/; https://pubmed.ncbi.nlm.nih.gov/10999555/; https://pubmed.ncbi.nlm.nih.gov/10612342/; https://pubmed.ncbi.nlm.nih.gov/10371538/; https://pubmed.ncbi.nlm.nih.gov/10227615/; https://pubmed.ncbi.nlm.nih.gov/10227614/
- Current: 19-43 % (drug minus placebo RR50 differential...)
- Proposed: 14.7-43 % (drug minus placebo RR50 differential at maximum effective dose/regimen; add Chung2014 USL255/topiramate ER 200 mg/day 14.7% to the existing verified entries)

## HIGH topiramate / outcome_check
- Field: diff_median_pct_change_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Existing immediate-release median percent-change differentials are supported, but FDA review/USL255 trial evidence reports median seizure-frequency reduction of 39.50% with USL255 versus 21.65% with placebo, differential 17.85% rounded to 17.9%, changing the minimum range.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2014/205122Orig1s000MedR.pdf; https://pubmed.ncbi.nlm.nih.gov/24902983/; https://pubmed.ncbi.nlm.nih.gov/12225311/; https://pubmed.ncbi.nlm.nih.gov/10612342/; https://pubmed.ncbi.nlm.nih.gov/10371538/; https://pubmed.ncbi.nlm.nih.gov/10227615/; https://pubmed.ncbi.nlm.nih.gov/10227614/
- Current: 19.9-58 % (drug minus placebo MPC differential...)
- Proposed: 17.9-58 % (drug minus placebo MPC differential at maximum effective dose/regimen; add Chung2014 USL255/topiramate ER 200 mg/day 17.9% to the existing verified entries)

## HIGH topiramate / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is supported by FDA labeling, but the current row wording and source rely on DailyMed, which is not permissible for the boxed-warning field under the audit rule.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA label.

## MEDIUM topiramate / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for boxed-warning verification in this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=e2a4df59-fead-4a01-9021-9eda02c48010; published=Mar 23, 2026; title=EPRONTIA (TOPIRAMATE) SOLUTION [AZURITY PHARMACEUTICALS, INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=e2a4df59-fead-4a01-9021-9eda02c48010
- Proposed: FDA label and FDA/openFDA only; status=no_boxed_warning_identified_in_selected_fda_sources; TOPAMAX label revised 03/2026 url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf; EPRONTIA/topiramate openFDA label API spl_set_id=e2a4df59-fead-4a01-9021-9eda02c48010 api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22e2a4df59-fead-4a01-9021-9eda02c48010%22&limit=5

## MEDIUM topiramate / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism text is directly supported by FDA label section 12.1; cite FDA label rather than DailyMed wording.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA TOPAMAX prescribing information (Drugs@FDA label)

## MEDIUM topiramate / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replaces non-trusted or insufficiently specific source names with trusted sources that support the row facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK548632/; https://clinicaltrials.gov/study/NCT01142193; https://pubmed.ncbi.nlm.nih.gov/24902983/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA TOPAMAX prescribing information; FDA/openFDA labeling; NCBI LiverTox topiramate; PubMed RCT abstracts; ClinicalTrials.gov records

## MEDIUM topiramate / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: USL255/Qudexy XR is a topiramate extended-release alias used in phase III RCT literature.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24902983/; https://clinicaltrials.gov/study/NCT01142193
- Proposed: USL255; topiramate extended-release

## MEDIUM topiramate / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: False
- Summary: Adds missing same-active-drug placebo-controlled randomized trial reports for USL255/topiramate ER and Kerr2005.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24902983/; https://pubmed.ncbi.nlm.nih.gov/16140593/
- Current: Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/; Novotny2010|https://pubmed.ncbi.nlm.nih.gov/20089937/; Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/; Yen2000|https://pubmed.ncbi.nlm.nih.gov/10999555/; Sachdeo1999|https://pubmed.ncbi.nlm.nih.gov/10371538/; PMID1999|https://pubmed.ncbi.nlm.nih.gov/10612342/; Elterman1999|https://pubmed.ncbi.nlm.nih.gov/10227615/; Biton1999|https://pubmed.ncbi.nlm.nih.gov/10227614/; Faught1997|https://pubmed.ncbi.nlm.nih.gov/9092954/; Tassinari1996|https://pubmed.ncbi.nlm.nih.gov/8764816/; Sharief1996|https://pubmed.ncbi.nlm.nih.gov/8956919/; Privitera1996|https://pubmed.ncbi.nlm.nih.gov/8649569/; Faught1996|https://pubmed.ncbi.nlm.nih.gov/8649570/; BenMenachem1996|https://pubmed.ncbi.nlm.nih.gov/8641230/
- Proposed: Chung2014|https://pubmed.ncbi.nlm.nih.gov/24902983/; Zhang2011|https://pubmed.ncbi.nlm.nih.gov/21672344/; Novotny2010|https://pubmed.ncbi.nlm.nih.gov/20089937/; Kerr2005|https://pubmed.ncbi.nlm.nih.gov/16140593/; Guberman2002|https://pubmed.ncbi.nlm.nih.gov/12225311/; Yen2000|https://pubmed.ncbi.nlm.nih.gov/10999555/; Sachdeo1999|https://pubmed.ncbi.nlm.nih.gov/10371538/; PMID1999|https://pubmed.ncbi.nlm.nih.gov/10612342/; Elterman1999|https://pubmed.ncbi.nlm.nih.gov/10227615/; Biton1999|https://pubmed.ncbi.nlm.nih.gov/10227614/; Faught1997|https://pubmed.ncbi.nlm.nih.gov/9092954/; Tassinari1996|https://pubmed.ncbi.nlm.nih.gov/8764816/; Sharief1996|https://pubmed.ncbi.nlm.nih.gov/8956919/; Privitera1996|https://pubmed.ncbi.nlm.nih.gov/8649569/; Faught1996|https://pubmed.ncbi.nlm.nih.gov/8649570/; BenMenachem1996|https://pubmed.ncbi.nlm.nih.gov/8641230/

## MEDIUM topiramate / proposed_row_update
- Field: diff_50_responder_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Includes missing USL255/topiramate ER phase III RCT outcome; existing listed immediate-release values otherwise check out.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24902983/
- Current: 19-43 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Zhang2011 topiramate 200 mg/day 40.3%; Yen2000 topiramate 300 mg/day 34.8%; PMID1999 topiramate 600 mg/day 37.7%; Sachdeo1999 topiramate approximately 6 mg/kg/day 25%; Elterman1999 topiramate 6 mg/kg/day 19%; Biton1999 topiramate approximately 6 mg/kg/day 36%; Sharief1996 topiramate 400 mg/day 27%; Tassinari1996 topiramate 600 mg/day 37%; Faught1996 topiramate 400 mg/day 29%; Privitera1996 topiramate 600 mg/day 35%; BenMenachem1996 topiramate up to 800 mg/day 43%)
- Proposed: 14.7-43 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Chung2014 USL255/topiramate ER 200 mg/day 14.7%; Zhang2011 topiramate 200 mg/day 40.3%; Yen2000 topiramate 300 mg/day 34.8%; PMID1999 topiramate 600 mg/day 37.7%; Sachdeo1999 topiramate approximately 6 mg/kg/day 25%; Elterman1999 topiramate 6 mg/kg/day 19%; Biton1999 topiramate approximately 6 mg/kg/day 36%; Sharief1996 topiramate 400 mg/day 27%; Tassinari1996 topiramate 600 mg/day 37%; Faught1996 topiramate 400 mg/day 29%; Privitera1996 topiramate 600 mg/day 35%; BenMenachem1996 topiramate up to 800 mg/day 43%)

## MEDIUM topiramate / proposed_row_update
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Adds same-active-drug USL255/topiramate ER RR50 differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/24902983/
- Current: Zhang2011|40.3|https://pubmed.ncbi.nlm.nih.gov/21672344/|86; Yen2000|34.8|https://pubmed.ncbi.nlm.nih.gov/10999555/|46; Sachdeo1999|25|https://pubmed.ncbi.nlm.nih.gov/10371538/|98; PMID1999|37.7|https://pubmed.ncbi.nlm.nih.gov/10612342/|177; Elterman1999|19|https://pubmed.ncbi.nlm.nih.gov/10227615/|86; Biton1999|36|https://pubmed.ncbi.nlm.nih.gov/10227614/|80; Tassinari1996|37|https://pubmed.ncbi.nlm.nih.gov/8764816/|60; Sharief1996|27|https://pubmed.ncbi.nlm.nih.gov/8956919/|47; Privitera1996|35|https://pubmed.ncbi.nlm.nih.gov/8649569/|190; Faught1996|29|https://pubmed.ncbi.nlm.nih.gov/8649570/|181; BenMenachem1996|43|https://pubmed.ncbi.nlm.nih.gov/8641230/|56
- Proposed: Chung2014|14.7|https://pubmed.ncbi.nlm.nih.gov/24902983/|249; Zhang2011|40.3|https://pubmed.ncbi.nlm.nih.gov/21672344/|86; Yen2000|34.8|https://pubmed.ncbi.nlm.nih.gov/10999555/|46; Sachdeo1999|25|https://pubmed.ncbi.nlm.nih.gov/10371538/|98; PMID1999|37.7|https://pubmed.ncbi.nlm.nih.gov/10612342/|177; Elterman1999|19|https://pubmed.ncbi.nlm.nih.gov/10227615/|86; Biton1999|36|https://pubmed.ncbi.nlm.nih.gov/10227614/|80; Tassinari1996|37|https://pubmed.ncbi.nlm.nih.gov/8764816/|60; Sharief1996|27|https://pubmed.ncbi.nlm.nih.gov/8956919/|47; Privitera1996|35|https://pubmed.ncbi.nlm.nih.gov/8649569/|190; Faught1996|29|https://pubmed.ncbi.nlm.nih.gov/8649570/|181; BenMenachem1996|43|https://pubmed.ncbi.nlm.nih.gov/8641230/|56

## MEDIUM topiramate / proposed_row_update
- Field: diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Adds same-active-drug USL255/topiramate ER median percent-change differential.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2014/205122Orig1s000MedR.pdf; https://pubmed.ncbi.nlm.nih.gov/24902983/
- Current: 19.9-58 % (drug minus placebo MPC differential at maximum effective dose/regimen: Guberman2002 topiramate 200 mg/day 24%; PMID1999 topiramate 600 mg/day 42.2%; Sachdeo1999 topiramate approximately 6 mg/kg/day 19.9%; Elterman1999 topiramate 6 mg/kg/day 22.6%; Biton1999 topiramate approximately 6 mg/kg/day 47.7%; Sharief1996 topiramate 400 mg/day 40%; Tassinari1996 topiramate 600 mg/day 58%; Faught1996 topiramate 400 mg/day 35%; Privitera1996 topiramate 600 mg/day 40%; BenMenachem1996 topiramate up to 800 mg/day 54%)
- Proposed: 17.9-58 % (drug minus placebo MPC differential at maximum effective dose/regimen: Chung2014 USL255/topiramate ER 200 mg/day 17.9%; Guberman2002 topiramate 200 mg/day 24%; PMID1999 topiramate 600 mg/day 42.2%; Sachdeo1999 topiramate approximately 6 mg/kg/day 19.9%; Elterman1999 topiramate 6 mg/kg/day 22.6%; Biton1999 topiramate approximately 6 mg/kg/day 47.7%; Sharief1996 topiramate 400 mg/day 40%; Tassinari1996 topiramate 600 mg/day 58%; Faught1996 topiramate 400 mg/day 35%; Privitera1996 topiramate 600 mg/day 40%; BenMenachem1996 topiramate up to 800 mg/day 54%)

## MEDIUM topiramate / proposed_row_update
- Field: plot_diff_median_pct_change_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Adds same-active-drug USL255/topiramate ER MPC differential.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/nda/2014/205122Orig1s000MedR.pdf; https://pubmed.ncbi.nlm.nih.gov/24902983/
- Current: Guberman2002|24|https://pubmed.ncbi.nlm.nih.gov/12225311/|263; Sachdeo1999|19.9|https://pubmed.ncbi.nlm.nih.gov/10371538/|98; PMID1999|42.2|https://pubmed.ncbi.nlm.nih.gov/10612342/|177; Elterman1999|22.6|https://pubmed.ncbi.nlm.nih.gov/10227615/|86; Biton1999|47.7|https://pubmed.ncbi.nlm.nih.gov/10227614/|80; Tassinari1996|58|https://pubmed.ncbi.nlm.nih.gov/8764816/|60; Sharief1996|40|https://pubmed.ncbi.nlm.nih.gov/8956919/|47; Privitera1996|40|https://pubmed.ncbi.nlm.nih.gov/8649569/|190; Faught1996|35|https://pubmed.ncbi.nlm.nih.gov/8649570/|181; BenMenachem1996|54|https://pubmed.ncbi.nlm.nih.gov/8641230/|56
- Proposed: Chung2014|17.9|https://pubmed.ncbi.nlm.nih.gov/24902983/|249; Guberman2002|24|https://pubmed.ncbi.nlm.nih.gov/12225311/|263; Sachdeo1999|19.9|https://pubmed.ncbi.nlm.nih.gov/10371538/|98; PMID1999|42.2|https://pubmed.ncbi.nlm.nih.gov/10612342/|177; Elterman1999|22.6|https://pubmed.ncbi.nlm.nih.gov/10227615/|86; Biton1999|47.7|https://pubmed.ncbi.nlm.nih.gov/10227614/|80; Tassinari1996|58|https://pubmed.ncbi.nlm.nih.gov/8764816/|60; Sharief1996|40|https://pubmed.ncbi.nlm.nih.gov/8956919/|47; Privitera1996|40|https://pubmed.ncbi.nlm.nih.gov/8649569/|190; Faught1996|35|https://pubmed.ncbi.nlm.nih.gov/8649570/|181; BenMenachem1996|54|https://pubmed.ncbi.nlm.nih.gov/8641230/|56

## CRITICAL topiramate / proposed_row_update
- Field: maximum_approved_daily_dose
- Status: proposed
- Approval required: True
- Summary: Current FDA labeling does not support 1000 mg/day as a current approved dose statement.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf
- Current: 400 mg/day for most adult epilepsy indications; up to 1000 mg/day in older adjunctive labeling
- Proposed: 400 mg/day for current FDA-approved adult epilepsy indications; adult adjunctive partial-onset/LGS dosing is 200-400 mg/day, adult adjunctive PGTC and monotherapy dosing is 400 mg/day, and doses above 400 mg/day have not been shown to improve adult partial-onset responses.

## CRITICAL topiramate / proposed_row_update
- Field: typical_doses_per_day
- Status: proposed
- Approval required: True
- Summary: Removes unsupported current-dose wording about higher adjunctive regimens.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf
- Current: Adults epilepsy: 200-400 mg/day divided or once daily XR; higher for some adjunctive regimens
- Proposed: Adults epilepsy: 200-400 mg/day; immediate-release products are generally given in two divided doses and extended-release products once daily.

## CRITICAL topiramate / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: Replaces mixed-context adverse-event percentages with a coherent FDA-label table for adult adjunctive epilepsy at recommended doses.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2026/020505s068lbl.pdf
- Current: Neurologic: paresthesia 51%, CNS: somnolence 29%, CNS: dizziness 25%, cognitive: psychomotor slowing 21%, constitutional: fatigue 16%, metabolic: weight loss 16%
- Proposed: Adult adjunctive epilepsy, FDA recommended-dose pooled trials: CNS: somnolence 29%, CNS: dizziness 25%, constitutional: fatigue 15%, cognitive: psychomotor slowing 13%, neurologic: paresthesia 11%, metabolic: weight loss 9%

## MEDIUM topiramate / proposed_row_update
- Field: data_most_recently_refreshed
- Status: proposed
- Approval required: False
- Summary: Audit performed with current-date source checks on 2026-05-21.
- Current: 05-20-2026
- Proposed: 05-21-2026

## HIGH trimethadione / fact_check
- Field: alternate_generic_names
- Status: missing
- Approval required: False
- Summary: NCBI MeSH lists Troxidone and Trimetin as entry terms for trimethadione. Tridione is already captured as the trade name.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68014293
- Proposed: Troxidone; Trimetin

## HIGH trimethadione / fact_check
- Field: pubmed_search_aliases
- Status: incorrect
- Approval required: False
- Summary: PubMed/MeSH search should include the MeSH entry terms to avoid duplicate alias rows and improve retrieval.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68014293
- Current: Tridione
- Proposed: Tridione; Troxidone; Trimetin

## CRITICAL trimethadione / fact_check
- Field: epilepsy_type
- Status: incorrect
- Approval required: True
- Summary: FDA label states Tridione is indicated for control of refractory petit mal seizures; the current row incorrectly says no specific FDA-labeled seizure category is available.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)
- Proposed: Petit mal/absence seizures refractory to treatment with other drugs (historical FDA-labeled indication).

## CRITICAL trimethadione / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: FDA label lists adverse reactions by category, but without percentage incidence; the no-label rationale is contradicted by the FDA label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A - FDA-approved Tridione label lists adverse reactions but does not provide incidence percentages.

## CRITICAL trimethadione / fact_check
- Field: major_organ_for_metabolism
- Status: incorrect
- Approval required: True
- Summary: FDA label provides metabolism information identifying liver microsomal demethylation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Liver - trimethadione is demethylated by liver microsomes to active metabolite dimethadione.

## CRITICAL trimethadione / fact_check
- Field: filter_metabolism
- Status: incorrect
- Approval required: True
- Summary: The label identifies liver microsomal metabolism, so the filter should not remain limited/unknown if hepatic is an available category.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: Limited/unknown
- Proposed: Hepatic/liver microsomal

## CRITICAL trimethadione / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: True
- Summary: N/A is plausible, but the row rationale should cite the FDA label rather than saying no label exists.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe enzyme induction or inhibition.
- Proposed: N/A - FDA label does not state that trimethadione induces or inhibits drug-metabolizing enzymes.

## CRITICAL trimethadione / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: True
- Summary: FDA label describes absorption, metabolism, and excretion but does not state a half-life.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: N/A - FDA label does not state a half-life.

## CRITICAL trimethadione / fact_check
- Field: qt_interval_effect
- Status: incorrect
- Approval required: True
- Summary: No QT text was found in the FDA label, but the no-label rationale is incorrect.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe QT effect.
- Proposed: N/A - FDA label does not describe a QT interval effect.

## CRITICAL trimethadione / fact_check
- Field: maximum_approved_daily_dose
- Status: incorrect
- Approval required: True
- Summary: FDA label provides adult dosage range and divided dosing.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a maximum approved daily dose.
- Proposed: 2.4 g/day (usual adult dosage range 0.9-2.4 g/day).

## CRITICAL trimethadione / fact_check
- Field: minimum_effective_dose
- Status: incorrect
- Approval required: True
- Summary: FDA label provides initial adult dosing and maintenance principle.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a minimum effective dose.
- Proposed: Adult initial dose 0.9 g/day; FDA label does not state a fixed minimum effective dose and says maintenance should be the least amount required to maintain control.

## CRITICAL trimethadione / fact_check
- Field: typical_doses_per_day
- Status: incorrect
- Approval required: True
- Summary: FDA label states adult and pediatric dosing is given in 3 or 4 divided doses.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide dosing.
- Proposed: 3 or 4 divided doses daily.

## CRITICAL trimethadione / fact_check
- Field: mechanism_of_action
- Status: incorrect
- Approval required: True
- Summary: FDA label provides limited pharmacology; Orange Book alone is not the best mechanism source.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Unclear/limited - FDA label identifies trimethadione as an oxazolidinedione antiepileptic and describes animal anticonvulsant activity, but does not state a molecular mechanism.

## CRITICAL trimethadione / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: True
- Summary: The mechanism/pharmacology facts are supported by the FDA label, not the Orange Book products file.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: FDA Orange Book products file
- Proposed: FDA accessdata Tridione label (Description/Clinical Pharmacology)

## CRITICAL trimethadione / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: True
- Summary: DailyMed should not be used for the black-box field, and the FDA accessdata label is needed for indication, dosing, metabolism, adverse reactions, and warning facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.ncbi.nlm.nih.gov/mesh/68014293; https://www.epilepsy.com/stories/community-corner-new-drug-alerts
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA accessdata/Drugs@FDA Tridione (trimethadione) label; NCBI MeSH/PubMed search audit; Epilepsy Foundation availability note.

## CRITICAL trimethadione / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: True
- Summary: The FDA accessdata label for Tridione (trimethadione) exists and contains a top-of-label warning. DailyMed was not used for this check.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2012/005856s021ltr.pdf
- Current: No current FDA/DailyMed label identified.
- Proposed: Potential fetal malformations and serious side effects; reserve Tridione for petit mal seizures not controlled by less toxic drugs.

## CRITICAL trimethadione / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: True
- Summary: DailyMed should not be used for black-box verification, and the FDA accessdata label supports many row facts currently marked unavailable.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf; https://www.fda.gov/drugs/drug-approvals-and-databases/orange-book-data-files; https://www.ncbi.nlm.nih.gov/mesh/68014293; https://www.epilepsy.com/stories/community-corner-new-drug-alerts
- Current: FDA Orange Book products file; FDA/DailyMed labeling
- Proposed: FDA Orange Book products file; FDA accessdata/Drugs@FDA Tridione (trimethadione) label; NCBI MeSH/PubMed search audit; Epilepsy Foundation availability note.

## CRITICAL trimethadione / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: True
- Summary: FDA label was found; DailyMed is not permissible for this field.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2012/005856s021ltr.pdf
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [trimethadione; Tridione].
- Proposed: FDA accessdata Tridione (trimethadione) label, NDA 005856/S-021, approved 06-06-2012; top warning/boxed warning verified 05-21-2026.

## CRITICAL trimethadione / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: True
- Summary: Orange Book does not support the mechanism/pharmacology wording; FDA label does.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: FDA Orange Book products file
- Proposed: FDA accessdata Tridione label (Description/Clinical Pharmacology)

## MEDIUM trimethadione / proposed_row_update
- Field: data_most_recently_refreshed
- Status: proposed
- Approval required: False
- Summary: Audit performed against FDA/NCBI/PubMed sources on 05-21-2026.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## CRITICAL trimethadione / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: FDA label exists and lists adverse reactions without incidence rates.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A 0%: no current FDA/DailyMed label identified; FDA Orange Book product listing does not provide adverse-event percentages.
- Proposed: N/A - FDA-approved Tridione label lists adverse reactions but does not provide incidence percentages.

## MEDIUM trimethadione / proposed_row_update
- Field: alternate_generic_names
- Status: proposed
- Approval required: False
- Summary: NCBI MeSH entry terms for trimethadione.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68014293
- Proposed: Troxidone; Trimetin

## CRITICAL trimethadione / proposed_row_update
- Field: epilepsy_type
- Status: proposed
- Approval required: True
- Summary: FDA label gives the seizure category.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: Historical/unspecified epilepsy (specific FDA-labeled seizure category not available from Orange Book listing)
- Proposed: Petit mal/absence seizures refractory to treatment with other drugs (historical FDA-labeled indication).

## CRITICAL trimethadione / proposed_row_update
- Field: filter_epilepsy_type
- Status: proposed
- Approval required: True
- Summary: Align filter with FDA-labeled indication.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: Historical/unspecified epilepsy
- Proposed: Petit mal/absence seizures

## CRITICAL trimethadione / proposed_row_update
- Field: fda_black_box_warning
- Status: proposed
- Approval required: True
- Summary: FDA accessdata label contains a top warning; DailyMed was not used.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2012/005856s021ltr.pdf
- Current: No current FDA/DailyMed label identified.
- Proposed: Potential fetal malformations and serious side effects; reserve Tridione for petit mal seizures not controlled by less toxic drugs.

## CRITICAL trimethadione / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: True
- Summary: Black-box warning verification must use FDA sources only; FDA label was identified.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/appletter/2012/005856s021ltr.pdf
- Current: FDA/DailyMed search on 05-20-2026: no current label found for terms [trimethadione; Tridione].
- Proposed: FDA accessdata Tridione (trimethadione) label, NDA 005856/S-021, approved 06-06-2012; top warning/boxed warning verified 05-21-2026.

## MEDIUM trimethadione / proposed_row_update
- Field: fda_black_box_warning_verified
- Status: proposed
- Approval required: False
- Summary: FDA warning re-verified during this audit.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: 05-20-2026
- Proposed: 05-21-2026

## CRITICAL trimethadione / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: True
- Summary: Corrects source rationale while retaining unknown enzyme effect.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe enzyme induction or inhibition.
- Proposed: N/A - FDA label does not state that trimethadione induces or inhibits drug-metabolizing enzymes.

## CRITICAL trimethadione / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: FDA label exists but lacks half-life.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide half-life.
- Proposed: N/A - FDA label does not state a half-life.

## CRITICAL trimethadione / proposed_row_update
- Field: major_organ_for_metabolism
- Status: proposed
- Approval required: True
- Summary: FDA label provides hepatic metabolism information.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide metabolism information.
- Proposed: Liver - trimethadione is demethylated by liver microsomes to active metabolite dimethadione.

## CRITICAL trimethadione / proposed_row_update
- Field: filter_metabolism
- Status: proposed
- Approval required: True
- Summary: FDA label identifies liver microsomal demethylation.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: Limited/unknown
- Proposed: Hepatic/liver microsomal

## CRITICAL trimethadione / proposed_row_update
- Field: maximum_approved_daily_dose
- Status: proposed
- Approval required: True
- Summary: FDA label provides adult dosage range.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a maximum approved daily dose.
- Proposed: 2.4 g/day (usual adult dosage range 0.9-2.4 g/day).

## CRITICAL trimethadione / proposed_row_update
- Field: minimum_effective_dose
- Status: proposed
- Approval required: True
- Summary: FDA label provides initial dosing and maintenance principle.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide a minimum effective dose.
- Proposed: Adult initial dose 0.9 g/day; FDA label does not state a fixed minimum effective dose and says maintenance should be the least amount required to maintain control.

## CRITICAL trimethadione / proposed_row_update
- Field: mechanism_of_action
- Status: proposed
- Approval required: True
- Summary: FDA label provides limited pharmacology; current no-label rationale is incorrect.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located; FDA Orange Book confirms historical U.S. product approval/listing but does not provide mechanism of action.
- Proposed: Unclear/limited - FDA label identifies trimethadione as an oxazolidinedione antiepileptic and describes animal anticonvulsant activity, but does not state a molecular mechanism.

## CRITICAL trimethadione / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: True
- Summary: Mechanism/pharmacology is supported by FDA label rather than Orange Book.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: FDA Orange Book products file
- Proposed: FDA accessdata Tridione label (Description/Clinical Pharmacology)

## CRITICAL trimethadione / proposed_row_update
- Field: mechanism_source_tier
- Status: proposed
- Approval required: True
- Summary: The supporting source is a historical FDA-approved label.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: Historical/limited
- Proposed: FDA label/historical

## MEDIUM trimethadione / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Adds NCBI MeSH entry terms for the same drug.
- Sources: https://www.ncbi.nlm.nih.gov/mesh/68014293
- Current: Tridione
- Proposed: Tridione; Troxidone; Trimetin

## CRITICAL trimethadione / proposed_row_update
- Field: qt_interval_effect
- Status: proposed
- Approval required: True
- Summary: FDA label exists but does not mention QT.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not describe QT effect.
- Proposed: N/A - FDA label does not describe a QT interval effect.

## MEDIUM trimethadione / proposed_row_update
- Field: rct_pubmed_verification_notes
- Status: proposed
- Approval required: False
- Summary: Updates alias coverage and audit date.
- Sources: https://pubmed.ncbi.nlm.nih.gov/?term=%28trimethadione+OR+Tridione+OR+Troxidone+OR+Trimetin%29+%28placebo+OR+randomized+OR+double-blind%29+epilepsy; https://www.ncbi.nlm.nih.gov/mesh/68014293
- Current: No qualifying phase II/III placebo-controlled randomized epilepsy RCT was retained in the PubMed RCT audit/gap review as of 05-19-2026; RCT section set to N/A per current scope.
- Proposed: No qualifying phase II/III placebo-controlled randomized epilepsy RCT was located in PubMed for trimethadione/Tridione/Troxidone/Trimetin as of 05-21-2026; RCT/outcome fields remain N/A.

## CRITICAL trimethadione / proposed_row_update
- Field: typical_doses_per_day
- Status: proposed
- Approval required: True
- Summary: FDA label provides dosing frequency.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2012/005856s021lbl.pdf
- Current: N/A - no current FDA/DailyMed label located and FDA Orange Book product listing does not provide dosing.
- Proposed: 3 or 4 divided doses daily.

## CRITICAL valproic acid / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The FDA Depakote ER label adverse-reaction table supporting the other listed percentages reports vomiting at 27%, not 23%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/021168s044lbl.pdf
- Current: GI: nausea 48%, CNS: somnolence 27%, neurologic: tremor 25%, CNS: dizziness 25%, GI: vomiting 23%, dermatologic: alopecia 6%
- Proposed: GI: nausea 48%, CNS: somnolence 27%, neurologic: tremor 25%, CNS: dizziness 25%, GI: vomiting 27%, dermatologic: alopecia 6%

## HIGH valproic acid / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed-warning verification and Epilepsy Society is outside the allowed trusted-source domain list. Replace with trusted FDA, NCBI/PubMed/PMC, and ClinicalTrials.gov sources that support the row facts.
- Sources: https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/valproate-information; https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5; https://www.ncbi.nlm.nih.gov/books/NBK559112/
- Current: FDA Orange Book products file; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review; NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list
- Proposed: FDA Orange Book products file; FDA/accessdata labeling; FDA/openFDA labeling; FDA Valproate Information page; NCBI Bookshelf/StatPearls; NCBI LiverTox; PubMed/PMC RCT reports; ClinicalTrials.gov

## HIGH valproic acid / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: The current source uses DailyMed, which is explicitly not permitted for black-box-warning verification. FDA/openFDA is permitted.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=0dc024ce-efc8-4690-7cb5-639c728fccac; published=Apr 13, 2026; title=DEPAKOTE ER (DIVALPROEX SODIUM) TABLET, EXTENDED RELEASE [ABBVIE INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0dc024ce-efc8-4690-7cb5-639c728fccac
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=0dc024ce-efc8-4690-7cb5-639c728fccac; effective_time=20260331; title=DEPAKOTE ER / DIVALPROEX SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5

## HIGH valproic acid / fact_check
- Field: mechanism_source
- Status: incorrect
- Approval required: False
- Summary: The mechanism fact can be supported without DailyMed by FDA/accessdata labeling and NCBI Bookshelf. This also aligns with the trusted-source-domain policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/021168s044lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK559112/
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; NCBI Bookshelf/StatPearls mechanism review

## HIGH valproic acid / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: Add standalone valproate and FDA-listed Depakote CP/Depakote Sprinkle Capsules variants to improve alias coverage. Existing aliases are appropriate for the consolidated active-moiety row.
- Sources: https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/valproate-information; https://www.ema.europa.eu/en/medicines/human/referrals/valproate-related-substances
- Current: divalproex sodium; sodium valproate; valproate semisodium; valproate sodium; Depacon; Depakote; Depakote ER; Depakote Sprinkles; Depakene; Depakine; Epilim; Epival
- Proposed: valproate; divalproex sodium; sodium valproate; valproate semisodium; valproate sodium; Depacon; Depakote; Depakote CP; Depakote ER; Depakote Sprinkle Capsules; Depakote Sprinkles; Depakene; Depakine; Epilim; Epival

## MEDIUM valproic acid / fact_check
- Field: qt_interval_effect
- Status: missing_source
- Approval required: False
- Summary: No trusted row source specifically supports a QT-effect conclusion. The statement is plausible as an absence-of-established-effect claim, but it should not be treated as source-verified from the current evidence_sources.
- Current: No clinically meaningful QT effect established
- Proposed: No clinically meaningful QT effect established

## HIGH valproic acid / fact_check
- Field: trade_names
- Status: missing
- Approval required: False
- Summary: FDA sources support Depacon, Depakene, Depakote, Depakote ER, Depakote CP, and valproate sodium products; EMA/eMC sources support non-US brands such as Convulex, Depakine, Dyzantil, and Epilim variants. Depakyn and Epival were not independently verified from the allowed source set in this pass, but no direct contradiction was found, so they are retained.
- Sources: https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/valproate-information; https://www.ema.europa.eu/en/medicines/human/referrals/valproate-related-substances; https://www.medicines.org.uk/emc/product/6102/smpc
- Current: Convulex; Depacon; Depakene; Depakine; Depakote; Depakote ER; Depakote Sprinkles; Depakyn; Dyzantil; Epilim Chrono; Epilim Chronosphere; Epival; Stavzor; Valproate Sodium
- Proposed: Convulex; Depacon; Depakene; Depakine; Depakote; Depakote CP; Depakote ER; Depakote Sprinkle Capsules; Depakote Sprinkles; Depakyn; Dyzantil; Epilim Chrono; Epilim Chronosphere; Epival; Stavzor; Valproate Sodium

## HIGH valproic acid / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: Although the record is randomized/placebo-controlled, it is a haem-biosynthesis/porphyria safety/pharmacology study in healthy subjects and established monotherapy patients, not a seizure-frequency epilepsy efficacy RCT for valproate.
- Sources: https://pubmed.ncbi.nlm.nih.gov/3130256/
- Current: https://pubmed.ncbi.nlm.nih.gov/3130256/
- Proposed: Do not add to pubmed_phase_ii_iii_rct_links.

## HIGH valproic acid / rct_link_check
- Field: pubmed_phase_ii_iii_rct_links
- Status: not_phase_ii_iii
- Approval required: True
- Summary: This is a phase II pharmacokinetic drug-drug interaction study of cannabidiol with stiripentol or valproate in epilepsy patients, not a valproate placebo-controlled seizure-efficacy RCT.
- Sources: https://pubmed.ncbi.nlm.nih.gov/32350749/
- Current: https://pubmed.ncbi.nlm.nih.gov/32350749/
- Proposed: Do not add to pubmed_phase_ii_iii_rct_links.

## MEDIUM valproic acid / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not allowed for black-box-warning verification.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=0dc024ce-efc8-4690-7cb5-639c728fccac; published=Apr 13, 2026; title=DEPAKOTE ER (DIVALPROEX SODIUM) TABLET, EXTENDED RELEASE [ABBVIE INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0dc024ce-efc8-4690-7cb5-639c728fccac
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=0dc024ce-efc8-4690-7cb5-639c728fccac; effective_time=20260331; title=DEPAKOTE ER / DIVALPROEX SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5

## MEDIUM valproic acid / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace non-allowed or insufficient source names with trusted-source domains used in this audit.
- Sources: https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/valproate-information; https://www.ncbi.nlm.nih.gov/books/NBK559112/; https://pubmed.ncbi.nlm.nih.gov/8559420/
- Current: FDA Orange Book products file; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review; NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list
- Proposed: FDA Orange Book products file; FDA/accessdata labeling; FDA/openFDA labeling; FDA Valproate Information page; NCBI Bookshelf/StatPearls; NCBI LiverTox; PubMed/PMC RCT reports; ClinicalTrials.gov

## MEDIUM valproic acid / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: FDA/accessdata and NCBI sources support the mechanism wording while avoiding DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/021168s044lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK559112/
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; NCBI Bookshelf/StatPearls mechanism review

## CRITICAL valproic acid / proposed_row_update
- Field: adverse_symptoms_percentages
- Status: proposed
- Approval required: True
- Summary: FDA label table supporting the listed adverse-event percentages reports vomiting 27%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/021168s044lbl.pdf
- Current: GI: nausea 48%, CNS: somnolence 27%, neurologic: tremor 25%, CNS: dizziness 25%, GI: vomiting 23%, dermatologic: alopecia 6%
- Proposed: GI: nausea 48%, CNS: somnolence 27%, neurologic: tremor 25%, CNS: dizziness 25%, GI: vomiting 27%, dermatologic: alopecia 6%

## MEDIUM valproic acid / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: Black-box source must be FDA/openFDA, FDA labels, or Drugs@FDA only; DailyMed is not permissible.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=0dc024ce-efc8-4690-7cb5-639c728fccac; published=Apr 13, 2026; title=DEPAKOTE ER (DIVALPROEX SODIUM) TABLET, EXTENDED RELEASE [ABBVIE INC.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=0dc024ce-efc8-4690-7cb5-639c728fccac
- Proposed: FDA/openFDA drug label API; status=boxed_warning_found; spl_set_id=0dc024ce-efc8-4690-7cb5-639c728fccac; effective_time=20260331; title=DEPAKOTE ER / DIVALPROEX SODIUM; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%220dc024ce-efc8-4690-7cb5-639c728fccac%22&limit=5

## MEDIUM valproic acid / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Use only trusted-source domains and remove DailyMed/Epilepsy Society as row support sources for this audit context.
- Sources: https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/valproate-information; https://www.ncbi.nlm.nih.gov/books/NBK559112/; https://pubmed.ncbi.nlm.nih.gov/8559420/
- Current: FDA Orange Book products file; FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review; NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list
- Proposed: FDA Orange Book products file; FDA/accessdata labeling; FDA/openFDA labeling; FDA Valproate Information page; NCBI Bookshelf/StatPearls; NCBI LiverTox; PubMed/PMC RCT reports; ClinicalTrials.gov

## MEDIUM valproic acid / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The mechanism statement is supported by trusted FDA and NCBI sources without using DailyMed.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2023/021168s044lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK559112/
- Current: FDA/DailyMed labeling; Sills and Rogawski 2020 ASM mechanism review
- Proposed: FDA/accessdata labeling; NCBI Bookshelf/StatPearls mechanism review

## MEDIUM valproic acid / proposed_row_update
- Field: diff_50_responder_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Numerically correct, but the RCT intervention was divalproex sodium; this wording is more exact.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8559420/
- Current: 19 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Willmore1996 add-on divalproex sodium/valproate 19%)
- Proposed: 19 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Willmore1996 add-on divalproex sodium 19%)

## MEDIUM valproic acid / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: Add standalone valproate and FDA-listed Depakote CP/Depakote Sprinkle Capsules variants.
- Sources: https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/valproate-information
- Current: divalproex sodium; sodium valproate; valproate semisodium; valproate sodium; Depacon; Depakote; Depakote ER; Depakote Sprinkles; Depakene; Depakine; Epilim; Epival
- Proposed: valproate; divalproex sodium; sodium valproate; valproate semisodium; valproate sodium; Depacon; Depakote; Depakote CP; Depakote ER; Depakote Sprinkle Capsules; Depakote Sprinkles; Depakene; Depakine; Epilim; Epival

## MEDIUM valproic acid / proposed_row_update
- Field: trade_names
- Status: proposed
- Approval required: False
- Summary: Add FDA-listed Depakote CP and formal Depakote Sprinkle Capsules alias; retain uncontradicted existing names.
- Sources: https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/valproate-information; https://www.ema.europa.eu/en/medicines/human/referrals/valproate-related-substances; https://www.medicines.org.uk/emc/product/6102/smpc
- Current: Convulex; Depacon; Depakene; Depakine; Depakote; Depakote ER; Depakote Sprinkles; Depakyn; Dyzantil; Epilim Chrono; Epilim Chronosphere; Epival; Stavzor; Valproate Sodium
- Proposed: Convulex; Depacon; Depakene; Depakine; Depakote; Depakote CP; Depakote ER; Depakote Sprinkle Capsules; Depakote Sprinkles; Depakyn; Dyzantil; Epilim Chrono; Epilim Chronosphere; Epival; Stavzor; Valproate Sodium

## CRITICAL vigabatrin / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: True
- Summary: The current values mix unsupported or placebo/other-dose values. FDA labeling gives adult CPS 3000 mg/day values of fatigue 23%, somnolence 22%, dizziness 24%, tremor 15%, and weight gain 6%; pediatric CPS weight gain is 15%; infantile-spasm somnolence is 45% vs placebo 30%.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/217684s000lbl.pdf
- Current: CNS: somnolence 24%, constitutional: fatigue 24%, ophthalmologic: visual field loss 30% or more with chronic exposure, CNS: dizziness 12%, metabolic: weight gain 10%, neurologic: tremor 8%
- Proposed: CNS: somnolence 22% (adult CPS 3000 mg/day; 45% in infantile-spasm placebo-controlled study), CNS: dizziness 24% (adult CPS 3000 mg/day), constitutional: fatigue 23% (adult CPS 3000 mg/day), neurologic: tremor 15% (adult CPS 3000 mg/day), metabolic: weight gain 6% (adult CPS 3000 mg/day; 15% pediatric CPS), ophthalmologic: permanent vision loss/visual field defects, 30% or more in adults with chronic exposure

## INFO vigabatrin / fact_check
- Field: alternate_generic_names
- Status: not_applicable
- Approval required: False
- Summary: No separate generic alias must be added here because the important literature alias is already handled in pubmed_search_aliases; no duplicate-drug row evidence was found in the bundle.
- Sources: https://pubmed.ncbi.nlm.nih.gov/3514204/; https://pubmed.ncbi.nlm.nih.gov/6141335/

## CRITICAL vigabatrin / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: True
- Summary: FDA labeling directly states vigabatrin is not significantly metabolized and is primarily renally excreted, but also states it induces CYP2C9. The current text incorrectly says it is not an inducer.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: Not significantly metabolized; not an enzyme inducer/inhibitor
- Proposed: Not significantly metabolized; eliminated primarily by renal excretion; induces CYP2C9 but does not induce other hepatic cytochrome P450 systems.

## HIGH vigabatrin / fact_check
- Field: evidence_sources
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not permissible for boxed warning verification, and Epilepsy Society/Epilepsy Foundation Australia are not in the requested trusted-domain list. The proposed sources support the row facts on trusted domains.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf; https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/sabril-vigabatrin; https://www.ncbi.nlm.nih.gov/books/NBK548253/; https://www.ncbi.nlm.nih.gov/books/NBK548365/table/Anticonvulsants.Tc/; https://www.ema.europa.eu/en/medicines/human/EPAR/kigabeq; https://www.medicines.org.uk/emc/product/14629/smpc; https://clinicaltrials.gov/study/NCT02849457
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov); FDA Sabril safety page; NCBI LiverTox vigabatrin record and anticonvulsants table; EMA/eMC Kigabeq product information; PubMed RCT abstracts; ClinicalTrials.gov NCT02849457

## HIGH vigabatrin / fact_check
- Field: fda_black_box_warning_source
- Status: incorrect
- Approval required: False
- Summary: DailyMed is not allowed for this field. FDA accessdata labeling supports the boxed warning.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=a88ac1b4-e2c9-45c0-b321-4785902172e3; published=Dec 17, 2025; title=SABRIL (VIGABATRIN) POWDER, FOR SOLUTION [LUNDBECK PHARMACEUTICALS LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a88ac1b4-e2c9-45c0-b321-4785902172e3
- Proposed: FDA prescribing information (accessdata.fda.gov); status=boxed_warning_found; application=NDA020427/NDA022006; label=020427s025,022006s026; revised=10/2021; title=SABRIL (vigabatrin) tablets, for oral use; SABRIL (vigabatrin) for oral solution; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf

## HIGH vigabatrin / fact_check
- Field: formulations_available
- Status: incorrect
- Approval required: False
- Summary: FDA Sabril labeling supports tablets and powder for oral solution; FDA Vigafyde labeling supports oral solution; EMA/eMC supports Kigabeq soluble tablets.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/217684s000lbl.pdf; https://www.medicines.org.uk/emc/product/14629/smpc
- Current: Tablet; powder for oral solution
- Proposed: Tablet; powder for oral solution; oral solution; soluble tablet (Kigabeq EU/UK)

## CRITICAL vigabatrin / fact_check
- Field: half_life_range
- Status: incorrect
- Approval required: True
- Summary: FDA labeling gives a longer adult and adolescent terminal half-life than the current row range.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: 5-8 h
- Proposed: 5.7-10.5 h (age-dependent: infants 5.7 h, children 6.8 h, adolescents 9.5 h, adults 10.5 h)

## MEDIUM vigabatrin / fact_check
- Field: mechanism_source
- Status: missing_source
- Approval required: False
- Summary: The fact is FDA-label supported, but the source text should avoid DailyMed and point to FDA labeling.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov)

## MEDIUM vigabatrin / fact_check
- Field: pubmed_search_aliases
- Status: missing_source
- Approval required: False
- Summary: Existing PubMed trial titles use both spacing/hyphenation variants; adding the hyphenated form improves alias coverage without creating a duplicate drug row.
- Sources: https://pubmed.ncbi.nlm.nih.gov/3514204/; https://pubmed.ncbi.nlm.nih.gov/3130253/; https://pubmed.ncbi.nlm.nih.gov/6141335/
- Current: gamma-vinyl GABA
- Proposed: gamma-vinyl GABA; gamma-vinyl-GABA

## HIGH vigabatrin / missing_rct
- Field: pubmed_phase_ii_iii_rct_links
- Status: missing
- Approval required: False
- Summary: This appears to be a primary double-blind placebo-controlled vigabatrin 3 g/day trial in uncontrolled complex partial seizures and corresponds to FDA label Study 2, which reports RR50 39% on vigabatrin 3 g/day versus 21% placebo.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8559421/
- Proposed: French1996|https://pubmed.ncbi.nlm.nih.gov/8559421/

## HIGH vigabatrin / outcome_check
- Field: diff_50_responder_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: The listed values are supported by the cited outcome evidence, but the row appears to omit French1996/FDA Study 2, where 39% on vigabatrin 3 g/day versus 21% placebo gives an 18-point differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/41500178/; https://pubmed.ncbi.nlm.nih.gov/10777431/; https://pubmed.ncbi.nlm.nih.gov/9924905/; https://pubmed.ncbi.nlm.nih.gov/8089668/; https://pubmed.ncbi.nlm.nih.gov/8559421/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: 22-44 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Kalita2025 vigabatrin add-on regimen 42.8%; Bruni2000 vigabatrin adult add-on regimen 22%; Dean1999 vigabatrin 3 g/day 44%; Grunewald1994 vigabatrin 3 g/day 32.61%)
- Proposed: 18-44 % (drug minus placebo RR50 differential at maximum effective dose/regimen: Kalita2025 vigabatrin add-on regimen 42.8%; Bruni2000 vigabatrin adult add-on regimen 22%; Dean1999 vigabatrin 3 g/day 44%; French1996 vigabatrin 3 g/day 18%; Grunewald1994 vigabatrin 3 g/day 32.61%)

## HIGH vigabatrin / outcome_check
- Field: plot_diff_50_responder_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: Add the missing French1996/FDA Study 2 extractable RR50 differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8559421/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: Kalita2025|42.8|https://pubmed.ncbi.nlm.nih.gov/41500178/|100; Bruni2000|22|https://pubmed.ncbi.nlm.nih.gov/10777431/|111; Dean1999|44|https://pubmed.ncbi.nlm.nih.gov/9924905/|174; Grunewald1994|32.61|https://pubmed.ncbi.nlm.nih.gov/8089668/|45
- Proposed: Kalita2025|42.8|https://pubmed.ncbi.nlm.nih.gov/41500178/|100; Bruni2000|22|https://pubmed.ncbi.nlm.nih.gov/10777431/|111; Dean1999|44|https://pubmed.ncbi.nlm.nih.gov/9924905/|174; French1996|18|https://pubmed.ncbi.nlm.nih.gov/8559421/|183; Grunewald1994|32.61|https://pubmed.ncbi.nlm.nih.gov/8089668/|45

## MEDIUM vigabatrin / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: False
- Summary: Replace non-trusted or non-compliant source names with trusted-domain sources that support the populated facts.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf; https://www.fda.gov/drugs/postmarket-drug-safety-information-patients-and-providers/sabril-vigabatrin; https://www.ncbi.nlm.nih.gov/books/NBK548253/; https://www.ncbi.nlm.nih.gov/books/NBK548365/table/Anticonvulsants.Tc/; https://www.ema.europa.eu/en/medicines/human/EPAR/kigabeq; https://www.medicines.org.uk/emc/product/14629/smpc; https://clinicaltrials.gov/study/NCT02849457
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov); FDA Sabril safety page; NCBI LiverTox vigabatrin record and anticonvulsants table; EMA/eMC Kigabeq product information; PubMed RCT abstracts; ClinicalTrials.gov NCT02849457

## MEDIUM vigabatrin / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: The mechanism is FDA-label supported; DailyMed should not be named as the row source when an FDA label URL is available.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA prescribing information (accessdata.fda.gov)

## MEDIUM vigabatrin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: FDA boxed warning source must be FDA/openFDA, FDA label, or Drugs@FDA; DailyMed is not permissible.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=a88ac1b4-e2c9-45c0-b321-4785902172e3; published=Dec 17, 2025; title=SABRIL (VIGABATRIN) POWDER, FOR SOLUTION [LUNDBECK PHARMACEUTICALS LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a88ac1b4-e2c9-45c0-b321-4785902172e3
- Proposed: FDA prescribing information (accessdata.fda.gov); status=boxed_warning_found; application=NDA020427/NDA022006; label=020427s025,022006s026; revised=10/2021; title=SABRIL (vigabatrin) tablets, for oral use; SABRIL (vigabatrin) for oral solution; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf

## MEDIUM vigabatrin / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for FDA boxed warning verification.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: FDA/DailyMed SPL; status=boxed_warning_found; setid=a88ac1b4-e2c9-45c0-b321-4785902172e3; published=Dec 17, 2025; title=SABRIL (VIGABATRIN) POWDER, FOR SOLUTION [LUNDBECK PHARMACEUTICALS LLC]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=a88ac1b4-e2c9-45c0-b321-4785902172e3
- Proposed: FDA prescribing information (accessdata.fda.gov); status=boxed_warning_found; application=NDA020427/NDA022006; label=020427s025,022006s026; revised=10/2021; title=SABRIL (vigabatrin) tablets, for oral use; SABRIL (vigabatrin) for oral solution; url=https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf

## CRITICAL vigabatrin / proposed_row_update
- Field: half_life_range
- Status: proposed
- Approval required: True
- Summary: FDA labeling contradicts the current upper bound.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: 5-8 h
- Proposed: 5.7-10.5 h (age-dependent: infants 5.7 h, children 6.8 h, adolescents 9.5 h, adults 10.5 h)

## CRITICAL vigabatrin / proposed_row_update
- Field: enzyme_inducing_or_inhibiting
- Status: proposed
- Approval required: True
- Summary: FDA labeling says vigabatrin induces CYP2C9.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: Not significantly metabolized; not an enzyme inducer/inhibitor
- Proposed: Not significantly metabolized; eliminated primarily by renal excretion; induces CYP2C9 but does not induce other hepatic cytochrome P450 systems.

## MEDIUM vigabatrin / proposed_row_update
- Field: formulations_available
- Status: proposed
- Approval required: False
- Summary: The row lists Vigafyde and Kigabeq but omits their oral-solution/soluble-tablet formulations.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2024/217684s000lbl.pdf; https://www.medicines.org.uk/emc/product/14629/smpc
- Current: Tablet; powder for oral solution
- Proposed: Tablet; powder for oral solution; oral solution; soluble tablet (Kigabeq EU/UK)

## MEDIUM vigabatrin / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: PubMed trial titles use both alias spellings.
- Sources: https://pubmed.ncbi.nlm.nih.gov/3514204/; https://pubmed.ncbi.nlm.nih.gov/3130253/
- Current: gamma-vinyl GABA
- Proposed: gamma-vinyl GABA; gamma-vinyl-GABA

## MEDIUM vigabatrin / proposed_row_update
- Field: pubmed_phase_ii_iii_rct_links
- Status: proposed
- Approval required: False
- Summary: French1996 appears to be a missing primary placebo-controlled vigabatrin RCT and is supported by FDA label Study 2.
- Sources: https://pubmed.ncbi.nlm.nih.gov/8559421/; https://www.accessdata.fda.gov/drugsatfda_docs/label/2021/020427s025%2C022006s026lbl.pdf
- Current: Kalita2025|https://pubmed.ncbi.nlm.nih.gov/41500178/; Bebin2023|https://pubmed.ncbi.nlm.nih.gov/37638552/; Bruni2000|https://pubmed.ncbi.nlm.nih.gov/10777431/; Dean1999|https://pubmed.ncbi.nlm.nih.gov/9924905/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10565592/; Beran1996|https://pubmed.ncbi.nlm.nih.gov/8952010/; Jackson1994|https://pubmed.ncbi.nlm.nih.gov/7957035/; Grunewald1994|https://pubmed.ncbi.nlm.nih.gov/8089668/; Gillham1993|https://pubmed.ncbi.nlm.nih.gov/8270925/; PMID1992|https://pubmed.ncbi.nlm.nih.gov/1483856/; Cosi1989|https://pubmed.ncbi.nlm.nih.gov/2757911/; Cosi1988|https://pubmed.ncbi.nlm.nih.gov/3130253/; Tassinari1987|https://pubmed.ncbi.nlm.nih.gov/2887152/; Tartara1986|https://pubmed.ncbi.nlm.nih.gov/3536469/; Loiseau1986|https://pubmed.ncbi.nlm.nih.gov/3514204/; Rimmer1984|https://pubmed.ncbi.nlm.nih.gov/6141335/
- Proposed: Kalita2025|https://pubmed.ncbi.nlm.nih.gov/41500178/; Bebin2023|https://pubmed.ncbi.nlm.nih.gov/37638552/; Bruni2000|https://pubmed.ncbi.nlm.nih.gov/10777431/; Dean1999|https://pubmed.ncbi.nlm.nih.gov/9924905/; Appleton1999|https://pubmed.ncbi.nlm.nih.gov/10565592/; Beran1996|https://pubmed.ncbi.nlm.nih.gov/8952010/; French1996|https://pubmed.ncbi.nlm.nih.gov/8559421/; Jackson1994|https://pubmed.ncbi.nlm.nih.gov/7957035/; Grunewald1994|https://pubmed.ncbi.nlm.nih.gov/8089668/; Gillham1993|https://pubmed.ncbi.nlm.nih.gov/8270925/; PMID1992|https://pubmed.ncbi.nlm.nih.gov/1483856/; Cosi1989|https://pubmed.ncbi.nlm.nih.gov/2757911/; Cosi1988|https://pubmed.ncbi.nlm.nih.gov/3130253/; Tassinari1987|https://pubmed.ncbi.nlm.nih.gov/2887152/; Tartara1986|https://pubmed.ncbi.nlm.nih.gov/3536469/; Loiseau1986|https://pubmed.ncbi.nlm.nih.gov/3514204/; Rimmer1984|https://pubmed.ncbi.nlm.nih.gov/6141

## HIGH zonisamide / fact_check
- Field: pubmed_search_aliases
- Status: missing
- Approval required: False
- Summary: RCT evidence summaries commonly abbreviate zonisamide as ZNS, so this is a useful PubMed/search alias.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK327367/bin/appl-et1.pdf
- Proposed: ZNS

## MEDIUM zonisamide / fact_check
- Field: trade_names
- Status: insufficient_evidence
- Approval required: False
- Summary: Zonegran and Zonisade are verified by FDA labeling. Desizon was not verified from the trusted sources available in this audit, so retain only if a trusted eMC/SmPC or EMA source is added. Do not add 'Zonisamide' as a trade name; it is the generic name, not a proprietary name.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2000/20789lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: Desizon; Zonegran; Zonisade
- Proposed: Desizon; Zonegran; Zonisade

## CRITICAL zonisamide / fact_check
- Field: maximum_approved_daily_dose
- Status: incorrect
- Approval required: True
- Summary: Current FDA Zonisade labeling states patients tolerating 400 mg daily may be increased to a maximum dosage of 600 mg daily, while also noting controlled trials show no increased response above 400 mg/day.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: 400 mg/day
- Proposed: 600 mg/day; usual target 400 mg/day, with labeling noting no evidence of increasing response above 400 mg/day

## HIGH zonisamide / fact_check
- Field: typical_doses_per_day
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports once- or twice-daily administration, initial 100 mg/day, titration to 400 mg/day, and possible increase to 600 mg/day.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: Adults: 100-400 mg/day once daily or divided
- Proposed: Adults: 100-400 mg/day once daily or divided; selected patients may be increased to 600 mg/day per FDA labeling

## HIGH zonisamide / fact_check
- Field: enzyme_inducing_or_inhibiting
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports insignificant CYP inhibition, CYP3A4 metabolism, and carbonic anhydrase inhibition. The label does not frame the carbonic anhydrase effect as 'weak'.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: Not a major inducer/inhibitor; CYP3A4 substrate; weak carbonic anhydrase inhibitor
- Proposed: Not expected to affect other drugs via CYP450-mediated mechanisms; metabolized partly by CYP3A4; carbonic anhydrase inhibitor

## HIGH zonisamide / fact_check
- Field: mechanism_of_action
- Status: incorrect
- Approval required: False
- Summary: FDA labeling supports the sodium-channel, T-type calcium-current, and carbonic-anhydrase statements; it does not use 'weak' for the carbonic-anhydrase effect.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: Precise mechanism is unknown; in vitro data suggest sodium-channel blockade and reduced T-type calcium currents, with weak carbonic-anhydrase inhibition of uncertain therapeutic contribution.
- Proposed: Precise mechanism is unknown; in vitro data suggest sodium-channel blockade and reduced T-type calcium currents, with carbonic-anhydrase inhibition of uncertain therapeutic contribution.

## CRITICAL zonisamide / fact_check
- Field: filter_mechanism
- Status: incorrect
- Approval required: True
- Summary: Alpha-2-delta is not supported for zonisamide. FDA labeling supports sodium channels, T-type calcium currents, and carbonic anhydrase inhibition.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: Calcium channel / alpha-2-delta; Sodium channel
- Proposed: Calcium channel / T-type; Sodium channel; Carbonic anhydrase inhibitor

## MEDIUM zonisamide / fact_check
- Field: epilepsy_type
- Status: missing_source
- Approval required: True
- Summary: FDA labeling supports adjunctive treatment of partial-onset seizures. The cited row sources do not verify generalized or primary generalized tonic-clonic use as a supported row fact.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf; https://clinicaltrials.gov/study/NCT00692003
- Current: Focal; Generalized; Primary generalized tonic-clonic
- Proposed: Focal/partial-onset seizures; generalized and primary generalized tonic-clonic use require an added trusted source or should be marked off-label/not verified

## HIGH zonisamide / fact_check
- Field: adverse_symptoms_percentages
- Status: incorrect
- Approval required: False
- Summary: FDA labeling verifies somnolence, anorexia, dizziness, and ataxia percentages. The 6% cognitive events are reported as confusion, difficulty concentrating, and difficulty with memory rather than the exact term 'abnormal thinking'.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2000/20789lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: CNS: somnolence 17%, GI: anorexia 13%, CNS: dizziness 13%, neurologic: ataxia 6%, cognitive: abnormal thinking 6%, renal/metabolic: kidney stones 4% over development program
- Proposed: CNS: somnolence 17%, GI: anorexia 13%, CNS: dizziness 13%, neurologic: ataxia 6%, cognitive: confusion/difficulty concentrating/difficulty with memory 6%, renal/metabolic: kidney stones 4% over development program

## MEDIUM zonisamide / fact_check
- Field: qt_interval_effect
- Status: missing_source
- Approval required: False
- Summary: The reviewed FDA labels do not establish a clinically meaningful QT effect, but absence of a QT warning is narrower than proof of no clinically meaningful QT effect.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: No clinically meaningful QT effect established
- Proposed: No FDA QT-prolongation warning identified in reviewed FDA labeling

## MEDIUM zonisamide / fact_check
- Field: status_or_notes
- Status: missing_source
- Approval required: True
- Summary: FDA labeling supports partial-onset seizure use. The migraine/weight-related off-label statement is not supported by the row's named trusted evidence sources.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: Current ASM for focal/partial seizures; also used off-label for migraine/weight-related indications in some settings.
- Proposed: Current ASM for adjunctive treatment of focal/partial-onset seizures; non-epilepsy off-label uses require added trusted sources if retained.

## HIGH zonisamide / outcome_check
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: NCBI evidence tables report Lu2011 seizure freedom as 3/52 for zonisamide versus 1/50 for placebo, so the current NR statement is not fully correct.
- Sources: https://pubmed.ncbi.nlm.nih.gov/21166480/; https://www.ncbi.nlm.nih.gov/books/NBK327367/bin/appl-et1.pdf
- Current: NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records
- Proposed: 3.8 % (drug minus placebo seizure-freedom patient-rate differential extractable from Lu2011 pooled zonisamide 300-400 mg/day: 3/52 [5.8%] vs 1/50 [2.0%]; no dose-specific 400 mg/day seizure-freedom differential extractable from included abstracts/evidence summaries)

## HIGH zonisamide / outcome_check
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: incorrect
- Approval required: False
- Summary: A pooled Lu2011 seizure-freedom differential is extractable, although not dose-specific to the 400 mg/day arm.
- Sources: https://pubmed.ncbi.nlm.nih.gov/21166480/; https://www.ncbi.nlm.nih.gov/books/NBK327367/bin/appl-et1.pdf
- Proposed: Lu2011|3.8|https://pubmed.ncbi.nlm.nih.gov/21166480/|104

## HIGH zonisamide / black_box_warning
- Field: fda_black_box_warning
- Status: incorrect
- Approval required: False
- Summary: The no-boxed-warning conclusion is plausible, but the current row relies on DailyMed, which is not permissible for this field. Use FDA/openFDA or FDA accessdata label metadata instead.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d12de43e-3ac3-4335-bc85-70d7366a91eb%22&limit=5; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: No FDA boxed warning identified in selected current DailyMed label.
- Proposed: No FDA boxed warning identified in selected current FDA/openFDA label.

## CRITICAL zonisamide / proposed_row_update
- Field: evidence_sources
- Status: proposed
- Approval required: True
- Summary: The current evidence_sources field names DailyMed and non-whitelisted epilepsy organization sources. The retained row facts should cite trusted source domains from the audit policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2000/20789lbl.pdf; https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf; https://www.ncbi.nlm.nih.gov/books/NBK327367/bin/appl-et1.pdf; https://pubmed.ncbi.nlm.nih.gov/21166480/
- Current: NCBI LiverTox anticonvulsants table; Epilepsy Society ASM list; Epilepsy Foundation Australia ASM list; FDA/DailyMed labeling
- Proposed: FDA accessdata labeling; FDA/openFDA labeling; NCBI Bookshelf/PubMed RCT evidence summaries; PubMed RCT records; ClinicalTrials.gov where trial-registry facts are used

## MEDIUM zonisamide / proposed_row_update
- Field: mechanism_source
- Status: proposed
- Approval required: False
- Summary: Mechanism facts are supported by FDA labeling; cite FDA accessdata rather than DailyMed to stay within trusted-source policy.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: FDA/DailyMed labeling
- Proposed: FDA accessdata labeling

## MEDIUM zonisamide / proposed_row_update
- Field: fda_black_box_warning_source
- Status: proposed
- Approval required: False
- Summary: DailyMed is not permissible for black-box verification; use FDA/openFDA metadata.
- Sources: https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d12de43e-3ac3-4335-bc85-70d7366a91eb%22&limit=5
- Current: FDA/DailyMed SPL; status=no_boxed_warning_in_selected_label; setid=d12de43e-3ac3-4335-bc85-70d7366a91eb; published=Oct 03, 2025; title=ZONEGRAN (ZONISAMIDE) CAPSULE [ADVANZ PHARMA (US) CORP.]; url=https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid=d12de43e-3ac3-4335-bc85-70d7366a91eb
- Proposed: FDA/openFDA drug label API; status=no_boxed_warning_in_selected_fda_label; spl_set_id=d12de43e-3ac3-4335-bc85-70d7366a91eb; effective_time=20250912; title=Zonegran / ZONISAMIDE; api_url=https://api.fda.gov/drug/label.json?search=openfda.spl_set_id%3A%22d12de43e-3ac3-4335-bc85-70d7366a91eb%22&limit=5

## MEDIUM zonisamide / proposed_row_update
- Field: pubmed_search_aliases
- Status: proposed
- Approval required: False
- Summary: ZNS is a common zonisamide abbreviation in RCT evidence summaries.
- Sources: https://www.ncbi.nlm.nih.gov/books/NBK327367/bin/appl-et1.pdf
- Proposed: ZNS

## CRITICAL zonisamide / proposed_row_update
- Field: maximum_approved_daily_dose
- Status: proposed
- Approval required: True
- Summary: Current FDA labeling permits increase to 600 mg/day in selected patients tolerating 400 mg/day.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: 400 mg/day
- Proposed: 600 mg/day; usual target 400 mg/day, with labeling noting no evidence of increasing response above 400 mg/day

## CRITICAL zonisamide / proposed_row_update
- Field: filter_mechanism
- Status: proposed
- Approval required: True
- Summary: Alpha-2-delta is not supported; FDA labeling supports T-type calcium currents, sodium channels, and carbonic anhydrase inhibition.
- Sources: https://www.accessdata.fda.gov/drugsatfda_docs/label/2022/214273s000lbl.pdf
- Current: Calcium channel / alpha-2-delta; Sodium channel
- Proposed: Calcium channel / T-type; Sodium channel; Carbonic anhydrase inhibitor

## MEDIUM zonisamide / proposed_row_update
- Field: diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Lu2011 reports extractable seizure-freedom counts in NCBI evidence tables.
- Sources: https://pubmed.ncbi.nlm.nih.gov/21166480/; https://www.ncbi.nlm.nih.gov/books/NBK327367/bin/appl-et1.pdf
- Current: NR/not extractable as a drug-minus-placebo seizure-freedom patient-rate differential at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records
- Proposed: 3.8 % (drug minus placebo seizure-freedom patient-rate differential extractable from Lu2011 pooled zonisamide 300-400 mg/day: 3/52 [5.8%] vs 1/50 [2.0%]; no dose-specific 400 mg/day seizure-freedom differential extractable from included abstracts/evidence summaries)

## MEDIUM zonisamide / proposed_row_update
- Field: plot_diff_seizure_freedom_maximum_effective_dose
- Status: proposed
- Approval required: False
- Summary: Adds the extractable Lu2011 pooled seizure-freedom differential.
- Sources: https://pubmed.ncbi.nlm.nih.gov/21166480/; https://www.ncbi.nlm.nih.gov/books/NBK327367/bin/appl-et1.pdf
- Proposed: Lu2011|3.8|https://pubmed.ncbi.nlm.nih.gov/21166480/|104
