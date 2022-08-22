# EnzymeML

EnzymeML is an XML-based data exchange format that supports the comprehensive documentation of enzymatic data by describing reaction conditions, time courses of substrate and product concentrations, the kinetic model, and the estimated kinetic constants. EnzymeML is based on the Systems Biology Markup Language, which was extended by implementing the STRENDA Guidelines. An EnzymeML document serves as a container to transfer data between experimental platforms, modeling tools, and databases. EnzymeML supports the scientific community by introducing a standardized data exchange format to make enzymatic data findable, accessible, interoperable, and reusable according to the FAIR data principles.

### EnzymeMLDocument

This is the root object that composes all objects found in an EnzymeML document. It also includes general metadata such as the name of the document, when it was created/modified and references to publications, databases and arbitrary links to the web.

- __name*__
    - Type: string
    - Description: Title of the EnzymeML Document.
- __pubmedid__
    - Type: string
    - Description: Pubmed ID reference.
- __url__
    - Type: string
    - Description: Arbitrary type of URL that is related to the EnzymeML document.
- __doi__
    - Type: string
    - Description: Digital Object Identifier of the referenced publication or the EnzymeML document.
- __created__
    - Type: datetime
    - Description: Date the EnzymeML document was created.
- __modified__
    - Type: datetime
    - Description: Date the EnzymeML document was modified.
