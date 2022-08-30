import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import List

from .series import Series


@forge_signature
class UVVisSpectrum(sdRDM.DataModel):
    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("uvvisspectrumINDEX"),
    )
    concentration_unit: str = Field(
        ...,
        description="Concentration unit.",
    )

    concentration: List[float] = Field(
        description="Concentration at which spectrum is recorded.",
        default_factory=ListPlus,
    )

    wavelength: List[float] = Field(
        description="Wavelengths used for detection.",
        default_factory=ListPlus,
    )

    absorption: List[Series] = Field(
        description="Measured absorption, corresponding to detection wavelengths.",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="d4078dbbd5249efa479ea94332cf7067d6c4d2fb"
    )

    def add_to_absorption(
        self,
        values: List[float] = ListPlus(),
    ) -> None:
        """
        Adds an instance of 'Series' to the attribute 'absorption'.

        Args:
            values (List[float]): Series representing an array of values.
        """

        absorption = [
            Series(
                values=values,
            )
        ]

        self.absorption = self.absorption + absorption
