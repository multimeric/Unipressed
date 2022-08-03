import sys

import pytest

if sys.version_info < (3, 9):
    # Python 3.7 doesn't have get_args(), and Python 3.8 has it, but it doesn't simplify the type of a Literal[Literal[...]] which
    # would require an awkward workaround
    pytest.skip(
        reason="Python 3.9 required for this set of tests", allow_module_level=True
    )

from typing import Type, get_args, get_type_hints

import unipressed.types
from unipressed.base import Search


@pytest.mark.parametrize(["client"], [[it] for it in unipressed.types.all_clients])
def test_valid_query_fields(client: Type[Search]):
    """
    Test that all the query fields defined by our schemas are accepted by Uniprot
    """
    query = {}
    query_cls = get_type_hints(client)["query"]
    for query_field in query_cls.__optional_keys__ | query_cls.__required_keys__:
        if query_field not in {"and_", "or_", "not_"}:
            query[query_field] = "foo"
    response = next(iter(client(query=query).each_response()))

    # Only raise an error if the request failed, and then only if because we provided an invalid field
    # We aren't interested in other types of validation error in this test
    if response.status_code != 200:
        for warning in response.json()["messages"]:
            assert "is not a valid search field" not in warning


@pytest.mark.parametrize(["client"], [[it] for it in unipressed.types.all_clients])
def test_valid_return_fields(client: Type[Search]):
    """
    Test that all the return fields defined by our schemas are accepted by Uniprot
    """
    # We get a response such as "Invalid fields parameter value 'foo'" with a 400 status code if we provide an invalid field
    fields_field = get_type_hints(client)["fields"]
    (literal,) = get_args(fields_field)
    response = next(
        iter(
            client(
                query="ThisQueryShouldReturnNoResults", fields=get_args(literal)
            ).each_response()
        )
    )
    response.raise_for_status()
