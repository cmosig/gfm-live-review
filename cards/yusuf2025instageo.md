---
arxiv_id: '2510.05617'
authors:
- Ibrahim Salihu Yusuf
- Iffanice Houndayi
- Rym Oualha
- Mohamed Aziz Cherif
- Kobby Panford-Quainoo
- Arnu Pretorius
axes:
- G5_cost
- G6_compactness
- G1_label_rich_parity
claims:
- axis: G1_label_rich_parity
  baseline: prithvi
  baseline_value: 88.3
  dataset: Sentinel-2 flood mapping (replica)
  direction: worse
  id: yusuf2025instageo#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: InstaGeo-Replica (S2)
  span_sha256: 08dcefdcd08da349739e989736777e47072739ab673cb5671608d801b42f1d2d
  task: flood_mapping
  value: 87.8
- axis: G1_label_rich_parity
  baseline: prithvi
  baseline_value: 42.7
  dataset: Multi-Temporal Crop Segmentation (US) replica
  direction: better
  id: yusuf2025instageo#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: InstaGeo-Replica
  span_sha256: 5cf3426166f197699bf32849eb155f9e1ede6d9cab05e6d3f97f0778c00345b6
  task: crop_type_mapping
  value: 47.87
- axis: G6_compactness
  baseline: prithvi
  baseline_value: 85.4
  dataset: Flood Mapping (HLS)
  direction: worse
  id: yusuf2025instageo#c3
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: Task‑specific (student)
  span_sha256: 3ded6d5d20555ebb397b50748537b7962ababa2b44b7225913a35c196f2841e7
  task: flood_mapping
  value: 84.99
- axis: G6_compactness
  baseline: prithvi
  baseline_value: 55.1
  dataset: Multi-Temporal Crop Segmentation (US)
  direction: worse
  id: yusuf2025instageo#c4
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: Vanilla FT
  span_sha256: 6dc05a1b958af9279630fc966c8c8d3be9208e825c927caf1605b8bca33d1b85
  task: crop_type_mapping
  value: 54.21
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 48.6
  dataset: Expanded 2022 CDL
  direction: better
  id: yusuf2025instageo#c5
  label_ratio: null
  locator: Table 3
  metric: miou
  model: prithvi
  span: achieving a new state-of-the-art mIoU of 60.65
  span_sha256: 02917443a599a21ed72ea8f4df6a62e0f25bd3e4481bbdb4852a0983c24b1e5b
  task: crop_type_mapping
  value: 60.65
date: '2025-10-07'
doi: 10.48550/arxiv.2510.05617
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:45:47.671707Z'
key: yusuf2025instageo
limitations:
- compute_cost
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- desert_locust_breeding_ground_prediction
- task_specific_distillation
- data_pipeline_reproducibility
- knowledge_distillation
regions:
- global
self_evaluation: false
tasks:
- flood_mapping
- crop_type_mapping
title: 'InstaGeo: Compute-Efficient Geospatial Machine Learning from Data to Deployment'
venue: arXiv
---

## summary

InstaGeo is an end-to-end open-source geospatial ML framework combining a data pipeline for converting raw satellite imagery into model-ready chips, task-specific distillation to compress fine-tuned GFMs, and a web-map deployment application. Using Prithvi GFMs, the authors reproduce three published benchmarks (flood mapping, crop segmentation, locust breeding prediction) within a few percentage points mIoU, achieve up to 8x model compression via distillation with minimal accuracy loss, and establish a new state-of-the-art crop segmentation benchmark using an expanded dataset.

## setup

Experiments use HLS/Sentinel-2 imagery and Prithvi-V1-100M and Prithvi-V2-300M GFMs fine-tuned on flood mapping, multi-temporal crop segmentation (US CDL 2022/2024), and desert locust breeding ground prediction datasets, comparing vanilla fine-tuning against task-specific distilled student models across mIoU, accuracy, F1, and ROC-AUC.

## caveats

The authors note the HLS-derived flood mapping replica trails the original by ~3pp mIoU due to spectral adjustments in HLS preprocessing versus native Sentinel-2, and that the 2024 CDL variant's smaller mIoU gain (vs 2022) likely stems from a revised 10m-to-30m downsampled label generation pipeline with different compositing and sampling strategies.
