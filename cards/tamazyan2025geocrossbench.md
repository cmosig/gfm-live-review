---
arxiv_id: '2511.02831'
authors:
- Hakob Tamazyan
- Ani Vanyan
- Alvard Barseghyan
- Anna Khosrovyan
- Evan Shelhamer
- Hrant Khachatrian
axes:
- G3_spatial_transfer
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: GeoCrossBench (In-Distribution avg)
  direction: worse
  id: tamazyan2025geocrossbench#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: dofa
  span: RS foundation models do not outperform general-purpose models in-distribution
  span_sha256: 67e076e05e3ccc1033bc67c19decbc89f63ba45522ae2cd8ffedf15c489de795
  task: land_cover_classification
  value: 63.05
date: '2025-11-04'
doi: 10.48550/arxiv.2511.02831
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:26:52.825206Z'
key: tamazyan2025geocrossbench
limitations:
- benchmark_narrowness
- spatial_transfer
- data_bias
- compute_cost
models:
- dofa
- croma
- prithvi
- scalemae
proposed_tags:
- cross_band_generalization
- sensor_modality_transfer
- channelvit
- geobench_extension
- sar_optical_fusion
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
- change_detection
- crop_type_mapping
- flood_mapping
- representation_probing
title: 'GeoCrossBench: Cross-Band Generalization for Remote Sensing'
venue: arXiv
---

## summary

GeoCrossBench extends GeoBench with a cross-band generalization protocol testing in-distribution, no-overlap-band, and superset-band transfer for remote sensing foundation models. The authors find RS-specific foundation models like DOFA and TerraFM do not outperform general-purpose models like DINOv3 in-distribution, and all models suffer large performance drops under band-shift settings. They propose a new self-supervised ChannelViT-based baseline, χViT, which improves cross-band generalization.

## setup

Built from GeoBench datasets fused with Sentinel-1 SAR data plus new datasets (x-sen1floods11, x-oscd, x-harvey-flood, x-harvey-building), covering scene classification, semantic segmentation, and change detection across RGB, S2, S1, and superset band combinations. Models are fine-tuned (full and frozen-backbone) and evaluated under In-Distribution, No-Overlap, and Superset band settings.

## caveats

The authors note the datasets are limited to static objects/scenes and do not cover moving objects, for which parallel optical-SAR imagery is hard to obtain, so even perfect benchmark scores may not indicate robustness to moving-object detection on unseen bands.
