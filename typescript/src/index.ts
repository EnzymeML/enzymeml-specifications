import * as D from 'io-ts/Decoder';
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
  '@context'?: JsonLdContext;
  '@id'?: string;
  '@type'?: string;
}

// EnzymeML Type definitions
/**
    This is the root object that composes all objects found in an EnzymeML
    document. It also includes general metadata such as the name of
    the document, when it was created/modified, and references to
    publications, databases, and arbitrary links to the web.

    * @param name - Title of the EnzymeML Document.
    * @param references - Contains references to publications, databases, and arbitrary links to
             the web.
    * @param created - Date the EnzymeML document was created.
    * @param modified - Date the EnzymeML document was modified.
    * @param creators - Contains all authors that are part of the experiment.
    * @param vessels - Contains all vessels that are part of the experiment.
    * @param proteins - Contains all proteins that are part of the experiment.
    * @param complexes - Contains all complexes that are part of the experiment.
    * @param small_molecules - Contains all reactants that are part of the experiment.
    * @param reactions - Dictionary mapping from reaction IDs to reaction-describing objects.
    * @param measurements - Contains measurements that describe outcomes of an experiment.
    * @param equations - Contains ordinary differential equations that describe the kinetic
             model.
**/
export interface EnzymeMLDocument extends JsonLd {
  name: string;
  references?: string[] | null;
  created?: string | null;
  modified?: string | null;
  creators?: Creator[] | null;
  vessels?: Vessel[] | null;
  proteins?: Protein[] | null;
  complexes?: Complex[] | null;
  small_molecules?: SmallMolecule[] | null;
  reactions?: Reaction[] | null;
  measurements?: Measurement[] | null;
  equations?: Equation[] | null;
}

export const EnzymeMLDocumentCodec = D.lazy("EnzymeMLDocument", () => D.struct({
    name: D.string,
    references: D.array(D.string),
    created: D.nullable(D.string),
    modified: D.nullable(D.string),
    creators: D.array(CreatorCodec),
    vessels: D.array(VesselCodec),
    proteins: D.array(ProteinCodec),
    complexes: D.array(ComplexCodec),
    small_molecules: D.array(SmallMoleculeCodec),
    reactions: D.array(ReactionCodec),
    measurements: D.array(MeasurementCodec),
    equations: D.array(EquationCodec),
}));


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

export const CreatorCodec = D.lazy("Creator", () => D.struct({
    given_name: D.string,
    family_name: D.string,
    mail: D.string,
}));


/**
    This object describes vessels in which the experiment has been carried
    out. These can include any type of vessel used in biocatalytic
    experiments.

    * @param id - Unique identifier of the vessel.
    * @param name - Name of the used vessel.
    * @param volume - Volumetric value of the vessel.
    * @param unit - Volumetric unit of the vessel.
    * @param constant - Whether the volume of the vessel is constant or not.
**/
export interface Vessel extends JsonLd {
  id: string;
  name: string;
  volume: number;
  unit: UnitDefinition;
  constant: boolean;
}

export const VesselCodec = D.lazy("Vessel", () => D.struct({
    id: D.string,
    name: D.string,
    volume: D.number,
    unit: UnitDefinitionCodec,
    constant: D.boolean,
}));


/**
    This object describes the proteins that were used or formed throughout
    the experiment.

    * @param id - Unique internal identifier of the protein.
    * @param name
    * @param constant
    * @param sequence - Amino acid sequence of the protein
    * @param vessel_id - Unique identifier of the vessel this protein has been used in.
    * @param ecnumber - EC number of the protein.
    * @param organism - Organism the protein was expressed in.
    * @param organism_tax_id - Taxonomy identifier of the expression host.
    * @param references - Array of references to publications, database entries, etc. that
             describe the protein.
**/
export interface Protein extends JsonLd {
  id: string;
  name: string;
  constant: boolean;
  sequence?: string | null;
  vessel_id?: string | null;
  ecnumber?: string | null;
  organism?: string | null;
  organism_tax_id?: string | null;
  references?: string[] | null;
}

