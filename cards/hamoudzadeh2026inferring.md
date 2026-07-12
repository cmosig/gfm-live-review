---
arxiv_id: '2602.17250'
authors:
- Alireza Hamoudzadeh
- Valeria Belloni
- Roberta Ravanelli
axes:
- G3_spatial_transfer
- G9_ecological_fine_scale
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.38
  dataset: Nouvelle-Aquitaine IGN RGE ALTI DSM
  direction: better
  id: hamoudzadeh2026inferring#c1
  label_ratio: null
  locator: Table 4
  metric: r2
  model: alphaearth
  span: U-Net++ achieved the best results, with an R² of 0.84
  span_sha256: 54495dc2aee8cb45404f77a0cc511f17606d2502ba782133715bef6a7f93b7c2
  task: canopy_height_estimation
  value: 0.84
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 32.22
  dataset: Nouvelle-Aquitaine IGN RGE ALTI DSM
  direction: better
  id: hamoudzadeh2026inferring#c2
  label_ratio: null
  locator: Table 4
  metric: rmse
  model: alphaearth
  span: U-Net++ achieved the best performance, with an RMSE of approximately 16 m
    on the testing set
  span_sha256: d1b510f801edf89f5cedfdd832fefec88d06060a69f73f5cbfb06a88af1748fc
  task: canopy_height_estimation
  value: 16.42
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.38
  dataset: Nouvelle-Aquitaine IGN RGE ALTI DSM
  direction: better
  id: hamoudzadeh2026inferring#c3
  label_ratio: null
  locator: Table 4
  metric: r2
  model: alphaearth
  span: U-Net++ shows better generalization (R2=0.84R^{2}=0.84, median difference
    = -2.62 m) compared with the standard U-Net (R2=0.78R^{2}=0.78
  span_sha256: 4ce0f5f2470fd52eca7dc8e453439cc70dafcdee35c4d138c3ea8bb6c1487ef2
  task: canopy_height_estimation
  value: 0.78
- axis: G9_ecological_fine_scale
  baseline: alphaearth
  baseline_value: 16.1
  dataset: Danum Valley
  direction: better
  id: hamoudzadeh2026inferring#c4
  label_ratio: null
  locator: Sec 3
  metric: rmse
  model: tessera
  span: TESSERA, AlphaEarth, and Presto achieved Root Mean Square Error (RMSE) values
    of 12.2 m, 16.1 m, and 17.9 m
  span_sha256: 29a2a3e675b512540a89a2fbb1e8fb85e683a73ae468aac7c80678a9bf5fc81b
  task: canopy_height_estimation
  value: 12.2
- axis: G9_ecological_fine_scale
  baseline: tessera
  baseline_value: 12.2
  dataset: Danum Valley
  direction: worse
  id: hamoudzadeh2026inferring#c5
  label_ratio: null
  locator: Sec 6.5
  metric: rmse
  model: alphaearth
  span: Feng et al. (2025) reported an RMSE of 16.1 m for canopy height regression
    using AlphaEarth Embeddings
  span_sha256: 447c49f576579e59ce104d52f84ff9a8a9b39865deb5a22c4db17de446238624
  task: canopy_height_estimation
  value: 16.1
date: '2026-02-19'
doi: 10.48550/arxiv.2602.17250
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T16:36:27.401924Z'
key: hamoudzadeh2026inferring
limitations:
- spatial_transfer
- temporal_transfer
- data_bias
- benchmark_narrowness
models:
- alphaearth
- tessera
- presto
proposed_tags:
- surface_height_mapping
- dsm_regression
- digital_surface_model
- distribution_shift
- unet
- unet++
- ridge_regression_baseline
- earth_embeddings
- terrain_elevation
regions:
- fr
self_evaluation: false
tasks:
- canopy_height_estimation
- land_cover_classification
- crop_yield_estimation
- crop_type_mapping
- biomass_estimation
- hydrological_modeling
title: 'Inferring Height from Earth Embeddings: First insights using Google AlphaEarth'
venue: arXiv
---

## summary

The authors evaluate Google AlphaEarth Embeddings for regional surface height mapping by training lightweight U-Net and U-Net++ decoders to regress a high-quality DSM over Nouvelle-Aquitaine, France. Both architectures achieved strong training performance (R2=0.97), with U-Net++ generalizing better on the test set (R2=0.84, RMSE ~16 m) than U-Net (R2=0.78) and a Ridge regression baseline (R2=0.38). Results indicate the embeddings encode transferable topographic signals but suffer bias under height-distribution shift between train and test regions.

## setup

AlphaEarth Embeddings (2020, 10 m, 64 bands, uint8 version) served as inputs to U-Net/U-Net++ (ResNet-18 encoder) regression heads targeting the IGN RGE ALTI 5 m DSM resampled to 10 m over ~7865 km2 of Nouvelle-Aquitaine, France, split ~70% train/val and ~30% contiguous test. Models were trained with AdamW, MSE loss, 512x512 patches, and compared against a Ridge regression linear baseline using R2, Pearson/Spearman correlations, and height-difference statistics.

## caveats

The authors flag substantial performance degradation on the test set due to a shift in height frequency distribution between training and testing regions, elevated testing RMSE (~16 m) and residual bias, and a temporal mismatch between the IGN DSM (multi-year) and 2020 embeddings. They note the evaluation covers a single region and call for expanded, geographically distinct training data to assess transferability.
