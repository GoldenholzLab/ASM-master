#!/usr/bin/env python3
import csv
from collections import defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
ASM_CSV = ROOT / "ASM-list.csv"
RCT_REPORT = ROOT / "pubmed_cache" / "reports" / "pubmed_rct_audit.csv"
REPORT_DIR = ROOT / "pubmed_cache" / "reports"
OUTCOME_REPORT = REPORT_DIR / "efficacy_outcome_audit.csv"
SEIZURE_FREEDOM_REPORT = REPORT_DIR / "seizure_freedom_audit.csv"
GAP_REPORT = REPORT_DIR / "efficacy_gap_review.csv"
REFRESH_DATE = "05-15-2026"

RR50_FIELD = "diff_50_responder_maximum_effective_dose"
MPC_FIELD = "diff_median_pct_change_maximum_effective_dose"
SF_FIELD = "diff_seizure_freedom_maximum_effective_dose"


def pct(value):
    if value is None:
        return None
    return round(float(value), 2)


def diff(active, placebo):
    return pct(float(active) - float(placebo))


def item(
    dose="",
    endpoint="",
    rr50=None,
    mpc=None,
    sf=None,
    rr50_diff=None,
    mpc_diff=None,
    sf_diff=None,
    include_rr50=True,
    include_mpc=True,
    include_sf=True,
    note="",
):
    rr50_active, rr50_placebo = rr50 if rr50 else (None, None)
    mpc_active, mpc_placebo = mpc if mpc else (None, None)
    sf_active, sf_placebo = sf if sf else (None, None)
    rr50_value = pct(rr50_diff) if rr50_diff is not None else diff(rr50_active, rr50_placebo) if rr50 else None
    mpc_value = pct(mpc_diff) if mpc_diff is not None else diff(mpc_active, mpc_placebo) if mpc else None
    sf_value = pct(sf_diff) if sf_diff is not None else diff(sf_active, sf_placebo) if sf else None
    return {
        "dose_or_regimen": dose,
        "endpoint": endpoint,
        "rr50_active_percent": pct(rr50_active),
        "rr50_placebo_percent": pct(rr50_placebo),
        "rr50_differential_percent": rr50_value,
        "rr50_included_in_csv_summary": "yes" if include_rr50 and rr50_value is not None else "no",
        "mpc_active_percent": pct(mpc_active),
        "mpc_placebo_percent": pct(mpc_placebo),
        "mpc_differential_percent": mpc_value,
        "mpc_included_in_csv_summary": "yes" if include_mpc and mpc_value is not None else "no",
        "sf_active_percent": pct(sf_active),
        "sf_placebo_percent": pct(sf_placebo),
        "sf_differential_percent": sf_value,
        "sf_included_in_csv_summary": "yes" if include_sf and sf_value is not None else "no",
        "audit_note": note,
    }


def reviewed(note):
    return item(note=note)


