import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .datatypes import DataTypes
from .replicate import Replicate


@forge_signature
class MeasurementData(sdRDM.DataModel):
    """This object describes a single entity of a measurement, which corresponds to one species. It also holds replicates which contain time course data.
    """

    init_conc: float = Field(
        ..., description="Initial concentration of the measurement data."
    )

    unit: str = Field(..., description="The unit of the measurement data.")

    measurement_id: str = Field(
        ..., description="Unique measurement identifier this dataset belongs to."
    )

    species_id: Optional[str] = Field(
        description="The identifier for the described reactant.", default=None
    )

    replicates: List[Replicate] = Field(
        description="A list of replicate objects holding raw data of the measurement.",
        default_factory=ListPlus,
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("measurementdataINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="82e00b7446c13ed5ba6c191d79f2622cc9226be7"
    )

    def add_to_replicates(
        self,
        species_id: str,
        measurement_id: str,
        data_unit: str,
        time_unit: str,
        time: List[float],
        data: List[float],
        data_type: DataTypes = DataTypes.CONCENTRATION,
        is_calculated: bool = False,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Replicate' to the attribute 'replicates'.

        Args:


            id (str): Unique identifier of the 'Replicate' object. Defaults to 'None'.


            species_id (str): Unique identifier of the species that has been measured.


            measurement_id (str): Unique identifier of the measurement that the replicate is part of.


            data_unit (str): SI unit of the data that was measured.


            time_unit (str): Time unit of the replicate.


            time (List[float]): Time steps of the replicate.


            data (List[float]): Data that was measured.


            data_type (DataTypes): Type of data that was measured (e.g. concentration). Defaults to DataTypes.CONCENTRATION


            is_calculated (bool): Whether or not the data has been generated by simulation. Defaults to False


            uri (Optional[str]): URI of the protein. Defaults to None


            creator_id (Optional[str]): Unique identifier of the author. Defaults to None
        """

        params = {
            "species_id": species_id,
            "measurement_id": measurement_id,
            "data_unit": data_unit,
            "time_unit": time_unit,
            "time": time,
            "data": data,
            "data_type": data_type,
            "is_calculated": is_calculated,
            "uri": uri,
            "creator_id": creator_id,
        }
        if id is not None:
            params["id"] = id
        replicates = [Replicate(**params)]
        self.replicates = self.replicates + replicates
