---
arxiv_id: '2403.02059'
authors:
- Benedikt Blumenstiel
- Viktoria Moor
- Romeo Kienzler
- Thomas Brunschwiler
axes:
- G1_label_rich_parity
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 89.31
  dataset: BigEarthNet-43
  direction: better
  id: blumenstiel2024multi#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: prithvi
  span: Prithvi processes six bands and achieves a mean Average Precision of 97.62%
    on BigEarthNet-43
  span_sha256: 2e5e11cc023f16f6bc818e38d7540ae35b7fb882ec4e7c02b02dc820912161b3
  task: representation_probing
  value: 97.62
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 38.92
  dataset: ForestNet-12
  direction: better
  id: blumenstiel2024multi#c2
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: prithvi
  span: 44.51% on ForestNet-12, outperforming other RGB-based models
  span_sha256: e583d71c7d9737f19bf4f6aff33fd5eb6f43808660e7b87f10920d489989f674
  task: representation_probing
  value: 44.51
- axis: G6_compactness
  baseline: null
  baseline_value: null
  dataset: BigEarthNet-43
  direction: worse
  id: blumenstiel2024multi#c3
  label_ratio: null
  locator: Sec 5
  metric: accuracy
  model: prithvi
  span: which is also represented by a 92.58 mAP
  span_sha256: 591a173fa44058076ac9b7779d63690747ca393f84c6254687de7ac214b1e428
  task: representation_probing
  value: 92.58
date: '2024-03-04'
doi: 10.48550/arxiv.2403.02059
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T22:37:38.767010Z'
key: blumenstiel2024multi
limitations:
- compute_cost
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- image_retrieval
- content_based_image_retrieval
- hash_compression
- vector_database
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: Multi-Spectral Remote Sensing Image Retrieval Using Geospatial Foundation Models
venue: arXiv
---

## summary



## setup



## caveats