export const ProteinCodec = D.lazy("Protein", () => D.struct({
    id: D.string,
    name: D.string,
    constant: D.boolean,
    sequence: D.nullable(D.string),
    vessel_id: D.nullable(D.string),
    ecnumber: D.nullable(D.string),
    organism: D.nullable(D.string),
    organism_tax_id: D.nullable(D.string),
    references: D.array(D.string),
}));


/**
    This object describes complexes made of reactants and/or proteins that
    were used or produced in the course of the experiment.

    * @param id - Unique identifier of the complex.
    * @param name
    * @param constant
    * @param participants - Array of IDs the complex contains
**/
export interface Complex extends JsonLd {
  id: string;
  name: string;
  constant: boolean;
  participants?: string[] | null;
}

export const ComplexCodec = D.lazy("Complex", () => D.struct({
    id: D.string,
    name: D.string,
    constant: D.boolean,
    participants: D.array(D.string),
}));


/**
    This object describes the reactants that were used or produced in the
    course of the experiment.

    * @param id - Unique identifier of the small molecule.
    * @param name
    * @param constant
    * @param vessel_id - Unique identifier of the vessel this small molecule has been used in.
    * @param canonical_smiles - Canonical Simplified Molecular-Input Line-Entry System (SMILES)
             encoding of the reactant.
    * @param inchi - International Chemical Identifier (InChI) encoding of the reactant.
    * @param inchikey - Hashed International Chemical Identifier (InChIKey) encoding of the
             reactant.
    * @param references - Array of references to publications, database entries, etc. that
             describe the reactant.
**/
export interface SmallMolecule extends JsonLd {
  id: string;
  name: string;
  constant: boolean;
  vessel_id?: string | null;
  canonical_smiles?: string | null;
  inchi?: string | null;
  inchikey?: string | null;
  references?: string[] | null;
}

export const SmallMoleculeCodec = D.lazy("SmallMolecule", () => D.struct({
    id: D.string,
    name: D.string,
    constant: D.boolean,
    vessel_id: D.nullable(D.string),
    canonical_smiles: D.nullable(D.string),
    inchi: D.nullable(D.string),
    inchikey: D.nullable(D.string),
    references: D.array(D.string),
}));


/**
    This object describes a chemical or enzymatic reaction that was
    investigated in the course of the experiment. All species used
    within this object need to be part of the data model.

    * @param id - Unique identifier of the reaction.
    * @param name - Name of the reaction.
    * @param reversible - Whether the reaction is reversible or irreversible
    * @param kinetic_law - Mathematical expression of the reaction.
    * @param species - List of reaction elements that are part of the reaction.
    * @param modifiers - List of reaction elements that are not part of the reaction but
             influence it.
**/
export interface Reaction extends JsonLd {
  id: string;
  name: string;
  reversible: boolean;
  kinetic_law?: Equation | null;
  species?: ReactionElement[] | null;
  modifiers?: string[] | null;
}

export const ReactionCodec = D.lazy("Reaction", () => D.struct({
    id: D.string,
    name: D.string,
    reversible: D.boolean,
    kinetic_law: D.nullable(EquationCodec),
    species: D.array(ReactionElementCodec),
    modifiers: D.array(D.string),
}));


/**
    This object is part of the Reaction object and describes either an
    educt, product or modifier. The latter includes buffers, counter-
    ions as well as proteins/enzymes.

    * @param species_id - Internal identifier to either a protein or reactant defined in the
             EnzymeMLDocument.
    * @param stoichiometry - Float number representing the associated stoichiometry.
**/
export interface ReactionElement extends JsonLd {
  species_id: string;
  stoichiometry: number;
}

export const ReactionElementCodec = D.lazy("ReactionElement", () => D.struct({
    species_id: D.string,
    stoichiometry: D.number,
}));


