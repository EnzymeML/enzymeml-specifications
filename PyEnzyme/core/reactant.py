
from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature
from .sboterm import SBOTerm
from .abstractspecies import AbstractSpecies


@forge_signature
class Reactant(
    AbstractSpecies,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#Reactant"
    },
):
    """This object describes the reactants that were used or produced in the course of the experiment."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    smiles: Optional[str] = element(
        description=(
            "Simplified Molecular Input Line Entry System (SMILES) encoding of the"
            " reactant."
        ),
        default=None,
        tag="smiles",
        json_schema_extra=dict(template_alias="SMILES"),
    )

    inchi: Optional[str] = element(
        description=(
            "International Chemical Identifier (InChI) encoding of the reactant."
        ),
        default=None,
        tag="inchi",
        json_schema_extra=dict(template_alias="InCHI"),
    )

    chebi_id: Optional[str] = element(
        description=(
            "Unique identifier of the CHEBI database. Use this identifier to initialize"
            " the object from the CHEBI database."
        ),
        default=None,
        tag="chebi_id",
        json_schema_extra=dict(),
    )

    ontology: SBOTerm = element(
        description="SBO term defining the role of the given species in the reaction.",
        default=SBOTerm.SMALL_MOLECULE,
        tag="ontology",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )
