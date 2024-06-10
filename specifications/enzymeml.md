---
prefixes:
  schema: "https://schema.org/"
  OBO: "http://purl.obolibrary.org/obo/"
---

# EnzymeML

EnzymeML is an data exchange format that supports the comprehensive documentation of enzymatic data by describing reaction conditions, time courses of substrate and product concentrations, the kinetic model, and the estimated kinetic constants. EnzymeML is based on the Systems Biology Markup Language, which was extended by implementing the STRENDA Guidelines. An EnzymeML document serves as a container to transfer data between experimental platforms, modeling tools, and databases. EnzymeML supports the scientific community by introducing a standardized data exchange format to make enzymatic data findable, accessible, interoperable, and reusable according to the FAIR data principles.

## Root objects

### EnzymeMLDocument

This is the root object that composes all objects found in an EnzymeML document. It also includes general metadata such as the name of the document, when it was created/modified and references to publications, databases and arbitrary links to the web.

- __name__
  - Type: string
  - Description: Title of the EnzymeML Document.
  - Term: schema:name
- references
  - Type: Identifier[]
  - Description: Contains references to publications, databases and arbitrary links to the web.
- created
  - Type: string
  - Description: Date the EnzymeML document was created.
- modified
  - Type: string
  - Description: Date the EnzymeML document was modified.
- creators
  - Type: Creator[]
  - Description: Contains all authors that are part of the experiment.
- vessels
  - Type: Vessel[]
  - Description: Contains all vessels that are part of the experiment.
- proteins
  - Type: Protein[]
  - Description: Contains all proteins that are part of the experiment.
- complexes
  - Type: Complex[]
  - Description: Contains all complexes that are part of the experiment.
- reactants
  - Type: Reactant[]
  - Description: Contains all reactants that are part of the experiment.
- reactions
  - Type: Reaction[]
  - Description: Dictionary mapping from reaction IDs to reaction describing objects.
- conditions
  - Type: ReactionConditions
  - Description: Conditions under which the reaction was carried out.
- measurements
  - Type: Measurement[]
  - Description: Contains measurements that describe outcomes of an experiment.
- kinetic_model
  - Type: KineticModel
  - Description: Contains the kinetic model of the experiment.

## General information

### Creator (schema:creator)

The creator object contains all information about authors that contributed to the resulting document.

- __given_name__
  - Type: string
  - Description: Given name of the author or contributor.
  - Term: schema:givenName
- __family_name__
  - Type: string
  - Description: Family name of the author or contributor.
  - Term: schema:familyName
- __mail__
  - Type: string
  - Description: Email address of the author or contributor.
  - Term: schema:email

## Species

### Vessel (OBO:OBI_0400081)

This object describes vessels in which the experiment has been carried out. These can include any type of vessel used in biocatalytic experiments.

- __name__
  - Type: string
  - Description: Name of the used vessel.
  - Term: schema:name
- __volume__
  - Type: float
  - Description: Volumetric value of the vessel.
  - Template_alias: Volume value
  - Term: OBO:OBI_0002139
- __unit__
  - Type: UnitDefinition
  - Description: Volumetric unit of the vessel.
- __constant__
  - Type: boolean
  - Description: Whether the volume of the vessel is constant or not.
- creator_id
  - Type: Identifier
  - Description: Unique identifier of the author.
  - Term: schema:identifier

### Protein (schema:Protein)

This objects describes the proteins that were used or formed over the course of the experiment.

- __name__
  - Type: string
  - Term: schema:name
- __constant__
  - Type: boolean
  - Default: False
- __sequence__
  - Type: string
  - Description: Amino acid sequence of the protein
  - Term: OBO:GSSO_007262
- vessel_id
  - Type: Identifier
  - Term: schema:identifier
- ecnumber
  - Type: string
  - Description: EC number of the protein.
- organism
  - Type: string
  - Description: Organism the protein was expressed in.
  - Term: OBO:OBI_0100026
- organism_tax_id
  - Type: Identifier
  - Description: Taxonomy identifier of the expression host.
- references
  - Type: Identifier[]
  - Description: Array of references to publications, database entries etc. that describe the protein.


### Complex

This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment.

- participants
  - Type: Identifier[]
  - Description: Array of IDs the complex contains

### Reactant

This objects describes the reactants that were used or produced in the course of the experiment.

- __name__
  - Type: string
  - Term: schema:name
- __constant__
  - Type: boolean
  - Default: False
