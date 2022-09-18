import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from pydantic.types import PositiveFloat


@forge_signature
class Vessel(sdRDM.DataModel):
    """This object describes vessels in which the experiment has been carried out. These can include any type of vessel used in biocatalytic experiments.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("vesselINDEX"),
    )

    name: str = Field(
        ..., description="Name of the used vessel.", template_alias="Name"
    )

    volume: PositiveFloat = Field(
        ...,
        description="Volumetric value of the vessel.",
        template_alias="Volume value",
    )

    unit: str = Field(
        ..., description="Volumetric unit of the vessel.", template_alias="Volume unit"
    )

    constant: bool = Field(
        description="Whether the volume of the vessel is constant or not.", default=True
    )

    uri: Optional[str] = Field(description="URI of the vessel.", default=None)

    creator_id: Optional[str] = Field(
        description="Unique identifier of the author.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c6342efd3f53ff26cc9c7320fd85c39df74d3d4d"
    )
