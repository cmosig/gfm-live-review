---
arxiv_id: '2506.08780'
authors:
- Isaac Corley
- Lakshay Sharma
- Ruth Crasto
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G3_spatial_transfer
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 78.9
  dataset: EuroSAT-L
  direction: better
  id: corley2025landsat#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: presto
  span: '78.9'
  span_sha256: 2949e01aa33c27170eff6d7293b40522f8bfe27fd7918fbefe77df84983785f6
  task: land_cover_classification
  value: 83.4
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 74.1
  dataset: EuroSAT-L
  direction: better
  id: corley2025landsat#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: presto
  span: '74.1'
  span_sha256: 8c9caf44d93d8dcf24460e434007202cc3298905a421c5c954ad16121db0e465
  task: land_cover_classification
  value: 88.8
date: '2025-06-10'
doi: 10.48550/arxiv.2506.08780
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:48:00.911663Z'
key: corley2025landsat
limitations:
- benchmark_narrowness
- compute_cost
- spatial_transfer
models: []
proposed_tags:
- landsat
- ssl4eo-l
- moco_v2
- simclr
- eurosat-l
- bigearthnet-l
- lc100-l
- knn_probe
- linear_probe
- zonal_stats_baseline
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- crop_type_mapping
- representation_probing
title: 'Landsat-Bench: Datasets and Benchmarks for Landsat Foundation Models'
venue: arXiv
---

## summary



## setup



## caveats


