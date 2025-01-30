//! This file contains Rust struct definitions with serde serialization.
//!
//! WARNING: This is an auto-generated file.
//! Do not edit directly - any changes will be overwritten.

use serde::{Deserialize, Serialize};
use std::collections::HashMap;

// JSON-LD base types
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct JsonLdContext(pub HashMap<String, serde_json::Value>);

#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct JsonLd {
    #[serde(rename = "@context", skip_serializing_if = "Option::is_none")]
    pub context: Option<JsonLdContext>,
    #[serde(rename = "@id", skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    #[serde(rename = "@type", skip_serializing_if = "Option::is_none")]
    pub type_: Option<String>,
}

//
// EnzymeML Type definitions
//
/// This is the root object that composes all objects found in an EnzymeML
/// document. It also includes general metadata such as the name of
/// the document, when it was created/modified, and references to
/// publications, databases, and arbitrary links to the web.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct EnzymeMLDocument {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Title of the EnzymeML Document.
    pub name: String,
    /// Contains references to publications, databases, and arbitrary links to
    /// the web.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub references: Option<Vec<String>>,
    /// Date the EnzymeML document was created.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub created: Option<String>,
    /// Date the EnzymeML document was modified.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub modified: Option<String>,
    /// Contains all authors that are part of the experiment.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub creators: Option<Vec<Creator>>,
    /// Contains all vessels that are part of the experiment.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub vessels: Option<Vec<Vessel>>,
    /// Contains all proteins that are part of the experiment.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub proteins: Option<Vec<Protein>>,
    /// Contains all complexes that are part of the experiment.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub complexes: Option<Vec<Complex>>,
    /// Contains all reactants that are part of the experiment.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub small_molecules: Option<Vec<SmallMolecule>>,
    /// Dictionary mapping from reaction IDs to reaction-describing objects.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub reactions: Option<Vec<Reaction>>,
    /// Contains measurements that describe outcomes of an experiment.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub measurements: Option<Vec<Measurement>>,
    /// Contains ordinary differential equations that describe the kinetic
    /// model.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub equations: Option<Vec<Equation>>,
    /// List of parameters that are part of the equation
    #[serde(skip_serializing_if = "Option::is_none")]
    pub parameters: Option<Vec<Parameter>>,
}

/// The creator object contains all information about authors that
/// contributed to the resulting document.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Creator {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Given name of the author or contributor.
    pub given_name: String,
    /// Family name of the author or contributor.
    pub family_name: String,
    /// Email address of the author or contributor.
    pub mail: String,
}

/// This object describes vessels in which the experiment has been carried
/// out. These can include any type of vessel used in biocatalytic
/// experiments.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Vessel {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique identifier of the vessel.
    pub id: String,
    /// Name of the used vessel.
    pub name: String,
    /// Volumetric value of the vessel.
    pub volume: f64,
    /// Volumetric unit of the vessel.
    pub unit: UnitDefinition,
    /// Whether the volume of the vessel is constant or not.
    pub constant: bool,
}

/// This object describes the proteins that were used or formed throughout
/// the experiment.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Protein {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique internal identifier of the protein.
    pub id: String,
    pub name: String,
    pub constant: bool,
    /// Amino acid sequence of the protein
    #[serde(skip_serializing_if = "Option::is_none")]
    pub sequence: Option<String>,
    /// Unique identifier of the vessel this protein has been used in.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub vessel_id: Option<String>,
    /// EC number of the protein.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub ecnumber: Option<String>,
    /// Organism the protein was expressed in.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub organism: Option<String>,
    /// Taxonomy identifier of the expression host.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub organism_tax_id: Option<String>,
    /// Array of references to publications, database entries, etc. that
    /// describe the protein.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub references: Option<Vec<String>>,
}

/// This object describes complexes made of reactants and/or proteins that
/// were used or produced in the course of the experiment.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Complex {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique identifier of the complex.
    pub id: String,
    pub name: String,
    pub constant: bool,
    /// Unique identifier of the vessel this complex has been used in.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub vessel_id: Option<String>,
    /// Array of IDs the complex contains
    #[serde(skip_serializing_if = "Option::is_none")]
    pub participants: Option<Vec<String>>,
}

