from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

Identity: TypeAlias = Literal["1.0", "0.9", "0.5"]
UnirefQuery: TypeAlias = TypedDict(
    "UnirefQuery",
    {
        "id": NotRequired[str],
        "name": NotRequired[str],
        "identity": NotRequired[Identity],
        "count": NotRequired[int],
        "length": NotRequired[int],
        "created": NotRequired[date],
        "uniprot_id": NotRequired[str],
        "upi": NotRequired[str],
        "taxonomy_name": NotRequired[str],
        "cluster": NotRequired[str],
    },
)
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
class UnirefSearch(uniprot_rest.Search):
    dataset: Literal["uniref"] = field(default="uniref", init=False)
    query: UnirefQuery
    fields: UnirefFields
