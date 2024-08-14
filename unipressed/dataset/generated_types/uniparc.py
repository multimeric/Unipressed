from __future__ import annotations

from datetime import date
from typing import Iterable, Union

from typing_extensions import Literal, NotRequired, TypeAlias, TypedDict

Database: TypeAlias = Literal[
    "EnsemblBacteria",
    "EnsemblFungi",
    "EnsemblMetazoa",
    "EnsemblPlants",
    "EnsemblProtists",
    "embl-cds",
    "EMBL_CON",
    "EMBL_TPA",
    "EMBL_TSA",
    "EMBLWGS",
    "Ensembl",
    "EnsemblRapid",
    "EPO",
    "FlyBase",
    "FusionGDB",
    "H-InvDB",
    "IPI",
    "JPO",
    "KIPO",
    "PATRIC",
    "PDB",
    "PIR",
    "PIRARC",
    "PRF",
    "RefSeq",
    "REMTREMBL",
    "SEED",
    "SGD",
    "UniProt",
    "isoforms",
    "TAIR",
    "TREMBLNEW",
    "TREMBL_VARSPLIC",
    "TROME",
    "UNIMES",
    "USPTO",
    "VectorBase",
    "VEGA",
    "WBParaSite",
    "WormBase",
]
Active: TypeAlias = Literal[
    "EnsemblBacteria",
    "EnsemblFungi",
    "EnsemblMetazoa",
    "EnsemblPlants",
    "EnsemblProtists",
    "embl-cds",
    "EMBL_CON",
    "EMBL_TSA",
    "EMBLWGS",
    "Ensembl",
    "EnsemblRapid",
    "EPO",
    "FlyBase",
    "FusionGDB",
    "JPO",
    "KIPO",
    "PATRIC",
    "PDB",
    "RefSeq",
    "SEED",
    "SGD",
    "UniProt",
    "isoforms",
    "TAIR",
    "TROME",
    "USPTO",
    "VEGA",
    "WBParaSite",
    "WormBase",
]


class UniparcQueryDict(TypedDict):
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
    "Taxonomy [OC]\ne.g. Human"
    taxonomy_id: NotRequired[str]
    "Taxonomy id"
    gene: NotRequired[str]
    "Gene name [GN]\ne.g. PROZ"
    protein: NotRequired[str]
    "Protein name\ne.g. Protein Z"
    database: NotRequired[Database]
    "Database\ne.g. Gene3D\n* EnsemblBacteria: EnsemblBacteria\n* EnsemblFungi: EnsemblFungi\n* EnsemblMetazoa: EnsemblMetazoa\n* EnsemblPlants: EnsemblPlants\n* EnsemblProtists: EnsemblProtists\n* embl-cds: EMBL CDS\n* EMBL_CON: EMBL_CON\n* EMBL_TPA: EMBL_TPA\n* EMBL_TSA: EMBL_TSA\n* EMBLWGS: EMBLWGS\n* Ensembl: Ensembl\n* EnsemblRapid: EnsemblRapid\n* EPO: EPO\n* FlyBase: FlyBase\n* FusionGDB: FusionGDB\n* H-InvDB: H-InvDB\n* IPI: IPI\n* JPO: JPO\n* KIPO: KIPO\n* PATRIC: PATRIC\n* PDB: PDB\n* PIR: PIR\n* PIRARC: PIRARC\n* PRF: PRF\n* RefSeq: RefSeq\n* REMTREMBL: REMTREMBL\n* SEED: SEED\n* SGD: SGD\n* UniProt: UniProtKB\n* isoforms: UniProtKB/Swiss-Prot isoforms\n* TAIR: TAIR\n* TREMBLNEW: TREMBLNEW\n* TREMBL_VARSPLIC: TREMBL_VARSPLIC\n* TROME: TROME\n* UNIMES: UNIMES\n* USPTO: USPTO\n* VectorBase: VectorBase\n* VEGA: VEGA\n* WBParaSite: WBParaSite\n* WormBase: WormBase"
    active: NotRequired[Active]
    "Active\ne.g. Gene3D\n* EnsemblBacteria: EnsemblBacteria\n* EnsemblFungi: EnsemblFungi\n* EnsemblMetazoa: EnsemblMetazoa\n* EnsemblPlants: EnsemblPlants\n* EnsemblProtists: EnsemblProtists\n* embl-cds: EMBL CDS\n* EMBL_CON: EMBL_CON\n* EMBL_TSA: EMBL_TSA\n* EMBLWGS: EMBLWGS\n* Ensembl: Ensembl\n* EnsemblRapid: EnsemblRapid\n* EPO: EPO\n* FlyBase: FlyBase\n* FusionGDB: FusionGDB\n* JPO: JPO\n* KIPO: KIPO\n* PATRIC: PATRIC\n* PDB: PDB\n* RefSeq: RefSeq\n* SEED: SEED\n* SGD: SGD\n* UniProt: UniProtKB\n* isoforms: UniProtKB/Swiss-Prot isoforms\n* TAIR: TAIR\n* TROME: TROME\n* USPTO: USPTO\n* VEGA: VEGA\n* WBParaSite: WBParaSite\n* WormBase: WormBase"
    checksum: NotRequired[str]
    "Checksum (CRC64/MD5)\ne.g. B8824CE1ECAEEEAE"
    length: NotRequired[
        tuple[
            Union[
                int,
                Literal["*",],
            ],
            Union[
                int,
                Literal["*",],
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
    organism_id: NotRequired[int]
    "Organism ID\ne.g. 10254"


UniparcQuery: TypeAlias = Union[UniparcQueryDict, str]
UniparcNamesTaxonomy: TypeAlias = Literal[
    "upi", "gene", "organism_id", "organism", "protein", "proteome"
]
UniparcSequences: TypeAlias = Literal["checksum", "length", "sequence"]
UniparcMiscellaneous: TypeAlias = Literal["accession",]
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
    "NCBIfam",
]
UniparcFields: TypeAlias = Literal[
    UniparcNamesTaxonomy,
    UniparcSequences,
    UniparcMiscellaneous,
    UniparcDateOf,
    UniparcFamilyDomains,
]
