import sdRDM

from typing import Optional
from pydantic import PrivateAttr, validator
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature
from pydantic.types import PositiveFloat
from .sboterm import SBOTerm


@forge_signature
class ReactionElement(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#ReactionElement"
    },
):
    """This object is part of the Reaction object and describes either an educt, product, or modifier. The latter includes buffers, counter-ions as well as proteins/enzymes."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    species_id: str = element(
        description=(
            "Internal identifier to either a protein or reactant defined in the"
            " EnzymeMLDocument."
        ),
        tag="species_id",
        json_schema_extra=dict(references="EnzymeMLDocument.reactants.id"),
    )

    stoichiometry: PositiveFloat = element(
        description="Positive float number representing the associated stoichiometry.",
        default=1.0,
        tag="stoichiometry",
        json_schema_extra=dict(),
    )

    constant: bool = element(
        description=(
            "Whether or not the concentration of this species remains constant."
        ),
        default=False,
        tag="constant",
        json_schema_extra=dict(),
    )

    ontology: Optional[SBOTerm] = element(
        description="Ontology defining the role of the given species.",
        default=None,
        tag="ontology",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
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
