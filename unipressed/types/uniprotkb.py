from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base

Existence: TypeAlias = Literal["1", "2", "3", "4", "5"]
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


class UniprotkbQuery(TypedDict):
    and_: NotRequired[Iterable["UniprotkbQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UniprotkbQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UniprotkbQuery"]]
    "Negate a filter"
    accession: NotRequired[str]
    "UniProtKB AC"
    id: NotRequired[str]
    "Entry Name [ID]"
    protein_name: NotRequired[str]
    "Protein Name [DE]"
    gene: NotRequired[str]
    "Gene Name [GN]"
    organism_name: NotRequired[str]
    "Organism [OS]"
    taxonomy_name: NotRequired[str]
    "Taxonomy [OC]"
    virus_host_name: NotRequired[str]
    "Virus host"
    existence: NotRequired[Existence]
    "Protein Existence [PE]\n1: Evidence at protein level\n2: Evidence at transcript level\n3: Inferred from homology\n4: Predicted\n5: Uncertain"
    ec: NotRequired[str]
    "Enzyme classification [EC]"
    cc_cofactor_chebi: NotRequired[str]
    ccev_cofactor_chebi: NotRequired[str]
    cc_cofactor_note: NotRequired[str]
    ccev_cofactor_note: NotRequired[str]
    cc_bpcp: NotRequired[str]
    ccev_bpcp: NotRequired[str]
    cc_bpcp_absorption: NotRequired[str]
    ccev_bpcp_absorption: NotRequired[str]
    cc_bpcp_kinetics: NotRequired[str]
    ccev_bpcp_kinetics: NotRequired[str]
    cc_bpcp_ph_dependence: NotRequired[str]
    ccev_bpcp_ph_dependence: NotRequired[str]
    cc_bpcp_redox_potential: NotRequired[str]
    ccev_bpcp_redox_potential: NotRequired[str]
    cc_bpcp_temp_dependence: NotRequired[str]
    ccev_bpcp_temp_dependence: NotRequired[str]
    cc_catalytic_activity: NotRequired[str]
    ccev_catalytic_activity: NotRequired[str]
    cc_activity_regulation: NotRequired[str]
    ccev_activity_regulation: NotRequired[str]
    cc_function: NotRequired[str]
    ccev_function: NotRequired[str]
    cc_caution: NotRequired[str]
    ccev_caution: NotRequired[str]
    ft_sites: NotRequired[str]
    ftlen_sites: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_sites: NotRequired[str]
    ft_act_site: NotRequired[str]
    ftlen_act_site: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_act_site: NotRequired[str]
    ft_metal: NotRequired[str]
    ftlen_metal: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_metal: NotRequired[str]
    ft_binding: NotRequired[str]
    ftlen_binding: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_binding: NotRequired[str]
    ft_site: NotRequired[str]
    ftlen_site: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_site: NotRequired[str]
    ft_ca_bind: NotRequired[str]
    ftlen_ca_bind: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_ca_bind: NotRequired[str]
    ft_dna_bind: NotRequired[str]
    ftlen_dna_bind: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_dna_bind: NotRequired[str]
    ft_np_bind: NotRequired[str]
    ftlen_np_bind: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_np_bind: NotRequired[str]
    cc_pathway: NotRequired[str]
    ccev_pathway: NotRequired[str]
    cc_miscellaneous: NotRequired[str]
    ccev_miscellaneous: NotRequired[str]
    cc_scl_term: NotRequired[str]
    ccev_scl_term: NotRequired[str]
    cc_scl_note: NotRequired[str]
    ccev_scl_note: NotRequired[str]
    ft_transmem: NotRequired[str]
    ftlen_transmem: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_transmem: NotRequired[str]
    ft_topo_dom: NotRequired[str]
    ftlen_topo_dom: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_topo_dom: NotRequired[str]
    ft_intramem: NotRequired[str]
    ftlen_intramem: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_intramem: NotRequired[str]
    cc_disease: NotRequired[str]
    ccev_disease: NotRequired[str]
    cc_allergen: NotRequired[str]
    ccev_allergen: NotRequired[str]
    cc_toxic_dose: NotRequired[str]
    ccev_toxic_dose: NotRequired[str]
    cc_biotechnology: NotRequired[str]
    ccev_biotechnology: NotRequired[str]
    cc_pharmaceutical: NotRequired[str]
    ccev_pharmaceutical: NotRequired[str]
    cc_disruption_phenotype: NotRequired[str]
    ccev_disruption_phenotype: NotRequired[str]
    ft_mutagen: NotRequired[str]
    ftlen_mutagen: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_mutagen: NotRequired[str]
    cc_ptm: NotRequired[str]
    ccev_ptm: NotRequired[str]
    ft_mod_res: NotRequired[str]
    ftlen_mod_res: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_mod_res: NotRequired[str]
    ft_lipid: NotRequired[str]
    ftlen_lipid: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_lipid: NotRequired[str]
    ft_carbohyd: NotRequired[str]
    ftlen_carbohyd: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_carbohyd: NotRequired[str]
    ft_disulfid: NotRequired[str]
    ftlen_disulfid: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_disulfid: NotRequired[str]
    ft_crosslnk: NotRequired[str]
    ftlen_crosslnk: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_crosslnk: NotRequired[str]
    ft_molecule_processing: NotRequired[str]
    ftlen_molecule_processing: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_molecule_processing: NotRequired[str]
    ft_chain: NotRequired[str]
    ftlen_chain: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_chain: NotRequired[str]
    ft_init_met: NotRequired[str]
    ftlen_init_met: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_init_met: NotRequired[str]
    ft_peptide: NotRequired[str]
    ftlen_peptide: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_peptide: NotRequired[str]
    ft_signal: NotRequired[str]
    ftlen_signal: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_signal: NotRequired[str]
    ft_propep: NotRequired[str]
    ftlen_propep: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_propep: NotRequired[str]
    ft_transit: NotRequired[str]
    ftlen_transit: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_transit: NotRequired[str]
    cc_developmental_stage: NotRequired[str]
    ccev_developmental_stage: NotRequired[str]
    cc_induction: NotRequired[str]
    ccev_induction: NotRequired[str]
    cc_tissue_specificity: NotRequired[str]
    ccev_tissue_specificity: NotRequired[str]
    interactor: NotRequired[str]
    "Binary Interaction"
    cc_subunit: NotRequired[str]
    ccev_subunit: NotRequired[str]
    structure_3d: NotRequired[bool]
    "3D Structure"
    ft_secstruct: NotRequired[str]
    ftlen_secstruct: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_secstruct: NotRequired[str]
    ft_helix: NotRequired[str]
    ftlen_helix: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_helix: NotRequired[str]
    ft_turn: NotRequired[str]
    ftlen_turn: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_turn: NotRequired[str]
    ft_strand: NotRequired[str]
    ftlen_strand: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_strand: NotRequired[str]
    mass: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    "Mass(Da)"
    length: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    "Sequence length"
    cc_ap: NotRequired[str]
    ccev_ap: NotRequired[str]
    cc_ap_apu: NotRequired[str]
    ccev_ap_apu: NotRequired[str]
    cc_ap_as: NotRequired[str]
    ccev_ap_as: NotRequired[str]
    cc_ap_ai: NotRequired[str]
    ccev_ap_ai: NotRequired[str]
    cc_ap_rf: NotRequired[str]
    ccev_ap_rf: NotRequired[str]
    cc_sequence_caution: NotRequired[str]
    ccev_sequence_caution: NotRequired[str]
    cc_sc_framesh: NotRequired[str]
    "Frameshift"
    cc_sc_einit: NotRequired[str]
    "Erroneous initiation"
    cc_sc_eterm: NotRequired[str]
    "Erroneous termination"
    cc_sc_epred: NotRequired[str]
    "Erroneous gene model prediction"
    cc_sc_etran: NotRequired[str]
    "Erroneous translation"
    cc_sc_misc: NotRequired[str]
    ccev_sc_misc: NotRequired[str]
    cc_mass_spectrometry: NotRequired[str]
    ccev_mass_spectrometry: NotRequired[str]
    cc_polymorphism: NotRequired[str]
    ccev_polymorphism: NotRequired[str]
    cc_rna_editing: NotRequired[str]
    ccev_rna_editing: NotRequired[str]
    ft_variants: NotRequired[str]
    ftlen_variants: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_variants: NotRequired[str]
    ft_variant: NotRequired[str]
    ftlen_variant: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_variant: NotRequired[str]
    ft_var_seq: NotRequired[str]
    ftlen_var_seq: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_var_seq: NotRequired[str]
    ft_non_std: NotRequired[str]
    ftlen_non_std: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_non_std: NotRequired[str]
    ft_non_ter: NotRequired[str]
    ftlen_non_ter: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_non_ter: NotRequired[str]
    ft_non_cons: NotRequired[str]
    ftlen_non_cons: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_non_cons: NotRequired[str]
    ft_conflict: NotRequired[str]
    ftlen_conflict: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_conflict: NotRequired[str]
    ft_unsure: NotRequired[str]
    ftlen_unsure: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_unsure: NotRequired[str]
    ft_positional: NotRequired[str]
    ftlen_positional: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_positional: NotRequired[str]
    fragment: NotRequired[bool]
    "Fragment"
    organelle: NotRequired[Organelle]
    "Encoded in\nmitochondrion: Mitochondrion\nplastid: Plastid\nchloroplast: Chloroplast\ncyanelle: Cyanelle\napicoplast: Apicoplast\norganellar chromatophore: Organellar chromatophore\nnon-photosynthetic plastid: Non-photosynthetic plastid\nnucleomorph: Nucleomorph\nhydrogenosome: Hydrogenosome"
    precursor: NotRequired[bool]
    "Precursor"
    tissue: NotRequired[str]
    "Tissue"
    strain: NotRequired[str]
    "Strain"
    plasmid: NotRequired[str]
    "Plasmid"
    transposon: NotRequired[str]
    "Transposon"
    ft_domain: NotRequired[str]
    ftlen_domain: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_domain: NotRequired[str]
    cc_domain: NotRequired[str]
    ccev_domain: NotRequired[str]
    family: NotRequired[str]
    "Protein family"
    ft_coiled: NotRequired[str]
    ftlen_coiled: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_coiled: NotRequired[str]
    ft_compbias: NotRequired[str]
    ftlen_compbias: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_compbias: NotRequired[str]
    ft_motif: NotRequired[str]
    ftlen_motif: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_motif: NotRequired[str]
    ft_region: NotRequired[str]
    ftlen_region: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_region: NotRequired[str]
    ft_repeat: NotRequired[str]
    ftlen_repeat: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_repeat: NotRequired[str]
    cc_similarity: NotRequired[str]
    ccev_similarity: NotRequired[str]
    ft_zn_fing: NotRequired[str]
    ftlen_zn_fing: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    ftev_zn_fing: NotRequired[str]
    xref: NotRequired[str]
    "Any cross-reference"
    database: NotRequired[str]
    cc_webresource: NotRequired[str]
    ccev_webresource: NotRequired[str]
    date_created: NotRequired[
        tuple[
            Union[
                date,
                Literal[
                    "*",
                ],
            ],
            Union[
                date,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    "Date Of Creation"
    date_modified: NotRequired[
        tuple[
            Union[
                date,
                Literal[
                    "*",
                ],
            ],
            Union[
                date,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    "Date of last entry modification"
    date_sequence_modified: NotRequired[
        tuple[
            Union[
                date,
                Literal[
                    "*",
                ],
            ],
            Union[
                date,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    "Date of last sequence modification"
    go: NotRequired[str]
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
    "CHEBI ID"
    inchikey: NotRequired[str]
    "InChIKey"
    keyword: NotRequired[str]
    "Keyword [KW]"
    lit_author: NotRequired[str]
    "Author"
    lit_journal: NotRequired[str]
    "Journal"
    lit_pubdate: NotRequired[
        tuple[
            Union[
                date,
                Literal[
                    "*",
                ],
            ],
            Union[
                date,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    "Published"
    lit_pubmed: NotRequired[str]
    "PubMed ID"
    lit_title: NotRequired[str]
    "Title"
    lit_citation_id: NotRequired[str]
    "Citation ID"
    computational_pubmed_id: NotRequired[str]
    "Computational PubMed ID"
    community_pubmed_id: NotRequired[str]
    "Community PubMed ID"
    proteome: NotRequired[str]
    "Proteome ID"
    proteomecomponent: NotRequired[str]
    "Proteome Component"
    scope: NotRequired[str]
    "Cited for"
    reviewed: NotRequired[bool]
    "Reviewed"
    active: NotRequired[bool]
    "Active"
    uniref_cluster_50: NotRequired[str]
    "UniRef50"
    uniref_cluster_90: NotRequired[str]
    "UniRef90"
    uniref_cluster_100: NotRequired[str]
    "UniRef100"
    uniparc: NotRequired[str]
    "UniParc ID"


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
class UniprotkbSearch(unipressed.base.Search):
    """Client for querying the [uniprotkb Uniprot dataset](https://www.uniprot.org/help/uniprotkb)"""

    dataset: Literal["uniprotkb"] = field(default="uniprotkb", init=False)
    query: UniprotkbQuery
    "A query that filters the returned proteins"
    fields: Iterable[UniprotkbFields]
    "Fields to return in the result object"
