
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
        default="2df473809eff599cdb7b5db2e5d4014cfbdb3766"
    )
