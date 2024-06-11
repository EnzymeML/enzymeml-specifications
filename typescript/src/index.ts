import * as D from "io-ts/Decoder";
import { isLeft } from "fp-ts/Either";

// Generic validate function
export function validate<T>(codec: D.Decoder<unknown, T>, value: unknown): T {
  const result = codec.decode(value);
  if (isLeft(result)) {
    throw new Error(D.draw(result.left));
  }
  return result.right;
}

// JSON-LD Types
export interface JsonLdContext {
  [key: string]: any;
}

export interface JsonLd {
  "@context"?: JsonLdContext;
  "@id"?: string;
  "@type"?: string;
}

// EnzymeML Type definitions
/**
    This is the root object that composes all objects found in an EnzymeML
    document. It also includes general metadata such as the name
    of the document, when it was created/modified and references to
    publications, databases and arbitrary links to the web.

    * @param name - Title of the EnzymeML Document.
    * @param references - Contains references to publications, databases and arbitrary links to the web.
    * @param created - Date the EnzymeML document was created.
    * @param modified - Date the EnzymeML document was modified.
    * @param creators - Contains all authors that are part of the experiment.
    * @param vessels - Contains all vessels that are part of the experiment.
    * @param proteins - Contains all proteins that are part of the experiment.
    * @param complexes - Contains all complexes that are part of the experiment.
    * @param reactants - Contains all reactants that are part of the experiment.
    * @param reactions - Dictionary mapping from reaction IDs to reaction describing objects.
    * @param conditions - Conditions under which the reaction was carried out.
    * @param measurements - Contains measurements that describe outcomes of an experiment.
    * @param kinetic_model - Contains the kinetic model of the experiment.
**/
export interface EnzymeMLDocument extends JsonLd {
  name: string;
  references?: string[];
  created?: string;
  modified?: string;
  creators?: Creator[];
  vessels?: Vessel[];
  proteins?: Protein[];
  complexes?: Complex[];
  reactants?: Reactant[];
  reactions?: Reaction[];
  conditions?: ReactionConditions;
  measurements?: Measurement[];
  kinetic_model?: KineticModel;
}

export const EnzymeMLDocumentCodec = D.lazy("EnzymeMLDocument", () =>
  D.struct({
    name: D.string,
    references: D.array(D.string),
    created: D.nullable(D.string),
    modified: D.nullable(D.string),
    creators: D.array(CreatorCodec),
    vessels: D.array(VesselCodec),
    proteins: D.array(ProteinCodec),
    complexes: D.array(ComplexCodec),
    reactants: D.array(ReactantCodec),
    reactions: D.array(ReactionCodec),
    conditions: D.nullable(ReactionConditionsCodec),
    measurements: D.array(MeasurementCodec),
    kinetic_model: D.nullable(KineticModelCodec),
  }),
);

/**
    The creator object contains all information about authors that
    contributed to the resulting document.

    * @param given_name - Given name of the author or contributor.
    * @param family_name - Family name of the author or contributor.
    * @param mail - Email address of the author or contributor.
**/
export interface Creator extends JsonLd {
  given_name: string;
  family_name: string;
  mail: string;
}

export const CreatorCodec = D.lazy("Creator", () =>
  D.struct({
    given_name: D.string,
    family_name: D.string,
    mail: D.string,
  }),
);

/**
    This object describes vessels in which the experiment has been carried
    out. These can include any type of vessel used in biocatalytic
    experiments.

    * @param name - Name of the used vessel.
    * @param volume - Volumetric value of the vessel.
    * @param unit - Volumetric unit of the vessel.
    * @param constant - Whether the volume of the vessel is constant or not.
    * @param creator_id - Unique identifier of the author.
**/
export interface Vessel extends JsonLd {
  name: string;
  volume: number;
  unit: UnitDefinition;
  constant: boolean;
  creator_id?: string;
}

export const VesselCodec = D.lazy("Vessel", () =>
  D.struct({
    name: D.string,
    volume: D.number,
    unit: UnitDefinitionCodec,
    constant: D.boolean,
    creator_id: D.nullable(D.string),
  }),
);

