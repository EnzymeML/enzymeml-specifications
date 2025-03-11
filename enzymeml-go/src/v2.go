// Package enzymeml v2 contains Go struct definitions with JSON serialization.
//
// WARNING: This is an auto-generated file.
// Do not edit directly - any changes will be overwritten.

package enzymeml_v2

//
// Type definitions
//

// EnzymeMLDocument
//
// The EnzymeMLDocument is the root object that serves as a container for all
// components of an enzymatic experiment. It includes essential metadata about
// the document itself, such as its title and creation/modification dates,
// as well as references to related publications and databases. Additionally,
// it contains comprehensive information about the experimental setup,
// including reaction vessels, proteins, complexes, small molecules, reactions,
// measurements, equations, and parameters.
type EnzymeMLDocument struct {
    Name string `json:"name" `
    Created string `json:"created,omitempty" `
    Modified string `json:"modified,omitempty" `
    Version string `json:"version,omitempty" `
    Creators []Creator `json:"creators,omitempty" `
    Vessels []Vessel `json:"vessels,omitempty" `
    Proteins []Protein `json:"proteins,omitempty" `
    Complexes []Complex `json:"complexes,omitempty" `
    SmallMolecules []SmallMolecule `json:"small_molecules,omitempty" `
    Reactions []Reaction `json:"reactions,omitempty" `
    Measurements []Measurement `json:"measurements,omitempty" `
    Equations []Equation `json:"equations,omitempty" `
    Parameters []Parameter `json:"parameters,omitempty" `
    References []string `json:"references,omitempty" `
}

// Creator
//
// The Creator object represents an individual author or contributor who has
// participated in creating or modifying the EnzymeML Document. It captures
// essential personal information such as their name and contact details,
// allowing proper attribution and enabling communication with the document's
// creators.
type Creator struct {
    GivenName string `json:"given_name" `
    FamilyName string `json:"family_name" `
    Mail string `json:"mail" `
}

// Vessel
//
// The Vessel object represents containers used to conduct experiments, such as
// reaction vessels, microplates, or bioreactors. It captures key properties
// like volume and whether the volume remains constant during the experiment.
type Vessel struct {
    Id string `json:"id" `
    Name string `json:"name" `
    Volume float64 `json:"volume" `
    Unit UnitDefinition `json:"unit" `
    Constant bool `json:"constant" `
}

// Protein
//
// The Protein object represents enzymes and other proteins involved in the
// experiment.
type Protein struct {
    Id string `json:"id" `
    Name string `json:"name" `
    Constant bool `json:"constant" `
    Sequence string `json:"sequence,omitempty" `
    VesselId string `json:"vessel_id,omitempty" `
    Ecnumber string `json:"ecnumber,omitempty" `
    Organism string `json:"organism,omitempty" `
    OrganismTaxId string `json:"organism_tax_id,omitempty" `
    References []string `json:"references,omitempty" `
}

// Complex
//
// The Complex object allows the grouping of multiple species using their . This
// enables the representation of protein-small molecule complexes (e.g., enzyme-
// substrate complexes) as well as buffer or solvent mixtures (combinations of
// SmallMolecule species).
type Complex struct {
    Id string `json:"id" `
    Name string `json:"name" `
    Constant bool `json:"constant" `
    VesselId string `json:"vessel_id,omitempty" `
    Participants []string `json:"participants,omitempty" `
}

// SmallMolecule
//
// The SmallMolecule object represents small chemical compounds that participate
// in the experiment as substrates, products, or modifiers. It captures key
// molecular identifiers like SMILES and InChI.
type SmallMolecule struct {
    Id string `json:"id" `
    Name string `json:"name" `
    Constant bool `json:"constant" `
    VesselId string `json:"vessel_id,omitempty" `
    CanonicalSmiles string `json:"canonical_smiles,omitempty" `
    Inchi string `json:"inchi,omitempty" `
    Inchikey string `json:"inchikey,omitempty" `
    References []string `json:"references,omitempty" `
}

// Reaction
//
// The Reaction object represents a chemical or enzymatic reaction and holds the
// different species and modifiers that are part of the reaction.
type Reaction struct {
    Id string `json:"id" `
    Name string `json:"name" `
    Reversible bool `json:"reversible" `
    KineticLaw Equation `json:"kinetic_law,omitempty" `
    Species []ReactionElement `json:"species,omitempty" `
    Modifiers []string `json:"modifiers,omitempty" `
}

// ReactionElement
//
// This object is part of the object and describes a species (SmallMolecule,
// Protein, Complex) participating in the reaction. THE TYPE OF THE REACTION
// ELEMENT IS SPECIFIED IN THE TYPE FIELD. The stochiometry is of the species
// is specified in the field, whereas negative values indicate that the species
// is a reactant and positive values indicate that the species is a product of
// the reaction.
type ReactionElement struct {
    SpeciesId string `json:"species_id" `
    Stoichiometry float64 `json:"stoichiometry" `
}

// Equation
//
// The Equation object describes a mathematical equation used to model parts of a
// reaction system.
type Equation struct {
    SpeciesId string `json:"species_id" `
    Equation string `json:"equation" `
    EquationType EquationType `json:"equation_type" `
    Variables []Variable `json:"variables,omitempty" `
}

// Variable
//
// This object describes a variable that is part of an equation. Variables can
// represent species concentrations, time, or other quantities that appear in
// mathematical expressions. Each variable must have a unique identifier, name,
// and symbol that is used in equations.
type Variable struct {
    Id string `json:"id" `
    Name string `json:"name" `
    Symbol string `json:"symbol" `
}

// Parameter
//
// This object describes parameters used in kinetic models, including estimated
// values, bounds, and associated uncertainties. Parameters can represent rate
// constants, binding constants, or other numerical values that appear in rate
// equations or other mathematical expressions.
type Parameter struct {
    Id string `json:"id" `
    Name string `json:"name" `
    Symbol string `json:"symbol" `
    Value float64 `json:"value,omitempty" `
    Unit UnitDefinition `json:"unit,omitempty" `
    InitialValue float64 `json:"initial_value,omitempty" `
    UpperBound float64 `json:"upper_bound,omitempty" `
    LowerBound float64 `json:"lower_bound,omitempty" `
    Stderr float64 `json:"stderr,omitempty" `
    Constant bool `json:"constant,omitempty" `
}

// Measurement
//
// This object describes a single measurement, which includes time course data
// of any type defined in DataTypes. It contains initial concentrations and
// measurement data for all species involved in the experiment. Multiple
// measurements can be grouped together using the group_id field to indicate
// they are part of the same experimental series.
type Measurement struct {
    Id string `json:"id" `
    Name string `json:"name" `
    SpeciesData []MeasurementData `json:"species_data,omitempty" `
    GroupId string `json:"group_id,omitempty" `
    Ph float64 `json:"ph,omitempty" `
    Temperature float64 `json:"temperature,omitempty" `
    TemperatureUnit UnitDefinition `json:"temperature_unit,omitempty" `
}

// MeasurementData
//
// This object describes a single entity of a measurement, which corresponds to
// one species (Protein, Complex, SmallMolecule). It contains time course data
// for that species, including the initial amount, prepared amount, and measured
// data points over time. Endpoint data is treated as a time course data point
// with only one data point.
type MeasurementData struct {
    SpeciesId string `json:"species_id" `
    Initial float64 `json:"initial" `
    DataUnit UnitDefinition `json:"data_unit" `
    DataType DataTypes `json:"data_type" `
    Prepared float64 `json:"prepared,omitempty" `
    Data []float64 `json:"data,omitempty" `
    Time []float64 `json:"time,omitempty" `
    TimeUnit UnitDefinition `json:"time_unit,omitempty" `
    IsSimulated bool `json:"is_simulated" `
}

// UnitDefinition
//
// Represents a unit definition that is based on the SI unit system.
type UnitDefinition struct {
    Id string `json:"id,omitempty" `
    Name string `json:"name,omitempty" `
    BaseUnits []BaseUnit `json:"base_units,omitempty" `
}

// BaseUnit
//
// Represents a base unit in the unit definition.
type BaseUnit struct {
    Kind UnitType `json:"kind" `
    Exponent int64 `json:"exponent" `
    Multiplier float64 `json:"multiplier,omitempty" `
    Scale float64 `json:"scale,omitempty" `
}

//
// Enum definitions
//
type EquationType string

const (
    ASSIGNMENT EquationType = "assignment"
    INITIAL_ASSIGNMENT EquationType = "initialAssignment"
    ODE EquationType = "ode"
    RATE_LAW EquationType = "rateLaw"
)
type DataTypes string

const (
    ABSORBANCE DataTypes = "absorbance"
    CONCENTRATION DataTypes = "concentration"
    CONVERSION DataTypes = "conversion"
    FLUORESCENCE DataTypes = "fluorescence"
    PEAK_AREA DataTypes = "peakarea"
    TRANSMITTANCE DataTypes = "transmittance"
)
type UnitType string

const (
    AMPERE UnitType = "ampere"
    AVOGADRO UnitType = "avogadro"
    BECQUEREL UnitType = "becquerel"
    CANDELA UnitType = "candela"
    CELSIUS UnitType = "celsius"
    COULOMB UnitType = "coulomb"
    DIMENSIONLESS UnitType = "dimensionless"
    FARAD UnitType = "farad"
    GRAM UnitType = "gram"
    GRAY UnitType = "gray"
    HENRY UnitType = "henry"
    HERTZ UnitType = "hertz"
    ITEM UnitType = "item"
    JOULE UnitType = "joule"
    KATAL UnitType = "katal"
    KELVIN UnitType = "kelvin"
    KILOGRAM UnitType = "kilogram"
    LITRE UnitType = "litre"
    LUMEN UnitType = "lumen"
    LUX UnitType = "lux"
    METRE UnitType = "metre"
    MOLE UnitType = "mole"
    NEWTON UnitType = "newton"
    OHM UnitType = "ohm"
    PASCAL UnitType = "pascal"
    RADIAN UnitType = "radian"
    SECOND UnitType = "second"
    SIEMENS UnitType = "siemens"
    SIEVERT UnitType = "sievert"
    STERADIAN UnitType = "steradian"
    TESLA UnitType = "tesla"
    VOLT UnitType = "volt"
    WATT UnitType = "watt"
    WEBER UnitType = "weber"
)