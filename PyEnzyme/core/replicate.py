import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List
from typing import Optional

from .datatypes import DataTypes


@forge_signature
class Replicate(sdRDM.DataModel):

    """This object contains the measured time course data as well as metadata to the replicate itself."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("replicateINDEX"),
    )
    species_id: str = Field(
        ...,
        description="Unique identifier of the species that has been measured.",
    )

    measurement_id: str = Field(
        ...,
        description="Unique identifier of the measurement that the replicate is part of.",
    )

    data_unit: str = Field(
        ...,
        description="SI unit of the data that was measured.",
    )

    time_unit: str = Field(
        ...,
        description="Time unit of the replicate.",
    )

    data_type: DataTypes = Field(
        description="Type of data that was measured (e.g. concentration)",
        default=DataTypes.CONCENTRATION,
    )

    time: List[float] = Field(
        description="Time steps of the replicate.",
        default_factory=ListPlus,
    )

    data: List[float] = Field(
        description="Data that was measured.",
        default_factory=ListPlus,
    )

    is_calculated: bool = Field(
        description="Whether or not the data has been generated by simulation.",
        default=False,
    )

    uri: Optional[str] = Field(
        description="URI of the protein.",
        default=None,
    )

    creator_id: Optional[str] = Field(
        description="Unique identifier of the author.",
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0a477aff983a6c599d5807335a62ad8cbbd1ffff"
    )
