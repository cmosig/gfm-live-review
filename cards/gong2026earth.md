---
arxiv_id: '2604.03456'
authors:
- Wenjing Gong
- Udbhav Srivastava
- Yuchen Wang
- Yuhao Jia
- Qifan Wu
- Weishan Bai
- Yifan Yang
- Xiao Huang
- Xinyue Ye
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G6_compactness
- G10_human_semantics
- G11_complementarity
claims:
- axis: G10_human_semantics
  baseline: prithvi
  baseline_value: 0.71
  dataset: ACS 5-year
  direction: better
  id: gong2026earth#c1
  label_ratio: null
  locator: Sec 2.1
  metric: r2
  model: alphaearth
  span: '%Drive Alone reaches 0.74 (AlphaEarth) and 0.71 (Prithvi)'
  span_sha256: 324778454e70e978190035d7373b6ecc18d6bb253049b1f0aad300a1a8734d3f
  task: urban_signal_mapping
  value: 0.74
- axis: G10_human_semantics
  baseline: prithvi
  baseline_value: 0.63
  dataset: ACS 5-year
  direction: better
  id: gong2026earth#c2
  label_ratio: null
  locator: Sec 2.1
  metric: r2
  model: alphaearth
  span: '%Transit shows the same ordering (0.72, 0.63, and 0.58)'
  span_sha256: a8ee887042f21191f2ab9d262cba7286f345ef6adbdd6f30c01068a4f13b7576
  task: urban_signal_mapping
  value: 0.72
- axis: G10_human_semantics
  baseline: null
  baseline_value: null
  dataset: ACS 5-year
  direction: parity
  id: gong2026earth#c3
  label_ratio: null
  locator: Sec 2.1
  metric: r2
  model: alphaearth
  span: '%Bike staying low across all three embeddings (0.16, 0.10, and 0.07)'
  span_sha256: 9458d9b0461596b8a17445ab0b0e1147d129ec1f3d829b2c9fd8f85ac7ebc6d0
  task: urban_signal_mapping
  value: 0.16
- axis: G10_human_semantics
  baseline: prithvi
  baseline_value: 0.31
  dataset: ACS 5-year
  direction: better
  id: gong2026earth#c4
  label_ratio: null
  locator: Sec 2.1
  metric: r2
  model: alphaearth
  span: Log-transformed median household income is only moderately captured (AlphaEarth,
    0.44; Prithvi, 0.31; Clay, 0.21)
  span_sha256: a27c0f8709f92c2abcc94b23b93f7389c612f8631c3cd9a41a3b13ee2f4b4391
  task: socioeconomic_estimation
  value: 0.44
- axis: G10_human_semantics
  baseline: prithvi
  baseline_value: 0.67
  dataset: CDC PLACES
  direction: better
  id: gong2026earth#c5
  label_ratio: null
  locator: Sec 2.1
  metric: r2
  model: alphaearth
  span: '%Obesity remaining high for both AlphaEarth and Prithvi (0.69 and 0.67, respectively)'
  span_sha256: be4c6cb7d0e16c51dc5a28986d72c0aa31079d2f1b498e51ac3e70859235c11e
  task: urban_signal_mapping
  value: 0.69
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: ACS 5-year
  direction: parity
  id: gong2026earth#c6
  label_ratio: null
  locator: Sec 2.2
  metric: r2
  model: alphaearth
  span: all three models cluster at low R2 (AlphaEarth ∼\sim 0.15, Clay ∼\sim 0.15)
  span_sha256: f86460f41bd55985f4f852fc03a18e1668017cd8704152f6ad32f3501db0561f
  task: urban_signal_mapping
  value: 0.15
- axis: G11_complementarity
  baseline: alphaearth
  baseline_value: 0.37
  dataset: city open-data crime records
  direction: better
  id: gong2026earth#c7
  label_ratio: null
  locator: Sec 2.2
  metric: r2
  model: clay
  span: predicting crime in Houston (R2 ∼\sim 0.55 for Clay vs. ∼\sim 0.37 for AlphaEarth)
  span_sha256: 3b43e5430cfed3d2503c6c6fb94179d5d8e71ad37340ed1cffb74b805cd3ec07
  task: urban_signal_mapping
  value: 0.55
date: '2026-04-03'
doi: null
doi_status: no_doi_found
extractor_version: '1'
ingested_at: '2026-07-12T16:37:30.914989Z'
key: gong2026earth
limitations:
- benchmark_narrowness
- spatial_transfer
- temporal_transfer
- human_semantics
- data_bias
- time_sensitivity
models:
- alphaearth
- prithvi
- clay
proposed_tags:
- urban_signal_prediction
- socioeconomic_prediction
- dimensionality_reduction
- modifiable_areal_unit_problem
- representation_efficiency
- commuting_mode_share
- crime_prediction
- health_burden_prediction
- census_block_group
- sdg_monitoring
regions:
- us
self_evaluation: false
tasks:
- urban_signal_mapping
- socioeconomic_estimation
- representation_probing
title: Earth Embeddings Reveal Diverse Urban Signals from Space
venue: arXiv
---

## summary

The authors benchmark three off-the-shelf Earth-embedding families (AlphaEarth, Prithvi, Clay) for predicting 14 neighborhood-level urban indicators across crime, income, health, and travel in six U.S. metropolitan areas from 2020 to 2023. Earth embeddings recover substantial urban variation, best for built-environment-coupled outcomes (chronic health, dominant commuting modes) and poorly for behavior-driven ones like cycling, with AlphaEarth most reliable. Performance is spatially heterogeneous across cities but temporally stable, and compact 64-d AlphaEarth embeddings are more information-dense than compressed Prithvi/Clay variants.

## setup

Embeddings (AlphaEarth 64-d, Prithvi-EO-2.0-300M 768-d, Clay-v1.5 1024-d) were aggregated to census block groups (or census tracts for health) and used as fixed features in a unified supervised pipeline (OLS, Random Forest, XGBoost, LightGBM) with 80/20 train-test splits and five-fold CV, reporting test R² under global, city-wise, year-wise, and city–year settings. Targets come from city crime open-data portals, ACS 5-year estimates, and CDC PLACES; dimensionality-reduction experiments (PCA, FA, kPCA, Isomap, random projection) compress Prithvi/Clay to 64-d.

## caveats

Authors flag limited geographic scope (six U.S. MSAs, no other countries), sensitivity to the modifiable areal unit problem from CBG/CT aggregation, and that ACS 5-year rolling estimates attenuate true year-to-year variation so annual labels are period rather than single-year snapshots. They note behavioral/policy-driven outcomes like cycling remain hard to infer, cross-city measurement differences may bias performance, and multi-modal fusion is needed.
