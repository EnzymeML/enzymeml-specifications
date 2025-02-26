// Package enzymeml contains Go struct definitions with JSON serialization.
//
// WARNING: This is an auto-generated file.
// Do not edit directly - any changes will be overwritten.

package enzymeml

import (
	"encoding/json"
	"fmt"
)

//
// Type definitions
//

// EnzymeMLDocument
//
// This is the root object that composes all objects found in an EnzymeML document.
// It also includes general metadata such as the name of the document, when
// it was created/modified, and references to publications, databases, and
// arbitrary links to the web.
type EnzymeMLDocument struct {
        ID *uint `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
        Name string `json:"name" xml:"name" `
        References []string `json:"references,omitempty" xml:"references,omitempty" `
        Description string `json:"description,omitempty" xml:"description,omitempty" `
        Created string `json:"created,omitempty" xml:"created,omitempty" `
        Modified string `json:"modified,omitempty" xml:"modified,omitempty" `
        Creators []Creator `json:"creators,omitempty" xml:"creators,omitempty" gorm:"many2many:enzymemldocument_creators;"`
        Vessels []Vessel `json:"vessels,omitempty" xml:"vessels,omitempty" gorm:"many2many:enzymemldocument_vessels;"`
        Proteins []Protein `json:"proteins,omitempty" xml:"proteins,omitempty" gorm:"many2many:enzymemldocument_proteins;"`
        Complexes []Complex `json:"complexes,omitempty" xml:"complexes,omitempty" gorm:"many2many:enzymemldocument_complexes;"`
        SmallMolecules []SmallMolecule `json:"small_molecules,omitempty" xml:"small_molecules,omitempty" gorm:"many2many:enzymemldocument_small_molecules;"`
        Reactions []Reaction `json:"reactions,omitempty" xml:"reactions,omitempty" gorm:"many2many:enzymemldocument_reactions;"`
        Measurements []Measurement `json:"measurements,omitempty" xml:"measurements,omitempty" gorm:"many2many:enzymemldocument_measurements;"`
        Equations []Equation `json:"equations,omitempty" xml:"equations,omitempty" gorm:"many2many:enzymemldocument_equations;"`
        Parameters []Parameter `json:"parameters,omitempty" xml:"parameters,omitempty" gorm:"many2many:enzymemldocument_parameters;"`
}

// Creator
//
// The creator object contains all information about authors that contributed to
// the resulting document.
type Creator struct {
        ID *uint `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
        GivenName string `json:"given_name" xml:"given_name" `
        FamilyName string `json:"family_name" xml:"family_name" `
        Mail string `json:"mail" xml:"mail" `
}

// Vessel
//
// This object describes vessels in which the experiment has been carried out.
// These can include any type of vessel used in biocatalytic experiments.
type Vessel struct {
        Id string `json:"id" xml:"id" gorm:"primaryKey"`
        Name string `json:"name" xml:"name" `
        Volume float64 `json:"volume" xml:"volume" `
        Unit UnitDefinition `json:"unit" xml:"unit" `
        Constant bool `json:"constant" xml:"constant" `
}

// Protein
//
// This object describes the proteins that were used or formed throughout the
// experiment.
type Protein struct {
        Id string `json:"id" xml:"id" gorm:"primaryKey"`
        Name string `json:"name" xml:"name" `
        Constant bool `json:"constant" xml:"constant" `
        Sequence string `json:"sequence,omitempty" xml:"sequence,omitempty" `
        VesselId string `json:"vessel_id,omitempty" xml:"vessel_id,omitempty" `
        Ecnumber string `json:"ecnumber,omitempty" xml:"ecnumber,omitempty" `
        Organism string `json:"organism,omitempty" xml:"organism,omitempty" `
        OrganismTaxId string `json:"organism_tax_id,omitempty" xml:"organism_tax_id,omitempty" `
        References []string `json:"references,omitempty" xml:"references,omitempty" `
}

// Complex
//
// This object describes complexes made of reactants and/or proteins that were used
// or produced in the course of the experiment.
type Complex struct {
        Id string `json:"id" xml:"id" gorm:"primaryKey"`
        Name string `json:"name" xml:"name" `
        Constant bool `json:"constant" xml:"constant" `
        VesselId string `json:"vessel_id,omitempty" xml:"vessel_id,omitempty" `
        Participants []string `json:"participants,omitempty" xml:"participants,omitempty" `
}

// SmallMolecule
//
// This object describes the reactants that were used or produced in the course of
// the experiment.
type SmallMolecule struct {
        Id string `json:"id" xml:"id" gorm:"primaryKey"`
        Name string `json:"name" xml:"name" `
        Constant bool `json:"constant" xml:"constant" `
        SynonymousNames []string `json:"synonymous_names,omitempty" xml:"synonymous_names,omitempty" `
        VesselId string `json:"vessel_id,omitempty" xml:"vessel_id,omitempty" `
        CanonicalSmiles string `json:"canonical_smiles,omitempty" xml:"canonical_smiles,omitempty" `
        Inchi string `json:"inchi,omitempty" xml:"inchi,omitempty" `
        Inchikey string `json:"inchikey,omitempty" xml:"inchikey,omitempty" `
        References []string `json:"references,omitempty" xml:"references,omitempty" `
}

// Reaction
//
// This object describes a chemical or enzymatic reaction that was investigated in
// the course of the experiment. All species used within this object need to be
// part of the data model.
type Reaction struct {
        Id string `json:"id" xml:"id" gorm:"primaryKey"`
        Name string `json:"name" xml:"name" `
        Reversible bool `json:"reversible" xml:"reversible" `
        KineticLaw Equation `json:"kinetic_law,omitempty" xml:"kinetic_law,omitempty" `
        Species []ReactionElement `json:"species,omitempty" xml:"species,omitempty" gorm:"many2many:reaction_species;"`
        Modifiers []string `json:"modifiers,omitempty" xml:"modifiers,omitempty" `
}

// ReactionElement
//
// This object is part of the Reaction object and describes either an educt,
// product or modifier. The latter includes buffers, counter-ions as well as
// proteins/enzymes.
type ReactionElement struct {
        ID *uint `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
        SpeciesId string `json:"species_id" xml:"species_id" `
        Stoichiometry float64 `json:"stoichiometry" xml:"stoichiometry" `
}

// Equation
//
// This object describes an equation that can be used to model the kinetics of a
// reaction. There are different types of equations that can be used to model
// the kinetics of a reaction. The equation can be an ordinary differential
// equation, a rate law or assignment rule.
type Equation struct {
        ID *uint `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
        Equation string `json:"equation" xml:"equation" `
        EquationType EquationType `json:"equation_type" xml:"equation_type" `
        SpeciesId string `json:"species_id,omitempty" xml:"species_id,omitempty" `
        Variables []Variable `json:"variables,omitempty" xml:"variables,omitempty" gorm:"many2many:equation_variables;"`
}

// Variable
//
// This object describes a variable that is part of an equation.
type Variable struct {
        Id string `json:"id" xml:"id" gorm:"primaryKey"`
        Name string `json:"name" xml:"name" `
        Symbol string `json:"symbol" xml:"symbol" `
}

// Parameter
//
// This object describes the parameters of the kinetic model and can include all
// estimated values.
type Parameter struct {
        Id string `json:"id" xml:"id" gorm:"primaryKey"`
        Name string `json:"name" xml:"name" `
        Symbol string `json:"symbol" xml:"symbol" `
        Value float64 `json:"value,omitempty" xml:"value,omitempty" `
        Unit UnitDefinition `json:"unit,omitempty" xml:"unit,omitempty" `
        InitialValue float64 `json:"initial_value,omitempty" xml:"initial_value,omitempty" `
        Upper float64 `json:"upper,omitempty" xml:"upper,omitempty" `
        Lower float64 `json:"lower,omitempty" xml:"lower,omitempty" `
        Stderr float64 `json:"stderr,omitempty" xml:"stderr,omitempty" `
        Constant bool `json:"constant,omitempty" xml:"constant,omitempty" `
}

// Measurement
//
// This object describes the result of a measurement, which includes time course
// data of any type defined in DataTypes. It includes initial concentrations of
// all species used in a single measurement.
type Measurement struct {
        Id string `json:"id" xml:"id" gorm:"primaryKey"`
        Name string `json:"name" xml:"name" `
        SpeciesData []MeasurementData `json:"species_data,omitempty" xml:"species_data,omitempty" gorm:"many2many:measurement_species_data;"`
        GroupId string `json:"group_id,omitempty" xml:"group_id,omitempty" `
        Ph float64 `json:"ph,omitempty" xml:"ph,omitempty" `
        Temperature float64 `json:"temperature,omitempty" xml:"temperature,omitempty" `
        TemperatureUnit UnitDefinition `json:"temperature_unit,omitempty" xml:"temperature_unit,omitempty" `
}

// MeasurementData
//
// This object describes a single entity of a measurement, which corresponds to one
// species. It also holds replicates that contain time course data.
type MeasurementData struct {
        ID *uint `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
        SpeciesId string `json:"species_id" xml:"species_id" `
        Initial float64 `json:"initial" xml:"initial" `
        DataUnit UnitDefinition `json:"data_unit" xml:"data_unit" `
        DataType DataTypes `json:"data_type" xml:"data_type" `
        Prepared float64 `json:"prepared,omitempty" xml:"prepared,omitempty" `
        Data []float64 `json:"data,omitempty" xml:"data,omitempty" `
        Time []float64 `json:"time,omitempty" xml:"time,omitempty" `
        TimeUnit UnitDefinition `json:"time_unit,omitempty" xml:"time_unit,omitempty" `
        IsSimulated bool `json:"is_simulated" xml:"is_simulated" `
}

// UnitDefinition
//
// Represents a unit definition that is based on the SI unit system.
type UnitDefinition struct {
        Id string `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey"`
        Name string `json:"name,omitempty" xml:"name,attr,omitempty" `
        BaseUnits []BaseUnit `json:"base_units,omitempty" xml:"base_units,omitempty" gorm:"many2many:unitdefinition_base_units;"`
}

// BaseUnit
//
// Represents a base unit in the unit definition.
type BaseUnit struct {
        ID *uint `json:"id,omitempty" xml:"id,attr,omitempty" gorm:"primaryKey,autoIncrement"`
        Kind UnitType `json:"kind" xml:"kind,attr" `
        Exponent int64 `json:"exponent" xml:"exponent,attr" `
        Multiplier float64 `json:"multiplier,omitempty" xml:"multiplier,attr,omitempty" `
        Scale float64 `json:"scale,omitempty" xml:"scale,attr,omitempty" `
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
    ABSORBANCE DataTypes = "http://purl.allotrope.org/ontologies/quality#AFQ_0000061"
    CONCENTRATION DataTypes = "http://purl.obolibrary.org/obo/PATO_0000033"
    CONVERSION DataTypes = "http://purl.allotrope.org/ontologies/quality#AFQ_0000226"
    FLUORESCENCE DataTypes = "http://purl.obolibrary.org/obo/PATO_0000018"
    PEAK_AREA DataTypes = "http://purl.allotrope.org/ontologies/result#AFR_0001073"
    TRANSMITTANCE DataTypes = "http://purl.allotrope.org/ontologies/result#AFR_0002261"
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