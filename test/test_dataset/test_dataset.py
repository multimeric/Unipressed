import itertools

import pytest
from typing_extensions import Type

from unipressed import all_clients
from unipressed.dataset.core import FetchManyDataset, UniprotDataset


@pytest.mark.parametrize(["client"], [[client] for client in all_clients])
def test_dataset(client: Type[UniprotDataset]):
    # Test the search method
    records = client.search("*", format="json").each_record()

    # Compile IDs
    first_records = list(itertools.islice(records, 20))
    ids = []
    for record in first_records:
        ids.append(record[client.id_field()])

    # Test the search method with all other formats
    for format in client._allowed_formats() - {"json"}:
        # Test the search method
        res = next(iter(client.search("*", format=format).each_response()))
        res.raise_for_status()

    # Test the fetch_one method with JSON
    assert client.fetch_one(ids[0], format="json", parse=True) == records[0]

    # Test the fetch_one method with other formats
    for format in client._allowed_formats() - {"json"}:
        client.fetch_one(ids[0], format=format)

    if isinstance(client, FetchManyDataset):
        # Test the fetch_many method with JSON
        client.fetch_many(ids, format="json", parse=True)

        # Test the fetch_many method with other formats
        for format in client._allowed_formats() - {"json"}:
            client.fetch_many(ids, format=format)
