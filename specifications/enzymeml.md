### EnzymeMLDocument

- __name__
    - Type: string
    - Description: Title of the EnzymeML Document.
- __level*__
    - Type: int
    - Description: SBML evel of the EnzymeML XML.
    - Inclusiveminimum: 1
    - Inclusivemaximum: 3
- __version*__
    - Type: int
    - Description: SBML version of the EnzymeML XML.
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
    - Type: string
    - Description: Date the EnzymeML document was created.
- __modified__
    - Type: string
    - Description: Date the EnzymeML document was modified.
- __creators__
    - Type: [Creator](#Creator)
    - Multiple: True
    - Description: Dictionary mapping from creator IDs to creator describing objects.
- __vessels__
    - Type: [Vessel](#Vessel)
    - Multiple: True
    - Description: Dictionary mapping from vessel IDs to vessel describing objects.
- __proteins__
    - Type: [Protein](#Protein)
    - Multiple: True
    - Description: Dictionary mapping from protein IDs to protein describing objects.
- __complexes__
    - Type: [Complex](#Complex)
    - Multiple: True
    - Description: Dictionary mapping from complex IDs to complex describing objects.
- __reactants__
    - Type: [Reactant](#Reactant)
    - Multiple: True
    - Description: Dictionary mapping from reactant IDs to reactant describing objects.
- __reactions__
    - Type: [EnzymeReaction](#EnzymeReaction)
    - Multiple: True
    - Description: Dictionary mapping from reaction IDs to reaction describing objects.
- __measurements__
    - Type: [Measurement](#Measurement)
    - Multiple: True
    - Description: Dictionary mapping from measurement IDs to measurement describing objects.
- __files__
    - Type: [dict](#dict)
    - Multiple: True
    - Description: Dictionary mapping from protein IDs to protein describing objects.
- __global_parameters__
    - Type: [KineticParameter](#KineticParameter)
    - Multiple: True
    - Description: Dictionary mapping from parameter IDs to global kinetic parameter describing objects.
- __log*__
    - Type: string
    - Description: None

### Creator

- __given_name__
    - Type: string
    - Description: Given name of the author or contributor.
- __family_name__
    - Type: string
    - Description: Family name of the author or contributor.
- __mail__
    - Type: string
    - Description: Email address of the author or contributor.
- __id__
    - Type: string
    - Description: Unique identifier of the protein.
    - Regex: a[\d]+

### Vessel

- __name__
    - Type: string
    - Description: Name of the used vessel.
    - Template_alias: Name
- __volume__
    - Type: [PositiveFloat](#PositiveFloat)
    - Description: Volumetric value of the vessel.
    - Template_alias: Volume value
- __unit__
    - Type: string
    - Description: Volumetric unit of the vessel.
    - Template_alias: Volume unit
- __constant*__
    - Type: bool
    - Description: Whether the volume of the vessel is constant or not.
- __meta_id__
    - Type: string
    - Description: Unique meta identifier of the vessel.
- __id__
    - Type: string
    - Description: Unique identifier of the vessel.
    - Regex: v[\d]+
    - Template_alias: ID
- __uri__
    - Type: string
    - Description: URI of the vessel.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.

### Protein

- __name__
    - Type: string
    - Description: Name of the protein
    - Template_alias: Name
- __meta_id__
    - Type: string
    - Description: Unique meta identifier of the protein.
- __id__
    - Type: string
    - Description: Unique identifier of the protein.
    - Regex: p[\d]+
    - Template_alias: ID
- __vessel_id__
    - Type: string
    - Description: Identifier of the vessel in which the protein was stored.
    - Regex: v[\d.]+
    - Template_alias: Vessel
- __init_conc__
    - Type: float
    - Description: Initial concentration of the protein.
- __constant*__
    - Type: bool
    - Description: Whether the proteins concentration remains constant or not.
    - Template_alias: Constant
- __boundary*__
    - Type: bool
    - Description: Whether the protein is under any boundary conditions (SBML Technicality, better leave it to default)
- __unit__
    - Type: string
    - Description: Unit of the proteins intial concentration.
- __ontology*__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Ontology describing the characteristic of the protein.
- __uri__
    - Type: string
    - Description: URI of the protein.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.
- __sequence__
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

### Complex

- __name__
    - Type: string
    - Description: Name of the complex
- __meta_id__
    - Type: string
    - Description: Unique meta identifier of the protein.
- __id__
    - Type: string
    - Description: Unique identifier of the protein.
    - Regex: c[\d]+
- __vessel_id__
    - Type: string
    - Description: Identifier of the vessel in which the protein was stored.
    - Regex: v[\d]+
- __init_conc__
    - Type: float
    - Description: Initial concentration of the protein.
    - Inclusiveminimum: 0.0
- __constant*__
    - Type: bool
    - Description: Whether the proteins concentration remains constant or not.
- __boundary*__
    - Type: bool
    - Description: Whether the protein is under any boundary conditions (SBML Technicality, better leave it to default)
- __unit__
    - Type: string
    - Description: Unit of the proteins intial concentration.
- __ontology*__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Ontology describing the characteristic of the protein.
- __uri__
    - Type: string
    - Description: URI of the protein.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.
- __participants__
    - Type: string
    - Multiple: True
    - Description: Array of IDs the complex contains

### Reactant

- __name__
    - Type: string
    - Description: Name of the reactant.
    - Template_alias: Name
- __meta_id__
    - Type: string
    - Description: Unique meta identifier of the protein.
- __id__
    - Type: string
    - Description: Unique identifier of the protein.
    - Regex: s[\d]+
    - Template_alias: ID
- __vessel_id__
    - Type: string
    - Description: Identifier of the vessel in which the reactant was stored.
    - Template_alias: Vessel
- __init_conc__
    - Type: float
    - Description: Initial concentration of the reactant.
- __constant*__
    - Type: bool
    - Description: Whether the reactants concentration remains constant or not.
    - Template_alias: Constant
- __boundary*__
    - Type: bool
    - Description: Whether the reactant is under any boundary conditions (SBML Technicality, better leave it to default)
- __unit__
    - Type: string
    - Description: Unit of the reactant intial concentration.
- __ontology*__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Ontology describing the characteristic of the reactant.
- __uri__
    - Type: string
    - Description: URI of the protein.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.
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

### EnzymeReaction

- __name__
    - Type: string
    - Description: Name of the reaction.
    - Template_alias: Name
- __reversible__
    - Type: bool
    - Description: Whether the reaction is reversible or irreversible
    - Template_alias: Reversible
- __temperature__
    - Type: float
    - Description: Numeric value of the temperature of the reaction.
    - Template_alias: Temperature value
- __temperature_unit__
    - Type: string
    - Description: Unit of the temperature of the reaction.
    - Regex: kelvin|Kelvin|k|K|celsius|Celsius|C|c
    - Template_alias: Temperature unit
- __ph__
    - Type: float
    - Description: PH value of the reaction.
    - Template_alias: pH value
    - Inclusiveminimum: 0
    - Inclusivemaximum: 14
- __ontology*__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Ontology defining the role of the given species.
- __meta_id__
    - Type: string
    - Description: Unique meta identifier for the reaction.
- __id__
    - Type: string
    - Description: Unique identifier of the reaction.
    - Regex: r[\d]+
    - Template_alias: ID
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

### KineticModel

- __name__
    - Type: string
    - Description: Name of the kinetic law.
- __equation__
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

- __name__
    - Type: string
    - Description: Name of the estimated parameter.
- __value__
    - Type: float
    - Description: Numerical value of the estimated parameter.
- __unit__
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
- __stdev__
    - Type: float
    - Description: Standard deviation of the estimated parameter.
- __constant*__
    - Type: bool
    - Description: Specifies if this parameter is constant
- __ontology__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Type of the estimated parameter.

### ReactionElement

- __species_id__
    - Type: string
    - Description: Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.
- __stoichiometry__
    - Type: [PositiveFloat](#PositiveFloat)
    - Description: Positive float number representing the associated stoichiometry.
- __constant__
    - Type: bool
    - Description: Whether or not the concentration of this species remains constant.
- __ontology__
    - Type: [SBOTerm](#SBOTerm)
    - Description: Ontology defining the role of the given species.

### Measurement

- __name__
    - Type: string
    - Description: Name of the measurement
- __temperature__
    - Type: float
    - Description: Numeric value of the temperature of the reaction.
    - Template_alias: Temperature value
- __temperature_unit__
    - Type: string
    - Description: Unit of the temperature of the reaction.
    - Regex: kelvin|Kelvin|k|K|celsius|Celsius|C|c
- __ph__
    - Type: float
    - Description: PH value of the reaction.
    - Inclusiveminimum: 0
    - Inclusivemaximum: 14
- __species_dict*__
    - Type: [MeasurementData](#MeasurementData)
    - Multiple: True
    - Description: Species of the measurement.
- __global_time__
    - Type: float
    - Multiple: True
    - Description: Global time of the measurement all replicates agree on.
- __global_time_unit__
    - Type: string
    - Description: Unit of the global time.
- __id__
    - Type: string
    - Description: Unique identifier of the measurement.
    - Regex: m[\d]+
- __uri__
    - Type: string
    - Description: URI of the reaction.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.

### MeasurementData

- __init_conc__
    - Type: float
    - Description: Initial concentration of the measurement data.
- __unit__
    - Type: string
    - Description: The unit of the measurement data.
- __measurement_id__
    - Type: string
    - Description: Unique measurement identifier this dataset belongs to.
- __reactant_id__
    - Type: string
    - Description: The identifier for the described reactant.
- __protein_id__
    - Type: string
    - Description: The identifier for the described protein.
- __replicates__
    - Type: [Replicate](#Replicate)
    - Multiple: True
    - Description: A list of replicate objects holding raw data of the measurement.

### Replicate

- __id__
    - Type: string
    - Description: Unique identifier of the replicate
- __species_id__
    - Type: string
    - Description: Unique identifier of the species that has been measured.
    - Regex: [s|r|p][\d]+
- __measurement_id__
    - Type: string
    - Description: Unique identifier of the measurement that the replicate is part of.
    - Regex: m[\d]+
- __data_type*__
    - Type: [DataTypes](#DataTypes)
    - Description: Type of data that was measured (e.g. concentration)
- __data_unit__
    - Type: string
    - Description: SI unit of the data that was measured.
- __time_unit__
    - Type: string
    - Description: Time unit of the replicate.
- __time__
    - Type: float
    - Multiple: True
    - Description: Time steps of the replicate.
- __data__
    - Type: float
    - Multiple: True
    - Description: Data that was measured.
- __is_calculated*__
    - Type: bool
    - Description: Whether or not the data has been generated by simulation.
- __uri__
    - Type: string
    - Description: URI of the protein.
- __creator_id__
    - Type: string
    - Description: Unique identifier of the author.

## Ontologies

#### SBOTerm

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

```python
CONCENTRATION = "conc"
ABSORPTION = "abs"
FEED = "feed"
BIOMASS = "biomass"
CONVERSION = "conversion"
PEAK_AREA = "peak-area"
```
