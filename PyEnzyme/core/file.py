import sdRDM

from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


@forge_signature
class File(sdRDM.DataModel):
    """This objects contains a files that has been attached to the document."""

    name: str = Field(..., description="Name of the file")

    content: bytes = Field(..., description="Contents of the file")

    filetype: str = Field(
        ..., description="Type of the file such as .xml, .json and so on"
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("fileINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="82e00b7446c13ed5ba6c191d79f2622cc9226be7"
    )
