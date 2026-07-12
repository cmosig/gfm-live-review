---
arxiv_id: '2506.20380'
authors:
- Zhengpeng Feng
- Clement Atzberger
- Sadiq Jaffer
- Jovana Knezevic
- Silja Sormunen
- Robin Young
- Madeline C. Lisaius
- Markus Immitzer
- Toby Jackson
- James Ball
- David A. Coomes
- Anil Madhavapeddy
- Andrew Blake
- Srinivasan Keshav
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G6_compactness
- G8_uncertainty
- G9_ecological_fine_scale
- G12_openness
claims:
- axis: G1_label_rich_parity
  baseline: alphaearth
  baseline_value: 76.9
  dataset: TreeSatAI-TS
  direction: better
  id: feng2025tessera#c1
  label_ratio: 1.0
  locator: Table 1 (a1)
  metric: f1
  model: tessera
  span: TESSERA achieves a state-of-the-art F1-score of 77.96 with full supervision
  span_sha256: f2e477e3f5b369c002db4c91a89fd77c37326d2dc122353120aaa5daa743518e
  task: land_cover_classification
  value: 77.96
- axis: G2_label_scarce_efficiency
  baseline: alphaearth
  baseline_value: 52.79
  dataset: TreeSatAI-TS
  direction: better
  id: feng2025tessera#c2
  label_ratio: 0.01
  locator: Table 1 (a1)
  metric: f1
  model: tessera
  span: it achieves an F1 score of 60.58
  span_sha256: e5d5b099cede05b4505efc9248e28c0637fc47e783ebe5a95b2060696cda840e
  task: land_cover_classification
  value: 60.58
- axis: G2_label_scarce_efficiency
  baseline: alphaearth
  baseline_value: 37.22
  dataset: Austrian Crop
  direction: better
  id: feng2025tessera#c3
  label_ratio: 0.01
  locator: Table 1 (a2)
  metric: f1
  model: tessera
  span: TESSERA achieves a 66.15 F1 score
  span_sha256: b9cc761b950ebd03d15a4720041c34aca9dc5150bd7b8203852f1e3052532a9c
  task: crop_type_mapping
  value: 66.15
- axis: G1_label_rich_parity
  baseline: alphaearth
  baseline_value: 25.7
  dataset: Austrian Crop
  direction: better
  id: feng2025tessera#c4
  label_ratio: 1.0
  locator: Table 1 (b)
  metric: miou
  model: tessera
  span: TESSERA achieves 53.12 mIoU, establishing a new SOTA
  span_sha256: 2f2b5066c4c0bb087bf7b98b9b09a25d1838040e906d796b6244add852e5ee85
  task: crop_type_mapping
  value: 53.12
- axis: G1_label_rich_parity
  baseline: alphaearth
  baseline_value: 51.08
  dataset: PASTIS-R
  direction: worse
  id: feng2025tessera#c5
  label_ratio: 1.0
  locator: Table 1 (b)
  metric: miou
  model: tessera
  span: it obtains 50.68 mIoU, ranking second
  span_sha256: 4a1df0746059c8a57b54c0d163f5434a135d4a03b46195a9f64e415fba62d05e
  task: semantic_segmentation
  value: 50.68
- axis: G1_label_rich_parity
  baseline: alphaearth
  baseline_value: 29.59
  dataset: Biomassters
  direction: better
  id: feng2025tessera#c6
  label_ratio: 1.0
  locator: Table 1 (c)
  metric: rmse
  model: tessera
  span: TESSERA achieves an RMSE of 27.43 t/ha with full labels
  span_sha256: bfb39e5c775b97568cb9efa6fe4049fffa38bab1f8edfe1bb8c6bf17214ca72f
  task: biomass_estimation
  value: 27.43
- axis: G9_ecological_fine_scale
  baseline: alphaearth
  baseline_value: 16.1
  dataset: Borneo Canopy Height
  direction: better
  id: feng2025tessera#c7
  label_ratio: 1.0
  locator: Table 1 (c)
  metric: rmse
  model: tessera
  span: achieving the lowest RMSE of 12.2 m.
  span_sha256: cc91aff175705e33445dbd8e56cf8b927ba18090d6a61321c31c1b6da2a86e74
  task: canopy_height_estimation
  value: 12.2
date: '2025-06-25'
doi: 10.48550/arxiv.2506.20380
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T16:31:02.740876Z'
key: feng2025tessera
limitations:
- benchmark_narrowness
- time_sensitivity
models:
- tessera
- alphaearth
- presto
- croma
- dofa
- prithvi
- scalemae
- galileo
proposed_tags:
- tree_species_classification
- embeddings_as_data
- temporal_sampling_invariance
- cloud_robustness
- sentinel1_sentinel2_fusion
- barlow_twins
- int8_quantization
- pixel_wise_foundation_model
regions:
- de
- fr
- at
- fi
- my
- global
self_evaluation: true
tasks:
- land_cover_classification
- crop_type_mapping
- semantic_segmentation
- biomass_estimation
- canopy_height_estimation
title: 'TESSERA: Temporal Embeddings of Surface Spectra for Earth Representation and
  Analysis'
venue: arXiv
---

## summary

TESSERA is a pixel-wise, multi-modal (Sentinel-1/2) foundation model that learns label-efficient temporal embeddings via Barlow Twins with sparse random temporal sampling, global shuffling, and mix-based regularization. It releases global, annual, 10m, int8 pixel-wise embeddings and achieves state-of-the-art or competitive accuracy across classification, segmentation, and regression benchmarks, especially in low-label regimes. Lightweight adaptation heads on frozen embeddings match or beat larger fine-tuned RSFMs and even task-specific competition winners.

## setup

Pretrained on ~800M d-pixels from 3,012 global MGRS tiles (2017-2024) on 16 AMD MI300X GPUs. Evaluated on six Sentinel-1/2 benchmarks (TreeSatAI-TS, PASTIS-R, Austrian Crop classification/segmentation, Biomassters, Borneo Canopy Height) at 1%/30%/100% label ratios against RSFM baselines using the Pangaea framework, with lightweight MLP/UNet heads on frozen embeddings.

## caveats

Authors note embedding robustness degrades sharply when annual valid Sentinel-2 observations drop below ~10-20; winter/dormant-season data adds non-discriminative noise; and dense, high-resolution multi-temporal S1+S2 labeled datasets are scarce, prompting them to contribute two new benchmarks.
