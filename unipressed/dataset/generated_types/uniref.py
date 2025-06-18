from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

Identity: TypeAlias = Literal["1.0", "0.9", "0.5"]


class UnirefQueryDict(TypedDict):
    and_: NotRequired[Iterable["UnirefQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UnirefQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UnirefQuery"]]
    "Negate a filter"
    id: NotRequired[str]
    "UniRef ID\ne.g. UniRef100_A0A001"
    name: NotRequired[str]
    "Cluster name\ne.g. Integrase core domain protein"
    identity: NotRequired[Identity]
    "Sequence identity\ne.g. 1.0\n* 1.0: 100%\n* 0.9: 90%\n* 0.5: 50%"
    count: NotRequired[
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
    "Cluster size\ne.g. [1 TO 10]"
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
    "Sequence length\ne.g. [1 TO 100]"
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
    "Date of last modification\ne.g. [2011-10-10 TO 2019-10-10]"
    uniprotkb: NotRequired[str]
    "UniProtKB ID/AC\ne.g. P35222"
    uniparc: NotRequired[str]
    "UniParc ID\ne.g. UPI000002DB1C"
    taxonomy_name: NotRequired[str]
    "Taxonomy [OC]\ne.g. mammalia"
    taxonomy_id: NotRequired[str]
    "Taxonomy id"
    cluster: NotRequired[str]
    "Related clusters\ne.g. UniRef100_A0A001"


UnirefQuery: TypeAlias = Union[UnirefQueryDict, str]
UnirefNamesTaxonomy: TypeAlias = Literal[
    "id", "name", "common_taxon", "common_taxonid", "organism_id", "organism"
]
UnirefSequences: TypeAlias = Literal["identity", "length", "sequence"]
UnirefMiscellaneous: TypeAlias = Literal["types", "members", "count"]
UnirefDateOf: TypeAlias = Literal["date_modified",]
UnirefFields: TypeAlias = Literal[
    UnirefNamesTaxonomy, UnirefSequences, UnirefMiscellaneous, UnirefDateOf
]
