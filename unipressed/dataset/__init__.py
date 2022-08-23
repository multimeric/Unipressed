from __future__ import annotations

from typing import Type

from unipressed.dataset.arba import Arba
from unipressed.dataset.citations import Citations
from unipressed.dataset.core import UniprotDataset
from unipressed.dataset.database import Database
from unipressed.dataset.diseases import Diseases
from unipressed.dataset.keywords import Keywords
from unipressed.dataset.locations import Locations
from unipressed.dataset.proteomes import Proteomes
from unipressed.dataset.taxonomy import Taxonomy
from unipressed.dataset.uniparc import Uniparc
from unipressed.dataset.uniprotkb import Uniprotkb
from unipressed.dataset.uniref import Uniref
from unipressed.dataset.unirule import Unirule

all_clients: list[Type[UniprotDataset]] = [
    Arba,
    Citations,
    Database,
    Diseases,
    Keywords,
    Locations,
    Proteomes,
    Taxonomy,
    Uniparc,
    Uniprotkb,
    Uniref,
    Unirule,
]
