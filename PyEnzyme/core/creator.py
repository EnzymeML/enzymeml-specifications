import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature


@forge_signature
class Creator(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#Creator"
    },
):
    """The creator object contains all information about authors that contributed to the resulting document."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    given_name: str = element(
        description="Given name of the author or contributor.",
        tag="given_name",
        json_schema_extra=dict(),
    )

    family_name: str = element(
        description="Family name of the author or contributor.",
        tag="family_name",
        json_schema_extra=dict(),
    )

    mail: str = element(
        description="Email address of the author or contributor.",
        tag="mail",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )
