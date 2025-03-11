/**
 * This file contains Zod schema definitions for data validation.
 *
 * Zod is a TypeScript-first schema declaration and validation library.
 * It allows you to create schemas that validate data at runtime while
 * providing static type inference.
 *
 * Usage example:
 * ```typescript
 * import { TestSchema } from './schemas';
 *
 * // Validates data at runtime
 * const result = TestSchema.parse(data);
 *
 * // Type-safe - result has correct TypeScript types
 * console.log(result.name);
 *
 * // Will throw error if validation fails
 * try {
 *   TestSchema.parse(invalidData);
 * } catch (err) {
 *   console.error(err);
 * }
 * ```
 *
 * @see https://github.com/colinhacks/zod
 *
 * WARNING: This is an auto-generated file.
 * Do not edit directly - any changes will be overwritten.
 */


import { z } from 'zod';

// JSON-LD Types
export const JsonLdContextSchema = z.record(z.any());

export const JsonLdSchema = z.object({
  '@context': JsonLdContextSchema.optional(),
  '@id': z.string().optional(),
  '@type': z.string().optional(),
});

// EnzymeML V2 Type definitions
// The EnzymeMLDocument is the root object that serves as a container for
// all components of an enzymatic experiment. It includes essential
// metadata about the document itself, such as its title and creation/
// modification dates, as well as references to related publications
// and databases. Additionally, it contains comprehensive information
// about the experimental setup, including reaction vessels, proteins,
// complexes, small molecules, reactions, measurements, equations,
// and parameters.
export const EnzymeMLDocumentSchema = z.lazy(() => JsonLdSchema.extend({
  name: z.string().describe(`
    Title of the EnzymeML Document.
  `),
  created: z.string().nullable().describe(`
    Date the EnzymeML Document was created.
  `),
  modified: z.string().nullable().describe(`
    Date the EnzymeML Document was modified.
  `),
  creators: z.array(CreatorSchema).describe(`
    Contains descriptions of all authors that are part of the experiment.
  `),
  vessels: z.array(VesselSchema).describe(`
    Contains descriptions of all vessels that are part of the experiment.
  `),
  proteins: z.array(ProteinSchema).describe(`
    Contains descriptions of all proteins that are part of the experiment
    that may be referenced in reactions, measurements, and equations.
  `),
  complexes: z.array(ComplexSchema).describe(`
    Contains descriptions of all complexes that are part of the experiment
    that may be referenced in reactions, measurements, and equations.
  `),
  small_molecules: z.array(SmallMoleculeSchema).describe(`
    Contains descriptions of all reactants that are part of the experiment
    that may be referenced in reactions, measurements, and equations.
  `),
  reactions: z.array(ReactionSchema).describe(`
    Contains descriptions of all reactions that are part of the
    experiment.
  `),
  measurements: z.array(MeasurementSchema).describe(`
    Contains descriptions of all measurements that are part of the
    experiment.
  `),
  equations: z.array(EquationSchema).describe(`
    Contains descriptions of all equations that are part of the
    experiment.
  `),
  parameters: z.array(ParameterSchema).describe(`
    Contains descriptions of all parameters that are part of the
    experiment and may be used in equations.
  `),
  references: z.array(z.string()).describe(`
    Contains references to publications, databases, and arbitrary links to
    the web.
  `),
}));

export type EnzymeMLDocument = z.infer<typeof EnzymeMLDocumentSchema>;

// The Creator object represents an individual author or contributor who
// has participated in creating or modifying the EnzymeML Document.
// It captures essential personal information such as their name
// and contact details, allowing proper attribution and enabling
// communication with the document's creators.
export const CreatorSchema = z.lazy(() => JsonLdSchema.extend({
  given_name: z.string().describe(`
    Given name of the author or contributor.
  `),
  family_name: z.string().describe(`
    Family name of the author or contributor.
  `),
  mail: z.string().describe(`
    Email address of the author or contributor.
  `),
}));

export type Creator = z.infer<typeof CreatorSchema>;

// The Vessel object represents containers used to conduct experiments,
// such as reaction vessels, microplates, or bioreactors. It captures
// key properties like volume and whether the volume remains constant
// during the experiment.
export const VesselSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().describe(`
    Unique identifier of the vessel.
  `),
  name: z.string().describe(`
    Name of the used vessel.
  `),
  volume: z.number().describe(`
    Volumetric value of the vessel.
  `),
  unit: UnitDefinitionSchema.describe(`
    Volumetric unit of the vessel.
  `),
  constant: z.boolean().describe(`
    Whether the volume of the vessel is constant or not. Default is True.
  `),
}));

