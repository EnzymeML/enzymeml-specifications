import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature
from .sboterm import SBOTerm


@forge_signature
class KineticParameter(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#KineticParameter"
    },
):
    """This object describes the parameters of the kinetic model and can include all estimated values."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="Name of the estimated parameter.",
        tag="name",
        json_schema_extra=dict(),
    )

    value: float = element(
        description="Numerical value of the estimated parameter.",
        tag="value",
        json_schema_extra=dict(),
    )

    unit: str = element(
        description="Unit of the estimated parameter.",
        tag="unit",
        json_schema_extra=dict(),
    )

    initial_value: Optional[float] = element(
        description="Initial value that was used for the parameter estimation.",
        default=None,
        tag="initial_value",
        json_schema_extra=dict(),
    )

    upper: Optional[float] = element(
        description="Upper bound of the estimated parameter.",
        default=None,
        tag="upper",
        json_schema_extra=dict(),
    )

    lower: Optional[float] = element(
        description="Lower bound of the estimated parameter.",
        default=None,
        tag="lower",
        json_schema_extra=dict(),
    )

    is_global: bool = element(
        description=(
            "Specifies if this parameter is global for the entire EnzymeMLDocument."
        ),
        default=False,
        tag="is_global",
        json_schema_extra=dict(),
    )

    stdev: Optional[float] = element(
        description="Standard deviation of the estimated parameter.",
        default=None,
        tag="stdev",
        json_schema_extra=dict(),
    )

    constant: bool = element(
        description="Specifies if this parameter is constant",
        default=False,
        tag="constant",
        json_schema_extra=dict(),
    )

    ontology: Optional[SBOTerm] = element(
        description="Type of the estimated parameter.",
        default=None,
        tag="ontology",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )
