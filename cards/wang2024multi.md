---
arxiv_id: '2405.20462'
authors:
- Yi Wang
- Conrad M Albrecht
- Xiao Xiang Zhu
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G12_openness
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: BigEarthNet-10%
  direction: better
  id: wang2024multi#c1
  label_ratio: 0.1
  locator: Table I / Abstract
  metric: auc
  model: dofa
  span: our ResNet50/ViT-S achieve 84.8/85.0 linear probing mAP scores on BigEarthNet-10%
  span_sha256: f05c9e7eea919446821f668fa60e97ceab0c2a3f7820e0f4551a09b98d122312
  task: land_cover_classification
  value: 84.8
- axis: G3_spatial_transfer
  baseline: croma
  baseline_value: null
  dataset: fMoW-sentinel-10%
  direction: better
  id: wang2024multi#c2
  label_ratio: 0.1
  locator: Sec V-A1 / Table III
  metric: accuracy
  model: dofa
  span: 4.8% better than the current best model CROMA [29] in linear probing
  span_sha256: e16ea0e31d01a48f0dc494598e59a10b1276506dbc86135f4e15138f697781e3
  task: land_cover_classification
  value: 44.0
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 47.3
  dataset: DFC2020
  direction: better
  id: wang2024multi#c3
  label_ratio: null
  locator: Table IV
  metric: miou
  model: dofa
  span: our ResNet50 outperforms MoCo-v2 [55] by 3%
  span_sha256: 330a09d7b6363acab2cb385a3e5c6385b2b7bb30a5f3148f42090c744b351824
  task: semantic_segmentation
  value: 50.3
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: null
  dataset: BigEarthNet-SAR-10%
  direction: better
  id: wang2024multi#c4
  label_ratio: 0.1
  locator: Sec V-A2
  metric: auc
  model: dofa
  span: Our ViT-B sets a new record of 81.4% on BigEarthNet-SAR, 3.5% better than
    CROMA
  span_sha256: 6d6f8b6bab484345aea8973558b4c942ccc45324b36d6457b20d2250009b6e67
  task: land_cover_classification
  value: 81.4
date: '2024-05-30'
doi: 10.48550/arxiv.2405.20462
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:12:42.657316Z'
key: wang2024multi
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
models: []
proposed_tags:
- soft_contrastive_learning
- multi_label_pretraining
- continual_pretraining
- dynamic_world_labels
- siamese_masking
- SSL4EO-S12-ML
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- crop_type_mapping
- local_climate_zone_classification
- change_detection
- semantic_segmentation
- representation_probing
title: Multi-Label Guided Soft Contrastive Learning for Efficient Earth Observation
  Pretraining
venue: arXiv
---

## summary



## setup



## caveats


