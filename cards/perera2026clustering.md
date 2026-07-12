---
arxiv_id: '2605.30467'
authors:
- Amal S. Perera
- Chandi Witharana
- Elias Manos
- Michael Pimenta
- Anna K. Liljedahl
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G9_ecological_fine_scale
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: Arctic infrastructure
  direction: better
  id: perera2026clustering#c1
  label_ratio: null
  locator: Abstract
  metric: f1
  model: prithvi
  span: consistent improvements in foreground mean F1 scores of 0.87, 0.72, 0.93,
    and 0.87
  span_sha256: 611beb88a644c1112ca08d6037abd77b468cc6be26be3a748c71d60a39e444f7
  task: semantic_segmentation
  value: 0.87
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: IWP
  direction: better
  id: perera2026clustering#c2
  label_ratio: null
  locator: Abstract
  metric: f1
  model: prithvi
  span: consistent improvements in foreground mean F1 scores of 0.87, 0.72, 0.93,
    and 0.87
  span_sha256: 611beb88a644c1112ca08d6037abd77b468cc6be26be3a748c71d60a39e444f7
  task: semantic_segmentation
  value: 0.72
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: RTS
  direction: better
  id: perera2026clustering#c3
  label_ratio: null
  locator: Abstract
  metric: f1
  model: prithvi
  span: consistent improvements in foreground mean F1 scores of 0.87, 0.72, 0.93,
    and 0.87
  span_sha256: 611beb88a644c1112ca08d6037abd77b468cc6be26be3a748c71d60a39e444f7
  task: semantic_segmentation
  value: 0.93
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: TCN
  direction: better
  id: perera2026clustering#c4
  label_ratio: null
  locator: Abstract
  metric: f1
  model: prithvi
  span: consistent improvements in foreground mean F1 scores of 0.87, 0.72, 0.93,
    and 0.87
  span_sha256: 611beb88a644c1112ca08d6037abd77b468cc6be26be3a748c71d60a39e444f7
  task: semantic_segmentation
  value: 0.87
date: '2026-05-28'
doi: 10.48550/arxiv.2605.30467
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:39:49.923228Z'
key: perera2026clustering
limitations:
- benchmark_narrowness
- spatial_transfer
- compute_cost
- time_sensitivity
models:
- prithvi
proposed_tags:
- arctic_infrastructure_mapping
- ice_wedge_polygon_detection
- retrogressive_thaw_slump_detection
- tundra_capillary_network_detection
- VHSR_pretraining_curation
- affinity_propagation_clustering
- domain_specific_MAE
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- change_detection
- landslide_susceptibility
title: Clustering Guided Domain-Specific Pretrained Foundation Model for Very High-Resolution
  Arctic Remote Sensing
venue: arXiv
---

## summary

The paper introduces an Arctic-domain-adapted MAE-pretrained ViT-Large remote sensing foundation model, built via diversity-aware clustering-based curation of Vantor VHSR imagery, and evaluates it on four hand-labeled Arctic feature-mapping datasets (infrastructure, ice-wedge polygons, retrogressive thaw slumps, tundra capillary networks).

## setup

Approximately 3 million training patches were curated from 267 TB of Vantor VHSR multispectral imagery via two-stage affinity-propagation clustering, used to pretrain a ViT-Large MAE, then fine-tuned within a ViTDetLoc detection/segmentation framework and evaluated on four Arctic feature datasets against an ImageNet-initialized baseline and Prithvi-EO-2.0.

## caveats

Authors note Prithvi-EO-2.0 was pretrained on 30m-resolution global HLS imagery, creating a resolution/domain mismatch with the 0.5m Arctic evaluation data, and that qualitative examples are for discussion only since quantitative comparisons rely on per-task metrics; they also acknowledge Arctic feature semantics (e.g., TCN and RTS appearance) are strongly seasonally and phenologically conditioned, complicating generalization.
