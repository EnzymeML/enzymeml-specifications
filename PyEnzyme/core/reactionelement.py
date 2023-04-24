import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import PositiveFloat

from .sboterm import SBOTerm


@forge_signature
class ReactionElement(sdRDM.DataModel):

    """This object is part of the Reaction object and describes either an educt, product or modifier. The latter includes buffers, counter-ions as well as proteins/enzymes."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactionelementINDEX"),
        xml="@id",
    )

    species_id: str = Field(
        ...,
        description=(
            "Internal identifier to either a protein or reactant defined in the"
            " EnzymeMLDocument."
        ),
    )

    stoichiometry: PositiveFloat = Field(
        description="Positive float number representing the associated stoichiometry.",
        default=1.0,
    )

    constant: bool = Field(
        description=(
            "Whether or not the concentration of this species remains constant."
        ),
        default=False,
    )

    ontology: Optional[SBOTerm] = Field(
        default=None,
        description="Ontology defining the role of the given species.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="f3502066a5b52b5dbe2cf1464b7f855e9ce80c2d"
    )
