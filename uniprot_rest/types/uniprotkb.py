from typing import Union
from typing_extensions import TypeAlias, Literal, TypedDict, NotRequired
from dataclasses import dataclass, field
from datetime import date
import uniprot_rest

Existence: TypeAlias = Literal["1", "2", "3", "4", "5"]
ccevCofactorChebiEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevCofactorChebi(TypedDict):
    query: str
    evidence: ccevCofactorChebiEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevCofactorNoteEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevCofactorNote(TypedDict):
    query: str
    evidence: ccevCofactorNoteEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevBpcpEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevBpcp(TypedDict):
    query: str
    evidence: ccevBpcpEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevBpcpAbsorptionEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevBpcpAbsorption(TypedDict):
    query: str
    evidence: ccevBpcpAbsorptionEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevBpcpKineticsEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevBpcpKinetics(TypedDict):
    query: str
    evidence: ccevBpcpKineticsEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevBpcpPhDependenceEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevBpcpPhDependence(TypedDict):
    query: str
    evidence: ccevBpcpPhDependenceEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevBpcpRedoxPotentialEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevBpcpRedoxPotential(TypedDict):
    query: str
    evidence: ccevBpcpRedoxPotentialEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevBpcpTempDependenceEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevBpcpTempDependence(TypedDict):
    query: str
    evidence: ccevBpcpTempDependenceEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevCatalyticActivityEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevCatalyticActivity(TypedDict):
    query: str
    evidence: ccevCatalyticActivityEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevActivityRegulationEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevActivityRegulation(TypedDict):
    query: str
    evidence: ccevActivityRegulationEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevFunctionEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevFunction(TypedDict):
    query: str
    evidence: ccevFunctionEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevCautionEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevCaution(TypedDict):
    query: str
    evidence: ccevCautionEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevSitesEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevSites(TypedDict):
    query: str
    evidence: ftevSitesEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevActSiteEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevActSite(TypedDict):
    query: str
    evidence: ftevActSiteEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevMetalEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevMetal(TypedDict):
    query: str
    evidence: ftevMetalEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevBindingEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevBinding(TypedDict):
    query: str
    evidence: ftevBindingEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevSiteEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevSite(TypedDict):
    query: str
    evidence: ftevSiteEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevCaBindEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevCaBind(TypedDict):
    query: str
    evidence: ftevCaBindEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevDnaBindEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevDnaBind(TypedDict):
    query: str
    evidence: ftevDnaBindEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevNpBindEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevNpBind(TypedDict):
    query: str
    evidence: ftevNpBindEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevPathwayEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevPathway(TypedDict):
    query: str
    evidence: ccevPathwayEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevMiscellaneousEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevMiscellaneous(TypedDict):
    query: str
    evidence: ccevMiscellaneousEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevSclTermEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevSclTerm(TypedDict):
    query: str
    evidence: ccevSclTermEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevSclNoteEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevSclNote(TypedDict):
    query: str
    evidence: ccevSclNoteEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevTransmemEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevTransmem(TypedDict):
    query: str
    evidence: ftevTransmemEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevTopoDomEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevTopoDom(TypedDict):
    query: str
    evidence: ftevTopoDomEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevIntramemEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevIntramem(TypedDict):
    query: str
    evidence: ftevIntramemEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevDiseaseEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevDisease(TypedDict):
    query: str
    evidence: ccevDiseaseEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevAllergenEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevAllergen(TypedDict):
    query: str
    evidence: ccevAllergenEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevToxicDoseEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevToxicDose(TypedDict):
    query: str
    evidence: ccevToxicDoseEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevBiotechnologyEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevBiotechnology(TypedDict):
    query: str
    evidence: ccevBiotechnologyEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevPharmaceuticalEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevPharmaceutical(TypedDict):
    query: str
    evidence: ccevPharmaceuticalEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevDisruptionPhenotypeEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevDisruptionPhenotype(TypedDict):
    query: str
    evidence: ccevDisruptionPhenotypeEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevMutagenEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevMutagen(TypedDict):
    query: str
    evidence: ftevMutagenEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevPtmEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevPtm(TypedDict):
    query: str
    evidence: ccevPtmEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevModResEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevModRes(TypedDict):
    query: str
    evidence: ftevModResEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevLipidEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevLipid(TypedDict):
    query: str
    evidence: ftevLipidEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevCarbohydEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevCarbohyd(TypedDict):
    query: str
    evidence: ftevCarbohydEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevDisulfidEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevDisulfid(TypedDict):
    query: str
    evidence: ftevDisulfidEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevCrosslnkEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevCrosslnk(TypedDict):
    query: str
    evidence: ftevCrosslnkEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevMoleculeProcessingEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevMoleculeProcessing(TypedDict):
    query: str
    evidence: ftevMoleculeProcessingEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevChainEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevChain(TypedDict):
    query: str
    evidence: ftevChainEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevInitMetEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevInitMet(TypedDict):
    query: str
    evidence: ftevInitMetEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevPeptideEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevPeptide(TypedDict):
    query: str
    evidence: ftevPeptideEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevSignalEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevSignal(TypedDict):
    query: str
    evidence: ftevSignalEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevPropepEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevPropep(TypedDict):
    query: str
    evidence: ftevPropepEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevTransitEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevTransit(TypedDict):
    query: str
    evidence: ftevTransitEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevDevelopmentalStageEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevDevelopmentalStage(TypedDict):
    query: str
    evidence: ccevDevelopmentalStageEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevInductionEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevInduction(TypedDict):
    query: str
    evidence: ccevInductionEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevTissueSpecificityEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevTissueSpecificity(TypedDict):
    query: str
    evidence: ccevTissueSpecificityEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevSubunitEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevSubunit(TypedDict):
    query: str
    evidence: ccevSubunitEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevSecstructEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevSecstruct(TypedDict):
    query: str
    evidence: ftevSecstructEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevHelixEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevHelix(TypedDict):
    query: str
    evidence: ftevHelixEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevTurnEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevTurn(TypedDict):
    query: str
    evidence: ftevTurnEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevStrandEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevStrand(TypedDict):
    query: str
    evidence: ftevStrandEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevApEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevAp(TypedDict):
    query: str
    evidence: ccevApEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevApApuEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevApApu(TypedDict):
    query: str
    evidence: ccevApApuEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevApAsEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevApAs(TypedDict):
    query: str
    evidence: ccevApAsEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevApAiEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevApAi(TypedDict):
    query: str
    evidence: ccevApAiEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevApRfEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevApRf(TypedDict):
    query: str
    evidence: ccevApRfEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevSequenceCautionEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevSequenceCaution(TypedDict):
    query: str
    evidence: ccevSequenceCautionEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevScMiscEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevScMisc(TypedDict):
    query: str
    evidence: ccevScMiscEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevMassSpectrometryEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevMassSpectrometry(TypedDict):
    query: str
    evidence: ccevMassSpectrometryEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevPolymorphismEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevPolymorphism(TypedDict):
    query: str
    evidence: ccevPolymorphismEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevRnaEditingEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevRnaEditing(TypedDict):
    query: str
    evidence: ccevRnaEditingEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevVariantsEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevVariants(TypedDict):
    query: str
    evidence: ftevVariantsEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevVariantEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevVariant(TypedDict):
    query: str
    evidence: ftevVariantEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevVarSeqEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevVarSeq(TypedDict):
    query: str
    evidence: ftevVarSeqEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevNonStdEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevNonStd(TypedDict):
    query: str
    evidence: ftevNonStdEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevNonTerEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevNonTer(TypedDict):
    query: str
    evidence: ftevNonTerEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevNonConsEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevNonCons(TypedDict):
    query: str
    evidence: ftevNonConsEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevConflictEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevConflict(TypedDict):
    query: str
    evidence: ftevConflictEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevUnsureEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevUnsure(TypedDict):
    query: str
    evidence: ftevUnsureEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevPositionalEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevPositional(TypedDict):
    query: str
    evidence: ftevPositionalEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


