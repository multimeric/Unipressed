from typing import Any, Literal, Mapping

from unipressed.dataset.core import FetchManyDataset, UniprotDataset
from unipressed.dataset.generated_types.uniprotkb import (
    UniprotkbFields,
    UniprotkbQuery,
    UniprotkbSearch,
)

UniprotkbFormats = Literal[
    "html", "txt", "xml", "rdf", "fasta", "gff", "json", "list", "tsv", "xlsx"
]


class Uniprotkb(
    FetchManyDataset[
        UniprotkbQuery,
        Mapping[str, Any],
        UniprotkbFields,
        UniprotkbSearch,
        UniprotkbFormats,
    ]
):
    @classmethod
    def name(cls):
        return "uniprotkb"

    @classmethod
    def bulk_endpoint(cls):
        return "accessions"
