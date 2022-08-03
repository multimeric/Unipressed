from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base

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


class TaxonomyQuery(TypedDict):
    and_: NotRequired[Iterable["TaxonomyQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["TaxonomyQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["TaxonomyQuery"]]
    "Negate a filter"
    tax_id: NotRequired[int]
    "Taxon ID"
    scientific: NotRequired[str]
    "Scientific name"
    common: NotRequired[str]
    "Common name"
    mnemonic: NotRequired[str]
    "Mnemonic"
    rank: NotRequired[Rank]
    "Rank\nSUPERKINGDOM: Superkingdom\nKINGDOM: Kingdom\nSUBKINGDOM: Subkingdom\nSUPERPHYLUM: Superphylum\nPHYLUM: Phylum\nSUBPHYLUM: Subphylum\nSUPERCLASS: Superclass\nCLASS: Class\nSUBCLASS: Subclass\nINFRACLASS: Infraclass\nCOHORT: Cohort\nSUBCOHORT: Subcohort\nSUPERORDER: Superorder\nORDER: Order\nSUBORDER: Suborder\nINFRAORDER: Infraorder\nPARVORDER: Parvorder\nSUPERFAMILY: Superfamily\nFAMILY: Family\nSUBFAMILY: Subfamily\nTRIBE: Tribe\nSUBTRIBE: Subtribe\nGENUS: Genus\nSUBGENUS: Subgenus\nSPECIES_GROUP: Species group\nSPECIES_SUBGROUP: Species subgroup\nSPECIES: Species\nSUBSPECIES: Subspecies\nVARIETAS: Varietas\nFORMA: Forma\nNO_RANK: No rank"
    strain: NotRequired[str]
    "Strain"
    host: NotRequired[int]
    "Virus host"
    linked: NotRequired[bool]
    "With external info"
    parent: NotRequired[str]
    "Parent"
    ancestor: NotRequired[str]
    "Ancestor"


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
class TaxonomySearch(unipressed.base.Search):
    """Client for querying the [taxonomy Uniprot dataset](https://www.uniprot.org/help/taxonomy)"""

    dataset: Literal["taxonomy"] = field(default="taxonomy", init=False)
    query: TaxonomyQuery
    "A query that filters the returned proteins"
    fields: Iterable[TaxonomyFields]
    "Fields to return in the result object"
