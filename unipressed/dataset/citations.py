from typing import Any, Literal, Mapping

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.citations import (
    CitationsFields,
    CitationsQuery,
    CitationsSearch,
)

CitationsFormats = Literal["json", "list", "tsv", "xlsx"]


class Citations(
    UniprotDataset[
        CitationsQuery,
        Mapping[str, Any],
        CitationsFields,
        CitationsSearch,
        CitationsFormats,
    ]
):
    @classmethod
    def name(cls):
        return "citations"
