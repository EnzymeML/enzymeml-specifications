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
	ID             *uint           `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
	Name           string          `json:"name" xml:"name" `
	Created        string          `json:"created,omitempty" xml:"created,omitempty" `
	Modified       string          `json:"modified,omitempty" xml:"modified,omitempty" `
	Creators       []Creator       `json:"creators,omitempty" xml:"creators,omitempty" gorm:"many2many:enzymemldocument_creators;"`
	Vessels        []Vessel        `json:"vessels,omitempty" xml:"vessels,omitempty" gorm:"many2many:enzymemldocument_vessels;"`
	Proteins       []Protein       `json:"proteins,omitempty" xml:"proteins,omitempty" gorm:"many2many:enzymemldocument_proteins;"`
	Complexes      []Complex       `json:"complexes,omitempty" xml:"complexes,omitempty" gorm:"many2many:enzymemldocument_complexes;"`
	SmallMolecules []SmallMolecule `json:"small_molecules,omitempty" xml:"small_molecules,omitempty" gorm:"many2many:enzymemldocument_small_molecules;"`
	Reactions      []Reaction      `json:"reactions,omitempty" xml:"reactions,omitempty" gorm:"many2many:enzymemldocument_reactions;"`
	Measurements   []Measurement   `json:"measurements,omitempty" xml:"measurements,omitempty" gorm:"many2many:enzymemldocument_measurements;"`
	Equations      []Equation      `json:"equations,omitempty" xml:"equations,omitempty" gorm:"many2many:enzymemldocument_equations;"`
	Parameters     []Parameter     `json:"parameters,omitempty" xml:"parameters,omitempty" gorm:"many2many:enzymemldocument_parameters;"`
	References     []string        `json:"references,omitempty" xml:"references,omitempty" `
}

// Creator
//
// The Creator object represents an individual author or contributor who has
// participated in creating or modifying the EnzymeML Document. It captures
// essential personal information such as their name and contact details,
// allowing proper attribution and enabling communication with the document's
// creators.
type Creator struct {
	ID         *uint  `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
	GivenName  string `json:"given_name" xml:"given_name" `
	FamilyName string `json:"family_name" xml:"family_name" `
	Mail       string `json:"mail" xml:"mail" `
}

// Vessel
//
// The Vessel object represents containers used to conduct experiments, such as
// reaction vessels, microplates, or bioreactors. It captures key properties
// like volume and whether the volume remains constant during the experiment.
type Vessel struct {
	Id       string         `json:"id" xml:"id" gorm:"primaryKey"`
	Name     string         `json:"name" xml:"name" `
	Volume   float64        `json:"volume" xml:"volume" `
	Unit     UnitDefinition `json:"unit" xml:"unit" `
	Constant bool           `json:"constant" xml:"constant" `
}

// Protein
//
// The Protein object represents enzymes and other proteins involved in the
// experiment.
type Protein struct {
	Id            string   `json:"id" xml:"id" gorm:"primaryKey"`
	Name          string   `json:"name" xml:"name" `
	Constant      bool     `json:"constant" xml:"constant" `
	Sequence      string   `json:"sequence,omitempty" xml:"sequence,omitempty" `
	VesselId      string   `json:"vessel_id,omitempty" xml:"vessel_id,omitempty" `
	Ecnumber      string   `json:"ecnumber,omitempty" xml:"ecnumber,omitempty" `
	Organism      string   `json:"organism,omitempty" xml:"organism,omitempty" `
	OrganismTaxId string   `json:"organism_tax_id,omitempty" xml:"organism_tax_id,omitempty" `
	References    []string `json:"references,omitempty" xml:"references,omitempty" `
}

// Complex
//
// The Complex object allows the grouping of multiple species using their . This
// enables the representation of protein-small molecule complexes (e.g., enzyme-
// substrate complexes) as well as buffer or solvent mixtures (combinations of
// SmallMolecule species).
type Complex struct {
	Id           string   `json:"id" xml:"id" gorm:"primaryKey"`
	Name         string   `json:"name" xml:"name" `
	Constant     bool     `json:"constant" xml:"constant" `
	VesselId     string   `json:"vessel_id,omitempty" xml:"vessel_id,omitempty" `
	Participants []string `json:"participants,omitempty" xml:"participants,omitempty" `
}

// SmallMolecule
//
// The SmallMolecule object represents small chemical compounds that participate
// in the experiment as substrates, products, or modifiers. It captures key
// molecular identifiers like SMILES and InChI.
type SmallMolecule struct {
	Id              string   `json:"id" xml:"id" gorm:"primaryKey"`
	Name            string   `json:"name" xml:"name" `
	Constant        bool     `json:"constant" xml:"constant" `
	VesselId        string   `json:"vessel_id,omitempty" xml:"vessel_id,omitempty" `
	CanonicalSmiles string   `json:"canonical_smiles,omitempty" xml:"canonical_smiles,omitempty" `
	Inchi           string   `json:"inchi,omitempty" xml:"inchi,omitempty" `
	Inchikey        string   `json:"inchikey,omitempty" xml:"inchikey,omitempty" `
	References      []string `json:"references,omitempty" xml:"references,omitempty" `
}

// Reaction
//
// The Reaction object represents a chemical or enzymatic reaction and holds the
// different species and modifiers that are part of the reaction.
type Reaction struct {
	Id         string            `json:"id" xml:"id" gorm:"primaryKey"`
	Name       string            `json:"name" xml:"name" `
	Reversible bool              `json:"reversible" xml:"reversible" `
	KineticLaw Equation          `json:"kinetic_law,omitempty" xml:"kinetic_law,omitempty" `
	Species    []ReactionElement `json:"species,omitempty" xml:"species,omitempty" gorm:"many2many:reaction_species;"`
	Modifiers  []string          `json:"modifiers,omitempty" xml:"modifiers,omitempty" `
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
	ID            *uint   `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
	SpeciesId     string  `json:"species_id" xml:"species_id" `
	Stoichiometry float64 `json:"stoichiometry" xml:"stoichiometry" `
}

// Equation
//
// The Equation object describes a mathematical equation used to model parts of a
// reaction system.
type Equation struct {
	ID           *uint        `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
	SpeciesId    string       `json:"species_id" xml:"species_id" `
	Equation     string       `json:"equation" xml:"equation" `
	EquationType EquationType `json:"equation_type" xml:"equation_type" `
	Variables    []Variable   `json:"variables,omitempty" xml:"variables,omitempty" gorm:"many2many:equation_variables;"`
}

// Variable
//
// This object describes a variable that is part of an equation. Variables can
// represent species concentrations, time, or other quantities that appear in
// mathematical expressions. Each variable must have a unique identifier, name,
// and symbol that is used in equations.
type Variable struct {
	Id     string `json:"id" xml:"id" gorm:"primaryKey"`
	Name   string `json:"name" xml:"name" `
	Symbol string `json:"symbol" xml:"symbol" `
}

// Parameter
//
// This object describes parameters used in kinetic models, including estimated
// values, bounds, and associated uncertainties. Parameters can represent rate
// constants, binding constants, or other numerical values that appear in rate
// equations or other mathematical expressions.
type Parameter struct {
	Id           string         `json:"id" xml:"id" gorm:"primaryKey"`
	Name         string         `json:"name" xml:"name" `
	Symbol       string         `json:"symbol" xml:"symbol" `
	Value        float64        `json:"value,omitempty" xml:"value,omitempty" `
	Unit         UnitDefinition `json:"unit,omitempty" xml:"unit,omitempty" `
	InitialValue float64        `json:"initial_value,omitempty" xml:"initial_value,omitempty" `
	UpperBound   float64        `json:"upper_bound,omitempty" xml:"upper_bound,omitempty" `
	LowerBound   float64        `json:"lower_bound,omitempty" xml:"lower_bound,omitempty" `
	Stderr       float64        `json:"stderr,omitempty" xml:"stderr,omitempty" `
	Constant     bool           `json:"constant,omitempty" xml:"constant,omitempty" `
}

// Measurement
//
// This object describes a single measurement, which includes time course data
// of any type defined in DataTypes. It contains initial concentrations and
// measurement data for all species involved in the experiment. Multiple
// measurements can be grouped together using the group_id field to indicate
// they are part of the same experimental series.
type Measurement struct {
	Id              string            `json:"id" xml:"id" gorm:"primaryKey"`
	Name            string            `json:"name" xml:"name" `
	SpeciesData     []MeasurementData `json:"species_data,omitempty" xml:"species_data,omitempty" gorm:"many2many:measurement_species_data;"`
	GroupId         string            `json:"group_id,omitempty" xml:"group_id,omitempty" `
	Ph              float64           `json:"ph,omitempty" xml:"ph,omitempty" `
	Temperature     float64           `json:"temperature,omitempty" xml:"temperature,omitempty" `
	TemperatureUnit UnitDefinition    `json:"temperature_unit,omitempty" xml:"temperature_unit,omitempty" `
}

// MeasurementData
//
// This object describes a single entity of a measurement, which corresponds to
// one species (Protein, Complex, SmallMolecule). It contains time course data
// for that species, including the initial amount, prepared amount, and measured
// data points over time. Endpoint data is treated as a time course data point
// with only one data point.
type MeasurementData struct {
	ID          *uint          `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
	SpeciesId   string         `json:"species_id" xml:"species_id" `
	Initial     float64        `json:"initial" xml:"initial" `
	DataUnit    UnitDefinition `json:"data_unit" xml:"data_unit" `
	DataType    DataTypes      `json:"data_type" xml:"data_type" `
	Prepared    float64        `json:"prepared,omitempty" xml:"prepared,omitempty" `
	Data        []float64      `json:"data,omitempty" xml:"data,omitempty" `
	Time        []float64      `json:"time,omitempty" xml:"time,omitempty" `
	TimeUnit    UnitDefinition `json:"time_unit,omitempty" xml:"time_unit,omitempty" `
	IsSimulated bool           `json:"is_simulated" xml:"is_simulated" `
}

// UnitDefinition
//
// Represents a unit definition that is based on the SI unit system.
type UnitDefinition struct {
	Id        string     `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey"`
	Name      string     `json:"name,omitempty" xml:"name,attr,omitempty" `
	BaseUnits []BaseUnit `json:"base_units,omitempty" xml:"base_units,omitempty" gorm:"many2many:unitdefinition_base_units;"`
}

// BaseUnit
//
// Represents a base unit in the unit definition.
type BaseUnit struct {
	ID         *uint    `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
	Kind       UnitType `json:"kind" xml:"kind,attr" `
	Exponent   int64    `json:"exponent" xml:"exponent,attr" `
	Multiplier float64  `json:"multiplier,omitempty" xml:"multiplier,attr,omitempty" `
	Scale      float64  `json:"scale,omitempty" xml:"scale,attr,omitempty" `
}

// Enum definitions
type EquationType string

const (
	ASSIGNMENT         EquationType = "assignment"
	INITIAL_ASSIGNMENT EquationType = "initialAssignment"
	ODE                EquationType = "ode"
	RATE_LAW           EquationType = "rateLaw"
)

type DataTypes string

const (
	ABSORBANCE    DataTypes = "absorbance"
	CONCENTRATION DataTypes = "concentration"
	CONVERSION    DataTypes = "conversion"
	FLUORESCENCE  DataTypes = "fluorescence"
	PEAK_AREA     DataTypes = "peakarea"
	TRANSMITTANCE DataTypes = "transmittance"
)

type UnitType string

const (
	AMPERE        UnitType = "ampere"
	AVOGADRO      UnitType = "avogadro"
	BECQUEREL     UnitType = "becquerel"
	CANDELA       UnitType = "candela"
	CELSIUS       UnitType = "celsius"
	COULOMB       UnitType = "coulomb"
	DIMENSIONLESS UnitType = "dimensionless"
	FARAD         UnitType = "farad"
	GRAM          UnitType = "gram"
	GRAY          UnitType = "gray"
	HENRY         UnitType = "henry"
	HERTZ         UnitType = "hertz"
	ITEM          UnitType = "item"
	JOULE         UnitType = "joule"
	KATAL         UnitType = "katal"
	KELVIN        UnitType = "kelvin"
	KILOGRAM      UnitType = "kilogram"
	LITRE         UnitType = "litre"
	LUMEN         UnitType = "lumen"
	LUX           UnitType = "lux"
	METRE         UnitType = "metre"
	MOLE          UnitType = "mole"
	NEWTON        UnitType = "newton"
	OHM           UnitType = "ohm"
	PASCAL        UnitType = "pascal"
	RADIAN        UnitType = "radian"
	SECOND        UnitType = "second"
	SIEMENS       UnitType = "siemens"
	SIEVERT       UnitType = "sievert"
	STERADIAN     UnitType = "steradian"
	TESLA         UnitType = "tesla"
	VOLT          UnitType = "volt"
	WATT          UnitType = "watt"
	WEBER         UnitType = "weber"
)
