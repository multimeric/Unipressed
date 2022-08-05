from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

import unipressed.base


class UniparcQuery(TypedDict):
    and_: NotRequired[Iterable["UniparcQuery"]]
    "Two or more filters that must both be satisfied"
    or_: NotRequired[Iterable["UniparcQuery"]]
    "Two or more filters, any of which can be satisfied"
    not_: NotRequired[Iterable["UniparcQuery"]]
    "Negate a filter"
    upi: NotRequired[str]
    "UniParc ID\ne.g. UPI0000000001"
    uniprotkb: NotRequired[str]
    "UniProtKB AC\ne.g. P12345"
    isoform: NotRequired[str]
    "UniProtKB isoform ID\ne.g. P12345"
    upid: NotRequired[str]
    "Proteome ID\ne.g. UP123456789"
    taxonomy_name: NotRequired[str]
    "Taxonomy [OC]\ne.g. sample name"
    taxonomy_id: NotRequired[str]
    "Taxonomy id"
    gene: NotRequired[str]
    "Gene name [GN]\ne.g. sample gene"
    protein: NotRequired[str]
    "Protein name\ne.g. sample protein"
    database: NotRequired[str]
    "Database\n\nEnsemblBacteria: EnsemblBacteria\n\nEnsemblFungi: EnsemblFungi\n\nEnsemblMetazoa: EnsemblMetazoa\n\nEnsemblPlants: EnsemblPlants\n\nEnsemblProtists: EnsemblProtists\n\nembl-cds: EMBL CDS\n\nEMBLWGS: EMBLWGS\n\nEMBL_CON: EMBL_CON\n\nEMBL_TPA: EMBL_TPA\n\nEMBL_TSA: EMBL_TSA\n\nEnsembl: Ensembl\n\nEPO: EPO\n\nFlyBase: FlyBase\n\nH-InvDB: H-InvDB\n\nIPI: IPI\n\nJPO: JPO\n\nKIPO: KIPO\n\nPATRIC: PATRIC\n\nPDB: PDB\n\nPIR: PIR\n\nPIRARC: PIRARC\n\nPRF: PRF\n\nRefSeq: RefSeq\n\nREMTREMBL: REMTREMBL\n\nSEED: SEED\n\nSGD: SGD\n\nUniProt: UniProtKB\n\nisoforms: UniProtKB/Swiss-Prot isoforms\n\nTAIR: TAIR\n\nTREMBLNEW: TREMBLNEW\n\nTREMBL_VARSPLIC: TREMBL_VARSPLIC\n\nTROME: TROME\n\nUNIMES: UNIMES\n\nUSPTO: USPTO\n\nVectorBase: VectorBase\n\nVEGA: VEGA\n\nWormBase: WormBase\n\nWBParaSite: WBParaSite\ne.g. sample database"
    active: NotRequired[str]
    "Active\n\nEnsemblBacteria: EnsemblBacteria\n\nEnsemblFungi: EnsemblFungi\n\nEnsemblMetazoa: EnsemblMetazoa\n\nEnsemblPlants: EnsemblPlants\n\nEnsemblProtists: EnsemblProtists\n\nembl-cds: EMBL CDS\n\nEMBLWGS: EMBLWGS\n\nEMBL_CON: EMBL_CON\n\nEMBL_TSA: EMBL_TSA\n\nEnsembl: Ensembl\n\nEPO: EPO\n\nFlyBase: FlyBase\n\nJPO: JPO\n\nKIPO: KIPO\n\nPATRIC: PATRIC\n\nPDB: PDB\n\nRefSeq: RefSeq\n\nSEED: SEED\n\nSGD: SGD\n\nUniProt: UniProtKB\n\nisoforms: UniProtKB/Swiss-Prot isoforms\n\nTAIR: TAIR\n\nTROME: TROME\n\nUSPTO: USPTO\n\nVEGA: VEGA\n\nWormBase: WormBase\n\nWBParaSite: WBParaSite\ne.g. sample active"
    checksum: NotRequired[str]
    "Checksum (CRC64/MD5)\ne.g. sample checksum"
    length: NotRequired[
        tuple[
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
            Union[
                int,
                Literal[
                    "*",
                ],
            ],
        ]
    ]
    "Sequence length\ne.g. [100 TO 300]"
    dbid: NotRequired[str]
    "Database ID\ne.g. AAC02967"
    feature_id: NotRequired[str]
    "Feature ID\ne.g. IPR004251"
    proteomecomponent: NotRequired[str]
    "Proteome Component\ne.g. chromosome"


UniparcNamesTaxonomy: TypeAlias = Literal[
    "upi", "gene", "organism_id", "organism", "protein", "proteome"
]
UniparcSequences: TypeAlias = Literal["checksum", "length", "sequence"]
UniparcMiscellaneous: TypeAlias = Literal[
    "accession",
]
UniparcDateOf: TypeAlias = Literal["first_seen", "last_seen"]
UniparcFamilyDomains: TypeAlias = Literal[
    "CDD",
    "Gene3D",
    "HAMAP",
    "PANTHER",
    "Pfam",
    "PIRSF",
    "PRINTS",
    "PROSITE",
    "SFLD",
    "SMART",
    "SUPFAM",
    "TIGRFAMs",
]
UniparcFields: TypeAlias = Literal[
    UniparcNamesTaxonomy,
    UniparcSequences,
    UniparcMiscellaneous,
    UniparcDateOf,
    UniparcFamilyDomains,
]


@dataclass
class UniparcSearch(unipressed.base.Search):
    """Client for querying the [uniparc Uniprot dataset](https://www.uniprot.org/help/uniparc)"""

    dataset: Literal["uniparc"] = field(default="uniparc", init=False)
    query: UniparcQuery
    "A query that filters the returned proteins"
    fields: Iterable[UniparcFields]
    "Fields to return in the result object"
