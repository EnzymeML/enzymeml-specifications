from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .abstractspecies import AbstractSpecies
from .sboterm import SBOTerm


@forge_signature
class Complex(AbstractSpecies):
    """This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment.
    """

    participants: List[str] = Field(
        description="Array of IDs the complex contains",
        regex="[s|p][\\d]+",
        default_factory=ListPlus,
    )

    ontology: SBOTerm = Field(
        description="None", default=SBOTerm.MACROMOLECULAR_COMPLEX
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("complexINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="1bdd251254e451397d8f5c4a4d821cd7562579a0"
    )
