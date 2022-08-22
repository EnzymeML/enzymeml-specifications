import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field


@forge_signature
class File(sdRDM.DataModel):

    """This objects contains a files that has been attached to the document."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("fileINDEX"),
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

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0a477aff983a6c599d5807335a62ad8cbbd1ffff"
    )
