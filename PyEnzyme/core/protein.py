
from typing import Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element
from sdRDM.base.utils import forge_signature
from .sboterm import SBOTerm
from .abstractspecies import AbstractSpecies


@forge_signature
class Protein(
    AbstractSpecies,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#Protein"
    },
):
    """This objects describes the proteins that were used or produced in the course of the experiment."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    sequence: str = element(
        description="Amino acid sequence of the protein",
        tag="sequence",
        json_schema_extra=dict(template_alias="Sequence"),
    )

    ecnumber: Optional[str] = element(
        description="EC number of the protein.",
        default=None,
        tag="ecnumber",
        json_schema_extra=dict(
            pattern="(\\d+.)(\\d+.)(\\d+.)(\\d+)", template_alias="EC Number"
        ),
    )

    organism: Optional[str] = element(
        description="Organism the protein was expressed in.",
        default=None,
        tag="organism",
        json_schema_extra=dict(template_alias="Source organism"),
    )

    organism_tax_id: Optional[str] = element(
        description="Taxonomy identifier of the expression host.",
        default=None,
        tag="organism_tax_id",
        json_schema_extra=dict(),
    )

    uniprotid: Optional[str] = element(
        description=(
            "Unique identifier referencing a protein entry at UniProt. Use this"
            " identifier to initialize the object from the UniProt database."
        ),
        default=None,
        tag="uniprotid",
        json_schema_extra=dict(template_alias="UniProt ID"),
    )

    ontology: SBOTerm = element(
        description="None",
        default=SBOTerm.PROTEIN,
        tag="ontology",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )
