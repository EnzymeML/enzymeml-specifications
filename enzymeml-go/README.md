# EnzymeML Go

Welcome to the Go implementation of EnzymeML - a comprehensive data exchange format for enzymatic data. This package provides a robust Go interface to work with EnzymeML documents, allowing you to describe reaction conditions, time courses, kinetic models, and more.

## Overview

EnzymeML Go implements the complete EnzymeML v2 specification, enabling you to:

- Document enzymatic experiments in a standardized format
- Capture reaction conditions and measurements
- Define kinetic models and parameters
- Exchange data between experimental platforms and modeling tools
- Ensure FAIR (Findable, Accessible, Interoperable, Reusable) data principles

## Installation

To add EnzymeML Go to your project, use:

```bash
go get github.com/enzymeml/enzymeml-specifications/enzymeml-go
```

## Usage

In this example, we create a new EnzymeML document and marshal it to JSON.

```go
package main

import (
    enzymeml_v2 "github.com/enzymeml/enzymeml-specifications/enzymeml-go"
)

func main() {
    // Create a new EnzymeML document
    doc := enzymeml_v2.EnzymeMLDocument{
        Name: "My Experiment",
        Created: "2024-01-01",
        Creators: []enzymeml_v2.Creator{
            {
                Given_name:  "John",
                Family_name: "Doe", 
                Mail:        "john.doe@example.com",
            },
        },
    }

    // Marshal to JSON
    jsonData, err := json.Marshal(doc)
    if err != nil {
        panic(err)
    }

    // Unmarshal from JSON
    var newDoc enzymeml_v2.EnzymeMLDocument
    err = json.Unmarshal(jsonData, &newDoc)
    if err != nil {
        panic(err)
    }
}
```
