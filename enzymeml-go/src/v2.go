// Package enzymeml contains Go struct definitions with JSON serialization.
//
// WARNING: This is an auto-generated file.
// Do not edit directly - any changes will be overwritten.

package enzymeml


//
// Type definitions
//

// EnzymeMLDocument This is the root object that composes all objects found in an EnzymeML
// document. It also includes general metadata such as the name of
// the document, when it was created/modified, and references to
// publications, databases, and arbitrary links to the web.
type EnzymeMLDocument struct {
        // Title of the EnzymeML Document.
        Name string `json:"name"`
        // Contains references to publications, databases, and arbitrary links to
        // the web.
        References []string `json:"references,omitempty"`
        // Date the EnzymeML document was created.
        Created string `json:"created,omitempty"`
        // Date the EnzymeML document was modified.
        Modified string `json:"modified,omitempty"`
        // Contains all authors that are part of the experiment.
        Creators []Creator `json:"creators,omitempty"`
        // Contains all vessels that are part of the experiment.
        Vessels []Vessel `json:"vessels,omitempty"`
        // Contains all proteins that are part of the experiment.
        Proteins []Protein `json:"proteins,omitempty"`
        // Contains all complexes that are part of the experiment.
        Complexes []Complex `json:"complexes,omitempty"`
        // Contains all reactants that are part of the experiment.
        Small_molecules []SmallMolecule `json:"small_molecules,omitempty"`
        // Dictionary mapping from reaction IDs to reaction-describing objects.
        Reactions []Reaction `json:"reactions,omitempty"`
        // Contains measurements that describe outcomes of an experiment.
        Measurements []Measurement `json:"measurements,omitempty"`
        // Contains ordinary differential equations that describe the kinetic
        // model.
        Equations []Equation `json:"equations,omitempty"`
        // List of parameters that are part of the equation
        Parameters []Parameter `json:"parameters,omitempty"`
}

// Creator The creator object contains all information about authors that
// contributed to the resulting document.
type Creator struct {
        // Given name of the author or contributor.
        Given_name string `json:"given_name"`
        // Family name of the author or contributor.
        Family_name string `json:"family_name"`
        // Email address of the author or contributor.
        Mail string `json:"mail"`
}

// Vessel This object describes vessels in which the experiment has been carried
// out. These can include any type of vessel used in biocatalytic
// experiments.
type Vessel struct {
        // Unique identifier of the vessel.
        Id string `json:"id"`
        // Name of the used vessel.
        Name string `json:"name"`
        // Volumetric value of the vessel.
        Volume float64 `json:"volume"`
        // Volumetric unit of the vessel.
        Unit UnitDefinition `json:"unit"`
        // Whether the volume of the vessel is constant or not.
        Constant bool `json:"constant"`
}

// Protein This object describes the proteins that were used or formed throughout
// the experiment.
type Protein struct {
        // Unique internal identifier of the protein.
        Id string `json:"id"`
        Name string `json:"name"`
        Constant bool `json:"constant"`
        // Amino acid sequence of the protein
        Sequence string `json:"sequence,omitempty"`
        // Unique identifier of the vessel this protein has been used in.
        Vessel_id string `json:"vessel_id,omitempty"`
        // EC number of the protein.
        Ecnumber string `json:"ecnumber,omitempty"`
        // Organism the protein was expressed in.
        Organism string `json:"organism,omitempty"`
        // Taxonomy identifier of the expression host.
        Organism_tax_id string `json:"organism_tax_id,omitempty"`
        // Array of references to publications, database entries, etc. that
        // describe the protein.
        References []string `json:"references,omitempty"`
}

// Complex This object describes complexes made of reactants and/or proteins that
// were used or produced in the course of the experiment.
type Complex struct {
        // Unique identifier of the complex.
        Id string `json:"id"`
        Name string `json:"name"`
        Constant bool `json:"constant"`
        // Unique identifier of the vessel this complex has been used in.
        Vessel_id string `json:"vessel_id,omitempty"`
        // Array of IDs the complex contains
        Participants []string `json:"participants,omitempty"`
}

// SmallMolecule This object describes the reactants that were used or produced in the
// course of the experiment.
type SmallMolecule struct {
        // Unique identifier of the small molecule.
        Id string `json:"id"`
        Name string `json:"name"`
        Constant bool `json:"constant"`
        // Unique identifier of the vessel this small molecule has been used in.
        Vessel_id string `json:"vessel_id,omitempty"`
        // Canonical Simplified Molecular-Input Line-Entry System (SMILES)
        // encoding of the reactant.
        Canonical_smiles string `json:"canonical_smiles,omitempty"`
        // International Chemical Identifier (InChI) encoding of the reactant.
        Inchi string `json:"inchi,omitempty"`
        // Hashed International Chemical Identifier (InChIKey) encoding of the
        // reactant.
        Inchikey string `json:"inchikey,omitempty"`
        // Array of references to publications, database entries, etc. that
        // describe the reactant.
        References []string `json:"references,omitempty"`
}

// Reaction This object describes a chemical or enzymatic reaction that was
// investigated in the course of the experiment. All species used
// within this object need to be part of the data model.
type Reaction struct {
        // Unique identifier of the reaction.
        Id string `json:"id"`
        // Name of the reaction.
        Name string `json:"name"`
        // Whether the reaction is reversible or irreversible
        Reversible bool `json:"reversible"`
        // Mathematical expression of the reaction.
        Kinetic_law Equation `json:"kinetic_law,omitempty"`
        // List of reaction elements that are part of the reaction.
        Species []ReactionElement `json:"species,omitempty"`
        // List of reaction elements that are not part of the reaction but
        // influence it.
        Modifiers []string `json:"modifiers,omitempty"`
}

// ReactionElement This object is part of the Reaction object and describes either an
// educt, product or modifier. The latter includes buffers, counter-
// ions as well as proteins/enzymes.
type ReactionElement struct {
        // Internal identifier to either a protein or reactant defined in the
        // EnzymeMLDocument.
        Species_id string `json:"species_id"`
        // Float number representing the associated stoichiometry.
        Stoichiometry float64 `json:"stoichiometry"`
}

// Equation This object describes an equation that can be used to model the
// kinetics of a reaction. There are different types of equations
// that can be used to model the kinetics of a reaction. The equation
// can be an ordinary differential equation, a rate law or assignment
// rule.
type Equation struct {
        // Mathematical expression of the equation.
        Equation string `json:"equation"`
        // Type of the equation.
        Equation_type EquationType `json:"equation_type"`
        // Internal identifier to a species defined in the EnzymeMLDocument,
        // given it is a rate equation.
        Species_id string `json:"species_id,omitempty"`
        // List of variables that are part of the equation
        Variables []Variable `json:"variables,omitempty"`
}

// Variable This object describes a variable that is part of an equation.
type Variable struct {
        // Unique identifier of the variable.
        Id string `json:"id"`
        // Name of the variable.
        Name string `json:"name"`
        // Symbol of the variable.
        Symbol string `json:"symbol"`
}

// Parameter This object describes the parameters of the kinetic model and can
// include all estimated values.
type Parameter struct {
        // Unique identifier of the parameter.
        Id string `json:"id"`
        // Name of the parameter.
        Name string `json:"name"`
        // Symbol of the parameter.
        Symbol string `json:"symbol"`
        // Numerical value of the estimated parameter.
        Value float64 `json:"value,omitempty"`
        // Unit of the estimated parameter.
        Unit UnitDefinition `json:"unit,omitempty"`
        // Initial value that was used for the parameter estimation.
        Initial_value float64 `json:"initial_value,omitempty"`
        // Upper bound of the estimated parameter.
        Upper float64 `json:"upper,omitempty"`
        // Lower bound of the estimated parameter.
        Lower float64 `json:"lower,omitempty"`
        // Standard error of the estimated parameter.
        Stderr float64 `json:"stderr,omitempty"`
        // Specifies if this parameter is constant
        Constant bool `json:"constant,omitempty"`
}

// Measurement This object describes the result of a measurement, which includes time
// course data of any type defined in DataTypes. It includes initial
// concentrations of all species used in a single measurement.
type Measurement struct {
        // Unique identifier of the measurement.
        Id string `json:"id"`
        // Name of the measurement
        Name string `json:"name"`
        // Measurement data of all species that were part of the measurement. A
        // species can refer to a protein, complex, or small molecule.
        Species_data []MeasurementData `json:"species_data,omitempty"`
        // User-defined group ID to signal relationships between measurements.
        Group_id string `json:"group_id,omitempty"`
        // PH value of the measurement.
        Ph float64 `json:"ph,omitempty"`
        // Temperature of the measurement.
        Temperature float64 `json:"temperature,omitempty"`
        // Unit of the temperature of the measurement.
        Temperature_unit UnitDefinition `json:"temperature_unit,omitempty"`
}

// MeasurementData This object describes a single entity of a measurement, which
// corresponds to one species. It also holds replicates that contain
// time course data.
type MeasurementData struct {
        // The identifier for the described reactant.
        Species_id string `json:"species_id"`
        // Initial amount of the measurement data. This must be the same as the
        // first data point in the array.
        Initial float64 `json:"initial"`
        // SI unit of the data that was measured.
        Data_unit UnitDefinition `json:"data_unit"`
        // Type of data that was measured (e.g. concentration)
        Data_type DataTypes `json:"data_type"`
        // Amount of the reactant before the measurement. This field should be
        // used for specifying the prepared amount of a species in
        // the reaction mix. Not to be confused with , specifying the
        // concentration at the first data point from the array.
        Prepared float64 `json:"prepared,omitempty"`
        // Data that was measured.
        Data []float64 `json:"data,omitempty"`
        // Time steps of the replicate.
        Time []float64 `json:"time,omitempty"`
        // Time unit of the replicate.
        Time_unit UnitDefinition `json:"time_unit,omitempty"`
        // Whether or not the data has been generated by simulation.
        Is_simulated bool `json:"is_simulated"`
}

// UnitDefinition Represents a unit definition that is based on the SI unit system.
type UnitDefinition struct {
        // Unique identifier of the unit definition.
        Id string `json:"id,omitempty"`
        // Common name of the unit definition.
        Name string `json:"name,omitempty"`
        // Base units that define the unit.
        Base_units []BaseUnit `json:"base_units,omitempty"`
}

// BaseUnit Represents a base unit in the unit definition.
type BaseUnit struct {
        // Kind of the base unit (e.g., meter, kilogram, second).
        Kind UnitType `json:"kind"`
        // Exponent of the base unit in the unit definition.
        Exponent int64 `json:"exponent"`
        // Multiplier of the base unit in the unit definition.
        Multiplier float64 `json:"multiplier,omitempty"`
        // Scale of the base unit in the unit definition.
        Scale float64 `json:"scale,omitempty"`
}

//
// Enum definitions
//
type EquationType string

const (
    EquationTypeASSIGNMENT EquationType = "assignment"
    EquationTypeINITIAL_ASSIGNMENT EquationType = "initialAssignment"
    EquationTypeODE EquationType = "ode"
    EquationTypeRATE_LAW EquationType = "rateLaw"
)
type DataTypes string

const (
    DataTypesABSORBANCE DataTypes = "http://purl.allotrope.org/ontologies/quality#AFQ_0000061"
    DataTypesCONCENTRATION DataTypes = "http://purl.obolibrary.org/obo/PATO_0000033"
    DataTypesCONVERSION DataTypes = "http://purl.allotrope.org/ontologies/quality#AFQ_0000226"
    DataTypesFLUORESCENCE DataTypes = "http://purl.obolibrary.org/obo/PATO_0000018"
    DataTypesPEAK_AREA DataTypes = "http://purl.allotrope.org/ontologies/result#AFR_0001073"
    DataTypesTRANSMITTANCE DataTypes = "http://purl.allotrope.org/ontologies/result#AFR_0002261"
)
type UnitType string

const (
    UnitTypeAMPERE UnitType = "ampere"
    UnitTypeAVOGADRO UnitType = "avogadro"
    UnitTypeBECQUEREL UnitType = "becquerel"
    UnitTypeCANDELA UnitType = "candela"
    UnitTypeCELSIUS UnitType = "celsius"
    UnitTypeCOULOMB UnitType = "coulomb"
    UnitTypeDIMENSIONLESS UnitType = "dimensionless"
    UnitTypeFARAD UnitType = "farad"
    UnitTypeGRAM UnitType = "gram"
    UnitTypeGRAY UnitType = "gray"
    UnitTypeHENRY UnitType = "henry"
    UnitTypeHERTZ UnitType = "hertz"
    UnitTypeITEM UnitType = "item"
    UnitTypeJOULE UnitType = "joule"
    UnitTypeKATAL UnitType = "katal"
    UnitTypeKELVIN UnitType = "kelvin"
    UnitTypeKILOGRAM UnitType = "kilogram"
    UnitTypeLITRE UnitType = "litre"
    UnitTypeLUMEN UnitType = "lumen"
    UnitTypeLUX UnitType = "lux"
    UnitTypeMETRE UnitType = "metre"
    UnitTypeMOLE UnitType = "mole"
    UnitTypeNEWTON UnitType = "newton"
    UnitTypeOHM UnitType = "ohm"
    UnitTypePASCAL UnitType = "pascal"
    UnitTypeRADIAN UnitType = "radian"
    UnitTypeSECOND UnitType = "second"
    UnitTypeSIEMENS UnitType = "siemens"
    UnitTypeSIEVERT UnitType = "sievert"
    UnitTypeSTERADIAN UnitType = "steradian"
    UnitTypeTESLA UnitType = "tesla"
    UnitTypeVOLT UnitType = "volt"
    UnitTypeWATT UnitType = "watt"
    UnitTypeWEBER UnitType = "weber"
)

//
// Type definitions for attributes with multiple types
//