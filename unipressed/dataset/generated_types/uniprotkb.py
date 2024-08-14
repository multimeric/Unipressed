from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

Existence: TypeAlias = Literal["1", "2", "3", "4", "5"]
Organelle: TypeAlias = Literal[
    "mitochondrion",
    "plasmid",
    "plastid",
    "chloroplast",
    "cyanelle",
    "apicoplast",
    "organellar chromatophore",
    "non-photosynthetic plastid",
    "nucleomorph",
    "hydrogenosome",
]


class UniprotkbQueryDict(TypedDict):
    and_: NotRequired[Iterable["UniprotkbQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UniprotkbQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UniprotkbQuery"]]
    "Negate a filter"
    accession: NotRequired[str]
    "UniProtKB AC\ne.g. P12345"
    id: NotRequired[str]
    "Entry Name [ID]\ne.g. P53_HUMAN"
    protein_name: NotRequired[str]
    "Protein Name [DE]\ne.g. mas5"
    gene: NotRequired[str]
    "Gene Name [GN]\ne.g. ydj1"
    organism_name: NotRequired[str]
    "Organism [OS]\ne.g. saccharomyces"
    organism_id: NotRequired[str]
    "Organism id"
    taxonomy_name: NotRequired[str]
    "Taxonomy [OC]\ne.g. human"
    taxonomy_id: NotRequired[str]
    "Taxonomy id"
    virus_host_name: NotRequired[str]
    "Virus host\ne.g. human"
    virus_host_id: NotRequired[str]
    "Virus host id"
    existence: NotRequired[Existence]
    "Protein Existence [PE]\ne.g. 1\n* 1: Evidence at protein level\n* 2: Evidence at transcript level\n* 3: Inferred from homology\n* 4: Predicted\n* 5: Uncertain"
    ec: NotRequired[str]
    "Enzyme classification [EC]\ne.g. 1.1.2.3"
    cc_cofactor_chebi: NotRequired[str]
    "Cc cofactor chebi\ne.g. 29105"
    cc_cofactor_chebi_exp: NotRequired[str]
    "Cc cofactor chebi exp\ne.g. 29105"
    cc_cofactor_note: NotRequired[str]
    "Cc cofactor note\ne.g. subunit"
    cc_cofactor_note_exp: NotRequired[str]
    "Cc cofactor note exp\ne.g. subunit"
    cc_bpcp: NotRequired[str]
    "Cc bpcp\ne.g. prosthetic"
    cc_bpcp_exp: NotRequired[str]
    "Cc bpcp exp\ne.g. prosthetic"
    cc_bpcp_absorption: NotRequired[str]
    "Cc bpcp absorption\ne.g. prosthetic"
    cc_bpcp_absorption_exp: NotRequired[str]
    "Cc bpcp absorption exp\ne.g. prosthetic"
    cc_bpcp_kinetics: NotRequired[str]
    "Cc bpcp kinetics\ne.g. aspartate"
    cc_bpcp_kinetics_exp: NotRequired[str]
    "Cc bpcp kinetics exp\ne.g. aspartate"
    cc_bpcp_ph_dependence: NotRequired[str]
    "Cc bpcp ph dependence\ne.g. optimum"
    cc_bpcp_ph_dependence_exp: NotRequired[str]
    "Cc bpcp ph dependence exp\ne.g. optimum"
    cc_bpcp_redox_potential: NotRequired[str]
    "Cc bpcp redox potential\ne.g. siroheme"
    cc_bpcp_redox_potential_exp: NotRequired[str]
    "Cc bpcp redox potential exp\ne.g. siroheme"
    cc_bpcp_temp_dependence: NotRequired[str]
    "Cc bpcp temp dependence\ne.g. *"
    cc_bpcp_temp_dependence_exp: NotRequired[str]
    "Cc bpcp temp dependence exp\ne.g. *"
    cc_catalytic_activity: NotRequired[str]
    "Cc catalytic activity\ne.g. tyrosine"
    cc_catalytic_activity_exp: NotRequired[str]
    "Cc catalytic activity exp\ne.g. tyrosine"
    cc_activity_regulation: NotRequired[str]
    "Cc activity regulation\ne.g. inhibited"
    cc_activity_regulation_exp: NotRequired[str]
    "Cc activity regulation exp\ne.g. inhibited"
    cc_function: NotRequired[str]
    "Cc function\ne.g. enzyme"
    cc_function_exp: NotRequired[str]
    "Cc function exp\ne.g. enzyme"
    cc_caution: NotRequired[str]
    "Cc caution\ne.g. kinase"
    cc_caution_exp: NotRequired[str]
    "Cc caution exp\ne.g. kinase"
    ft_sites: NotRequired[str]
    "Ft sites\ne.g. translocation"
    ft_sites_exp: NotRequired[str]
    "Ft sites exp\ne.g. translocation"
    ft_act_site: NotRequired[str]
    "Ft act site\ne.g. phosphocysteine"
    ft_act_site_exp: NotRequired[str]
    "Ft act site exp\ne.g. phosphocysteine"
    ft_binding: NotRequired[str]
    "Ft binding\ne.g. phosphocysteine"
    ft_binding_exp: NotRequired[str]
    "Ft binding exp\ne.g. phosphocysteine"
    ft_site: NotRequired[str]
    "Ft site\ne.g. phosphocysteine"
    ft_site_exp: NotRequired[str]
    "Ft site exp\ne.g. phosphocysteine"
    ft_dna_bind: NotRequired[str]
    "Ft dna bind\ne.g. *"
    ft_dna_bind_exp: NotRequired[str]
    "Ft dna bind exp\ne.g. *"
    cc_pathway: NotRequired[str]
    "Cc pathway\ne.g. metabolism"
    cc_pathway_exp: NotRequired[str]
    "Cc pathway exp\ne.g. metabolism"
    cc_miscellaneous: NotRequired[str]
    "Cc miscellaneous\ne.g. abscisic"
    cc_miscellaneous_exp: NotRequired[str]
    "Cc miscellaneous exp\ne.g. abscisic"
    cc_scl_term: NotRequired[str]
    "Cc scl term\ne.g. membrane"
    cc_scl_term_exp: NotRequired[str]
    "Cc scl term exp\ne.g. membrane"
    cc_scl_note: NotRequired[str]
    "Cc scl note\ne.g. membrane"
    cc_scl_note_exp: NotRequired[str]
    "Cc scl note exp\ne.g. membrane"
    ft_transmem: NotRequired[str]
    "Ft transmem\ne.g. forming"
    ft_transmem_exp: NotRequired[str]
    "Ft transmem exp\ne.g. forming"
    ft_topo_dom: NotRequired[str]
    "Ft topo dom\ne.g. forming"
    ft_topo_dom_exp: NotRequired[str]
    "Ft topo dom exp\ne.g. forming"
    ft_intramem: NotRequired[str]
    "Ft intramem\ne.g. forming"
    ft_intramem_exp: NotRequired[str]
    "Ft intramem exp\ne.g. forming"
    cc_disease: NotRequired[str]
    "Cc disease\ne.g. nephrotic"
    cc_disease_exp: NotRequired[str]
    "Cc disease exp\ne.g. nephrotic"
    cc_allergen: NotRequired[str]
    "Cc allergen\ne.g. allergic"
    cc_allergen_exp: NotRequired[str]
    "Cc allergen exp\ne.g. allergic"
    cc_toxic_dose: NotRequired[str]
    "Cc toxic dose\ne.g. intracistenal"
    cc_toxic_dose_exp: NotRequired[str]
    "Cc toxic dose exp\ne.g. intracistenal"
    cc_biotechnology: NotRequired[str]
    "Cc biotechnology\ne.g. vaccine"
    cc_biotechnology_exp: NotRequired[str]
    "Cc biotechnology exp\ne.g. vaccine"
    cc_pharmaceutical: NotRequired[str]
    "Cc pharmaceutical\ne.g. peptide"
    cc_pharmaceutical_exp: NotRequired[str]
    "Cc pharmaceutical exp\ne.g. peptide"
    cc_disruption_phenotype: NotRequired[str]
    "Cc disruption phenotype\ne.g. infected"
    cc_disruption_phenotype_exp: NotRequired[str]
    "Cc disruption phenotype exp\ne.g. infected"
    ft_mutagen: NotRequired[str]
    "Ft mutagen\ne.g. phosphatase"
    ft_mutagen_exp: NotRequired[str]
    "Ft mutagen exp\ne.g. phosphatase"
    cc_ptm: NotRequired[str]
    "Cc ptm\ne.g. mitosis"
    cc_ptm_exp: NotRequired[str]
    "Cc ptm exp\ne.g. mitosis"
    ft_mod_res: NotRequired[str]
    "Ft mod res\ne.g. phosphoserine"
    ft_mod_res_exp: NotRequired[str]
    "Ft mod res exp\ne.g. phosphoserine"
    ft_lipid: NotRequired[str]
    "Ft lipid\ne.g. cysteine"
    ft_lipid_exp: NotRequired[str]
    "Ft lipid exp\ne.g. cysteine"
    ft_carbohyd: NotRequired[str]
    "Ft carbohyd\ne.g. cysteine"
    ft_carbohyd_exp: NotRequired[str]
    "Ft carbohyd exp\ne.g. cysteine"
    ft_disulfid: NotRequired[str]
    "Ft disulfid\ne.g. reversible"
    ft_disulfid_exp: NotRequired[str]
    "Ft disulfid exp\ne.g. reversible"
    ft_crosslnk: NotRequired[str]
    "Ft crosslnk\ne.g. lysine"
    ft_crosslnk_exp: NotRequired[str]
    "Ft crosslnk exp\ne.g. lysine"
    ft_molecule_processing: NotRequired[str]
    "Ft molecule processing\ne.g. disulfide"
    ft_molecule_processing_exp: NotRequired[str]
    "Ft molecule processing exp\ne.g. disulfide"
    ft_chain: NotRequired[str]
    "Ft chain\ne.g. kinase"
    ft_chain_exp: NotRequired[str]
    "Ft chain exp\ne.g. kinase"
    ft_init_met: NotRequired[str]
    "Ft init met\ne.g. Removed"
    ft_init_met_exp: NotRequired[str]
    "Ft init met exp\ne.g. Removed"
    ft_peptide: NotRequired[str]
    "Ft peptide\ne.g. Removed"
    ft_peptide_exp: NotRequired[str]
    "Ft peptide exp\ne.g. Removed"
    ft_signal: NotRequired[str]
    "Ft signal\ne.g. cleaved"
    ft_signal_exp: NotRequired[str]
    "Ft signal exp\ne.g. cleaved"
    ft_propep: NotRequired[str]
    "Ft propep\ne.g. Activation peptide"
    ft_propep_exp: NotRequired[str]
    "Ft propep exp\ne.g. Activation peptide"
    ft_transit: NotRequired[str]
    "Ft transit\ne.g. Mitochondrion"
    ft_transit_exp: NotRequired[str]
    "Ft transit exp\ne.g. Mitochondrion"
    cc_developmental_stage: NotRequired[str]
    "Cc developmental stage\ne.g. brain"
    cc_developmental_stage_exp: NotRequired[str]
    "Cc developmental stage exp\ne.g. brain"
    cc_induction: NotRequired[str]
    "Cc induction\ne.g. calcium"
    cc_induction_exp: NotRequired[str]
    "Cc induction exp\ne.g. calcium"
    cc_tissue_specificity: NotRequired[str]
    "Cc tissue specificity\ne.g. pancreas"
    cc_tissue_specificity_exp: NotRequired[str]
    "Cc tissue specificity exp\ne.g. pancreas"
    interactor: NotRequired[str]
    "Binary Interaction\ne.g. EBI-1042898"
    cc_subunit: NotRequired[str]
    "Cc subunit\ne.g. homodimer"
    cc_subunit_exp: NotRequired[str]
    "Cc subunit exp\ne.g. homodimer"
    structure_3d: NotRequired[bool]
    "3D Structure\ne.g. true"
    ft_secstruct: NotRequired[str]
    "Ft secstruct\ne.g. *"
    ft_secstruct_exp: NotRequired[str]
    "Ft secstruct exp\ne.g. *"
    ft_helix: NotRequired[str]
    "Ft helix\ne.g. *"
    ft_helix_exp: NotRequired[str]
    "Ft helix exp\ne.g. *"
    ft_turn: NotRequired[str]
    "Ft turn\ne.g. *"
    ft_turn_exp: NotRequired[str]
    "Ft turn exp\ne.g. *"
    ft_strand: NotRequired[str]
    "Ft strand\ne.g. *"
    ft_strand_exp: NotRequired[str]
    "Ft strand exp\ne.g. *"
    mass: NotRequired[
        tuple[
            Union[
                int,
                Literal["*",],
            ],
            Union[
                int,
                Literal["*",],
            ],
        ]
    ]
    "Mass(Da)\ne.g. [441126 TO 441126]"
    length: NotRequired[
        tuple[
            Union[
                int,
                Literal["*",],
            ],
            Union[
                int,
                Literal["*",],
            ],
        ]
    ]
    "Sequence length\ne.g. [441 TO 450]"
    cc_ap: NotRequired[str]
    "Cc ap\ne.g. tissues"
    cc_ap_exp: NotRequired[str]
    "Cc ap exp\ne.g. tissues"
    cc_ap_apu: NotRequired[str]
    "Cc ap apu\ne.g. *"
    cc_ap_apu_exp: NotRequired[str]
    "Cc ap apu exp\ne.g. *"
    cc_ap_as: NotRequired[str]
    "Cc ap as\ne.g. experimental"
    cc_ap_as_exp: NotRequired[str]
    "Cc ap as exp\ne.g. experimental"
    cc_ap_ai: NotRequired[str]
    "Cc ap ai\ne.g. acetylalanine"
    cc_ap_ai_exp: NotRequired[str]
    "Cc ap ai exp\ne.g. acetylalanine"
    cc_ap_rf: NotRequired[str]
    "Cc ap rf\ne.g. translation"
    cc_ap_rf_exp: NotRequired[str]
    "Cc ap rf exp\ne.g. translation"
    cc_sequence_caution: NotRequired[str]
    "Cc sequence caution\ne.g. translated"
    cc_sequence_caution_exp: NotRequired[str]
    "Cc sequence caution exp\ne.g. translated"
    cc_sc_framesh: NotRequired[str]
    "Frameshift\ne.g. *"
    cc_sc_einit: NotRequired[str]
    "Erroneous initiation\ne.g. extended"
    cc_sc_eterm: NotRequired[str]
    "Erroneous termination\ne.g. translated"
    cc_sc_epred: NotRequired[str]
    "Erroneous gene model prediction\ne.g. *"
    cc_sc_etran: NotRequired[str]
    "Erroneous translation\ne.g. choice"
    cc_sc_misc: NotRequired[str]
    "Cc sc misc\ne.g. sequence"
    cc_sc_misc_exp: NotRequired[str]
    "Cc sc misc exp\ne.g. sequence"
    cc_mass_spectrometry: NotRequired[str]
    "Cc mass spectrometry\ne.g. electrospray"
    cc_mass_spectrometry_exp: NotRequired[str]
    "Cc mass spectrometry exp\ne.g. electrospray"
    cc_polymorphism: NotRequired[str]
    "Cc polymorphism\ne.g. transcript"
    cc_polymorphism_exp: NotRequired[str]
    "Cc polymorphism exp\ne.g. transcript"
    cc_rna_editing: NotRequired[str]
    "Cc rna editing\ne.g. target"
    cc_rna_editing_exp: NotRequired[str]
    "Cc rna editing exp\ne.g. target"
    ft_variants: NotRequired[str]
    "Ft variants\ne.g. colorectal"
    ft_variants_exp: NotRequired[str]
    "Ft variants exp\ne.g. colorectal"
    ft_variant: NotRequired[str]
    "Ft variant\ne.g. colorectal"
    ft_variant_exp: NotRequired[str]
    "Ft variant exp\ne.g. colorectal"
    ft_var_seq: NotRequired[str]
    "Ft var seq\ne.g. isoform"
    ft_var_seq_exp: NotRequired[str]
    "Ft var seq exp\ne.g. isoform"
    ft_non_std: NotRequired[str]
    "Ft non std\ne.g. selenocysteine"
    ft_non_std_exp: NotRequired[str]
    "Ft non std exp\ne.g. selenocysteine"
    ft_non_ter: NotRequired[str]
    "Ft non ter\ne.g. *"
    ft_non_ter_exp: NotRequired[str]
    "Ft non ter exp\ne.g. *"
    ft_non_cons: NotRequired[str]
    "Ft non cons\ne.g. *"
    ft_non_cons_exp: NotRequired[str]
    "Ft non cons exp\ne.g. *"
    ft_conflict: NotRequired[str]
    "Ft conflict\ne.g. *"
    ft_conflict_exp: NotRequired[str]
    "Ft conflict exp\ne.g. *"
    ft_unsure: NotRequired[str]
    "Ft unsure\ne.g. *"
    ft_unsure_exp: NotRequired[str]
    "Ft unsure exp\ne.g. *"
    ft_positional: NotRequired[str]
    "Ft positional\ne.g. colorectal"
    ft_positional_exp: NotRequired[str]
    "Ft positional exp\ne.g. colorectal"
    fragment: NotRequired[bool]
    "Fragment\ne.g. true"
    organelle: NotRequired[Organelle]
    "Encoded in\ne.g. mitochondrion\n* mitochondrion: Mitochondrion\n* plasmid: Plasmid\n* plastid: Plastid\n* chloroplast: Chloroplast\n* cyanelle: Cyanelle\n* apicoplast: Apicoplast\n* organellar chromatophore: Organellar chromatophore\n* non-photosynthetic plastid: Non-photosynthetic plastid\n* nucleomorph: Nucleomorph\n* hydrogenosome: Hydrogenosome"
    precursor: NotRequired[bool]
    "Precursor\ne.g. true"
    tissue: NotRequired[str]
    "Tissue\ne.g. head"
    strain: NotRequired[str]
    "Strain\ne.g. berkeley"
    plasmid: NotRequired[str]
    "Plasmid\ne.g. pO113"
    transposon: NotRequired[str]
    "Transposon\ne.g. tn3"
    ft_domain: NotRequired[str]
    "Ft domain\ne.g. phosphatase"
    ft_domain_exp: NotRequired[str]
    "Ft domain exp\ne.g. phosphatase"
    cc_domain: NotRequired[str]
    "Cc domain\ne.g. conformation"
    cc_domain_exp: NotRequired[str]
    "Cc domain exp\ne.g. conformation"
    family: NotRequired[str]
    "Protein family\ne.g. pa28"
    ft_coiled: NotRequired[str]
    "Ft coiled\ne.g. *"
    ft_coiled_exp: NotRequired[str]
    "Ft coiled exp\ne.g. *"
    ft_compbias: NotRequired[str]
    "Ft compbias\ne.g. basic residues"
    ft_compbias_exp: NotRequired[str]
    "Ft compbias exp\ne.g. basic residues"
    ft_motif: NotRequired[str]
    "Ft motif\ne.g. motif"
    ft_motif_exp: NotRequired[str]
    "Ft motif exp\ne.g. motif"
    ft_region: NotRequired[str]
    "Ft region\ne.g. motif"
    ft_region_exp: NotRequired[str]
    "Ft region exp\ne.g. motif"
    ft_repeat: NotRequired[str]
    "Ft repeat\ne.g. motif"
    ft_repeat_exp: NotRequired[str]
    "Ft repeat exp\ne.g. motif"
    cc_similarity: NotRequired[str]
    "Cc similarity\ne.g. phosphatase"
    cc_similarity_exp: NotRequired[str]
    "Cc similarity exp\ne.g. phosphatase"
    ft_zn_fing: NotRequired[str]
    "Ft zn fing\ne.g. UBP"
    ft_zn_fing_exp: NotRequired[str]
    "Ft zn fing exp\ne.g. UBP"
    xref: NotRequired[str]
    "Any cross-reference"
    database: NotRequired[str]
    "Database\ne.g. Bgee"
    cc_webresource: NotRequired[str]
    "Cc webresource\ne.g. lck"
    cc_webresource_exp: NotRequired[str]
    "Cc webresource exp\ne.g. lck"
    date_created: NotRequired[
        tuple[
            Union[
                date,
                Literal["*",],
            ],
            Union[
                date,
                Literal["*",],
            ],
        ]
    ]
    "Date Of Creation\ne.g. [2018-03-04 TO 2018-03-08]"
    date_modified: NotRequired[
        tuple[
            Union[
                date,
                Literal["*",],
            ],
            Union[
                date,
                Literal["*",],
            ],
        ]
    ]
    "Date of last entry modification\ne.g. [2018-03-04 TO 2018-03-08]"
    date_sequence_modified: NotRequired[
        tuple[
            Union[
                date,
                Literal["*",],
            ],
            Union[
                date,
                Literal["*",],
            ],
        ]
    ]
    "Date of last sequence modification\ne.g. [2018-03-04 TO 2018-03-08]"
    go: NotRequired[str]
    "Go\ne.g. 0009986"
    go_manual: NotRequired[str]
    "go, any manual assertion"
    go_automatic: NotRequired[str]
    "go, any automatic assertion"
    go_exp: NotRequired[str]
    "go, inferred from experiment [exp]"
    go_iba: NotRequired[str]
    "go, inferred from biological aspect of ancestor [iba]"
    go_ic: NotRequired[str]
    "go, inferred by curator [ic]"
    go_ida: NotRequired[str]
    "go, inferred from direct assay [ida]"
    go_iep: NotRequired[str]
    "go, inferred from expression pattern [iep]"
    go_igc: NotRequired[str]
    "go, inferred from genomic context [igc]"
    go_igi: NotRequired[str]
    "go, inferred from genetic interaction [igi]"
    go_imp: NotRequired[str]
    "go, inferred from mutant phenotype [imp]"
    go_ipi: NotRequired[str]
    "go, inferred from physical interaction [ipi]"
    go_isa: NotRequired[str]
    "go, inferred from sequence alignment [isa]"
    go_ism: NotRequired[str]
    "go, inferred from sequence mode [ism]"
    go_iso: NotRequired[str]
    "go, inferred from sequence orthology [iso]"
    go_iss: NotRequired[str]
    "go, inferred from sequence or structural similarity [iss]"
    go_nas: NotRequired[str]
    "go, non-traceable author statement [nas]"
    go_tas: NotRequired[str]
    "go, traceable author statement [tas]"
    go_hda: NotRequired[str]
    "go, inferred from high throughput direct assay [hda]"
    go_hmp: NotRequired[str]
    "go, inferred from high throughput mutant phenotype [hmp]"
    go_hgi: NotRequired[str]
    "go, inferred from high throughput genetic interaction [hgi]"
    go_hep: NotRequired[str]
    "go, interred from high throughput expression pattern [hep]"
    go_htp: NotRequired[str]
    "go, inferred from high throughput experiment [htp]"
    go_iea: NotRequired[str]
    "go, inferred from electronic annotation [iea]"
    chebi: NotRequired[str]
    "CHEBI ID\ne.g. 29105"
    inchikey: NotRequired[str]
    "InChIKey\ne.g. XLYOFNOQVPJJNP-UHFFFAOYSA-N"
    keyword: NotRequired[str]
    "Keyword [KW]\ne.g. chromosomal"
    lit_author: NotRequired[str]
    "Author\ne.g. smith"
    lit_journal: NotRequired[str]
    "Journal\ne.g. nature"
    lit_pubdate: NotRequired[
        tuple[
            Union[
                date,
                Literal["*",],
            ],
            Union[
                date,
                Literal["*",],
            ],
        ]
    ]
    "Published\ne.g. [2009-01-01 TO 2019-12-31]"
    lit_pubmed: NotRequired[str]
    "PubMed ID\ne.g. 15165820"
    lit_title: NotRequired[str]
    "Title\ne.g. protein"
    lit_citation_id: NotRequired[str]
    "Citation ID\ne.g. CI-6EPRJ6MFFS5LC"
    computational_pubmed_id: NotRequired[str]
    "Computational PubMed ID\ne.g. 15165820"
    community_pubmed_id: NotRequired[str]
    "Community PubMed ID\ne.g. 15165820"
    proteome: NotRequired[str]
    "Proteome ID\ne.g. UP000005640"
    proteomecomponent: NotRequired[str]
    "Proteome Component\ne.g. chromosome"
    scope: NotRequired[str]
    "Cited for\ne.g. microtubule"
    reviewed: NotRequired[bool]
    "Reviewed\ne.g. true"
    active: NotRequired[bool]
    "Active\ne.g. true"
    uniref_cluster_50: NotRequired[str]
    "UniRef50\ne.g. UniRef50_P05067"
    uniref_cluster_90: NotRequired[str]
    "UniRef90\ne.g. UniRef90_P05067"
    uniref_cluster_100: NotRequired[str]
    "UniRef100\ne.g. UniRef100_P05067"
    uniparc: NotRequired[str]
    "UniParc ID\ne.g. UPI000002DB1C"


