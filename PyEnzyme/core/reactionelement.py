import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import PositiveFloat

from .sboterm import SBOTerm
from .abstractspecies import AbstractSpecies


@forge_signature
class ReactionElement(sdRDM.DataModel):
    """This object is part of the Reaction object and describes either an educt, product or modifier. The latter includes buffers, counter-ions as well as proteins/enzymes."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactionelementINDEX"),
        xml="@id",
    )

    species_id: Union[AbstractSpecies, str] = Field(
        ...,
        reference="AbstractSpecies.id",
        description=(
            "Internal identifier to either a protein or reactant defined in the"
            " EnzymeMLDocument."
        ),
        references="EnzymeMLDocument.reactants.id",
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
        default="be5b096d8b21ddf8fc513e3e62f1d3ebcdfa4187"
    )

    @validator("species_id")
    def get_species_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .abstractspecies import AbstractSpecies

        if isinstance(value, AbstractSpecies):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [AbstractSpecies, str] got '{type(value).__name__}'"
                " instead."
            )
