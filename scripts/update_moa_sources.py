#!/usr/bin/env python3
import csv
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
CSV_PATH = ROOT / "ASM-list.csv"
AUDIT_PATH = ROOT / "pubmed_cache" / "reports" / "mechanism_audit.csv"
REFRESH_DATE = "05-15-2026"

FDA = "FDA/DailyMed labeling"
AES = "American Epilepsy Society 2024 U.S. ASM summary"
SILLS = "Sills and Rogawski 2020 ASM mechanism review"
NCBI_TABLE = "NCBI Bookshelf AED mechanism table"
UK_EMC = "UK eMC SmPC labeling"
PUBCHEM = "NCBI PubChem pharmacology records"
EMA_TROBALT = "EMA Trobalt withdrawal page"
PMC_VALNOCTAMIDE = "PMC valnoctamide GABA-A mechanism study"
SULTIAME_SODIUM = "Sulthiame sodium-current mechanism study"


MOA = {
    "acetazolamide": {
        "mechanism_of_action": "Carbonic anhydrase inhibitor; antiseizure effect is attributed to carbonic-anhydrase inhibition with brain/tissue acidosis and reduced neuronal excitability, but the clinical antiseizure mechanism is not fully established.",
        "mechanism_source": SILLS,
        "mechanism_source_tier": "Peer-reviewed review",
        "mechanism_confidence": "Moderate",
    },
    "adrenocorticotropic hormone": {
        "mechanism_of_action": "Mechanism for infantile spasms is unknown; ACTH stimulates adrenal cortisol, corticosterone, aldosterone, and weak androgen secretion and is reported to bind melanocortin receptors.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "barbexaclone": {
        "mechanism_of_action": "Phenobarbital/propylhexedrine salt; antiseizure effect is attributed to the phenobarbital moiety, which potentiates GABA-A receptor-mediated inhibition.",
        "mechanism_source": f"{PUBCHEM}; {SILLS}",
        "mechanism_source_tier": "NCBI/PubChem",
        "mechanism_confidence": "Moderate",
    },
    "beclamide": {
        "mechanism_of_action": "Older anticonvulsant with no well-established antiseizure mechanism; limited data suggest CNS monoamine effects rather than a defined modern ASM target.",
        "mechanism_source": PUBCHEM,
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "brivaracetam": {
        "mechanism_of_action": "Precise anticonvulsant mechanism is unknown; brivaracetam binds selectively and with high affinity to synaptic vesicle protein 2A (SV2A), which may contribute to the anticonvulsant effect.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "cannabidiol": {
        "mechanism_of_action": "Precise human anticonvulsant mechanisms are unknown; effects do not appear to be mediated by CB1/CB2 cannabinoid receptors, with GPR55, TRPV1, and adenosine-mediated signaling proposed.",
        "mechanism_source": f"{FDA}; {AES}",
        "mechanism_source_tier": "FDA/AES summary",
        "mechanism_confidence": "Limited",
    },
    "carbamazepine": {
        "mechanism_of_action": "Antiseizure mechanism is not fully established in labeling; accepted primary proposed effect is use-dependent voltage-gated sodium-channel blockade, reducing repetitive firing and seizure spread.",
        "mechanism_source": f"{FDA}; {SILLS}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "cenobamate": {
        "mechanism_of_action": "Precise therapeutic mechanism is unknown; cenobamate reduces repetitive neuronal firing by inhibiting voltage-gated sodium currents and positively modulates GABA-A ion channels.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "clobazam": {
        "mechanism_of_action": "Exact mechanism is not fully understood; 1,5-benzodiazepine positive allosteric modulation of GABA-A receptors potentiates GABAergic neurotransmission.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "High",
    },
    "clonazepam": {
        "mechanism_of_action": "Benzodiazepine positive allosteric modulator of GABA-A receptors; enhances GABAergic inhibition by binding at the benzodiazepine site.",
        "mechanism_source": f"{AES}; {SILLS}",
        "mechanism_source_tier": "AES/FDA summary",
        "mechanism_confidence": "High",
    },
    "clorazepate": {
        "mechanism_of_action": "Benzodiazepine prodrug to nordiazepam; positive allosteric modulation of GABA-A receptors enhances GABAergic inhibition.",
        "mechanism_source": f"{SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Peer-reviewed review",
        "mechanism_confidence": "High",
    },
    "diazepam": {
        "mechanism_of_action": "Precise antiseizure mechanism is unknown; diazepam enhances GABA-A receptor-mediated chloride-channel inhibition by increasing GABA effects at the receptor.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "High",
    },
    "divalproex sodium": {
        "mechanism_of_action": "Dissociates to valproate; mechanisms are not established, but labeling suggests antiseizure activity may relate to increased brain GABA concentrations. Additional ion-channel effects are proposed but not definitive.",
        "mechanism_source": f"{FDA}; {SILLS}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "eslicarbazepine acetate": {
        "mechanism_of_action": "Converted to eslicarbazepine; precise mechanism is unknown but is thought to involve inhibition of voltage-gated sodium channels.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "ethadione": {
        "mechanism_of_action": "Oxazolidinedione-class antiseizure drug; exact drug-specific mechanism is not established, with the class proposed to reduce low-threshold T-type calcium currents in thalamic neurons.",
        "mechanism_source": f"{NCBI_TABLE}; {SILLS}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "ethosuximide": {
        "mechanism_of_action": "Reduces low-threshold T-type calcium currents in thalamic neurons, the established anti-absence succinimide mechanism.",
        "mechanism_source": f"{AES}; {NCBI_TABLE}; {SILLS}",
        "mechanism_source_tier": "AES/FDA summary",
        "mechanism_confidence": "High",
    },
    "ethotoin": {
        "mechanism_of_action": "Hydantoin-class antiseizure drug; exact ethotoin-specific mechanism is not well defined, but the class is proposed to reduce high-frequency firing via voltage-gated sodium-channel effects.",
        "mechanism_source": f"{NCBI_TABLE}; {SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "etiracetam": {
        "mechanism_of_action": "Racetam development compound related to levetiracetam; exact antiseizure mechanism is not established, though levetiracetam-related analogs act through SV2A-associated mechanisms.",
        "mechanism_source": PUBCHEM,
        "mechanism_source_tier": "NCBI/PubChem",
        "mechanism_confidence": "Limited",
    },
    "everolimus": {
        "mechanism_of_action": "Binds FKBP-12 to inhibit mTOR complex 1 (mTORC1), targeting dysregulated mTOR signaling in tuberous sclerosis complex.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "High",
    },
    "ezogabine": {
        "mechanism_of_action": "Neuronal potassium-channel opener; primarily activates Kv7/KCNQ channels, stabilizing resting membrane potential and reducing neuronal excitability.",
        "mechanism_source": f"{EMA_TROBALT}; {SILLS}",
        "mechanism_source_tier": "EMA/UK SmPC",
        "mechanism_confidence": "High",
    },
    "felbamate": {
        "mechanism_of_action": "Anticonvulsant mechanism is unknown in labeling; proposed mechanisms include reduced seizure spread with NMDA receptor inhibition and GABA-A receptor modulation.",
        "mechanism_source": f"{FDA}; {SILLS}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "fenfluramine": {
        "mechanism_of_action": "Precise seizure mechanism is unknown; fenfluramine and norfenfluramine exhibit serotonin 5-HT2 receptor agonist activity, with sigma-1 modulation also proposed.",
        "mechanism_source": f"{FDA}; {AES}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "fosphenytoin": {
        "mechanism_of_action": "Phenytoin prodrug; anticonvulsant effects are attributable to phenytoin, whose mechanism is not established but is thought to involve voltage-dependent sodium-channel blockade.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "gabapentin": {
        "mechanism_of_action": "Precise antiepileptic mechanism is unknown; gabapentin binds the alpha-2-delta subunit of voltage-activated calcium channels, but the relationship of this binding to efficacy is not fully established.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "ganaxolone": {
        "mechanism_of_action": "Precise therapeutic mechanism is unknown; anticonvulsant effects are thought to result from positive allosteric modulation of CNS GABA-A receptors.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "lacosamide": {
        "mechanism_of_action": "Human antiseizure mechanism remains incompletely elucidated; lacosamide selectively enhances slow inactivation of voltage-gated sodium channels and stabilizes hyperexcitable neuronal membranes.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "lamotrigine": {
        "mechanism_of_action": "Precise anticonvulsant mechanism is unknown; a proposed mechanism is inhibition of voltage-sensitive sodium channels with reduced glutamate and aspartate release.",
        "mechanism_source": f"{FDA}; {SILLS}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "levetiracetam": {
        "mechanism_of_action": "Precise antiepileptic mechanism is unknown; levetiracetam binds synaptic vesicle protein 2A (SV2A), and this interaction may contribute to antiseizure activity.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "lorazepam": {
        "mechanism_of_action": "Benzodiazepine positive allosteric modulator of GABA-A receptors; enhances GABAergic inhibition and is used acutely for seizure termination.",
        "mechanism_source": f"{AES}; {SILLS}",
        "mechanism_source_tier": "AES/FDA summary",
        "mechanism_confidence": "High",
    },
    "mephenytoin": {
        "mechanism_of_action": "Hydantoin-class antiseizure drug; exact drug-specific mechanism is limited, but hydantoins are proposed to reduce high-frequency neuronal firing through voltage-gated sodium-channel effects.",
        "mechanism_source": f"{NCBI_TABLE}; {SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "mephobarbital": {
        "mechanism_of_action": "Barbiturate related to phenobarbital and partly metabolized to phenobarbital; antiseizure effect is attributed to GABA-A receptor-mediated inhibitory potentiation.",
        "mechanism_source": f"{SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Moderate",
    },
    "methazolamide": {
        "mechanism_of_action": "Potent carbonic anhydrase inhibitor; DailyMed labeling states that although methazolamide reaches high cerebrospinal-fluid concentrations, it is not considered an effective anticonvulsant.",
        "mechanism_source": f"{FDA}; {PUBCHEM}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Limited",
    },
    "methsuximide": {
        "mechanism_of_action": "Succinimide-class antiseizure drug; exact mechanism is not fully established, but succinimides are associated with reduced low-threshold T-type calcium currents; active metabolite contributes.",
        "mechanism_source": f"{NCBI_TABLE}; {SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Moderate",
    },
    "midazolam": {
        "mechanism_of_action": "Benzodiazepine positive allosteric modulator of GABA-A receptors; enhances GABAergic inhibition by binding at the benzodiazepine site.",
        "mechanism_source": f"{AES}; {FDA}",
        "mechanism_source_tier": "AES/FDA summary",
        "mechanism_confidence": "High",
    },
    "mirogabalin": {
        "mechanism_of_action": "Gabapentinoid that binds alpha-2-delta subunits of voltage-gated calcium channels; it is not established or approved as an antiseizure medication.",
        "mechanism_source": f"{PUBCHEM}; {SILLS}",
        "mechanism_source_tier": "NCBI/PubChem",
        "mechanism_confidence": "Moderate",
    },
    "nitrazepam": {
        "mechanism_of_action": "Benzodiazepine positive allosteric modulator of GABA-A receptors; enhances GABAergic inhibition.",
        "mechanism_source": f"{SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Peer-reviewed review",
        "mechanism_confidence": "High",
    },
    "oxcarbazepine": {
        "mechanism_of_action": "Precise mechanism is unknown; active MHD metabolite blocks voltage-sensitive sodium channels, stabilizes hyperexcited neural membranes, and may also increase potassium conductance and modulate high-voltage calcium channels.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "paraldehyde": {
        "mechanism_of_action": "Historical CNS depressant used for convulsions/status epilepticus; exact anticonvulsant mechanism is not well established and is best treated as limited/unknown rather than a defined modern ASM target.",
        "mechanism_source": PUBCHEM,
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "paramethadione": {
        "mechanism_of_action": "Oxazolidinedione-class antiseizure drug; exact mechanism is not established, with the class proposed to reduce low-threshold T-type calcium currents in thalamic neurons.",
        "mechanism_source": f"{NCBI_TABLE}; {SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "perampanel": {
        "mechanism_of_action": "Noncompetitive antagonist of ionotropic AMPA glutamate receptors on postsynaptic neurons; precise human antiepileptic mechanism is still described as unknown in labeling.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "High",
    },
    "phenacemide": {
        "mechanism_of_action": "Ureide anticonvulsant; mechanism in humans has not been established. Older records describe raised seizure threshold and reduced spread of seizure discharge, with sodium/calcium-channel blockade proposed.",
        "mechanism_source": PUBCHEM,
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "pheneturide": {
        "mechanism_of_action": "Older ureide anticonvulsant structurally related to phenacemide; exact antiseizure mechanism is not established.",
        "mechanism_source": PUBCHEM,
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "phenobarbital": {
        "mechanism_of_action": "Mechanism is not fully understood; barbiturate potentiation of synaptic inhibition through GABA-A receptors is the principal accepted antiseizure mechanism.",
        "mechanism_source": f"{FDA}; {AES}; {SILLS}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "High",
    },
    "phensuximide": {
        "mechanism_of_action": "Succinimide-class antiseizure drug; exact mechanism is not fully established, but the class is associated with reduced low-threshold T-type calcium currents.",
        "mechanism_source": f"{NCBI_TABLE}; {SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Moderate",
    },
    "phenytoin": {
        "mechanism_of_action": "Precise mechanism is not established in labeling; thought to involve voltage-dependent blockade of membrane sodium channels, reducing sustained high-frequency neuronal discharges.",
        "mechanism_source": f"{FDA}; {SILLS}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "piracetam": {
        "mechanism_of_action": "Mode of action in cortical myoclonus is unknown; do not classify as a direct GABAergic ASM despite being a cyclic GABA derivative.",
        "mechanism_source": UK_EMC,
        "mechanism_source_tier": "EMA/UK SmPC",
        "mechanism_confidence": "Limited",
    },
    "potassium bromide": {
        "mechanism_of_action": "Bromide-ion antiseizure mechanism is not defined by modern labeling; proposed effect is increased inhibitory hyperpolarizing tone through bromide/chloride conductance, with evidence largely historical/veterinary.",
        "mechanism_source": f"{PUBCHEM}; {NCBI_TABLE}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "pregabalin": {
        "mechanism_of_action": "Mechanism is not fully elucidated; pregabalin binds alpha-2-delta subunits of voltage-gated calcium channels, which may be involved in anti-seizure effects.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "primidone": {
        "mechanism_of_action": "Mechanism is not fully established; antiseizure activity reflects parent primidone plus phenobarbital/PEMA metabolites, with barbiturate-related GABA-A potentiation contributing.",
        "mechanism_source": f"{AES}; {SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "AES/FDA summary",
        "mechanism_confidence": "Moderate",
    },
    "progabide": {
        "mechanism_of_action": "GABA analog/prodrug with agonist activity at GABA-A and GABA-B receptors, enhancing inhibitory GABAergic signaling.",
        "mechanism_source": PUBCHEM,
        "mechanism_source_tier": "NCBI/PubChem",
        "mechanism_confidence": "High",
    },
    "pyridoxine": {
        "mechanism_of_action": "Vitamin B6 precursor/cofactor support; in pyridoxine-dependent epilepsies, treatment restores pyridoxal-phosphate-dependent neurotransmitter metabolism, including GABA synthesis.",
        "mechanism_source": PUBCHEM,
        "mechanism_source_tier": "NCBI/PubChem",
        "mechanism_confidence": "High",
    },
    "rufinamide": {
        "mechanism_of_action": "Precise mechanism is unknown; in vitro studies suggest sodium-channel modulation, especially prolongation of the inactive state and limitation of repetitive sodium-dependent firing.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "seletracetam": {
        "mechanism_of_action": "Investigational levetiracetam-related racetam; proposed mechanism is SV2A modulation with possible reduction of calcium-dependent neurotransmitter release, but it is not an approved ASM.",
        "mechanism_source": PUBCHEM,
        "mechanism_source_tier": "NCBI/PubChem",
        "mechanism_confidence": "Moderate",
    },
    "sodium valproate": {
        "mechanism_of_action": "Valproate ion; mechanisms are not established, but labeling suggests antiseizure activity may relate to increased brain GABA concentrations. Additional ion-channel effects are proposed but not definitive.",
        "mechanism_source": f"{FDA}; {SILLS}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "stiripentol": {
        "mechanism_of_action": "Human anticonvulsant mechanism is unknown; possible mechanisms include direct GABA-A receptor effects and indirect CYP inhibition that increases clobazam and norclobazam exposure.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "sultiame": {
        "mechanism_of_action": "Carbonic anhydrase inhibitor with documented anticonvulsant effect; sodium-current reduction has also been reported, but the relative clinical contribution is not fully defined.",
        "mechanism_source": f"{UK_EMC}; {SULTIAME_SODIUM}",
        "mechanism_source_tier": "EMA/UK SmPC",
        "mechanism_confidence": "Moderate",
    },
    "temazepam": {
        "mechanism_of_action": "Benzodiazepine positive allosteric modulator of GABA-A receptors; not a standard contemporary epilepsy ASM.",
        "mechanism_source": f"{SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Peer-reviewed review",
        "mechanism_confidence": "Moderate",
    },
    "tiagabine": {
        "mechanism_of_action": "Precise antiseizure mechanism is unknown, but tiagabine blocks GABA uptake by the GAT-1 GABA transporter, increasing synaptic GABA availability.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "High",
    },
    "topiramate": {
        "mechanism_of_action": "Precise anticonvulsant mechanism is unknown; preclinical effects include voltage-dependent sodium-channel blockade, GABA-A augmentation, AMPA/kainate antagonism, and carbonic-anhydrase inhibition.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "trimethadione": {
        "mechanism_of_action": "Oxazolidinedione anti-absence drug; proposed mechanism is reduction of low-threshold T-type calcium currents in thalamic neurons.",
        "mechanism_source": f"{NCBI_TABLE}; {SILLS}; {PUBCHEM}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Moderate",
    },
    "valnoctamide": {
        "mechanism_of_action": "Valproate-related amide; precise antiseizure mechanism is not established. Preclinical work suggests enhancement of GABA-A-mediated phasic inhibition, but clinical MOA evidence is limited.",
        "mechanism_source": f"{PMC_VALNOCTAMIDE}; {PUBCHEM}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "valproic acid": {
        "mechanism_of_action": "Dissociates to valproate; mechanisms are not established, but labeling suggests antiseizure activity may relate to increased brain GABA concentrations. Additional ion-channel effects are proposed but not definitive.",
        "mechanism_source": f"{FDA}; {SILLS}",
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
    "valpromide": {
        "mechanism_of_action": "Valproate-related amide; precise antiseizure mechanism is not established, with valproate-like effects on GABAergic and ion-channel systems proposed but not definitive.",
        "mechanism_source": f"{PUBCHEM}; {SILLS}",
        "mechanism_source_tier": "Historical/limited",
        "mechanism_confidence": "Limited",
    },
    "vigabatrin": {
        "mechanism_of_action": "Precise anti-seizure mechanism is unknown, but effect is believed to result from irreversible inhibition of GABA transaminase, increasing CNS GABA levels.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "High",
    },
    "zonisamide": {
        "mechanism_of_action": "Precise mechanism is unknown; in vitro data suggest sodium-channel blockade and reduced T-type calcium currents, with weak carbonic-anhydrase inhibition of uncertain therapeutic contribution.",
        "mechanism_source": FDA,
        "mechanism_source_tier": "FDA label",
        "mechanism_confidence": "Moderate",
    },
}


NEW_FIELDS = ["mechanism_source", "mechanism_source_tier", "mechanism_confidence"]


def split_sources(value):
    return [part.strip() for part in (value or "").split(";") if part.strip()]


def source_union(existing, additions):
    seen = []
    for source in split_sources(existing) + split_sources(additions):
        if source not in seen:
            seen.append(source)
    return "; ".join(seen)


def build_fieldnames(fieldnames):
    fieldnames = [field for field in fieldnames if field not in NEW_FIELDS]
    output = []
    for field in fieldnames:
        output.append(field)
        if field == "mechanism_of_action":
            output.extend(NEW_FIELDS)
    return output


def main():
    with CSV_PATH.open(newline="", encoding="utf-8") as handle:
        reader = csv.DictReader(handle)
        rows = list(reader)
        fieldnames = build_fieldnames(reader.fieldnames or [])

    missing = sorted(set(row["generic_name"] for row in rows) - set(MOA))
    extra = sorted(set(MOA) - set(row["generic_name"] for row in rows))
    if missing or extra:
        raise SystemExit(f"MOA mapping mismatch. Missing={missing}; extra={extra}")

    for row in rows:
        update = MOA[row["generic_name"]]
        row.update(update)
        row["evidence_sources"] = source_union(row["evidence_sources"], update["mechanism_source"])
        row["data_most_recently_refreshed"] = REFRESH_DATE

    with CSV_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(rows)

    AUDIT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with AUDIT_PATH.open("w", newline="", encoding="utf-8") as handle:
        writer = csv.DictWriter(
            handle,
            fieldnames=[
                "generic_name",
                "mechanism_of_action",
                "mechanism_source",
                "mechanism_source_tier",
                "mechanism_confidence",
                "data_most_recently_refreshed",
            ],
        )
        writer.writeheader()
        for row in rows:
            writer.writerow({field: row[field] for field in writer.fieldnames})

    print(f"Updated {len(rows)} mechanism rows and wrote {AUDIT_PATH.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
