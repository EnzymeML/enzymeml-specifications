---
template: home.html
---

![EnzymeML Logo](img/enzymeml.svg){ width="10%" }

## What is EnzymeML?

EnzymeML is a standardized data format for catalytic reaction data, designed to ensure consistency and interoperability. It enables researchers to store, share, and enrich reaction data with detailed metadata in JSON or XML formats. Tools for reading and writing EnzymeML simplify data handling and ensure reproducibility, paving the way for data-driven research in biocatalysis.


## Why EnzymeML?

🧩 **Standardization**  
  An EnzymeML Document is a standardized data format. It allows representing all data of a biocatalytic reaction in a consistent structure, independent of the experimental setup.

🔄 **Data Exchange**  
  EnzymeML facilitates the sharing of enzyme-catalyzed reaction data across scientists, tools, and databases, enabling collaborative research and integration of diverse datasets.

⚡ **Efficiency**  
  Standardization of data formats enables automation of data processing, minimizing manual steps, reducing errors, and saving time.

🌟 **FAIR Data**  
  EnzymeML makes data interoperable, constituting an important building block for making data FAIR.

🤖 **No data - no AI-party**  
  Structured data is the foundation for making your data compatible with machine learning.


## What comprises an EnzymeML Document?

An EnzymeML Document organizes and contextualizes data of a biocatalytic reaction. It integrates information about proteins, small molecules (e.g., substrates, products, inhibitors, activators), experimental conditions, and measurement data, providing a structured representation that links these elements seamlessly. The following elements are the key elements of an EnzymeML Document:

<div class="grid cards" markdown>

