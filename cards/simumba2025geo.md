---
arxiv_id: '2511.15658'
authors:
- Naomi Simumba
- Nils Lehmann
- Paolo Fraccaro
- Hamed Alemohammad
- Geeth De Mel
- Salman Khan
- Manil Maskey
- Nicolas Longepe
- Xiao Xiang Zhu
- Hannah Kerner
- Juan Bernabe-Moreno
- Alexandre Lacoste
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G4_temporal_transfer
- G6_compactness
- G9_ecological_fine_scale
claims: []
date: '2025-11-19'
doi: 10.48550/arxiv.2511.15658
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:43:33.851984Z'
key: simumba2025geo
limitations:
- benchmark_narrowness
- data_bias
- uncertainty
- compute_cost
models:
- prithvi
- clay
- dofa
proposed_tags:
- capability_groups
- GEO-Bench-2
- hyperparameter_optimization_protocol
- frozen_vs_finetuned_ablation
- multi_spectral_ablation
- leaderboard
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- crop_type_mapping
- biomass_estimation
- semantic_segmentation
- change_detection
- flood_mapping
- representation_probing
title: 'GEO-Bench-2: From Performance to Capability, Rethinking Evaluation in Geospatial
  AI'
venue: arXiv
---

## summary

GEO-Bench-2 introduces a benchmark of 19 permissively-licensed EO datasets organized into overlapping 'capability' groups spanning classification, segmentation, regression, detection, and instance segmentation, alongside a prescriptive fine-tuning evaluation protocol. Results show no single GeoFM dominates across all capabilities: natural-image-pretrained models (ConvNeXt, DINOv3) excel on high-resolution RGB tasks, while EO-specific models (TerraMind, Prithvi, Clay) outperform on multi-spectral tasks like agriculture and disaster response. Ablations show full fine-tuning, UNet decoders, and multi-temporal inputs all matter substantially for ranking and performance.

## setup

19 datasets covering classification, pixel-wise regression/segmentation, object detection, and instance segmentation tasks are each split into train/val/test and grouped into 9 overlapping capability sets (Core, ML task type, temporality, resolution, spectral diversity). Models are evaluated via a standardized HPO (16 trials, Optuna/TPE) plus 5 repeated seeds per best configuration, using linear/UNet/Faster-RCNN/Mask-RCNN decoders depending on task type, with aggregated IQM bootstrapped scores per capability.

## caveats

The authors note a missing SAR-specific capability despite five SAR-inclusive datasets, dataset coverage biased toward Europe and North America, some arbitrary/non-universal baseline adaptation choices, untested additional models, and that predictive uncertainty is not assessed despite being critical for real-world applications.
