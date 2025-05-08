// Package database provides functionality for storing and retrieving EnzymeML documents
// and their components in a SQLite database using GORM as the ORM layer.
//
// The package centers around the DBManager type which handles all database operations
// including:
// - Creating and initializing the database schema
// - CRUD operations for EnzymeML documents and their nested components
// - Managing database connections and transactions
// - Handling relationships between different EnzymeML entities
package database

import (
	"fmt"
	"os"
	"path/filepath"

	"gorm.io/driver/sqlite"
	"gorm.io/gorm"
	"gorm.io/gorm/logger"

	enzymeml_v2 "enzymeml/src"
)

// DBManager handles database operations for EnzymeML documents.
// It encapsulates a GORM database connection and provides methods
// for interacting with EnzymeML data in a type-safe way.
type DBManager struct {
	db *gorm.DB
}

// NewDBManager creates a new database manager with the specified database file.
// It initializes the database connection and creates all necessary tables.
//
// Parameters:
//   - dbPath: Path to the SQLite database file
//   - models: Slice of model structs to be registered with GORM
//
// Returns:
//   - *DBManager: Initialized database manager
//   - error: Any error that occurred during initialization
func NewDBManager(dbPath string, models []interface{}) (*DBManager, error) {
	// Ensure directory exists
	dir := filepath.Dir(dbPath)
	if dir != "." && dir != "" {
		// Create directory if it doesn't exist (you might need to import "os" for this)
		os.MkdirAll(dir, 0755)
	}

	// Configure GORM
	config := &gorm.Config{
		Logger: logger.Default.LogMode(logger.Error),
	}

	// Connect to SQLite database
	db, err := gorm.Open(sqlite.Open(dbPath), config)
	if err != nil {
		return nil, fmt.Errorf("failed to connect to database: %w", err)
	}

	// Create a new manager
	manager := &DBManager{db: db}

	// Initialize database schema
	if err := manager.initSchema(models); err != nil {
		return nil, fmt.Errorf("failed to initialize database schema: %w", err)
	}

	return manager, nil
}

// initSchema creates all necessary tables for EnzymeML documents
func (m *DBManager) initSchema(models []interface{}) error {
	for _, model := range models {
		if err := m.db.AutoMigrate(model); err != nil {
			return fmt.Errorf("failed to migrate model %T: %w", model, err)
		}
	}
	return nil
}

// Close closes the database connection
func (m *DBManager) Close() error {
	sqlDB, err := m.db.DB()
	if err != nil {
		return fmt.Errorf("failed to get database connection: %w", err)
	}
	return sqlDB.Close()
}

// EnzymeML Document methods

// SaveEnzymeMLDocument stores a new EnzymeML document in the database
func (m *DBManager) SaveEnzymeMLDocument(doc *enzymeml_v2.EnzymeMLDocument) error {
	return m.db.Create(doc).Error
}

// GetEnzymeMLDocumentByID retrieves an EnzymeML document by its ID,
// including all nested relationships
func (m *DBManager) GetEnzymeMLDocumentByID(id uint) (*enzymeml_v2.EnzymeMLDocument, error) {
	var doc enzymeml_v2.EnzymeMLDocument
	if err := m.db.Preload("Creators").
		Preload("Vessels.Unit.BaseUnits").
		Preload("Proteins").
		Preload("Complexes").
		Preload("SmallMolecules").
		Preload("Reactions.KineticLaw.Variables").
		Preload("Reactions.Reactants").
		Preload("Reactions.Products").
		Preload("Measurements.SpeciesData.DataUnit.BaseUnits").
		Preload("Measurements.SpeciesData.TimeUnit.BaseUnits").
		Preload("Measurements.TemperatureUnit.BaseUnits").
		Preload("Equations.Variables").
		Preload("Parameters.Unit.BaseUnits").
		First(&doc, id).Error; err != nil {
		return nil, err
	}
	return &doc, nil
}

// GetAllEnzymeMLDocuments retrieves all EnzymeML documents from the database,
// including all nested relationships
func (m *DBManager) GetAllEnzymeMLDocuments() ([]enzymeml_v2.EnzymeMLDocument, error) {
	var docs []enzymeml_v2.EnzymeMLDocument
	if err := m.db.Preload("Creators").
		Preload("Vessels.Unit.BaseUnits").
		Preload("Proteins").
		Preload("Complexes").
		Preload("SmallMolecules").
		Preload("Reactions.KineticLaw.Variables").
		Preload("Reactions.Reactants").
		Preload("Reactions.Products").
		Preload("Measurements.SpeciesData.DataUnit.BaseUnits").
		Preload("Measurements.SpeciesData.TimeUnit.BaseUnits").
		Preload("Measurements.TemperatureUnit.BaseUnits").
		Preload("Equations.Variables").
		Preload("Parameters.Unit.BaseUnits").
		Find(&docs).Error; err != nil {
		return nil, err
	}
	return docs, nil
}

// GetEnzymeMLDocuments retrieves a limited number of EnzymeML documents,
// including all nested relationships
func (m *DBManager) GetEnzymeMLDocuments(limit int) ([]enzymeml_v2.EnzymeMLDocument, error) {
	var docs []enzymeml_v2.EnzymeMLDocument
	if err := m.db.Preload("Creators").
		Preload("Vessels.Unit.BaseUnits").
		Preload("Proteins").
		Preload("Complexes").
		Preload("SmallMolecules").
		Preload("Reactions.KineticLaw.Variables").
		Preload("Reactions.Reactants").
		Preload("Reactions.Products").
		Preload("Measurements.SpeciesData.DataUnit.BaseUnits").
		Preload("Measurements.SpeciesData.TimeUnit.BaseUnits").
		Preload("Measurements.TemperatureUnit.BaseUnits").
		Preload("Equations.Variables").
		Preload("Parameters.Unit.BaseUnits").
		Limit(limit).Find(&docs).Error; err != nil {
		return nil, err
	}
	return docs, nil
}

// Creator methods

// SaveCreator stores a new Creator in the database
func (m *DBManager) SaveCreator(creator *enzymeml_v2.Creator) error {
	return m.db.Create(creator).Error
}

// GetCreatorByID retrieves a Creator by its ID
func (m *DBManager) GetCreatorByID(id uint) (*enzymeml_v2.Creator, error) {
	var creator enzymeml_v2.Creator
	if err := m.db.First(&creator, id).Error; err != nil {
		return nil, err
	}
	return &creator, nil
}

// GetAllCreators retrieves all Creators from the database
func (m *DBManager) GetAllCreators() ([]enzymeml_v2.Creator, error) {
	var creators []enzymeml_v2.Creator
	if err := m.db.Find(&creators).Error; err != nil {
		return nil, err
	}
	return creators, nil
}

// GetCreators retrieves a limited number of Creators
func (m *DBManager) GetCreators(limit int) ([]enzymeml_v2.Creator, error) {
	var creators []enzymeml_v2.Creator
	if err := m.db.Limit(limit).Find(&creators).Error; err != nil {
		return nil, err
	}
	return creators, nil
}

// Vessel methods

// SaveVessel stores a new Vessel in the database
func (m *DBManager) SaveVessel(vessel *enzymeml_v2.Vessel) error {
	return m.db.Create(vessel).Error
}

// GetVesselByID retrieves a Vessel by its ID, including unit information
func (m *DBManager) GetVesselByID(id uint) (*enzymeml_v2.Vessel, error) {
	var vessel enzymeml_v2.Vessel
	if err := m.db.Preload("Unit.BaseUnits").First(&vessel, id).Error; err != nil {
		return nil, err
	}
	return &vessel, nil
}

// GetAllVessels retrieves all Vessels from the database, including unit information
func (m *DBManager) GetAllVessels() ([]enzymeml_v2.Vessel, error) {
	var vessels []enzymeml_v2.Vessel
	if err := m.db.Preload("Unit.BaseUnits").Find(&vessels).Error; err != nil {
		return nil, err
	}
	return vessels, nil
}

// GetVessels retrieves a limited number of Vessels, including unit information
func (m *DBManager) GetVessels(limit int) ([]enzymeml_v2.Vessel, error) {
	var vessels []enzymeml_v2.Vessel
	if err := m.db.Preload("Unit.BaseUnits").Limit(limit).Find(&vessels).Error; err != nil {
		return nil, err
	}
	return vessels, nil
}

// Protein methods

// SaveProtein stores a new Protein in the database
func (m *DBManager) SaveProtein(protein *enzymeml_v2.Protein) error {
	return m.db.Create(protein).Error
}

// GetProteinByID retrieves a Protein by its ID
func (m *DBManager) GetProteinByID(id uint) (*enzymeml_v2.Protein, error) {
	var protein enzymeml_v2.Protein
	if err := m.db.First(&protein, id).Error; err != nil {
		return nil, err
	}
	return &protein, nil
}

// GetAllProteins retrieves all Proteins from the database
func (m *DBManager) GetAllProteins() ([]enzymeml_v2.Protein, error) {
	var proteins []enzymeml_v2.Protein
	if err := m.db.Find(&proteins).Error; err != nil {
		return nil, err
	}
	return proteins, nil
}

// GetProteins retrieves a limited number of Proteins
func (m *DBManager) GetProteins(limit int) ([]enzymeml_v2.Protein, error) {
	var proteins []enzymeml_v2.Protein
	if err := m.db.Limit(limit).Find(&proteins).Error; err != nil {
		return nil, err
	}
	return proteins, nil
}

// Complex methods

// SaveComplex stores a new Complex in the database
func (m *DBManager) SaveComplex(complex *enzymeml_v2.Complex) error {
	return m.db.Create(complex).Error
}

// GetComplexByID retrieves a Complex by its ID
func (m *DBManager) GetComplexByID(id uint) (*enzymeml_v2.Complex, error) {
	var complex enzymeml_v2.Complex
	if err := m.db.First(&complex, id).Error; err != nil {
		return nil, err
	}
	return &complex, nil
}

// GetAllComplexes retrieves all Complexes from the database
func (m *DBManager) GetAllComplexes() ([]enzymeml_v2.Complex, error) {
	var complexes []enzymeml_v2.Complex
	if err := m.db.Find(&complexes).Error; err != nil {
		return nil, err
	}
	return complexes, nil
}

// GetComplexes retrieves a limited number of Complexes
func (m *DBManager) GetComplexes(limit int) ([]enzymeml_v2.Complex, error) {
	var complexes []enzymeml_v2.Complex
	if err := m.db.Limit(limit).Find(&complexes).Error; err != nil {
		return nil, err
	}
	return complexes, nil
}

// SmallMolecule methods

// SaveSmallMolecule stores a new SmallMolecule in the database
func (m *DBManager) SaveSmallMolecule(molecule *enzymeml_v2.SmallMolecule) error {
	return m.db.Create(molecule).Error
}

// GetSmallMoleculeByID retrieves a SmallMolecule by its ID
func (m *DBManager) GetSmallMoleculeByID(id uint) (*enzymeml_v2.SmallMolecule, error) {
	var molecule enzymeml_v2.SmallMolecule
	if err := m.db.First(&molecule, id).Error; err != nil {
		return nil, err
	}
	return &molecule, nil
}

// GetAllSmallMolecules retrieves all SmallMolecules from the database
func (m *DBManager) GetAllSmallMolecules() ([]enzymeml_v2.SmallMolecule, error) {
	var molecules []enzymeml_v2.SmallMolecule
	if err := m.db.Find(&molecules).Error; err != nil {
		return nil, err
	}
	return molecules, nil
}

// GetSmallMolecules retrieves a limited number of SmallMolecules
func (m *DBManager) GetSmallMolecules(limit int) ([]enzymeml_v2.SmallMolecule, error) {
	var molecules []enzymeml_v2.SmallMolecule
	if err := m.db.Limit(limit).Find(&molecules).Error; err != nil {
		return nil, err
	}
	return molecules, nil
}

// Reaction methods

// SaveReaction stores a new Reaction in the database
func (m *DBManager) SaveReaction(reaction *enzymeml_v2.Reaction) error {
	return m.db.Create(reaction).Error
}

// GetReactionByID retrieves a Reaction by its ID, including kinetic law and species information
func (m *DBManager) GetReactionByID(id uint) (*enzymeml_v2.Reaction, error) {
	var reaction enzymeml_v2.Reaction
	if err := m.db.Preload("KineticLaw.Variables").
		Preload("Reactants").
		Preload("Products").
		First(&reaction, id).Error; err != nil {
		return nil, err
	}
	return &reaction, nil
}

// GetAllReactions retrieves all Reactions from the database, including kinetic law and species information
func (m *DBManager) GetAllReactions() ([]enzymeml_v2.Reaction, error) {
	var reactions []enzymeml_v2.Reaction
	if err := m.db.Preload("KineticLaw.Variables").Preload("Species").Find(&reactions).Error; err != nil {
		return nil, err
	}
	return reactions, nil
}

// GetReactions retrieves a limited number of Reactions, including kinetic law and species information
func (m *DBManager) GetReactions(limit int) ([]enzymeml_v2.Reaction, error) {
	var reactions []enzymeml_v2.Reaction
	if err := m.db.Preload("KineticLaw.Variables").Preload("Species").Limit(limit).Find(&reactions).Error; err != nil {
		return nil, err
	}
	return reactions, nil
}

// Measurement methods

// SaveMeasurement stores a new Measurement in the database
func (m *DBManager) SaveMeasurement(measurement *enzymeml_v2.Measurement) error {
	return m.db.Create(measurement).Error
}

// GetMeasurementByID retrieves a Measurement by its ID, including all unit information
func (m *DBManager) GetMeasurementByID(id uint) (*enzymeml_v2.Measurement, error) {
	var measurement enzymeml_v2.Measurement
	if err := m.db.Preload("SpeciesData.DataUnit.BaseUnits").
		Preload("SpeciesData.TimeUnit.BaseUnits").
		Preload("TemperatureUnit.BaseUnits").
		First(&measurement, id).Error; err != nil {
		return nil, err
	}
	return &measurement, nil
}

// GetAllMeasurements retrieves all Measurements from the database, including all unit information
func (m *DBManager) GetAllMeasurements() ([]enzymeml_v2.Measurement, error) {
	var measurements []enzymeml_v2.Measurement
	if err := m.db.Preload("SpeciesData.DataUnit.BaseUnits").
		Preload("SpeciesData.TimeUnit.BaseUnits").
		Preload("TemperatureUnit.BaseUnits").
		Find(&measurements).Error; err != nil {
		return nil, err
	}
	return measurements, nil
}

// GetMeasurements retrieves a limited number of Measurements, including all unit information
func (m *DBManager) GetMeasurements(limit int) ([]enzymeml_v2.Measurement, error) {
	var measurements []enzymeml_v2.Measurement
	if err := m.db.Preload("SpeciesData.DataUnit.BaseUnits").
		Preload("SpeciesData.TimeUnit.BaseUnits").
		Preload("TemperatureUnit.BaseUnits").
		Limit(limit).Find(&measurements).Error; err != nil {
		return nil, err
	}
	return measurements, nil
}

// Equation methods

// SaveEquation stores a new Equation in the database
func (m *DBManager) SaveEquation(equation *enzymeml_v2.Equation) error {
	return m.db.Create(equation).Error
}

// GetEquationByID retrieves an Equation by its ID, including variables
func (m *DBManager) GetEquationByID(id uint) (*enzymeml_v2.Equation, error) {
	var equation enzymeml_v2.Equation
	if err := m.db.Preload("Variables").First(&equation, id).Error; err != nil {
		return nil, err
	}
	return &equation, nil
}

// GetAllEquations retrieves all Equations from the database, including variables
func (m *DBManager) GetAllEquations() ([]enzymeml_v2.Equation, error) {
	var equations []enzymeml_v2.Equation
	if err := m.db.Preload("Variables").Find(&equations).Error; err != nil {
		return nil, err
	}
	return equations, nil
}

// GetEquations retrieves a limited number of Equations, including variables
func (m *DBManager) GetEquations(limit int) ([]enzymeml_v2.Equation, error) {
	var equations []enzymeml_v2.Equation
	if err := m.db.Preload("Variables").Limit(limit).Find(&equations).Error; err != nil {
		return nil, err
	}
	return equations, nil
}

// Parameter methods

// SaveParameter stores a new Parameter in the database
func (m *DBManager) SaveParameter(parameter *enzymeml_v2.Parameter) error {
	return m.db.Create(parameter).Error
}

// GetParameterByID retrieves a Parameter by its ID, including unit information
func (m *DBManager) GetParameterByID(id uint) (*enzymeml_v2.Parameter, error) {
	var parameter enzymeml_v2.Parameter
	if err := m.db.Preload("Unit.BaseUnits").First(&parameter, id).Error; err != nil {
		return nil, err
	}
	return &parameter, nil
}

// GetAllParameters retrieves all Parameters from the database, including unit information
func (m *DBManager) GetAllParameters() ([]enzymeml_v2.Parameter, error) {
	var parameters []enzymeml_v2.Parameter
	if err := m.db.Preload("Unit.BaseUnits").Find(&parameters).Error; err != nil {
		return nil, err
	}
	return parameters, nil
}

// GetParameters retrieves a limited number of Parameters, including unit information
func (m *DBManager) GetParameters(limit int) ([]enzymeml_v2.Parameter, error) {
	var parameters []enzymeml_v2.Parameter
	if err := m.db.Preload("Unit.BaseUnits").Limit(limit).Find(&parameters).Error; err != nil {
		return nil, err
	}
	return parameters, nil
}
