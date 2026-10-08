---
title: Chromatographic data
description: From GC / HPLC exports to concentrations and an EnzymeML document.
---

:::note[Draft outline]
:::

## Typical raw data
- GC / HPLC exports (peak tables, chromatograms)
- One file per injection, many injections per time course

## Tool
- [Chromhandler](https://fairchemistry.github.io/Chromhandler/): reads chromatographic time-course data

## Steps
1. Put the instrument exports into `data/raw/`
2. Inspect: formats, peaks, retention times
3. Assign retention times to molecules
4. Calibrate: peak area → concentration
5. Compute: conversion, selectivity, rates
6. Plot and check
7. Export as EnzymeML

## Open questions
- Example dataset (GC or HPLC? which instrument vendor?)
