---
hide:
    - navigation
---

# EnzymeML

This page provides comprehensive information about the structure and components of the data model, including detailed descriptions of the types and their properties, information on enumerations, and an overview of the ontologies used and their associated prefixes. Below, you will find a graph that visually represents the overall structure of the data model.

??? quote "Graph"
    ``` mermaid
    flowchart TB
        enzymemldocument(EnzymeMLDocument)
        creator(Creator)
        vessel(Vessel)
        protein(Protein)
        complex(Complex)
        reactant(Reactant)
        reaction(Reaction)
        reactionspecies(ReactionSpecies)
        reactionconditions(ReactionConditions)
        kineticmodel(KineticModel)
        ratelaw(RateLaw)
        kineticparameter(KineticParameter)
        measurement(Measurement)
        measurementdata(MeasurementData)
        equation(Equation)
        eqvariable(EqVariable)
        eqparameter(EqParameter)
        unitdefinition(UnitDefinition)
        baseunit(BaseUnit)
        datatypes(DataTypes)
        unittype(UnitType)
        enzymemldocument(EnzymeMLDocument) --> creator(Creator)
        enzymemldocument(EnzymeMLDocument) --> vessel(Vessel)
        enzymemldocument(EnzymeMLDocument) --> protein(Protein)
        enzymemldocument(EnzymeMLDocument) --> complex(Complex)
        enzymemldocument(EnzymeMLDocument) --> reactant(Reactant)
        enzymemldocument(EnzymeMLDocument) --> reaction(Reaction)
        enzymemldocument(EnzymeMLDocument) --> reactionconditions(ReactionConditions)
        enzymemldocument(EnzymeMLDocument) --> measurement(Measurement)
        enzymemldocument(EnzymeMLDocument) --> kineticmodel(KineticModel)
        vessel(Vessel) --> unitdefinition(UnitDefinition)
        reaction(Reaction) --> reactionspecies(ReactionSpecies)
        reactionconditions(ReactionConditions) --> unitdefinition(UnitDefinition)
        kineticmodel(KineticModel) --> ratelaw(RateLaw)
        kineticmodel(KineticModel) --> kineticparameter(KineticParameter)
        ratelaw(RateLaw) --> equation(Equation)
        kineticparameter(KineticParameter) --> unitdefinition(UnitDefinition)
        measurement(Measurement) --> measurementdata(MeasurementData)
        measurementdata(MeasurementData) --> datatypes(DataTypes)
        measurementdata(MeasurementData) --> unitdefinition(UnitDefinition)
        measurementdata(MeasurementData) --> unitdefinition(UnitDefinition)
        equation(Equation) --> eqvariable(EqVariable)
        equation(Equation) --> eqparameter(EqParameter)
        unitdefinition(UnitDefinition) --> baseunit(BaseUnit)
        baseunit(BaseUnit) --> unittype(UnitType)

        click enzymemldocument "#enzymemldocument" "Go to EnzymeMLDocument"
        click creator "#creator" "Go to Creator"
        click vessel "#vessel" "Go to Vessel"
        click protein "#protein" "Go to Protein"
        click complex "#complex" "Go to Complex"
        click reactant "#reactant" "Go to Reactant"
        click reaction "#reaction" "Go to Reaction"
        click reactionspecies "#reactionspecies" "Go to ReactionSpecies"
        click reactionconditions "#reactionconditions" "Go to ReactionConditions"
        click kineticmodel "#kineticmodel" "Go to KineticModel"
        click ratelaw "#ratelaw" "Go to RateLaw"
        click kineticparameter "#kineticparameter" "Go to KineticParameter"
        click measurement "#measurement" "Go to Measurement"
        click measurementdata "#measurementdata" "Go to MeasurementData"
        click equation "#equation" "Go to Equation"
        click eqvariable "#eqvariable" "Go to EqVariable"
        click eqparameter "#eqparameter" "Go to EqParameter"
        click unitdefinition "#unitdefinition" "Go to UnitDefinition"
        click baseunit "#baseunit" "Go to BaseUnit"
        click datatypes "#datatypes" "Go to DataTypes"
        click unittype "#unittype" "Go to UnitType"
    ```


