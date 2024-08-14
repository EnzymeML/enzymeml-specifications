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
        smallmolecule(SmallMolecule)
        reaction(Reaction)
        reactionelement(ReactionElement)
        equation(Equation)
        variable(Variable)
        parameter(Parameter)
        measurement(Measurement)
        measurementdata(MeasurementData)
        unitdefinition(UnitDefinition)
        baseunit(BaseUnit)
        equationtype(EquationType)
        datatypes(DataTypes)
        unittype(UnitType)
        enzymemldocument(EnzymeMLDocument) --> creator(Creator)
        enzymemldocument(EnzymeMLDocument) --> vessel(Vessel)
        enzymemldocument(EnzymeMLDocument) --> protein(Protein)
        enzymemldocument(EnzymeMLDocument) --> complex(Complex)
        enzymemldocument(EnzymeMLDocument) --> smallmolecule(SmallMolecule)
        enzymemldocument(EnzymeMLDocument) --> reaction(Reaction)
        enzymemldocument(EnzymeMLDocument) --> measurement(Measurement)
        enzymemldocument(EnzymeMLDocument) --> equation(Equation)
        vessel(Vessel) --> unitdefinition(UnitDefinition)
        reaction(Reaction) --> equation(Equation)
        reaction(Reaction) --> reactionelement(ReactionElement)
        equation(Equation) --> unitdefinition(UnitDefinition)
        equation(Equation) --> equationtype(EquationType)
        equation(Equation) --> variable(Variable)
        equation(Equation) --> parameter(Parameter)
        parameter(Parameter) --> unitdefinition(UnitDefinition)
        measurement(Measurement) --> measurementdata(MeasurementData)
        measurement(Measurement) --> unitdefinition(UnitDefinition)
        measurementdata(MeasurementData) --> unitdefinition(UnitDefinition)
        measurementdata(MeasurementData) --> unitdefinition(UnitDefinition)
        unitdefinition(UnitDefinition) --> baseunit(BaseUnit)
        baseunit(BaseUnit) --> unittype(UnitType)

        click enzymemldocument "#enzymemldocument" "Go to EnzymeMLDocument"
        click creator "#creator" "Go to Creator"
        click vessel "#vessel" "Go to Vessel"
        click protein "#protein" "Go to Protein"
        click complex "#complex" "Go to Complex"
        click smallmolecule "#smallmolecule" "Go to SmallMolecule"
        click reaction "#reaction" "Go to Reaction"
        click reactionelement "#reactionelement" "Go to ReactionElement"
        click equation "#equation" "Go to Equation"
        click variable "#variable" "Go to Variable"
        click parameter "#parameter" "Go to Parameter"
        click measurement "#measurement" "Go to Measurement"
        click measurementdata "#measurementdata" "Go to MeasurementData"
        click unitdefinition "#unitdefinition" "Go to UnitDefinition"
        click baseunit "#baseunit" "Go to BaseUnit"
        click equationtype "#equationtype" "Go to EquationType"
        click datatypes "#datatypes" "Go to DataTypes"
        click unittype "#unittype" "Go to UnitType"
    ```


## Ontologies
- [OBO](http://purl.obolibrary.org/obo/)
- [schema](https://schema.org/)


## Types


### EnzymeMLDocument
This is the root object that composes all objects found in an EnzymeML document. It also includes general metadata such as the name of the document, when it was created/modified, and references to publications, databases, and arbitrary links to the web.

__name__* `string`

- Title of the EnzymeML Document.


__references__ `list[string]`

- Contains references to publications, databases, and arbitrary links to the web.


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


__small_molecules__ [`list[SmallMolecule]`](#smallmolecule)

- Contains all reactants that are part of the experiment.


__reactions__ [`list[Reaction]`](#reaction)

- Dictionary mapping from reaction IDs to reaction-describing objects.


__measurements__ [`list[Measurement]`](#measurement)

- Contains measurements that describe outcomes of an experiment.


__equations__ [`list[Equation]`](#equation)

- Contains ordinary differential equations that describe the kinetic model.


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

__id__* `string`

- Unique identifier of the vessel.


__name__* `string`

- Name of the used vessel.


__volume__* `float`

- Volumetric value of the vessel.


__unit__* [`UnitDefinition`](#unitdefinition)

- Volumetric unit of the vessel.


__constant__* `boolean`

- Whether the volume of the vessel is constant or not.

- `Default`: true

------

### Protein
This object describes the proteins that were used or formed throughout the experiment.

__id__* `string`

- Unique internal identifier of the protein.
- `Schema`: identifier

__name__* `string`


__constant__* `boolean`


- `Default`: false

__sequence__ `string`

- Amino acid sequence of the protein


__vessel_id__ `string`

- Unique identifier of the vessel this protein has been used in.


__ecnumber__ `string`

- EC number of the protein.


__organism__ `string`

- Organism the protein was expressed in.


__organism_tax_id__ `string`

- Taxonomy identifier of the expression host.


__references__ `list[string]`

- Array of references to publications, database entries, etc. that describe the protein.


------

### Complex
This object describes complexes made of reactants and/or proteins that were used or produced in the course of the experiment.

__id__* `string`

- Unique identifier of the complex.


__name__* `string`


__constant__* `boolean`


- `Default`: false

__participants__ `list[string]`

- Array of IDs the complex contains


------

### SmallMolecule
This object describes the reactants that were used or produced in the course of the experiment.

__id__* `string`

- Unique identifier of the small molecule.


__name__* `string`


__constant__* `boolean`


- `Default`: false

__vessel_id__ `string`

- Unique identifier of the vessel this small molecule has been used in.


__canonical_smiles__ `string`

- Canonical Simplified Molecular-Input Line-Entry System (SMILES) encoding of the reactant.


__inchi__ `string`

- International Chemical Identifier (InChI) encoding of the reactant.


__inchikey__ `string`

- Hashed International Chemical Identifier (InChIKey) encoding of the reactant.


__references__ `list[string]`

- Array of references to publications, database entries, etc. that describe the reactant.


------

### Reaction
This object describes a chemical or enzymatic reaction that was investigated in the course of the experiment. All species used within this object need to be part of the data model.

__id__* `string`

- Unique identifier of the reaction.


__name__* `string`

- Name of the reaction.


__reversible__* `boolean`

- Whether the reaction is reversible or irreversible

- `Default`: false

__kinetic_law__ [`Equation`](#equation)

- Mathematical expression of the reaction.


__species__ [`list[ReactionElement]`](#reactionelement)

- List of reaction elements that are part of the reaction.


__modifiers__ `list[string]`

- List of reaction elements that are not part of the reaction but influence it.


------

### ReactionElement
This object is part of the Reaction object and describes either an educt, product or modifier. The latter includes buffers, counter-ions as well as proteins/enzymes.

__species_id__* `string`

- Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.
- `Schema`: identifier

__stoichiometry__* `float`

- Float number representing the associated stoichiometry.


------

### Equation
This object describes an equation that can be used to model the kinetics of a reaction. There are different types of equations that can be used to model the kinetics of a reaction. The equation can be an ordinary differential equation, a rate law or assignment rule.

__equation__* `string`

- Mathematical expression of the equation.


__unit__* [`UnitDefinition`](#unitdefinition)

- Unit of the rate law.


__equation_type__* [`EquationType`](#equationtype)

- Type of the equation.


__species_id__ `string`

- Internal identifier to a species defined in the EnzymeMLDocument, given it is a rate equation.


__variables__ [`list[Variable]`](#variable)

- List of variables that are part of the equation


__parameters__ [`list[Parameter]`](#parameter)

- List of parameters that are part of the equation


------

### Variable
This object describes a variable that is part of an equation.

__id__* `string`

- Unique identifier of the variable.


__name__* `string`

- Name of the variable.


__symbol__* `string`

- Symbol of the variable.


------

### Parameter
This object describes the parameters of the kinetic model and can include all estimated values.

__id__* `string`

- Unique identifier of the parameter.


__name__* `string`

- Name of the parameter.


__symbol__* `string`

- Symbol of the parameter.


__value__ `float`

- Numerical value of the estimated parameter.


__unit__ [`UnitDefinition`](#unitdefinition)

- Unit of the estimated parameter.


__initial_value__ `float`

- Initial value that was used for the parameter estimation.


__upper__ `float`

- Upper bound of the estimated parameter.


__lower__ `float`

- Lower bound of the estimated parameter.


__stderr__ `float`

- Standard error of the estimated parameter.


__constant__ `boolean`

- Specifies if this parameter is constant

- `Default`: true

------

### Measurement
This object describes the result of a measurement, which includes time course data of any type defined in DataTypes. It includes initial concentrations of all species used in a single measurement.

__id__* `string`

- Unique identifier of the measurement.


__name__* `string`

- Name of the measurement


__species_data__ [`list[MeasurementData]`](#measurementdata)

- Measurement data of all species that were part of the measurement. A species can refer to a protein, complex, or small molecule.


__group_id__ `string`

- User-defined group ID to signal relationships between measurements.


__ph__ `float`

- PH value of the measurement.
- `Minimum`: 0- `Maximum`: 14

__temperature__ `float`

- Temperature of the measurement.


__temperature_unit__ [`UnitDefinition`](#unitdefinition)

- Unit of the temperature of the measurement.


------

### MeasurementData
This object describes a single entity of a measurement, which corresponds to one species. It also holds replicates that contain time course data.

__species_id__* `string`

- The identifier for the described reactant.


__initial__* `float`

- Initial amount of the measurement data. This must be the same as the first data point in the


__data_unit__* [`UnitDefinition`](#unitdefinition)

- SI unit of the data that was measured.


__time_unit__* [`UnitDefinition`](#unitdefinition)

- Time unit of the replicate.


__data_type__* `string`

- Type of data that was measured (e.g. concentration)


__prepared__ `float`

- Amount of the reactant before the measurement. This field should be used for specifying the prepared amount of a species in the reaction mix. Not to be confused with


__data__* `list[float]`

- Data that was measured.


__time__* `list[float]`

- Time steps of the replicate.


__is_simulated__* `boolean`

- Whether or not the data has been generated by simulation.

- `Default`: false

------

### UnitDefinition
Represents a unit definition that is based on the SI unit system.

__id__ `string`

- Unique identifier of the unit definition.


__name__ `string`

- Common name of the unit definition.


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

### EquationType

| Alias | Value |
|-------|-------|
| `ASSIGNMENT` | assignment |
| `INITIAL_ASSIGNMENT` | initialAssignment |
| `ODE` | ode |
| `RATE_LAW` | rateLaw |

### DataTypes

| Alias | Value |
|-------|-------|
| `ABSORBANCE` | http://purl.allotrope.org/ontologies/quality#AFQ_0000061 |
| `CONCENTRATION` | http://purl.obolibrary.org/obo/PATO_0000033 |
| `CONVERSION` | http://purl.allotrope.org/ontologies/quality#AFQ_0000226 |
| `FLUORESCENCE` | http://purl.obolibrary.org/obo/PATO_0000018 |
| `PEAK_AREA` | http://purl.allotrope.org/ontologies/result#AFR_0001073 |
| `TRANSMITTANCE` | http://purl.allotrope.org/ontologies/result#AFR_0002261 |

### UnitType

| Alias | Value |
|-------|-------|
| `AMPERE` | ampere |
| `AVOGADRO` | avogadro |
| `BECQUEREL` | becquerel |
| `CANDELA` | candela |
| `CELSIUS` | celsius |
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