from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class UniparcQuery(TypedDict):
    and_: NotRequired[Iterable["UniparcQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UniparcQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UniparcQuery"]]
    "Negate a filter"
    upi: NotRequired[str]
    "UniParc ID"
    uniprotkb: NotRequired[str]
    "UniProtKB AC"
    isoform: NotRequired[str]
    "UniProtKB isoform ID"
    upid: NotRequired[str]
    "Proteome ID"
    taxonomy_name: NotRequired[str]
    "Taxonomy [OC]"
    gene: NotRequired[str]
    "Gene name [GN]"
    protein: NotRequired[str]
    "Protein name"
    database: NotRequired[str]
    "Database"
    active: NotRequired[str]
    "Active"
    checksum: NotRequired[str]
    "Checksum (CRC64/MD5)"
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
    dbid: NotRequired[str]
    "Database ID"
    feature_id: NotRequired[str]
    "Feature ID"
    proteomecomponent: NotRequired[str]
    "Proteome Component"


UniparcNamesTaxonomy: TypeAlias = Literal[
    "upi", "gene", "organism_id", "organism", "protein", "proteome"
]
UniparcSequences: TypeAlias = Literal["checksum", "length", "sequence"]
UniparcMiscellaneous: TypeAlias = Literal[
    "accession",
]
UniparcDateOf: TypeAlias = Literal["first_seen", "last_seen"]
UniparcFamilyDomains: TypeAlias = Literal[
    "CDD",
    "Gene3D",
    "HAMAP",
    "PANTHER",
    "Pfam",
    "PIRSF",
    "PRINTS",
    "PROSITE",
    "SFLD",
    "SMART",
    "SUPFAM",
    "TIGRFAMs",
]
UniparcFields: TypeAlias = Literal[
    UniparcNamesTaxonomy,
    UniparcSequences,
    UniparcMiscellaneous,
    UniparcDateOf,
    UniparcFamilyDomains,
]


@dataclass
class UniparcSearch(unipressed.base.Search):
    """Client for querying the [uniparc Uniprot dataset](https://www.uniprot.org/help/uniparc)"""

    dataset: Literal["uniparc"] = field(default="uniparc", init=False)
    query: UniparcQuery
    "A query that filters the returned proteins"
    fields: Iterable[UniparcFields]
    "Fields to return in the result object"
