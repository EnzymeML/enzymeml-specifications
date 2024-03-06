import sdRDM

from typing import List, Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element, wrapped
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from .measurementdata import MeasurementData
from .replicate import Replicate


@forge_signature
class Measurement(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#Measurement"
    },
):
    """This object describes the result of a measurement, which includes time course data of any type defined in DataTypes. It includes initial concentrations of all species used in a single measurement."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="Name of the measurement",
        tag="name",
        json_schema_extra=dict(),
    )

    temperature: float = element(
        description="Numeric value of the temperature of the reaction.",
        tag="temperature",
        json_schema_extra=dict(template_alias="Temperature value"),
    )

    temperature_unit: str = element(
        description="Unit of the temperature of the reaction.",
        tag="temperature_unit",
        json_schema_extra=dict(pattern="kelvin|Kelvin|k|K|celsius|Celsius|C|c"),
    )

    ph: float = element(
        description="PH value of the reaction.",
        tag="ph",
        json_schema_extra=dict(inclusiveminimum=0, inclusivemaximum=14),
    )

    species: List[MeasurementData] = wrapped(
        "species",
        element(
            description="Species of the measurement.",
            default_factory=ListPlus,
            tag="MeasurementData",
            json_schema_extra=dict(multiple=True),
        ),
    )

    global_time: List[float] = wrapped(
        "global_time",
        element(
            description="Global time of the measurement all replicates agree on.",
            default_factory=ListPlus,
            tag="float",
            json_schema_extra=dict(multiple=True),
        ),
    )

    global_time_unit: str = element(
        description="Unit of the global time.",
        tag="global_time_unit",
        json_schema_extra=dict(),
    )

    uri: Optional[str] = element(
        description="URI of the reaction.",
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

    def add_to_species(
        self,
        init_conc: float,
        unit: str,
        measurement_id: str,
        species_id: Optional[str] = None,
        replicates: List[Replicate] = ListPlus(),
        id: Optional[str] = None,
    ) -> MeasurementData:
        """
        This method adds an object of type 'MeasurementData' to attribute species

        Args:
            id (str): Unique identifier of the 'MeasurementData' object. Defaults to 'None'.
            init_conc (): Initial concentration of the measurement data..
            unit (): The unit of measurement data..
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