- [**Protein**](versions/v2.md#protein)

    ----

    ![Protein](img/protein.png){ width="12%", align=left }
    Contains information about the enzyme, such as its `sequence`, `EC number`, `organism`, and `taxonomy`.

- [**Small Molecule**](versions/v2.md#smallmolecule)

    ----

    ![Small Molecule](img/smallmolecule.png){ width="15%", align=left }
    Contains information about the small molecules involved in the reaction, such as their `canonical SMILES`, or `InChI`.

- [**Measurement**](versions/v2.md#measurement)

    ----

    ![Measurement](img/measurement.png){ width="15%", align=left }
    Contains the `measurement data` besides measurement conditions such as `temperature` and `pH`.

- [**Reaction**](versions/v2.md#reaction)

    ----

    ![Reaction](img/reaction.png){ width="17%", align=left }
    Contains information about the reaction, including the involved `species` (small molecules) and `modifiers`. Modifiers can be activating or inhibiting small molecules or proteins. It also specifies whether the reaction is `reversible` and provides the reaction equation.


</div>

For the full specification of an EnzymeML Document, refer to the [EnzymeML Data Model](versions/v2.md).


## How to use EnzymeML?

EnzymeML can be used in different ways, ranging from a desktop application to a set of native APIs:

### EnzymeML Suite

The EnzymeML Suite is a desktop application for creating, editing, and visualizing EnzymeML Documents. Via the sidebar, different elements of an EnzymeML Document can be added and edited.
![EnzymeML Suite](img/suite.png){ width="75%" }  
The EnzymeML Suite is available for Windows, macOS, and Linux and can be downloaded from [here](https://github.com/EnzymeML/enzymeml-suite/releases/tag/v0.0.1).


### Native APIs

EnzymeML provides native APIs in Python, TypeScript, Rust, and Go. These APIs allow to read and write EnzymeML Documents programmatically in different programming languages.

??? example "EnzymeML API Examples"

    === "`pyenzyme`"

        ```python
        from pyenzyme.v2 import (
            EnzymeMLDocument, Protein, SmallMolecule, 
            UnitDefinition, BaseUnit, UnitType
        )

        # Create a new EnzymeML document
        doc = EnzymeMLDocument(
            name="Example Document",
            created="2024-03-20",
            creators=[]
        )

        # Add an enzyme
        enzyme = doc.add_to_proteins(
            id="P13006",
            name="Glucose Oxidase",
            constant=True,
            sequence="MKLLLPVL...",  # Full sequence here
            ecnumber="1.1.3.4"
        )

        # Add glucose as substrate
        glucose = doc.add_to_small_molecules(
            id="50-99-7", 
            name="D-Glucose",
            constant=False,
            canonical_smiles="C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O"
        )
        ```

    === "`enzymeml-ts`"

        ```typescript
        import { 
            EnzymeMLDocument, Protein, SmallMolecule,
            UnitDefinition, BaseUnit, UnitType 
        } from 'enzymeml-ts';

        // Create a new EnzymeML document
        const doc: EnzymeMLDocument = {
            name: "Example Document",
            created: "2024-03-20",
            creators: [],
            proteins: [],
            small_molecules: [],
            references: []
        };

        // Add an enzyme
        const enzyme: Protein = {
            id: "P13006",
            name: "Glucose Oxidase",
            constant: true,
            sequence: "MKLLLPVL...", // Full sequence here
            ecnumber: "1.1.3.4"
        };
        doc.proteins.push(enzyme);

        // Add glucose as substrate
        const glucose: SmallMolecule = {
            id: "50-99-7",
            name: "D-Glucose",
            constant: false,
            canonical_smiles: "C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O"
        };
        doc.small_molecules.push(glucose);
        ```

    === "`enzymeml-rs`"

        ```rust
        use enzymeml::versions::v2::{
            EnzymeMLDocument, Protein, SmallMolecule,
            UnitDefinition, BaseUnit, UnitType
        };

        // Create a new EnzymeML document
        let mut doc = EnzymeMLDocument {
            name: String::from("Example Document"),
            created: Some(String::from("2024-03-20")),
            creators: None,
            proteins: Some(Vec::new()),
            small_molecules: Some(Vec::new()),
            references: None,
            ..Default::default()
        };

        // Add an enzyme
        let enzyme = Protein {
            id: String::from("P13006"),
            name: String::from("Glucose Oxidase"),
            constant: true,
            sequence: Some(String::from("MKLLLPVL...")), // Full sequence here
            ecnumber: Some(String::from("1.1.3.4")),
            ..Default::default()
        };
        doc.proteins.as_mut().unwrap().push(enzyme);

        // Add glucose as substrate
        let glucose = SmallMolecule {
            id: String::from("50-99-7"),
            name: String::from("D-Glucose"),
            constant: false,
            canonical_smiles: Some(String::from(
                "C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O"
            )),
            ..Default::default()
        };
        doc.small_molecules.as_mut().unwrap().push(glucose);
        ```

    === "`enzymeml-go`"

        ```go
        package main

        import "github.com/enzymeml/enzymeml-go"

        func main() {
            // Create a new EnzymeML document
            doc := enzymeml.EnzymeMLDocument{
                Name:    "Example Document",
                Created: "2024-03-20",
            }

            // Add an enzyme
            enzyme := enzymeml.Protein{
                Id:       "P13006",
                Name:     "Glucose Oxidase",
                Constant: true,
                Sequence: "MKLLLPVL...", // Full sequence here
                Ecnumber: "1.1.3.4",
            }
            doc.Proteins = append(doc.Proteins, enzyme)

            // Add glucose as substrate
            glucose := enzymeml.SmallMolecule{
                Id:              "50-99-7",
                Name:            "D-Glucose",
                Constant:        false,
                Canonical_smiles: "C([C@@H]1[C@H]([C@@H]([C@H](C(O1)O)O)O)O)O",
            }
            doc.Small_molecules = append(doc.Small_molecules, glucose)
        }
        ```


### Python tools

Besides the native APIs, Python tools for directly reading in and processing data from different analytical instruments are available.

#### 🔬 Photometric Data

The [MTPHandler](https://fairchemistry.github.io/MTPHandler/) Python library streamlines the processing of photometric data from plate readers. It enables reading, processing, and exporting data from a variety of plate reader formats, blank correction, and concentration calculation in a scalable way.

#### 🌈 Chromatographic Data

The [Chromatopy](https://fairchemistry.github.io/Chromatopy) Python library streamlines the processing of chromatographic time-course data. It enables reading, processing, and exporting data from a variety of chromatographic instruments, assignment of retention times to molecules, and concentration calculation in a scalable way.

#### 🧲 NMR Data

The [NMRPy](https://nmrpy.readthedocs.io/en/latest/) Python library streamlines the processing of NMR time-course data.

