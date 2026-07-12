---
arxiv_id: '2603.16911'
authors:
- Ivan Felipe Benavides-Martinez
- Justin Guthrie
- Jhon Edwin Arias
- Yeison Alberto Garces-Gomez
- Angela Ines Guzman-Alvis
- Cristiam Victoriano Portilla-Cabrera
- Somnath Mondal
- Andrew J. Allyn
- Auroop R. Ganguly
axes:
- G7_interpretability
- G6_compactness
- G5_cost
claims:
- axis: G6_compactness
  baseline: null
  baseline_value: null
  dataset: ESA WorldCover 2020
  direction: parity
  id: benavidesmartinez2026what#c1
  label_ratio: null
  locator: Sec 3.1
  metric: accuracy
  model: alphaearth
  span: required to recover 98% of baseline classification performance varies substantially
  span_sha256: eb4b9a1932c123963a5d00833438f8348b7b09939e85c64763b4eeec1da9e681
  task: land_cover_classification
  value: 98.0
date: '2026-03-08'
doi: 10.48550/arxiv.2603.16911
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T16:42:07.839908Z'
key: benavidesmartinez2026what
limitations:
- interpretability
- spatial_transfer
- benchmark_narrowness
- mixed_pixels
- data_bias
- time_sensitivity
- human_semantics
- temporal_transfer
- uncertainty
models:
- alphaearth
proposed_tags:
- functional interpretability
- embedding dimension ablation
- specialist-generalist taxonomy
- MDI feature importance
- dimension pruning
- ecotone representation
- embedding redundancy
- hierarchical embedding structure
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- representation_probing
title: What on Earth is AlphaEarth? Hierarchical structure and functional interpretability
  for global land cover
venue: arXiv
---

## summary

The authors propose a functional interpretability framework that reverse-engineers the role of Google AlphaEarth Foundations (GAEF) 64-dimensional embeddings by characterizing each dimension's contribution to land cover discrimination. They find embedding dimensions form a hierarchical functional spectrum (specialist, low-, mid-, and high-generalist) and that 2 to 12 of the 64 dimensions suffice to recover 98% of baseline classification performance. This reveals substantial redundancy and a pathway to reduced computational cost.

## setup

Over 130,000 binary land-cover classification experiments (target class vs. all others) were run using ESA WorldCover 2020 labels and GAEF embeddings over globally sampled ROIs, with Random Forest, Gradient Boosting, XGBoost, and LightGBM, a 75/25 split, MDI-based feature importance, and progressive ablation over the top 1-30 dimensions to find each class's minimum subset at a 98% baseline-recovery threshold.

## caveats

The authors note importance measures depend on the ML algorithm and data distribution, the functional taxonomy is sensitive to the chosen 98% recovery threshold, the visualization simplifies a high-dimensional space, classification accuracy and dimension roles vary geographically (regional vs. global), and the proposed interpretations are not validated against specific physical variables.
