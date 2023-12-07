import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class Creator(sdRDM.DataModel):
    """The creator object contains all information about authors that contributed to the resulting document."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("creatorINDEX"),
        xml="@id",
    )

    given_name: str = Field(
        ...,
        description="Given name of the author or contributor.",
    )

    family_name: str = Field(
        ...,
        description="Family name of the author or contributor.",
    )

    mail: str = Field(
        ...,
        description="Email address of the author or contributor.",
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="8246809f84df365e1152d10d4e0335e1c0db90b7"
    )
