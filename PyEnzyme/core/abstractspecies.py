import sdRDM

from typing import Optional
from typing import Optional, Union
from typing import Union
from pydantic import PrivateAttr
from pydantic import Field
from pydantic import validator
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

@forge_signature
class AbstractSpecies(sdRDM.DataModel):
    """This object is used to inherit basic attributes common to all species used in the data model.
    """


    id: str = Field(description='Unique identifier of the given object.', default_factory=IDGenerator('abstractspeciesINDEX'))


    name: str = Field(..., description='None')


    vessel_id: str = Field(..., description='None')


    constant: bool = Field(..., description='None')


    init_conc: Optional[float] = Field(description='None', default=None)


    unit: Optional[str] = Field(description='None', default=None)


    uri: Optional[str] = Field(description='None', default=None)


    creator_id: Optional[str] = Field(description='None', default=None)


    __repo__: Optional[str] = PrivateAttr(default='git://github.com/EnzymeML/enzymeml-specifications.git')


    __commit__: Optional[str] = PrivateAttr(default='c6342efd3f53ff26cc9c7320fd85c39df74d3d4d')

    @validator('vessel_id', pre=True)
    def get_vessel_id_reference(cls, value):
        """Extracts the ID from a given object to create a reference"""
        
from .vessel import Vessel
        if not isinstance(value, (Vessel, str)):
            raise TypeError(f"Expected 'Vessel' or 'str' got '{type(value).__name__}' instead.")
        elif isinstance(value, Vessel):
            return value.id
        elif isinstance(value, str):
            return value