/**
    This object describes an equation that can be used to model the
    kinetics of a reaction. There are different types of equations
    that can be used to model the kinetics of a reaction. The equation
    can be an ordinary differential equation, a rate law or assignment
    rule.

    * @param equation - Mathematical expression of the equation.
    * @param unit - Unit of the rate law.
    * @param equation_type - Type of the equation.
    * @param species_id - Internal identifier to a species defined in the EnzymeMLDocument,
             given it is a rate equation.
    * @param variables - List of variables that are part of the equation
    * @param parameters - List of parameters that are part of the equation
**/
export interface Equation extends JsonLd {
  equation: string;
  unit: UnitDefinition;
  equation_type: EquationType;
  species_id?: string | null;
  variables?: Variable[] | null;
  parameters?: Parameter[] | null;
}

export const EquationCodec = D.lazy("Equation", () => D.struct({
    equation: D.string,
    unit: UnitDefinitionCodec,
    equation_type: EquationTypeCodec,
    species_id: D.nullable(D.string),
    variables: D.array(VariableCodec),
    parameters: D.array(ParameterCodec),
}));


/**
    This object describes a variable that is part of an equation.

    * @param id - Unique identifier of the variable.
    * @param name - Name of the variable.
    * @param symbol - Symbol of the variable.
**/
export interface Variable extends JsonLd {
  id: string;
  name: string;
  symbol: string;
}

export const VariableCodec = D.lazy("Variable", () => D.struct({
    id: D.string,
    name: D.string,
    symbol: D.string,
}));


/**
    This object describes the parameters of the kinetic model and can
    include all estimated values.

    * @param id - Unique identifier of the parameter.
    * @param name - Name of the parameter.
    * @param symbol - Symbol of the parameter.
    * @param value - Numerical value of the estimated parameter.
    * @param unit - Unit of the estimated parameter.
    * @param initial_value - Initial value that was used for the parameter estimation.
    * @param upper - Upper bound of the estimated parameter.
    * @param lower - Lower bound of the estimated parameter.
    * @param stderr - Standard error of the estimated parameter.
    * @param constant - Specifies if this parameter is constant
**/
export interface Parameter extends JsonLd {
  id: string;
  name: string;
  symbol: string;
  value?: number | null;
  unit?: UnitDefinition | null;
  initial_value?: number | null;
  upper?: number | null;
  lower?: number | null;
  stderr?: number | null;
  constant?: boolean | null;
}

export const ParameterCodec = D.lazy("Parameter", () => D.struct({
    id: D.string,
    name: D.string,
    symbol: D.string,
    value: D.nullable(D.number),
    unit: D.nullable(UnitDefinitionCodec),
    initial_value: D.nullable(D.number),
    upper: D.nullable(D.number),
    lower: D.nullable(D.number),
    stderr: D.nullable(D.number),
    constant: D.nullable(D.boolean),
}));


/**
    This object describes the result of a measurement, which includes time
    course data of any type defined in DataTypes. It includes initial
    concentrations of all species used in a single measurement.

    * @param id - Unique identifier of the measurement.
    * @param name - Name of the measurement
    * @param species_data - Measurement data of all species that were part of the measurement.
             A species can refer to a protein, complex, or small
             molecule.
    * @param group_id - User-defined group ID to signal relationships between measurements.
    * @param ph - PH value of the measurement.
    * @param temperature - Temperature of the measurement.
    * @param temperature_unit - Unit of the temperature of the measurement.
**/
export interface Measurement extends JsonLd {
  id: string;
  name: string;
  species_data?: MeasurementData[] | null;
  group_id?: string | null;
  ph?: number | null;
  temperature?: number | null;
  temperature_unit?: UnitDefinition | null;
}

export const MeasurementCodec = D.lazy("Measurement", () => D.struct({
    id: D.string,
    name: D.string,
    species_data: D.array(MeasurementDataCodec),
    group_id: D.nullable(D.string),
    ph: D.nullable(D.number),
    temperature: D.nullable(D.number),
    temperature_unit: D.nullable(UnitDefinitionCodec),
}));


