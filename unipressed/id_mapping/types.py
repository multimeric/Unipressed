from typing import Iterable, Optional

from typing_extensions import Literal, overload


class SubmitDummyClass:
    @classmethod
    @overload
    def submit(
        cls,
        source: Literal["UniProtKB_AC-ID",],
        dest: Literal[
            "CCDS",
            "PIR",
            "PDB",
            "BioGRID",
            "ComplexPortal",
            "DIP",
            "STRING",
            "ChEMBL",
            "DrugBank",
            "GuidetoPHARMACOLOGY",
            "SwissLipids",
            "Allergome",
            "ESTHER",
            "MEROPS",
            "PeroxiBase",
            "REBASE",
            "TCDB",
            "GlyConnect",
            "BioMuta",
            "DMDM",
            "CPTAC",
            "ProteomicsDB",
            "DNASU",
            "Ensembl",
            "GeneID",
            "KEGG",
            "PATRIC",
            "UCSC",
            "WBParaSite",
            "ArachnoServer",
            "Araport",
            "CGD",
            "ConoServer",
            "dictyBase",
            "EchoBASE",
            "euHCVdb",
            "VEuPathDB",
            "FlyBase",
            "GeneCards",
            "GeneReviews",
            "HGNC",
            "LegioList",
            "Leproma",
            "MaizeGDB",
            "MGI",
            "MIM",
            "neXtProt",
            "OpenTargets",
            "Orphanet",
            "PharmGKB",
            "PomBase",
            "PseudoCAP",
            "RGD",
            "SGD",
            "TubercuList",
            "VGNC",
            "WormBase",
            "Xenbase",
            "ZFIN",
            "eggNOG",
            "GeneTree",
            "HOGENOM",
            "OMA",
            "OrthoDB",
            "TreeFam",
            "BioCyc",
            "Reactome",
            "UniPathway",
            "PlantReactome",
            "ChiTaRS",
            "GeneWiki",
            "GenomeRNAi",
            "PHI-base",
            "CollecTF",
            "IDEAL",
            "DisProt",
            "UniProtKB",
            "UniProtKB-Swiss-Prot",
            "UniParc",
            "UniRef50",
            "UniRef90",
            "UniRef100",
            "Gene_Name",
            "CRC64",
            "EMBL-GenBank-DDBJ",
            "EMBL-GenBank-DDBJ_CDS",
            "GI_number",
            "RefSeq_Nucleotide",
            "RefSeq_Protein",
            "Ensembl_Protein",
            "Ensembl_Transcript",
            "Ensembl_Genomes",
            "Ensembl_Genomes_Protein",
            "Ensembl_Genomes_Transcript",
            "WBParaSite_Transcript-Protein",
            "WormBase_Protein",
            "WormBase_Transcript",
        ],
        ids: Iterable[str],
    ):
        ...

    @classmethod
    @overload
    def submit(
        cls,
        source: Literal["UniParc",],
        dest: Literal["UniProtKB", "UniProtKB-Swiss-Prot", "UniParc"],
        ids: Iterable[str],
    ):
        ...

    @classmethod
    @overload
    def submit(
        cls,
        source: Literal["UniRef50",],
        dest: Literal["UniProtKB", "UniProtKB-Swiss-Prot", "UniRef50"],
        ids: Iterable[str],
    ):
        ...

    @classmethod
    @overload
    def submit(
        cls,
        source: Literal["UniRef90",],
        dest: Literal["UniProtKB", "UniProtKB-Swiss-Prot", "UniRef90"],
        ids: Iterable[str],
    ):
        ...

    @classmethod
    @overload
    def submit(
        cls,
        source: Literal["UniRef100",],
        dest: Literal["UniProtKB", "UniProtKB-Swiss-Prot", "UniRef100"],
        ids: Iterable[str],
    ):
        ...

    @classmethod
    @overload
    def submit(
        cls,
        source: Literal["Gene_Name",],
        dest: Literal["UniProtKB", "UniProtKB-Swiss-Prot"],
        ids: Iterable[str],
        taxon_id: Optional[int] = None,
    ):
        ...

    @classmethod
    @overload
    def submit(
        cls,
        source: Literal[
            "CRC64",
            "CCDS",
            "EMBL-GenBank-DDBJ",
            "EMBL-GenBank-DDBJ_CDS",
            "GI_number",
            "PIR",
            "RefSeq_Nucleotide",
            "RefSeq_Protein",
            "PDB",
            "BioGRID",
            "ComplexPortal",
            "DIP",
            "STRING",
            "ChEMBL",
            "DrugBank",
            "GuidetoPHARMACOLOGY",
            "SwissLipids",
            "Allergome",
            "ESTHER",
            "MEROPS",
            "PeroxiBase",
            "REBASE",
            "TCDB",
            "GlyConnect",
            "BioMuta",
            "DMDM",
            "CPTAC",
            "ProteomicsDB",
            "DNASU",
            "Ensembl",
            "Ensembl_Genomes",
            "Ensembl_Genomes_Protein",
            "Ensembl_Genomes_Transcript",
            "Ensembl_Protein",
            "Ensembl_Transcript",
            "GeneID",
            "KEGG",
            "PATRIC",
            "UCSC",
            "WBParaSite",
            "WBParaSite_Transcript-Protein",
            "ArachnoServer",
            "Araport",
            "CGD",
            "ConoServer",
            "dictyBase",
            "EchoBASE",
            "euHCVdb",
            "FlyBase",
            "GeneCards",
            "GeneReviews",
            "HGNC",
            "LegioList",
            "Leproma",
            "MaizeGDB",
            "MGI",
            "MIM",
            "neXtProt",
            "OpenTargets",
            "Orphanet",
            "PharmGKB",
            "PomBase",
            "PseudoCAP",
            "RGD",
            "SGD",
            "TubercuList",
            "VEuPathDB",
            "VGNC",
            "WormBase",
            "WormBase_Protein",
            "WormBase_Transcript",
            "Xenbase",
            "ZFIN",
            "eggNOG",
            "GeneTree",
            "HOGENOM",
            "OMA",
            "OrthoDB",
            "TreeFam",
            "BioCyc",
            "PlantReactome",
            "Reactome",
            "UniPathway",
            "ChiTaRS",
            "GeneWiki",
            "GenomeRNAi",
            "PHI-base",
            "CollecTF",
            "DisProt",
            "IDEAL",
        ],
        dest: Literal["UniProtKB", "UniProtKB-Swiss-Prot"],
        ids: Iterable[str],
    ):
        ...

    @classmethod
    def submit(
        cls, source: str, dest: str, ids: Iterable[str], taxon_id: Optional[int] = None
    ):
        ...
