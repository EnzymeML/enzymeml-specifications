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

import { z } from "zod";

// JSON-LD Types
export const JsonLdContextSchema = z.record(z.any());

export const JsonLdSchema = z.object({
  "@context": JsonLdContextSchema.optional(),
  "@id": z.string().optional(),
  "@type": z.string().optional(),
});

// EnzymeML Type definitions
export const EnzymeMLDocumentSchema = z.lazy(() =>
  JsonLdSchema.extend({
    name: z.string().describe(`
    Title of the EnzymeML Document.
  `),
    references: z.array(z.string()).describe(`
    Contains references to publications, databases, and arbitrary links to
    the web.
  `),
    created: z.string().nullable().describe(`
    Date the EnzymeML document was created.
  `),
    modified: z.string().nullable().describe(`
    Date the EnzymeML document was modified.
  `),
    creators: z.array(CreatorSchema).describe(`
    Contains all authors that are part of the experiment.
  `),
    vessels: z.array(VesselSchema).describe(`
    Contains all vessels that are part of the experiment.
  `),
    proteins: z.array(ProteinSchema).describe(`
    Contains all proteins that are part of the experiment.
  `),
    complexes: z.array(ComplexSchema).describe(`
    Contains all complexes that are part of the experiment.
  `),
    small_molecules: z.array(SmallMoleculeSchema).describe(`
    Contains all reactants that are part of the experiment.
  `),
    reactions: z.array(ReactionSchema).describe(`
    Dictionary mapping from reaction IDs to reaction-describing objects.
  `),
    measurements: z.array(MeasurementSchema).describe(`
    Contains measurements that describe outcomes of an experiment.
  `),
    equations: z.array(EquationSchema).describe(`
    Contains ordinary differential equations that describe the kinetic
    model.
  `),
    parameters: z.array(ParameterSchema).describe(`
    List of parameters that are part of the equation
  `),
  }),
);

export type EnzymeMLDocument = z.infer<typeof EnzymeMLDocumentSchema>;

export const CreatorSchema = z.lazy(() =>
  JsonLdSchema.extend({
    given_name: z.string().describe(`
    Given name of the author or contributor.
  `),
    family_name: z.string().describe(`
    Family name of the author or contributor.
  `),
    mail: z.string().describe(`
    Email address of the author or contributor.
  `),
  }),
);

export type Creator = z.infer<typeof CreatorSchema>;

export const VesselSchema = z.lazy(() =>
  JsonLdSchema.extend({
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
    Whether the volume of the vessel is constant or not.
  `),
  }),
);

export type Vessel = z.infer<typeof VesselSchema>;

export const ProteinSchema = z.lazy(() =>
  JsonLdSchema.extend({
    id: z.string().describe(`
    Unique internal identifier of the protein.
  `),
    name: z.string(),
    constant: z.boolean(),
    sequence: z.string().nullable().describe(`
    Amino acid sequence of the protein
  `),
    vessel_id: z.string().nullable().describe(`
    Unique identifier of the vessel this protein has been used in.
  `),
    ecnumber: z.string().nullable().describe(`
    EC number of the protein.
  `),
    organism: z.string().nullable().describe(`
    Organism the protein was expressed in.
  `),
    organism_tax_id: z.string().nullable().describe(`
    Taxonomy identifier of the expression host.
  `),
    references: z.array(z.string()).describe(`
    Array of references to publications, database entries, etc. that
    describe the protein.
  `),
  }),
);

export type Protein = z.infer<typeof ProteinSchema>;

export const ComplexSchema = z.lazy(() =>
  JsonLdSchema.extend({
    id: z.string().describe(`
    Unique identifier of the complex.
  `),
    name: z.string(),
    constant: z.boolean(),
    vessel_id: z.string().nullable().describe(`
    Unique identifier of the vessel this complex has been used in.
  `),
    participants: z.array(z.string()).describe(`
    Array of IDs the complex contains
  `),
  }),
);

export type Complex = z.infer<typeof ComplexSchema>;

export const SmallMoleculeSchema = z.lazy(() =>
  JsonLdSchema.extend({
    id: z.string().describe(`
    Unique identifier of the small molecule.
  `),
    name: z.string(),
    constant: z.boolean(),
    vessel_id: z.string().nullable().describe(`
    Unique identifier of the vessel this small molecule has been used in.
  `),
    canonical_smiles: z.string().nullable().describe(`
    Canonical Simplified Molecular-Input Line-Entry System (SMILES)
    encoding of the reactant.
  `),
    inchi: z.string().nullable().describe(`
    International Chemical Identifier (InChI) encoding of the reactant.
  `),
    inchikey: z.string().nullable().describe(`
    Hashed International Chemical Identifier (InChIKey) encoding of the
    reactant.
  `),
    references: z.array(z.string()).describe(`
    Array of references to publications, database entries, etc. that
    describe the reactant.
  `),
  }),
);

export type SmallMolecule = z.infer<typeof SmallMoleculeSchema>;

export const ReactionSchema = z.lazy(() =>
  JsonLdSchema.extend({
    id: z.string().describe(`
    Unique identifier of the reaction.
  `),
    name: z.string().describe(`
    Name of the reaction.
  `),
    reversible: z.boolean().describe(`
    Whether the reaction is reversible or irreversible
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
  }),
);

