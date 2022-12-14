import sdRDM

from typing import Optional
from typing import List
from typing import Optional, Union
from pydantic import PrivateAttr
from pydantic import Field
from sdRDM.base.listplus import ListPlus
from sdRDM.base.utils import forge_signature, IDGenerator
from datetime import datetime
from pydantic.types import PositiveFloat
from pydantic.types import StrictBool
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

    id: str = Field(
        description="Unique identifier of the given object.",
        default_factory=IDGenerator("enzymemldocumentINDEX"),
        xml="@id",
    )

    __repo__: Optional[str] = PrivateAttr(
        default="git://github.com/EnzymeML/enzymeml-specifications.git"
    )

    __commit__: Optional[str] = PrivateAttr(
        default="82e00b7446c13ed5ba6c191d79f2622cc9226be7"
    )

    def add_to_creators(
        self, given_name: str, family_name: str, mail: str, id: Optional[str] = None
    ) -> None:
        """
        Adds an instance of 'Creator' to the attribute 'creators'.

        Args:


            id (str): Unique identifier of the 'Creator' object. Defaults to 'None'.


            given_name (str): Given name of the author or contributor.


            family_name (str): Family name of the author or contributor.


            mail (str): Email address of the author or contributor.
        """

        params = {"given_name": given_name, "family_name": family_name, "mail": mail}
        if id is not None:
            params["id"] = id
        creators = [Creator(**params)]
        self.creators = self.creators + creators

    def add_to_vessels(
        self,
        name: str,
        volume: PositiveFloat,
        unit: str,
        constant: StrictBool = True,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Vessel' to the attribute 'vessels'.

        Args:


            id (str): Unique identifier of the 'Vessel' object. Defaults to 'None'.


            name (str): Name of the used vessel.


            volume (PositiveFloat): Volumetric value of the vessel.


            unit (str): Volumetric unit of the vessel.


            constant (StrictBool): Whether the volume of the vessel is constant or not. Defaults to True


            uri (Optional[str]): URI of the vessel. Defaults to None


            creator_id (Optional[str]): Unique identifier of the author. Defaults to None
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
        vessels = [Vessel(**params)]
        self.vessels = self.vessels + vessels

    def add_to_proteins(
        self,
        name: str,
        vessel_id: str,
        constant: StrictBool,
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
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Protein' to the attribute 'proteins'.

        Args:


            id (str): Unique identifier of the 'Protein' object. Defaults to 'None'.


            name (str): None.


            vessel_id (str): None.


            constant (StrictBool): None.


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

        params = {
            "name": name,
            "vessel_id": vessel_id,
            "constant": constant,
            "sequence": sequence,
            "init_conc": init_conc,
            "unit": unit,
            "uri": uri,
            "creator_id": creator_id,
            "ecnumber": ecnumber,
            "organism": organism,
            "organism_tax_id": organism_tax_id,
            "uniprotid": uniprotid,
            "ontology": ontology,
        }
        if id is not None:
            params["id"] = id
        proteins = [Protein(**params)]
        self.proteins = self.proteins + proteins

    def add_to_complexes(
        self,
        name: str,
        vessel_id: str,
        constant: StrictBool,
        participants: List[str],
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        ontology: SBOTerm = SBOTerm.MACROMOLECULAR_COMPLEX,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Complex' to the attribute 'complexes'.

        Args:


            id (str): Unique identifier of the 'Complex' object. Defaults to 'None'.


            name (str): None.


            vessel_id (str): None.


            constant (StrictBool): None.


            participants (List[str]): Array of IDs the complex contains.


            init_conc (Optional[float]): None. Defaults to None


            unit (Optional[str]): None. Defaults to None


            uri (Optional[str]): None. Defaults to None


            creator_id (Optional[str]): None. Defaults to None


            ontology (SBOTerm): None. Defaults to SBOTerm.MACROMOLECULAR_COMPLEX
        """

        params = {
            "name": name,
            "vessel_id": vessel_id,
            "constant": constant,
            "participants": participants,
            "init_conc": init_conc,
            "unit": unit,
            "uri": uri,
            "creator_id": creator_id,
            "ontology": ontology,
        }
        if id is not None:
            params["id"] = id
        complexes = [Complex(**params)]
        self.complexes = self.complexes + complexes

    def add_to_reactants(
        self,
        name: str,
        vessel_id: str,
        constant: StrictBool,
        init_conc: Optional[float] = None,
        unit: Optional[str] = None,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        smiles: Optional[str] = None,
        inchi: Optional[str] = None,
        chebi_id: Optional[str] = None,
        ontology: SBOTerm = SBOTerm.SMALL_MOLECULE,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Reactant' to the attribute 'reactants'.

        Args:


            id (str): Unique identifier of the 'Reactant' object. Defaults to 'None'.


            name (str): None.


            vessel_id (str): None.


            constant (StrictBool): None.


            init_conc (Optional[float]): None. Defaults to None


            unit (Optional[str]): None. Defaults to None


            uri (Optional[str]): None. Defaults to None


            creator_id (Optional[str]): None. Defaults to None


            smiles (Optional[str]): Simplified Molecular Input Line Entry System (SMILES) encoding of the reactant. Defaults to None


            inchi (Optional[str]): International Chemical Identifier (InChI) encoding of the reactant. Defaults to None


            chebi_id (Optional[str]): Unique identifier of the CHEBI database. Use this identifier to initialize the object from the CHEBI database. Defaults to None


            ontology (SBOTerm): None. Defaults to SBOTerm.SMALL_MOLECULE
        """

        params = {
            "name": name,
            "vessel_id": vessel_id,
            "constant": constant,
            "init_conc": init_conc,
            "unit": unit,
            "uri": uri,
            "creator_id": creator_id,
            "smiles": smiles,
            "inchi": inchi,
            "chebi_id": chebi_id,
            "ontology": ontology,
        }
        if id is not None:
            params["id"] = id
        reactants = [Reactant(**params)]
        self.reactants = self.reactants + reactants

    def add_to_reactions(
        self,
        name: str,
        educts: List[ReactionElement],
        products: List[ReactionElement],
        modifiers: List[ReactionElement],
        reversible: bool = False,
        temperature: Optional[float] = None,
        temperature_unit: Optional[str] = None,
        ph: Optional[float] = None,
        ontology: SBOTerm = SBOTerm.BIOCHEMICAL_REACTION,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        model: Optional[KineticModel] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Reaction' to the attribute 'reactions'.

        Args:


            id (str): Unique identifier of the 'Reaction' object. Defaults to 'None'.


            name (str): Name of the reaction.


            educts (List[ReactionElement]): List of educts containing ReactionElement objects.


            products (List[ReactionElement]): List of products containing ReactionElement objects.


            modifiers (List[ReactionElement]): List of modifiers (Proteins, snhibitors, stimulators) containing ReactionElement objects.


            reversible (bool): Whether the reaction is reversible or irreversible. Defaults to False


            temperature (Optional[float]): Numeric value of the temperature of the reaction. Defaults to None


            temperature_unit (Optional[str]): Unit of the temperature of the reaction. Defaults to None


            ph (Optional[float]): PH value of the reaction. Defaults to None


            ontology (SBOTerm): Ontology defining the role of the given species. Defaults to SBOTerm.BIOCHEMICAL_REACTION


            uri (Optional[str]): URI of the reaction. Defaults to None


            creator_id (Optional[str]): Unique identifier of the author. Defaults to None


            model (Optional[KineticModel]): Kinetic model decribing the reaction. Defaults to None
        """

        params = {
            "name": name,
            "educts": educts,
            "products": products,
            "modifiers": modifiers,
            "reversible": reversible,
            "temperature": temperature,
            "temperature_unit": temperature_unit,
            "ph": ph,
            "ontology": ontology,
            "uri": uri,
            "creator_id": creator_id,
            "model": model,
        }
        if id is not None:
            params["id"] = id
        reactions = [Reaction(**params)]
        self.reactions = self.reactions + reactions

    def add_to_measurements(
        self,
        name: str,
        temperature: float,
        temperature_unit: str,
        ph: float,
        species: List[MeasurementData],
        global_time: List[float],
        global_time_unit: str,
        uri: Optional[str] = None,
        creator_id: Optional[str] = None,
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'Measurement' to the attribute 'measurements'.

        Args:


            id (str): Unique identifier of the 'Measurement' object. Defaults to 'None'.


            name (str): Name of the measurement.


            temperature (float): Numeric value of the temperature of the reaction.


            temperature_unit (str): Unit of the temperature of the reaction.


            ph (float): PH value of the reaction.


            species (List[MeasurementData]): Species of the measurement.


            global_time (List[float]): Global time of the measurement all replicates agree on.


            global_time_unit (str): Unit of the global time.


            uri (Optional[str]): URI of the reaction. Defaults to None


            creator_id (Optional[str]): Unique identifier of the author. Defaults to None
        """

        params = {
            "name": name,
            "temperature": temperature,
            "temperature_unit": temperature_unit,
            "ph": ph,
            "species": species,
            "global_time": global_time,
            "global_time_unit": global_time_unit,
            "uri": uri,
            "creator_id": creator_id,
        }
        if id is not None:
            params["id"] = id
        measurements = [Measurement(**params)]
        self.measurements = self.measurements + measurements

    def add_to_files(
        self, name: str, content: bytes, filetype: str, id: Optional[str] = None
    ) -> None:
        """
        Adds an instance of 'File' to the attribute 'files'.

        Args:


            id (str): Unique identifier of the 'File' object. Defaults to 'None'.


            name (str): Name of the file.


            content (bytes): Contents of the file.


            filetype (str): Type of the file such as .xml, .json and so on.
        """

        params = {"name": name, "content": content, "filetype": filetype}
        if id is not None:
            params["id"] = id
        files = [File(**params)]
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
        id: Optional[str] = None,
    ) -> None:
        """
        Adds an instance of 'KineticParameter' to the attribute 'global_parameters'.

        Args:


            id (str): Unique identifier of the 'KineticParameter' object. Defaults to 'None'.


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
        global_parameters = [KineticParameter(**params)]
        self.global_parameters = self.global_parameters + global_parameters