/**
    This object describes a single entity of a measurement, which
    corresponds to one species. It also holds replicates that contain
    time course data.

    * @param species_id - The identifier for the described reactant.
    * @param initial - Initial amount of the measurement data. This must be the same as the
             first data point in the
    * @param data_unit - SI unit of the data that was measured.
    * @param time_unit - Time unit of the replicate.
    * @param data_type - Type of data that was measured (e.g. concentration)
    * @param prepared - Amount of the reactant before the measurement. This field should be
             used for specifying the prepared amount of a species in
             the reaction mix. Not to be confused with
    * @param data - Data that was measured.
    * @param time - Time steps of the replicate.
    * @param is_simulated - Whether or not the data has been generated by simulation.
**/
export interface MeasurementData extends JsonLd {
  species_id: string;
  initial: number;
  data_unit: UnitDefinition;
  time_unit: UnitDefinition;
  data_type: DataTypes;
  prepared?: number | null;
  data: number[];
  time: number[];
  is_simulated: boolean;
}

export const MeasurementDataCodec = D.lazy("MeasurementData", () => D.struct({
    species_id: D.string,
    initial: D.number,
    data_unit: UnitDefinitionCodec,
    time_unit: UnitDefinitionCodec,
    data_type: DataTypesCodec,
    prepared: D.nullable(D.number),
    data: D.array(D.number),
    time: D.array(D.number),
    is_simulated: D.boolean,
}));


/**
    Represents a unit definition that is based on the SI unit system.

    * @param id - Unique identifier of the unit definition.
    * @param name - Common name of the unit definition.
    * @param base_units - Base units that define the unit.
**/
export interface UnitDefinition extends JsonLd {
  id?: string | null;
  name?: string | null;
  base_units?: BaseUnit[] | null;
}

export const UnitDefinitionCodec = D.lazy("UnitDefinition", () => D.struct({
    id: D.nullable(D.string),
    name: D.nullable(D.string),
    base_units: D.array(BaseUnitCodec),
}));


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
  multiplier?: number | null;
  scale?: number | null;
}

export const BaseUnitCodec = D.lazy("BaseUnit", () => D.struct({
    kind: UnitTypeCodec,
    exponent: D.number,
    multiplier: D.nullable(D.number),
    scale: D.nullable(D.number),
}));


// EnzymeML Enum definitions
export enum EquationType {
  ASSIGNMENT = 'assignment',
  INITIAL_ASSIGNMENT = 'initialAssignment',
  ODE = 'ode',
  RATE_LAW = 'rateLaw',
}

export const EquationTypeCodec = D.union(
  D.literal(EquationType.ASSIGNMENT),
  D.literal(EquationType.INITIAL_ASSIGNMENT),
  D.literal(EquationType.ODE),
  D.literal(EquationType.RATE_LAW),
);

export enum DataTypes {
  ABSORBANCE = 'http://purl.allotrope.org/ontologies/quality#AFQ_0000061',
  CONCENTRATION = 'http://purl.obolibrary.org/obo/PATO_0000033',
  CONVERSION = 'http://purl.allotrope.org/ontologies/quality#AFQ_0000226',
  FLUORESCENCE = 'http://purl.obolibrary.org/obo/PATO_0000018',
  PEAK_AREA = 'http://purl.allotrope.org/ontologies/result#AFR_0001073',
  TRANSMITTANCE = 'http://purl.allotrope.org/ontologies/result#AFR_0002261',
}

export const DataTypesCodec = D.union(
  D.literal(DataTypes.ABSORBANCE),
  D.literal(DataTypes.CONCENTRATION),
  D.literal(DataTypes.CONVERSION),
  D.literal(DataTypes.FLUORESCENCE),
  D.literal(DataTypes.PEAK_AREA),
  D.literal(DataTypes.TRANSMITTANCE),
);

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

export const UnitTypeCodec = D.union(
  D.literal(UnitType.AMPERE),
  D.literal(UnitType.AVOGADRO),
  D.literal(UnitType.BECQUEREL),
  D.literal(UnitType.CANDELA),
  D.literal(UnitType.CELSIUS),
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