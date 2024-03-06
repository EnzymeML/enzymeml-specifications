
from typing import Optional
from pydantic import Field, PrivateAttr
from sdRDM.base.utils import forge_signature, IDGenerator
from .abstractspecies import AbstractSpecies
from .sboterm import SBOTerm


@forge_signature
class Reactant(AbstractSpecies):
    """This object describes the reactants that were used or produced in the course of the experiment."""

    id: Optional[str] = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactantINDEX"),
        xml="@id",
    )

    smiles: Optional[str] = Field(
        default=None,
        description="Simplified Molecular Input Line Entry System (SMILES) encoding of the reactant.",
        template_alias="SMILES",
    )

    inchi: Optional[str] = Field(
        default=None,
        description="International Chemical Identifier (InChI) encoding of the reactant.",
        template_alias="InCHI",
    )

    chebi_id: Optional[str] = Field(
        default=None,
        description="Unique identifier of the CHEBI database. Use this identifier to initialize the object from the CHEBI database.",
    )

    ontology: SBOTerm = Field(
        description="SBO term defining the role of the given species in the reaction.",
        default=SBOTerm.SMALL_MOLECULE,
    )
    __repo__: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="45c5aa64db4e885152a7e877878a25f1baeb20da"
    )
