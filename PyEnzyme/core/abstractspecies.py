import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from pydantic.types import StrictBool


@forge_signature
class AbstractSpecies(sdRDM.DataModel):
    """This object is used to inherit basic attributes common to all species used in the data model.
    """

    name: str = Field(..., description="None")

    vessel_id: str = Field(..., description="None")

    init_conc: Optional[float] = Field(description="None", default=None)

    unit: Optional[str] = Field(description="None", default=None)

    uri: Optional[str] = Field(description="None", default=None)

    creator_id: Optional[str] = Field(description="None", default=None)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("abstractspeciesINDEX"),
        xml="@id",
    )

    constant: StrictBool = Field(..., description="None")

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="82e00b7446c13ed5ba6c191d79f2622cc9226be7"
    )
