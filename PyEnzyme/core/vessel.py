import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import StrictBool
from pydantic.types import PositiveFloat


@forge_signature
class Vessel(sdRDM.DataModel):

    """This object describes vessels in which the experiment has been carried out. These can include any type of vessel used in biocatalytic experiments."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("vesselINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Name of the used vessel.",
        template_alias="Name",
    )

    volume: PositiveFloat = Field(
        ...,
        description="Volumetric value of the vessel.",
        template_alias="Volume value",
    )

    unit: str = Field(
        ...,
        description="Volumetric unit of the vessel.",
        template_alias="Volume unit",
    )

    constant: StrictBool = Field(
        description="Whether the volume of the vessel is constant or not.",
        default=True,
    )

    uri: Optional[str] = Field(
        default=None,
        description="URI of the vessel.",
    )

    creator_id: Optional[str] = Field(
        default=None,
        description="Unique identifier of the author.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="feacdf68c751bf9cdc0c1594f449551c7b70bfdf"
    )
