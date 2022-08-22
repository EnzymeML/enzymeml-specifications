from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List

from .abstractspecies import AbstractSpecies
from .sboterm import SBOTerm


@forge_signature
class Complex(AbstractSpecies):

    """This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("complexINDEX"),
    )
    participants: List[str] = Field(
        description="Array of IDs the complex contains",
        regex="[s|p][\d]+",
        default_factory=ListPlus,
    )

    ontology: SBOTerm = Field(
        description="None",
        default=SBOTerm.MACROMOLECULAR_COMPLEX,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0a477aff983a6c599d5807335a62ad8cbbd1ffff"
    )
