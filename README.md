

# EnzymeML Specifications

This repository contains all available schema definitions and programming APIs of the EnzymeML format.

EnzymeML is a data exchange format that supports the comprehensive documentation of enzymatic data by describing reaction conditions, time courses of substrate and product concentrations, the kinetic model, and the estimated kinetic constants. An EnzymeML document serves as a container for transferring data between experimental platforms, modeling tools, and databases. EnzymeML supports the scientific community by introducing a standardized data exchange format to make enzymatic data findable, accessible, interoperable, and reusable according to the FAIR data principles. It also supports the Systems Biology Markup Language, to which it can be converted.

Please refer to the [EnzymeML Website](enzymeml.org) for a detailed overview of EnzymeML and how to get started.

## EnzymeML Schemas
This repository contains the formal definition of an EnzymeML Document in the following schema definitions
- [`markdown`](specifications/v2.md)
- [`linkml`](schemes/v2/enzymeml-v2-linkml.yaml)
- [`graphql`](schemes/v2/enzymeml-v2.graphql)
- [`json-schema`](schemes/v2/enzymeml-v2.json),
- [`proto`](schemes/v2/enzymeml-v2.proto)
- [`shex`](schemes/v2/enzymeml-v2.shex)
- [`ttl`](schemes/v2/enzymeml-v2.ttl)
- [`xsd`](schemes/v2/enzymeml-v2.xsd)

## EnzymeML APIs
Besides schema definitions, EnzymeML-APIs in the following programming languages are available:
- [`Python` (pyenzyme)](https://github.com/EnzymeML/PyEnzyme)
- [`Rust` (enzymeml-rs)](https://github.com/EnzymeML/enzymeml-rs)
- [`GO` (enzymeml-go)](enzymeml-go)
- [`Julia` (enzymeml-jl)](enzymeml-jl)
- [`TypeScript` (enzymeml-ts)](enzymeml-ts)