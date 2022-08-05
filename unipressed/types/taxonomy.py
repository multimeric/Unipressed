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
    "Taxon ID\ne.g. 85621"
    scientific: NotRequired[str]
    "Scientific name\ne.g. 16SrII"
    common: NotRequired[str]
    "Common name\ne.g. sample name"
    mnemonic: NotRequired[str]
    "Mnemonic\ne.g. sample mnemonic"
    rank: NotRequired[Rank]
    "Rank\n\nSUPERKINGDOM: Superkingdom\n\nKINGDOM: Kingdom\n\nSUBKINGDOM: Subkingdom\n\nSUPERPHYLUM: Superphylum\n\nPHYLUM: Phylum\n\nSUBPHYLUM: Subphylum\n\nSUPERCLASS: Superclass\n\nCLASS: Class\n\nSUBCLASS: Subclass\n\nINFRACLASS: Infraclass\n\nCOHORT: Cohort\n\nSUBCOHORT: Subcohort\n\nSUPERORDER: Superorder\n\nORDER: Order\n\nSUBORDER: Suborder\n\nINFRAORDER: Infraorder\n\nPARVORDER: Parvorder\n\nSUPERFAMILY: Superfamily\n\nFAMILY: Family\n\nSUBFAMILY: Subfamily\n\nTRIBE: Tribe\n\nSUBTRIBE: Subtribe\n\nGENUS: Genus\n\nSUBGENUS: Subgenus\n\nSPECIES_GROUP: Species group\n\nSPECIES_SUBGROUP: Species subgroup\n\nSPECIES: Species\n\nSUBSPECIES: Subspecies\n\nVARIETAS: Varietas\n\nFORMA: Forma\n\nNO_RANK: No rank\ne.g. SPECIES_GROUP"
    strain: NotRequired[str]
    "Strain\ne.g. SPECIES_GROUP"
    host: NotRequired[int]
    "Virus host\ne.g. 85621"
    linked: NotRequired[bool]
    "With external info\n\ntrue: Yes\n\nfalse: No\ne.g. true"
    parent: NotRequired[str]
    "Parent\ne.g. 9606"
    ancestor: NotRequired[str]
    "Ancestor\ne.g. 85621"


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
