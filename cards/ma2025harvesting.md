---
arxiv_id: '2601.00857'
authors:
- Yuchi Ma
- Yawen Shen
- Anu Swatantran
- David B. Lobell
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G6_compactness
- G7_interpretability
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: USDA-NASS county-level yield
  direction: parity
  id: ma2025harvesting#c1
  label_ratio: null
  locator: Table 3
  metric: r2
  model: alphaearth
  span: achieving an R2 of around 0.80 for corn and soybean, and 0.70 for winter wheat
  span_sha256: d2847d66481410c8561b60b24a7468eba38bd785b958ecc3fc41cebda709e8c7
  task: crop_yield_estimation
  value: 0.8
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: USDA-NASS county-level yield (ETF/GP ecoregions)
  direction: worse
  id: ma2025harvesting#c2
  label_ratio: null
  locator: Table 6
  metric: r2
  model: alphaearth
  span: with R² values around -0.28–0.07
  span_sha256: 696ca94bb14ae62a88b74a4904e1110a7c782e0a89936830b27b2810357d9662
  task: crop_yield_estimation
  value: -0.28
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: USDA-NASS county-level yield (ETF/GP ecoregions)
  direction: worse
  id: ma2025harvesting#c3
  label_ratio: null
  locator: Table 6
  metric: r2
  model: alphaearth
  span: with R² values around 0.39–0.51
  span_sha256: 83e9682f9bfc7960502f041b837ce1692bbae8c1e2d8a1ababeb4422c0d64565
  task: crop_yield_estimation
  value: 0.39
date: '2025-12-30'
doi: 10.1016/j.jag.2026.105258
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T16:34:52.229566Z'
key: ma2025harvesting
limitations:
- spatial_transfer
- interpretability
- time_sensitivity
- temporal_transfer
- mixed_pixels
models:
- alphaearth
proposed_tags:
- tillage_mapping
- cover_crop_mapping
- agricultural_practice_mapping
- data_harmonization
- scale_transfer
- embedding_compression
- analysis_ready_embeddings
regions:
- us
- ar
self_evaluation: false
tasks:
- crop_yield_estimation
title: 'Harvesting AlphaEarth: Benchmarking the Geospatial Foundation Model for Agricultural
  Downstream Tasks'
venue: arXiv
---

## summary

This study benchmarks Google DeepMind's AlphaEarth Foundation (AEF) annual embeddings against traditional remote-sensing features on three U.S. agricultural tasks: crop yield prediction, tillage mapping, and cover crop mapping. AEF-based models are competitive with purpose-built RS models in local yield prediction and county-level tillage mapping, and require far less preprocessing. However, AEF shows limited spatial transferability, low interpretability, and limited time sensitivity.

## setup

County- and field-level labels for corn, soybean, and winter wheat yield (USDA-NASS and Corteva, 2017–2024), plus tillage and cover crop records, are paired with 64-dim AEF embeddings versus Landsat/ERA5/topographic RS features. RF and XGBoost models are trained and evaluated with State/County-Year CV, yearly CV, and scale- and space-transfer schemes (including U.S.-to-Argentina), reporting R2/RMSE and F1/accuracy.

## caveats

Authors flag AEF's limited spatial transferability (large geographic shifts causing failed cross-region/cross-country yield predictions), low interpretability (unlabeled bands A00–A63 with no physical meaning), temporal variability across years, and limited time sensitivity from annual-only embeddings that preclude in-season prediction; aggregating embeddings to county level also dilutes field-scale signal, hurting scale transfer.
