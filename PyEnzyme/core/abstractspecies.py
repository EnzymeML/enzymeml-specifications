import sdRDM

from typing import Optional, Union
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import StrictBool

from .vessel import Vessel


@forge_signature
class AbstractSpecies(sdRDM.DataModel):

    """This object is used to inherit basic attributes common to all species used in the data model."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("abstractspeciesINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="None",
    )

    vessel_id: Union[Vessel, str] = Field(
        ...,
        reference="Vessel.id",
        description="None",
    )

    init_conc: Optional[float] = Field(
        default=None,
        description="None",
    )

    constant: StrictBool = Field(
        ...,
        description="None",
    )

    unit: Optional[str] = Field(
        default=None,
        description="None",
    )

    uri: Optional[str] = Field(
        default=None,
        description="None",
    )

    creator_id: Optional[str] = Field(
        default=None,
        description="None",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="880cff909f356ede1f4ed33ecfb9df11edd470a8"
    )

    @validator("vessel_id")
    def get_vessel_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .vessel import Vessel

        if isinstance(value, Vessel):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [Vessel, str] got '{type(value).__name__}' instead."
            )