# Manual extraction map built from the included PubMed phase II/III placebo-
# controlled RCT records. Values are included when the maximum effective
# dose/regimen represented within a qualifying RCT is extractable from the
# abstract as active/placebo arm values or an explicit placebo-adjusted value.
EXTRACTIONS = {
    ("brivaracetam", "Yu2026"): item(
        dose="BRV 200 mg/day",
        endpoint="focal-onset seizures",
        rr50=(48.89, 23.86),
        sf=(11.11, 2.27),
        note="Abstract reports 200 mg/day RR50 48.89% vs 23.86% and seizure freedom 11.11% vs 2.27%. Median active/placebo reductions were not reported.",
    ),
    ("brivaracetam", "Inoue2024"): item(
        dose="BRV 200 mg/day",
        endpoint="focal-onset seizures",
        rr50=(49.3, 19.0),
        mpc=(46.7, 21.3),
        sf=(6.8, 0.0),
        note="Abstract reports the 200 mg/day arm separately; 50 mg/day was not used for the max-dose rollup.",
    ),
    ("brivaracetam", "Klein2015"): item(
        dose="BRV 200 mg/day",
        endpoint="partial-onset seizures",
        rr50=(37.8, 21.6),
        note="Abstract reports RR50 for 200 mg/day. It reports placebo-adjusted seizure-frequency reduction but not median active/placebo reductions.",
    ),
    ("brivaracetam", "Kwan2013"): item(
        dose="BRV flexible dose up to 150 mg/day",
        endpoint="focal seizures",
        rr50=(30.3, 16.7),
        mpc=(26.9, 18.9),
        note="Abstract reports focal-seizure responder and median reduction values for the flexible-dose trial; 150 mg/day was the trial maximum.",
    ),
    ("brivaracetam", "Biton2013"): reviewed("Highest dose was 50 mg/day, below the current 200 mg/day maximum effective/approved regimen."),
    ("brivaracetam", "Ryvlin2013"): reviewed("Highest dose was 100 mg/day, below the 200 mg/day maximum effective/approved regimen."),
    ("brivaracetam", "VanPaesschen2012"): reviewed("Highest dose was 150 mg/day, below the 200 mg/day maximum effective/approved regimen."),
    ("brivaracetam", "French2010"): reviewed("Highest dose was 50 mg/day, below the 200 mg/day maximum effective/approved regimen."),
    ("brivaracetam", "Kalviainen2015"): reviewed("EPM1 trials reported myoclonus-score outcomes rather than seizure-frequency RR50/MPC/seizure-freedom outcomes."),
    ("brivaracetam", "Bast2022"): reviewed("Adaptive absence-epilepsy trial design publication; no extractable efficacy-arm results."),

    ("cannabidiol", "Thiele2021"): item(
        dose="CBD 25 mg/kg/day",
        endpoint="TSC-associated seizures",
        mpc=(48.6, 26.5),
        mpc_diff=30.1,
        note="Abstract reports CBD25 active/placebo reductions and the model-based placebo-adjusted reduction of 30.1%. CBD50 was not used because 25 mg/kg/day is the approved TSC maximum.",
    ),
    ("cannabidiol", "Devinsky2018b"): item(
        dose="CBD 20 mg/kg/day",
        endpoint="LGS drop seizures",
        mpc=(41.9, 17.2),
        note="Abstract reports median percent reduction for the 20 mg/kg/day arm and placebo.",
    ),
    ("cannabidiol", "Thiele2018"): item(
        dose="CBD 20 mg/kg/day",
        endpoint="LGS drop seizures",
        mpc=(43.9, 21.8),
        note="Abstract reports median percentage reduction for 20 mg/kg/day and placebo.",
    ),
    ("cannabidiol", "Devinsky2017"): item(
        dose="CBD 20 mg/kg/day",
        endpoint="Dravet convulsive seizures",
        rr50=(43.0, 27.0),
        mpc_diff=22.8,
        sf=(5.0, 0.0),
        note="Abstract reports RR50 and seizure-free rates; MPC is the adjusted median difference reported in the abstract.",
    ),
    ("cannabidiol", "Miller2020"): item(
        dose="CBD 20 mg/kg/day",
        endpoint="Dravet convulsive seizures",
        mpc_diff=25.7,
        note="Abstract reports placebo-adjusted convulsive seizure-frequency reduction for the 20 mg/kg/day arm; RR50 and seizure freedom were not extractable from the abstract.",
    ),
    ("cannabidiol", "OBrien2022"): reviewed("Transdermal CBD focal-epilepsy study did not show a significant double-blind efficacy difference and did not report RR50 by blinded arm."),
    ("cannabidiol", "Devinsky2018"): reviewed("Dose-ranging safety/pharmacokinetic trial; no extractable placebo-adjusted efficacy outcome for max-dose rollup."),

    ("cenobamate", "Lee2025"): item(
        dose="cenobamate 400 mg/day",
        endpoint="focal seizures",
        mpc=(100.0, 25.9),
        sf=(52.4, 2.6),
        note="Abstract reports 400 mg/day median seizure-frequency change and seizure-free rates during maintenance.",
    ),
    ("cenobamate", "Krauss2019"): item(
        dose="cenobamate 400 mg/day",
        endpoint="focal seizures",
        rr50=(64.0, 25.0),
        mpc=(55.0, 24.0),
        note="Abstract reports 400 mg/day responder and median seizure-frequency reduction values.",
    ),
    ("cenobamate", "Chung2020"): item(
        dose="cenobamate 200 mg/day",
        endpoint="focal seizures",
        rr50=(50.4, 22.2),
        mpc=(55.6, 21.5),
        sf=(28.3, 8.8),
        note="Abstract reports the maximum dose tested in this phase II RCT: 200 mg/day responder, median seizure-frequency reduction, and maintenance seizure-free rates.",
    ),
    ("cenobamate", "Vossler2020"): reviewed("No PubMed abstract efficacy values available for extraction."),
    ("cenobamate", "KasteleijnNolstTrenite2019"): reviewed("Photosensitivity proof-of-principle study reported PPR suppression, not seizure-frequency RR50/MPC/seizure-freedom outcomes."),

    ("divalproex sodium", "Willmore1996"): item(
        dose="add-on divalproex sodium",
        endpoint="complex partial seizures",
        rr50=(38.0, 19.0),
        note="Abstract reports >=50% seizure-frequency reduction rates; median outcome was an absolute seizure-count reduction, not a percentage MPC.",
    ),

    ("clobazam", "Ng2011"): item(
        dose="clobazam 1.0 mg/kg/day",
        endpoint="LGS drop seizures",
        rr50=(77.6, 31.6),
        mpc=(68.3, 12.1),
        note="Abstract reports highest-dose clobazam RR50 and average weekly drop-seizure-rate decrease versus placebo.",
    ),

    ("diazepam", "Cereghino1998"): item(
        dose="single caregiver-administered rectal diazepam dose",
        endpoint="acute repetitive seizure post-treatment seizure freedom",
        sf=(55.0, 34.0),
        note="Abstract reports post-treatment seizure freedom for Diastat and placebo.",
    ),

    ("eslicarbazepine acetate", "Sperling2014"): item(
        dose="ESL 1200 mg/day",
        endpoint="partial-onset seizures",
        rr50=(42.6, 23.1),
        note="Abstract reports max-dose RR50. Median active/placebo reductions were not extractable from the abstract.",
    ),
    ("eslicarbazepine acetate", "Elger2009"): item(
        dose="ESL 1200 mg/day",
        endpoint="partial-onset seizures",
        rr50=(43.0, 20.0),
        mpc=(45.0, 16.0),
        note="Abstract reports max-dose responder and median relative seizure-frequency reduction values.",
    ),
    ("eslicarbazepine acetate", "GilNagel2009"): item(
        dose="ESL 1200 mg/day",
        endpoint="partial-onset seizures",
        rr50=(38.0, 23.0),
        mpc=(42.0, 17.0),
        note="Abstract reports 1200 mg/day responder and median relative seizure-frequency reduction values.",
    ),
    ("eslicarbazepine acetate", "BenMenachem2010"): item(
        dose="ESL 1200 mg/day",
        endpoint="partial-onset seizures",
        rr50=(37.1, 13.0),
        mpc=(32.8, 0.8),
        note="Abstract reports 1200 mg/day responder and median relative seizure-frequency reduction values.",
    ),
    ("eslicarbazepine acetate", "Elger2007"): item(
        dose="ESL titrated to 1200 mg/day once daily",
        endpoint="partial-onset seizures",
        rr50=(54.0, 28.0),
        note="Exploratory trial titrated the once-daily group to 1200 mg/day and reports responder rates. Placebo seizure-free percentage was not reported.",
    ),
    ("eslicarbazepine acetate", "Kirkham2020"): reviewed("Pediatric study used 20-30 mg/kg/day but reports LS mean relative change and no extractable max-dose RR50."),
    ("eslicarbazepine acetate", "Koepp2026"): reviewed("Post-stroke seizure-prevention proof-of-concept trial; not a seizure-frequency RR50/MPC epilepsy-treatment endpoint."),
    ("eslicarbazepine acetate", "Mintzer2018"): reviewed("Post hoc lipid analysis, not a primary efficacy report."),

    ("everolimus", "French2016"): item(
        dose="everolimus high-exposure trough 9-15 ng/mL",
        endpoint="TSC-associated focal-onset seizures",
        rr50=(40.0, 15.1),
        mpc=(39.6, 14.9),
        note="Abstract reports high-exposure response rate and median percentage seizure-frequency reduction versus placebo.",
    ),

    ("ezogabine", "French2011"): item(
        dose="ezogabine/retigabine 1200 mg/day",
        endpoint="partial-onset seizures",
        rr50=(44.4, 17.8),
        mpc=(44.3, 17.5),
        note="Abstract reports 1200 mg/day double-blind-period values.",
    ),
    ("ezogabine", "Porter2007"): item(
        dose="retigabine 1200 mg/day",
        endpoint="partial-onset seizures",
        rr50=(33.0, 16.0),
        mpc=(35.0, 13.0),
        note="Abstract reports dose-ranging 1200 mg/day values.",
    ),
    ("ezogabine", "Brodie2010"): item(
        dose="ezogabine/retigabine 900 mg/day",
        endpoint="partial-onset seizures",
        rr50=(47.0, 18.9),
        mpc=(39.9, 15.9),
        note="Abstract reports the highest effective arm in this RCT: 900 mg/day responder and median seizure-reduction values.",
    ),
    ("ezogabine", "Lim2016"): item(
        dose="ezogabine/retigabine 600 mg/day",
        endpoint="partial-onset seizures",
        rr50=(31.0, 0.0),
        mpc=(33.90, 22.21),
        note="Asian phase III trial was stopped early; abstract reports 600 mg/day as the higher-performing arm versus placebo.",
    ),

    ("felbamate", "FelbamateStudyGroupinLennoxGastautSyndrome1993"): item(
        dose="felbamate up to 45 mg/kg/day or 3600 mg/day",
        endpoint="LGS seizures",
        mpc_diff=23.0,
        note="Abstract reports total seizure frequency decreased 19% with felbamate versus a 4% increase with placebo.",
    ),
    ("felbamate", "Devinsky1995"): reviewed("Presurgical monotherapy trial reports daily seizure frequency ranks and completer seizure reductions, but no extractable active/placebo RR50, MPC, or seizure-freedom differential."),
    ("felbamate", "Siegel1999"): reviewed("Small crossover add-on study reports fewer seizures on felbamate plus valproate, but not an extractable arm-specific RR50/MPC/seizure-freedom differential."),

    ("gabapentin", "PMID1990"): item(
        dose="gabapentin 1200 mg/day",
        endpoint="partial seizures",
        rr50=(25.0, 9.8),
        mpc=(29.2, 12.5),
        note="Abstract reports 1200 mg/day responder and median partial-seizure reduction values.",
    ),

    ("fenfluramine", "Sullivan2023"): item(
        dose="fenfluramine 0.7 mg/kg/day",
        endpoint="Dravet monthly convulsive seizure frequency",
        rr50=(72.9, 6.3),
        mpc_diff=64.8,
        note="Abstract reports RR50 and a placebo-adjusted 64.8% greater reduction at 0.7 mg/kg/day.",
    ),
    ("fenfluramine", "Lagae2019"): item(
        dose="fenfluramine 0.7 mg/kg/day",
        endpoint="Dravet monthly convulsive seizure frequency",
        mpc=(74.9, 19.2),
        note="Abstract reports median reductions for 0.7 mg/kg/day and placebo; RR50 was not reported in the abstract.",
    ),
    ("fenfluramine", "Nabbout2020"): item(
        dose="fenfluramine 0.4 mg/kg/day with stiripentol",
        endpoint="Dravet monthly convulsive seizure frequency",
        rr50=(54.0, 5.0),
        mpc_diff=54.0,
        note="Abstract reports RR50 and placebo-adjusted mean monthly convulsive seizure-frequency reduction in the stiripentol-inclusive regimen max dose.",
    ),
    ("fenfluramine", "Knupp2022"): item(
        dose="fenfluramine 0.7 mg/kg/day",
        endpoint="LGS drop seizures",
        rr50=(25.0, 10.0),
        mpc_diff=19.9,
        note="Abstract reports RR50 and estimated median difference for the LGS 0.7 mg/kg/day arm.",
    ),
    ("fenfluramine", "Sullivan2021"): reviewed("Responder-analysis/NNT publication; source RCT values are captured from the primary RCT reports."),

    ("ganaxolone", "Sperling2017"): item(
        dose="ganaxolone 1500 mg/day",
        endpoint="partial-onset seizures",
        rr50=(24.0, 15.0),
        mpc=(17.6, -2.0),
        note="Abstract reports responder rates and mean percent change. The mean percent change is retained with an explicit note because a median value was not reported.",
    ),
    ("ganaxolone", "Sullivan2023"): item(
        dose="ganaxolone up to 63 mg/kg/day or 1800 mg/day",
        endpoint="PCDH19-clustering seizures",
        mpc=(61.5, 24.0),
        note="Abstract reports median percentage change in 28-day seizure frequency.",
    ),
    ("ganaxolone", "Knight2022"): item(
        dose="ganaxolone up to 63 mg/kg/day or 1800 mg/day",
        endpoint="CDD-associated major motor seizures",
        mpc_diff=27.1,
        note="Abstract reports the Hodges-Lehmann placebo-adjusted median difference for 28-day major motor seizure-frequency change.",
    ),
    ("ganaxolone", "Downs2024"): reviewed("Non-seizure outcomes analysis; seizure efficacy data are not extractable from this PubMed abstract."),

    ("lacosamide", "Vossler2020"): item(
        dose="lacosamide up to 12 mg/kg/day or 400 mg/day",
        endpoint="primary generalized tonic-clonic seizures",
        rr50=(68.1, 46.3),
        sf=(31.3, 17.2),
        note="Abstract reports RR50 and Kaplan-Meier seizure freedom at day 166.",
    ),
    ("lacosamide", "Chung2010"): item(
        dose="lacosamide 400 mg/day",
        endpoint="partial-onset seizures",
        rr50=(38.3, 18.3),
        mpc=(37.3, 20.8),
        note="Abstract reports 400 mg/day responder and median seizure-frequency reduction values.",
    ),
    ("lacosamide", "Halasz2009"): item(
        dose="lacosamide 400 mg/day",
        endpoint="partial-onset seizures",
        rr50=(40.5, 25.8),
        mpc=(36.4, 20.5),
        note="Abstract reports 400 mg/day responder and median seizure-frequency reduction values.",
    ),
    ("lacosamide", "Farkas2019"): item(
        dose="lacosamide target weight-based pediatric regimen",
        endpoint="pediatric focal seizures",
        rr50=(52.9, 33.3),
        mpc=(51.7, 21.7),
        note="Abstract reports pediatric target-regimen responder and median seizure-frequency reduction values.",
    ),
    ("lacosamide", "BenMenachem2007"): item(
        dose="lacosamide 400 mg/day",
        endpoint="partial-onset seizures",
        rr50=(41.0, 22.0),
        mpc=(39.0, 10.0),
        note="Abstract reports 400 mg/day responder and median seizure-frequency reduction values; 600 mg/day was not used because efficacy was not greater and tolerability was poorer.",
    ),
    ("lacosamide", "Makedonska2024"): item(
        dose="lacosamide 8-12 mg/kg/day",
        endpoint="focal seizures in patients aged <4 years",
        rr50=(41.4, 37.5),
        mpc_diff=3.2,
        note="Abstract reports 50% responder rates and placebo-adjusted electrographic focal-seizure ADF reduction; efficacy was not statistically superior to placebo.",
    ),
    ("lacosamide", "Hong2016"): reviewed("Abstract reports placebo-adjusted percentage reduction over placebo but not arm-specific responder or median values for the max-dose rollup."),
    ("lacosamide", "FoldvarySchaefer2017"): reviewed("Sleep/cognition study, not a seizure efficacy report."),
    ("lacosamide", "Rudd2015"): reviewed("Cardiac safety analysis, not a seizure efficacy report."),

    ("lamotrigine", "Biton2010"): item(
        dose="lamotrigine XR individualized adjunctive dose",
        endpoint="primary generalized tonic-clonic seizures",
        mpc=(75.4, 32.1),
        note="Abstract reports median percentage reduction for the 19-week treatment phase. RR50 percentage was not reported.",
    ),
    ("lamotrigine", "Biton2005"): item(
        dose="lamotrigine individualized adjunctive dose",
        endpoint="primary generalized tonic-clonic seizures",
        rr50=(72.0, 49.0),
        mpc=(66.5, 34.2),
        note="Abstract reports combined-phase median reduction and maintenance-phase RR50.",
    ),
    ("lamotrigine", "Schapel1993"): item(
        dose="lamotrigine 150-300 mg/day",
        endpoint="partial seizures",
        rr50=(22.0, 0.0),
        note="Abstract reports 22% with >=50% reduction on lamotrigine and none on placebo.",
    ),
    ("lamotrigine", "Naritoku2007"): item(
        dose="lamotrigine XR individualized adjunctive dose",
        endpoint="partial seizures",
        rr50=(44.0, 20.8),
        mpc=(46.6, 24.5),
        note="Abstract reports once-daily XR responder and median partial-seizure reduction values.",
    ),
    ("lamotrigine", "Trevathan2006"): item(
        dose="lamotrigine individualized adjunctive dose",
        endpoint="pediatric/adolescent primary generalized tonic-clonic seizures",
        mpc=(77.0, 40.0),
        sf=(48.0, 17.0),
        note="Abstract reports pediatric/adolescent PGTC median reduction and maintenance seizure-free rates.",
    ),
    ("lamotrigine", "Motte1997"): item(
        dose="lamotrigine individualized adjunctive dose",
        endpoint="LGS major seizures",
        rr50=(33.0, 16.0),
        mpc_diff=44.8,
        note="Abstract reports LGS RR50; MPC is derived from baseline-to-treatment major-seizure frequency changes in the abstract.",
    ),
    ("lamotrigine", "Frank1999"): item(
        dose="lamotrigine monotherapy responder-enriched regimen",
        endpoint="typical absence seizures",
        sf=(62.0, 21.0),
        note="Abstract reports seizure freedom maintained in the double-blind phase.",
    ),
    ("lamotrigine", "Messenheimer1994"): item(
        dose="lamotrigine mostly 400 mg/day",
        endpoint="partial seizures",
        mpc_diff=25.0,
        note="Abstract reports overall median seizure frequency decreased by 25% with lamotrigine compared with placebo.",
    ),

    ("levetiracetam", "Wu2018"): item(
        dose="LEV 1000-3000 mg/day",
        endpoint="generalized tonic-clonic seizures",
        rr50=(77.8, 28.4),
        mpc=(68.8, 12.6),
        sf=(29.6, 3.1),
        note="Flexible-dose regimen allowed escalation to 3000 mg/day; abstract reports active and placebo outcomes.",
    ),
    ("levetiracetam", "Wu2008"): item(
        dose="LEV 1000-3000 mg/day",
        endpoint="partial-onset seizures",
        rr50=(55.9, 26.0),
        mpc=(55.9, 13.7),
        sf=(10.8, 2.0),
        note="Flexible-dose regimen allowed escalation to 3000 mg/day; abstract reports active and placebo outcomes.",
    ),
    ("levetiracetam", "Berkovic2007"): item(
        dose="LEV target 3000 mg/day adults or 60 mg/kg/day children",
        endpoint="generalized tonic-clonic seizures",
        rr50=(72.2, 45.2),
        mpc=(56.5, 28.2),
        sf=(34.2, 10.7),
        note="Abstract reports target-dose GTC outcomes.",
    ),
    ("levetiracetam", "Glauser2006"): item(
        dose="LEV target 60 mg/kg/day",
        endpoint="pediatric partial-onset seizures",
        rr50=(44.6, 19.6),
        mpc_diff=26.8,
        sf=(6.9, 1.0),
        note="Abstract reports target-dose pediatric outcomes; MPC is reported as reduction over placebo.",
    ),
    ("levetiracetam", "Cereghino2000"): item(
        dose="LEV 3000 mg/day",
        endpoint="partial seizures",
        rr50=(39.8, 10.8),
        note="Abstract reports fixed 3000 mg/day responder rate. Seizure freedom was reported only pooled across LEV doses and is not included.",
    ),
    ("levetiracetam", "Xiao2009"): item(
        dose="LEV 3000 mg/day",
        endpoint="partial seizures",
        rr50=(46.4, 39.3),
        note="Abstract reports 3000 mg/day responder rates; the trial did not show expected efficacy.",
    ),
    ("levetiracetam", "PinaGarza2009"): item(
        dose="LEV 40-50 mg/kg/day",
        endpoint="infant/young-child partial-onset seizures",
        rr50=(43.1, 19.6),
        mpc=(43.6, 7.1),
        note="Abstract reports pediatric responder and median seizure-frequency reduction values from video-EEG monitoring.",
    ),
    ("levetiracetam", "Tsai2006"): reviewed("Highest dose was 2000 mg/day, below adult 3000 mg/day maximum; excluded from max-dose rollup."),
    ("levetiracetam", "Shorvon2000"): reviewed("Highest dose was 2000 mg/day, below adult 3000 mg/day maximum; excluded from max-dose rollup."),
    ("levetiracetam", "Boon2002"): reviewed("Highest dose was 2000 mg/day, below adult 3000 mg/day maximum; excluded from max-dose rollup."),
    ("levetiracetam", "Peltola2009"): reviewed("LEV XR 1000 mg/day trial was below adult 3000 mg/day maximum; excluded from max-dose rollup."),
    ("levetiracetam", "Fattore2011"): reviewed("Neonatal seizure study endpoint was short acute electroclinical seizure freedom, not chronic max-dose seizure-frequency efficacy."),
    ("levetiracetam", "Navarro2015"): reviewed("Both arms received clonazepam; levetiracetam add-on acute status endpoint is not a chronic seizure-frequency max-dose endpoint."),
    ("levetiracetam", "PeterDerex2022"): reviewed("Post-stroke prophylaxis endpoint; not included in chronic seizure-frequency max-dose rollup."),

    ("midazolam", "Spencer2020"): item(
        dose="midazolam nasal spray 5 mg",
        endpoint="seizure cluster/EMU 6-hour seizure freedom",
        sf=(54.8, 38.7),
        note="Abstract reports 6-hour post-treatment seizure freedom.",
    ),
    ("midazolam", "Detyniecki2019"): item(
        dose="midazolam nasal spray 5 mg",
        endpoint="seizure cluster treatment success",
        sf=(53.7, 34.4),
        note="Treatment success required seizure termination within 10 minutes and no recurrence 10 minutes to 6 hours after dosing.",
    ),

    ("oxcarbazepine", "French2013"): item(
        dose="extended-release oxcarbazepine 2400 mg/day",
        endpoint="partial-onset seizures",
        rr50=(40.7, 28.1),
        mpc=(42.9, 28.7),
        sf=(11.4, 3.3),
        note="Abstract reports 2400 mg/day responder, median reduction, and 16-week seizure-free rates.",
    ),
    ("oxcarbazepine", "Barcs2000"): item(
        dose="oxcarbazepine 2400 mg/day",
        endpoint="partial seizures",
        rr50=(50.0, 13.0),
        mpc=(50.0, 8.0),
        note="Abstract reports 2400 mg/day responder and median reduction values.",
    ),

    ("perampanel", "French2015"): item(
        dose="perampanel up to 8 mg/day",
        endpoint="primary generalized tonic-clonic seizures",
        rr50=(64.2, 39.5),
        mpc=(76.5, 38.4),
        sf=(30.9, 12.3),
        note="Abstract reports PGTC responder and seizure-freedom rates; median PGTC reduction values are taken from the reported active/placebo percent changes.",
    ),
    ("perampanel", "French2012b"): item(
        dose="perampanel 12 mg/day",
        endpoint="partial-onset seizures",
        rr50=(33.9, 14.7),
        mpc=(17.6, 9.7),
        note="Abstract reports 12 mg/day responder and median seizure-frequency reduction values.",
    ),
    ("perampanel", "French2012"): item(
        dose="perampanel 12 mg/day",
        endpoint="partial-onset seizures",
        rr50=(36.1, 26.4),
        mpc=(34.5, 21.0),
        note="Abstract reports 12 mg/day responder and median seizure-frequency reduction values.",
    ),
    ("perampanel", "Krauss2012"): reviewed("Highest focal-seizure dose in this study was 8 mg/day; excluded from the 12 mg/day focal-seizure max-dose rollup."),

    ("pregabalin", "French2003"): item(
        dose="pregabalin 600 mg/day BID",
        endpoint="partial seizures",
        rr50=(51.0, 14.0),
        mpc=(54.0, 7.0),
        note="Abstract reports 600 mg/day responder and seizure-frequency reduction values.",
    ),
    ("pregabalin", "Arroyo2004"): item(
        dose="pregabalin 600 mg/day TID",
        endpoint="partial seizures",
        rr50=(43.5, 6.2),
        mpc=(47.8, -1.8),
        note="Abstract reports 600 mg/day responder and seizure-frequency reduction values.",
    ),
    ("pregabalin", "Antinew2019"): item(
        dose="pregabalin 10 mg/kg/day or 14 mg/kg/day if <30 kg",
        endpoint="pediatric focal-onset seizures",
        rr50=(40.6, 22.6),
        mpc_diff=19.9,
        note="Abstract reports high pediatric dose responder rate and improvement over placebo.",
    ),
    ("pregabalin", "Beydoun2005"): item(
        dose="pregabalin 600 mg/day TID",
        endpoint="partial seizures",
        rr50=(49.0, 9.0),
        mpc=(53.0, -1.0),
        note="Abstract reports 600 mg/day TID responder and seizure-frequency reduction values; BID was similar but slightly lower.",
    ),
    ("pregabalin", "Baulac2010"): item(
        dose="pregabalin up to 600 mg/day",
        endpoint="partial seizures",
        rr50=(36.0, 21.0),
        mpc_diff=20.0,
        note="Abstract reports responder rates and a placebo-comparator median percentage reduction across treatment.",
    ),

    ("progabide", "MartinezLage1984"): reviewed("Crossover abstract reports seizure reductions for individual progabide-treated patients but not extractable active/placebo RR50, MPC, or seizure-freedom arm values."),
    ("progabide", "Loiseau1983"): reviewed("Crossover abstract reports global improvement and 48-100% total-seizure reductions in some progabide periods, but not extractable active/placebo RR50, MPC, or seizure-freedom arm values."),
    ("progabide", "Dam1983"): reviewed("Crossover abstract reports no significant partial-seizure difference and does not give extractable active/placebo RR50, MPC, or seizure-freedom arm values."),

    ("rufinamide", "Biton2010"): item(
        dose="rufinamide 3200 mg/day",
        endpoint="partial-onset seizures",
        rr50=(32.5, 14.3),
        mpc=(23.25, 9.80),
        note="Abstract reports 3200 mg/day responder and median percentage reduction values.",
    ),
    ("rufinamide", "Brodie2009"): item(
        dose="rufinamide 3200 mg/day",
        endpoint="partial seizures",
        rr50=(28.2, 18.6),
        mpc=(20.4, -1.6),
        note="Abstract reports 3200 mg/day responder and median partial-seizure reduction values.",
    ),
    ("rufinamide", "Ohtsuka2014"): item(
        dose="rufinamide adjunctive LGS target/max regimen",
        endpoint="LGS tonic-atonic and total seizures",
        mpc=(24.2, 3.3),
        note="Abstract reports tonic-atonic seizure median percent change; total-seizure differential was 29.8% and is noted but not used for the primary rollup.",
    ),
    ("rufinamide", "Glauser2008"): item(
        dose="rufinamide adjunctive LGS target/max regimen",
        endpoint="LGS total and tonic-atonic seizures",
        mpc=(32.7, 11.7),
        note="Abstract reports total seizure median percentage reduction; tonic-atonic differential was 43.9% and is noted but not used for the primary rollup.",
    ),
    ("rufinamide", "Elger2010"): reviewed("Dose-ranging study showed a dose-response trend, but the PubMed abstract does not give arm-specific responder or median percentage reduction values."),
    ("rufinamide", "Palhagen2001"): item(
        dose="rufinamide up to 1600 mg/day",
        endpoint="partial or primary generalized tonic-clonic seizures",
        rr50=(39.0, 16.0),
        mpc=(41.0, -52.0),
        note="Abstract reports responder rates and seizure-frequency percentage changes for the proof-of-principle trial.",
    ),

    ("sultiame", "Rating2000"): item(
        dose="sultiame 5 mg/kg/day",
        endpoint="BECTS seizure prevention",
        sf=(87.1, 40.0),
        note="Derived directly from abstract seizure TFE counts: 4/31 sultiame and 21/35 placebo had seizures, so seizure-free rates were 87.1% and 40.0%.",
    ),
    ("sultiame", "Debus2004"): item(
        dose="sultiame 5-10 mg/kg/day add-on to baseline pyridoxine",
        endpoint="West syndrome response",
        sf=(30.0, 0.0),
        note="Abstract reports complete cessation of infantile spasms and hypsarrhythmia resolution in 6/20 sultiame patients and 0/17 placebo patients.",
    ),

    ("stiripentol", "Guerrini2024"): item(
        dose="stiripentol add-on to clobazam/valproate",
        endpoint="Dravet generalized tonic-clonic seizures",
        rr50=(72.0, 7.0),
        sf=(38.0, 0.0),
        note="Post hoc STICLO analysis reports >=50% GTCS decrease and GTCS freedom in the double-blind period.",
    ),
    ("stiripentol", "Chiron2000"): item(
        dose="stiripentol add-on to valproate and clobazam",
        endpoint="Dravet clonic or tonic-clonic seizures",
        rr50=(71.0, 5.0),
        mpc=(69.0, -7.0),
        sf=(42.9, 0.0),
        note="Abstract reports responders, percent change from baseline, and seizure-free patients in the STICLO Dravet trial.",
    ),
    ("stiripentol", "Chiron2006"): item(
        dose="stiripentol pediatric partial-epilepsy add-on regimen",
        endpoint="childhood partial seizures",
        mpc=(75.0, 22.0),
        include_mpc=False,
        note="Partial-epilepsy enrichment/withdrawal trial is audited, but not included in the Dravet max-dose rollup.",
    ),
    ("stiripentol", "Nabbout2020"): reviewed("Fenfluramine was the randomized active treatment; stiripentol was background therapy."),

    ("tiagabine", "Uthman1998"): item(
        dose="tiagabine 56 mg/day",
        endpoint="complex partial seizures",
        rr50=(29.0, 4.0),
        note="Abstract reports 56 mg/day responder rate. Median change was reported as absolute 4-week seizure-frequency change, not percent.",
    ),
    ("tiagabine", "Sachdeo1997"): item(
        dose="tiagabine 32 mg/day BID",
        endpoint="complex partial seizures",
        rr50=(31.0, 10.0),
        note="Abstract reports responder rates for the BID maximum-effective regimen; seizure-frequency change was reported as an absolute 4-week rate, not percent.",
    ),
    ("tiagabine", "Crawford2001"): item(
        dose="tiagabine response-dependent dose up to 64 mg/day",
        endpoint="partial seizures",
        rr50_diff=33.0,
        note="Enrichment/withdrawal trial reports 33% of tiagabine-treated double-blind patients had >=50% all-partial-seizure reduction; placebo rate was not extractable from the abstract.",
    ),

    ("topiramate", "Biton1999"): item(
        dose="topiramate approximately 6 mg/kg/day",
        endpoint="primary generalized tonic-clonic seizures",
        rr50=(56.0, 20.0),
        mpc=(56.7, 9.0),
        note="Abstract reports target-dose PGTC responder and median reduction values.",
    ),
    ("topiramate", "Sharief1996"): item(
        dose="topiramate 400 mg/day",
        endpoint="partial seizures",
        rr50=(35.0, 8.0),
        mpc=(41.0, 1.0),
        note="Abstract reports 400 mg/day responder and median reduction values.",
    ),
    ("topiramate", "Faught1996"): item(
        dose="topiramate 400 mg/day",
        endpoint="partial-onset seizures",
        rr50=(47.0, 18.0),
        mpc=(48.0, 13.0),
        note="Abstract reports 400 mg/day responder and median reduction values. Higher 600 mg/day arm was not used because incremental efficacy above 400 mg/day is not the selected maximum effective dose.",
    ),
    ("topiramate", "PMID1999"): item(
        dose="topiramate 600 mg/day",
        endpoint="partial epilepsy",
        rr50=(50.6, 12.9),
        mpc=(51.3, 9.1),
        sf=(7.9, 1.2),
        note="Abstract reports target 600 mg/day responder, median seizure-frequency reduction, and seizure-free rates.",
    ),
    ("topiramate", "Guberman2002"): item(
        dose="topiramate 200 mg/day",
        endpoint="partial-onset seizures",
        mpc=(44.0, 20.0),
        note="Abstract reports 200 mg/day median seizure-frequency reduction values; responder rate was not extractable.",
    ),
    ("topiramate", "Zhang2011"): item(
        dose="topiramate 200 mg/day",
        endpoint="elderly refractory partial epilepsy",
        rr50=(47.8, 7.5),
        note="Abstract reports responder rates for the 200 mg/day elderly trial.",
    ),

    ("vigabatrin", "Bruni2000"): item(
        dose="vigabatrin adult add-on regimen",
        endpoint="complex partial/secondarily generalized seizures",
        rr50=(48.0, 26.0),
        note="Abstract reports RR50 for active and placebo groups; exact dose is not stated in the abstract.",
    ),
    ("vigabatrin", "Grunewald1994"): item(
        dose="vigabatrin 3 g/day",
        endpoint="complex partial seizures",
        rr50=(50.0, 17.39),
        mpc=(69.0, -25.0),
        note="Abstract reports 10/20 vs 4/23 with >50% complex partial seizure reduction and median complex partial seizure changes in the last 8 weeks.",
    ),
    ("vigabatrin", "Appleton1999"): item(
        dose="vigabatrin infantile-spasm regimen",
        endpoint="infantile spasms",
        mpc=(78.0, 26.0),
        sf=(35.0, 10.0),
        note="Abstract reports spasm reduction and spasm-free rates on the final double-blind day.",
    ),
    ("vigabatrin", "Dean1999"): item(
        dose="vigabatrin 3 g/day",
        endpoint="complex partial seizures",
        rr50=(51.0, 7.0),
        note="Abstract reports therapeutic success rates for 3 g/day and placebo; 6 g/day was not used because it exceeds the current adult approved maximum and had more dropouts.",
    ),

    ("zonisamide", "Guerrini2013"): item(
        dose="zonisamide target 8 mg/kg/day",
        endpoint="pediatric partial epilepsy",
        rr50=(50.0, 31.0),
        note="Abstract reports target-dose pediatric responder rates.",
    ),
    ("zonisamide", "Lu2011"): item(
        dose="zonisamide 400 mg/day",
        endpoint="partial-onset epilepsy",
        rr50=(56.5, 36.0),
        note="Abstract reports 400 mg/day responder rate and placebo responder rate.",
    ),
    ("zonisamide", "Faught2001"): item(
        dose="zonisamide 400 mg/day",
        endpoint="partial-onset seizures",
        mpc=(40.5, 9.0),
        note="Abstract reports 400 mg/day median all-seizure reduction versus placebo.",
    ),
    ("zonisamide", "Brodie2005"): reviewed("Highest trial dose was 500 mg/day, above the current 400 mg/day approved maximum; excluded from max-approved-dose rollup."),
    ("zonisamide", "Sackellares2004"): reviewed("Titrated 400-600 mg/day mixed regimen; not included because max-dose arm-specific values were not separable."),
    ("zonisamide", "Schmidt1993"): reviewed("Dose was not extractable from the PubMed abstract for a current max-dose rollup."),
}


