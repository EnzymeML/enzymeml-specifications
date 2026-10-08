---
title: Home
description: EnzymeML is a standardized data format for catalytic reaction data.
template: splash
editUrl: false
hero:
  title: EnzymeML
  tagline: A standardized data exchange format for biocatalysis and enzymology.
  image:
    file: ../../assets/enzymeml.svg
    alt: EnzymeML logo
  actions:
    - text: Data Model
      link: /versions/v2/
      icon: right-arrow
    - text: Validate a document
      link: /validation/
      variant: minimal
---

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

<div class="grid-cards">

<div class="card">

[**Protein**](/versions/v2/#protein)

---

<img src="/img/protein.png" alt="Protein" width="12%" align="left" /> Contains information about the enzyme, such as its `sequence`, `EC number`, `organism`, and `taxonomy`.

</div>
<div class="card">

[**Small Molecule**](/versions/v2/#smallmolecule)

---

<img src="/img/smallmolecule.png" alt="Small Molecule" width="15%" align="left" /> Contains information about the small molecules involved in the reaction, such as their `canonical SMILES`, or `InChI`.

</div>
<div class="card">

[**Measurement**](/versions/v2/#measurement)

---

<img src="/img/measurement.png" alt="Measurement" width="15%" align="left" /> Contains the `measurement data` besides measurement conditions such as `temperature` and `pH`.

</div>
<div class="card">

[**Reaction**](/versions/v2/#reaction)

---

<img src="/img/reaction.png" alt="Reaction" width="17%" align="left" /> Contains information about the reaction, including the involved `species` (small molecules) and `modifiers`. Modifiers can be activating or inhibiting small molecules or proteins. It also specifies whether the reaction is `reversible` and provides the reaction equation.

</div>

</div>

For the full specification of an EnzymeML Document, refer to the [EnzymeML Data Model](/versions/v2/) or download it [here](https://github.com/EnzymeML/enzymeml-specifications/blob/main/specifications/v2.md).
