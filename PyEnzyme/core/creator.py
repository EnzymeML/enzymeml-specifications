import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Creator(sdRDM.DataModel):
    """The creator object contains all information about authors that contributed to the resulting document.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("creatorINDEX"),
    )

    given_name: str = Field(..., description="Given name of the author or contributor.")

    family_name: str = Field(
        ..., description="Family name of the author or contributor."
    )

    mail: str = Field(..., description="Email address of the author or contributor.")

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c6342efd3f53ff26cc9c7320fd85c39df74d3d4d"
    )