export type Vessel = z.infer<typeof VesselSchema>;

// The Protein object represents enzymes and other proteins involved in
// the experiment.
export const ProteinSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().describe(`
    Identifier of the protein, such as a UniProt ID, or a custom
    identifier.
  `),
  name: z.string().describe(`
    Name of the protein.
  `),
  constant: z.boolean().describe(`
    Whether the concentration of the protein is constant through the
    experiment or not. Default is True.
  `),
  sequence: z.string().nullable().describe(`
    Amino acid sequence of the protein
  `),
  vessel_id: z.string().nullable().describe(`
    Identifier of the vessel this protein has been applied to.
  `),
  ecnumber: z.string().nullable().describe(`
    EC number of the protein.
  `),
  organism: z.string().nullable().describe(`
    Expression host organism of the protein.
  `),
  organism_tax_id: z.string().nullable().describe(`
    Taxonomy identifier of the expression host.
  `),
  references: z.array(z.string()).describe(`
    List of references to publications, database entries, etc. that
    describe or reference the protein.
  `),
}));

export type Protein = z.infer<typeof ProteinSchema>;

// The Complex object allows the grouping of multiple species using
// their . This enables the representation of protein-small molecule
// complexes (e.g., enzyme-substrate complexes) as well as buffer or
// solvent mixtures (combinations of SmallMolecule species).
export const ComplexSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().describe(`
    Unique identifier of the complex.
  `),
  name: z.string().describe(`
    Name of the complex.
  `),
  constant: z.boolean().describe(`
    Whether the concentration of the complex is constant through the
    experiment or not. Default is False.
  `),
  vessel_id: z.string().nullable().describe(`
    Unique identifier of the vessel this complex has been used in.
  `),
  participants: z.array(z.string()).describe(`
    Array of IDs the complex contains
  `),
}));

export type Complex = z.infer<typeof ComplexSchema>;

// The SmallMolecule object represents small chemical compounds
// that participate in the experiment as substrates, products, or
// modifiers. It captures key molecular identifiers like SMILES and
// InChI.
export const SmallMoleculeSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().describe(`
    Identifier of the small molecule, such as a Pubchem ID, ChEBI ID, or a
    custom identifier.
  `),
  name: z.string().describe(`
    Name of the small molecule.
  `),
  constant: z.boolean().describe(`
    Whether the concentration of the small molecule is constant through
    the experiment or not. Default is False.
  `),
  vessel_id: z.string().nullable().describe(`
    Identifier of the vessel this small molecule has been used in.
  `),
  canonical_smiles: z.string().nullable().describe(`
    Canonical Simplified Molecular-Input Line-Entry System (SMILES)
    encoding of the small molecule.
  `),
  inchi: z.string().nullable().describe(`
    International Chemical Identifier (InChI) encoding of the small
    molecule.
  `),
  inchikey: z.string().nullable().describe(`
    Hashed International Chemical Identifier (InChIKey) encoding of the
    small molecule.
  `),
  references: z.array(z.string()).describe(`
    List of references to publications, database entries, etc. that
    describe or reference the small molecule.
  `),
}));

export type SmallMolecule = z.infer<typeof SmallMoleculeSchema>;

// The Reaction object represents a chemical or enzymatic reaction and
// holds the different species and modifiers that are part of the
// reaction.
export const ReactionSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().describe(`
    Unique identifier of the reaction.
  `),
  name: z.string().describe(`
    Name of the reaction.
  `),
  reversible: z.boolean().describe(`
    Whether the reaction is reversible or irreversible. Default is False.
  `),
  kinetic_law: EquationSchema.nullable().describe(`
    Mathematical expression of the reaction.
  `),
  species: z.array(ReactionElementSchema).describe(`
    List of reaction elements that are part of the reaction.
  `),
  modifiers: z.array(z.string()).describe(`
    List of reaction elements that are not part of the reaction but
    influence it.
  `),
}));

export type Reaction = z.infer<typeof ReactionSchema>;

