from __future__ import annotations

from typing import Any, Iterable

import requests


def iter_pages(
    response: requests.Response, method: str = "GET"
) -> Iterable[requests.Response]:
    yield response
    while True:
        link: dict[str, Any] | None = response.links.get("next")
        if link is not None:
            response = requests.request(method, url=link["url"])
            yield response
        else:
            break
