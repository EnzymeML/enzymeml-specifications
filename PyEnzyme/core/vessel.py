import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature
from pydantic.types import PositiveFloat


@forge_signature
class Vessel(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#Vessel"
    },
):
    """This object describes vessels in which the experiment has been carried out. These can include any type of vessel used in biocatalytic experiments."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="Name of the used vessel.",
        tag="name",
        json_schema_extra=dict(template_alias="Name"),
    )

    volume: PositiveFloat = element(
        description="Volumetric value of the vessel.",
        tag="volume",
        json_schema_extra=dict(template_alias="Volume value"),
    )

    unit: str = element(
        description="Volumetric unit of the vessel.",
        tag="unit",
        json_schema_extra=dict(template_alias="Volume unit"),
    )

    constant: bool = element(
        description="Whether the volume of the vessel is constant or not.",
        default=True,
        tag="constant",
        json_schema_extra=dict(),
    )

    uri: Optional[str] = element(
        description="URI of the vessel.",
        default=None,
        tag="uri",
        json_schema_extra=dict(),
    )

    creator_id: Optional[str] = element(
        description="Unique identifier of the author.",
        default=None,
        tag="creator_id",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )
