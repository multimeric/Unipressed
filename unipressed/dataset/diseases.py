from typing import Any, Literal, Mapping

from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.generated_types.diseases import (
    DiseasesFields,
    DiseasesQuery,
    DiseasesSearch,
)

DiseasesFormats = Literal["json", "tsv", "xlsx", "list", "obo"]


class Diseases(
    UniprotDataset[
        DiseasesQuery,
        Mapping[str, Any],
        DiseasesFields,
        DiseasesSearch,
        DiseasesFormats,
    ]
):
    @classmethod
    def name(cls):
        return "diseases"
