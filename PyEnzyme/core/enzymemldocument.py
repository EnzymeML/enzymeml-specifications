import sdRDM

from typing import List, Optional
from pydantic import PrivateAttr
from uuid import uuid4
from pydantic_xml import attr, element, wrapped
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature
from datetime import datetime as Datetime
from pydantic.types import PositiveFloat
from .kineticmodel import KineticModel
from .complex import Complex
from .reaction import Reaction
from .protein import Protein
from .kineticparameter import KineticParameter
from .sboterm import SBOTerm
from .reactionelement import ReactionElement
from .vessel import Vessel
from .file import File
from .creator import Creator
from .reactant import Reactant
from .measurementdata import MeasurementData
from .measurement import Measurement


@forge_signature
class EnzymeMLDocument(
    sdRDM.DataModel,
    nsmap={
        "": "https://github.com/EnzymeML/enzymeml-specifications@142ca246cf92944bcbc11fbda9892f64bff77e8b#EnzymeMLDocument"
    },
):
    """This is the root object that composes all objects found in an EnzymeML document. It also includes general metadata such as the name of the document, when it was created/modified and references to publications, databases and arbitrary links to the web."""

    id: Optional[str] = attr(
        name="id",
        description="Unique identifier of the given object.",
        default_factory=lambda: str(uuid4()),
        xml="@id",
    )

    name: str = element(
        description="Title of the EnzymeML Document.",
        tag="name",
        json_schema_extra=dict(),
    )

    pubmedid: Optional[str] = element(
        description="Pubmed ID reference.",
        default=None,
        tag="pubmedid",
        json_schema_extra=dict(),
    )

    url: Optional[str] = element(
        description="Arbitrary type of URL that is related to the EnzymeML document.",
        default=None,
        tag="url",
        json_schema_extra=dict(),
    )

    doi: Optional[str] = element(
        description=(
            "Digital Object Identifier of the referenced publication or the EnzymeML"
            " document."
        ),
        default=None,
        tag="doi",
        json_schema_extra=dict(),
    )

    created: Optional[Datetime] = element(
        description="Date the EnzymeML document was created.",
        default=None,
        tag="created",
        json_schema_extra=dict(),
    )

    modified: Optional[Datetime] = element(
        description="Date the EnzymeML document was modified.",
        default=None,
        tag="modified",
        json_schema_extra=dict(),
    )

    creators: List[Creator] = wrapped(
        "creators",
        element(
            description="Contains all authors that are part of the experiment.",
            default_factory=ListPlus,
            tag="Creator",
            json_schema_extra=dict(multiple=True),
        ),
    )

    vessels: List[Vessel] = wrapped(
        "vessels",
        element(
            description="Contains all vessels that are part of the experiment.",
            default_factory=ListPlus,
            tag="Vessel",
            json_schema_extra=dict(multiple=True),
        ),
    )

    proteins: List[Protein] = wrapped(
        "proteins",
        element(
            description="Contains all proteins that are part of the experiment.",
            default_factory=ListPlus,
            tag="Protein",
            json_schema_extra=dict(multiple=True),
        ),
    )

    complexes: List[Complex] = wrapped(
        "complexes",
        element(
            description="Contains all complexes that are part of the experiment.",
            default_factory=ListPlus,
            tag="Complex",
            json_schema_extra=dict(multiple=True),
        ),
    )

    reactants: List[Reactant] = wrapped(
        "reactants",
        element(
            description="Contains all reactants that are part of the experiment.",
            default_factory=ListPlus,
            tag="Reactant",
            json_schema_extra=dict(multiple=True),
        ),
    )

    reactions: List[Reaction] = wrapped(
        "reactions",
        element(
            description=(
                "Dictionary mapping from reaction IDs to reaction-describing objects."
            ),
            default_factory=ListPlus,
            tag="Reaction",
            json_schema_extra=dict(multiple=True),
        ),
    )

    measurements: List[Measurement] = wrapped(
        "measurements",
        element(
            description=(
                "Contains measurements that describe outcomes of an experiment."
            ),
            default_factory=ListPlus,
            tag="Measurement",
            json_schema_extra=dict(multiple=True),
        ),
    )

    files: List[File] = wrapped(
        "files",
        element(
            description="Contains files attached to the data model.",
            default_factory=ListPlus,
            tag="File",
            json_schema_extra=dict(multiple=True),
        ),
    )

    global_parameters: List[KineticParameter] = wrapped(
        "global_parameters",
        element(
            description=(
                "Dictionary mapping from parameter IDs to global kinetic parameters"
                " describing objects."
            ),
            default_factory=ListPlus,
            tag="KineticParameter",
            json_schema_extra=dict(multiple=True),
        ),
    )
    _repo: Optional[str] = PrivateAttr(
        default="https://github.com/EnzymeML/enzymeml-specifications"
    )
    _commit: Optional[str] = PrivateAttr(
        default="142ca246cf92944bcbc11fbda9892f64bff77e8b"
    )

    def add_to_creators(
        self, given_name: str, family_name: str, mail: str, id: Optional[str] = None
    ) -> Creator:
        """
        This method adds an object of type 'Creator' to attribute creators

        Args:
            id (str): Unique identifier of the 'Creator' object. Defaults to 'None'.
            given_name (): Given name of the author or contributor..
            family_name (): Family name of the author or contributor..
            mail (): Email address of the author or contributor..
        """
        params = {"given_name": given_name, "family_name": family_name, "mail": mail}
        if id is not None:
            params["id"] = id
        self.creators.append(Creator(**params))
        return self.creators[-1]

    def add_to_vessels(
        self,
        name: str,
        volume: PositiveFloat,
        unit: str,
        constant: bool = True,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Vessel:
        """
        This method adds an object of type 'Vessel' to attribute vessels

        Args:
            id (str): Unique identifier of the 'Vessel' object. Defaults to 'None'.
            name (): Name of the used vessel..
            volume (): Volumetric value of the vessel..
            unit (): Volumetric unit of the vessel..
            constant (): Whether the volume of the vessel is constant or not.. Defaults to True
            uri (): URI of the vessel.. Defaults to None
            creator_id (): Unique identifier of the author.. Defaults to None
        """
        params = {
            "name": name,
            "volume": volume,
            "unit": unit,
            "constant": constant,
            "uri": uri,
            "creator_id": creator_id,
        }
        if id is not None:
            params["id"] = id
        self.vessels.append(Vessel(**params))
        return self.vessels[-1]

    def add_to_proteins(
        self,
        sequence: str,
        name: str,
        vessel_id: str,
        constant: bool,
        ecnumber: Optional[str] = None,
        organism: Optional[str] = None,
        organism_tax_id: Optional[str] = None,
        uniprotid: Optional[str] = None,
        ontology: SBOTerm = SBOTerm.PROTEIN,
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Protein:
        """
        This method adds an object of type 'Protein' to attribute proteins

        Args:
            id (str): Unique identifier of the 'Protein' object. Defaults to 'None'.
            sequence (): Amino acid sequence of the protein.
            name (): None.
            vessel_id (): None.
            constant (): None.
            ecnumber (): EC number of the protein.. Defaults to None
            organism (): Organism the protein was expressed in.. Defaults to None
            organism_tax_id (): Taxonomy identifier of the expression host.. Defaults to None
            uniprotid (): Unique identifier referencing a protein entry at UniProt. Use this identifier to initialize the object from the UniProt database.. Defaults to None
            ontology (): None. Defaults to SBOTerm.PROTEIN
            init_conc (): None. Defaults to None
            unit (): None. Defaults to None
            uri (): None. Defaults to None
            creator_id (): None. Defaults to None
        """
        params = {
            "sequence": sequence,
            "name": name,
            "vessel_id": vessel_id,
            "constant": constant,
            "ecnumber": ecnumber,
            "organism": organism,
            "organism_tax_id": organism_tax_id,
            "uniprotid": uniprotid,
            "ontology": ontology,
            "init_conc": init_conc,
            "unit": unit,
            "uri": uri,
            "creator_id": creator_id,
        }
        if id is not None:
            params["id"] = id
        self.proteins.append(Protein(**params))
        return self.proteins[-1]

    def add_to_complexes(
        self,
        name: str,
        vessel_id: str,
        constant: bool,
        participants: List[str] = ListPlus(),
        ontology: SBOTerm = SBOTerm.MACROMOLECULAR_COMPLEX,
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Complex:
        """
        This method adds an object of type 'Complex' to attribute complexes

        Args:
            id (str): Unique identifier of the 'Complex' object. Defaults to 'None'.
            name (): None.
            vessel_id (): None.
            constant (): None.
            participants (): Array of IDs the complex contains. Defaults to ListPlus()
            ontology (): None. Defaults to SBOTerm.MACROMOLECULAR_COMPLEX
            init_conc (): None. Defaults to None
            unit (): None. Defaults to None
            uri (): None. Defaults to None
            creator_id (): None. Defaults to None
        """
        params = {
            "name": name,
            "vessel_id": vessel_id,
            "constant": constant,
            "participants": participants,
            "ontology": ontology,
            "init_conc": init_conc,
            "unit": unit,
            "uri": uri,
            "creator_id": creator_id,
        }
        if id is not None:
            params["id"] = id
        self.complexes.append(Complex(**params))
        return self.complexes[-1]

    def add_to_reactants(
        self,
        name: str,
        vessel_id: str,
        constant: bool,
        smiles: Optional[str] = None,
        inchi: Optional[str] = None,
        chebi_id: Optional[str] = None,
        ontology: SBOTerm = SBOTerm.SMALL_MOLECULE,
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Reactant:
        """
        This method adds an object of type 'Reactant' to attribute reactants

        Args:
            id (str): Unique identifier of the 'Reactant' object. Defaults to 'None'.
            name (): None.
            vessel_id (): None.
            constant (): None.
            smiles (): Simplified Molecular Input Line Entry System (SMILES) encoding of the reactant.. Defaults to None
            inchi (): International Chemical Identifier (InChI) encoding of the reactant.. Defaults to None
            chebi_id (): Unique identifier of the CHEBI database. Use this identifier to initialize the object from the CHEBI database.. Defaults to None
            ontology (): SBO term defining the role of the given species in the reaction.. Defaults to SBOTerm.SMALL_MOLECULE
            init_conc (): None. Defaults to None
            unit (): None. Defaults to None
            uri (): None. Defaults to None
            creator_id (): None. Defaults to None
        """
        params = {
            "name": name,
            "vessel_id": vessel_id,
            "constant": constant,
            "smiles": smiles,
            "inchi": inchi,
            "chebi_id": chebi_id,
            "ontology": ontology,
            "init_conc": init_conc,
            "unit": unit,
            "uri": uri,
            "creator_id": creator_id,
        }
        if id is not None:
            params["id"] = id
        self.reactants.append(Reactant(**params))
        return self.reactants[-1]

    def add_to_reactions(
        self,
        name: str,
        reversible: bool = False,
        temperature: Optional[float] = None,
        temperature_unit: Optional[str] = None,
        ph: Optional[float] = None,
        ontology: SBOTerm = SBOTerm.BIOCHEMICAL_REACTION,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        model: Optional[KineticModel] = None,
        educts: List[ReactionElement] = ListPlus(),
        products: List[ReactionElement] = ListPlus(),
        modifiers: List[ReactionElement] = ListPlus(),
        id: Optional[str] = None,
    ) -> Reaction:
        """
        This method adds an object of type 'Reaction' to attribute reactions

        Args:
            id (str): Unique identifier of the 'Reaction' object. Defaults to 'None'.
            name (): Name of the reaction..
            reversible (): Whether the reaction is reversible or irreversible. Defaults to False
            temperature (): Numeric value of the temperature of the reaction.. Defaults to None
            temperature_unit (): Unit of the temperature of the reaction.. Defaults to None
            ph (): PH value of the reaction.. Defaults to None
            ontology (): Ontology defining the role of the given species.. Defaults to SBOTerm.BIOCHEMICAL_REACTION
            uri (): URI of the reaction.. Defaults to None
            creator_id (): Unique identifier of the author.. Defaults to None
            model (): Kinetic model describing the reaction.. Defaults to None
            educts (): List of educts containing ReactionElement objects.. Defaults to ListPlus()
            products (): List of products containing ReactionElement objects.. Defaults to ListPlus()
            modifiers (): List of modifiers (proteins, inhibitors, stimulators) containing ReactionElement objects.. Defaults to ListPlus()
        """
        params = {
            "name": name,
            "reversible": reversible,
            "temperature": temperature,
            "temperature_unit": temperature_unit,
            "ph": ph,
            "ontology": ontology,
            "uri": uri,
            "creator_id": creator_id,
            "model": model,
            "educts": educts,
            "products": products,
            "modifiers": modifiers,
        }
        if id is not None:
            params["id"] = id
        self.reactions.append(Reaction(**params))
        return self.reactions[-1]

    def add_to_measurements(
        self,
        name: str,
        temperature: float,
        temperature_unit: str,
        ph: float,
        global_time_unit: str,
        species: List[MeasurementData] = ListPlus(),
        global_time: List[float] = ListPlus(),
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> Measurement:
        """
        This method adds an object of type 'Measurement' to attribute measurements

        Args:
            id (str): Unique identifier of the 'Measurement' object. Defaults to 'None'.
            name (): Name of the measurement.
            temperature (): Numeric value of the temperature of the reaction..
            temperature_unit (): Unit of the temperature of the reaction..
            ph (): PH value of the reaction..
            global_time_unit (): Unit of the global time..
            species (): Species of the measurement.. Defaults to ListPlus()
            global_time (): Global time of the measurement all replicates agree on.. Defaults to ListPlus()
            uri (): URI of the reaction.. Defaults to None
            creator_id (): Unique identifier of the author.. Defaults to None
        """
        params = {
            "name": name,
            "temperature": temperature,
            "temperature_unit": temperature_unit,
            "ph": ph,
            "global_time_unit": global_time_unit,
            "species": species,
            "global_time": global_time,
            "uri": uri,
            "creator_id": creator_id,
        }
        if id is not None:
            params["id"] = id
        self.measurements.append(Measurement(**params))
        return self.measurements[-1]

    def add_to_files(
        self, name: str, content: bytes, filetype: str, id: Optional[str] = None
    ) -> File:
        """
        This method adds an object of type 'File' to attribute files

        Args:
            id (str): Unique identifier of the 'File' object. Defaults to 'None'.
            name (): Name of the file.
            content (): Contents of the file.
            filetype (): Type of the file such as .xml, .json, and so on.
        """
        params = {"name": name, "content": content, "filetype": filetype}
        if id is not None:
            params["id"] = id
        self.files.append(File(**params))
        return self.files[-1]

    def add_to_global_parameters(
        self,
        name: str,
        value: float,
        unit: str,
        initial_value: Optional[float] = None,
        upper: Optional[float] = None,
        lower: Optional[float] = None,
        is_global: bool = False,
        stdev: Optional[float] = None,
        constant: bool = False,
        ontology: Optional[SBOTerm] = None,
        id: Optional[str] = None,
    ) -> KineticParameter:
        """
        This method adds an object of type 'KineticParameter' to attribute global_parameters

        Args:
            id (str): Unique identifier of the 'KineticParameter' object. Defaults to 'None'.
            name (): Name of the estimated parameter..
            value (): Numerical value of the estimated parameter..
            unit (): Unit of the estimated parameter..
            initial_value (): Initial value that was used for the parameter estimation.. Defaults to None
            upper (): Upper bound of the estimated parameter.. Defaults to None
            lower (): Lower bound of the estimated parameter.. Defaults to None
            is_global (): Specifies if this parameter is global for the entire EnzymeMLDocument.. Defaults to False
            stdev (): Standard deviation of the estimated parameter.. Defaults to None
            constant (): Specifies if this parameter is constant. Defaults to False
            ontology (): Type of the estimated parameter.. Defaults to None
        """
        params = {
            "name": name,
            "value": value,
            "unit": unit,
            "initial_value": initial_value,
            "upper": upper,
            "lower": lower,
            "is_global": is_global,
            "stdev": stdev,
            "constant": constant,
            "ontology": ontology,
        }
        if id is not None:
            params["id"] = id
        self.global_parameters.append(KineticParameter(**params))
        return self.global_parameters[-1]