def read_csv(path):
    with path.open(newline="", encoding="utf-8-sig") as handle:
        return list(csv.DictReader(handle))


def write_csv(path, rows, fieldnames):
    with path.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, lineterminator="\r\n")
        writer.writeheader()
        writer.writerows(rows)


def format_number(value):
    value = round(float(value), 2)
    if value.is_integer():
        return str(int(value))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def summarize(generic, rows, diff_field, include_field, noun):
    included = [row for row in rows if row[include_field] == "yes" and row[diff_field] != ""]
    if included:
        values = [float(row[diff_field]) for row in included]
        low = min(values)
        high = max(values)
        value_text = f"{format_number(low)} %" if low == high else f"{format_number(low)}-{format_number(high)} %"
        details = "; ".join(
            f"{row['label']} {row['dose_or_regimen']} {format_number(row[diff_field])}%"
            for row in included
        )
        return f"{value_text} (drug minus placebo {noun} at maximum effective dose/regimen: {details})"
    return ""


def nonextractable_text(has_rcts, noun):
    if not has_rcts:
        return "No PubMed phase II/III RCTs found"
    return f"NR/not extractable as a drug-minus-placebo {noun} at the maximum effective dose/regimen from included phase II/III placebo-controlled RCT records"


def report_row(rct_row):
    extracted = EXTRACTIONS.get((rct_row["generic_name"], rct_row["label"]))
    if extracted is None:
        extracted = reviewed("Reviewed PubMed title/abstract; no extractable maximum-effective-dose RR50, MPC, or seizure-freedom differential.")
    row = {
        "generic_name": rct_row["generic_name"],
        "label": rct_row["label"],
        "pmid": rct_row["pmid"],
        "title": rct_row["title"],
        "pubmed_url": rct_row["url"],
    }
    for key, value in extracted.items():
        row[key] = "" if value is None else value
    return row


def main():
    REPORT_DIR.mkdir(parents=True, exist_ok=True)
    asm_rows = read_csv(ASM_CSV)
    rct_rows = [row for row in read_csv(RCT_REPORT) if row["status"] == "included"]
    outcome_rows = [report_row(row) for row in rct_rows]

    outcome_fields = [
        "generic_name",
        "label",
        "pmid",
        "title",
        "dose_or_regimen",
        "endpoint",
        "rr50_active_percent",
        "rr50_placebo_percent",
        "rr50_differential_percent",
        "rr50_included_in_csv_summary",
        "mpc_active_percent",
        "mpc_placebo_percent",
        "mpc_differential_percent",
        "mpc_included_in_csv_summary",
        "sf_active_percent",
        "sf_placebo_percent",
        "sf_differential_percent",
        "sf_included_in_csv_summary",
        "audit_note",
        "pubmed_url",
    ]
    write_csv(OUTCOME_REPORT, outcome_rows, outcome_fields)

    seizure_rows = []
    for row in outcome_rows:
        seizure_rows.append(
            {
                "generic_name": row["generic_name"],
                "label": row["label"],
                "pmid": row["pmid"],
                "title": row["title"],
                "active_rate_percent": row["sf_active_percent"],
                "placebo_rate_percent": row["sf_placebo_percent"],
                "differential_percent": row["sf_differential_percent"],
                "dose_or_regimen": row["dose_or_regimen"],
                "endpoint": row["endpoint"],
                "included_in_csv_summary": row["sf_included_in_csv_summary"],
                "extraction_status": "differential_extracted" if row["sf_included_in_csv_summary"] == "yes" else "reviewed_no_extractable_differential",
                "audit_note": row["audit_note"],
                "pubmed_url": row["pubmed_url"],
            }
        )
    write_csv(
        SEIZURE_FREEDOM_REPORT,
        seizure_rows,
        [
            "generic_name",
            "label",
            "pmid",
            "title",
            "active_rate_percent",
            "placebo_rate_percent",
            "differential_percent",
            "dose_or_regimen",
            "endpoint",
            "included_in_csv_summary",
            "extraction_status",
            "audit_note",
            "pubmed_url",
        ],
    )

    by_drug = defaultdict(list)
    rct_count = defaultdict(int)
    for row in outcome_rows:
        by_drug[row["generic_name"]].append(row)
        rct_count[row["generic_name"]] += 1

    for row in asm_rows:
        generic = row["generic_name"]
        has_rcts = rct_count[generic] > 0
        rr50 = summarize(generic, by_drug[generic], "rr50_differential_percent", "rr50_included_in_csv_summary", "RR50 differential")
        mpc = summarize(generic, by_drug[generic], "mpc_differential_percent", "mpc_included_in_csv_summary", "MPC differential")
        sf = summarize(generic, by_drug[generic], "sf_differential_percent", "sf_included_in_csv_summary", "seizure-freedom differential")
        row[RR50_FIELD] = rr50 or nonextractable_text(has_rcts, "RR50 differential")
        row[MPC_FIELD] = mpc or nonextractable_text(has_rcts, "MPC differential")
        row[SF_FIELD] = sf or nonextractable_text(has_rcts, "seizure-freedom patient-rate differential")
        row["data_most_recently_refreshed"] = REFRESH_DATE

    write_csv(ASM_CSV, asm_rows, list(asm_rows[0].keys()))

    gap_rows = []
    for row in asm_rows:
        missing = []
        for field in [RR50_FIELD, MPC_FIELD, SF_FIELD]:
            if "%" not in row[field]:
                missing.append(field)
        if missing:
            gap_rows.append(
                {
                    "generic_name": row["generic_name"],
                    "missing_fields": "; ".join(missing),
                    "rct_count": rct_count[row["generic_name"]],
                    "review_status": "no qualifying PubMed RCTs" if not rct_count[row["generic_name"]] else "reviewed RCTs; max-dose value not extractable",
                    "rct_links": row.get("pubmed_phase_ii_iii_rct_links", ""),
                }
            )
    write_csv(GAP_REPORT, gap_rows, ["generic_name", "missing_fields", "rct_count", "review_status", "rct_links"])

    print(f"Reviewed {len(outcome_rows)} included RCT rows.")
    print(f"RR50 extracted for {sum(1 for row in outcome_rows if row['rr50_included_in_csv_summary'] == 'yes')} row(s).")
    print(f"MPC extracted for {sum(1 for row in outcome_rows if row['mpc_included_in_csv_summary'] == 'yes')} row(s).")
    print(f"Seizure freedom extracted for {sum(1 for row in outcome_rows if row['sf_included_in_csv_summary'] == 'yes')} row(s).")
    print(f"Wrote {OUTCOME_REPORT.relative_to(ROOT)}, {SEIZURE_FREEDOM_REPORT.relative_to(ROOT)}, and {GAP_REPORT.relative_to(ROOT)}.")


if __name__ == "__main__":
    main()
