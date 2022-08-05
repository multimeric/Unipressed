from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base

ProteomeType: TypeAlias = Literal["1", "2", "3", "4"]
Cpd: TypeAlias = Literal["1", "2", "3", "4", "5", "6"]


class ProteomesQuery(TypedDict):
    and_: NotRequired[Iterable["ProteomesQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["ProteomesQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["ProteomesQuery"]]
    "Negate a filter"
    upid: NotRequired[str]
    "Proteome ID\ne.g. UP000000718"
    proteome_type: NotRequired[ProteomeType]
    "Proteome Type\n1: Reference\n2: Other\n3: Redundant\n4: Excluded\ne.g. 1"
    organism_name: NotRequired[str]
    "Organism [OS]\ne.g. Human"
    organism_id: NotRequired[str]
    "Organism id"
    taxonomy_name: NotRequired[str]
    "Taxonomy [OC]\ne.g. Human"
    taxonomy_id: NotRequired[str]
    "Taxonomy id"
    genome_accession: NotRequired[str]
    "Genome Accession\ne.g. CM000663"
    genome_assembly: NotRequired[str]
    "Genome Assembly\ne.g. GCA_000001405.27"
    cpd: NotRequired[Cpd]
    "CPD (Complete Proteome Detector)\n1: Standard\n2: Close to standard (high value)\n3: Close to standard (low value)\n4: Outlier (high value)\n5: Outlier (low value)\n6: Unknown\ne.g. 1"
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
    "BUSCO (Complete %)\ne.g. 97"


ProteomesNamesTaxonomy: TypeAlias = Literal[
    "upid", "organism", "organism_id", "components", "mnemonic", "lineage"
]
ProteomesMiscellaneous: TypeAlias = Literal[
    "busco", "cpd", "genome_assembly", "genome_representation", "protein_count"
]
ProteomesFields: TypeAlias = Literal[ProteomesNamesTaxonomy, ProteomesMiscellaneous]


@dataclass
class ProteomesSearch(unipressed.base.Search):
    """Client for querying the [proteomes Uniprot dataset](https://www.uniprot.org/help/proteomes)"""

    dataset: Literal["proteomes"] = field(default="proteomes", init=False)
    query: ProteomesQuery
    "A query that filters the returned proteins"
    fields: Iterable[ProteomesFields]
    "Fields to return in the result object"
