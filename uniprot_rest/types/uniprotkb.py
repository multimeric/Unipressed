from typing import Union, Iterable
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

Existence: TypeAlias = Literal["1", "2", "3", "4", "5"]
CcevCofactorChebiEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class CcevCofactorChebi(TypedDict):
    query: str
    evidence: CcevCofactorChebiEvidence


CcevCofactorNoteEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevCofactorNote(TypedDict):
    query: str
    evidence: CcevCofactorNoteEvidence


CcevBpcpEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevBpcp(TypedDict):
    query: str
    evidence: CcevBpcpEvidence


CcevBpcpAbsorptionEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevBpcpAbsorption(TypedDict):
    query: str
    evidence: CcevBpcpAbsorptionEvidence


CcevBpcpKineticsEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevBpcpKinetics(TypedDict):
    query: str
    evidence: CcevBpcpKineticsEvidence


CcevBpcpPhDependenceEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevBpcpPhDependence(TypedDict):
    query: str
    evidence: CcevBpcpPhDependenceEvidence


CcevBpcpRedoxPotentialEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevBpcpRedoxPotential(TypedDict):
    query: str
    evidence: CcevBpcpRedoxPotentialEvidence


CcevBpcpTempDependenceEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevBpcpTempDependence(TypedDict):
    query: str
    evidence: CcevBpcpTempDependenceEvidence


CcevCatalyticActivityEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevCatalyticActivity(TypedDict):
    query: str
    evidence: CcevCatalyticActivityEvidence


CcevActivityRegulationEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevActivityRegulation(TypedDict):
    query: str
    evidence: CcevActivityRegulationEvidence


CcevFunctionEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevFunction(TypedDict):
    query: str
    evidence: CcevFunctionEvidence


CcevCautionEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevCaution(TypedDict):
    query: str
    evidence: CcevCautionEvidence


FtevSitesEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevSites(TypedDict):
    query: str
    evidence: FtevSitesEvidence


FtevActSiteEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevActSite(TypedDict):
    query: str
    evidence: FtevActSiteEvidence


FtevMetalEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevMetal(TypedDict):
    query: str
    evidence: FtevMetalEvidence


FtevBindingEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevBinding(TypedDict):
    query: str
    evidence: FtevBindingEvidence


FtevSiteEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevSite(TypedDict):
    query: str
    evidence: FtevSiteEvidence


FtevCaBindEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevCaBind(TypedDict):
    query: str
    evidence: FtevCaBindEvidence


FtevDnaBindEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevDnaBind(TypedDict):
    query: str
    evidence: FtevDnaBindEvidence


FtevNpBindEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevNpBind(TypedDict):
    query: str
    evidence: FtevNpBindEvidence


CcevPathwayEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevPathway(TypedDict):
    query: str
    evidence: CcevPathwayEvidence


CcevMiscellaneousEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevMiscellaneous(TypedDict):
    query: str
    evidence: CcevMiscellaneousEvidence


CcevSclTermEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevSclTerm(TypedDict):
    query: str
    evidence: CcevSclTermEvidence


CcevSclNoteEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevSclNote(TypedDict):
    query: str
    evidence: CcevSclNoteEvidence


FtevTransmemEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevTransmem(TypedDict):
    query: str
    evidence: FtevTransmemEvidence


FtevTopoDomEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevTopoDom(TypedDict):
    query: str
    evidence: FtevTopoDomEvidence


FtevIntramemEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevIntramem(TypedDict):
    query: str
    evidence: FtevIntramemEvidence


CcevDiseaseEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevDisease(TypedDict):
    query: str
    evidence: CcevDiseaseEvidence


CcevAllergenEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevAllergen(TypedDict):
    query: str
    evidence: CcevAllergenEvidence


CcevToxicDoseEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevToxicDose(TypedDict):
    query: str
    evidence: CcevToxicDoseEvidence


CcevBiotechnologyEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevBiotechnology(TypedDict):
    query: str
    evidence: CcevBiotechnologyEvidence


CcevPharmaceuticalEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevPharmaceutical(TypedDict):
    query: str
    evidence: CcevPharmaceuticalEvidence


CcevDisruptionPhenotypeEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevDisruptionPhenotype(TypedDict):
    query: str
    evidence: CcevDisruptionPhenotypeEvidence


FtevMutagenEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevMutagen(TypedDict):
    query: str
    evidence: FtevMutagenEvidence


CcevPtmEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevPtm(TypedDict):
    query: str
    evidence: CcevPtmEvidence


FtevModResEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevModRes(TypedDict):
    query: str
    evidence: FtevModResEvidence


FtevLipidEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevLipid(TypedDict):
    query: str
    evidence: FtevLipidEvidence


FtevCarbohydEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevCarbohyd(TypedDict):
    query: str
    evidence: FtevCarbohydEvidence


FtevDisulfidEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevDisulfid(TypedDict):
    query: str
    evidence: FtevDisulfidEvidence


FtevCrosslnkEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevCrosslnk(TypedDict):
    query: str
    evidence: FtevCrosslnkEvidence


FtevMoleculeProcessingEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevMoleculeProcessing(TypedDict):
    query: str
    evidence: FtevMoleculeProcessingEvidence


FtevChainEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevChain(TypedDict):
    query: str
    evidence: FtevChainEvidence


FtevInitMetEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevInitMet(TypedDict):
    query: str
    evidence: FtevInitMetEvidence


FtevPeptideEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevPeptide(TypedDict):
    query: str
    evidence: FtevPeptideEvidence


FtevSignalEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevSignal(TypedDict):
    query: str
    evidence: FtevSignalEvidence


FtevPropepEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevPropep(TypedDict):
    query: str
    evidence: FtevPropepEvidence


FtevTransitEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevTransit(TypedDict):
    query: str
    evidence: FtevTransitEvidence


CcevDevelopmentalStageEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevDevelopmentalStage(TypedDict):
    query: str
    evidence: CcevDevelopmentalStageEvidence


CcevInductionEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevInduction(TypedDict):
    query: str
    evidence: CcevInductionEvidence


CcevTissueSpecificityEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevTissueSpecificity(TypedDict):
    query: str
    evidence: CcevTissueSpecificityEvidence


CcevSubunitEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevSubunit(TypedDict):
    query: str
    evidence: CcevSubunitEvidence


FtevSecstructEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevSecstruct(TypedDict):
    query: str
    evidence: FtevSecstructEvidence


FtevHelixEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevHelix(TypedDict):
    query: str
    evidence: FtevHelixEvidence


FtevTurnEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevTurn(TypedDict):
    query: str
    evidence: FtevTurnEvidence


FtevStrandEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevStrand(TypedDict):
    query: str
    evidence: FtevStrandEvidence


CcevApEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevAp(TypedDict):
    query: str
    evidence: CcevApEvidence


CcevApApuEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevApApu(TypedDict):
    query: str
    evidence: CcevApApuEvidence


CcevApAsEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevApAs(TypedDict):
    query: str
    evidence: CcevApAsEvidence


CcevApAiEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevApAi(TypedDict):
    query: str
    evidence: CcevApAiEvidence


CcevApRfEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevApRf(TypedDict):
    query: str
    evidence: CcevApRfEvidence


CcevSequenceCautionEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevSequenceCaution(TypedDict):
    query: str
    evidence: CcevSequenceCautionEvidence


CcevScMiscEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevScMisc(TypedDict):
    query: str
    evidence: CcevScMiscEvidence


CcevMassSpectrometryEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevMassSpectrometry(TypedDict):
    query: str
    evidence: CcevMassSpectrometryEvidence


CcevPolymorphismEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevPolymorphism(TypedDict):
    query: str
    evidence: CcevPolymorphismEvidence


CcevRnaEditingEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevRnaEditing(TypedDict):
    query: str
    evidence: CcevRnaEditingEvidence


FtevVariantsEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevVariants(TypedDict):
    query: str
    evidence: FtevVariantsEvidence


FtevVariantEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevVariant(TypedDict):
    query: str
    evidence: FtevVariantEvidence


FtevVarSeqEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevVarSeq(TypedDict):
    query: str
    evidence: FtevVarSeqEvidence


FtevNonStdEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevNonStd(TypedDict):
    query: str
    evidence: FtevNonStdEvidence


FtevNonTerEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevNonTer(TypedDict):
    query: str
    evidence: FtevNonTerEvidence


FtevNonConsEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevNonCons(TypedDict):
    query: str
    evidence: FtevNonConsEvidence


FtevConflictEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevConflict(TypedDict):
    query: str
    evidence: FtevConflictEvidence


FtevUnsureEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevUnsure(TypedDict):
    query: str
    evidence: FtevUnsureEvidence


FtevPositionalEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevPositional(TypedDict):
    query: str
    evidence: FtevPositionalEvidence


Organelle: TypeAlias = Literal[
    "mitochondrion",
    "plastid",
    "chloroplast",
    "cyanelle",
    "apicoplast",
    "organellar chromatophore",
    "non-photosynthetic plastid",
    "nucleomorph",
    "hydrogenosome",
]
FtevDomainEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevDomain(TypedDict):
    query: str
    evidence: FtevDomainEvidence


CcevDomainEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevDomain(TypedDict):
    query: str
    evidence: CcevDomainEvidence


FtevCoiledEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevCoiled(TypedDict):
    query: str
    evidence: FtevCoiledEvidence


FtevCompbiasEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevCompbias(TypedDict):
    query: str
    evidence: FtevCompbiasEvidence


FtevMotifEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevMotif(TypedDict):
    query: str
    evidence: FtevMotifEvidence


FtevRegionEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevRegion(TypedDict):
    query: str
    evidence: FtevRegionEvidence


FtevRepeatEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevRepeat(TypedDict):
    query: str
    evidence: FtevRepeatEvidence


CcevSimilarityEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevSimilarity(TypedDict):
    query: str
    evidence: CcevSimilarityEvidence


FtevZnFingEvidence: TypeAlias = CcevCofactorChebiEvidence


class FtevZnFing(TypedDict):
    query: str
    evidence: FtevZnFingEvidence


CcevWebresourceEvidence: TypeAlias = CcevCofactorChebiEvidence


class CcevWebresource(TypedDict):
    query: str
    evidence: CcevWebresourceEvidence


GoEvidenceEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "exp",
    "iba",
    "ic",
    "ida",
    "iep",
    "igc",
    "igi",
    "imp",
    "ipi",
    "isa",
    "ism",
    "iso",
    "iss",
    "nas",
    "tas",
    "hda",
    "hmp",
    "hgi",
    "hep",
    "htp",
    "iea",
]


class GoEvidence(TypedDict):
    query: str
    evidence: GoEvidenceEvidence


