from typing import Optional
from pydantic import PrivateAttr
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator

from pydantic import Field
from typing import Optional

from .abstractspecies import AbstractSpecies
from .sboterm import SBOTerm


@forge_signature
class Reactant(AbstractSpecies):

    """This objects describes the reactants that were used or produced in the course of the experiment."""

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactantINDEX"),
    )
    smiles: Optional[str] = Field(
        description="Simplified Molecular Input Line Entry System (SMILES) encoding of the reactant.",
        template_alias="SMILES",
        default=None,
    )

    inchi: Optional[str] = Field(
        description="International Chemical Identifier (InChI) encoding of the reactant.",
        template_alias="InCHI",
        default=None,
    )

    chebi_id: Optional[str] = Field(
        description="Unique identifier of the CHEBI database. Use this identifier to initialize the object from the CHEBI database.",
        default=None,
    )

    ontology: SBOTerm = Field(
        description="None",
        default=SBOTerm.SMALL_MOLECULE,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )
    __commit__: Optional[str] = PrivateAttr(
        default="0a477aff983a6c599d5807335a62ad8cbbd1ffff"
    )