/**
    This objects describes the proteins that were used or formed over the
    course of the experiment.

    * @param name
    * @param constant
    * @param sequence - Amino acid sequence of the protein
    * @param vessel_id
    * @param ecnumber - EC number of the protein.
    * @param organism - Organism the protein was expressed in.
    * @param organism_tax_id - Taxonomy identifier of the expression host.
    * @param references - Array of references to publications, database entries etc. that describe the protein.
**/
export interface Protein extends JsonLd {
  name: string;
  constant: boolean;
  sequence: string;
  vessel_id?: string;
  ecnumber?: string;
  organism?: string;
  organism_tax_id?: string;
  references?: string[];
}

export const ProteinCodec = D.lazy("Protein", () =>
  D.struct({
    name: D.string,
    constant: D.boolean,
    sequence: D.string,
    vessel_id: D.nullable(D.string),
    ecnumber: D.nullable(D.string),
    organism: D.nullable(D.string),
    organism_tax_id: D.nullable(D.string),
    references: D.array(D.string),
  }),
);

/**
    This object describes complexes made of reactants and/or proteins that
    were used or produced in the course of the experiment.

    * @param participants - Array of IDs the complex contains
**/
export interface Complex extends JsonLd {
  participants?: string[];
}

export const ComplexCodec = D.lazy("Complex", () =>
  D.struct({
    participants: D.array(D.string),
  }),
);

/**
    This objects describes the reactants that were used or produced in the
    course of the experiment.

    * @param name
    * @param constant
    * @param vessel_id
    * @param canonical_smiles - Canonical Simplified Molecular-Input Line-Entry System (SMILES) encoding of the reactant.
    * @param inchikey - Hashed International Chemical Identifier (InChIKey) encoding of the reactant.
    * @param references - Array of references to publications, database entries etc. that describe the reactant.
**/
export interface Reactant extends JsonLd {
  name: string;
  constant: boolean;
  vessel_id?: string;
  canonical_smiles?: string;
  inchikey?: string;
  references?: string[];
}

export const ReactantCodec = D.lazy("Reactant", () =>
  D.struct({
    name: D.string,
    constant: D.boolean,
    vessel_id: D.nullable(D.string),
    canonical_smiles: D.nullable(D.string),
    inchikey: D.nullable(D.string),
    references: D.array(D.string),
  }),
);

/**
    This object describes a chemical or enzymatic reaction that was
    investigated in the course of the experiment. All species used
    within this object need to be part of the data model.

    * @param name - Name of the reaction.
    * @param reversible - Whether the reaction is reversible or irreversible
    * @param species - List of reaction elements that are part of the reaction.
    * @param modifiers - List of reaction elements that are not part of the reaction but influence it.
**/
export interface Reaction extends JsonLd {
  name: string;
  reversible: boolean;
  species?: ReactionSpecies[];
  modifiers?: string[];
}

export const ReactionCodec = D.lazy("Reaction", () =>
  D.struct({
    name: D.string,
    reversible: D.boolean,
    species: D.array(ReactionSpeciesCodec),
    modifiers: D.array(D.string),
  }),
);

/**
    This object is part of the Reaction object and describes either an
    educt, product or modifier. The latter includes buffers, counter-
    ions as well as proteins/enzymes.

    * @param species_id - Internal identifier to either a protein or reactant defined in the EnzymeMLDocument.
    * @param stoichiometry - Float number representing the associated stoichiometry.
**/
export interface ReactionSpecies extends JsonLd {
  species_id: string;
  stoichiometry?: number;
}

export const ReactionSpeciesCodec = D.lazy("ReactionSpecies", () =>
  D.struct({
    species_id: D.string,
    stoichiometry: D.nullable(D.number),
  }),
);

/**
 * @param temperature - Numeric value of the temperature of the reaction.
 * @param temperature_unit - Unit of the temperature of the reaction.
 * @param ph - PH value of the reaction.
 **/
export interface ReactionConditions extends JsonLd {
  temperature?: number;
  temperature_unit?: UnitDefinition;
  ph?: number;
}

export const ReactionConditionsCodec = D.lazy("ReactionConditions", () =>
  D.struct({
    temperature: D.nullable(D.number),
    temperature_unit: D.nullable(UnitDefinitionCodec),
    ph: D.nullable(D.number),
  }),
);

/**
    This object describes a kinetic model that was derived from the
    experiment.

    * @param name - Name of the kinetic law.
    * @param equations - Equation for the kinetic law.
    * @param parameters - List of estimated parameters.
**/
export interface KineticModel extends JsonLd {
  name: string;
  equations: RateLaw[];
  parameters?: KineticParameter[];
}

