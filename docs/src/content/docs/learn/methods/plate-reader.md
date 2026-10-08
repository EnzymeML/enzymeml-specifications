---
title: Plate reader data
description: From plate reader exports to blank-corrected concentrations and an EnzymeML document.
---

:::note[Draft outline]
:::

## Typical raw data
- Plate reader exports (absorbance / fluorescence per well over time)
- Plate layout: which well holds what

## Tool
- [MTPHandler](https://fairchemistry.github.io/MTPHandler/): reads and processes plate reader data

## Steps
1. Put the instrument export and plate layout into `data/raw/`
2. Inspect: format, wells, time points
3. Describe the plate layout (samples, blanks, standards)
4. Blank correction
5. Signal → concentration (standard curve or extinction coefficient)
6. Plot and check
7. Export as EnzymeML

## Open questions
- Example dataset (which reader / vendor format?)