- vessel_id
  - Type: Identifier
  - Term: schema:identifier
- canonical_smiles
  - Type: string
  - Description: Canonical Simplified Molecular-Input Line-Entry System (SMILES) encoding of the reactant.
- inchikey
  - Type: string
  - Description: Hashed International Chemical Identifier (InChIKey) encoding of the reactant.
- references
  - Type: Identifier[]
  - Description: Array of references to publications, database entries etc. that describe the reactant.

## EnzymeReaction

### Reaction

This object describes a chemical or enzymatic reaction that was investigated in the course of the experiment. All species used within this object need to be part of the data model.

- __name__
  - Type: string
  - Description: Name of the reaction.
- __reversible__
  - Type: boolean
  - Description: Whether the reaction is reversible or irreversible
  - Default: False
- species
  - Type: ReactionSpecies[]
  - Description: List of reaction elements that are part of the reaction.
- modifiers
  - Type: Identifier[]
  - Description: List of reaction elements that are not part of the reaction but influence it.

### ReactionSpecies

This object is part of the Reaction object and describes either an educt, product or modifier. The latter includes buffers, counter-ions as well as proteins/enzymes.

- __species_id__
  - Type: Identifier
  - Description: Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.
- stoichiometry
  - Type: float
  - Description: Float number representing the associated stoichiometry.

### ReactionConditions

- temperature
  - Type: float
  - Description: Numeric value of the temperature of the reaction.
- temperature_unit
  - Type: UnitDefinition
  - Description: Unit of the temperature of the reaction.
- ph
  - Type: float
  - Description: PH value of the reaction.

## Modelling

### KineticModel

This object describes a kinetic model that was derived from the experiment.

- __name__
  - Type: string
  - Description: Name of the kinetic law.
- __equations__
  - Type: RateLaw[]
  - Description: Equation for the kinetic law.
- parameters
  - Type: KineticParameter[]
  - Description: List of estimated parameters.

### RateLaw

This object describes an ordinary differential equation that is part of the kinetic model.

- __species_id__
  - Type: Identifier
  - Description: Internal identifier to a species defined in the EnzymeMLDocument.
- __equation__
  - Type: Equation
  - Description: Equation of the rate law.

### KineticParameter

This object describes the parameters of the kinetic model and can include all estimated values.

- __name__
  - Type: string
  - Description: Name of the estimated parameter.
- __value__
  - Type: float
  - Description: Numerical value of the estimated parameter.
- __unit__
  - Type: UnitDefinition
  - Description: Unit of the estimated parameter.
- initial_value
  - Type: float
  - Description: Initial value that was used for the parameter estimation.
- upper
  - Type: float
  - Description: Upper bound of the estimated parameter.
- lower
  - Type: float
  - Description: Lower bound of the estimated parameter.
- stderr
  - Type: float
  - Description: Standard error of the estimated parameter.
- __constant__
  - Type: boolean
  - Description: Specifies if this parameter is constant

## Time course data handling

### Measurement

This object describes the result of a measurement, which includes time course data of any type defined in DataTypes. It includes initial concentrations of all species used in a single measurement.

- __name__
  - Type: string
  - Description: Name of the measurement
- species
  - Type: MeasurementData[]
  - Description: Species of the measurement.
- group_id
  - Type: Identifier
  - Description: User-defined group ID to signalize relationships between measurements.

### MeasurementData

This object describes a single entity of a measurement, which corresponds to one species. It also holds replicates which contain time course data.

- __species_id__
  - Type: Identifier
  - Description: The identifier for the described reactant.
- __init_conc__
  - Type: float
  - Description: Initial concentration of the measurement data.
- __data_type__
  - Type: DataTypes
  - Description: Type of data that was measured (e.g. concentration)
- __data_unit__
  - Type: UnitDefinition
  - Description: SI unit of the data that was measured.
- __time_unit__
  - Type: UnitDefinition
  - Description: Time unit of the replicate.
- __time__
  - Type: float[]
  - Description: Time steps of the replicate.
- __data__
  - Type: float[]
  - Description: Data that was measured.
- __is_calculated__
  - Type: boolean
  - Description: Whether or not the data has been generated by simulation.
  - Default: False

## Enumerations

### DataTypes

These values are used to determine the type of time course data.

```python
CONCENTRATION = "conc"
ABSORPTION = "abs"
FEED = "feed"
BIOMASS = "biomass"
CONVERSION = "conversion"
PEAK_AREA = "peak-area"
```
