from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

UniparcQuery: TypeAlias = TypedDict(
    "UniparcQuery",
    {
        "upi": NotRequired[str],
        "uniprotkb": NotRequired[str],
        "isoform": NotRequired[str],
        "upid": NotRequired[str],
        "taxonomy_name": NotRequired[str],
        "gene": NotRequired[str],
        "protein": NotRequired[str],
        "database": NotRequired[str],
        "active": NotRequired[str],
        "checksum": NotRequired[str],
        "length": NotRequired[int],
        "dbid": NotRequired[str],
        "feature_id": NotRequired[str],
        "proteomecomponent": NotRequired[str],
    },
)
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
class UniparcSearch(uniprot_rest.Search):
    dataset: Literal["uniparc"] = field(default="uniparc", init=False)
    query: UniparcQuery
    fields: UniparcFields
