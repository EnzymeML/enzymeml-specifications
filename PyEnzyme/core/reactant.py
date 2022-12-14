from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .abstractspecies import AbstractSpecies
from .sboterm import SBOTerm


@forge_signature
class Reactant(AbstractSpecies):
    """This objects describes the reactants that were used or produced in the course of the experiment.
    """

    smiles: Optional[str] = Field(
        description=(
            "Simplified Molecular Input Line Entry System (SMILES) encoding of the"
            " reactant."
        ),
        template_alias="SMILES",
        default=None,
    )

    inchi: Optional[str] = Field(
        description=(
            "International Chemical Identifier (InChI) encoding of the reactant."
        ),
        template_alias="InCHI",
        default=None,
    )

    chebi_id: Optional[str] = Field(
        description=(
            "Unique identifier of the CHEBI database. Use this identifier to initialize"
            " the object from the CHEBI database."
        ),
        default=None,
    )

    ontology: SBOTerm = Field(description="None", default=SBOTerm.SMALL_MOLECULE)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("reactantINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="82e00b7446c13ed5ba6c191d79f2622cc9226be7"
    )
