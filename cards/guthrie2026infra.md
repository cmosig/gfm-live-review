---
arxiv_id: '2609.09482'
authors:
- Justin Guthrie
- Edward Oughton
- Konrad Wessels
- Matthew Rice
- Isaac Corley
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.392
  dataset: Infra-Bench CLS
  direction: better
  id: guthrie2026infra#c1
  label_ratio: 1.0
  locator: Table S9
  metric: f1
  model: prithvi
  span: Macro F1
  span_sha256: 25d5622a303ab91a681d3dd8ecbe542f7f84f9474b1685f6df7c325430c20b74
  task: urban_signal_mapping
  value: 0.531
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.392
  dataset: Infra-Bench CLS
  direction: worse
  id: guthrie2026infra#c2
  label_ratio: 1.0
  locator: Table S1
  metric: f1
  model: croma
  span: Macro F1
  span_sha256: 25d5622a303ab91a681d3dd8ecbe542f7f84f9474b1685f6df7c325430c20b74
  task: urban_signal_mapping
  value: 0.341
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.392
  dataset: Infra-Bench CLS
  direction: better
  id: guthrie2026infra#c3
  label_ratio: 0.3
  locator: Sec 4
  metric: f1
  model: prithvi
  span: Prithvi-EO-2.0, and OlmoEarth v1.1-Base, all at FT and 0.3× training data,
    also exceed the supervised baseline at 1.0×
  span_sha256: ae3b407b2a99b12045c1e885a364f6999b783275f7196fffcb37081aaeea93a9
  task: urban_signal_mapping
  value: 0.481
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.287
  dataset: Infra-Bench CLS
  direction: worse
  id: guthrie2026infra#c4
  label_ratio: 0.3
  locator: Table S8
  metric: f1
  model: croma
  span: Macro F1
  span_sha256: 25d5622a303ab91a681d3dd8ecbe542f7f84f9474b1685f6df7c325430c20b74
  task: urban_signal_mapping
  value: 0.28
date: '2026-09-08'
doi: 10.48550/arxiv.2609.09482
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-17T00:06:12.264259Z'
key: guthrie2026infra
limitations:
- benchmark_narrowness
- data_bias
- mixed_pixels
- compute_cost
models:
- croma
- prithvi
proposed_tags:
- critical_infrastructure_classification
- facility_scale_asset_classification
- linear_probing_vs_fine_tuning
- DINOv3
- SatlasPretrain
- OlmoEarth
- AlphaEarth Foundations
regions:
- global
self_evaluation: false
tasks:
- urban_signal_mapping
- land_cover_classification
title: 'Infra-Bench CLS: A Global, Open-Source Benchmark for Critical Infrastructure
  Classification with Earth Observation Foundation Models'
venue: arXiv
---

## summary



## setup



## caveats


