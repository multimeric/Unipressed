from typing_extensions import Literal, TypeAlias

Format: TypeAlias = Literal[
    "html", "txt", "xml", "rdf", "fasta", "gff", "json", "list", "tsv", "obo", "xlsx"
]
