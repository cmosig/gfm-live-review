---
arxiv_id: '2609.11689'
authors:
- Nathaniel Hendrix
- Carl Y. Zhang
- Chris Heitzig
- Andrew Bazemore
- David H. Rehkopf
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G6_compactness
- G7_interpretability
- G10_human_semantics
- G11_complementarity
- G12_openness
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: American Community Survey (owner/renter occupancy)
  direction: parity
  id: hendrix2026geospatial#c1
  label_ratio: null
  locator: Results - Prediction of ACS Variables
  metric: r2
  model: alphaearth
  span: percent of houses that were owner- or renter-occupied
  span_sha256: 895fea35130554261148345d37adab1ac62a4e78e1e2280125c476b8ebf9a5df
  task: socioeconomic_estimation
  value: 0.513
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.31
  dataset: CDC PLACES (mean across 40 outcomes, residual after social risk indices)
  direction: better
  id: hendrix2026geospatial#c2
  label_ratio: null
  locator: Abstract
  metric: r2
  model: alphaearth
  span: increased from 0.31 in the smallest tract-size decile to 0.39 in the largest
  span_sha256: 6846462934424ea69dde2fc7c65d66d94b34c41d25e0d25456f9ac87a6067c86
  task: socioeconomic_estimation
  value: 0.39
date: '2026-09-10'
doi: 10.48550/arxiv.2609.11689
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-17T00:15:29.448859Z'
key: hendrix2026geospatial
limitations:
- benchmark_narrowness
- human_semantics
- interpretability
- compute_cost
- time_sensitivity
- spatial_transfer
models:
- alphaearth
- prithvi
- clay
proposed_tags:
- OlmoEarth
- census_tract_embeddings
- social_risk_index
- CDC_PLACES
- area_deprivation_index
- residual_variance_analysis
regions:
- us
self_evaluation: false
tasks:
- socioeconomic_estimation
- urban_signal_mapping
title: Geospatial Foundation Models Capture Health-Relevant Dimensions of Place Beyond
  Conventional Social Risk Indices
venue: arXiv
---

## summary



## setup



## caveats


