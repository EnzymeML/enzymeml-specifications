import sdRDM

from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator
from .sboterm import SBOTerm


@forge_signature
class KineticParameter(sdRDM.DataModel):
    """This object describes the parameters of the kinetic model and can include all estimated values."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("kineticparameterINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Name of the estimated parameter.",
    )

    value: float = Field(
        ...,
        description="Numerical value of the estimated parameter.",
    )

    unit: str = Field(
        ...,
        description="Unit of the estimated parameter.",
    )

    initial_value: Optional[float] = Field(
        default=None,
        description="Initial value that was used for the parameter estimation.",
    )

    upper: Optional[float] = Field(
        default=None,
        description="Upper bound of the estimated parameter.",
    )

    lower: Optional[float] = Field(
        default=None,
        description="Lower bound of the estimated parameter.",
    )

    is_global: bool = Field(
        description="Specifies if this parameter is a global parameter.",
        default=False,
    )

    stdev: Optional[float] = Field(
        default=None,
        description="Standard deviation of the estimated parameter.",
    )

    constant: bool = Field(
        description="Specifies if this parameter is constant",
        default=False,
    )

    ontology: Optional[SBOTerm] = Field(
        default=None,
        description="Type of the estimated parameter.",
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="7d41b44d1c5104e3654c144843fefd748efe40e0"
    )
