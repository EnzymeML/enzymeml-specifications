import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class File(sdRDM.DataModel):
    """This object contains files that have been attached to the document."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("fileINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Name of the file",
    )

    content: bytes = Field(
        ...,
        description="Contents of the file",
    )

    filetype: str = Field(
        ...,
        description="Type of the file such as .xml, .json, and so on",
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="45c5aa64db4e885152a7e877878a25f1baeb20da"
    )
