import sdRDM

from typing import Optional
from pydantic import PrivateAttr, validator
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature


@forge_signature
class AbstractSpecies(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#AbstractSpecies"
    },
):
    """This object is used to inherit basic attributes common to all species used in the data model."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="None",
        tag="name",
        json_schema_extra=dict(),
    )

    vessel_id: str = element(
        description="None",
        tag="vessel_id",
        json_schema_extra=dict(),
    )

    init_conc: Optional[float] = element(
        description="None",
        default=None,
        tag="init_conc",
        json_schema_extra=dict(),
    )

    constant: bool = element(
        description="None",
        tag="constant",
        json_schema_extra=dict(),
    )

    unit: Optional[str] = element(
        description="None",
        default=None,
        tag="unit",
        json_schema_extra=dict(),
    )

    uri: Optional[str] = element(
        description="None",
        default=None,
        tag="uri",
        json_schema_extra=dict(),
    )

    creator_id: Optional[str] = element(
        description="None",
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

    @validator("vessel_id")
    def get_vessel_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""
        from .vessel import Vessel

        if isinstance(value, Vessel):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [Vessel, str] got '{type(value).__name__}' instead."
            )

    @validator("vessel_id")
    def get_vessel_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""
        from .vessel import Vessel

        if isinstance(value, Vessel):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [Vessel, str] got '{type(value).__name__}' instead."
            )

    @validator("vessel_id")
    def get_vessel_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .vessel import Vessel

        if isinstance(value, Vessel):
            return value.id
        elif isinstance(value, str):
            return value
        else:
            raise TypeError(
                f"Expected types [Vessel, str] got '{type(value).__name__}' instead."
            )
