import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import StrictBool


@forge_signature
class AbstractSpecies(sdRDM.DataModel):

    """This object is used to inherit basic attributes common to all species used in the data model."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("abstractspeciesINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="None",
    )

    vessel_id: str = Field(
        ...,
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
        default="feacdf68c751bf9cdc0c1594f449551c7b70bfdf"
    )