## Ontologies
- [OBO](http://purl.obolibrary.org/obo/)
- [schema](https://schema.org/)


## Types


### EnzymeMLDocument
This is the root object that composes all objects found in an EnzymeML document. It also includes general metadata such as the name of the document, when it was created/modified and references to publications, databases and arbitrary links to the web.

__name__* `string`

- Title of the EnzymeML Document.


__references__ `list[string]`

- Contains references to publications, databases and arbitrary links to the web.


__created__ `string`

- Date the EnzymeML document was created.


__modified__ `string`

- Date the EnzymeML document was modified.


__creators__ [`list[Creator]`](#creator)

- Contains all authors that are part of the experiment.


__vessels__ [`list[Vessel]`](#vessel)

- Contains all vessels that are part of the experiment.


__proteins__ [`list[Protein]`](#protein)

- Contains all proteins that are part of the experiment.


__complexes__ [`list[Complex]`](#complex)

- Contains all complexes that are part of the experiment.


__reactants__ [`list[Reactant]`](#reactant)

- Contains all reactants that are part of the experiment.


__reactions__ [`list[Reaction]`](#reaction)

- Dictionary mapping from reaction IDs to reaction describing objects.


__conditions__ [`ReactionConditions`](#reactionconditions)

- Conditions under which the reaction was carried out.


__measurements__ [`list[Measurement]`](#measurement)

- Contains measurements that describe outcomes of an experiment.


__kinetic_model__ [`KineticModel`](#kineticmodel)

- Contains the kinetic model of the experiment.


------

### Creator
The creator object contains all information about authors that contributed to the resulting document.

__given_name__* `string`

- Given name of the author or contributor.


__family_name__* `string`

- Family name of the author or contributor.


__mail__* `string`

- Email address of the author or contributor.


------

### Vessel
This object describes vessels in which the experiment has been carried out. These can include any type of vessel used in biocatalytic experiments.

__name__* `string`

- Name of the used vessel.


__volume__* `float`

- Volumetric value of the vessel.
- `Template_alias`: Volume value

__unit__* [`UnitDefinition`](#unitdefinition)

- Volumetric unit of the vessel.


__constant__* `boolean`

- Whether the volume of the vessel is constant or not.


__creator_id__ `string`

- Unique identifier of the author.


------

### Protein
This objects describes the proteins that were used or formed over the course of the experiment.

__name__* `string`


__sequence__* `string`

- Amino acid sequence of the protein


__constant__* `boolean`


- `Default`: false

__vessel_id__ `string`


__ecnumber__ `string`

- EC number of the protein.


__organism__ `string`

- Organism the protein was expressed in.


__organism_tax_id__ `string`

- Taxonomy identifier of the expression host.


__references__ `list[string]`

- Array of references to publications, database entries etc. that describe the protein.


------

### Complex
This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment.

__participants__ `list[string]`

- Array of IDs the complex contains


------

### Reactant
This objects describes the reactants that were used or produced in the course of the experiment.

__name__* `string`


__constant__* `boolean`


- `Default`: false

__vessel_id__ `string`


__canonical_smiles__ `string`

- Canonical Simplified Molecular-Input Line-Entry System (SMILES) encoding of the reactant.


__inchikey__ `string`

- Hashed International Chemical Identifier (InChIKey) encoding of the reactant.


__references__ `list[string]`

- Array of references to publications, database entries etc. that describe the reactant.


------

### Reaction
This object describes a chemical or enzymatic reaction that was investigated in the course of the experiment. All species used within this object need to be part of the data model.

__name__* `string`

- Name of the reaction.


__reversible__* `boolean`

- Whether the reaction is reversible or irreversible

- `Default`: false

__species__ [`list[ReactionSpecies]`](#reactionspecies)

- List of reaction elements that are part of the reaction.


__modifiers__ `list[string]`

- List of reaction elements that are not part of the reaction but influence it.


------

### ReactionSpecies
This object is part of the Reaction object and describes either an educt, product or modifier. The latter includes buffers, counter-ions as well as proteins/enzymes.

__species_id__* `string`

- Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.


__stoichiometry__ `float`

- Float number representing the associated stoichiometry.


------

### ReactionConditions


__temperature__ `float`

- Numeric value of the temperature of the reaction.


__temperature_unit__ [`UnitDefinition`](#unitdefinition)

- Unit of the temperature of the reaction.


__ph__ `float`

- PH value of the reaction.


------

### KineticModel
This object describes a kinetic model that was derived from the experiment.

__name__* `string`

- Name of the kinetic law.


__equations__* [`list[RateLaw]`](#ratelaw)

- Equation for the kinetic law.


__parameters__ [`list[KineticParameter]`](#kineticparameter)

- List of estimated parameters.


------

### RateLaw
This object describes an ordinary differential equation that is part of the kinetic model.

__species_id__* `string`

- Internal identifier to a species defined in the EnzymeMLDocument.


__equation__* [`Equation`](#equation)

- Equation of the rate law.


------

### KineticParameter
This object describes the parameters of the kinetic model and can include all estimated values.

__name__* `string`

- Name of the estimated parameter.


__value__* `float`

- Numerical value of the estimated parameter.


__unit__* [`UnitDefinition`](#unitdefinition)

- Unit of the estimated parameter.


__constant__* `boolean`

- Specifies if this parameter is constant


__initial_value__ `float`

- Initial value that was used for the parameter estimation.


__upper__ `float`

- Upper bound of the estimated parameter.


__lower__ `float`

- Lower bound of the estimated parameter.


__stderr__ `float`

- Standard error of the estimated parameter.


------

### Measurement
This object describes the result of a measurement, which includes time course data of any type defined in DataTypes. It includes initial concentrations of all species used in a single measurement.

__name__* `string`

- Name of the measurement


__species__ [`list[MeasurementData]`](#measurementdata)

- Species of the measurement.


__group_id__ `string`

- User-defined group ID to signalize relationships between measurements.


------

### MeasurementData
This object describes a single entity of a measurement, which corresponds to one species. It also holds replicates which contain time course data.

__species_id__* `string`

- The identifier for the described reactant.


__init_conc__* `float`

- Initial concentration of the measurement data.


__data_type__* [`DataTypes`](#datatypes)

- Type of data that was measured (e.g. concentration)


__data_unit__* [`UnitDefinition`](#unitdefinition)

- SI unit of the data that was measured.


__time_unit__* [`UnitDefinition`](#unitdefinition)

- Time unit of the replicate.


__time__* `list[float]`

- Time steps of the replicate.


__data__* `list[float]`

- Data that was measured.


__is_calculated__* `boolean`

- Whether or not the data has been generated by simulation.

- `Default`: false

------

### Equation
Represents an equation that can be used in a data model.

__id__ `string`

- Unique identifier for the equation.


__equation__ `string`

- The equation that is used in the data model.


__variables__ [`list[EqVariable]`](#eqvariable)

- List of variables that are used in the equation.


__parameters__ [`list[EqParameter]`](#eqparameter)

- List of parameters that are used in the equation.


------

### EqVariable
Represents a variable that is used in the equation.

__id__ `string`

- Unique identifier for the variable.


__name__ `string`

- Name of the variable.


__symbol__ `string`

- Symbol of the variable.


------

### EqParameter
Represents a parameter that is used in the equation.

__id__ `string`

- Unique identifier for the parameter.


__name__ `string`

- Name of the parameter.


__symbol__ `string`

- Symbol of the parameter.


__value__ `float`

- Value of the parameter.


------

### UnitDefinition
Represents a unit definition that is based on the SI unit system.

__id__ `string`

- Unique identifier for the unit definition.


__base_units__ [`list[BaseUnit]`](#baseunit)

- Base units that define the unit.


------

### BaseUnit
Represents a base unit in the unit definition.

__kind__* [`UnitType`](#unittype)

- Kind of the base unit (e.g., meter, kilogram, second).


__exponent__* `integer`

- Exponent of the base unit in the unit definition.


__multiplier__ `float`

- Multiplier of the base unit in the unit definition.


__scale__ `float`

- Scale of the base unit in the unit definition.


## Enumerations

### DataTypes

| Alias | Value |
|-------|-------|
| `ABSORPTION` | abs |
| `BIOMASS` | biomass |
| `CONCENTRATION` | conc |
| `CONVERSION` | conversion |
| `FEED` | feed |
| `PEAK_AREA` | peak-area |

### UnitType

| Alias | Value |
|-------|-------|
| `AMPERE` | ampere |
| `AVOGADRO` | avogadro |
| `BECQUEREL` | becquerel |
| `CANDELA` | candela |
| `COULOMB` | coulomb |
| `DIMENSIONLESS` | dimensionless |
| `FARAD` | farad |
| `GRAM` | gram |
| `GRAY` | gray |
| `HENRY` | henry |
| `HERTZ` | hertz |
| `ITEM` | item |
| `JOULE` | joule |
| `KATAL` | katal |
| `KELVIN` | kelvin |
| `KILOGRAM` | kilogram |
| `LITRE` | litre |
| `LUMEN` | lumen |
| `LUX` | lux |
| `METRE` | metre |
| `MOLE` | mole |
| `NEWTON` | newton |
| `OHM` | ohm |
| `PASCAL` | pascal |
| `RADIAN` | radian |
| `SECOND` | second |
| `SIEMENS` | siemens |
| `SIEVERT` | sievert |
| `STERADIAN` | steradian |
| `TESLA` | tesla |
| `VOLT` | volt |
| `WATT` | watt |
| `WEBER` | weber |