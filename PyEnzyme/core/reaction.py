import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from pydantic.types import PositiveFloat
from .kineticmodel import KineticModel
from .reactionelement import ReactionElement
from .sboterm import SBOTerm


@forge_signature
class Reaction(sdRDM.DataModel):
    """This object describes a chemical or enzymatic reaction that was investigated in the course of the experiment. All species used within this object need to be part of the data model.
    """

    name: str = Field(..., description="Name of the reaction.", template_alias="Name")

    reversible: bool = Field(
        description="Whether the reaction is reversible or irreversible",
        default=False,
        template_alias="Reversible",
    )

    ontology: SBOTerm = Field(
        default=SBOTerm.BIOCHEMICAL_REACTION,
        description="Ontology defining the role of the given species.",
    )

    uri: Optional[str] = Field(description="URI of the reaction.", default=None)

    creator_id: Optional[str] = Field(
        description="Unique identifier of the author.", default=None
    )

    model: Optional[KineticModel] = Field(
        description="Kinetic model decribing the reaction.", default=None
    )

    educts: List[ReactionElement] = Field(
        description="List of educts containing ReactionElement objects.",
        template_alias="Educts",
        default_factory=ListPlus,
    )

    products: List[ReactionElement] = Field(
        description="List of products containing ReactionElement objects.",
        template_alias="Products",
        default_factory=ListPlus,
    )

    modifiers: List[ReactionElement] = Field(
        description=(
            "List of modifiers (Proteins, snhibitors, stimulators) containing"
            " ReactionElement objects."
        ),
        template_alias="Modifiers",
        default_factory=ListPlus,
    )

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactionINDEX"),
        xml="@id",
    )

    temperature: Optional[float] = Field(
        description="Numeric value of the temperature of the reaction.",
        template_alias="Temperature value",
        default=None,
    )

    temperature_unit: Optional[str] = Field(
        description="Unit of the temperature of the reaction.",
        regex="kelvin|Kelvin|k|K|celsius|Celsius|C|c",
        template_alias="Temperature unit",
        default=None,
    )

    ph: Optional[float] = Field(
        description="PH value of the reaction.",
        template_alias="pH value",
        inclusiveminimum=0,
        inclusivemaximum=14,
        default=None,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="82e00b7446c13ed5ba6c191d79f2622cc9226be7"
    )

    def add_to_educts(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = "1.0",
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'ReactionElement' to the attribute 'educts'.

        Args:


            id (str): Unique identifier of the 'ReactionElement' object. Defaults to 'None'.


            species_id (str): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.


            stoichiometry (PositiveFloat): Positive float number representing the associated stoichiometry. Defaults to "1.0"


            constant (bool): Whether or not the concentration of this species remains constant. Defaults to False


            ontology (Optional[SBOTerm]): Ontology defining the role of the given species. Defaults to None
        """

        params = {
            "species_id": species_id,
            "stoichiometry": stoichiometry,
            "constant": constant,
            "ontology": ontology,
        }
        if id is not None:
            params["id"] = id
        educts = [ReactionElement(**params)]
        self.educts = self.educts + educts

    def add_to_products(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = "1.0",
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'ReactionElement' to the attribute 'products'.

        Args:


            id (str): Unique identifier of the 'ReactionElement' object. Defaults to 'None'.


            species_id (str): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.


            stoichiometry (PositiveFloat): Positive float number representing the associated stoichiometry. Defaults to "1.0"


            constant (bool): Whether or not the concentration of this species remains constant. Defaults to False


            ontology (Optional[SBOTerm]): Ontology defining the role of the given species. Defaults to None
        """

        params = {
            "species_id": species_id,
            "stoichiometry": stoichiometry,
            "constant": constant,
            "ontology": ontology,
        }
        if id is not None:
            params["id"] = id
        products = [ReactionElement(**params)]
        self.products = self.products + products

    def add_to_modifiers(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = "1.0",
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'ReactionElement' to the attribute 'modifiers'.

        Args:


            id (str): Unique identifier of the 'ReactionElement' object. Defaults to 'None'.


            species_id (str): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.


            stoichiometry (PositiveFloat): Positive float number representing the associated stoichiometry. Defaults to "1.0"


            constant (bool): Whether or not the concentration of this species remains constant. Defaults to False


            ontology (Optional[SBOTerm]): Ontology defining the role of the given species. Defaults to None
        """

        params = {
            "species_id": species_id,
            "stoichiometry": stoichiometry,
            "constant": constant,
            "ontology": ontology,
        }
        if id is not None:
            params["id"] = id
        modifiers = [ReactionElement(**params)]
        self.modifiers = self.modifiers + modifiers
