import sdRDM

from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from pydantic.types import PositiveFloat
from typing import List
from typing import Optional

from .kineticmodel import KineticModel
from .reactionelement import ReactionElement
from .sboterm import SBOTerm


@forge_signature
class Reaction(sdRDM.DataModel):

    """This object describes a chemical or enzymatic reaction that was investigated in the course of the experiment. All species used within this object need to be part of the data model."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactionINDEX"),
    )
    name: str = Field(
        ...,
        description="Name of the reaction.",
        template_alias="Name",
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
        template_alias="Temperature unit",
    )

    ph: float = Field(
        ...,
        description="PH value of the reaction.",
        template_alias="pH value",
        inclusiveminimum=0,
        inclusivemaximum=14,
    )

    reversible: bool = Field(
        description="Whether the reaction is reversible or irreversible",
        default=False,
        template_alias="Reversible",
    )

    ontology: SBOTerm = Field(
        default=SBOTerm.BIOCHEMICAL_REACTION,
        description="Ontology defining the role of the given species.",
    )

    uri: Optional[str] = Field(
        description="URI of the reaction.",
        default=None,
    )

    creator_id: Optional[str] = Field(
        description="Unique identifier of the author.",
        default=None,
    )

    model: Optional[KineticModel] = Field(
        description="Kinetic model decribing the reaction.",
        default=None,
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
        description="List of modifiers (Proteins, snhibitors, stimulators) containing ReactionElement objects.",
        template_alias="Modifiers",
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0a477aff983a6c599d5807335a62ad8cbbd1ffff"
    )

    def add_to_educts(
        self,
        species_id: str,
        stoichiometry: PositiveFloat,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
    ) -> None:
        """
        Adds an instance of 'ReactionElement' to the attribute 'educts'.

        Args:
            species_id (str): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.
            stoichiometry (PositiveFloat): Positive float number representing the associated stoichiometry.
            constant (bool): Whether or not the concentration of this species remains constant. Defaults to False
            ontology (Optional[SBOTerm]): Ontology defining the role of the given species. Defaults to None
        """

        educts = [
            ReactionElement(
                species_id=species_id,
                stoichiometry=stoichiometry,
                constant=constant,
                ontology=ontology,
            )
        ]

        self.educts = self.educts + educts

    def add_to_products(
        self,
        species_id: str,
        stoichiometry: PositiveFloat,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
    ) -> None:
        """
        Adds an instance of 'ReactionElement' to the attribute 'products'.

        Args:
            species_id (str): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.
            stoichiometry (PositiveFloat): Positive float number representing the associated stoichiometry.
            constant (bool): Whether or not the concentration of this species remains constant. Defaults to False
            ontology (Optional[SBOTerm]): Ontology defining the role of the given species. Defaults to None
        """

        products = [
            ReactionElement(
                species_id=species_id,
                stoichiometry=stoichiometry,
                constant=constant,
                ontology=ontology,
            )
        ]

        self.products = self.products + products

    def add_to_modifiers(
        self,
        species_id: str,
        stoichiometry: PositiveFloat,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
    ) -> None:
        """
        Adds an instance of 'ReactionElement' to the attribute 'modifiers'.

        Args:
            species_id (str): Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.
            stoichiometry (PositiveFloat): Positive float number representing the associated stoichiometry.
            constant (bool): Whether or not the concentration of this species remains constant. Defaults to False
            ontology (Optional[SBOTerm]): Ontology defining the role of the given species. Defaults to None
        """

        modifiers = [
            ReactionElement(
                species_id=species_id,
                stoichiometry=stoichiometry,
                constant=constant,
                ontology=ontology,
            )
        ]

        self.modifiers = self.modifiers + modifiers
