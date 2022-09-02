import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class AbstractSpecies(sdRDM.DataModel):
    """This object is used to inherit basic attributes common to all species used in the data model.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("abstractspeciesINDEX"),
    )

    name: str = Field(..., description="None")

    vessel_id: str = Field(..., description="None")

    constant: bool = Field(..., description="None")

    init_conc: Optional[float] = Field(description="None", default=None)

    unit: Optional[str] = Field(description="None", default=None)

    uri: Optional[str] = Field(description="None", default=None)

    creator_id: Optional[str] = Field(description="None", default=None)

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c6342efd3f53ff26cc9c7320fd85c39df74d3d4d"
    )