export type Reaction = z.infer<typeof ReactionSchema>;

export const ReactionElementSchema = z.lazy(() =>
  JsonLdSchema.extend({
    species_id: z.string().describe(`
    Internal identifier to either a protein or reactant defined in the
    EnzymeMLDocument.
  `),
    stoichiometry: z.number().describe(`
    Float number representing the associated stoichiometry.
  `),
  }),
);

export type ReactionElement = z.infer<typeof ReactionElementSchema>;

export const EquationSchema = z.lazy(() =>
  JsonLdSchema.extend({
    equation: z.string().describe(`
    Mathematical expression of the equation.
  `),
    equation_type: EquationTypeSchema.describe(`
    Type of the equation.
  `),
    species_id: z.string().nullable().describe(`
    Internal identifier to a species defined in the EnzymeMLDocument,
    given it is a rate equation.
  `),
    variables: z.array(VariableSchema).describe(`
    List of variables that are part of the equation
  `),
  }),
);

export type Equation = z.infer<typeof EquationSchema>;

export const VariableSchema = z.lazy(() =>
  JsonLdSchema.extend({
    id: z.string().describe(`
    Unique identifier of the variable.
  `),
    name: z.string().describe(`
    Name of the variable.
  `),
    symbol: z.string().describe(`
    Symbol of the variable.
  `),
  }),
);

export type Variable = z.infer<typeof VariableSchema>;

export const ParameterSchema = z.lazy(() =>
  JsonLdSchema.extend({
    id: z.string().describe(`
    Unique identifier of the parameter.
  `),
    name: z.string().describe(`
    Name of the parameter.
  `),
    symbol: z.string().describe(`
    Symbol of the parameter.
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
    upper: z.number().nullable().describe(`
    Upper bound of the estimated parameter.
  `),
    lower: z.number().nullable().describe(`
    Lower bound of the estimated parameter.
  `),
    stderr: z.number().nullable().describe(`
    Standard error of the estimated parameter.
  `),
    constant: z.boolean().nullable().describe(`
    Specifies if this parameter is constant
  `),
  }),
);

export type Parameter = z.infer<typeof ParameterSchema>;

export const MeasurementSchema = z.lazy(() =>
  JsonLdSchema.extend({
    id: z.string().describe(`
    Unique identifier of the measurement.
  `),
    name: z.string().describe(`
    Name of the measurement
  `),
    species_data: z.array(MeasurementDataSchema).describe(`
    Measurement data of all species that were part of the measurement. A
    species can refer to a protein, complex, or small molecule.
  `),
    group_id: z.string().nullable().describe(`
    User-defined group ID to signal relationships between measurements.
  `),
    ph: z.number().nullable().describe(`
    PH value of the measurement.
  `),
    temperature: z.number().nullable().describe(`
    Temperature of the measurement.
  `),
    temperature_unit: UnitDefinitionSchema.nullable().describe(`
    Unit of the temperature of the measurement.
  `),
  }),
);

export type Measurement = z.infer<typeof MeasurementSchema>;

export const MeasurementDataSchema = z.lazy(() =>
  JsonLdSchema.extend({
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
    Type of data that was measured (e.g. concentration)
  `),
    prepared: z.number().nullable().describe(`
    Amount of the reactant before the measurement. This field should
    be used for specifying the prepared amount of a species in
    the reaction mix. Not to be confused with , specifying the
    concentration at the first data point from the array.
  `),
    data: z.array(z.number()).describe(`
    Data that was measured.
  `),
    time: z.array(z.number()).describe(`
    Time steps of the replicate.
  `),
    time_unit: UnitDefinitionSchema.nullable().describe(`
    Time unit of the replicate.
  `),
    is_simulated: z.boolean().describe(`
    Whether or not the data has been generated by simulation.
  `),
  }),
);

export type MeasurementData = z.infer<typeof MeasurementDataSchema>;

export const UnitDefinitionSchema = z.lazy(() =>
  JsonLdSchema.extend({
    id: z.string().nullable().describe(`
    Unique identifier of the unit definition.
  `),
    name: z.string().nullable().describe(`
    Common name of the unit definition.
  `),
    base_units: z.array(BaseUnitSchema).describe(`
    Base units that define the unit.
  `),
  }),
);

export type UnitDefinition = z.infer<typeof UnitDefinitionSchema>;

export const BaseUnitSchema = z.lazy(() =>
  JsonLdSchema.extend({
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
  }),
);

export type BaseUnit = z.infer<typeof BaseUnitSchema>;

// EnzymeML Enum definitions
export enum EquationType {
  ASSIGNMENT = "assignment",
  INITIAL_ASSIGNMENT = "initialAssignment",
  ODE = "ode",
  RATE_LAW = "rateLaw",
}

export const EquationTypeSchema = z.nativeEnum(EquationType);

export enum DataTypes {
  ABSORBANCE = "http://purl.allotrope.org/ontologies/quality#AFQ_0000061",
  CONCENTRATION = "http://purl.obolibrary.org/obo/PATO_0000033",
  CONVERSION = "http://purl.allotrope.org/ontologies/quality#AFQ_0000226",
  FLUORESCENCE = "http://purl.obolibrary.org/obo/PATO_0000018",
  PEAK_AREA = "http://purl.allotrope.org/ontologies/result#AFR_0001073",
  TRANSMITTANCE = "http://purl.allotrope.org/ontologies/result#AFR_0002261",
}

export const DataTypesSchema = z.nativeEnum(DataTypes);

export enum UnitType {
  AMPERE = "ampere",
  AVOGADRO = "avogadro",
  BECQUEREL = "becquerel",
  CANDELA = "candela",
  CELSIUS = "celsius",
  COULOMB = "coulomb",
  DIMENSIONLESS = "dimensionless",
  FARAD = "farad",
  GRAM = "gram",
  GRAY = "gray",
  HENRY = "henry",
  HERTZ = "hertz",
  ITEM = "item",
  JOULE = "joule",
  KATAL = "katal",
  KELVIN = "kelvin",
  KILOGRAM = "kilogram",
  LITRE = "litre",
  LUMEN = "lumen",
  LUX = "lux",
  METRE = "metre",
  MOLE = "mole",
  NEWTON = "newton",
  OHM = "ohm",
  PASCAL = "pascal",
  RADIAN = "radian",
  SECOND = "second",
  SIEMENS = "siemens",
  SIEVERT = "sievert",
  STERADIAN = "steradian",
  TESLA = "tesla",
  VOLT = "volt",
  WATT = "watt",
  WEBER = "weber",
}

export const UnitTypeSchema = z.nativeEnum(UnitType);
