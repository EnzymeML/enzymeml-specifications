import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature


@forge_signature
class File(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#File"
    },
):
    """This object contains files that have been attached to the document."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="Name of the file",
        tag="name",
        json_schema_extra=dict(),
    )

    content: bytes = element(
        description="Contents of the file",
        tag="content",
        json_schema_extra=dict(),
    )

    filetype: str = element(
        description="Type of the file such as .xml, .json, and so on",
        tag="filetype",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )
