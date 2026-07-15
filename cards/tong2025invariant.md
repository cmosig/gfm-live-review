---
arxiv_id: '2509.03497'
authors:
- Xin-Yi Tong
- Sherrie Wang
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G1_label_rich_parity
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 73.34
  dataset: CropGlobe (FRA→USA)
  direction: worse
  id: tong2025invariant#c1
  label_ratio: null
  locator: Table 3/Sec 5.2
  metric: accuracy
  model: presto
  span: For example, in the USA →\rightarrow AUS setting, Presto achieves 45.1% and
    AlphaEarth achieves 46.3% OA
  span_sha256: 3d670bb6e58675885c5c9f90f6196ec4f4ff6ad0d8a426ae2d74d36dc8739faa
  task: crop_type_mapping
  value: 43.35
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 86.7
  dataset: CropGlobe (USA→AUS)
  direction: worse
  id: tong2025invariant#c2
  label_ratio: null
  locator: Sec 5.2
  metric: accuracy
  model: presto
  span: Presto achieves 45.1% and AlphaEarth achieves 46.3% OA, whereas CropNet reaches
    86.7%
  span_sha256: 43bea450f59094cb85819ed5eea2ec38d485b485f4ea515f4ca872eeb26368b3
  task: crop_type_mapping
  value: 45.1
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 86.7
  dataset: CropGlobe (USA→AUS)
  direction: worse
  id: tong2025invariant#c3
  label_ratio: null
  locator: Sec 5.2
  metric: accuracy
  model: alphaearth
  span: Presto achieves 45.1% and AlphaEarth achieves 46.3% OA, whereas CropNet reaches
    86.7%
  span_sha256: 43bea450f59094cb85819ed5eea2ec38d485b485f4ea515f4ca872eeb26368b3
  task: crop_type_mapping
  value: 46.3
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 92.71
  dataset: CropGlobe USA (2023→2020)
  direction: better
  id: tong2025invariant#c4
  label_ratio: null
  locator: Table 11
  metric: accuracy
  model: alphaearth
  span: 'AlphaEarth_RF

    95.52 ±\pm 0.04

    96.03 ±\pm 0.05

    96.37 ±\pm 0.03

    96.81 ±\pm 0.03'
  span_sha256: 7313d35538df8e9786ed800261953289c8801bd9c4e8997f857598e8289ee05c
  task: crop_type_mapping
  value: 96.37
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 90.85
  dataset: CropGlobe USA (2023→2017)
  direction: worse
  id: tong2025invariant#c5
  label_ratio: null
  locator: Table 11
  metric: accuracy
  model: presto
  span: 'Presto_RF

    85.39 ±\pm 0.08

    85.66 ±\pm 0.09

    87.68 ±\pm 0.06

    88.31 ±\pm 0.06'
  span_sha256: e5a1dd9d5a4c0949a24ea395f723c687f890cf9457ca39eb1f25829883688b89
  task: crop_type_mapping
  value: 85.39
date: '2025-09-03'
doi: 10.48550/arxiv.2509.03497
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:47:03.918786Z'
key: tong2025invariant
limitations:
- spatial_transfer
- temporal_transfer
- benchmark_narrowness
- data_bias
models:
- presto
- alphaearth
proposed_tags:
- CropGlobe
- CropNet
- spectral_temporal_convolution
- data_augmentation
- harmonic_features
- temporal_median_features
regions:
- ar
- au
- be
- cn
- fr
- gb
- nl
- us
- global
self_evaluation: false
tasks:
- crop_type_mapping
title: Invariant Features for Global Crop Type Classification
venue: arXiv
---

## summary

The paper introduces CropGlobe, a global crop-type classification benchmark spanning eight countries, and CropNet, a lightweight spectral-temporal CNN that outperforms both handcrafted features and geospatial foundation model embeddings (Presto, AlphaEarth) under geographic domain shift. It finds that inductive bias toward joint spectral-temporal structure matters more for transfer than model scale or pretraining.

## setup

Evaluation uses CropGlobe, 300k Sentinel-2 pixel-level samples with 2023 crop labels from ARG, AUS, BEL, CHN, FRA, GBR, NLD, and USA, under cross-country, cross-continent, and cross-hemisphere transfer settings (train on source country, test on target with no target labels). Presto and AlphaEarth embeddings are compared against harmonic features, temporal median features, and CropNet using RF/MLP classifiers, reporting OA and mean F1.

## caveats

Authors note GFM embeddings are not necessarily aligned to crop phenology and show limited spatial/temporal transfer stability in agricultural tasks; performance for all methods degrades with increasing domain shift (cross-country to cross-hemisphere); category alignment across differing national labeling schemes and reliance on public reference products of varying quality are acknowledged limitations, along with CropGlobe's yield range not covering the low-yield conditions common in food-insecure regions like sub-Saharan Africa.
