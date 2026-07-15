---
arxiv_id: '2604.19591'
authors:
- Jienan Lyu
- Miao Yang
- Jinchen Cai
- Yiwen Hu
- Guanyi Lu
- Junhao Qiu
- Runmin Dong
axes:
- G11_complementarity
- G3_spatial_transfer
- G9_ecological_fine_scale
- G5_cost
claims:
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 39.08
  dataset: GID24 (4 m)
  direction: better
  id: lyu2026structure#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: alphaearth
  span: Baseline 75.29 39.08 48.87
  span_sha256: 67eeafa5162c61c94332993616e7db58f3957081db48ae85fc3f2fcbc3ac419d
  task: land_cover_classification
  value: 50.01
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 34.65
  dataset: GID24 (2 m)
  direction: better
  id: lyu2026structure#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: alphaearth
  span: 82.64 47.32 59.08
  span_sha256: 02f48ef4d72eb7b46bbba77d0e612022bd24dc9faae08661d54c0d8815eb9b17
  task: land_cover_classification
  value: 47.32
- axis: G11_complementarity
  baseline: alphaearth
  baseline_value: 50.01
  dataset: GID24 (4 m)
  direction: worse
  id: lyu2026structure#c3
  label_ratio: null
  locator: Table 4
  metric: miou
  model: tessera
  span: With TESSERA 84.57 49.38 61.30
  span_sha256: 48b48dd3b71be737e2c97ff335e11953e027e0ba549fb17f73502d09c995195d
  task: land_cover_classification
  value: 49.38
- axis: G5_cost
  baseline: task_specific
  baseline_value: 48.87
  dataset: GID24 (4 m)
  direction: better
  id: lyu2026structure#c4
  label_ratio: null
  locator: Table 1
  metric: miou
  model: alphaearth
  span: 84.24 48.87 60.73
  span_sha256: 9ef6260005382c4062c3544852f5b13a95ebde77a5562ae5e782fdcfd968256e
  task: land_cover_classification
  value: 50.01
date: '2026-04-21'
doi: 10.48550/arxiv.2604.19591
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:39:11.326785Z'
key: lyu2026structure
limitations:
- temporal_transfer
- mixed_pixels
- compute_cost
- benchmark_narrowness
models:
- alphaearth
- tessera
proposed_tags:
- structure_semantic_decoupled_modulation
- cross_modal_fusion
- AEF_embeddings
- ESD_embeddings
- Mask2Former
regions:
- cn
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
title: Structure-Semantic Decoupled Modulation of Global Geospatial Embeddings for
  High-Resolution Remote Sensing Mapping
venue: arXiv
---

## summary

The paper introduces SSDM, a framework that decouples global geospatial foundation model embeddings (e.g., AlphaEarth, TESSERA, ESD) into structural and semantic modulation pathways to improve high-resolution remote sensing semantic segmentation. SSDM injects structural priors as additive attention biases and semantic priors as residual mask-feature compensation, outperforming baselines and prior fusion methods (dual-encoder, SAM-based, DFormerv2) on the GID24 land-cover dataset. The method is shown to generalize across different global embedding sources and cross-resolution test sets with favorable computational efficiency.

## setup

Experiments use the GID24 24-class land-cover dataset (4m and 2m resolution subsets, 512x512 patches, 3000 train/1000 test) with a Mask2Former ResNet-50 backbone, fusing AlphaEarth Foundations (AEF) embeddings (10m) as the primary global representation, with additional generalization tests using TESSERA (10m) and ESD (30m) embeddings. Evaluation metrics are OA, mIoU, and mAcc.

## caveats

The authors note SSDM still struggles with categories exhibiting high intra-class variability, ambiguous boundaries, or small object scale (e.g., shrub forest, snow, square); structural modulation may cause oversmoothing on fine-grained details; there is an acknowledged temporal misalignment between 2015/2016 imagery and 2017 global embeddings; and the semantic branch remains limited in capturing subtle distinctions in highly ambiguous regions.
