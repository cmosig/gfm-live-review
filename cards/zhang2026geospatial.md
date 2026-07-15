---
arxiv_id: '2605.01650'
authors:
- Wenbin Zhang
- Eimear Cleary
- Francisco Rowe
- Somnath Chaudhuri
- Maksym Bondarenko
- Shengjie Lai
- Andrew J. Tatem
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G7_interpretability
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.287
  dataset: Brazil districts
  direction: better
  id: zhang2026geospatial#c1
  label_ratio: null
  locator: Fig 2a / Results
  metric: r2
  model: geoclip
  span: 'random forest (median 0.430 [IQR: 0.375-0.490] versus 0.287 [0.247-0.392]
    for the geospatial covariates)'
  span_sha256: e5dec6c4bae5ae79cb56752f0ee0cbc9f80aea8ee1bca3a45dfbd5712fb2c5c9
  task: population_density
  value: 0.43
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.673
  dataset: US ZCTAs
  direction: better
  id: zhang2026geospatial#c2
  label_ratio: null
  locator: Fig 2a / Results
  metric: r2
  model: geoclip
  span: random forest (0.758 [0.751-0.766] versus 0.673 [0.662-0.680])
  span_sha256: 07807496663d9786a7b15367a44c5ae6b1fea319ca0257832ce1ac83f5340853
  task: population_density
  value: 0.758
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.132
  dataset: Nigeria LGAs
  direction: better
  id: zhang2026geospatial#c3
  label_ratio: null
  locator: Fig 2a / Results
  metric: r2
  model: geoclip
  span: random forest (0.188 [0.138-0.237] versus 0.132 [0.065-0.216])
  span_sha256: 2bfc049bce78bb8d627f039531cfaebe90122f9ce172efe0d7ff802a176bd5c5
  task: population_density
  value: 0.188
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.754
  dataset: US counties (aggregated)
  direction: worse
  id: zhang2026geospatial#c4
  label_ratio: null
  locator: Fig 5 / Sensitivity to spatial granularity
  metric: r2
  model: geoclip
  span: 'median R² of 0.754 (IQR: 0.549-0.876) compared with 0.658 (0.457-0.737) for
    PDFM'
  span_sha256: e9e3e7fa4d1dd8f48be43386e17cd58746301ee32454345ec045742fa5477769
  task: population_density
  value: 0.658
date: '2026-05-03'
doi: 10.48550/arxiv.2605.01650
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:38:02.716360Z'
key: zhang2026geospatial
limitations:
- spatial_transfer
- interpretability
- data_bias
- benchmark_narrowness
models: []
proposed_tags:
- PDFM
- population_dynamics_foundation_model
- geospatial_covariates
- KL_divergence
- place_embeddings
regions:
- br
- ng
- us
- global
self_evaluation: false
tasks:
- population_density
title: Geospatial foundation-model embeddings improve population estimation unevenly
  across space and scale
venue: arXiv
---

## summary



## setup



## caveats


