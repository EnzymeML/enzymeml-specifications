// Example: Database Operations with EnzymeML Documents
//
// This example demonstrates how to:
// 1. Set up a SQLite database for EnzymeML documents
// 2. Create and store a sample EnzymeML document with:
//    - Creator information
//    - Reaction vessel specifications
//    - Proteins (enzymes)
//    - Small molecules (substrates and products)
//    - Reaction definitions
//    - Measurement conditions
// 3. Retrieve and export documents as JSON

package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"log"
	"os"

	enzymeml_v2 "enzymeml/src"
	database "enzymeml/src/database"
)

func main() {
	// Create a new database manager with all required model types
	dbManager, err := database.NewDBManager("enzymeml.db", []interface{}{
		&enzymeml_v2.EnzymeMLDocument{},
		&enzymeml_v2.Creator{},
		&enzymeml_v2.Vessel{},
		&enzymeml_v2.Protein{},
		&enzymeml_v2.Complex{},
		&enzymeml_v2.SmallMolecule{},
		&enzymeml_v2.Reaction{},
		&enzymeml_v2.ReactionElement{},
		&enzymeml_v2.Equation{},
		&enzymeml_v2.Variable{},
		&enzymeml_v2.Parameter{},
		&enzymeml_v2.Measurement{},
		&enzymeml_v2.MeasurementData{},
		&enzymeml_v2.UnitDefinition{},
		&enzymeml_v2.BaseUnit{},
	})
	if err != nil {
		log.Fatalf("Failed to create database manager: %v", err)
	}
	defer dbManager.Close()

	// Create and store an example EnzymeML document
	createExampleEnzymeMLDocument(dbManager)

	// Retrieve all documents from the database
	enzymeMLDocuments, err := dbManager.GetAllEnzymeMLDocuments()
	if err != nil {
		log.Fatalf("Failed to get enzymeMLDocuments: %v", err)
	}

	// Print and export documents as JSON files
	fmt.Println("EnzymeML Documents:")
	for _, eml := range enzymeMLDocuments {
		jsonBytes, err := json.MarshalIndent(eml, "", "    ")
		if err != nil {
			log.Printf("Failed to marshal document to JSON: %v", err)
			continue
		}
		fmt.Printf("%s\n", string(jsonBytes))

		// Save each document to a separate JSON file
		filename := fmt.Sprintf("enzymeml_doc_%d.json", eml.Id)
		prettyJSON := &bytes.Buffer{}
		if err := json.Indent(prettyJSON, jsonBytes, "", "    "); err != nil {
			log.Printf("Failed to format JSON: %v", err)
			continue
		}
		if err := os.WriteFile(filename, prettyJSON.Bytes(), 0644); err != nil {
			log.Printf("Failed to write document to file: %v", err)
			continue
		}
	}
}

// createExampleEnzymeMLDocument creates a sample EnzymeML document with
// typical experimental data and stores it in the database
func createExampleEnzymeMLDocument(dbManager *database.DBManager) {
	enzymeMLDocument := enzymeml_v2.EnzymeMLDocument{
		Name: "Example EnzymeML Document",
		// Add creator information
		Creators: []enzymeml_v2.Creator{
			{
				GivenName:  "John",
				FamilyName: "Doe",
				Mail:       "john.doe@example.com",
			},
		},
		// Define reaction vessel
		Vessels: []enzymeml_v2.Vessel{
			{
				Id:     "vessel1",
				Name:   "Reaction Vessel 1",
				Volume: 1.0,
				Unit: enzymeml_v2.UnitDefinition{
					Id:   "litre",
					Name: "litre",
					BaseUnits: []enzymeml_v2.BaseUnit{
						{
							Kind:       enzymeml_v2.LITRE,
							Exponent:   1,
							Multiplier: 1,
						},
					},
				},
			},
		},
		// Define enzyme
		Proteins: []enzymeml_v2.Protein{
			{
				Id:       "protein1",
				Name:     "Example Enzyme",
				Constant: false,
				VesselId: "vessel1",
				Ecnumber: "1.1.1.1",
			},
		},
		// Define substrates and products
		SmallMolecules: []enzymeml_v2.SmallMolecule{
			{
				Id:       "substrate1",
				Name:     "Example Substrate",
				Constant: false,
				VesselId: "vessel1",
			},
			{
				Id:       "product1",
				Name:     "Example Product",
				Constant: false,
				VesselId: "vessel1",
			},
		},
		// Define reaction with stoichiometry
		Reactions: []enzymeml_v2.Reaction{
			{
				Id:         "reaction1",
				Name:       "Example Reaction",
				Reversible: false,
				Reactants: []enzymeml_v2.ReactionElement{
					{
						SpeciesId:     "substrate1",
						Stoichiometry: 1,
					},
				},
				Products: []enzymeml_v2.ReactionElement{
					{
						SpeciesId:     "product1",
						Stoichiometry: 1,
					},
				},
				Modifiers: []string{"protein1"},
			},
		},
		// Define measurement conditions
		Measurements: []enzymeml_v2.Measurement{
			{
				Id:          "measurement1",
				Name:        "Example Measurement",
				Ph:          7.0,
				Temperature: 298.15,
				TemperatureUnit: enzymeml_v2.UnitDefinition{
					Id:   "kelvin",
					Name: "kelvin",
					BaseUnits: []enzymeml_v2.BaseUnit{
						{
							Kind:       enzymeml_v2.KELVIN,
							Exponent:   1,
							Multiplier: 1,
						},
					},
				},
			},
		},
	}

	if err := dbManager.SaveEnzymeMLDocument(&enzymeMLDocument); err != nil {
		log.Fatalf("Failed to save enzymeMLDocument: %v", err)
	}
}
