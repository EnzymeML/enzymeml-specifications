import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class File(sdRDM.DataModel):
    """This objects contains a files that has been attached to the document."""

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
        description="Type of the file such as .xml, .json and so on",
    )

    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="e30035f54df9387024ec6f7436acbbb9d12f139c"
    )
