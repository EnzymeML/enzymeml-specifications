
from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .sboterm import SBOTerm
from .abstractspecies import AbstractSpecies


@forge_signature
class Complex(AbstractSpecies):
    """This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("complexINDEX"),
        xml="@id",
    )

    participants: List[str] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Array of IDs the complex contains",
    )

    ontology: SBOTerm = Field(
        description="None",
        default=SBOTerm.MACROMOLECULAR_COMPLEX,
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8246809f84df365e1152d10d4e0335e1c0db90b7"
    )
