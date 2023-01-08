import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from pydantic.types import PositiveFloat
from pydantic.types import StrictBool


@forge_signature
class Vessel(sdRDM.DataModel):
    """This object describes vessels in which the experiment has been carried out. These can include any type of vessel used in biocatalytic experiments.
    """

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

    uri: Optional[str] = Field(description="URI of the vessel.", default=None)

    creator_id: Optional[str] = Field(
        description="Unique identifier of the author.", default=None
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("vesselINDEX"),
        xml="@id",
    )

    constant: StrictBool = Field(
        description="Whether the volume of the vessel is constant or not.", default=True
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="82e00b7446c13ed5ba6c191d79f2622cc9226be7"
    )
