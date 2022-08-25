from __future__ import annotations

import re
from typing import TYPE_CHECKING, Any, Iterable

from unipressed.dataset.search import Search

INVALID_FIELD_REGEX = re.compile(r"'(\w+)' is not a valid search field")

if TYPE_CHECKING:
    from codegen.search.generate_fields import FieldDefinition


def validate_query_fields(
    fields: Iterable[FieldDefinition], dataset: str
) -> Iterable[FieldDefinition]:
    """
    Given a list of field definitions, returns only those that are valid, based on the uniprot server's response
    """
    client = Search[Any, Any, Any, Any](
        # Populate every field
        query={field.name: "foo" for field in fields},
        dataset=dataset,
    )
    response = next(iter(client.each_response()))

    if response.status_code == 200:
        yield from fields
    else:
        invalid: set[str] = set()
        for warning in response.json()["messages"]:
            match = INVALID_FIELD_REGEX.match(warning)
            if match:
                invalid.add(match.group(1))
        for field in fields:
            if field.name not in invalid:
                yield field
