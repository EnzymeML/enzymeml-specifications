from typing import Optional
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from .abstractspecies import AbstractSpecies
from .sboterm import SBOTerm


@forge_signature
class Protein(AbstractSpecies):
    """This objects describes the proteins that were used or produced in the course of the experiment.
    """

    sequence: str = Field(
        ..., description="Amino acid sequence of the protein", template_alias="Sequence"
    )

    ecnumber: Optional[str] = Field(
        description="EC number of the protein.",
        regex="(\\d+.)(\\d+.)(\\d+.)(\\d+)",
        template_alias="EC Number",
        default=None,
    )

    organism: Optional[str] = Field(
        description="Organism the protein was expressed in.",
        template_alias="Source organism",
        default=None,
    )

    organism_tax_id: Optional[str] = Field(
        description="Taxonomy identifier of the expression host.", default=None
    )

    uniprotid: Optional[str] = Field(
        description=(
            "Unique identifier referencing a protein entry at UniProt. Use this"
            " identifier to initialize the object from the UniProt database."
        ),
        template_alias="UniProt ID",
        default=None,
    )

    ontology: SBOTerm = Field(description="None", default=SBOTerm.CATALYST)

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("proteinINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="82e00b7446c13ed5ba6c191d79f2622cc9226be7"
    )
