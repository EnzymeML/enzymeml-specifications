import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator


from .datatypes import DataTypes


@forge_signature
class Replicate(sdRDM.DataModel):

    """This object contains the measured time course data as well as metadata to the replicate itself."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("replicateINDEX"),
        xml="@id",
    )

    species_id: str = Field(
        ...,
        description="Unique identifier of the species that has been measured.",
    )

    measurement_id: str = Field(
        ...,
        description=(
            "Unique identifier of the measurement that the replicate is part of."
        ),
    )

    data_type: DataTypes = Field(
        description="Type of data that was measured (e.g. concentration)",
        default=DataTypes.CONCENTRATION,
    )

    data_unit: str = Field(
        ...,
        description="SI unit of the data that was measured.",
    )

    time_unit: str = Field(
        ...,
        description="Time unit of the replicate.",
    )

    time: List[float] = Field(
        multiple=True,
        description="Time steps of the replicate.",
        default_factory=ListPlus,
    )

    data: List[float] = Field(
        multiple=True,
        description="Data that was measured.",
        default_factory=ListPlus,
    )

    is_calculated: bool = Field(
        description="Whether or not the data has been generated by simulation.",
        default=False,
    )

    uri: Optional[str] = Field(
        default=None,
        description="URI of the protein.",
    )

    creator_id: Optional[str] = Field(
        default=None,
        description="Unique identifier of the author.",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0c4e3383699eaeb49bf59ab366e5a77d8e20e074"
    )
