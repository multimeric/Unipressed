from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

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


class TaxonomyQueryDict(TypedDict):
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
    "Rank\ne.g. SPECIES_GROUP\n* SUPERKINGDOM: Superkingdom\n* KINGDOM: Kingdom\n* SUBKINGDOM: Subkingdom\n* SUPERPHYLUM: Superphylum\n* PHYLUM: Phylum\n* SUBPHYLUM: Subphylum\n* SUPERCLASS: Superclass\n* CLASS: Class\n* SUBCLASS: Subclass\n* INFRACLASS: Infraclass\n* COHORT: Cohort\n* SUBCOHORT: Subcohort\n* SUPERORDER: Superorder\n* ORDER: Order\n* SUBORDER: Suborder\n* INFRAORDER: Infraorder\n* PARVORDER: Parvorder\n* SUPERFAMILY: Superfamily\n* FAMILY: Family\n* SUBFAMILY: Subfamily\n* TRIBE: Tribe\n* SUBTRIBE: Subtribe\n* GENUS: Genus\n* SUBGENUS: Subgenus\n* SPECIES_GROUP: Species group\n* SPECIES_SUBGROUP: Species subgroup\n* SPECIES: Species\n* SUBSPECIES: Subspecies\n* VARIETAS: Varietas\n* FORMA: Forma\n* NO_RANK: No rank"
    strain: NotRequired[str]
    "Strain\ne.g. SPECIES_GROUP"
    host: NotRequired[int]
    "Virus host\ne.g. 85621"
    linked: NotRequired[bool]
    "With external info\ne.g. true\n* true: Yes\n* false: No"
    parent: NotRequired[str]
    "Parent\ne.g. 9606"
    ancestor: NotRequired[str]
    "Ancestor\ne.g. 85621"


TaxonomyQuery: TypeAlias = Union[TaxonomyQueryDict, str]
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
