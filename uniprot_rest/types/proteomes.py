from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

Proteome_type: TypeAlias = Literal["1", "2", "3", "4"]
Cpd: TypeAlias = Literal["1", "2", "3", "4", "5", "6"]
ProteomesQuery: TypeAlias = TypedDict(
    "ProteomesQuery",
    {
        "upid": NotRequired[str],
        "proteome_type": NotRequired[Proteome_type],
        "organism_name": NotRequired[str],
        "taxonomy_name": NotRequired[str],
        "genome_accession": NotRequired[str],
        "genome_assembly": NotRequired[str],
        "cpd": NotRequired[Cpd],
        "busco": NotRequired[int],
    },
)
ProteomesNamesTaxonomy: TypeAlias = Literal[
    "upid", "organism", "organism_id", "components", "mnemonic", "lineage"
]
ProteomesMiscellaneous: TypeAlias = Literal[
    "busco", "cpd", "genome_assembly", "genome_representation", "protein_count"
]
ProteomesFields: TypeAlias = Literal[ProteomesNamesTaxonomy, ProteomesMiscellaneous]


@dataclass
class ProteomesSearch(uniprot_rest.Search):
    dataset: Literal["proteomes"] = field(default="proteomes", init=False)
    query: ProteomesQuery
    fields: ProteomesFields
