import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .kineticparameter import KineticParameter
from .sboterm import SBOTerm


@forge_signature
class KineticModel(sdRDM.DataModel):
    """This object describes a kinetic model that was derived from the experiment."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("kineticmodelINDEX"),
    )

    name: str = Field(..., description="Name of the kinetic law.")

    equation: str = Field(..., description="Equation for the kinetic law.")

    parameters: List[KineticParameter] = Field(
        description="List of estimated parameters.", default_factory=ListPlus
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

    def add_to_parameters(
        self,
        name: str,
        value: float,
        unit: str,
        initial_value: Optional[float] = None,
        upper: Optional[float] = None,
        lower: Optional[float] = None,
        is_global: bool = False,
        stdev: Optional[float] = None,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
    ) -> None:
        """
        Adds an instance of 'KineticParameter' to the attribute 'parameters'.

        Args:


            name (str): Name of the estimated parameter.


            value (float): Numerical value of the estimated parameter.


            unit (str): Unit of the estimated parameter.


            initial_value (Optional[float]): Initial value that was used for the parameter estimation. Defaults to None


            upper (Optional[float]): Upper bound of the estimated parameter. Defaults to None


            lower (Optional[float]): Lower bound of the estimated parameter. Defaults to None


            is_global (bool): Specifies if this parameter is a global parameter. Defaults to False


            stdev (Optional[float]): Standard deviation of the estimated parameter. Defaults to None


            constant (bool): Specifies if this parameter is constant. Defaults to False


            ontology (Optional[SBOTerm]): Type of the estimated parameter. Defaults to None
        """
        parameters = [
            KineticParameter(
                name=name,
                value=value,
                unit=unit,
                initial_value=initial_value,
                upper=upper,
                lower=lower,
                is_global=is_global,
                stdev=stdev,
                constant=constant,
                ontology=ontology,
            )
        ]
        self.parameters = self.parameters + parameters
