---
arxiv_id: '2507.07527'
authors:
- Joelle Hanna
- Linus Scheibenreif
- Damian Borth
axes:
- G2_label_scarce_efficiency
- G6_compactness
- G5_cost
- G11_complementarity
claims:
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 71.2
  dataset: ben-ge-8k
  direction: better
  id: hanna2025mapex#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: scalemae
  span: RGB 71.2 64.5 70.8 75.1 79.9 67.2 75.6
  span_sha256: af179373a340ce9c4b717b03f9bac19afce0c1c2a057546df2c9698353d0e982
  task: land_cover_classification
  value: 79.9
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 78.1
  dataset: SEN12-FLOOD
  direction: better
  id: hanna2025mapex#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: prithvi
  span: SAR 78.1 77.4 80.3 83.0 82.6 80.1 83.2
  span_sha256: c1caa024ccbcdd2a74d64c5de239d990cfce43576ebead39741c6f301077c5d0
  task: flood_mapping
  value: 83.2
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 56.3
  dataset: ben-ge-8k
  direction: better
  id: hanna2025mapex#c3
  label_ratio: null
  locator: Table 4
  metric: miou
  model: prithvi
  span: RGB 56.3 53.1 56.9
  span_sha256: 82af680c47ad8655c483b92e9316af151b716f4729b293a25b78ff26f0837847
  task: semantic_segmentation
  value: 56.9
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 32.1
  dataset: ben-ge-8k
  direction: better
  id: hanna2025mapex#c4
  label_ratio: null
  locator: Table 9
  metric: accuracy
  model: prithvi
  span: 10-shot 32.1 34.5 38.9 38.6
  span_sha256: 28c63f876fa7e85aa96959389675e229255a1f33515623deb80976f146e712d7
  task: land_cover_classification
  value: 38.6
- axis: G11_complementarity
  baseline: null
  baseline_value: null
  dataset: ben-ge-8k
  direction: parity
  id: hanna2025mapex#c5
  label_ratio: null
  locator: Table 10
  metric: accuracy
  model: prithvi
  span: RGB + SAR 74.8 70.8 74.7 67.2 80.2 72.9 79.9
  span_sha256: 67e910304ed476591bef58ffca7c2bd59bb59e789c0ff6a78f816ede5ea53240
  task: land_cover_classification
  value: 79.9
date: '2025-07-10'
doi: 10.48550/arxiv.2507.07527
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:02:20.165264Z'
key: hanna2025mapex
limitations:
- compute_cost
- benchmark_narrowness
models:
- satmae
- scalemae
proposed_tags:
- mixture_of_experts
- modality_pruning
- wildfire_detection
- multi_modal_pretraining
regions:
- global
- us
self_evaluation: false
tasks:
- land_cover_classification
- flood_mapping
- semantic_segmentation
title: 'MAPEX: Modality-Aware Pruning of Experts for Remote Sensing Foundation Models'
venue: arXiv
---

## summary



## setup



## caveats


