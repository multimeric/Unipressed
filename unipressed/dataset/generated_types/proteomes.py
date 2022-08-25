from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

ProteomeType: TypeAlias = Literal["1", "2", "3", "4"]
Cpd: TypeAlias = Literal["1", "2", "3", "4", "5", "6"]


class ProteomesQueryDict(TypedDict):
    and_: NotRequired[Iterable["ProteomesQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["ProteomesQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["ProteomesQuery"]]
    "Negate a filter"
    upid: NotRequired[str]
    "Proteome ID\ne.g. UP000000718"
    proteome_type: NotRequired[ProteomeType]
    "Proteome Type\ne.g. 1\n* 1: Reference\n* 2: Other\n* 3: Redundant\n* 4: Excluded"
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
    "CPD (Complete Proteome Detector)\ne.g. 1\n* 1: Standard\n* 2: Close to standard (high value)\n* 3: Close to standard (low value)\n* 4: Outlier (high value)\n* 5: Outlier (low value)\n* 6: Unknown"
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


ProteomesQuery: TypeAlias = Union[ProteomesQueryDict, str]
ProteomesNamesTaxonomy: TypeAlias = Literal[
    "upid", "organism", "organism_id", "components", "mnemonic", "lineage"
]
ProteomesMiscellaneous: TypeAlias = Literal[
    "busco", "cpd", "genome_assembly", "genome_representation", "protein_count"
]
ProteomesFields: TypeAlias = Literal[ProteomesNamesTaxonomy, ProteomesMiscellaneous]
