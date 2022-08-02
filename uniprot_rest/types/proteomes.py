from __future__ import annotations
from typing import Union, Iterable
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest.base

ProteomeType: TypeAlias = Literal["1", "2", "3", "4"]
Cpd: TypeAlias = Literal["1", "2", "3", "4", "5", "6"]


class ProteomesQuery(TypedDict("ProteomesQuery", {})):
    and_: NotRequired[Iterable["ProteomesQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["ProteomesQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["ProteomesQuery"]]
    "Negate a filter"
    upid: NotRequired[str]
    "Proteome ID"
    proteome_type: NotRequired[ProteomeType]
    "Proteome Type\n1: Reference\n2: Other\n3: Redundant\n4: Excluded"
    organism_name: NotRequired[str]
    "Organism [OS]"
    taxonomy_name: NotRequired[str]
    "Taxonomy [OC]"
    genome_accession: NotRequired[str]
    "Genome Accession"
    genome_assembly: NotRequired[str]
    "Genome Assembly"
    cpd: NotRequired[Cpd]
    "CPD (Complete Proteome Detector)\n1: Standard\n2: Close to standard (high value)\n3: Close to standard (low value)\n4: Outlier (high value)\n5: Outlier (low value)\n6: Unknown"
    busco: NotRequired[
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
    "BUSCO (Complete %)"


ProteomesNamesTaxonomy: TypeAlias = Literal[
    "upid", "organism", "organism_id", "components", "mnemonic", "lineage"
]
ProteomesMiscellaneous: TypeAlias = Literal[
    "busco", "cpd", "genome_assembly", "genome_representation", "protein_count"
]
ProteomesFields: TypeAlias = Literal[ProteomesNamesTaxonomy, ProteomesMiscellaneous]


@dataclass
class ProteomesSearch(uniprot_rest.base.Search):
    dataset: Literal["proteomes"] = field(default="proteomes", init=False)
    query: ProteomesQuery
    "A query that filters the returned proteins"
    fields: Iterable[ProteomesFields]
    "Fields to return in the result object"