Organelle: TypeAlias = Literal[
    "mitochondrion",
    "plastid",
    "chloroplast",
    "cyanelle",
    "apicoplast",
    "organellar chromatophore",
    "non-photosynthetic plastid",
    "nucleomorph",
    "hydrogenosome",
]
ftevDomainEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevDomain(TypedDict):
    query: str
    evidence: ftevDomainEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevDomainEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevDomain(TypedDict):
    query: str
    evidence: ccevDomainEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevCoiledEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevCoiled(TypedDict):
    query: str
    evidence: ftevCoiledEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevCompbiasEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevCompbias(TypedDict):
    query: str
    evidence: ftevCompbiasEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevMotifEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevMotif(TypedDict):
    query: str
    evidence: ftevMotifEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevRegionEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevRegion(TypedDict):
    query: str
    evidence: ftevRegionEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevRepeatEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevRepeat(TypedDict):
    query: str
    evidence: ftevRepeatEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevSimilarityEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevSimilarity(TypedDict):
    query: str
    evidence: ccevSimilarityEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ftevZnFingEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ftevZnFing(TypedDict):
    query: str
    evidence: ftevZnFingEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


ccevWebresourceEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "experimental",
    "ECO_0000269",
    "ECO_0000303",
    "ECO_0000305",
    "ECO_0000250",
    "ECO_0000255",
    "ECO_0000244",
    "ECO_0000312",
    "ECO_0000256",
    "ECO_0000213",
    "ECO_0000313",
    "ECO_0000259",
]


class ccevWebresource(TypedDict):
    query: str
    evidence: ccevWebresourceEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexperimental: Any experimental assertion\nECO_0000269: Experimental\nECO_0000303: Non-traceable author statement\nECO_0000305: Curator inference\nECO_0000250: Sequence similarity\nECO_0000255: Sequence model\nECO_0000244: Combinatorial\nECO_0000312: Imported information\nECO_0000256: Sequence model\nECO_0000213: Combinatorial\nECO_0000313: Imported information\nECO_0000259: Sequence motif match (InterPro)"


goEvidenceEvidence: TypeAlias = Literal[
    "any",
    "manual",
    "automatic",
    "exp",
    "iba",
    "ic",
    "ida",
    "iep",
    "igc",
    "igi",
    "imp",
    "ipi",
    "isa",
    "ism",
    "iso",
    "iss",
    "nas",
    "tas",
    "hda",
    "hmp",
    "hgi",
    "hep",
    "htp",
    "iea",
]


class goEvidence(TypedDict):
    query: str
    evidence: goEvidenceEvidence
    "any: Any assertion method\nmanual: Any manual assertion\nautomatic: Any automatic assertion\nexp: Inferred from experiment [EXP]\niba: Inferred from biological aspect of ancestor [IBA]\nic: Inferred by curator [IC]\nida: Inferred from direct assay [IDA]\niep: Inferred from expression pattern [IEP]\nigc: Inferred from genomic context [IGC]\nigi: Inferred from genetic interaction [IGI]\nimp: Inferred from mutant phenotype [IMP]\nipi: Inferred from physical interaction [IPI]\nisa: Inferred from sequence alignment [ISA]\nism: Inferred from sequence mode [ISM]\niso: Inferred from sequence orthology [ISO]\niss: Inferred from sequence or structural similarity [ISS]\nnas: Non-traceable author statement [NAS]\ntas: Traceable author statement [TAS]\nhda: Inferred from high throughput direct assay [HDA]\nhmp: Inferred from high throughput mutant phenotype [HMP]\nhgi: Inferred from high throughput genetic interaction [HGI]\nhep: Interred from high throughput expression pattern [HEP]\nhtp: Inferred from high throughput experiment [HTP]\niea: Inferred from electronic annotation [IEA]"


