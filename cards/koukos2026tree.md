---
arxiv_id: '2609.03480'
authors:
- Alkiviadis Koukos
- Spyros Kondylatos
- Thomas Nord-Larsen
- Lotte Nyborg
- Christian Tøttrup
- Kenneth Grogan
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.843
  dataset: Danish NFI pure test plots
  direction: worse
  id: koukos2026tree#c1
  label_ratio: null
  locator: Table 4 / Abstract
  metric: f1
  model: tessera
  span: The STF-based MLP achieves the highest classification performance, yielding
    macro F1 scores of 0.843 and 0.653
  span_sha256: 576d4b0765d385f66d53b06be04a04cf3ba937e64387fa8cadf3a7eb1c848933
  task: representation_probing
  value: 0.832
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.653
  dataset: Danish NFI mixed test plots
  direction: worse
  id: koukos2026tree#c2
  label_ratio: null
  locator: Table 5 / Sec 4.2
  metric: f1
  model: tessera
  span: '0.843

    0.653

    0.818

    0.631

    0.830

    0.644

    0.823

    0.637'
  span_sha256: e328a8d1377ede13f9e58f88a20649ee2b94a1bed44ba27d7d3dfeaec703c057
  task: representation_probing
  value: 0.603
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.743
  dataset: Danish NFI pure test plots (2022 only)
  direction: better
  id: koukos2026tree#c3
  label_ratio: null
  locator: Sec 5.1.3
  metric: f1
  model: tessera
  span: For 2022, TESSERA achieves an F1 score of 0.793 compared with 0.743 for STF
  span_sha256: f15abaa470669f697fd9b728107889d78cd546fff9d64e549fd5460a4eede5e9
  task: representation_probing
  value: 0.793
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.787
  dataset: Danish NFI pure test plots (2021-2022)
  direction: better
  id: koukos2026tree#c4
  label_ratio: null
  locator: Sec 5.1.3
  metric: f1
  model: tessera
  span: the corresponding scores are 0.809 and 0.787
  span_sha256: c06108a84db222ad75a2f4b418e8f51157463bc5763091f2c095042c3b9dbec8
  task: representation_probing
  value: 0.809
date: '2026-09-03'
doi: 10.48550/arxiv.2609.03480
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-17T00:07:03.578118Z'
key: koukos2026tree
limitations:
- benchmark_narrowness
- data_bias
- mixed_pixels
- spatial_transfer
- temporal_transfer
models:
- alphaearth
- tessera
proposed_tags:
- tree_species_classification
- national_forest_inventory
- spectral_temporal_features
- mixed_forest_stands
regions:
- dk
self_evaluation: false
tasks:
- representation_probing
title: 'Tree species mapping in Denmark: A comparison of spectral-temporal features
  with geospatial foundation model embeddings'
venue: arXiv
---

## summary

The paper maps dominant tree species across Denmark using National Forest Inventory plots, comparing manually engineered spectral-temporal features (STF) from Sentinel-1/2 against embeddings from the foundation models TESSERA and AlphaEarth. STF-based MLP achieved the best overall performance, but TESSERA was competitive and outperformed STF under limited training data and certain single-year configurations. The best STF model was used to produce Denmark's first open-access 10m national tree species map with 79.9% area-adjusted accuracy.

## setup

Reference labels come from 8,663 Danish NFI plots (2014-2022) aggregated into nine species groups, split into pure and mixed stands; models (RF, XGBoost, MLP) are trained on pure plots using STF (Sentinel-1/2 time series, spectral indices, canopy height) or FM embeddings (AlphaEarth, TESSERA, 2020-2022, concatenated with canopy height), and evaluated separately on held-out pure and mixed test plots via majority-vote pixel aggregation.

## caveats

Authors note optical/FM embeddings only capture upper-canopy signals and cannot resolve subcanopy structure or fine-scale heterogeneity in mixed stands; label noise arises from spatial mismatch between plot-level labels and pixels, especially for mixed plots; the random plot-level split does not enforce geographic separation, and temporal transfer beyond 2022 was not assessed.