/// This object describes the reactants that were used or produced in the
/// course of the experiment.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct SmallMolecule {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique identifier of the small molecule.
    pub id: String,
    pub name: String,
    pub constant: bool,
    /// Unique identifier of the vessel this small molecule has been used in.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub vessel_id: Option<String>,
    /// Canonical Simplified Molecular-Input Line-Entry System (SMILES)
    /// encoding of the reactant.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub canonical_smiles: Option<String>,
    /// International Chemical Identifier (InChI) encoding of the reactant.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub inchi: Option<String>,
    /// Hashed International Chemical Identifier (InChIKey) encoding of the
    /// reactant.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub inchikey: Option<String>,
    /// Array of references to publications, database entries, etc. that
    /// describe the reactant.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub references: Option<Vec<String>>,
}

/// This object describes a chemical or enzymatic reaction that was
/// investigated in the course of the experiment. All species used
/// within this object need to be part of the data model.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Reaction {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique identifier of the reaction.
    pub id: String,
    /// Name of the reaction.
    pub name: String,
    /// Whether the reaction is reversible or irreversible
    pub reversible: bool,
    /// Mathematical expression of the reaction.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub kinetic_law: Option<Equation>,
    /// List of reaction elements that are part of the reaction.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub species: Option<Vec<ReactionElement>>,
    /// List of reaction elements that are not part of the reaction but
    /// influence it.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub modifiers: Option<Vec<String>>,
}

/// This object is part of the Reaction object and describes either an
/// educt, product or modifier. The latter includes buffers, counter-
/// ions as well as proteins/enzymes.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct ReactionElement {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Internal identifier to either a protein or reactant defined in the
    /// EnzymeMLDocument.
    pub species_id: String,
    /// Float number representing the associated stoichiometry.
    pub stoichiometry: f64,
}

/// This object describes an equation that can be used to model the
/// kinetics of a reaction. There are different types of equations
/// that can be used to model the kinetics of a reaction. The equation
/// can be an ordinary differential equation, a rate law or assignment
/// rule.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Equation {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Mathematical expression of the equation.
    pub equation: String,
    /// Type of the equation.
    pub equation_type: EquationType,
    /// Internal identifier to a species defined in the EnzymeMLDocument,
    /// given it is a rate equation.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub species_id: Option<String>,
    /// List of variables that are part of the equation
    #[serde(skip_serializing_if = "Option::is_none")]
    pub variables: Option<Vec<Variable>>,
}

/// This object describes a variable that is part of an equation.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Variable {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique identifier of the variable.
    pub id: String,
    /// Name of the variable.
    pub name: String,
    /// Symbol of the variable.
    pub symbol: String,
}

/// This object describes the parameters of the kinetic model and can
/// include all estimated values.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Parameter {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique identifier of the parameter.
    pub id: String,
    /// Name of the parameter.
    pub name: String,
    /// Symbol of the parameter.
    pub symbol: String,
    /// Numerical value of the estimated parameter.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub value: Option<f64>,
    /// Unit of the estimated parameter.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub unit: Option<UnitDefinition>,
    /// Initial value that was used for the parameter estimation.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub initial_value: Option<f64>,
    /// Upper bound of the estimated parameter.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub upper: Option<f64>,
    /// Lower bound of the estimated parameter.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub lower: Option<f64>,
    /// Standard error of the estimated parameter.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub stderr: Option<f64>,
    /// Specifies if this parameter is constant
    #[serde(skip_serializing_if = "Option::is_none")]
    pub constant: Option<bool>,
}

/// This object describes the result of a measurement, which includes time
/// course data of any type defined in DataTypes. It includes initial
/// concentrations of all species used in a single measurement.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct Measurement {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique identifier of the measurement.
    pub id: String,
    /// Name of the measurement
    pub name: String,
    /// Measurement data of all species that were part of the measurement. A
    /// species can refer to a protein, complex, or small molecule.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub species_data: Option<Vec<MeasurementData>>,
    /// User-defined group ID to signal relationships between measurements.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub group_id: Option<String>,
    /// PH value of the measurement.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub ph: Option<f64>,
    /// Temperature of the measurement.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub temperature: Option<f64>,
    /// Unit of the temperature of the measurement.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub temperature_unit: Option<UnitDefinition>,
}

/// This object describes a single entity of a measurement, which
/// corresponds to one species. It also holds replicates that contain
/// time course data.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct MeasurementData {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// The identifier for the described reactant.
    pub species_id: String,
    /// Initial amount of the measurement data. This must be the same as the
    /// first data point in the array.
    pub initial: f64,
    /// SI unit of the data that was measured.
    pub data_unit: UnitDefinition,
    /// Type of data that was measured (e.g. concentration)
    pub data_type: DataTypes,
    /// Amount of the reactant before the measurement. This field should
    /// be used for specifying the prepared amount of a species in
    /// the reaction mix. Not to be confused with , specifying the
    /// concentration at the first data point from the array.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub prepared: Option<f64>,
    /// Data that was measured.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub data: Option<Vec<f64>>,
    /// Time steps of the replicate.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub time: Option<Vec<f64>>,
    /// Time unit of the replicate.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub time_unit: Option<UnitDefinition>,
    /// Whether or not the data has been generated by simulation.
    pub is_simulated: bool,
}

