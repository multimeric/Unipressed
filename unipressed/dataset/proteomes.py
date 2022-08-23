from typing import Any, Literal, Mapping

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.proteomes import (
    ProteomesFields,
    ProteomesQuery,
    ProteomesSearch,
)

ProteomesFormats = Literal["json", "tsv", "xlsx", "list", "xml", "rdf"]


class Proteomes(
    UniprotDataset[
        ProteomesQuery,
        Mapping[str, Any],
        ProteomesFields,
        ProteomesSearch,
        ProteomesFormats,
    ]
):
    @classmethod
    def name(cls):
        return "proteomes"