- __creators__
    - Type: [Creator](#Creator)
    - Multiple: True
    - Description: Contains all authors that are part of the experiment.
- __vessels__
    - Type: [Vessel](#Vessel)
    - Multiple: True
    - Description: Contains all vessels that are part of the experiment.
- __proteins__
    - Type: [Protein](#Protein)
    - Multiple: True
    - Description: Contains all proteins that are part of the experiment.
- __complexes__
    - Type: [Complex](#Complex)
    - Multiple: True
    - Description: Contains all complexes that are part of the experiment.
- __reactants__
    - Type: [Reactant](#Reactant)
    - Multiple: True
    - Description: Contains all reactants that are part of the experiment.
- __reactions__
    - Type: [Reaction](#Reaction)
    - Multiple: True
    - Description: Dictionary mapping from reaction IDs to reaction describing objects.
- __measurements__
    - Type: [Measurement](#Measurement)
    - Multiple: True
    - Description: Contains measurements that describe outcomes of an experiment.
- __files__
    - Type: [File](#File)
    - Multiple: True
    - Description: Contains files attached to the data model.
- __global_parameters__
    - Type: [KineticParameter](#KineticParameter)
    - Multiple: True
    - Description: Dictionary mapping from parameter IDs to global kinetic parameter describing objects.

## General information

### Creator

The creator object contains all information about authors that contributed to the resulting document.

- __given_name*__
    - Type: string
    - Description: Given name of the author or contributor.
- __family_name*__
    - Type: string
    - Description: Family name of the author or contributor.
- __mail*__
    - Type: string
    - Description: Email address of the author or contributor.

## Species

### Vessel

This object describes vessels in which the experiment has been carried out. These can include any type of vessel used in biocatalytic experiments.

- __name*__
    - Type: string
    - Description: Name of the used vessel.
    - Template_alias: Name
- __volume*__
    - Type: posfloat
    - Description: Volumetric value of the vessel.
    - Template_alias: Volume value
- __unit*__
    - Type: string
    - Description: Volumetric unit of the vessel.
    - Template_alias: Volume unit
- __constant*__
    - Type: bool
    - Description: Whether the volume of the vessel is constant or not.
    - Default: True
- __uri__
    - Type: string
    - Description: URI of the vessel.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.

### AbstractSpecies

This object is used to inherit basic attributes common to all species used in the data model.

- __name*__
    - Type: string
    - Description: None
- __vessel_id*__
    - Type: string
    - Description: None
- __init_conc__
    - Type: float
    - Description: None
- __constant*__
    - Type: bool
    - Description: None
- __unit__
    - Type: string
    - Description: None
- __uri__
    - Type: string
    - Description: None
- __creator_id__
    - Type: string
    - Description: None

### Protein [_AbstractSpecies_]

This objects describes the proteins that were used or produced in the course of the experiment.

- __sequence*__
    - Type: string
    - Description: Amino acid sequence of the protein
    - Template_alias: Sequence
- __ecnumber__
    - Type: string
    - Description: EC number of the protein.
    - Regex: (\d+.)(\d+.)(\d+.)(\d+)
    - Template_alias: EC Number
- __organism__
    - Type: string
    - Description: Organism the protein was expressed in.
    - Template_alias: Source organism
- __organism_tax_id__
    - Type: string
    - Description: Taxonomy identifier of the expression host.
- __uniprotid__
    - Type: string
    - Description: Unique identifier referencing a protein entry at UniProt. Use this identifier to initialize the object from the UniProt database.
    - Template_alias: UniProt ID
- __ontology*__
    - Type: [SBOTerm](#SBOTerm)
    - Description: None
    - Default: SBOTerm.CATALYST

### Complex [_AbstractSpecies_]

This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment.

- __participants__
    - Type: string
    - Multiple: True
    - Description: Array of IDs the complex contains
    - Regex: [s|p][\d]+
- __ontology*__
    - Type: [SBOTerm](#SBOTerm)
    - Description: None
    - Default: SBOTerm.MACROMOLECULAR_COMPLEX

### Reactant [_AbstractSpecies_]

This objects describes the reactants that were used or produced in the course of the experiment.

- __smiles__
    - Type: string
    - Description: Simplified Molecular Input Line Entry System (SMILES) encoding of the reactant.
    - Template_alias: SMILES
- __inchi__
    - Type: string
    - Description: International Chemical Identifier (InChI) encoding of the reactant.
    - Template_alias: InCHI
- __chebi_id__
    - Type: string
    - Description: Unique identifier of the CHEBI database. Use this identifier to initialize the object from the CHEBI database.
- __ontology*__
    - Type: [SBOTerm](#SBOTerm)
    - Description: None
    - Default: SBOTerm.SMALL_MOLECULE

## Reaction

### Reaction

This object describes a chemical or enzymatic reaction that was investigated in the course of the experiment. All species used within this object need to be part of the data model.

- __name*__
    - Type: string
    - Description: Name of the reaction.
    - Template_alias: Name
- __reversible*__
    - Type: bool
    - Description: Whether the reaction is reversible or irreversible
    - Default: False
    - Template_alias: Reversible
- __temperature*__
    - Type: float
    - Description: Numeric value of the temperature of the reaction.
    - Template_alias: Temperature value
- __temperature_unit*__
    - Type: string
    - Description: Unit of the temperature of the reaction.
    - Regex: kelvin|Kelvin|k|K|celsius|Celsius|C|c
    - Template_alias: Temperature unit
- __ph*__
    - Type: float
    - Description: PH value of the reaction.
    - Template_alias: pH value
    - Inclusiveminimum: 0
    - Inclusivemaximum: 14
- __ontology*__
    - Type: [SBOTerm](#SBOTerm)
    - Default: SBOTerm.BIOCHEMICAL_REACTION
    - Description: Ontology defining the role of the given species.
- __uri__
    - Type: string
    - Description: URI of the reaction.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.
- __model__
    - Type: [KineticModel](#KineticModel)
    - Description: Kinetic model decribing the reaction.
- __educts__
    - Type: [ReactionElement](#ReactionElement)
    - Multiple: True
    - Description: List of educts containing ReactionElement objects.
    - Template_alias: Educts
- __products__
    - Type: [ReactionElement](#ReactionElement)
    - Multiple: True
    - Description: List of products containing ReactionElement objects.
    - Template_alias: Products
- __modifiers__
    - Type: [ReactionElement](#ReactionElement)
    - Multiple: True
    - Description: List of modifiers (Proteins, snhibitors, stimulators) containing ReactionElement objects.
    - Template_alias: Modifiers

### ReactionElement

This object is part of the Reaction object and describes either an educt, product or modifier. The latter includes buffers, counter-ions as well as proteins/enzymes.

- __species_id*__
    - Type: string
    - Description: Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.
- __stoichiometry*__
    - Type: posfloat
    - Description: Positive float number representing the associated stoichiometry.
- __constant*__
    - Type: bool
    - Description: Whether or not the concentration of this species remains constant.
    - Default: False
- __ontology__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Ontology defining the role of the given species.

## Modelling

### KineticModel

This object describes a kinetic model that was derived from the experiment.

- __name*__
    - Type: string
    - Description: Name of the kinetic law.
- __equation*__
    - Type: string
    - Description: Equation for the kinetic law.
- __parameters__
    - Type: [KineticParameter](#KineticParameter)
    - Multiple: True
    - Description: List of estimated parameters.
- __ontology__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Type of the estimated parameter.

### KineticParameter

This object describes the parameters of the kinetic model and can include all estimated values.

- __name*__
    - Type: string
    - Description: Name of the estimated parameter.
- __value*__
    - Type: float
    - Description: Numerical value of the estimated parameter.
- __unit*__
    - Type: string
    - Description: Unit of the estimated parameter.
- __initial_value__
    - Type: float
    - Description: Initial value that was used for the parameter estimation.
- __upper__
    - Type: float
    - Description: Upper bound of the estimated parameter.
- __lower__
    - Type: float
    - Description: Lower bound of the estimated parameter.
- __is_global*__
    - Type: bool
    - Description: Specifies if this parameter is a global parameter.
    - Default: False
- __stdev__
    - Type: float
    - Description: Standard deviation of the estimated parameter.
- __constant*__
    - Type: bool
    - Description: Specifies if this parameter is constant
    - Default: False
- __ontology__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Type of the estimated parameter.

## Time course data handling

### Measurement

This object describes the result of a measurement, which includes time course data of any type defined in DataTypes. It includes initial concentrations of all species used in a single measurement.

- __name*__
    - Type: string
    - Description: Name of the measurement
- __temperature*__
    - Type: float
    - Description: Numeric value of the temperature of the reaction.
    - Template_alias: Temperature value
- __temperature_unit*__
    - Type: string
    - Description: Unit of the temperature of the reaction.
    - Regex: kelvin|Kelvin|k|K|celsius|Celsius|C|c
- __ph*__
    - Type: float
    - Description: PH value of the reaction.
    - Inclusiveminimum: 0
    - Inclusivemaximum: 14
- __species__
    - Type: [MeasurementData](#MeasurementData)
    - Multiple: True
    - Description: Species of the measurement.
- __global_time*__
    - Type: float
    - Multiple: True
    - Description: Global time of the measurement all replicates agree on.
- __global_time_unit*__
    - Type: string
    - Description: Unit of the global time.
- __uri__
    - Type: string
    - Description: URI of the reaction.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.

### MeasurementData

This object describes a single entity of a measurement, which corresponds to one species. It also holds replicates which contain time course data.

- __init_conc*__
    - Type: float
    - Description: Initial concentration of the measurement data.
- __unit*__
    - Type: string
    - Description: The unit of the measurement data.
- __measurement_id*__
    - Type: string
    - Description: Unique measurement identifier this dataset belongs to.
- __species_id__
    - Type: string
    - Description: The identifier for the described reactant.
- __replicates__
    - Type: [Replicate](#Replicate)
    - Multiple: True
    - Description: A list of replicate objects holding raw data of the measurement.

### Replicate

This object contains the measured time course data as well as metadata to the replicate itself.

- __species_id*__
    - Type: string
    - Description: Unique identifier of the species that has been measured.
- __measurement_id*__
    - Type: string
    - Description: Unique identifier of the measurement that the replicate is part of.
- __data_type*__
    - Type: [DataTypes](#DataTypes)
    - Description: Type of data that was measured (e.g. concentration)
    - Default: DataTypes.CONCENTRATION
- __data_unit*__
    - Type: string
    - Description: SI unit of the data that was measured.
- __time_unit*__
    - Type: string
    - Description: Time unit of the replicate.
- __time*__
    - Type: float
    - Multiple: True
    - Description: Time steps of the replicate.
- __data*__
    - Type: float
    - Multiple: True
    - Description: Data that was measured.
- __is_calculated*__
    - Type: bool
    - Description: Whether or not the data has been generated by simulation.
    - Default: False
- __uri__
    - Type: string
    - Description: URI of the protein.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.

## Miscellaneous

### File

This objects contains a files that has been attached to the document.

- __name*__
    - Type: string
    - Description: Name of the file
- __content*__
    - Type: bytes
    - Description: Contents of the file
- __filetype*__
    - Type: string
    - Description: Type of the file such as .xml, .json and so on

## Ontologies

#### SBOTerm

These are a small fraction of the SBOTerms defined for the SBML markup language.

```python
BIOCHEMICAL_REACTION = "SBO:0000176"
ACID_BASE_REACTION = "SBO:0000208"
CONFORMATIONAL_TRANSITION = "SBO:0000181"
CONVERSION = "SBO:0000182"
DEGRADATION = "SBO:0000179"
DISSOCIATION = "SBO:0000180"
IONISATION = "SBO:0000209"
ISOMERISATION = "SBO:0000377"
NON_COVALENT_BINDING = "SBO:0000177"
REDOX_REACTION = "SBO:0000200"
SPONTANEOUS_REACTION = "SBO:0000672"
PROTEIN = "SBO:0000252"
GENE = "SBO:0000251"
SMALL_MOLECULE = "SBO:0000247"
ION = "SBO:0000327"
RADICAL = "SBO:0000328"
INTERACTOR = "SBO:0000336"
SUBSTRATE = "SBO:0000015"
PRODUCT = "SBO:0000011"
CATALYST = "SBO:0000013"
INHIBITOR = "SBO:0000020"
ESSENTIAL_ACTIVATOR = "SBO:0000461"
NON_ESSENTIAL_ACTIVATOR = "SBO:0000462"
POTENTIATOR = "SBO:0000021"
MACROMOLECULAR_COMPLEX = "SBO:0000296"
PROTEIN_COMPLEX = "SBO:0000297"
DIMER = "SBO:0000607"
MICHAELIS_MENTEN = "SBO:0000028"
K_CAT = "SBO:0000025"
K_M = "SBO:0000027"
V_MAX = "SBO:0000186"
```

#### DataTypes

These values are used to determine the type of time course data.

```python
CONCENTRATION = "conc"
ABSORPTION = "abs"
FEED = "feed"
BIOMASS = "biomass"
CONVERSION = "conversion"
PEAK_AREA = "peak-area"
```
