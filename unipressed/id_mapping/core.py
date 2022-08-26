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
class IdMappingRequest:
    source: From
    dest: To
    ids: Iterable[str]

    def _submit(self) -> requests.Response:
        return requests.post(
            "https://rest.uniprot.org/idmapping/run",
            data={"ids": ",".join(self.ids), "from": self.source, "to": self.dest},
        )

    def submit(self) -> IdMappingJob:
        """
        Submits this ID mapping request to the UniProt server, and returns a new object that can be used to access the results
        """
        res = self._submit()
        job_id = res.json()["jobId"]
        return IdMappingJob(job_id)


@dataclass
class IdMappingJob:
    job_id: str

    def get_status(self) -> str:
        """
        Returns a string describing the status of the job (ie if it has completed or not)
        """
        return requests.get(
            f"https://rest.uniprot.org/idmapping/status/{self.job_id}"
        ).json()["jobStatus"]

    def each_result(self) -> Iterable[IdMappingResult]:
        """
        Returns a generator over dictionaries of results, one for each input ID
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
