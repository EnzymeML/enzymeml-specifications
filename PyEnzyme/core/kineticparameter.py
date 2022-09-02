import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .sboterm import SBOTerm


@forge_signature
class KineticParameter(sdRDM.DataModel):
    """This object describes the parameters of the kinetic model and can include all estimated values.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("kineticparameterINDEX"),
    )

    name: str = Field(..., description="Name of the estimated parameter.")

    value: float = Field(..., description="Numerical value of the estimated parameter.")

    unit: str = Field(..., description="Unit of the estimated parameter.")

    initial_value: Optional[float] = Field(
        description="Initial value that was used for the parameter estimation.",
        default=None,
    )

    upper: Optional[float] = Field(
        description="Upper bound of the estimated parameter.", default=None
    )

    lower: Optional[float] = Field(
        description="Lower bound of the estimated parameter.", default=None
    )

    is_global: bool = Field(
        description="Specifies if this parameter is a global parameter.", default=False
    )

    stdev: Optional[float] = Field(
        description="Standard deviation of the estimated parameter.", default=None
    )

    constant: bool = Field(
        description="Specifies if this parameter is constant", default=False
    )

    ontology: Optional[SBOTerm] = Field(
        description="Type of the estimated parameter.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c6342efd3f53ff26cc9c7320fd85c39df74d3d4d"
    )