export const KineticModelCodec = D.lazy("KineticModel", () =>
  D.struct({
    name: D.string,
    equations: D.array(RateLawCodec),
    parameters: D.array(KineticParameterCodec),
  }),
);

/**
    This object describes an ordinary differential equation that is part
    of the kinetic model.

    * @param species_id - Internal identifier to a species defined in the EnzymeMLDocument.
    * @param equation - Equation of the rate law.
**/
export interface RateLaw extends JsonLd {
  species_id: string;
  equation: Equation;
}

export const RateLawCodec = D.lazy("RateLaw", () =>
  D.struct({
    species_id: D.string,
    equation: EquationCodec,
  }),
);

/**
    This object describes the parameters of the kinetic model and can
    include all estimated values.

    * @param name - Name of the estimated parameter.
    * @param value - Numerical value of the estimated parameter.
    * @param unit - Unit of the estimated parameter.
    * @param initial_value - Initial value that was used for the parameter estimation.
    * @param upper - Upper bound of the estimated parameter.
    * @param lower - Lower bound of the estimated parameter.
    * @param stderr - Standard error of the estimated parameter.
    * @param constant - Specifies if this parameter is constant
**/
export interface KineticParameter extends JsonLd {
  name: string;
  value: number;
  unit: UnitDefinition;
  initial_value?: number;
  upper?: number;
  lower?: number;
  stderr?: number;
  constant: boolean;
}

export const KineticParameterCodec = D.lazy("KineticParameter", () =>
  D.struct({
    name: D.string,
    value: D.number,
    unit: UnitDefinitionCodec,
    initial_value: D.nullable(D.number),
    upper: D.nullable(D.number),
    lower: D.nullable(D.number),
    stderr: D.nullable(D.number),
    constant: D.boolean,
  }),
);

/**
    This object describes the result of a measurement, which includes time
    course data of any type defined in DataTypes. It includes initial
    concentrations of all species used in a single measurement.

    * @param name - Name of the measurement
    * @param species - Species of the measurement.
    * @param group_id - User-defined group ID to signalize relationships between measurements.
**/
export interface Measurement extends JsonLd {
  name: string;
  species?: MeasurementData[];
  group_id?: string;
}

export const MeasurementCodec = D.lazy("Measurement", () =>
  D.struct({
    name: D.string,
    species: D.array(MeasurementDataCodec),
    group_id: D.nullable(D.string),
  }),
);

/**
    This object describes a single entity of a measurement, which
    corresponds to one species. It also holds replicates which contain
    time course data.

    * @param species_id - The identifier for the described reactant.
    * @param init_conc - Initial concentration of the measurement data.
    * @param data_type - Type of data that was measured (e.g. concentration)
    * @param data_unit - SI unit of the data that was measured.
    * @param time_unit - Time unit of the replicate.
    * @param time - Time steps of the replicate.
    * @param data - Data that was measured.
    * @param is_calculated - Whether or not the data has been generated by simulation.
**/
export interface MeasurementData extends JsonLd {
  species_id: string;
  init_conc: number;
  data_type: DataTypes;
  data_unit: UnitDefinition;
  time_unit: UnitDefinition;
  time: number[];
  data: number[];
  is_calculated: boolean;
}

export const MeasurementDataCodec = D.lazy("MeasurementData", () =>
  D.struct({
    species_id: D.string,
    init_conc: D.number,
    data_type: DataTypesCodec,
    data_unit: UnitDefinitionCodec,
    time_unit: UnitDefinitionCodec,
    time: D.array(D.number),
    data: D.array(D.number),
    is_calculated: D.boolean,
  }),
);

/**
    Represents an equation that can be used in a data model.

    * @param id - Unique identifier for the equation.
    * @param equation - The equation that is used in the data model.
    * @param variables - List of variables that are used in the equation.
    * @param parameters - List of parameters that are used in the equation.
**/
export interface Equation extends JsonLd {
  id?: string;
  equation?: string;
  variables?: EqVariable[];
  parameters?: EqParameter[];
}

export const EquationCodec = D.lazy("Equation", () =>
  D.struct({
    id: D.nullable(D.string),
    equation: D.nullable(D.string),
    variables: D.array(EqVariableCodec),
    parameters: D.array(EqParameterCodec),
  }),
);

/**
    Represents a variable that is used in the equation.

    * @param id - Unique identifier for the variable.
    * @param name - Name of the variable.
    * @param symbol - Symbol of the variable.
**/
export interface EqVariable extends JsonLd {
  id?: string;
  name?: string;
  symbol?: string;
}