/// Represents a unit definition that is based on the SI unit system.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct UnitDefinition {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Unique identifier of the unit definition.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub id: Option<String>,
    /// Common name of the unit definition.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub name: Option<String>,
    /// Base units that define the unit.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub base_units: Option<Vec<BaseUnit>>,
}

/// Represents a base unit in the unit definition.
#[derive(Debug, Default, Clone, Serialize, Deserialize)]
pub struct BaseUnit {
    #[serde(flatten)]
    pub json_ld: JsonLd,
    /// Kind of the base unit (e.g., meter, kilogram, second).
    pub kind: UnitType,
    /// Exponent of the base unit in the unit definition.
    pub exponent: i64,
    /// Multiplier of the base unit in the unit definition.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub multiplier: Option<f64>,
    /// Scale of the base unit in the unit definition.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub scale: Option<f64>,
}

//
// EnzymeML Enum definitions
//

#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum EquationType {
    #[serde(rename = "assignment")]
    ASSIGNMENT,
    #[serde(rename = "initialAssignment")]
    INITIAL_ASSIGNMENT,
    #[serde(rename = "ode")]
    ODE,
    #[serde(rename = "rateLaw")]
    RATE_LAW,
}


#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum DataTypes {
    #[serde(rename = "http://purl.allotrope.org/ontologies/quality#AFQ_0000061")]
    ABSORBANCE,
    #[serde(rename = "http://purl.obolibrary.org/obo/PATO_0000033")]
    CONCENTRATION,
    #[serde(rename = "http://purl.allotrope.org/ontologies/quality#AFQ_0000226")]
    CONVERSION,
    #[serde(rename = "http://purl.obolibrary.org/obo/PATO_0000018")]
    FLUORESCENCE,
    #[serde(rename = "http://purl.allotrope.org/ontologies/result#AFR_0001073")]
    PEAK_AREA,
    #[serde(rename = "http://purl.allotrope.org/ontologies/result#AFR_0002261")]
    TRANSMITTANCE,
}


#[derive(Debug, Clone, Serialize, Deserialize)]
pub enum UnitType {
    #[serde(rename = "ampere")]
    AMPERE,
    #[serde(rename = "avogadro")]
    AVOGADRO,
    #[serde(rename = "becquerel")]
    BECQUEREL,
    #[serde(rename = "candela")]
    CANDELA,
    #[serde(rename = "celsius")]
    CELSIUS,
    #[serde(rename = "coulomb")]
    COULOMB,
    #[serde(rename = "dimensionless")]
    DIMENSIONLESS,
    #[serde(rename = "farad")]
    FARAD,
    #[serde(rename = "gram")]
    GRAM,
    #[serde(rename = "gray")]
    GRAY,
    #[serde(rename = "henry")]
    HENRY,
    #[serde(rename = "hertz")]
    HERTZ,
    #[serde(rename = "item")]
    ITEM,
    #[serde(rename = "joule")]
    JOULE,
    #[serde(rename = "katal")]
    KATAL,
    #[serde(rename = "kelvin")]
    KELVIN,
    #[serde(rename = "kilogram")]
    KILOGRAM,
    #[serde(rename = "litre")]
    LITRE,
    #[serde(rename = "lumen")]
    LUMEN,
    #[serde(rename = "lux")]
    LUX,
    #[serde(rename = "metre")]
    METRE,
    #[serde(rename = "mole")]
    MOLE,
    #[serde(rename = "newton")]
    NEWTON,
    #[serde(rename = "ohm")]
    OHM,
    #[serde(rename = "pascal")]
    PASCAL,
    #[serde(rename = "radian")]
    RADIAN,
    #[serde(rename = "second")]
    SECOND,
    #[serde(rename = "siemens")]
    SIEMENS,
    #[serde(rename = "sievert")]
    SIEVERT,
    #[serde(rename = "steradian")]
    STERADIAN,
    #[serde(rename = "tesla")]
    TESLA,
    #[serde(rename = "volt")]
    VOLT,
    #[serde(rename = "watt")]
    WATT,
    #[serde(rename = "weber")]
    WEBER,
}


//
// Enum definitions for attributes with multiple types
//