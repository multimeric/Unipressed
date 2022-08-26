import itertools

import pytest
from typing_extensions import Type

from unipressed.dataset import all_clients
from unipressed.dataset.core import DatasetClient, FetchManyClient


@pytest.mark.parametrize(["client"], [[client] for client in all_clients])
def test_dataset(client: Type[DatasetClient]):
    # Test the search method
    records = client.search("*", format="json").each_record()

    # Compile IDs
    first_records = list(itertools.islice(records, 20))
    ids = []
    for record in first_records:
        ids.append(client._id_field(record))

    # Test the search method with all other formats
    for format in client._allowed_formats() - {"json"}:
        # Test the search method
        res = next(iter(client.search("*", format=format).each_response()))
        res.raise_for_status()

    # Test the fetch_one method with JSON
    fetch_one = client.fetch_one(ids[0], format="json", parse=True)
    assert client._id_field(fetch_one) == client._id_field(first_records[0])

    # Test the fetch_one method with other formats
    for format in client._allowed_formats() - {"json"}:
        res = client.fetch_one(ids[0], format=format)
        content = res.read()
        assert len(content) > 0

        if format in {
            "html",
            "txt",
            "xml",
            "rdf",
            "fasta",
            "gff",
            "json",
            "list",
            "tsv",
        }:
            # If it's a text format, we can coarsely check that the file is valid by decoding it
            content.decode()

    if isinstance(client, FetchManyClient):
        # Test the fetch_many method with JSON
        client.fetch_many(ids, format="json", parse=True)

        # Test the fetch_many method with other formats
        for format in client._allowed_formats() - {"json"}:
            client.fetch_many(ids, format=format)
