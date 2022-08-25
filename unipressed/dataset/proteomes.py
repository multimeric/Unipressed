from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.proteomes import ProteomesFields, ProteomesQuery

ProteomesFormats = Literal["json", "tsv", "xlsx", "list", "xml"]


class Proteomes(
    UniprotDataset[
        ProteomesQuery,
        Mapping[str, Any],
        ProteomesFields,
        ProteomesFormats,
    ]
):
    @classmethod
    def name(cls):
        return "proteomes"
