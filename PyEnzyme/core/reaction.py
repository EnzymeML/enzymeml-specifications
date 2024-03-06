import sdRDM

from typing import List, Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element, wrapped
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from pydantic.types import PositiveFloat
from .sboterm import SBOTerm
from .reactionelement import ReactionElement
from .kineticmodel import KineticModel


@forge_signature
class Reaction(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#Reaction"
    },
):
    """This object describes a chemical or enzymatic reaction that was investigated in the course of the experiment. All species used within this object need to be part of the data model."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="Name of the reaction.",
        tag="name",
        json_schema_extra=dict(template_alias="Name"),
    )

    reversible: bool = element(
        description="Whether the reaction is reversible or irreversible",
        default=False,
        tag="reversible",
        json_schema_extra=dict(template_alias="Reversible"),
    )

    temperature: Optional[float] = element(
        description="Numeric value of the temperature of the reaction.",
        default=None,
        tag="temperature",
        json_schema_extra=dict(template_alias="Temperature value"),
    )

    temperature_unit: Optional[str] = element(
        description="Unit of the temperature of the reaction.",
        default=None,
        tag="temperature_unit",
        json_schema_extra=dict(
            pattern="kelvin|Kelvin|k|K|celsius|Celsius|C|c",
            template_alias="Temperature unit",
        ),
    )

    ph: Optional[float] = element(
        description="PH value of the reaction.",
        default=None,
        tag="ph",
        json_schema_extra=dict(
            template_alias="pH value", inclusiveminimum=0, inclusivemaximum=14
        ),
    )

    ontology: SBOTerm = element(
        description="Ontology defining the role of the given species.",
        default=SBOTerm.BIOCHEMICAL_REACTION,
        tag="ontology",
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

    model: Optional[KineticModel] = element(
        description="Kinetic model describing the reaction.",
        default=None,
        tag="model",
        json_schema_extra=dict(),
    )

    educts: List[ReactionElement] = wrapped(
        "educts",
        element(
            description="List of educts containing ReactionElement objects.",
            default_factory=ListPlus,
            tag="ReactionElement",
            json_schema_extra=dict(multiple=True, template_alias="Educts"),
        ),
    )

    products: List[ReactionElement] = wrapped(
        "products",
        element(
            description="List of products containing ReactionElement objects.",
            default_factory=ListPlus,
            tag="ReactionElement",
            json_schema_extra=dict(multiple=True, template_alias="Products"),
        ),
    )

    modifiers: List[ReactionElement] = wrapped(
        "modifiers",
        element(
            description=(
                "List of modifiers (proteins, inhibitors, stimulators) containing"
                " ReactionElement objects."
            ),
            default_factory=ListPlus,
            tag="ReactionElement",
            json_schema_extra=dict(multiple=True, template_alias="Modifiers"),
        ),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )

    def add_to_educts(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = 1.0,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> ReactionElement:
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
        return self.educts[-1]

    def add_to_products(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = 1.0,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> ReactionElement:
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
        return self.products[-1]

    def add_to_modifiers(
        self,
        species_id: str,
        stoichiometry: PositiveFloat = 1.0,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> ReactionElement:
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
        return self.modifiers[-1]
