from typing import Any, Mapping

from typing_extensions import Literal

from unipressed.dataset.core import FetchManyDataset, UniprotDataset
from unipressed.dataset.generated_types.uniprotkb import UniprotkbFields, UniprotkbQuery

UniprotkbFormats = Literal["txt", "xml", "fasta", "gff", "json", "list", "tsv", "xlsx"]


class Uniprotkb(
    FetchManyDataset[
        UniprotkbQuery,
        Mapping[str, Any],
        UniprotkbFields,
        UniprotkbFormats,
    ]
):
    @classmethod
    def name(cls):
        return "uniprotkb"

    @classmethod
    def bulk_endpoint(cls):
        return "accessions"

    @classmethod
    def id_field(cls, record: Mapping[str, Any]) -> str:
        return record["primaryAccession"]
