from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

Rank: TypeAlias = Literal[
    "SUPERKINGDOM",
    "KINGDOM",
    "SUBKINGDOM",
    "SUPERPHYLUM",
    "PHYLUM",
    "SUBPHYLUM",
    "SUPERCLASS",
    "CLASS",
    "SUBCLASS",
    "INFRACLASS",
    "COHORT",
    "SUBCOHORT",
    "SUPERORDER",
    "ORDER",
    "SUBORDER",
    "INFRAORDER",
    "PARVORDER",
    "SUPERFAMILY",
    "FAMILY",
    "SUBFAMILY",
    "TRIBE",
    "SUBTRIBE",
    "GENUS",
    "SUBGENUS",
    "SPECIES_GROUP",
    "SPECIES_SUBGROUP",
    "SPECIES",
    "SUBSPECIES",
    "VARIETAS",
    "FORMA",
    "NO_RANK",
]
TaxonomyQuery: TypeAlias = TypedDict(
    "TaxonomyQuery",
    {
        "tax_id": NotRequired[int],
        "scientific": NotRequired[str],
        "common": NotRequired[str],
        "mnemonic": NotRequired[str],
        "rank": NotRequired[Rank],
        "strain": NotRequired[str],
        "host": NotRequired[int],
        "linked": NotRequired[bool],
        "parent": NotRequired[str],
        "ancestor": NotRequired[str],
    },
)
TaxonomyTaxonomy: TypeAlias = Literal[
    "id",
    "mnemonic",
    "scientific_name",
    "common_name",
    "synonyms",
    "other_names",
    "rank",
    "reviewed",
    "lineage",
    "strains",
    "parent",
    "hosts",
    "links",
    "statistics",
]
TaxonomyFields: TypeAlias = Literal[
    TaxonomyTaxonomy,
]


@dataclass
class TaxonomySearch(uniprot_rest.Search):
    dataset: Literal["taxonomy"] = field(default="taxonomy", init=False)
    query: TaxonomyQuery
    fields: TaxonomyFields
