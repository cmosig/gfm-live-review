---
arxiv_id: '2603.07246'
authors:
- Erik Scheurer
- Rocco Sedona
- Stefan Kesselheim
- Gabriele Cavallaro
axes:
- G3_spatial_transfer
- G6_compactness
- G7_interpretability
- G11_complementarity
claims:
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: HLS (LEPA MRR eval)
  direction: worse
  id: scheurer2026lepa#c1
  label_ratio: null
  locator: Table I
  metric: accuracy
  model: prithvi
  span: Prithvi-EO-2.0-100M
  span_sha256: 840dcc1aecadedbc77477d3c1c052118126b3846b9e141fc3ac0710a6656d048
  task: representation_probing
  value: 0.2113
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: HLSBurnscars
  direction: parity
  id: scheurer2026lepa#c2
  label_ratio: null
  locator: Table II
  metric: miou
  model: prithvi
  span: Prithvi-EO-2.0-100M [30]
  span_sha256: ee4805a5e5fdfe89c3dbae29290ad3f72a57e63fb6c19a082c6dfd2358af7965
  task: semantic_segmentation
  value: 80.28
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: Sen1Floods11
  direction: parity
  id: scheurer2026lepa#c3
  label_ratio: null
  locator: Table II
  metric: miou
  model: prithvi
  span: Sen1Floods11
  span_sha256: 7d2baf15c8976f11bc43d53b43adda9e9fba6befd1e2f81a00d9ef0a687afb70
  task: flood_mapping
  value: 87.12
date: '2026-03-07'
doi: 10.48550/arxiv.2603.07246
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:41:56.163229Z'
key: scheurer2026lepa
limitations:
- benchmark_narrowness
- interpretability
- compute_cost
models:
- prithvi
proposed_tags:
- embedding_interpolation
- geometric_equivariance
- joint_embedding_predictive_architecture
- mean_reciprocal_rank
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- representation_probing
- flood_mapping
- crop_type_mapping
- land_cover_classification
- change_detection
title: 'LEPA: Learning Geometric Equivariance in Satellite Remote Sensing Data with
  a Predictive Architecture'
venue: arXiv
---

## summary



## setup



## caveats