UniprotkbQuery: TypeAlias = TypedDict(
    "UniprotkbQuery",
    {
        "and": Iterable[UniprotkbQuery],
        "or": Iterable[UniprotkbQuery],
        "accession_field": NotRequired[str],
        "id_field": NotRequired[str],
        "protein_name_field": NotRequired[str],
        "gene_field": NotRequired[str],
        "organism_name_field": NotRequired[str],
        "taxonomy_name": NotRequired[str],
        "virus_host_name": NotRequired[str],
        "existence": NotRequired[Existence],
        "ec": NotRequired[str],
        "cc_cofactor_chebi": NotRequired[str],
        "ccev_cofactor_chebi": NotRequired[CcevCofactorChebi],
        "cc_cofactor_note": NotRequired[str],
        "ccev_cofactor_note": NotRequired[CcevCofactorNote],
        "cc_bpcp": NotRequired[str],
        "ccev_bpcp": NotRequired[CcevBpcp],
        "cc_bpcp_absorption": NotRequired[str],
        "ccev_bpcp_absorption": NotRequired[CcevBpcpAbsorption],
        "cc_bpcp_kinetics": NotRequired[str],
        "ccev_bpcp_kinetics": NotRequired[CcevBpcpKinetics],
        "cc_bpcp_ph_dependence": NotRequired[str],
        "ccev_bpcp_ph_dependence": NotRequired[CcevBpcpPhDependence],
        "cc_bpcp_redox_potential": NotRequired[str],
        "ccev_bpcp_redox_potential": NotRequired[CcevBpcpRedoxPotential],
        "cc_bpcp_temp_dependence": NotRequired[str],
        "ccev_bpcp_temp_dependence": NotRequired[CcevBpcpTempDependence],
        "cc_catalytic_activity_field": NotRequired[str],
        "ccev_catalytic_activity": NotRequired[CcevCatalyticActivity],
        "cc_activity_regulation": NotRequired[str],
        "ccev_activity_regulation": NotRequired[CcevActivityRegulation],
        "cc_function": NotRequired[str],
        "ccev_function": NotRequired[CcevFunction],
        "cc_caution": NotRequired[str],
        "ccev_caution": NotRequired[CcevCaution],
        "ft_sites": NotRequired[str],
        "ftlen_sites": NotRequired[tuple[int, int]],
        "ftev_sites": NotRequired[FtevSites],
        "ft_act_site": NotRequired[str],
        "ftlen_act_site": NotRequired[tuple[int, int]],
        "ftev_act_site": NotRequired[FtevActSite],
        "ft_metal": NotRequired[str],
        "ftlen_metal": NotRequired[tuple[int, int]],
        "ftev_metal": NotRequired[FtevMetal],
        "ft_binding": NotRequired[str],
        "ftlen_binding": NotRequired[tuple[int, int]],
        "ftev_binding": NotRequired[FtevBinding],
        "ft_site": NotRequired[str],
        "ftlen_site": NotRequired[tuple[int, int]],
        "ftev_site": NotRequired[FtevSite],
        "ft_ca_bind": NotRequired[str],
        "ftlen_ca_bind": NotRequired[tuple[int, int]],
        "ftev_ca_bind": NotRequired[FtevCaBind],
        "ft_dna_bind": NotRequired[str],
        "ftlen_dna_bind": NotRequired[tuple[int, int]],
        "ftev_dna_bind": NotRequired[FtevDnaBind],
        "ft_np_bind": NotRequired[str],
        "ftlen_np_bind": NotRequired[tuple[int, int]],
        "ftev_np_bind": NotRequired[FtevNpBind],
        "cc_pathway": NotRequired[str],
        "ccev_pathway": NotRequired[CcevPathway],
        "cc_miscellaneous": NotRequired[str],
        "ccev_miscellaneous": NotRequired[CcevMiscellaneous],
        "cc_scl_term_field": NotRequired[str],
        "ccev_scl_term": NotRequired[CcevSclTerm],
        "cc_scl_note": NotRequired[str],
        "ccev_scl_note": NotRequired[CcevSclNote],
        "ft_transmem": NotRequired[str],
        "ftlen_transmem": NotRequired[tuple[int, int]],
        "ftev_transmem": NotRequired[FtevTransmem],
        "ft_topo_dom": NotRequired[str],
        "ftlen_topo_dom": NotRequired[tuple[int, int]],
        "ftev_topo_dom": NotRequired[FtevTopoDom],
        "ft_intramem": NotRequired[str],
        "ftlen_intramem": NotRequired[tuple[int, int]],
        "ftev_intramem": NotRequired[FtevIntramem],
        "cc_disease": NotRequired[str],
        "ccev_disease": NotRequired[CcevDisease],
        "cc_allergen": NotRequired[str],
        "ccev_allergen": NotRequired[CcevAllergen],
        "cc_toxic_dose": NotRequired[str],
        "ccev_toxic_dose": NotRequired[CcevToxicDose],
        "cc_biotechnology": NotRequired[str],
        "ccev_biotechnology": NotRequired[CcevBiotechnology],
        "cc_pharmaceutical": NotRequired[str],
        "ccev_pharmaceutical": NotRequired[CcevPharmaceutical],
        "cc_disruption_phenotype": NotRequired[str],
        "ccev_disruption_phenotype": NotRequired[CcevDisruptionPhenotype],
        "ft_mutagen": NotRequired[str],
        "ftlen_mutagen": NotRequired[tuple[int, int]],
        "ftev_mutagen": NotRequired[FtevMutagen],
        "cc_ptm": NotRequired[str],
        "ccev_ptm": NotRequired[CcevPtm],
        "ft_mod_res": NotRequired[str],
        "ftlen_mod_res": NotRequired[tuple[int, int]],
        "ftev_mod_res": NotRequired[FtevModRes],
        "ft_lipid": NotRequired[str],
        "ftlen_lipid": NotRequired[tuple[int, int]],
        "ftev_lipid": NotRequired[FtevLipid],
        "ft_carbohyd": NotRequired[str],
        "ftlen_carbohyd": NotRequired[tuple[int, int]],
        "ftev_carbohyd": NotRequired[FtevCarbohyd],
        "ft_disulfid": NotRequired[str],
        "ftlen_disulfid": NotRequired[tuple[int, int]],
        "ftev_disulfid": NotRequired[FtevDisulfid],
        "ft_crosslnk": NotRequired[str],
        "ftlen_crosslnk": NotRequired[tuple[int, int]],
        "ftev_crosslnk": NotRequired[FtevCrosslnk],
        "ft_molecule_processing": NotRequired[str],
        "ftlen_molecule_processing": NotRequired[tuple[int, int]],
        "ftev_molecule_processing": NotRequired[FtevMoleculeProcessing],
        "ft_chain": NotRequired[str],
        "ftlen_chain": NotRequired[tuple[int, int]],
        "ftev_chain": NotRequired[FtevChain],
        "ft_init_met": NotRequired[str],
        "ftlen_init_met": NotRequired[tuple[int, int]],
        "ftev_init_met": NotRequired[FtevInitMet],
        "ft_peptide": NotRequired[str],
        "ftlen_peptide": NotRequired[tuple[int, int]],
        "ftev_peptide": NotRequired[FtevPeptide],
        "ft_signal": NotRequired[str],
        "ftlen_signal": NotRequired[tuple[int, int]],
        "ftev_signal": NotRequired[FtevSignal],
        "ft_propep": NotRequired[str],
        "ftlen_propep": NotRequired[tuple[int, int]],
        "ftev_propep": NotRequired[FtevPropep],
        "ft_transit": NotRequired[str],
        "ftlen_transit": NotRequired[tuple[int, int]],
        "ftev_transit": NotRequired[FtevTransit],
        "cc_developmental_stage": NotRequired[str],
        "ccev_developmental_stage": NotRequired[CcevDevelopmentalStage],
        "cc_induction": NotRequired[str],
        "ccev_induction": NotRequired[CcevInduction],
        "cc_tissue_specificity": NotRequired[str],
        "ccev_tissue_specificity": NotRequired[CcevTissueSpecificity],
        "interactor": NotRequired[str],
        "cc_subunit": NotRequired[str],
        "ccev_subunit": NotRequired[CcevSubunit],
        "structure_3d": NotRequired[bool],
        "ft_secstruct": NotRequired[str],
        "ftlen_secstruct": NotRequired[tuple[int, int]],
        "ftev_secstruct": NotRequired[FtevSecstruct],
        "ft_helix": NotRequired[str],
        "ftlen_helix": NotRequired[tuple[int, int]],
        "ftev_helix": NotRequired[FtevHelix],
        "ft_turn": NotRequired[str],
        "ftlen_turn": NotRequired[tuple[int, int]],
        "ftev_turn": NotRequired[FtevTurn],
        "ft_strand": NotRequired[str],
        "ftlen_strand": NotRequired[tuple[int, int]],
        "ftev_strand": NotRequired[FtevStrand],
        "mass_range": NotRequired[tuple[int, int]],
        "length_range": NotRequired[tuple[int, int]],
        "cc_ap": NotRequired[str],
        "ccev_ap": NotRequired[CcevAp],
        "cc_ap_apu": NotRequired[str],
        "ccev_ap_apu": NotRequired[CcevApApu],
        "cc_ap_as": NotRequired[str],
        "ccev_ap_as": NotRequired[CcevApAs],
        "cc_ap_ai": NotRequired[str],
        "ccev_ap_ai": NotRequired[CcevApAi],
        "cc_ap_rf": NotRequired[str],
        "ccev_ap_rf": NotRequired[CcevApRf],
        "cc_sequence_caution": NotRequired[str],
        "ccev_sequence_caution": NotRequired[CcevSequenceCaution],
        "cc_sc_framesh": NotRequired[str],
        "cc_sc_einit": NotRequired[str],
        "cc_sc_eterm": NotRequired[str],
        "cc_sc_epred": NotRequired[str],
        "cc_sc_etran": NotRequired[str],
        "cc_sc_misc": NotRequired[str],
        "ccev_sc_misc": NotRequired[CcevScMisc],
        "cc_mass_spectrometry": NotRequired[str],
        "ccev_mass_spectrometry": NotRequired[CcevMassSpectrometry],
        "cc_polymorphism": NotRequired[str],
        "ccev_polymorphism": NotRequired[CcevPolymorphism],
        "cc_rna_editing": NotRequired[str],
        "ccev_rna_editing": NotRequired[CcevRnaEditing],
        "ft_variants": NotRequired[str],
        "ftlen_variants": NotRequired[tuple[int, int]],
        "ftev_variants": NotRequired[FtevVariants],
        "ft_variant": NotRequired[str],
        "ftlen_variant": NotRequired[tuple[int, int]],
        "ftev_variant": NotRequired[FtevVariant],
        "ft_var_seq": NotRequired[str],
        "ftlen_var_seq": NotRequired[tuple[int, int]],
        "ftev_var_seq": NotRequired[FtevVarSeq],
        "ft_non_std": NotRequired[str],
        "ftlen_non_std": NotRequired[tuple[int, int]],
        "ftev_non_std": NotRequired[FtevNonStd],
        "ft_non_ter": NotRequired[str],
        "ftlen_non_ter": NotRequired[tuple[int, int]],
        "ftev_non_ter": NotRequired[FtevNonTer],
        "ft_non_cons": NotRequired[str],
        "ftlen_non_cons": NotRequired[tuple[int, int]],
        "ftev_non_cons": NotRequired[FtevNonCons],
        "ft_conflict": NotRequired[str],
        "ftlen_conflict": NotRequired[tuple[int, int]],
        "ftev_conflict": NotRequired[FtevConflict],
        "ft_unsure": NotRequired[str],
        "ftlen_unsure": NotRequired[tuple[int, int]],
        "ftev_unsure": NotRequired[FtevUnsure],
        "ft_positional": NotRequired[str],
        "ftlen_positional": NotRequired[tuple[int, int]],
        "ftev_positional": NotRequired[FtevPositional],
        "fragment": NotRequired[bool],
        "organelle": NotRequired[Organelle],
        "precursor": NotRequired[bool],
        "tissue": NotRequired[str],
        "strain": NotRequired[str],
        "plasmid": NotRequired[str],
        "transposon": NotRequired[str],
        "ft_domain": NotRequired[str],
        "ftlen_domain": NotRequired[tuple[int, int]],
        "ftev_domain": NotRequired[FtevDomain],
        "cc_domain": NotRequired[str],
        "ccev_domain": NotRequired[CcevDomain],
        "family": NotRequired[str],
        "ft_coiled": NotRequired[str],
        "ftlen_coiled": NotRequired[tuple[int, int]],
        "ftev_coiled": NotRequired[FtevCoiled],
        "ft_compbias": NotRequired[str],
        "ftlen_compbias": NotRequired[tuple[int, int]],
        "ftev_compbias": NotRequired[FtevCompbias],
        "ft_motif": NotRequired[str],
        "ftlen_motif": NotRequired[tuple[int, int]],
        "ftev_motif": NotRequired[FtevMotif],
        "ft_region": NotRequired[str],
        "ftlen_region": NotRequired[tuple[int, int]],
        "ftev_region": NotRequired[FtevRegion],
        "ft_repeat": NotRequired[str],
        "ftlen_repeat": NotRequired[tuple[int, int]],
        "ftev_repeat": NotRequired[FtevRepeat],
        "cc_similarity": NotRequired[str],
        "ccev_similarity": NotRequired[CcevSimilarity],
        "ft_zn_fing": NotRequired[str],
        "ftlen_zn_fing": NotRequired[tuple[int, int]],
        "ftev_zn_fing": NotRequired[FtevZnFing],
        "xref_any": NotRequired[str],
        "xref_embl": NotRequired[str],
        "xref_ccds": NotRequired[str],
        "xref_pir": NotRequired[str],
        "xref_refseq": NotRequired[str],
        "xref_pdb": NotRequired[str],
        "xref_pdbsum": NotRequired[str],
        "xref_pcddb": NotRequired[str],
        "xref_sasbdb": NotRequired[str],
        "xref_bmrb": NotRequired[str],
        "xref_smr": NotRequired[str],
        "xref_alphafolddb": NotRequired[str],
        "xref_biogrid": NotRequired[str],
        "xref_complexportal": NotRequired[str],
        "xref_corum": NotRequired[str],
        "xref_dip": NotRequired[str],
        "xref_elm": NotRequired[str],
        "xref_intact": NotRequired[str],
        "xref_mint": NotRequired[str],
        "xref_string": NotRequired[str],
        "xref_bindingdb": NotRequired[str],
        "xref_chembl": NotRequired[str],
        "xref_drugbank": NotRequired[str],
        "xref_guidetopharmacology": NotRequired[str],
        "xref_swisslipids": NotRequired[str],
        "xref_drugcentral": NotRequired[str],
        "xref_allergome": NotRequired[str],
        "xref_cazy": NotRequired[str],
        "xref_esther": NotRequired[str],
        "xref_imgt_gene-db": NotRequired[str],
        "xref_merops": NotRequired[str],
        "xref_moondb": NotRequired[str],
        "xref_moonprot": NotRequired[str],
        "xref_clae": NotRequired[str],
        "xref_peroxibase": NotRequired[str],
        "xref_rebase": NotRequired[str],
        "xref_tcdb": NotRequired[str],
        "xref_unilectin": NotRequired[str],
        "xref_carbonyldb": NotRequired[str],
        "xref_depod": NotRequired[str],
        "xref_glyconnect": NotRequired[str],
        "xref_glygen": NotRequired[str],
        "xref_iptmnet": NotRequired[str],
        "xref_phosphositeplus": NotRequired[str],
        "xref_swisspalm": NotRequired[str],
        "xref_unicarbkb": NotRequired[str],
        "xref_metosite": NotRequired[str],
        "xref_biomuta": NotRequired[str],
        "xref_dmdm": NotRequired[str],
        "xref_dbsnp": NotRequired[str],
        "xref_compluyeast-2dpage": NotRequired[str],
        "xref_dosac-cobs-2dpage": NotRequired[str],
        "xref_ogp": NotRequired[str],
        "xref_reproduction-2dpage": NotRequired[str],
        "xref_swiss-2dpage": NotRequired[str],
        "xref_ucd-2dpage": NotRequired[str],
        "xref_world-2dpage": NotRequired[str],
        "xref_cptac": NotRequired[str],
        "xref_epd": NotRequired[str],
        "xref_maxqb": NotRequired[str],
        "xref_paxdb": NotRequired[str],
        "xref_peptideatlas": NotRequired[str],
        "xref_pride": NotRequired[str],
        "xref_promex": NotRequired[str],
        "xref_proteomicsdb": NotRequired[str],
        "xref_topdownproteomics": NotRequired[str],
        "xref_jpost": NotRequired[str],
        "xref_massive": NotRequired[str],
        "xref_dnasu": NotRequired[str],
        "xref_abcd": NotRequired[str],
        "xref_antibodypedia": NotRequired[str],
        "xref_cptc": NotRequired[str],
        "xref_ensembl": NotRequired[str],
        "xref_ensemblbacteria": NotRequired[str],
        "xref_ensemblfungi": NotRequired[str],
        "xref_ensemblmetazoa": NotRequired[str],
        "xref_ensemblplants": NotRequired[str],
        "xref_ensemblprotists": NotRequired[str],
        "xref_geneid": NotRequired[str],
        "xref_gramene": NotRequired[str],
        "xref_kegg": NotRequired[str],
        "xref_mane-select": NotRequired[str],
        "xref_patric": NotRequired[str],
        "xref_ucsc": NotRequired[str],
        "xref_vectorbase": NotRequired[str],
        "xref_wbparasite": NotRequired[str],
        "xref_wbparasitetranscriptprotein": NotRequired[str],
        "xref_arachnoserver": NotRequired[str],
        "xref_araport": NotRequired[str],
        "xref_cgd": NotRequired[str],
        "xref_conoserver": NotRequired[str],
        "xref_ctd": NotRequired[str],
        "xref_dictybase": NotRequired[str],
        "xref_disgenet": NotRequired[str],
        "xref_echobase": NotRequired[str],
        "xref_euhcvdb": NotRequired[str],
        "xref_veupathdb": NotRequired[str],
        "xref_flybase": NotRequired[str],
        "xref_genecards": NotRequired[str],
        "xref_genereviews": NotRequired[str],
        "xref_hgnc": NotRequired[str],
        "xref_hpa": NotRequired[str],
        "xref_legiolist": NotRequired[str],
        "xref_leproma": NotRequired[str],
        "xref_maizegdb": NotRequired[str],
        "xref_malacards": NotRequired[str],
        "xref_mgi": NotRequired[str],
        "xref_mim": NotRequired[str],
        "xref_niagads": NotRequired[str],
        "xref_nextprot": NotRequired[str],
        "xref_opentargets": NotRequired[str],
        "xref_orphanet": NotRequired[str],
        "xref_pharmgkb": NotRequired[str],
        "xref_pombase": NotRequired[str],
        "xref_pseudocap": NotRequired[str],
        "xref_rgd": NotRequired[str],
        "xref_sgd": NotRequired[str],
        "xref_tair": NotRequired[str],
        "xref_tuberculist": NotRequired[str],
        "xref_vgnc": NotRequired[str],
        "xref_wormbase": NotRequired[str],
        "xref_xenbase": NotRequired[str],
        "xref_zfin": NotRequired[str],
        "xref_eggnog": NotRequired[str],
        "xref_genetree": NotRequired[str],
        "xref_hogenom": NotRequired[str],
        "xref_inparanoid": NotRequired[str],
        "xref_ko": NotRequired[str],
        "xref_oma": NotRequired[str],
        "xref_orthodb": NotRequired[str],
        "xref_phylomedb": NotRequired[str],
        "xref_treefam": NotRequired[str],
        "xref_biocyc": NotRequired[str],
        "xref_brenda": NotRequired[str],
        "xref_reactome": NotRequired[str],
        "xref_sabio-rk": NotRequired[str],
        "xref_signalink": NotRequired[str],
        "xref_signor": NotRequired[str],
        "xref_unipathway": NotRequired[str],
        "xref_plantreactome": NotRequired[str],
        "xref_pathwaycommons": NotRequired[str],
        "xref_chitars": NotRequired[str],
        "xref_evolutionarytrace": NotRequired[str],
        "xref_genewiki": NotRequired[str],
        "xref_genomernai": NotRequired[str],
        "xref_phi-base": NotRequired[str],
        "xref_pro": NotRequired[str],
        "xref_pharos": NotRequired[str],
        "xref_rnact": NotRequired[str],
        "xref_biogrid-orcs": NotRequired[str],
        "xref_bgee": NotRequired[str],
        "xref_cleanex": NotRequired[str],
        "xref_collectf": NotRequired[str],
        "xref_expressionatlas": NotRequired[str],
        "xref_genevisible": NotRequired[str],
        "xref_cdd": NotRequired[str],
        "xref_gene3d": NotRequired[str],
        "xref_hamap": NotRequired[str],
        "xref_ideal": NotRequired[str],
        "xref_interpro": NotRequired[str],
        "xref_panther": NotRequired[str],
        "xref_pfam": NotRequired[str],
        "xref_pirsf": NotRequired[str],
        "xref_prints": NotRequired[str],
        "xref_prodom": NotRequired[str],
        "xref_sfld": NotRequired[str],
        "xref_smart": NotRequired[str],
        "xref_supfam": NotRequired[str],
        "xref_tigrfams": NotRequired[str],
        "xref_prosite": NotRequired[str],
        "xref_disprot": NotRequired[str],
        "xref_go": NotRequired[str],
        "xref_proteomes": NotRequired[str],
        "database": NotRequired[str],
        "cc_webresource": NotRequired[str],
        "ccev_webresource": NotRequired[CcevWebresource],
        "date_created": NotRequired[tuple[date, date]],
        "date_modified": NotRequired[tuple[date, date]],
        "date_sequence_modified": NotRequired[tuple[date, date]],
        "go_field": NotRequired[str],
        "go_evidence": NotRequired[GoEvidence],
        "chebi_field": NotRequired[str],
        "inchikey_field": NotRequired[str],
        "keyword_field": NotRequired[str],
        "lit_author": NotRequired[str],
        "lit_journal": NotRequired[str],
        "lit_pubdate": NotRequired[tuple[date, date]],
        "lit_pubmed": NotRequired[str],
        "lit_title": NotRequired[str],
        "lit_citation_id": NotRequired[str],
        "computational_pubmed_id": NotRequired[str],
        "community_pubmed_id": NotRequired[str],
        "proteome": NotRequired[str],
        "proteome_component": NotRequired[str],
        "cited_for": NotRequired[str],
        "reviewed": NotRequired[bool],
        "active": NotRequired[bool],
        "uniref_cluster_50": NotRequired[str],
        "uniref_cluster_90": NotRequired[str],
        "uniref_cluster_100": NotRequired[str],
        "uniparc": NotRequired[str],
    },
)
UniprotkbNamesTaxonomy: TypeAlias = Literal[
    "accession",
    "id",
    "gene_names",
    "gene_oln",
    "gene_orf",
    "gene_primary",
    "gene_synonym",
    "organism_name",
    "organism_id",
    "protein_name",
    "xref_proteomes",
    "lineage",
    "lineage_ids",
    "virus_hosts",
]
UniprotkbSequences: TypeAlias = Literal[
    "cc_alternative_products",
    "ft_var_seq",
    "error_gmodel_pred",
    "fragment",
    "organelle",
    "length",
    "mass",
    "cc_mass_spectrometry",
    "ft_variant",
    "ft_non_cons",
    "ft_non_std",
    "ft_non_ter",
    "cc_polymorphism",
    "cc_rna_editing",
    "sequence",
    "cc_sequence_caution",
    "ft_conflict",
    "ft_unsure",
    "sequence_version",
]
UniprotkbFunction: TypeAlias = Literal[
    "absorption",
    "ft_act_site",
    "ft_binding",
    "ft_ca_bind",
    "cc_catalytic_activity",
    "cc_cofactor",
    "ft_dna_bind",
    "ec",
    "cc_activity_regulation",
    "cc_function",
    "kinetics",
    "ft_metal",
    "ft_np_bind",
    "cc_pathway",
    "ph_dependence",
    "redox_potential",
    "rhea",
    "ft_site",
    "temp_dependence",
]
UniprotkbMiscellaneous: TypeAlias = Literal[
    "annotation_score",
    "cc_caution",
    "keyword",
    "keywordid",
    "cc_miscellaneous",
    "protein_existence",
    "reviewed",
    "tools",
    "uniparc_id",
    "comment_count",
    "feature_count",
]
UniprotkbInteraction: TypeAlias = Literal["cc_interaction", "cc_subunit"]
UniprotkbExpression: TypeAlias = Literal[
    "cc_developmental_stage", "cc_induction", "cc_tissue_specificity"
]
UniprotkbGeneOntologyGo: TypeAlias = Literal["go_p", "go_c", "go", "go_f", "go_id"]
UniprotkbPathologyBiotech: TypeAlias = Literal[
    "cc_allergen",
    "cc_biotechnology",
    "cc_disruption_phenotype",
    "cc_disease",
    "ft_mutagen",
    "cc_pharmaceutical",
    "cc_toxic_dose",
]
UniprotkbSubcellularLocation: TypeAlias = Literal[
    "ft_intramem", "cc_subcellular_location", "ft_topo_dom", "ft_transmem"
]
UniprotkbPtmProcessing: TypeAlias = Literal[
    "ft_chain",
    "ft_crosslnk",
    "ft_disulfid",
    "ft_carbohyd",
    "ft_init_met",
    "ft_lipid",
    "ft_mod_res",
    "ft_peptide",
    "cc_ptm",
    "ft_propep",
    "ft_signal",
    "ft_transit",
]
UniprotkbStructure: TypeAlias = Literal[
    "structure_3d", "ft_strand", "ft_helix", "ft_turn"
]
UniprotkbPublications: TypeAlias = Literal[
    "lit_pubmed_id",
]
UniprotkbDateOf: TypeAlias = Literal[
    "date_created", "date_modified", "date_sequence_modified", "version"
]
UniprotkbFamilyDomains: TypeAlias = Literal[
    "ft_coiled",
    "ft_compbias",
    "cc_domain",
    "ft_domain",
    "ft_motif",
    "protein_families",
    "ft_region",
    "ft_repeat",
    "ft_zn_fing",
]
UniprotkbSequence: TypeAlias = Literal[
    "xref_ccds", "xref_embl", "xref_pir", "xref_refseq"
]
UniprotkbThreedStructure: TypeAlias = Literal[
    "xref_alphafolddb",
    "xref_bmrb",
    "xref_pcddb",
    "xref_pdb",
    "xref_pdbsum",
    "xref_sasbdb",
    "xref_smr",
]
UniprotkbProteinProteinInteraction: TypeAlias = Literal[
    "xref_biogrid",
    "xref_corum",
    "xref_complexportal",
    "xref_dip",
    "xref_elm",
    "xref_intact",
    "xref_mint",
    "xref_string",
]
UniprotkbChemistry: TypeAlias = Literal[
    "xref_bindingdb",
    "xref_chembl",
    "xref_drugbank",
    "xref_drugcentral",
    "xref_guidetopharmacology",
    "xref_swisslipids",
]
UniprotkbProteinFamilygroup: TypeAlias = Literal[
    "xref_allergome",
    "xref_cazy",
    "xref_clae",
    "xref_esther",
    "xref_imgt_gene-db",
    "xref_merops",
    "xref_moondb",
    "xref_moonprot",
    "xref_peroxibase",
    "xref_rebase",
    "xref_tcdb",
    "xref_unilectin",
]
UniprotkbPtm: TypeAlias = Literal[
    "xref_carbonyldb",
    "xref_depod",
    "xref_glyconnect",
    "xref_glygen",
    "xref_metosite",
    "xref_phosphositeplus",
    "xref_swisspalm",
    "xref_unicarbkb",
    "xref_iptmnet",
]
UniprotkbPolymorphismAndMutation: TypeAlias = Literal[
    "xref_biomuta", "xref_dmdm", "xref_dbsnp"
]
UniprotkbTwodGel: TypeAlias = Literal[
    "xref_compluyeast-2dpage",
    "xref_dosac-cobs-2dpage",
    "xref_ogp",
    "xref_reproduction-2dpage",
    "xref_swiss-2dpage",
    "xref_ucd-2dpage",
    "xref_world-2dpage",
]
UniprotkbProteomic: TypeAlias = Literal[
    "xref_cptac",
    "xref_epd",
    "xref_massive",
    "xref_maxqb",
    "xref_pride",
    "xref_paxdb",
    "xref_peptideatlas",
    "xref_promex",
    "xref_proteomicsdb",
    "xref_topdownproteomics",
    "xref_jpost",
]
UniprotkbProtocolsAndMaterials: TypeAlias = Literal[
    "xref_abcd", "xref_antibodypedia", "xref_cptc", "xref_dnasu"
]
UniprotkbGenomeAnnotation: TypeAlias = Literal[
    "xref_ensembl",
    "xref_ensemblbacteria",
    "xref_ensemblfungi",
    "xref_ensemblmetazoa",
    "xref_ensemblplants",
    "xref_ensemblprotists",
    "xref_geneid",
    "xref_gramene",
    "xref_kegg",
    "xref_mane-select",
    "xref_patric",
    "xref_ucsc",
    "xref_vectorbase",
    "xref_wbparasite",
    "xref_wbparasitetranscriptprotein",
]
UniprotkbOrganismSpecific: TypeAlias = Literal[
    "xref_arachnoserver",
    "xref_araport",
    "xref_cgd",
    "xref_ctd",
    "xref_conoserver",
    "xref_disgenet",
    "xref_echobase",
    "xref_flybase",
    "xref_genecards",
    "xref_genereviews",
    "xref_hgnc",
    "xref_hpa",
    "xref_legiolist",
    "xref_leproma",
    "xref_mgi",
    "xref_mim",
    "xref_maizegdb",
    "xref_malacards",
    "xref_niagads",
    "xref_opentargets",
    "xref_orphanet",
    "xref_pharmgkb",
    "xref_pombase",
    "xref_pseudocap",
    "xref_rgd",
    "xref_sgd",
    "xref_tair",
    "xref_tuberculist",
    "xref_veupathdb",
    "xref_vgnc",
    "xref_wormbase",
    "xref_xenbase",
    "xref_zfin",
    "xref_dictybase",
    "xref_euhcvdb",
    "xref_nextprot",
]
UniprotkbPhylogenomic: TypeAlias = Literal[
    "xref_genetree",
    "xref_hogenom",
    "xref_inparanoid",
    "xref_ko",
    "xref_oma",
    "xref_orthodb",
    "xref_phylomedb",
    "xref_treefam",
    "xref_eggnog",
]
UniprotkbEnzymeAndPathway: TypeAlias = Literal[
    "xref_brenda",
    "xref_biocyc",
    "xref_pathwaycommons",
    "xref_plantreactome",
    "xref_reactome",
    "xref_sabio-rk",
    "xref_signor",
    "xref_signalink",
    "xref_unipathway",
]
UniprotkbOther: TypeAlias = Literal[
    "xref_biogrid-orcs",
    "xref_chitars",
    "xref_evolutionarytrace",
    "xref_genewiki",
    "xref_genomernai",
    "xref_phi-base",
    "xref_pro",
    "xref_pharos",
    "xref_rnact",
]
UniprotkbGeneExpression: TypeAlias = Literal[
    "xref_bgee",
    "xref_cleanex",
    "xref_collectf",
    "xref_expressionatlas",
    "xref_genevisible",
]
UniprotkbFamilyAndDomain: TypeAlias = Literal[
    "xref_cdd",
    "xref_disprot",
    "xref_gene3d",
    "xref_hamap",
    "xref_ideal",
    "xref_interpro",
    "xref_panther",
    "xref_pirsf",
    "xref_prints",
    "xref_prosite",
    "xref_pfam",
    "xref_prodom",
    "xref_sfld",
    "xref_smart",
    "xref_supfam",
    "xref_tigrfams",
]
UniprotkbFields: TypeAlias = Literal[
    UniprotkbNamesTaxonomy,
    UniprotkbSequences,
    UniprotkbFunction,
    UniprotkbMiscellaneous,
    UniprotkbInteraction,
    UniprotkbExpression,
    UniprotkbGeneOntologyGo,
    UniprotkbPathologyBiotech,
    UniprotkbSubcellularLocation,
    UniprotkbPtmProcessing,
    UniprotkbStructure,
    UniprotkbPublications,
    UniprotkbDateOf,
    UniprotkbFamilyDomains,
    UniprotkbSequence,
    UniprotkbThreedStructure,
    UniprotkbProteinProteinInteraction,
    UniprotkbChemistry,
    UniprotkbProteinFamilygroup,
    UniprotkbPtm,
    UniprotkbPolymorphismAndMutation,
    UniprotkbTwodGel,
    UniprotkbProteomic,
    UniprotkbProtocolsAndMaterials,
    UniprotkbGenomeAnnotation,
    UniprotkbOrganismSpecific,
    UniprotkbPhylogenomic,
    UniprotkbEnzymeAndPathway,
    UniprotkbOther,
    UniprotkbGeneExpression,
    UniprotkbFamilyAndDomain,
]


@dataclass
class UniprotkbSearch(uniprot_rest.Search):
    dataset: Literal["uniprotkb"] = field(default="uniprotkb", init=False)
    query: UniprotkbQuery
    fields: UniprotkbFields

