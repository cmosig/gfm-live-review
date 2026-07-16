---
arxiv_id: '2503.11849'
authors:
- Yi Wang
- Zhitong Xiong
- Chenying Liu
- Adam J. Stewart
- Thomas Dujardin
- Nikolaos Ioannis Bountos
- Angelos Zavras
- Franziska Gerken
- Ioannis Papoutsis
- Laura Leal-Taixé
- Xiao Xiang Zhu
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G9_ecological_fine_scale
- G12_openness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 64.2
  dataset: Cloud-S2
  direction: better
  id: wang2025towards#c1
  label_ratio: null
  locator: Table 4
  metric: miou
  model: dofa
  span: Cloud-S2
  span_sha256: b4a5e33c21999439dac9800bab3a01267febbebcf091707a4cdfd9fc6779331b
  task: semantic_segmentation
  value: 65.0
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 81.7
  dataset: EuroSAT-S1
  direction: parity
  id: wang2025towards#c2
  label_ratio: null
  locator: Table 4
  metric: accuracy
  model: dofa
  span: EuroSAT-S1
  span_sha256: d8e313b28e0db45dd3700a105cf741d246b736bbfdfd91dbf083cba397106c98
  task: land_cover_classification
  value: 81.7
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 97.6
  dataset: EuroSAT-S2
  direction: worse
  id: wang2025towards#c3
  label_ratio: null
  locator: Table 4
  metric: accuracy
  model: dofa
  span: EuroSAT-S2
  span_sha256: e6e6c36c635d4b16019c0642ea3870c06b2b0fd814528beb762b5fa7e1f1af8c
  task: land_cover_classification
  value: 97.2
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 71.5
  dataset: BigEarthNet-S1
  direction: worse
  id: wang2025towards#c4
  label_ratio: null
  locator: Table 4
  metric: auc
  model: dofa
  span: BigEarthNet-S1
  span_sha256: e47cefe2bbb5d89869ab8036ff3c9bc1f653209040465651863d9dff0ee76919
  task: land_cover_classification
  value: 70.5
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 80.1
  dataset: BigEarthNet-S2
  direction: worse
  id: wang2025towards#c5
  label_ratio: null
  locator: Table 4
  metric: auc
  model: dofa
  span: BigEarthNet-S2
  span_sha256: ac07d96dfb0042c6c054cf9e3e6f1810098026a597ede39879dd3adc4e702d54
  task: land_cover_classification
  value: 75.5
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 50.8
  dataset: DFC2020-S1
  direction: worse
  id: wang2025towards#c6
  label_ratio: null
  locator: Table 4
  metric: miou
  model: dofa
  span: DFC2020-S1
  span_sha256: e7af6ff35e3751a9a4a7e40d705e61ffa6a0b4d300d0348ed2c94a248cebc40e
  task: land_cover_classification
  value: 49.7
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 66.2
  dataset: DFC2020-S2
  direction: worse
  id: wang2025towards#c7
  label_ratio: null
  locator: Table 4
  metric: miou
  model: dofa
  span: DFC2020-S2
  span_sha256: a1f79703aee4ecb58187a4a8c7dc7cf7944002a38efd1478d79c914bb9149eb4
  task: land_cover_classification
  value: 61.8
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 78.3
  dataset: Flood-S1
  direction: worse
  id: wang2025towards#c8
  label_ratio: null
  locator: Table 4
  metric: miou
  model: dofa
  span: Flood-S1
  span_sha256: 7263db22109bd7a9dceee71bd942ac2f93f12cac4f3246172fb9b3cfb294086c
  task: flood_mapping
  value: 76.0
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 85.3
  dataset: LCZ-S2
  direction: worse
  id: wang2025towards#c9
  label_ratio: null
  locator: Table 4
  metric: accuracy
  model: dofa
  span: LCZ-S2
  span_sha256: 2a9b4377f4d7adbb78d540f7b47974b1a37e0a3c4059ab928d0796bea2650a05
  task: local_climate_zone_classification
  value: 83.0
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 68.3
  dataset: Biomass-S3
  direction: worse
  id: wang2025towards#c10
  label_ratio: null
  locator: Table 4
  metric: rmse
  model: dofa
  span: Biomass-S3
  span_sha256: 5a802bbad2e78140dd3e156dfc3cf9f86a87e1218560d841369a3addc316e2a2
  task: biomass_estimation
  value: 74.1
date: '2025-03-14'
doi: 10.48550/arxiv.2503.11849
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:11:54.118975Z'
key: wang2025towards
limitations:
- benchmark_narrowness
- compute_cost
- mixed_pixels
- data_bias
models:
- dofa
proposed_tags:
- multimodal_pretraining
- atmospheric_variables
- hypernetwork_patch_embedding
- climate_bridging
- sentinel_missions
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- crop_type_mapping
- flood_mapping
- biomass_estimation
- local_climate_zone_classification
title: Towards a Unified Copernicus Foundation Model for Earth Vision
venue: arXiv
---

## summary

The paper introduces Copernicus-Pretrain (18.7M images across all Sentinel missions), Copernicus-FM (a unified foundation model using sensor-aware hypernetworks and metadata Fourier encoding to handle any spectral/non-spectral modality), and Copernicus-Bench (15 hierarchical evaluation tasks spanning surface and atmospheric applications). Copernicus-FM is compared against DOFA and other foundation models plus supervised baselines across the benchmark.

## setup

Copernicus-FM (ViT-Base) is pretrained on 220K grid cells with all 8 Sentinel modalities via masked image modeling plus continual distillation from DINOv2/SoftCon, then evaluated with frozen-encoder linear probing/UPerNet decoding on the 15 Copernicus-Bench datasets against supervised baselines and other foundation models (SoftCon, CROMA, DOFA).

## caveats

Authors note S3/S5P images suffer from cloud and NaN filtering causing variable time series lengths, patch area does not strictly reflect true surface area due to geographic projection distortion, and DFC2020/LCZ datasets lack geolocation/time metadata limiting metadata-based evaluation.
