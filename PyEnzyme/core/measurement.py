import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from .measurementdata import MeasurementData
from .replicate import Replicate


@forge_signature
class Measurement(sdRDM.DataModel):
    """This object describes the result of a measurement, which includes time course data of any type defined in DataTypes. It includes initial concentrations of all species used in a single measurement.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementINDEX"),
    )

    name: str = Field(..., description="Name of the measurement")

    temperature: float = Field(
        ...,
        description="Numeric value of the temperature of the reaction.",
        template_alias="Temperature value",
    )

    temperature_unit: str = Field(
        ...,
        description="Unit of the temperature of the reaction.",
        regex="kelvin|Kelvin|k|K|celsius|Celsius|C|c",
    )

    ph: float = Field(
        ...,
        description="PH value of the reaction.",
        inclusiveminimum=0,
        inclusivemaximum=14,
    )

    global_time_unit: str = Field(..., description="Unit of the global time.")

    species: List[MeasurementData] = Field(
        description="Species of the measurement.", default_factory=ListPlus
    )

    global_time: List[float] = Field(
        description="Global time of the measurement all replicates agree on.",
        default_factory=ListPlus,
    )

    uri: Optional[str] = Field(description="URI of the reaction.", default=None)

    creator_id: Optional[str] = Field(
        description="Unique identifier of the author.", default=None
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c6342efd3f53ff26cc9c7320fd85c39df74d3d4d"
    )

    def add_to_species(
        self,
        init_conc: float,
        unit: str,
        measurement_id: str,
        replicates: List[Replicate],
        species_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'MeasurementData' to the attribute 'species'.

        Args:


            id (str): Unique identifier of the 'MeasurementData' object. Defaults to 'None'.


            init_conc (float): Initial concentration of the measurement data.


            unit (str): The unit of the measurement data.


            measurement_id (str): Unique measurement identifier this dataset belongs to.


            replicates (List[Replicate]): A list of replicate objects holding raw data of the measurement.


            species_id (Optional[str]): The identifier for the described reactant. Defaults to None
        """

        params = {
            "init_conc": init_conc,
            "unit": unit,
            "measurement_id": measurement_id,
            "replicates": replicates,
            "species_id": species_id,
        }
        if id is not None:
            params["id"] = id
        species = [MeasurementData(**params)]
        self.species = self.species + species
