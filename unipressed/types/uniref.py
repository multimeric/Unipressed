from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base

Identity: TypeAlias = Literal["1.0", "0.9", "0.5"]


class UnirefQuery(TypedDict):
    and_: NotRequired[Iterable["UnirefQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UnirefQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UnirefQuery"]]
    "Negate a filter"
    id: NotRequired[str]
    "UniRef ID"
    name: NotRequired[str]
    "Cluster name"
    identity: NotRequired[Identity]
    "Sequence identity\n1.0: 100%\n0.9: 90%\n0.5: 50%"
    count: NotRequired[
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
    "Cluster size"
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
    created: NotRequired[
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
    "Date published"
    uniprot_id: NotRequired[str]
    "UniProtKB ID/AC"
    upi: NotRequired[str]
    "UniParc ID"
    taxonomy_name: NotRequired[str]
    "Taxonomy [OC]"
    cluster: NotRequired[str]
    "Related clusters"


UnirefNamesTaxonomy: TypeAlias = Literal[
    "id", "name", "common_taxon", "common_taxonid", "organism_id", "organism"
]
UnirefSequences: TypeAlias = Literal["identity", "length", "sequence"]
UnirefMiscellaneous: TypeAlias = Literal["types", "members", "count"]
UnirefDateOf: TypeAlias = Literal[
    "created",
]
UnirefFields: TypeAlias = Literal[
    UnirefNamesTaxonomy, UnirefSequences, UnirefMiscellaneous, UnirefDateOf
]


@dataclass
class UnirefSearch(unipressed.base.Search):
    """Client for querying the [uniref Uniprot dataset](https://www.uniprot.org/help/uniref)"""

    dataset: Literal["uniref"] = field(default="uniref", init=False)
    query: UnirefQuery
    "A query that filters the returned proteins"
    fields: Iterable[UnirefFields]
    "Fields to return in the result object"