UniprotkbQuery: TypeAlias = TypedDict(
    "UniprotkbQuery",
    {
        "and": Iterable[UniprotkbQuery],
        "or": Iterable[UniprotkbQuery],
        "accession_field": NotRequired[str],
        "id_field": NotRequired[str],
        "protein_name_field": NotRequired[str],
        "gene_field": NotRequired[str],
        "organism_name_field": NotRequired[str],
        "taxonomy_name": NotRequired[str],
        "virus_host_name": NotRequired[str],
        "existence": NotRequired[Existence],
        "ec": NotRequired[str],
        "cc_cofactor_chebi": NotRequired[str],
        "ccev_cofactor_chebi": NotRequired[ccevCofactorChebi],
        "cc_cofactor_note": NotRequired[str],
        "ccev_cofactor_note": NotRequired[ccevCofactorNote],
        "cc_bpcp": NotRequired[str],
        "ccev_bpcp": NotRequired[ccevBpcp],
        "cc_bpcp_absorption": NotRequired[str],
        "ccev_bpcp_absorption": NotRequired[ccevBpcpAbsorption],
        "cc_bpcp_kinetics": NotRequired[str],
        "ccev_bpcp_kinetics": NotRequired[ccevBpcpKinetics],
        "cc_bpcp_ph_dependence": NotRequired[str],
        "ccev_bpcp_ph_dependence": NotRequired[ccevBpcpPhDependence],
        "cc_bpcp_redox_potential": NotRequired[str],
        "ccev_bpcp_redox_potential": NotRequired[ccevBpcpRedoxPotential],
        "cc_bpcp_temp_dependence": NotRequired[str],
        "ccev_bpcp_temp_dependence": NotRequired[ccevBpcpTempDependence],
        "cc_catalytic_activity_field": NotRequired[str],
        "ccev_catalytic_activity": NotRequired[ccevCatalyticActivity],
        "cc_activity_regulation": NotRequired[str],
        "ccev_activity_regulation": NotRequired[ccevActivityRegulation],
        "cc_function": NotRequired[str],
        "ccev_function": NotRequired[ccevFunction],
        "cc_caution": NotRequired[str],
        "ccev_caution": NotRequired[ccevCaution],
        "ft_sites": NotRequired[str],
        "ftlen_sites": NotRequired[tuple[int, int]],
        "ftev_sites": NotRequired[ftevSites],
        "ft_act_site": NotRequired[str],
        "ftlen_act_site": NotRequired[tuple[int, int]],
        "ftev_act_site": NotRequired[ftevActSite],
        "ft_metal": NotRequired[str],
        "ftlen_metal": NotRequired[tuple[int, int]],
        "ftev_metal": NotRequired[ftevMetal],
        "ft_binding": NotRequired[str],
        "ftlen_binding": NotRequired[tuple[int, int]],
        "ftev_binding": NotRequired[ftevBinding],
        "ft_site": NotRequired[str],
        "ftlen_site": NotRequired[tuple[int, int]],
        "ftev_site": NotRequired[ftevSite],
        "ft_ca_bind": NotRequired[str],
        "ftlen_ca_bind": NotRequired[tuple[int, int]],
        "ftev_ca_bind": NotRequired[ftevCaBind],
        "ft_dna_bind": NotRequired[str],
        "ftlen_dna_bind": NotRequired[tuple[int, int]],
        "ftev_dna_bind": NotRequired[ftevDnaBind],
        "ft_np_bind": NotRequired[str],
        "ftlen_np_bind": NotRequired[tuple[int, int]],
        "ftev_np_bind": NotRequired[ftevNpBind],
        "cc_pathway": NotRequired[str],
        "ccev_pathway": NotRequired[ccevPathway],
        "cc_miscellaneous": NotRequired[str],
        "ccev_miscellaneous": NotRequired[ccevMiscellaneous],
        "cc_scl_term_field": NotRequired[str],
        "ccev_scl_term": NotRequired[ccevSclTerm],
        "cc_scl_note": NotRequired[str],
        "ccev_scl_note": NotRequired[ccevSclNote],
        "ft_transmem": NotRequired[str],
        "ftlen_transmem": NotRequired[tuple[int, int]],
        "ftev_transmem": NotRequired[ftevTransmem],
        "ft_topo_dom": NotRequired[str],
        "ftlen_topo_dom": NotRequired[tuple[int, int]],
        "ftev_topo_dom": NotRequired[ftevTopoDom],
        "ft_intramem": NotRequired[str],
        "ftlen_intramem": NotRequired[tuple[int, int]],
        "ftev_intramem": NotRequired[ftevIntramem],
        "cc_disease": NotRequired[str],
        "ccev_disease": NotRequired[ccevDisease],
        "cc_allergen": NotRequired[str],
        "ccev_allergen": NotRequired[ccevAllergen],
        "cc_toxic_dose": NotRequired[str],
        "ccev_toxic_dose": NotRequired[ccevToxicDose],
        "cc_biotechnology": NotRequired[str],
        "ccev_biotechnology": NotRequired[ccevBiotechnology],
        "cc_pharmaceutical": NotRequired[str],
        "ccev_pharmaceutical": NotRequired[ccevPharmaceutical],
        "cc_disruption_phenotype": NotRequired[str],
        "ccev_disruption_phenotype": NotRequired[ccevDisruptionPhenotype],
        "ft_mutagen": NotRequired[str],
        "ftlen_mutagen": NotRequired[tuple[int, int]],
        "ftev_mutagen": NotRequired[ftevMutagen],
        "cc_ptm": NotRequired[str],
        "ccev_ptm": NotRequired[ccevPtm],
        "ft_mod_res": NotRequired[str],
        "ftlen_mod_res": NotRequired[tuple[int, int]],
        "ftev_mod_res": NotRequired[ftevModRes],
        "ft_lipid": NotRequired[str],
        "ftlen_lipid": NotRequired[tuple[int, int]],
        "ftev_lipid": NotRequired[ftevLipid],
        "ft_carbohyd": NotRequired[str],
        "ftlen_carbohyd": NotRequired[tuple[int, int]],
        "ftev_carbohyd": NotRequired[ftevCarbohyd],
        "ft_disulfid": NotRequired[str],
        "ftlen_disulfid": NotRequired[tuple[int, int]],
        "ftev_disulfid": NotRequired[ftevDisulfid],
        "ft_crosslnk": NotRequired[str],
        "ftlen_crosslnk": NotRequired[tuple[int, int]],
        "ftev_crosslnk": NotRequired[ftevCrosslnk],
        "ft_molecule_processing": NotRequired[str],
        "ftlen_molecule_processing": NotRequired[tuple[int, int]],
        "ftev_molecule_processing": NotRequired[ftevMoleculeProcessing],
        "ft_chain": NotRequired[str],
        "ftlen_chain": NotRequired[tuple[int, int]],
        "ftev_chain": NotRequired[ftevChain],
        "ft_init_met": NotRequired[str],
        "ftlen_init_met": NotRequired[tuple[int, int]],
        "ftev_init_met": NotRequired[ftevInitMet],
        "ft_peptide": NotRequired[str],
        "ftlen_peptide": NotRequired[tuple[int, int]],
        "ftev_peptide": NotRequired[ftevPeptide],
        "ft_signal": NotRequired[str],
        "ftlen_signal": NotRequired[tuple[int, int]],
        "ftev_signal": NotRequired[ftevSignal],
        "ft_propep": NotRequired[str],
        "ftlen_propep": NotRequired[tuple[int, int]],
        "ftev_propep": NotRequired[ftevPropep],
        "ft_transit": NotRequired[str],
        "ftlen_transit": NotRequired[tuple[int, int]],
        "ftev_transit": NotRequired[ftevTransit],
        "cc_developmental_stage": NotRequired[str],
        "ccev_developmental_stage": NotRequired[ccevDevelopmentalStage],
        "cc_induction": NotRequired[str],
        "ccev_induction": NotRequired[ccevInduction],
        "cc_tissue_specificity": NotRequired[str],
        "ccev_tissue_specificity": NotRequired[ccevTissueSpecificity],
        "interactor": NotRequired[str],
        "cc_subunit": NotRequired[str],
        "ccev_subunit": NotRequired[ccevSubunit],
        "structure_3d": NotRequired[bool],
        "ft_secstruct": NotRequired[str],
        "ftlen_secstruct": NotRequired[tuple[int, int]],
        "ftev_secstruct": NotRequired[ftevSecstruct],
        "ft_helix": NotRequired[str],
        "ftlen_helix": NotRequired[tuple[int, int]],
        "ftev_helix": NotRequired[ftevHelix],
        "ft_turn": NotRequired[str],
        "ftlen_turn": NotRequired[tuple[int, int]],
        "ftev_turn": NotRequired[ftevTurn],
        "ft_strand": NotRequired[str],
        "ftlen_strand": NotRequired[tuple[int, int]],
        "ftev_strand": NotRequired[ftevStrand],
        "mass_range": NotRequired[tuple[int, int]],
        "length_range": NotRequired[tuple[int, int]],
        "cc_ap": NotRequired[str],
        "ccev_ap": NotRequired[ccevAp],
        "cc_ap_apu": NotRequired[str],
        "ccev_ap_apu": NotRequired[ccevApApu],
        "cc_ap_as": NotRequired[str],
        "ccev_ap_as": NotRequired[ccevApAs],
        "cc_ap_ai": NotRequired[str],
        "ccev_ap_ai": NotRequired[ccevApAi],
        "cc_ap_rf": NotRequired[str],
        "ccev_ap_rf": NotRequired[ccevApRf],
        "cc_sequence_caution": NotRequired[str],
        "ccev_sequence_caution": NotRequired[ccevSequenceCaution],
        "cc_sc_framesh": NotRequired[str],
        "cc_sc_einit": NotRequired[str],
        "cc_sc_eterm": NotRequired[str],
        "cc_sc_epred": NotRequired[str],
        "cc_sc_etran": NotRequired[str],
        "cc_sc_misc": NotRequired[str],
        "ccev_sc_misc": NotRequired[ccevScMisc],
        "cc_mass_spectrometry": NotRequired[str],
        "ccev_mass_spectrometry": NotRequired[ccevMassSpectrometry],
        "cc_polymorphism": NotRequired[str],
        "ccev_polymorphism": NotRequired[ccevPolymorphism],
        "cc_rna_editing": NotRequired[str],
        "ccev_rna_editing": NotRequired[ccevRnaEditing],
        "ft_variants": NotRequired[str],
        "ftlen_variants": NotRequired[tuple[int, int]],
        "ftev_variants": NotRequired[ftevVariants],
        "ft_variant": NotRequired[str],
        "ftlen_variant": NotRequired[tuple[int, int]],
        "ftev_variant": NotRequired[ftevVariant],
        "ft_var_seq": NotRequired[str],
        "ftlen_var_seq": NotRequired[tuple[int, int]],
        "ftev_var_seq": NotRequired[ftevVarSeq],
        "ft_non_std": NotRequired[str],
        "ftlen_non_std": NotRequired[tuple[int, int]],
        "ftev_non_std": NotRequired[ftevNonStd],
        "ft_non_ter": NotRequired[str],
        "ftlen_non_ter": NotRequired[tuple[int, int]],
        "ftev_non_ter": NotRequired[ftevNonTer],
        "ft_non_cons": NotRequired[str],
        "ftlen_non_cons": NotRequired[tuple[int, int]],
        "ftev_non_cons": NotRequired[ftevNonCons],
        "ft_conflict": NotRequired[str],
        "ftlen_conflict": NotRequired[tuple[int, int]],
        "ftev_conflict": NotRequired[ftevConflict],
        "ft_unsure": NotRequired[str],
        "ftlen_unsure": NotRequired[tuple[int, int]],
        "ftev_unsure": NotRequired[ftevUnsure],
        "ft_positional": NotRequired[str],
        "ftlen_positional": NotRequired[tuple[int, int]],
        "ftev_positional": NotRequired[ftevPositional],
        "fragment": NotRequired[bool],
        "organelle": NotRequired[Organelle],
        "precursor": NotRequired[bool],
        "tissue": NotRequired[str],
        "strain": NotRequired[str],
        "plasmid": NotRequired[str],
        "transposon": NotRequired[str],
        "ft_domain": NotRequired[str],
        "ftlen_domain": NotRequired[tuple[int, int]],
        "ftev_domain": NotRequired[ftevDomain],
        "cc_domain": NotRequired[str],
        "ccev_domain": NotRequired[ccevDomain],
        "family": NotRequired[str],
        "ft_coiled": NotRequired[str],
        "ftlen_coiled": NotRequired[tuple[int, int]],
        "ftev_coiled": NotRequired[ftevCoiled],
        "ft_compbias": NotRequired[str],
        "ftlen_compbias": NotRequired[tuple[int, int]],
        "ftev_compbias": NotRequired[ftevCompbias],
        "ft_motif": NotRequired[str],
        "ftlen_motif": NotRequired[tuple[int, int]],
        "ftev_motif": NotRequired[ftevMotif],
        "ft_region": NotRequired[str],
        "ftlen_region": NotRequired[tuple[int, int]],
        "ftev_region": NotRequired[ftevRegion],
        "ft_repeat": NotRequired[str],
        "ftlen_repeat": NotRequired[tuple[int, int]],
        "ftev_repeat": NotRequired[ftevRepeat],
        "cc_similarity": NotRequired[str],
        "ccev_similarity": NotRequired[ccevSimilarity],
        "ft_zn_fing": NotRequired[str],
        "ftlen_zn_fing": NotRequired[tuple[int, int]],
        "ftev_zn_fing": NotRequired[ftevZnFing],
        "xref_any": NotRequired[str],
        "xref_embl": NotRequired[str],
        "xref_ccds": NotRequired[str],
        "xref_pir": NotRequired[str],
        "xref_refseq": NotRequired[str],
        "xref_pdb": NotRequired[str],
        "xref_pdbsum": NotRequired[str],
        "xref_pcddb": NotRequired[str],
        "xref_sasbdb": NotRequired[str],
        "xref_bmrb": NotRequired[str],
        "xref_smr": NotRequired[str],
        "xref_alphafolddb": NotRequired[str],
        "xref_biogrid": NotRequired[str],
        "xref_complexportal": NotRequired[str],
        "xref_corum": NotRequired[str],
        "xref_dip": NotRequired[str],
        "xref_elm": NotRequired[str],
        "xref_intact": NotRequired[str],
        "xref_mint": NotRequired[str],
        "xref_string": NotRequired[str],
        "xref_bindingdb": NotRequired[str],
        "xref_chembl": NotRequired[str],
        "xref_drugbank": NotRequired[str],
        "xref_guidetopharmacology": NotRequired[str],
        "xref_swisslipids": NotRequired[str],
        "xref_drugcentral": NotRequired[str],
        "xref_allergome": NotRequired[str],
        "xref_cazy": NotRequired[str],
        "xref_esther": NotRequired[str],
        "xref_imgt_gene-db": NotRequired[str],
        "xref_merops": NotRequired[str],
        "xref_moondb": NotRequired[str],
        "xref_moonprot": NotRequired[str],
        "xref_clae": NotRequired[str],
        "xref_peroxibase": NotRequired[str],
        "xref_rebase": NotRequired[str],
        "xref_tcdb": NotRequired[str],
        "xref_unilectin": NotRequired[str],
        "xref_carbonyldb": NotRequired[str],
        "xref_depod": NotRequired[str],
        "xref_glyconnect": NotRequired[str],
        "xref_glygen": NotRequired[str],
        "xref_iptmnet": NotRequired[str],
        "xref_phosphositeplus": NotRequired[str],
        "xref_swisspalm": NotRequired[str],
        "xref_unicarbkb": NotRequired[str],
        "xref_metosite": NotRequired[str],
        "xref_biomuta": NotRequired[str],
        "xref_dmdm": NotRequired[str],
        "xref_dbsnp": NotRequired[str],
        "xref_compluyeast-2dpage": NotRequired[str],
        "xref_dosac-cobs-2dpage": NotRequired[str],
        "xref_ogp": NotRequired[str],
        "xref_reproduction-2dpage": NotRequired[str],
        "xref_swiss-2dpage": NotRequired[str],
        "xref_ucd-2dpage": NotRequired[str],
        "xref_world-2dpage": NotRequired[str],
        "xref_cptac": NotRequired[str],
        "xref_epd": NotRequired[str],
        "xref_maxqb": NotRequired[str],
        "xref_paxdb": NotRequired[str],
        "xref_peptideatlas": NotRequired[str],
        "xref_pride": NotRequired[str],
        "xref_promex": NotRequired[str],
        "xref_proteomicsdb": NotRequired[str],
        "xref_topdownproteomics": NotRequired[str],
        "xref_jpost": NotRequired[str],
        "xref_massive": NotRequired[str],
        "xref_dnasu": NotRequired[str],
        "xref_abcd": NotRequired[str],
        "xref_antibodypedia": NotRequired[str],
        "xref_cptc": NotRequired[str],
        "xref_ensembl": NotRequired[str],
        "xref_ensemblbacteria": NotRequired[str],
        "xref_ensemblfungi": NotRequired[str],
        "xref_ensemblmetazoa": NotRequired[str],
        "xref_ensemblplants": NotRequired[str],
        "xref_ensemblprotists": NotRequired[str],
        "xref_geneid": NotRequired[str],
        "xref_gramene": NotRequired[str],
        "xref_kegg": NotRequired[str],
        "xref_mane-select": NotRequired[str],
        "xref_patric": NotRequired[str],
        "xref_ucsc": NotRequired[str],
        "xref_vectorbase": NotRequired[str],
        "xref_wbparasite": NotRequired[str],
        "xref_wbparasitetranscriptprotein": NotRequired[str],
        "xref_arachnoserver": NotRequired[str],
        "xref_araport": NotRequired[str],
        "xref_cgd": NotRequired[str],
        "xref_conoserver": NotRequired[str],
        "xref_ctd": NotRequired[str],
        "xref_dictybase": NotRequired[str],
        "xref_disgenet": NotRequired[str],
        "xref_echobase": NotRequired[str],
        "xref_euhcvdb": NotRequired[str],
        "xref_veupathdb": NotRequired[str],
        "xref_flybase": NotRequired[str],
        "xref_genecards": NotRequired[str],
        "xref_genereviews": NotRequired[str],
        "xref_hgnc": NotRequired[str],
        "xref_hpa": NotRequired[str],
        "xref_legiolist": NotRequired[str],
        "xref_leproma": NotRequired[str],
        "xref_maizegdb": NotRequired[str],
        "xref_malacards": NotRequired[str],
        "xref_mgi": NotRequired[str],
        "xref_mim": NotRequired[str],
        "xref_niagads": NotRequired[str],
        "xref_nextprot": NotRequired[str],
        "xref_opentargets": NotRequired[str],
        "xref_orphanet": NotRequired[str],
        "xref_pharmgkb": NotRequired[str],
        "xref_pombase": NotRequired[str],
        "xref_pseudocap": NotRequired[str],
        "xref_rgd": NotRequired[str],
        "xref_sgd": NotRequired[str],
        "xref_tair": NotRequired[str],
        "xref_tuberculist": NotRequired[str],
        "xref_vgnc": NotRequired[str],
        "xref_wormbase": NotRequired[str],
        "xref_xenbase": NotRequired[str],
        "xref_zfin": NotRequired[str],
        "xref_eggnog": NotRequired[str],
        "xref_genetree": NotRequired[str],
        "xref_hogenom": NotRequired[str],
        "xref_inparanoid": NotRequired[str],
        "xref_ko": NotRequired[str],
        "xref_oma": NotRequired[str],
        "xref_orthodb": NotRequired[str],
        "xref_phylomedb": NotRequired[str],
        "xref_treefam": NotRequired[str],
        "xref_biocyc": NotRequired[str],
        "xref_brenda": NotRequired[str],
        "xref_reactome": NotRequired[str],
        "xref_sabio-rk": NotRequired[str],
        "xref_signalink": NotRequired[str],
        "xref_signor": NotRequired[str],
        "xref_unipathway": NotRequired[str],
        "xref_plantreactome": NotRequired[str],
        "xref_pathwaycommons": NotRequired[str],
        "xref_chitars": NotRequired[str],
        "xref_evolutionarytrace": NotRequired[str],
        "xref_genewiki": NotRequired[str],
        "xref_genomernai": NotRequired[str],
        "xref_phi-base": NotRequired[str],
        "xref_pro": NotRequired[str],
        "xref_pharos": NotRequired[str],
        "xref_rnact": NotRequired[str],
        "xref_biogrid-orcs": NotRequired[str],
        "xref_bgee": NotRequired[str],
        "xref_cleanex": NotRequired[str],
        "xref_collectf": NotRequired[str],
        "xref_expressionatlas": NotRequired[str],
        "xref_genevisible": NotRequired[str],
        "xref_cdd": NotRequired[str],
        "xref_gene3d": NotRequired[str],
        "xref_hamap": NotRequired[str],
        "xref_ideal": NotRequired[str],
        "xref_interpro": NotRequired[str],
        "xref_panther": NotRequired[str],
        "xref_pfam": NotRequired[str],
        "xref_pirsf": NotRequired[str],
        "xref_prints": NotRequired[str],
        "xref_prodom": NotRequired[str],
        "xref_sfld": NotRequired[str],
        "xref_smart": NotRequired[str],
        "xref_supfam": NotRequired[str],
        "xref_tigrfams": NotRequired[str],
        "xref_prosite": NotRequired[str],
        "xref_disprot": NotRequired[str],
        "xref_go": NotRequired[str],
        "xref_proteomes": NotRequired[str],
        "database": NotRequired[str],
        "cc_webresource": NotRequired[str],
        "ccev_webresource": NotRequired[ccevWebresource],
        "date_created": NotRequired[tuple[date, date]],
        "date_modified": NotRequired[tuple[date, date]],
        "date_sequence_modified": NotRequired[tuple[date, date]],
        "go_field": NotRequired[str],
        "go_evidence": NotRequired[goEvidence],
        "chebi_field": NotRequired[str],
        "inchikey_field": NotRequired[str],
        "keyword_field": NotRequired[str],
        "lit_author": NotRequired[str],
        "lit_journal": NotRequired[str],
        "lit_pubdate": NotRequired[tuple[date, date]],
        "lit_pubmed": NotRequired[str],
        "lit_title": NotRequired[str],
        "lit_citation_id": NotRequired[str],
        "computational_pubmed_id": NotRequired[str],
        "community_pubmed_id": NotRequired[str],
        "proteome": NotRequired[str],
        "proteome_component": NotRequired[str],
        "cited_for": NotRequired[str],
        "reviewed": NotRequired[bool],
        "active": NotRequired[bool],
        "uniref_cluster_50": NotRequired[str],
        "uniref_cluster_90": NotRequired[str],
        "uniref_cluster_100": NotRequired[str],
        "uniparc": NotRequired[str],
    },
)
UniprotkbNamesTaxonomy: TypeAlias = Literal[
    "accession",
    "id",
    "gene_names",
    "gene_oln",
    "gene_orf",
    "gene_primary",
    "gene_synonym",
    "organism_name",
    "organism_id",
    "protein_name",
    "xref_proteomes",
    "lineage",
    "lineage_ids",
    "virus_hosts",
]
UniprotkbSequences: TypeAlias = Literal[
    "cc_alternative_products",
    "ft_var_seq",
    "error_gmodel_pred",
    "fragment",
    "organelle",
    "length",
    "mass",
    "cc_mass_spectrometry",
    "ft_variant",
    "ft_non_cons",
    "ft_non_std",
    "ft_non_ter",
    "cc_polymorphism",
    "cc_rna_editing",
    "sequence",
    "cc_sequence_caution",
    "ft_conflict",
    "ft_unsure",
    "sequence_version",
]
UniprotkbFunction: TypeAlias = Literal[
    "absorption",
    "ft_act_site",
    "ft_binding",
    "ft_ca_bind",
    "cc_catalytic_activity",
    "cc_cofactor",
    "ft_dna_bind",
    "ec",
    "cc_activity_regulation",
    "cc_function",
    "kinetics",
    "ft_metal",
    "ft_np_bind",
    "cc_pathway",
    "ph_dependence",
    "redox_potential",
    "rhea",
    "ft_site",
    "temp_dependence",
]
UniprotkbMiscellaneous: TypeAlias = Literal[
    "annotation_score",
    "cc_caution",
    "keyword",
    "keywordid",
    "cc_miscellaneous",
    "protein_existence",
    "reviewed",
    "tools",
    "uniparc_id",
    "comment_count",
    "feature_count",
]
UniprotkbInteraction: TypeAlias = Literal["cc_interaction", "cc_subunit"]
UniprotkbExpression: TypeAlias = Literal[
    "cc_developmental_stage", "cc_induction", "cc_tissue_specificity"
]
UniprotkbGeneOntologyGo: TypeAlias = Literal["go_p", "go_c", "go", "go_f", "go_id"]
UniprotkbPathologyBiotech: TypeAlias = Literal[
    "cc_allergen",
    "cc_biotechnology",
    "cc_disruption_phenotype",
    "cc_disease",
    "ft_mutagen",
    "cc_pharmaceutical",
    "cc_toxic_dose",
]
UniprotkbSubcellularLocation: TypeAlias = Literal[
    "ft_intramem", "cc_subcellular_location", "ft_topo_dom", "ft_transmem"
]
UniprotkbPtmProcessing: TypeAlias = Literal[
    "ft_chain",
    "ft_crosslnk",
    "ft_disulfid",
    "ft_carbohyd",
    "ft_init_met",
    "ft_lipid",
    "ft_mod_res",
    "ft_peptide",
    "cc_ptm",
    "ft_propep",
    "ft_signal",
    "ft_transit",
]
UniprotkbStructure: TypeAlias = Literal[
    "structure_3d", "ft_strand", "ft_helix", "ft_turn"
]
UniprotkbPublications: TypeAlias = Literal[
    "lit_pubmed_id",
]
UniprotkbDateOf: TypeAlias = Literal[
    "date_created", "date_modified", "date_sequence_modified", "version"
]
UniprotkbFamilyDomains: TypeAlias = Literal[
    "ft_coiled",
    "ft_compbias",
    "cc_domain",
    "ft_domain",
    "ft_motif",
    "protein_families",
    "ft_region",
    "ft_repeat",
    "ft_zn_fing",
]
UniprotkbSequence: TypeAlias = Literal[
    "xref_ccds", "xref_embl", "xref_pir", "xref_refseq"
]
UniprotkbThreedStructure: TypeAlias = Literal[
    "xref_alphafolddb",
    "xref_bmrb",
    "xref_pcddb",
    "xref_pdb",
    "xref_pdbsum",
    "xref_sasbdb",
    "xref_smr",
]
UniprotkbProteinProteinInteraction: TypeAlias = Literal[
    "xref_biogrid",
    "xref_corum",
    "xref_complexportal",
    "xref_dip",
    "xref_elm",
    "xref_intact",
    "xref_mint",
    "xref_string",
]
UniprotkbChemistry: TypeAlias = Literal[
    "xref_bindingdb",
    "xref_chembl",
    "xref_drugbank",
    "xref_drugcentral",
    "xref_guidetopharmacology",
    "xref_swisslipids",
]
UniprotkbProteinFamilygroup: TypeAlias = Literal[
    "xref_allergome",
    "xref_cazy",
    "xref_clae",
    "xref_esther",
    "xref_imgt_gene-db",
    "xref_merops",
    "xref_moondb",
    "xref_moonprot",
    "xref_peroxibase",
    "xref_rebase",
    "xref_tcdb",
    "xref_unilectin",
]
UniprotkbPtm: TypeAlias = Literal[
    "xref_carbonyldb",
    "xref_depod",
    "xref_glyconnect",
    "xref_glygen",
    "xref_metosite",
    "xref_phosphositeplus",
    "xref_swisspalm",
    "xref_unicarbkb",
    "xref_iptmnet",
]
UniprotkbPolymorphismAndMutation: TypeAlias = Literal[
    "xref_biomuta", "xref_dmdm", "xref_dbsnp"
]
UniprotkbTwodGel: TypeAlias = Literal[
    "xref_compluyeast-2dpage",
    "xref_dosac-cobs-2dpage",
    "xref_ogp",
    "xref_reproduction-2dpage",
    "xref_swiss-2dpage",
    "xref_ucd-2dpage",
    "xref_world-2dpage",
]
UniprotkbProteomic: TypeAlias = Literal[
    "xref_cptac",
    "xref_epd",
    "xref_massive",
    "xref_maxqb",
    "xref_pride",
    "xref_paxdb",
    "xref_peptideatlas",
    "xref_promex",
    "xref_proteomicsdb",
    "xref_topdownproteomics",
    "xref_jpost",
]
UniprotkbProtocolsAndMaterials: TypeAlias = Literal[
    "xref_abcd", "xref_antibodypedia", "xref_cptc", "xref_dnasu"
]
UniprotkbGenomeAnnotation: TypeAlias = Literal[
    "xref_ensembl",
    "xref_ensemblbacteria",
    "xref_ensemblfungi",
    "xref_ensemblmetazoa",
    "xref_ensemblplants",
    "xref_ensemblprotists",
    "xref_geneid",
    "xref_gramene",
    "xref_kegg",
    "xref_mane-select",
    "xref_patric",
    "xref_ucsc",
    "xref_vectorbase",
    "xref_wbparasite",
    "xref_wbparasitetranscriptprotein",
]
UniprotkbOrganismSpecific: TypeAlias = Literal[
    "xref_arachnoserver",
    "xref_araport",
    "xref_cgd",
    "xref_ctd",
    "xref_conoserver",
    "xref_disgenet",
    "xref_echobase",
    "xref_flybase",
    "xref_genecards",
    "xref_genereviews",
    "xref_hgnc",
    "xref_hpa",
    "xref_legiolist",
    "xref_leproma",
    "xref_mgi",
    "xref_mim",
    "xref_maizegdb",
    "xref_malacards",
    "xref_niagads",
    "xref_opentargets",
    "xref_orphanet",
    "xref_pharmgkb",
    "xref_pombase",
    "xref_pseudocap",
    "xref_rgd",
    "xref_sgd",
    "xref_tair",
    "xref_tuberculist",
    "xref_veupathdb",
    "xref_vgnc",
    "xref_wormbase",
    "xref_xenbase",
    "xref_zfin",
    "xref_dictybase",
    "xref_euhcvdb",
    "xref_nextprot",
]
UniprotkbPhylogenomic: TypeAlias = Literal[
    "xref_genetree",
    "xref_hogenom",
    "xref_inparanoid",
    "xref_ko",
    "xref_oma",
    "xref_orthodb",
    "xref_phylomedb",
    "xref_treefam",
    "xref_eggnog",
]
UniprotkbEnzymeAndPathway: TypeAlias = Literal[
    "xref_brenda",
    "xref_biocyc",
    "xref_pathwaycommons",
    "xref_plantreactome",
    "xref_reactome",
    "xref_sabio-rk",
    "xref_signor",
    "xref_signalink",
    "xref_unipathway",
]
UniprotkbOther: TypeAlias = Literal[
    "xref_biogrid-orcs",
    "xref_chitars",
    "xref_evolutionarytrace",
    "xref_genewiki",
    "xref_genomernai",
    "xref_phi-base",
    "xref_pro",
    "xref_pharos",
    "xref_rnact",
]
UniprotkbGeneExpression: TypeAlias = Literal[
    "xref_bgee",
    "xref_cleanex",
    "xref_collectf",
    "xref_expressionatlas",
    "xref_genevisible",
]
UniprotkbFamilyAndDomain: TypeAlias = Literal[
    "xref_cdd",
    "xref_disprot",
    "xref_gene3d",
    "xref_hamap",
    "xref_ideal",
    "xref_interpro",
    "xref_panther",
    "xref_pirsf",
    "xref_prints",
    "xref_prosite",
    "xref_pfam",
    "xref_prodom",
    "xref_sfld",
    "xref_smart",
    "xref_supfam",
    "xref_tigrfams",
]
UniprotkbFields: TypeAlias = Literal[
    UniprotkbNamesTaxonomy,
    UniprotkbSequences,
    UniprotkbFunction,
    UniprotkbMiscellaneous,
    UniprotkbInteraction,
    UniprotkbExpression,
    UniprotkbGeneOntologyGo,
    UniprotkbPathologyBiotech,
    UniprotkbSubcellularLocation,
    UniprotkbPtmProcessing,
    UniprotkbStructure,
    UniprotkbPublications,
    UniprotkbDateOf,
    UniprotkbFamilyDomains,
    UniprotkbSequence,
    UniprotkbThreedStructure,
    UniprotkbProteinProteinInteraction,
    UniprotkbChemistry,
    UniprotkbProteinFamilygroup,
    UniprotkbPtm,
    UniprotkbPolymorphismAndMutation,
    UniprotkbTwodGel,
    UniprotkbProteomic,
    UniprotkbProtocolsAndMaterials,
    UniprotkbGenomeAnnotation,
    UniprotkbOrganismSpecific,
    UniprotkbPhylogenomic,
    UniprotkbEnzymeAndPathway,
    UniprotkbOther,
    UniprotkbGeneExpression,
    UniprotkbFamilyAndDomain,
]


@dataclass
class UniprotkbSearch(uniprot_rest.Search):
    dataset: Literal["uniprotkb"] = field(default="uniprotkb", init=False)
    query: UniprotkbQuery
    fields: UniprotkbFields

