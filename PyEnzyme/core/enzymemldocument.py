import sdRDM

from typing import Optional
from typing import List
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from datetime import datetime
from pydantic.types import PositiveFloat

from .complex import Complex
from .creator import Creator
from .file import File
from .kineticmodel import KineticModel
from .kineticparameter import KineticParameter
from .measurement import Measurement
from .measurementdata import MeasurementData
from .protein import Protein
from .reactant import Reactant
from .reaction import Reaction
from .reactionelement import ReactionElement
from .sboterm import SBOTerm
from .vessel import Vessel


@forge_signature
class EnzymeMLDocument(sdRDM.DataModel):
    """This is the root object that composes all objects found in an EnzymeML document. It also includes general metadata such as the name of the document, when it was created/modified and references to publications, databases and arbitrary links to the web.
    """

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("enzymemldocumentINDEX"),
    )

    name: str = Field(..., description="Title of the EnzymeML Document.")

    pubmedid: Optional[str] = Field(description="Pubmed ID reference.", default=None)

    url: Optional[str] = Field(
        description="Arbitrary type of URL that is related to the EnzymeML document.",
        default=None,
    )

    doi: Optional[str] = Field(
        description=(
            "Digital Object Identifier of the referenced publication or the EnzymeML"
            " document."
        ),
        default=None,
    )

    created: Optional[datetime] = Field(
        description="Date the EnzymeML document was created.", default=None
    )

    modified: Optional[datetime] = Field(
        description="Date the EnzymeML document was modified.", default=None
    )

    creators: List[Creator] = Field(
        description="Contains all authors that are part of the experiment.",
        default_factory=ListPlus,
    )

    vessels: List[Vessel] = Field(
        description="Contains all vessels that are part of the experiment.",
        default_factory=ListPlus,
    )

    proteins: List[Protein] = Field(
        description="Contains all proteins that are part of the experiment.",
        default_factory=ListPlus,
    )

    complexes: List[Complex] = Field(
        description="Contains all complexes that are part of the experiment.",
        default_factory=ListPlus,
    )

    reactants: List[Reactant] = Field(
        description="Contains all reactants that are part of the experiment.",
        default_factory=ListPlus,
    )

    reactions: List[Reaction] = Field(
        description=(
            "Dictionary mapping from reaction IDs to reaction describing objects."
        ),
        default_factory=ListPlus,
    )

    measurements: List[Measurement] = Field(
        description="Contains measurements that describe outcomes of an experiment.",
        default_factory=ListPlus,
    )

    files: List[File] = Field(
        description="Contains files attached to the data model.",
        default_factory=ListPlus,
    )

    global_parameters: List[KineticParameter] = Field(
        description=(
            "Dictionary mapping from parameter IDs to global kinetic parameter"
            " describing objects."
        ),
        default_factory=ListPlus,
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="c6342efd3f53ff26cc9c7320fd85c39df74d3d4d"
    )

    def add_to_creators(self, given_name: str, family_name: str, mail: str) -> None:
        """
        Adds an instance of 'Creator' to the attribute 'creators'.

        Args:


            given_name (str): Given name of the author or contributor.


            family_name (str): Family name of the author or contributor.


            mail (str): Email address of the author or contributor.
        """
        creators = [Creator(given_name=given_name, family_name=family_name, mail=mail)]
        self.creators = self.creators + creators

    def add_to_vessels(
        self,
        name: str,
        volume: PositiveFloat,
        unit: str,
        constant: bool = True,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Vessel' to the attribute 'vessels'.

        Args:


            name (str): Name of the used vessel.


            volume (PositiveFloat): Volumetric value of the vessel.


            unit (str): Volumetric unit of the vessel.


            constant (bool): Whether the volume of the vessel is constant or not. Defaults to True


            uri (Optional[str]): URI of the vessel. Defaults to None


            creator_id (Optional[str]): Unique identifier of the author. Defaults to None
        """
        vessels = [
            Vessel(
                name=name,
                volume=volume,
                unit=unit,
                constant=constant,
                uri=uri,
                creator_id=creator_id,
            )
        ]
        self.vessels = self.vessels + vessels

    def add_to_proteins(
        self,
        name: str,
        vessel_id: str,
        constant: bool,
        sequence: str,
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        ecnumber: Optional[str] = None,
        organism: Optional[str] = None,
        organism_tax_id: Optional[str] = None,
        uniprotid: Optional[str] = None,
        ontology: SBOTerm = SBOTerm.CATALYST,
    ) -> None:
        """
        Adds an instance of 'Protein' to the attribute 'proteins'.

        Args:


            name (str): None.


            vessel_id (str): None.


            constant (bool): None.


            sequence (str): Amino acid sequence of the protein.


            init_conc (Optional[float]): None. Defaults to None


            unit (Optional[str]): None. Defaults to None


            uri (Optional[str]): None. Defaults to None


            creator_id (Optional[str]): None. Defaults to None


            ecnumber (Optional[str]): EC number of the protein. Defaults to None


            organism (Optional[str]): Organism the protein was expressed in. Defaults to None


            organism_tax_id (Optional[str]): Taxonomy identifier of the expression host. Defaults to None


            uniprotid (Optional[str]): Unique identifier referencing a protein entry at UniProt. Use this identifier to initialize the object from the UniProt database. Defaults to None


            ontology (SBOTerm): None. Defaults to SBOTerm.CATALYST
        """
        proteins = [
            Protein(
                name=name,
                vessel_id=vessel_id,
                constant=constant,
                sequence=sequence,
                init_conc=init_conc,
                unit=unit,
                uri=uri,
                creator_id=creator_id,
                ecnumber=ecnumber,
                organism=organism,
                organism_tax_id=organism_tax_id,
                uniprotid=uniprotid,
                ontology=ontology,
            )
        ]
        self.proteins = self.proteins + proteins

    def add_to_complexes(
        self,
        name: str,
        vessel_id: str,
        constant: bool,
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        participants: List[str] = ListPlus(),
        ontology: SBOTerm = SBOTerm.MACROMOLECULAR_COMPLEX,
    ) -> None:
        """
        Adds an instance of 'Complex' to the attribute 'complexes'.

        Args:


            name (str): None.


            vessel_id (str): None.


            constant (bool): None.


            init_conc (Optional[float]): None. Defaults to None


            unit (Optional[str]): None. Defaults to None


            uri (Optional[str]): None. Defaults to None


            creator_id (Optional[str]): None. Defaults to None


            participants (List[str]): Array of IDs the complex contains.


            ontology (SBOTerm): None. Defaults to SBOTerm.MACROMOLECULAR_COMPLEX
        """
        complexes = [
            Complex(
                name=name,
                vessel_id=vessel_id,
                constant=constant,
                init_conc=init_conc,
                unit=unit,
                uri=uri,
                creator_id=creator_id,
                participants=participants,
                ontology=ontology,
            )
        ]
        self.complexes = self.complexes + complexes

    def add_to_reactants(
        self,
        name: str,
        vessel_id: str,
        constant: bool,
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        smiles: Optional[str] = None,
        inchi: Optional[str] = None,
        chebi_id: Optional[str] = None,
        ontology: SBOTerm = SBOTerm.SMALL_MOLECULE,
    ) -> None:
        """
        Adds an instance of 'Reactant' to the attribute 'reactants'.

        Args:


            name (str): None.


            vessel_id (str): None.


            constant (bool): None.


            init_conc (Optional[float]): None. Defaults to None


            unit (Optional[str]): None. Defaults to None


            uri (Optional[str]): None. Defaults to None


            creator_id (Optional[str]): None. Defaults to None


            smiles (Optional[str]): Simplified Molecular Input Line Entry System (SMILES) encoding of the reactant. Defaults to None


            inchi (Optional[str]): International Chemical Identifier (InChI) encoding of the reactant. Defaults to None


            chebi_id (Optional[str]): Unique identifier of the CHEBI database. Use this identifier to initialize the object from the CHEBI database. Defaults to None


            ontology (SBOTerm): None. Defaults to SBOTerm.SMALL_MOLECULE
        """
        reactants = [
            Reactant(
                name=name,
                vessel_id=vessel_id,
                constant=constant,
                init_conc=init_conc,
                unit=unit,
                uri=uri,
                creator_id=creator_id,
                smiles=smiles,
                inchi=inchi,
                chebi_id=chebi_id,
                ontology=ontology,
            )
        ]
        self.reactants = self.reactants + reactants

    def add_to_reactions(
        self,
        name: str,
        temperature: float,
        temperature_unit: str,
        ph: float,
        reversible: bool = False,
        ontology: SBOTerm = SBOTerm.BIOCHEMICAL_REACTION,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        model: Optional[KineticModel] = None,
        educts: List[ReactionElement] = ListPlus(),
        products: List[ReactionElement] = ListPlus(),
        modifiers: List[ReactionElement] = ListPlus(),
    ) -> None:
        """
        Adds an instance of 'Reaction' to the attribute 'reactions'.

        Args:


            name (str): Name of the reaction.


            temperature (float): Numeric value of the temperature of the reaction.


            temperature_unit (str): Unit of the temperature of the reaction.


            ph (float): PH value of the reaction.


            reversible (bool): Whether the reaction is reversible or irreversible. Defaults to False


            ontology (SBOTerm): Ontology defining the role of the given species. Defaults to SBOTerm.BIOCHEMICAL_REACTION


            uri (Optional[str]): URI of the reaction. Defaults to None


            creator_id (Optional[str]): Unique identifier of the author. Defaults to None


            model (Optional[KineticModel]): Kinetic model decribing the reaction. Defaults to None


            educts (List[ReactionElement]): List of educts containing ReactionElement objects.


            products (List[ReactionElement]): List of products containing ReactionElement objects.


            modifiers (List[ReactionElement]): List of modifiers (Proteins, snhibitors, stimulators) containing ReactionElement objects.
        """
        reactions = [
            Reaction(
                name=name,
                temperature=temperature,
                temperature_unit=temperature_unit,
                ph=ph,
                reversible=reversible,
                ontology=ontology,
                uri=uri,
                creator_id=creator_id,
                model=model,
                educts=educts,
                products=products,
                modifiers=modifiers,
            )
        ]
        self.reactions = self.reactions + reactions

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
    ) -> None:
        """
        Adds an instance of 'Measurement' to the attribute 'measurements'.

        Args:


            name (str): Name of the measurement.


            temperature (float): Numeric value of the temperature of the reaction.


            temperature_unit (str): Unit of the temperature of the reaction.


            ph (float): PH value of the reaction.


            global_time_unit (str): Unit of the global time.


            species (List[MeasurementData]): Species of the measurement.


            global_time (List[float]): Global time of the measurement all replicates agree on.


            uri (Optional[str]): URI of the reaction. Defaults to None


            creator_id (Optional[str]): Unique identifier of the author. Defaults to None
        """
        measurements = [
            Measurement(
                name=name,
                temperature=temperature,
                temperature_unit=temperature_unit,
                ph=ph,
                global_time_unit=global_time_unit,
                species=species,
                global_time=global_time,
                uri=uri,
                creator_id=creator_id,
            )
        ]
        self.measurements = self.measurements + measurements

    def add_to_files(self, name: str, content: bytes, filetype: str) -> None:
        """
        Adds an instance of 'File' to the attribute 'files'.

        Args:


            name (str): Name of the file.


            content (bytes): Contents of the file.


            filetype (str): Type of the file such as .xml, .json and so on.
        """
        files = [File(name=name, content=content, filetype=filetype)]
        self.files = self.files + files

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
    ) -> None:
        """
        Adds an instance of 'KineticParameter' to the attribute 'global_parameters'.

        Args:


            name (str): Name of the estimated parameter.


            value (float): Numerical value of the estimated parameter.


            unit (str): Unit of the estimated parameter.


            initial_value (Optional[float]): Initial value that was used for the parameter estimation. Defaults to None


            upper (Optional[float]): Upper bound of the estimated parameter. Defaults to None


            lower (Optional[float]): Lower bound of the estimated parameter. Defaults to None


            is_global (bool): Specifies if this parameter is a global parameter. Defaults to False


            stdev (Optional[float]): Standard deviation of the estimated parameter. Defaults to None


            constant (bool): Specifies if this parameter is constant. Defaults to False


            ontology (Optional[SBOTerm]): Type of the estimated parameter. Defaults to None
        """
        global_parameters = [
            KineticParameter(
                name=name,
                value=value,
                unit=unit,
                initial_value=initial_value,
                upper=upper,
                lower=lower,
                is_global=is_global,
                stdev=stdev,
                constant=constant,
                ontology=ontology,
            )
        ]
        self.global_parameters = self.global_parameters + global_parameters
