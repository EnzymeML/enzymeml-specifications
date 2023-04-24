
from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .abstractspecies import AbstractSpecies
from .sboterm import SBOTerm


@forge_signature
class Complex(AbstractSpecies):

    """This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("complexINDEX"),
        xml="@id",
    )

    participants: List[str] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Array of IDs the complex contains",
        regex="[s|p][\d]+",
    )

    ontology: SBOTerm = Field(
        description="None",
        default=SBOTerm.MACROMOLECULAR_COMPLEX,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="f3502066a5b52b5dbe2cf1464b7f855e9ce80c2d"
    )