UniprotkbQuery: TypeAlias = Union[UniprotkbQueryDict, str]
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
    "cc_catalytic_activity",
    "cc_cofactor",
    "ft_dna_bind",
    "ec",
    "cc_activity_regulation",
    "cc_function",
    "kinetics",
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
UniprotkbPublications: TypeAlias = Literal["lit_pubmed_id", "lit_doi_id"]
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
    "cc_similarity",
    "ft_zn_fing",
]
UniprotkbSequence: TypeAlias = Literal[
    "xref_ccds", "xref_embl", "xref_generif", "xref_pir", "xref_refseq"
]
UniprotkbThreedStructure: TypeAlias = Literal[
    "xref_alphafolddb",
    "xref_bmrb",
    "xref_emdb",
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
    "xref_glycosmos",
    "xref_glygen",
    "xref_metosite",
    "xref_phosphositeplus",
    "xref_swisspalm",
    "xref_unicarbkb",
    "xref_iptmnet",
]
UniprotkbPolymorphismAndMutation: TypeAlias = Literal[
    "xref_alzforum", "xref_biomuta", "xref_dmdm", "xref_dbsnp"
]
UniprotkbTwodGel: TypeAlias = Literal[
    "xref_compluyeast-2dpage", "xref_ogp", "xref_reproduction-2dpage"
]
UniprotkbProteomic: TypeAlias = Literal[
    "xref_cptac",
    "xref_massive",
    "xref_pride",
    "xref_paxdb",
    "xref_peptideatlas",
    "xref_promex",
    "xref_proteomicsdb",
    "xref_pumba",
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
]
UniprotkbOrganismSpecific: TypeAlias = Literal[
    "xref_agr",
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
    "xref_ic4r",
    "xref_japonicusdb",
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
    "xref_orcid",
    "xref_pgenn",
    "xref_phi-base",
    "xref_pro",
    "xref_pharos",
    "xref_pubtator",
    "xref_rnact",
    "xref_emind",
]
UniprotkbGeneExpression: TypeAlias = Literal[
    "xref_bgee", "xref_cleanex", "xref_collectf", "xref_expressionatlas"
]
UniprotkbFamilyAndDomain: TypeAlias = Literal[
    "xref_cdd",
    "xref_disprot",
    "xref_gene3d",
    "xref_hamap",
    "xref_ideal",
    "xref_interpro",
    "xref_ncbifam",
    "xref_panther",
    "xref_pirsf",
    "xref_prints",
    "xref_prosite",
    "xref_pfam",
    "xref_sfld",
    "xref_smart",
    "xref_supfam",
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
