from __future__ import annotations

from dataclasses import dataclass
from typing import Any, Callable, Iterable

import requests
from typing_extensions import Literal, ParamSpec, TypeAlias, TypedDict, TypeVar

import unipressed.id_mapping.types as id_types
from unipressed.util import iter_pages

UniprotStatus: TypeAlias = Literal[
    # See https://github.com/ebi-uniprot/uniprot-rest-api/blob/master/idmapping-rest/src/main/java/org/uniprot/api/idmapping/controller/response/JobStatus.java
    "NEW",
    "RUNNING",
    "FINISHED",
    "ERROR",
]

Param1 = ParamSpec("Param1")
Param2 = ParamSpec("Param2")
Ret1 = TypeVar("Ret1")
Ret2 = TypeVar("Ret2")


def copy_signature(
    f: Callable[Param1, Ret1]
) -> Callable[[Callable[Param2, Ret2]], Callable[Param1, Ret2]]:
    """
    Copies the argument signature from function f and applies it to the decorated function, but keeps the return value
    """

    def _inner(f: Callable[Param2, Ret2]):
        return f

    return _inner  # type: ignore


class IdMappingError(Exception):
    pass


@dataclass
class IdMappingClient:
    """
    Client for submitting requests to convert between identifiers.
    """

    @classmethod
    def _submit(
        cls, source: str, dest: str, ids: Iterable[str], taxon_id: int | None
    ) -> requests.Response:
        data: dict[str, Any] = {"ids": ",".join(ids), "from": source, "to": dest}
        if taxon_id is not None:
            data["taxId"] = taxon_id
        return requests.post(
            "https://rest.uniprot.org/idmapping/run",
            data=data,
        )

    @copy_signature(id_types.SubmitDummyClass.submit)
    @classmethod
    def submit(
        cls, source: str, dest: str, ids: Iterable[str], taxon_id: int | None = None
    ) -> IdMappingJob:
        """
        Submits this ID mapping request to the UniProt server, and returns a new object that can be used to access the results

        Args:
            source: Name of the database from which the ids originate
            dest: Name of the database that the IDs will be converted to
            ids: Set of IDs to convert
            taxon_id: Optionally, a UniProt taxon ID to restrict the results to. For example, you can use `4932` to
                restrict the results to Baker's yest (https://www.uniprot.org/taxonomy/4932).
        """
        res = cls._submit(source, dest, ids, taxon_id=taxon_id)
        job_id = res.json()["jobId"]
        return IdMappingJob(job_id)


@dataclass
class IdMappingJob:
    """
    Object that tracks the status and results of an ID mapping request that has been sent to the UniProt server.
    """

    job_id: str

    def get_status(self) -> UniprotStatus:
        """
        Returns a string describing the status of the job (ie if it has completed or not).
        """
        data = requests.get(
            f"https://rest.uniprot.org/idmapping/status/{self.job_id}"
        ).json()
        if "jobStatus" in data:
            # This is the correct behaviour
            return data["jobStatus"]
        elif "results" in data:
            # Sometimes UniProt returns the actual results even though we asked for the status, see https://github.com/multimeric/Unipressed/issues/21
            return "FINISHED"
        else:
            raise IdMappingError(
                f"Unknown response returned by UniProt. Received {data}"
            )

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


IdMappingResult = TypedDict("IdMappingResult", {"from": str, "to": str})
