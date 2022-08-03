from typing_extensions import Literal, TypeAlias

Dataset: TypeAlias = Literal[
    "uniref",
    "uniparc",
    "taxonomy",
    "uniprotkb",
    "proteomes",
    "locations",
    "unirule",
    "diseases",
    "keywords",
    "citations",
    "database",
    "arba",
]


# class Dataset(Enum):
#     # uniprot = auto()
#     UNIREF = "uniref"
#     UNIPARC = "uniparc"
#     TAXONOMY = "taxonomy"
#     UNIPROTKB = "uniprotkb"
#     PROTEOMES = "proteomes"
#     LOCATIONS = "locations"
#     UNIRULE = "unirule"
#     DISEASES = "diseases"
#     KEYWORDS = "keywords"
#     CITATIONS = "citations"
#     DATABASE = "database"
#     ARBA = "arba"
