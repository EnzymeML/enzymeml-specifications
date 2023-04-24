import sdRDM

from typing import List, Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic.types import PositiveFloat

from .sboterm import SBOTerm
from .kineticmodel import KineticModel
from .reactionelement import ReactionElement


@forge_signature
class Reaction(sdRDM.DataModel):

    """This object describes a chemical or enzymatic reaction that was investigated in the course of the experiment. All species used within this object need to be part of the data model."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactionINDEX"),
        xml="@id",
    )

    name: str = Field(
        ...,
        description="Name of the reaction.",
        template_alias="Name",
    )

    reversible: bool = Field(
        description="Whether the reaction is reversible or irreversible",
        default=False,
        template_alias="Reversible",
    )

    temperature: Optional[float] = Field(
        default=None,
        description="Numeric value of the temperature of the reaction.",
        template_alias="Temperature value",
    )

    temperature_unit: Optional[str] = Field(
        default=None,
        description="Unit of the temperature of the reaction.",
        regex="kelvin|Kelvin|k|K|celsius|Celsius|C|c",
        template_alias="Temperature unit",
    )

    ph: Optional[float] = Field(
        default=None,
        description="PH value of the reaction.",
        template_alias="pH value",
        inclusiveminimum=0,
        inclusivemaximum=14,
    )

    ontology: SBOTerm = Field(
        default=SBOTerm.BIOCHEMICAL_REACTION,
        description="Ontology defining the role of the given species.",
    )

    uri: Optional[str] = Field(
        default=None,
        description="URI of the reaction.",
    )

    creator_id: Optional[str] = Field(
        default=None,
        description="Unique identifier of the author.",
    )

    model: Optional[KineticModel] = Field(
        default=None,
        description="Kinetic model decribing the reaction.",
    )

    educts: List[ReactionElement] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="List of educts containing ReactionElement objects.",
        template_alias="Educts",
    )

    products: List[ReactionElement] = Field(
        default_factory=ListPlus,
        multiple=True,
        description="List of products containing ReactionElement objects.",
        template_alias="Products",
    )

    modifiers: List[ReactionElement] = Field(
        default_factory=ListPlus,
        multiple=True,
        description=(
            "List of modifiers (Proteins, snhibitors, stimulators) containing"
            " ReactionElement objects."
        ),
        template_alias="Modifiers",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="feacdf68c751bf9cdc0c1594f449551c7b70bfdf"
    )

    def add_to_educts(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = 1.0,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ReactionElement' to attribute educts

        Args:
            id (str): Unique identifier of the 'ReactionElement' object. Defaults to 'None'.
            species_id (): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument..
            stoichiometry (): Positive float number representing the associated stoichiometry.. Defaults to 1.0
            constant (): Whether or not the concentration of this species remains constant.. Defaults to False
            ontology (): Ontology defining the role of the given species.. Defaults to None
        """

        params = {
            "species_id": species_id,
            "stoichiometry": stoichiometry,
            "constant": constant,
            "ontology": ontology,
        }

        if id is not None:
            params["id"] = id

        self.educts.append(ReactionElement(**params))

    def add_to_products(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = 1.0,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ReactionElement' to attribute products

        Args:
            id (str): Unique identifier of the 'ReactionElement' object. Defaults to 'None'.
            species_id (): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument..
            stoichiometry (): Positive float number representing the associated stoichiometry.. Defaults to 1.0
            constant (): Whether or not the concentration of this species remains constant.. Defaults to False
            ontology (): Ontology defining the role of the given species.. Defaults to None
        """

        params = {
            "species_id": species_id,
            "stoichiometry": stoichiometry,
            "constant": constant,
            "ontology": ontology,
        }

        if id is not None:
            params["id"] = id

        self.products.append(ReactionElement(**params))

    def add_to_modifiers(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = 1.0,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        This method adds an object of type 'ReactionElement' to attribute modifiers

        Args:
            id (str): Unique identifier of the 'ReactionElement' object. Defaults to 'None'.
            species_id (): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument..
            stoichiometry (): Positive float number representing the associated stoichiometry.. Defaults to 1.0
            constant (): Whether or not the concentration of this species remains constant.. Defaults to False
            ontology (): Ontology defining the role of the given species.. Defaults to None
        """

        params = {
            "species_id": species_id,
            "stoichiometry": stoichiometry,
            "constant": constant,
            "ontology": ontology,
        }

        if id is not None:
            params["id"] = id

        self.modifiers.append(ReactionElement(**params))