// This object is part of the object and describes a species
// (SmallMolecule, Protein, Complex) participating in the reaction.
// The stochiometry is of the species is specified in the field,
// whereas negative values indicate that the species is a reactant
// and positive values indicate that the species is a product of the
// reaction.
export const ReactionElementSchema = z.lazy(() => JsonLdSchema.extend({
  species_id: z.string().describe(`
    Internal identifier to either a protein or reactant defined in the
    EnzymeML Document.
  `),
  stoichiometry: z.number().describe(`
    Float number representing the associated stoichiometry. Negative
    values indicate that the species is a reactant and positive values
    indicate that the species is a product of the reaction.
  `),
}));

export type ReactionElement = z.infer<typeof ReactionElementSchema>;

// The Equation object describes a mathematical equation used to model
// parts of a reaction system.
export const EquationSchema = z.lazy(() => JsonLdSchema.extend({
  species_id: z.string().describe(`
    Identifier of a defined species (SmallMolecule, Protein, Complex).
    Represents the left hand side of the equation.
  `),
  equation: z.string().describe(`
    Mathematical expression of the equation. Represents the right hand
    side of the equation.
  `),
  equation_type: EquationTypeSchema.describe(`
    Type of the equation.
  `),
  variables: z.array(VariableSchema).describe(`
    List of variables that are part of the equation
  `),
}));

export type Equation = z.infer<typeof EquationSchema>;

// This object describes a variable that is part of an equation.
// Variables can represent species concentrations, time, or other
// quantities that appear in mathematical expressions. Each variable
// must have a unique identifier, name, and symbol that is used in
// equations.
export const VariableSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().describe(`
    Identifier of the variable.
  `),
  name: z.string().describe(`
    Name of the variable.
  `),
  symbol: z.string().describe(`
    Equation symbol of the variable.
  `),
}));

export type Variable = z.infer<typeof VariableSchema>;

// This object describes parameters used in kinetic models, including
// estimated values, bounds, and associated uncertainties. Parameters
// can represent rate constants, binding constants, or other numerical
// values that appear in rate equations or other mathematical
// expressions.
export const ParameterSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().describe(`
    Identifier of the parameter.
  `),
  name: z.string().describe(`
    Name of the parameter.
  `),
  symbol: z.string().describe(`
    Equation symbol of the parameter.
  `),
  value: z.number().nullable().describe(`
    Numerical value of the estimated parameter.
  `),
  unit: UnitDefinitionSchema.nullable().describe(`
    Unit of the estimated parameter.
  `),
  initial_value: z.number().nullable().describe(`
    Initial value that was used for the parameter estimation.
  `),
  upper_bound: z.number().nullable().describe(`
    Upper bound for the parameter value that was used for the parameter
    estimation
  `),
  lower_bound: z.number().nullable().describe(`
    Lower bound for the parameter value that was used for the parameter
    estimation
  `),
  stderr: z.number().nullable().describe(`
    Standard error of the estimated parameter.
  `),
  constant: z.boolean().nullable().describe(`
    Specifies if this parameter is constant. Default is True.
  `),
}));

export type Parameter = z.infer<typeof ParameterSchema>;

// This object describes a single measurement, which includes time
// course data of any type defined in DataTypes. It contains initial
// concentrations and measurement data for all species involved in the
// experiment. Multiple measurements can be grouped together using the
// group_id field to indicate they are part of the same experimental
// series.
export const MeasurementSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().describe(`
    Unique identifier of the measurement.
  `),
  name: z.string().describe(`
    Name of the measurement
  `),
  species_data: z.array(MeasurementDataSchema).describe(`
    Measurement data of all species that were part of the measurement. A
    species refers to a Protein, Complex, or SmallMolecule.
  `),
  group_id: z.string().nullable().describe(`
    User-defined group ID to signal relationships between measurements.
  `),
  ph: z.number().nullable().describe(`
    pH value of the measurement.
  `),
  temperature: z.number().nullable().describe(`
    Temperature of the measurement.
  `),
  temperature_unit: UnitDefinitionSchema.nullable().describe(`
    Unit of the temperature of the measurement.
  `),
}));

export type Measurement = z.infer<typeof MeasurementSchema>;

