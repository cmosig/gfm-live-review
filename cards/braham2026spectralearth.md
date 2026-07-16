---
arxiv_id: '2605.21075'
authors:
- Nassim Ait Ali Braham
- Aaron Banze
- Conrad M. Albrecht
- Julien Mairal
- Jocelyn Chanussot
- Xiao Xiang Zhu
axes:
- G3_spatial_transfer
- G11_complementarity
- G2_label_scarce_efficiency
- G1_label_rich_parity
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: CDL
  direction: worse
  id: braham2026spectralearth#c1
  label_ratio: null
  locator: Table 2
  metric: miou
  model: dofa
  span: '70.9

    67.2

    41.3

    60.7'
  span_sha256: a8388667bac67beab0ac0e2b2f0cdd4d4b1c03c6a36dcad183a3d477581af7fc
  task: semantic_segmentation
  value: 55.6
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: GF5-WH
  direction: worse
  id: braham2026spectralearth#c2
  label_ratio: null
  locator: Table 2
  metric: miou
  model: dofa
  span: '41.9'
  span_sha256: e6da2ed23244cd5d05ff47fabb923bf7b9580cae7be62f012ea12d2fd7fc4962
  task: semantic_segmentation
  value: 41.9
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 91.42
  dataset: Sen1Floods11
  direction: worse
  id: braham2026spectralearth#c3
  label_ratio: 1.0
  locator: Table 5
  metric: miou
  model: dofa
  span: '89.37'
  span_sha256: d7f2c142af7565838344b77a128fb282be9d9b48e54cd9209ad055e21398a633
  task: flood_mapping
  value: 89.37
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 54.79
  dataset: MADOS
  direction: better
  id: braham2026spectralearth#c4
  label_ratio: 1.0
  locator: Table 5
  metric: miou
  model: scalemae
  span: '76.68

    57.32

    24.55

    74.13

    35.11

    62.96

    21.47'
  span_sha256: 356b53d92699420786c53195b75126f960cbe57f0c186fcff027946264702f45
  task: semantic_segmentation
  value: 57.32
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 31.6
  dataset: PASTIS-R
  direction: worse
  id: braham2026spectralearth#c5
  label_ratio: 1.0
  locator: Table 5
  metric: miou
  model: dofa
  span: '80.63

    59.58

    30.02

    89.37

    39.29

    61.84

    27.07'
  span_sha256: 1861dcd53f4f1f269d27d747d3a23d830f2de62a3eb28cf2d3435fd9eb4eb4d8
  task: crop_type_mapping
  value: 30.02
date: '2026-05-20'
doi: 10.48550/arxiv.2605.21075
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:10:34.503973Z'
key: braham2026spectralearth
limitations:
- benchmark_narrowness
- interpretability
- compute_cost
models:
- dofa
- scalemae
proposed_tags:
- hyperspectral_imagery
- multisensor_fusion
- JEPA_pretraining
- spectral_tokenization
- sensor_branch_routing
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- crop_type_mapping
- change_detection
- flood_mapping
title: 'SpectralEarth-FM: Bringing Hyperspectral Imagery into Multimodal Earth Observation
  Pretraining'
venue: arXiv
---

## summary

SpectralEarth-FM is a hierarchical transformer trained with a JEPA-style objective on SpectralEarth-MM, a new ~40TB dataset co-locating spaceborne hyperspectral imagery (EnMAP, EMIT, DESIS) with Sentinel-2, Landsat-8/9, Landsat LST, and Sentinel-1 over ~2M global locations. The model uses spectral tokenization, sensor-specific branches, cross-sensor fusion, and a shared Hiera encoder, and is evaluated on ten hyperspectral benchmarks plus PANGAEA general EO benchmarks. It achieves top average rank on hyperspectral tasks and competitive (near-top) results on PANGAEA benchmarks against models including DOFA, CROMA, Prithvi, Scale-MAE, and TerraMind.

## setup

Pretraining uses SpectralEarth-MM (2M locations, 25M patches) with global/local view sampling and a teacher-student EMA JEPA objective with SIGReg regularization, trained 50 epochs on 48 A100 GPUs. Downstream evaluation covers ten hyperspectral segmentation benchmarks (frozen encoder, SegFormer head) and seven PANGAEA benchmarks (HLS Burns, MADOS, PASTIS-R, Sen1Floods11, DynEarthNet, SN7, AI4Farms) at 100% label ratio, reporting mIoU.

## caveats

The authors note SpectralEarth-FM trades sensor flexibility for in-distribution spectral performance, relying on explicit per-sensor branches rather than any-sensor generalization; they also state that how fused spatio-spectral features are encoded in the shared representation is not yet fully understood, and multi-branch routing can hurt on fine-grained tasks like MADOS due to coarser OLI spatial resolution.
