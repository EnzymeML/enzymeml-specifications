import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from pydantic.types import PositiveFloat

from .sboterm import SBOTerm


@forge_signature
class ReactionElement(sdRDM.DataModel):
    """This object is part of the Reaction object and describes either an educt, product or modifier. The latter includes buffers, counter-ions as well as proteins/enzymes.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactionelementINDEX"),
    )

    species_id: str = Field(
        ...,
        description=(
            "Internal identifier to either a protein or reactant defined in the"
            " EnzymeMLDocument."
        ),
    )

    stoichiometry: PositiveFloat = Field(
        ...,
        description="Positive float number representing the associated stoichiometry.",
    )

    constant: bool = Field(
        description=(
            "Whether or not the concentration of this species remains constant."
        ),
        default=False,
    )

    ontology: Optional[SBOTerm] = Field(
        description="Ontology defining the role of the given species.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c6342efd3f53ff26cc9c7320fd85c39df74d3d4d"
    )
