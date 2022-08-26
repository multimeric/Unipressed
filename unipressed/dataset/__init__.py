from __future__ import annotations

from typing import Type

from unipressed.dataset.arba import ArbaClient
from unipressed.dataset.citations import CitationsClient
from unipressed.dataset.core import DatasetClient
from unipressed.dataset.database import DatabaseClient
from unipressed.dataset.diseases import DiseasesClient
from unipressed.dataset.keywords import KeywordsClient
from unipressed.dataset.locations import LocationsClient
from unipressed.dataset.proteomes import ProteomesClient
from unipressed.dataset.taxonomy import TaxonomyClient
from unipressed.dataset.uniparc import UniparcClient
from unipressed.dataset.uniprotkb import UniprotkbClient
from unipressed.dataset.uniref import UnirefClient
from unipressed.dataset.unirule import UniruleClient

all_clients: list[Type[DatasetClient]] = [
    ArbaClient,
    CitationsClient,
    DatabaseClient,
    DiseasesClient,
    KeywordsClient,
    LocationsClient,
    ProteomesClient,
    TaxonomyClient,
    UniparcClient,
    UniprotkbClient,
    UnirefClient,
    UniruleClient,
]