export const EqVariableCodec = D.lazy("EqVariable", () =>
  D.struct({
    id: D.nullable(D.string),
    name: D.nullable(D.string),
    symbol: D.nullable(D.string),
  }),
);

/**
    Represents a parameter that is used in the equation.

    * @param id - Unique identifier for the parameter.
    * @param name - Name of the parameter.
    * @param symbol - Symbol of the parameter.
    * @param value - Value of the parameter.
**/
export interface EqParameter extends JsonLd {
  id?: string;
  name?: string;
  symbol?: string;
  value?: number;
}

export const EqParameterCodec = D.lazy("EqParameter", () =>
  D.struct({
    id: D.nullable(D.string),
    name: D.nullable(D.string),
    symbol: D.nullable(D.string),
    value: D.nullable(D.number),
  }),
);

/**
    Represents a unit definition that is based on the SI unit system.

    * @param id - Unique identifier for the unit definition.
    * @param base_units - Base units that define the unit.
**/
export interface UnitDefinition extends JsonLd {
  id?: string;
  base_units?: BaseUnit[];
}

export const UnitDefinitionCodec = D.lazy("UnitDefinition", () =>
  D.struct({
    id: D.nullable(D.string),
    base_units: D.array(BaseUnitCodec),
  }),
);

/**
    Represents a base unit in the unit definition.

    * @param kind - Kind of the base unit (e.g., meter, kilogram, second).
    * @param exponent - Exponent of the base unit in the unit definition.
    * @param multiplier - Multiplier of the base unit in the unit definition.
    * @param scale - Scale of the base unit in the unit definition.
**/
export interface BaseUnit extends JsonLd {
  kind: UnitType;
  exponent: number;
  multiplier?: number;
  scale?: number;
}

export const BaseUnitCodec = D.lazy("BaseUnit", () =>
  D.struct({
    kind: UnitTypeCodec,
    exponent: D.number,
    multiplier: D.nullable(D.number),
    scale: D.nullable(D.number),
  }),
);

// EnzymeML Enum definitions
export enum DataTypes {
  ABSORPTION = "abs",
  BIOMASS = "biomass",
  CONCENTRATION = "conc",
  CONVERSION = "conversion",
  FEED = "feed",
  PEAK_AREA = "peak-area",
}

export const DataTypesCodec = D.union(
  D.literal(DataTypes.ABSORPTION),
  D.literal(DataTypes.BIOMASS),
  D.literal(DataTypes.CONCENTRATION),
  D.literal(DataTypes.CONVERSION),
  D.literal(DataTypes.FEED),
  D.literal(DataTypes.PEAK_AREA),
);

export enum UnitType {
  AMPERE = "ampere",
  AVOGADRO = "avogadro",
  BECQUEREL = "becquerel",
  CANDELA = "candela",
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

export const UnitTypeCodec = D.union(
  D.literal(UnitType.AMPERE),
  D.literal(UnitType.AVOGADRO),
  D.literal(UnitType.BECQUEREL),
  D.literal(UnitType.CANDELA),
  D.literal(UnitType.COULOMB),
  D.literal(UnitType.DIMENSIONLESS),
  D.literal(UnitType.FARAD),
  D.literal(UnitType.GRAM),
  D.literal(UnitType.GRAY),
  D.literal(UnitType.HENRY),
  D.literal(UnitType.HERTZ),
  D.literal(UnitType.ITEM),
  D.literal(UnitType.JOULE),
  D.literal(UnitType.KATAL),
  D.literal(UnitType.KELVIN),
  D.literal(UnitType.KILOGRAM),
  D.literal(UnitType.LITRE),
  D.literal(UnitType.LUMEN),
  D.literal(UnitType.LUX),
  D.literal(UnitType.METRE),
  D.literal(UnitType.MOLE),
  D.literal(UnitType.NEWTON),
  D.literal(UnitType.OHM),
  D.literal(UnitType.PASCAL),
  D.literal(UnitType.RADIAN),
  D.literal(UnitType.SECOND),
  D.literal(UnitType.SIEMENS),
  D.literal(UnitType.SIEVERT),
  D.literal(UnitType.STERADIAN),
  D.literal(UnitType.TESLA),
  D.literal(UnitType.VOLT),
  D.literal(UnitType.WATT),
  D.literal(UnitType.WEBER),
);
