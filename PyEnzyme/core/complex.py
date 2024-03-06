
from typing import List, Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element, wrapped
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from .sboterm import SBOTerm
from .abstractspecies import AbstractSpecies


@forge_signature
class Complex(
    AbstractSpecies,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#Complex"
    },
):
    """This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    participants: List[str] = wrapped(
        "participants",
        element(
            description="Array of IDs the complex contains",
            default_factory=ListPlus,
            tag="string",
            json_schema_extra=dict(multiple=True),
        ),
    )

    ontology: SBOTerm = element(
        description="None",
        default=SBOTerm.MACROMOLECULAR_COMPLEX,
        tag="ontology",
        json_schema_extra=dict(),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )
