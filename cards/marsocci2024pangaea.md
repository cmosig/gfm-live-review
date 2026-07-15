---
arxiv_id: '2412.04204'
authors:
- Valerio Marsocci
- Yuru Jia
- Georges Le Bellier
- David Kerekes
- Liang Zeng
- Sebastian Hafner
- Sebastian Gerard
- Eric Brune
- Ritu Yadav
- Ali Shibli
- Heng Fang
- Yifang Ban
- Maarten Vergauwen
- Nicolas Audebert
- Andrea Nascetti
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G12_openness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 60.68
  dataset: Five Billion Pixels
  direction: better
  id: marsocci2024pangaea#c1
  label_ratio: 1.0
  locator: Table 5 / Table A8
  metric: miou
  model: scalemae
  span: reaching e.g. 67.19% mIoU on FBP
  span_sha256: 93e150569e8b2be34102679e35b7c2ca2034b5abb8ff6ef95a7431430eeceedc
  task: semantic_segmentation
  value: 67.19
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 62.09
  dataset: SpaceNet 7
  direction: better
  id: marsocci2024pangaea#c2
  label_ratio: 1.0
  locator: Table A15
  metric: miou
  model: scalemae
  span: 62.96% mIoU on SpaceNet 7
  span_sha256: 41a705228ea68510ff4fb5eedf06900eb63c97cdf885c0a63ca86b1a3f9055e3
  task: change_detection
  value: 62.96
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 35.67
  dataset: BioMassters
  direction: worse
  id: marsocci2024pangaea#c3
  label_ratio: 1.0
  locator: Sec 5.1
  metric: rmse
  model: croma
  span: 35.67 RMSE w.r.t. second best 36.11 RMSE with SpectralGPT
  span_sha256: bfb8b798d9fa184476ab7977ef8bf051c0d1baf52d92f1530078a499bc47d954
  task: biomass_estimation
  value: 36.81
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 91.42
  dataset: Sen1Floods11
  direction: worse
  id: marsocci2024pangaea#c4
  label_ratio: 1.0
  locator: Table 5
  metric: miou
  model: croma
  span: UNet achieves the best results on HLS Burn Scars (84.51 % mIoU), Sen1Floods11
    (91.42 % mIoU)
  span_sha256: 163d0b874720d53b5ab6ec5a23f23e2d0110449a140aaa7937882bfbc2e23e78
  task: flood_mapping
  value: 90.89
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 47.57
  dataset: Crop Type Mapping-SS
  direction: better
  id: marsocci2024pangaea#c5
  label_ratio: 1.0
  locator: Sec 5.1
  metric: miou
  model: croma
  span: CROMA reaches 67.55% mIoU on MADOS and 49.38% mIoU on Crop Type Mapping-SS
  span_sha256: f32ce3104b28f7e684aaf9d8f2efd8e1e15c1cd7044f4f35d567a8ee06296baa
  task: crop_type_mapping
  value: 49.38
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 46.08
  dataset: SpaceNet 7
  direction: worse
  id: marsocci2024pangaea#c6
  label_ratio: 0.1
  locator: Table A16
  metric: miou
  model: croma
  span: CROMA achieving a score of 6 in the 10% labeled data scenario
  span_sha256: 47e36a7fc00fca8ad52f195f691ba904cbf83b438d6b962cdba89625dd24997f
  task: change_detection
  value: 42.15
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 60.68
  dataset: Five Billion Pixels
  direction: worse
  id: marsocci2024pangaea#c7
  label_ratio: 1.0
  locator: Table A8
  metric: miou
  model: prithvi
  span: SpectralGPT, with an mIOU of 32.08% and m-f1 of 40.47%
  span_sha256: 4d19563b5ab5640c885e08c7f52fd0fda726ad2cca8b5965a17b3b7a62586ba5
  task: land_cover_classification
  value: 46.82
date: '2024-12-05'
doi: 10.48550/arxiv.2412.04204
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:51:46.254042Z'
key: marsocci2024pangaea
limitations:
- benchmark_narrowness
- spatial_transfer
- temporal_transfer
- data_bias
models:
- croma
- dofa
- prithvi
- scalemae
proposed_tags:
- multi-spectral
- SAR
- resolution_mismatch
- normalization_ablation
regions:
- global
- us
- fr
- ss
- cn
- fi
- vn
- kh
self_evaluation: false
tasks:
- semantic_segmentation
- change_detection
- biomass_estimation
- crop_type_mapping
- land_cover_classification
- flood_mapping
title: 'PANGAEA: A Global and Inclusive Benchmark for Geospatial Foundation Models'
venue: arXiv
---

## summary

PANGAEA is a standardized benchmark spanning 11 EO datasets across urban, agricultural, marine, forest, and disaster domains, evaluating GFMs on segmentation, change detection, and regression tasks under varying label availability. It finds GFMs do not consistently outperform supervised baselines (UNet, ViT), with performance strongly tied to alignment between pretraining and downstream data resolution/spectral characteristics.

## setup

11 datasets (HLS Burn Scars, MADOS, PASTIS-R, Sen1Floods11, xView2, Five Billion Pixels, DynamicEarthNet, Crop Type Mapping-SS, SpaceNet 7, AI4SmallFarms, BioMassters) evaluated with frozen GFM encoders plus a UPerNet decoder, fine-tuned under 10%/50%/100% label regimes, compared against UNet and ViT trained from scratch.

## caveats

Authors note GFMs struggle on low-resolution/multi-spectral tasks when pretrained on high-resolution RGB data, multi-temporal GFMs (Prithvi, SatlasNet) underperform uni-temporal models combined with L-TAE, multi-modal (SAR+optical) fusion generally underperforms optical alone, and object detection/classification tasks were excluded due to lack of consensus on evaluation protocol.
