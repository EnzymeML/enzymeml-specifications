import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .abstractspecies import AbstractSpecies
from .replicate import Replicate
from .measurementdata import MeasurementData


@forge_signature
class Measurement(sdRDM.DataModel):
    """This object describes the result of a measurement, which includes time course data of any type defined in DataTypes. It includes initial concentrations of all species used in a single measurement."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Name of the measurement",
    )

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

    species: List[MeasurementData] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="Species of the measurement.",
    )

    global_time: List[float] = Field(
        multiple=True,
        description="Global time of the measurement all replicates agree on.",
        default_factory=ListPlus,
    )

    global_time_unit: str = Field(
        ...,
        description="Unit of the global time.",
    )

    uri: Optional[str] = Field(
        default=None,
        description="URI of the reaction.",
    )

    creator_id: Optional[str] = Field(
        default=None,
        description="Unique identifier of the author.",
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="50253f9a1c0d24ac18da78642bf549337c0a3218"
    )

    def add_to_species(
        self,
        init_conc: float,
        unit: str,
        measurement_id: str,
        species_id: Optional[AbstractSpecies] = None,
        replicates: List[Replicate] = ListPlus(),
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'MeasurementData' to attribute species

        Args:
            id (str): Unique identifier of the 'MeasurementData' object. Defaults to 'None'.
            init_conc (): Initial concentration of the measurement data..
            unit (): The unit of the measurement data..
            measurement_id (): Unique measurement identifier this dataset belongs to..
            species_id (): The identifier for the described reactant.. Defaults to None
            replicates (): A list of replicate objects holding raw data of the measurement.. Defaults to ListPlus()
        """
        params = {
            "init_conc": init_conc,
            "unit": unit,
            "measurement_id": measurement_id,
            "species_id": species_id,
            "replicates": replicates,
        }
        if id is not None:
            params["id"] = id
        self.species.append(MeasurementData(**params))
        return self.species[-1]
