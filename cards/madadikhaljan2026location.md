---
arxiv_id: '2604.07092'
authors:
- Mojgan Madadikhaljan
- Jonathan Prexl
- Isabelle Wittmann
- Conrad M Albrecht
- Michael Schmitt
axes:
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
claims:
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 0.84
  dataset: Dynamic World
  direction: worse
  id: madadikhaljan2026location#c1
  label_ratio: null
  locator: Table 2
  metric: f1
  model: prithvi
  span: UNet / Micro UNet
  span_sha256: b71901cc94cbd6c9748ed96d9f9f6b3d9136775670f1bdd0d6fa8bbbb8e4bb19
  task: land_cover_classification
  value: 0.8
- axis: G2_label_scarce_efficiency
  baseline: dofa
  baseline_value: 0.79
  dataset: Dynamic World
  direction: better
  id: madadikhaljan2026location#c2
  label_ratio: null
  locator: Table 2
  metric: f1
  model: prithvi
  span: Prithvi v2-300 (Full / Frozen / Embedding)
  span_sha256: 30f411e3a663809cddffca47aa7e16e14c801065e55826aa772190276893e6a6
  task: land_cover_classification
  value: 0.8
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.053
  dataset: High resolution canopy height maps
  direction: better
  id: madadikhaljan2026location#c3
  label_ratio: null
  locator: Table 2
  metric: rmse
  model: prithvi
  span: UNet / Micro UNet
  span_sha256: b71901cc94cbd6c9748ed96d9f9f6b3d9136775670f1bdd0d6fa8bbbb8e4bb19
  task: canopy_height_estimation
  value: 0.051
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.26
  dataset: PASTIS
  direction: better
  id: madadikhaljan2026location#c4
  label_ratio: null
  locator: Table 3
  metric: f1
  model: prithvi
  span: UNet / Micro UNet
  span_sha256: b71901cc94cbd6c9748ed96d9f9f6b3d9136775670f1bdd0d6fa8bbbb8e4bb19
  task: semantic_segmentation
  value: 0.32
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.62
  dataset: HLS Burn Scars
  direction: worse
  id: madadikhaljan2026location#c5
  label_ratio: null
  locator: Table 3
  metric: f1
  model: prithvi
  span: UNet / Micro UNet
  span_sha256: b71901cc94cbd6c9748ed96d9f9f6b3d9136775670f1bdd0d6fa8bbbb8e4bb19
  task: change_detection
  value: 0.59
date: '2026-04-08'
doi: 10.48550/arxiv.2604.07092
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:39:46.243279Z'
key: madadikhaljan2026location
limitations:
- spatial_transfer
- benchmark_narrowness
- compute_cost
models:
- prithvi
- dofa
proposed_tags:
- coordinate_based_neural_representation
- implicit_neural_representation
- hyper_local_model
- TerraMind
regions:
- de
self_evaluation: false
tasks:
- land_cover_classification
- canopy_height_estimation
- semantic_segmentation
- crop_type_mapping
- change_detection
title: 'Location Is All You Need: Continuous Spatiotemporal Neural Representations
  of Earth Observation Data'
venue: arXiv
---

## summary

The paper introduces LIANet, a coordinate-based implicit neural representation that encodes a fixed geographic region as a continuous spatiotemporal field from Sentinel-2 imagery, enabling image reconstruction and lightweight fine-tuning for downstream tasks without requiring raw satellite data at adaptation time. It is compared against UNet baselines trained from scratch and three geospatial foundation models (TerraMind, Prithvi v2-300, DOFA-Large) on custom land-cover, leaf-type, building-footprint, and canopy-height tasks, plus PASTIS and HLS Burn Scars from PANGAEA. LIANet achieves competitive or superior performance with far fewer tunable parameters, but is hyper-local and does not generalize beyond its pretrained region.

## setup

Sentinel-2 multispectral imagery (four seasonal acquisitions) over Munich, Germany at three area sizes (2500, 5000, 12000 km2) is used to pretrain LIANet via image reconstruction; fine-tuning uses custom labeled datasets for land-cover, leaf-type, building footprints/density, and canopy height, plus PASTIS and HLS Burn Scars from the PANGAEA benchmark, compared against from-scratch UNets and full/frozen/embedding fine-tuning of TerraMind-Base, Prithvi v2-300, and DOFA-Large.

## caveats

The authors state LIANet's primary limitation is its hyper-local spatial scope: it operates only within the geographic region it was pretrained on and does not generalize to unseen areas, unlike GFMs designed for global applicability; downstream performance also degrades as the encoded area grows larger.
