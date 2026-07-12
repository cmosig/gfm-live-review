---
arxiv_id: '2603.19873'
authors:
- Víctor Barreiro
- Johannes Jakubik
- Francisco Argüello
- Dora B. Heras
axes:
- G5_cost
- G6_compactness
- G1_label_rich_parity
claims:
- axis: G5_cost
  baseline: null
  baseline_value: 66.9
  dataset: MADOS
  direction: worse
  id: barreiro2026simpler#c1
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: SIMPLER (Ours) 64.57 64.57
  span_sha256: ecfd8cc7f3e408f222da996b1b2f636b8a0defc4ad4c460e072a9787f1d472c2
  task: semantic_segmentation
  value: 62.8
- axis: G6_compactness
  baseline: null
  baseline_value: 69.6
  dataset: MADOS
  direction: worse
  id: barreiro2026simpler#c2
  label_ratio: null
  locator: Sec 4.3
  metric: miou
  model: prithvi
  span: SIMPLER retains 89% of baseline (mIoU 62.2% vs 69.6%)
  span_sha256: 36dc3cdef643a390a4f3418d8771a3045ad071f2686253dc662a8fa4e847cc3a
  task: semantic_segmentation
  value: 62.2
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 73.4
  dataset: BigEarthNetv2
  direction: worse
  id: barreiro2026simpler#c3
  label_ratio: null
  locator: Sec 4.3
  metric: accuracy
  model: prithvi
  span: retaining 97% baseline mAP (71.2% vs 73.4%)
  span_sha256: ced8f1a35ec6a68c4476f337f7c77e0bb3815257a348aee99798b737f8dffe88
  task: land_cover_classification
  value: 71.2
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 66.6
  dataset: Sen4Map
  direction: worse
  id: barreiro2026simpler#c4
  label_ratio: null
  locator: Sec 4.3
  metric: f1
  model: prithvi
  span: retaining 96% baseline F1-macro (63.8% vs 66.6%)
  span_sha256: b096aab10f95dc78ff4ff89745f6fe17b81bb45ae96be16a15fe08ff0d98d8e1
  task: crop_type_mapping
  value: 63.8
date: '2026-03-20'
doi: 10.48550/arxiv.2603.19873
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:41:42.226955Z'
key: barreiro2026simpler
limitations:
- compute_cost
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- layer_pruning
- model_compression
- representation_similarity
- CKA
- architecture_selection
- TerraMind
- ViT-MAE
- LoRA
- SoftCon
- DINOv3-SAT
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- crop_type_mapping
- land_cover_classification
title: 'SIMPLER: Efficient Foundation Model Adaptation via Similarity-Guided Layer
  Pruning for Earth Observation'
venue: arXiv
---

## summary



## setup



## caveats


