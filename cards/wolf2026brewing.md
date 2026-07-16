---
arxiv_id: '2602.19863'
authors:
- Filip Wolf
- Blaž Rolih
- Luka Čehovin Zajc
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: GEO-Bench+SpaceNetv1+Sen1Floods11+PASTIS (overall avg)
  direction: better
  id: wolf2026brewing#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: dofa
  span: with an average improvement of 3.64 percentage points in semantic segmentation
  span_sha256: 63cc71ebd01f127ec2bd118d1433773d8db235edfaa2ad1fa744d29c9ab50ce7
  task: semantic_segmentation
  value: 69.72
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: LEVIR + OSCD (avg)
  direction: better
  id: wolf2026brewing#c2
  label_ratio: null
  locator: Table 2
  metric: f1
  model: dofa
  span: 1.2 in change detection
  span_sha256: 63985960bce1fe5aa23818787f1e742d25759e57c461deec5a9b93288a3ad7d1
  task: change_detection
  value: 75.9
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: GB-ben+GB-s2s+GB-es (avg)
  direction: better
  id: wolf2026brewing#c3
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: dofa
  span: 1.31 in classification
  span_sha256: 1456d2b233fd428966d46166f760bd899ac6ff68e513edf1af2c4b43e5755400
  task: land_cover_classification
  value: 69.22
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: GB-SA-crop-type
  direction: better
  id: wolf2026brewing#c4
  label_ratio: 0.1
  locator: Table 7
  metric: miou
  model: dofa
  span: Results in a low-data regime (10%)
  span_sha256: 4fb0a32429b557d86d971e630f51bbae8057d311e5888d3715006c7d7d0a6805
  task: crop_type_mapping
  value: 28.98
date: '2026-02-23'
doi: 10.48550/arxiv.2602.19863
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:10:50.997905Z'
key: wolf2026brewing
limitations:
- compute_cost
- benchmark_narrowness
- data_bias
models:
- dofa
proposed_tags:
- dual_teacher_distillation
- contrastive_self_distillation
- DINOv3_distillation
- multispectral_pretraining
- Swin_transformer_backbone
- fMoW_Sentinel
- coding_rate_regularizer
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- change_detection
- crop_type_mapping
- flood_mapping
- land_cover_classification
title: 'Brewing Stronger Features: Dual-Teacher Distillation for Multispectral Earth
  Observation'
venue: arXiv
---

## summary



## setup



## caveats


