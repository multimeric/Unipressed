from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

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
    ccev_cofactor_chebi: NotRequired[str]
    "Ccev cofactor chebi\ne.g. manual"
    cc_cofactor_note: NotRequired[str]
    "Cc cofactor note\ne.g. subunit"
    ccev_cofactor_note: NotRequired[str]
    "Ccev cofactor note\ne.g. ECO_0000269"
    cc_bpcp: NotRequired[str]
    'Cc bpcp\ne.g. "some value"'
    ccev_bpcp: NotRequired[str]
    "Ccev bpcp\ne.g. automatic"
    cc_bpcp_absorption: NotRequired[str]
    "Cc bpcp absorption\ne.g. prosthetic"
    ccev_bpcp_absorption: NotRequired[str]
    "Ccev bpcp absorption\ne.g. ECO_0000213"
    cc_bpcp_kinetics: NotRequired[str]
    "Cc bpcp kinetics\ne.g. aspartate"
    ccev_bpcp_kinetics: NotRequired[str]
    "Ccev bpcp kinetics\ne.g. experimental"
    cc_bpcp_ph_dependence: NotRequired[str]
    "Cc bpcp ph dependence\ne.g. optimum"
    ccev_bpcp_ph_dependence: NotRequired[str]
    "Ccev bpcp ph dependence\ne.g. ECO_0000305"
    cc_bpcp_redox_potential: NotRequired[str]
    "Cc bpcp redox potential\ne.g. siroheme"
    ccev_bpcp_redox_potential: NotRequired[str]
    "Ccev bpcp redox potential\ne.g. manual"
    cc_bpcp_temp_dependence: NotRequired[str]
    "Cc bpcp temp dependence\ne.g. *"
    ccev_bpcp_temp_dependence: NotRequired[str]
    "Ccev bpcp temp dependence\ne.g. manual"
    cc_catalytic_activity: NotRequired[str]
    "Cc catalytic activity\ne.g. tyrosine"
    ccev_catalytic_activity: NotRequired[str]
    "Ccev catalytic activity\ne.g. manual"
    cc_activity_regulation: NotRequired[str]
    "Cc activity regulation\ne.g. inhibited"
    ccev_activity_regulation: NotRequired[str]
    "Ccev activity regulation\ne.g. manual"
    cc_function: NotRequired[str]
    "Cc function\ne.g. enzyme"
    ccev_function: NotRequired[str]
    "Ccev function\ne.g. experimental"
    cc_caution: NotRequired[str]
    "Cc caution\ne.g. kinase"
    ccev_caution: NotRequired[str]
    "Ccev caution\ne.g. manual"
    ft_sites: NotRequired[str]
    "Ft sites\ne.g. translocation"
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
    "Ftlen sites\ne.g. [0 TO 100]"
    ftev_sites: NotRequired[str]
    "Ftev sites\ne.g. manual"
    ft_act_site: NotRequired[str]
    "Ft act site\ne.g. phosphocysteine"
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
    "Ftlen act site\ne.g. [0 TO 100]"
    ftev_act_site: NotRequired[str]
    "Ftev act site\ne.g. manual"
    ft_binding: NotRequired[str]
    "Ft binding\ne.g. phosphocysteine"
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
    "Ftlen binding\ne.g. [0 TO 100]"
    ftev_binding: NotRequired[str]
    "Ftev binding\ne.g. any"
    ft_site: NotRequired[str]
    "Ft site\ne.g. phosphocysteine"
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
    "Ftlen site\ne.g. [0 TO 100]"
    ftev_site: NotRequired[str]
    "Ftev site\ne.g. any"
    ft_dna_bind: NotRequired[str]
    "Ft dna bind\ne.g. *"
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
    "Ftlen dna bind\ne.g. [0 TO 100]"
    ftev_dna_bind: NotRequired[str]
    "Ftev dna bind\ne.g. any"
    cc_pathway: NotRequired[str]
    "Cc pathway\ne.g. metabolism"
    ccev_pathway: NotRequired[str]
    "Ccev pathway\ne.g. any"
    cc_miscellaneous: NotRequired[str]
    "Cc miscellaneous\ne.g. abscisic"
    ccev_miscellaneous: NotRequired[str]
    "Ccev miscellaneous\ne.g. any"
    cc_scl_term: NotRequired[str]
    "Cc scl term\ne.g. membrane"
    ccev_scl_term: NotRequired[str]
    "Ccev scl term\ne.g. manual"
    cc_scl_note: NotRequired[str]
    "Cc scl note\ne.g. membrane"
    ccev_scl_note: NotRequired[str]
    "Ccev scl note\ne.g. manual"
    ft_transmem: NotRequired[str]
    "Ft transmem\ne.g. forming"
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
    "Ftlen transmem\ne.g. [0 TO 100]"
    ftev_transmem: NotRequired[str]
    "Ftev transmem\ne.g. manual"
    ft_topo_dom: NotRequired[str]
    "Ft topo dom\ne.g. forming"
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
    "Ftlen topo dom\ne.g. [0 TO 100]"
    ftev_topo_dom: NotRequired[str]
    "Ftev topo dom\ne.g. manual"
    ft_intramem: NotRequired[str]
    "Ft intramem\ne.g. forming"
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
    "Ftlen intramem\ne.g. [0 TO 100]"
    ftev_intramem: NotRequired[str]
    "Ftev intramem\ne.g. manual"
    cc_disease: NotRequired[str]
    "Cc disease\ne.g. nephrotic"
    ccev_disease: NotRequired[str]
    "Ccev disease\ne.g. manual"
    cc_allergen: NotRequired[str]
    "Cc allergen\ne.g. allergic"
    ccev_allergen: NotRequired[str]
    "Ccev allergen\ne.g. manual"
    cc_toxic_dose: NotRequired[str]
    "Cc toxic dose\ne.g. intracistenal"
    ccev_toxic_dose: NotRequired[str]
    "Ccev toxic dose\ne.g. manual"
    cc_biotechnology: NotRequired[str]
    "Cc biotechnology\ne.g. vaccine"
    ccev_biotechnology: NotRequired[str]
    "Ccev biotechnology\ne.g. manual"
    cc_pharmaceutical: NotRequired[str]
    "Cc pharmaceutical\ne.g. peptide"
    ccev_pharmaceutical: NotRequired[str]
    "Ccev pharmaceutical\ne.g. manual"
    cc_disruption_phenotype: NotRequired[str]
    "Cc disruption phenotype\ne.g. infected"
    ccev_disruption_phenotype: NotRequired[str]
    "Ccev disruption phenotype\ne.g. any"
    ft_mutagen: NotRequired[str]
    "Ft mutagen\ne.g. phosphatase"
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
    "Ftlen mutagen\ne.g. [0 TO 100]"
    ftev_mutagen: NotRequired[str]
    "Ftev mutagen\ne.g. manual"
    cc_ptm: NotRequired[str]
    "Cc ptm\ne.g. mitosis"
    ccev_ptm: NotRequired[str]
    "Ccev ptm\ne.g. any"
    ft_mod_res: NotRequired[str]
    "Ft mod res\ne.g. phosphoserine"
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
    "Ftlen mod res\ne.g. [0 TO 100]"
    ftev_mod_res: NotRequired[str]
    "Ftev mod res\ne.g. manual"
    ft_lipid: NotRequired[str]
    "Ft lipid\ne.g. cysteine"
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
    "Ftlen lipid\ne.g. [0 TO 100]"
    ftev_lipid: NotRequired[str]
    "Ftev lipid\ne.g. manual"
    ft_carbohyd: NotRequired[str]
    "Ft carbohyd\ne.g. cysteine"
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
    "Ftlen carbohyd\ne.g. [0 TO 100]"
    ftev_carbohyd: NotRequired[str]
    "Ftev carbohyd\ne.g. manual"
    ft_disulfid: NotRequired[str]
    "Ft disulfid\ne.g. reversible"
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
    "Ftlen disulfid\ne.g. [0 TO 100]"
    ftev_disulfid: NotRequired[str]
    "Ftev disulfid\ne.g. manual"
    ft_crosslnk: NotRequired[str]
    "Ft crosslnk\ne.g. lysine"
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
    "Ftlen crosslnk\ne.g. [0 TO 100]"
    ftev_crosslnk: NotRequired[str]
    "Ftev crosslnk\ne.g. manual"
    ft_molecule_processing: NotRequired[str]
    "Ft molecule processing\ne.g. disulfide"
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
    "Ftlen molecule processing\ne.g. [0 TO 100]"
    ftev_molecule_processing: NotRequired[str]
    "Ftev molecule processing\ne.g. manual"
    ft_chain: NotRequired[str]
    "Ft chain\ne.g. kinase"
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
    "Ftlen chain\ne.g. [0 TO 100]"
    ftev_chain: NotRequired[str]
    "Ftev chain\ne.g. manual"
    ft_init_met: NotRequired[str]
    "Ft init met\ne.g. Removed"
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
    "Ftlen init met\ne.g. [0 TO 100]"
    ftev_init_met: NotRequired[str]
    "Ftev init met\ne.g. manual"
    ft_peptide: NotRequired[str]
    "Ft peptide\ne.g. Removed"
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
    "Ftlen peptide\ne.g. [0 TO 100]"
    ftev_peptide: NotRequired[str]
    "Ftev peptide\ne.g. any"
    ft_signal: NotRequired[str]
    "Ft signal\ne.g. cleaved"
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
    "Ftlen signal\ne.g. [0 TO 100]"
    ftev_signal: NotRequired[str]
    "Ftev signal\ne.g. manual"
    ft_propep: NotRequired[str]
    "Ft propep\ne.g. Activation peptide"
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
    "Ftlen propep\ne.g. [0 TO 100]"
    ftev_propep: NotRequired[str]
    "Ftev propep\ne.g. manual"
    ft_transit: NotRequired[str]
    "Ft transit\ne.g. Mitochondrion"
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
    "Ftlen transit\ne.g. [0 TO 100]"
    ftev_transit: NotRequired[str]
    "Ftev transit\ne.g. manual"
    cc_developmental_stage: NotRequired[str]
    "Cc developmental stage\ne.g. brain"
    ccev_developmental_stage: NotRequired[str]
    "Ccev developmental stage\ne.g. manual"
    cc_induction: NotRequired[str]
    "Cc induction\ne.g. calcium"
    ccev_induction: NotRequired[str]
    "Ccev induction\ne.g. manual"
    cc_tissue_specificity: NotRequired[str]
    "Cc tissue specificity\ne.g. pancreas"
    ccev_tissue_specificity: NotRequired[str]
    "Ccev tissue specificity\ne.g. manual"
    interactor: NotRequired[str]
    "Binary Interaction\ne.g. EBI-1042898"
    cc_subunit: NotRequired[str]
    "Cc subunit\ne.g. homodimer"
    ccev_subunit: NotRequired[str]
    "Ccev subunit\ne.g. manual"
    structure_3d: NotRequired[bool]
    "3D Structure\ne.g. true\n* true: Yes\n* false: No"
    ft_secstruct: NotRequired[str]
    "Ft secstruct\ne.g. *"
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
    "Ftlen secstruct\ne.g. [0 TO 100]"
    ftev_secstruct: NotRequired[str]
    "Ftev secstruct\ne.g. manual"
    ft_helix: NotRequired[str]
    "Ft helix\ne.g. *"
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
    "Ftlen helix\ne.g. [0 TO 100]"
    ftev_helix: NotRequired[str]
    "Ftev helix\ne.g. manual"
    ft_turn: NotRequired[str]
    "Ft turn\ne.g. *"
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
    "Ftlen turn\ne.g. [0 TO 100]"
    ftev_turn: NotRequired[str]
    "Ftev turn\ne.g. manual"
    ft_strand: NotRequired[str]
    "Ft strand\ne.g. *"
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
    "Ftlen strand\ne.g. [0 TO 100]"
    ftev_strand: NotRequired[str]
    "Ftev strand\ne.g. manual"
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
    "Mass(Da)\ne.g. [441126 TO 441126]"
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
    "Sequence length\ne.g. [441 TO 450]"
    cc_ap: NotRequired[str]
    "Cc ap\ne.g. tissues"
    ccev_ap: NotRequired[str]
    "Ccev ap\ne.g. manual"
    cc_ap_apu: NotRequired[str]
    "Cc ap apu\ne.g. *"
    ccev_ap_apu: NotRequired[str]
    "Ccev ap apu\ne.g. any"
    cc_ap_as: NotRequired[str]
    "Cc ap as\ne.g. experimental"
    ccev_ap_as: NotRequired[str]
    "Ccev ap as\ne.g. experimental"
    cc_ap_ai: NotRequired[str]
    "Cc ap ai\ne.g. acetylalanine"
    ccev_ap_ai: NotRequired[str]
    "Ccev ap ai\ne.g. any"
    cc_ap_rf: NotRequired[str]
    "Cc ap rf\ne.g. translation"
    ccev_ap_rf: NotRequired[str]
    "Ccev ap rf\ne.g. manual"
    cc_sequence_caution: NotRequired[str]
    "Cc sequence caution\ne.g. translated"
    ccev_sequence_caution: NotRequired[str]
    "Ccev sequence caution\ne.g. any"
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
    ccev_sc_misc: NotRequired[str]
    "Ccev sc misc\ne.g. any"
    cc_mass_spectrometry: NotRequired[str]
    "Cc mass spectrometry\ne.g. electrospray"
    ccev_mass_spectrometry: NotRequired[str]
    "Ccev mass spectrometry\ne.g. manual"
    cc_polymorphism: NotRequired[str]
    "Cc polymorphism\ne.g. transcript"
    ccev_polymorphism: NotRequired[str]
    "Ccev polymorphism\ne.g. manual"
    cc_rna_editing: NotRequired[str]
    "Cc rna editing\ne.g. target"
    ccev_rna_editing: NotRequired[str]
    "Ccev rna editing\ne.g. manual"
    ft_variants: NotRequired[str]
    "Ft variants\ne.g. colorectal"
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
    "Ftlen variants\ne.g. [0 TO 100]"
    ftev_variants: NotRequired[str]
    "Ftev variants\ne.g. manual"
    ft_variant: NotRequired[str]
    "Ft variant\ne.g. colorectal"
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
    "Ftlen variant\ne.g. [0 TO 100]"
    ftev_variant: NotRequired[str]
    "Ftev variant\ne.g. manual"
    ft_var_seq: NotRequired[str]
    "Ft var seq\ne.g. isoform"
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
    "Ftlen var seq\ne.g. [0 TO 100]"
    ftev_var_seq: NotRequired[str]
    "Ftev var seq\ne.g. manual"
    ft_non_std: NotRequired[str]
    "Ft non std\ne.g. selenocysteine"
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
    "Ftlen non std\ne.g. [0 TO 100]"
    ftev_non_std: NotRequired[str]
    "Ftev non std\ne.g. manual"
    ft_non_ter: NotRequired[str]
    "Ft non ter\ne.g. *"
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
    "Ftlen non ter\ne.g. [0 TO 100]"
    ftev_non_ter: NotRequired[str]
    "Ftev non ter\ne.g. manual"
    ft_non_cons: NotRequired[str]
    "Ft non cons\ne.g. *"
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
    "Ftlen non cons\ne.g. [0 TO 100]"
    ftev_non_cons: NotRequired[str]
    "Ftev non cons\ne.g. manual"
    ft_conflict: NotRequired[str]
    "Ft conflict\ne.g. *"
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
    "Ftlen conflict\ne.g. [0 TO 100]"
    ftev_conflict: NotRequired[str]
    "Ftev conflict\ne.g. manual"
    ft_unsure: NotRequired[str]
    "Ft unsure\ne.g. *"
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
    "Ftlen unsure\ne.g. [0 TO 100]"
    ftev_unsure: NotRequired[str]
    "Ftev unsure\ne.g. manual"
    ft_positional: NotRequired[str]
    "Ft positional\ne.g. colorectal"
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
    "Ftlen positional\ne.g. [0 TO 100]"
    ftev_positional: NotRequired[str]
    "Ftev positional\ne.g. manual"
    fragment: NotRequired[bool]
    "Fragment\ne.g. true\n* true: Yes\n* false: No"
    organelle: NotRequired[Organelle]
    "Encoded in\ne.g. mitochondrion\n* mitochondrion: Mitochondrion\n* plastid: Plastid\n* chloroplast: Chloroplast\n* cyanelle: Cyanelle\n* apicoplast: Apicoplast\n* organellar chromatophore: Organellar chromatophore\n* non-photosynthetic plastid: Non-photosynthetic plastid\n* nucleomorph: Nucleomorph\n* hydrogenosome: Hydrogenosome"
    precursor: NotRequired[bool]
    "Precursor\ne.g. true\n* true: Yes\n* false: No"
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
    "Ftlen domain\ne.g. [0 TO 100]"
    ftev_domain: NotRequired[str]
    "Ftev domain\ne.g. manual"
    cc_domain: NotRequired[str]
    "Cc domain\ne.g. conformation"
    ccev_domain: NotRequired[str]
    "Ccev domain\ne.g. any"
    family: NotRequired[str]
    "Protein family\ne.g. pa28"
    ft_coiled: NotRequired[str]
    "Ft coiled\ne.g. *"
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
    "Ftlen coiled\ne.g. [0 TO 100]"
    ftev_coiled: NotRequired[str]
    "Ftev coiled\ne.g. manual"
    ft_compbias: NotRequired[str]
    "Ft compbias\ne.g. glu-rich"
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
    "Ftlen compbias\ne.g. [0 TO 100]"
    ftev_compbias: NotRequired[str]
    "Ftev compbias\ne.g. manual"
    ft_motif: NotRequired[str]
    "Ft motif\ne.g. motif"
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
    "Ftlen motif\ne.g. [0 TO 100]"
    ftev_motif: NotRequired[str]
    "Ftev motif\ne.g. manual"
    ft_region: NotRequired[str]
    "Ft region\ne.g. motif"
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
    "Ftlen region\ne.g. [0 TO 100]"
    ftev_region: NotRequired[str]
    "Ftev region\ne.g. manual"
    ft_repeat: NotRequired[str]
    "Ft repeat\ne.g. motif"
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
    "Ftlen repeat\ne.g. [0 TO 100]"
    ftev_repeat: NotRequired[str]
    "Ftev repeat\ne.g. manual"
    cc_similarity: NotRequired[str]
    "Cc similarity\ne.g. phosphatase"
    ccev_similarity: NotRequired[str]
    "Ccev similarity\ne.g. manual"
    ft_zn_fing: NotRequired[str]
    "Ft zn fing\ne.g. UBP"
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
    "Ftlen zn fing\ne.g. [0 TO 100]"
    ftev_zn_fing: NotRequired[str]
    "Ftev zn fing\ne.g. manual"
    xref: NotRequired[str]
    "Any cross-reference"
    database: NotRequired[str]
    "Database\ne.g. Bgee"
    cc_webresource: NotRequired[str]
    "Cc webresource\ne.g. lck"
    ccev_webresource: NotRequired[str]
    "Ccev webresource\ne.g. manual"
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
    "Date Of Creation\ne.g. [2018-03-04 TO 2018-03-08]"
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
    "Date of last entry modification\ne.g. [2018-03-04 TO 2018-03-08]"
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
    "Reviewed\ne.g. true\n* true: Yes\n* false: No"
    active: NotRequired[bool]
    "Active\ne.g. true\n* true: Yes\n* false: No"
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
