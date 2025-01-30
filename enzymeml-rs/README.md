# EnzymeML Rust

Welcome to the Rust implementation of EnzymeML - a comprehensive data exchange format for enzymatic data. This package provides a robust Rust interface to work with EnzymeML documents, allowing you to describe reaction conditions, time courses, kinetic models, and more.

## Overview

EnzymeML Rust implements the complete EnzymeML v2 specification, enabling you to:
- Document enzymatic experiments in a standardized format
- Capture reaction conditions and measurements
- Define kinetic models and parameters
- Exchange data between experimental platforms and modeling tools
- Ensure FAIR (Findable, Accessible, Interoperable, Reusable) data principles

## Installation

To add EnzymeML Rust to your project, use:

```bash
cargo add enzymeml
```

## Usage

In this example, we create a new EnzymeML document and marshal it to JSON.

```rust
use enzymeml_rs::versions::v2::{Creator, EnzymeMLDocument};

fn main() {
    // Create a new EnzymeML document
    let doc = EnzymeMLDocument {
        name: "My Experiment".to_string(),
        created: Some("2024-01-01".to_string()),
        creators: Some(vec![
            Creator {
                given_name: "John".to_string(),
                family_name: "Doe".to_string(), 
                mail: "john.doe@example.com".to_string(),
                ..Default::default()
            }
        ]),
        ..Default::default()
    };

    // Marshal to JSON
    let json = serde_json::to_string_pretty(&doc).unwrap();
    println!("{}", json);

    // Unmarshal from JSON 
    let new_doc: EnzymeMLDocument = serde_json::from_str(&json).unwrap();
}
```
