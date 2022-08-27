from __future__ import annotations

from dataclasses import dataclass
from typing import Iterable

import requests
from typing_extensions import TypeAlias, TypedDict

from unipressed.id_mapping.types import From, To
from unipressed.util import iter_pages


class IdMappingError(Exception):
    pass


@dataclass
class IdMappingClient:
    """
    Client for submitting requests to convert between identifiers.
    """

    @classmethod
    def _submit(cls, source: From, dest: To, ids: Iterable[str]) -> requests.Response:
        return requests.post(
            "https://rest.uniprot.org/idmapping/run",
            data={"ids": ",".join(ids), "from": source, "to": dest},
        )

    @classmethod
    def submit(cls, source: From, dest: To, ids: Iterable[str]) -> IdMappingJob:
        """
        Submits this ID mapping request to the UniProt server, and returns a new object that can be used to access the results
        """
        res = cls._submit(source, dest, ids)
        job_id = res.json()["jobId"]
        return IdMappingJob(job_id)


@dataclass
class IdMappingJob:
    """
    Object that tracks the status and results of an ID mapping request that has been sent to the UniProt server.
    """

    job_id: str

    def get_status(self) -> str:
        """
        Returns a string describing the status of the job (ie if it has completed or not).
        """
        return requests.get(
            f"https://rest.uniprot.org/idmapping/status/{self.job_id}"
        ).json()["jobStatus"]

    def each_result(self) -> Iterable[IdMappingResult]:
        """
        Returns a generator over dictionaries of results, one for each input ID.
        """
        res = requests.get(f"https://rest.uniprot.org/idmapping/results/{self.job_id}")
        for page in iter_pages(res):
            parsed = page.json()
            if "results" not in parsed:
                raise IdMappingError(
                    "UniProt has not yet processed the results, consider using time.sleep() to wait until they are complete."
                )
            else:
                yield from parsed["results"]


IdMappingResult: TypeAlias = TypedDict("IdMappingResult", {"from": str, "to": str})
