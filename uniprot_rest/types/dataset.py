from enum import Enum, auto

class Dataset(Enum):
    # uniprot = auto()
    UNIREF = "uniref"
    UNIPARC = "uniparc"
    TAXONOMY = "taxonomy"
    UNIPROTKB = "uniprotkb"
    PROTEOMES = "proteomes"
    LOCATIONS = "locations"
    UNIRULE = "unirule"
    DISEASES = "diseases"
    KEYWORDS = "keywords"
    CITATIONS = "citations"
    DATABASE = "database"
    ARBA = "arba"