// This object describes a single entity of a measurement, which
// corresponds to one species (Protein, Complex, SmallMolecule). It
// contains time course data for that species, including the initial
// amount, prepared amount, and measured data points over time.
// Endpoint data is treated as a time course data point with only one
// data point.
export const MeasurementDataSchema = z.lazy(() => JsonLdSchema.extend({
  species_id: z.string().describe(`
    The identifier for the described reactant.
  `),
  initial: z.number().describe(`
    Initial amount of the measurement data. This must be the same as the
    first data point in the array.
  `),
  data_unit: UnitDefinitionSchema.describe(`
    SI unit of the data that was measured.
  `),
  data_type: DataTypesSchema.describe(`
    Type of data that was measured (e.g. concentration, absorbance, etc.)
  `),
  prepared: z.number().nullable().describe(`
    Amount of the the species before starting the measurement. This
    field can be used for specifying the prepared amount of a species
    in the reaction mix. Not to be confused with , specifying the
    concentration of a species at the first data point from the array.
  `),
  data: z.array(z.number()).describe(`
    Data that was measured.
  `),
  time: z.array(z.number()).describe(`
    Corresponding time points of the .
  `),
  time_unit: UnitDefinitionSchema.nullable().describe(`
    Unit of the time points of the .
  `),
  is_simulated: z.boolean().describe(`
    Whether or not the data has been generated by simulation. Default
    is False.
  `),
}));

export type MeasurementData = z.infer<typeof MeasurementDataSchema>;

// Represents a unit definition that is based on the SI unit system.
export const UnitDefinitionSchema = z.lazy(() => JsonLdSchema.extend({
  id: z.string().nullable().describe(`
    Unique identifier of the unit definition.
  `),
  name: z.string().nullable().describe(`
    Common name of the unit definition.
  `),
  base_units: z.array(BaseUnitSchema).describe(`
    Base units that define the unit.
  `),
}));

export type UnitDefinition = z.infer<typeof UnitDefinitionSchema>;

// Represents a base unit in the unit definition.
export const BaseUnitSchema = z.lazy(() => JsonLdSchema.extend({
  kind: UnitTypeSchema.describe(`
    Kind of the base unit (e.g., meter, kilogram, second).
  `),
  exponent: z.number().describe(`
    Exponent of the base unit in the unit definition.
  `),
  multiplier: z.number().nullable().describe(`
    Multiplier of the base unit in the unit definition.
  `),
  scale: z.number().nullable().describe(`
    Scale of the base unit in the unit definition.
  `),
}));

export type BaseUnit = z.infer<typeof BaseUnitSchema>;

// EnzymeML V2 Enum definitions
export enum EquationType {
  ASSIGNMENT = 'assignment',
  INITIAL_ASSIGNMENT = 'initialAssignment',
  ODE = 'ode',
  RATE_LAW = 'rateLaw',
}

export const EquationTypeSchema = z.nativeEnum(EquationType);

export enum DataTypes {
  ABSORBANCE = 'absorbance',
  CONCENTRATION = 'concentration',
  CONVERSION = 'conversion',
  FLUORESCENCE = 'fluorescence',
  PEAK_AREA = 'peakarea',
  TRANSMITTANCE = 'transmittance',
}

export const DataTypesSchema = z.nativeEnum(DataTypes);

export enum UnitType {
  AMPERE = 'ampere',
  AVOGADRO = 'avogadro',
  BECQUEREL = 'becquerel',
  CANDELA = 'candela',
  CELSIUS = 'celsius',
  COULOMB = 'coulomb',
  DIMENSIONLESS = 'dimensionless',
  FARAD = 'farad',
  GRAM = 'gram',
  GRAY = 'gray',
  HENRY = 'henry',
  HERTZ = 'hertz',
  ITEM = 'item',
  JOULE = 'joule',
  KATAL = 'katal',
  KELVIN = 'kelvin',
  KILOGRAM = 'kilogram',
  LITRE = 'litre',
  LUMEN = 'lumen',
  LUX = 'lux',
  METRE = 'metre',
  MOLE = 'mole',
  NEWTON = 'newton',
  OHM = 'ohm',
  PASCAL = 'pascal',
  RADIAN = 'radian',
  SECOND = 'second',
  SIEMENS = 'siemens',
  SIEVERT = 'sievert',
  STERADIAN = 'steradian',
  TESLA = 'tesla',
  VOLT = 'volt',
  WATT = 'watt',
  WEBER = 'weber',
}

export const UnitTypeSchema = z.nativeEnum(UnitType);