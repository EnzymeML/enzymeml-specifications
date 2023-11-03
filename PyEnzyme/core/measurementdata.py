import sdRDM

from typing import Optional, Union, List
from pydantic import PrivateAttr, Field, validator
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .datatypes import DataTypes
from .abstractspecies import AbstractSpecies
from .replicate import Replicate


@forge_signature
class MeasurementData(sdRDM.DataModel):
    """This object describes a single entity of a measurement, which corresponds to one species. It also holds replicates which contain time course data."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementdataINDEX"),
        xml="@id",
    )

    init_conc: float = Field(
        ...,
        description="Initial concentration of the measurement data.",
    )

    unit: str = Field(
        ...,
        description="The unit of the measurement data.",
    )

    measurement_id: str = Field(
        ...,
        description="Unique measurement identifier this dataset belongs to.",
    )

    species_id: Union[AbstractSpecies, str, None] = Field(
        default=None,
        reference="AbstractSpecies.id",
        description="The identifier for the described reactant.",
    )

    replicates: List[Replicate] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="A list of replicate objects holding raw data of the measurement.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="ae9d6e7f791e602185e5b15643d4271c2b722265"
    )

    def add_to_replicates(
        self,
        species_id: AbstractSpecies,
        measurement_id: str,
        data_unit: str,
        time_unit: str,
        data_type: DataTypes = DataTypes.CONCENTRATION,
        time: List[float] = ListPlus(),
        data: List[float] = ListPlus(),
        is_calculated: bool = False,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'Replicate' to attribute replicates

        Args:
            id (str): Unique identifier of the 'Replicate' object. Defaults to 'None'.
            species_id (): Unique identifier of the species that has been measured..
            measurement_id (): Unique identifier of the measurement that the replicate is part of..
            data_unit (): SI unit of the data that was measured..
            time_unit (): Time unit of the replicate..
            data_type (): Type of data that was measured (e.g. concentration). Defaults to DataTypes.CONCENTRATION
            time (): Time steps of the replicate.. Defaults to ListPlus()
            data (): Data that was measured.. Defaults to ListPlus()
            is_calculated (): Whether or not the data has been generated by simulation.. Defaults to False
            uri (): URI of the protein.. Defaults to None
            creator_id (): Unique identifier of the author.. Defaults to None
        """

        params = {
            "species_id": species_id,
            "measurement_id": measurement_id,
            "data_unit": data_unit,
            "time_unit": time_unit,
            "data_type": data_type,
            "time": time,
            "data": data,
            "is_calculated": is_calculated,
            "uri": uri,
            "creator_id": creator_id,
        }

        if id is not None:
            params["id"] = id

        self.replicates.append(Replicate(**params))

    @validator("species_id")
    def get_species_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""

        from .abstractspecies import AbstractSpecies

        if isinstance(value, AbstractSpecies):
            return value.id
        elif isinstance(value, str):
            return value
        elif value is None:
            return value
        else:
            raise TypeError(
                f"Expected types [AbstractSpecies, str] got '{type(value).__name__}'"
                " instead."
            )
