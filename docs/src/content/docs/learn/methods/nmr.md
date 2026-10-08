---
title: NMR data
description: From raw NMR spectra to time courses and an EnzymeML document.
---

:::note[Draft outline]
:::

## Typical raw data
- Raw spectrometer output (e.g. Bruker, Varian), arrayed time-course spectra

## Tool
- [NMRPy](https://nmrpy.readthedocs.io/en/latest/): processes NMR time-course data

## Steps
1. Put the raw spectrometer output into `data/raw/`
2. Process: Fourier transform, phase and baseline correction
3. Pick and assign peaks to species
4. Deconvolute and integrate
5. Integrals → concentrations
6. Plot and check
7. Export as EnzymeML

## Open questions
- Example dataset (which spectrometer?)
