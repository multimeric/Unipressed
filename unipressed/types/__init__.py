from __future__ import annotations

from typing import Type

from unipressed.base import Search

from .arba import ArbaSearch
from .citations import CitationsSearch
from .database import DatabaseSearch
from .diseases import DiseasesSearch
from .keywords import KeywordsSearch
from .locations import LocationsSearch
from .proteomes import ProteomesSearch
from .taxonomy import TaxonomySearch
from .uniparc import UniparcSearch
from .uniprotkb import UniprotkbSearch
from .uniref import UnirefSearch
from .unirule import UniruleSearch

all_clients: list[Type[Search]] = [
    ArbaSearch,
    CitationsSearch,
    DatabaseSearch,
    DiseasesSearch,
    KeywordsSearch,
    LocationsSearch,
    ProteomesSearch,
    TaxonomySearch,
    UniparcSearch,
    UniprotkbSearch,
    UnirefSearch,
    UniruleSearch,
]
