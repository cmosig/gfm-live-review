---
arxiv_id: '2608.27175'
authors:
- Julia Guerrero-Viu
- Alex López-Cifuentes
- Ignacio Pérez-Villar
- Fabio Pacifici
axes:
- G4_temporal_transfer
- G2_label_scarce_efficiency
- G1_label_rich_parity
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 40.0
  dataset: PASTIS-R
  direction: better
  id: guerreroviu2026temporal#c1
  label_ratio: 1.0
  locator: Sec IV-B1
  metric: miou
  model: tessera
  span: with TESSERA-UNet reaching 58.358.3 mIoU at 1Y, a 46%46\% improvement over
    the best from-scratch model
  span_sha256: 8259bad1526494d3211177cbf7d1cbde153c67e76814f218349b77572a8ed023
  task: crop_type_mapping
  value: 58.3
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: 58.3
  dataset: PASTIS-R
  direction: worse
  id: guerreroviu2026temporal#c2
  label_ratio: 1.0
  locator: Sec IV-B1
  metric: miou
  model: tessera
  span: TESSERA-UNet drops by 39%39\% on PASTIS-R (58.3→35.558.3\rightarrow 35.5 mIoU,
    1Y→\rightarrow1M)
  span_sha256: a4d40eec1d248fa9e4bb70caf4b941c1b68616a04f84f1a4acf906c844be0dd7
  task: crop_type_mapping
  value: 35.5
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: 42.9
  dataset: DynamicEarthNet
  direction: worse
  id: guerreroviu2026temporal#c3
  label_ratio: 1.0
  locator: Sec IV-B1
  metric: miou
  model: tessera
  span: but by only 5%5\% on DEN (42.9→40.842.9\rightarrow 40.8)
  span_sha256: 53c906a0ac576026736c01ec663634e1d817920db8896da399ede03d487f80ac
  task: land_cover_classification
  value: 40.8
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 44.2
  dataset: DynamicEarthNet
  direction: parity
  id: guerreroviu2026temporal#c4
  label_ratio: 1.0
  locator: Sec IV-B1
  metric: miou
  model: tessera
  span: within 2.5%2.5\% of the best from-scratch UNet, 43.143.1 vs. 44.244.2 mIoU
    at 6M
  span_sha256: 6c4cf2466b0c9a1a7d77e15bbdeda76b61d917565cc9be24f48a36bed569a805
  task: land_cover_classification
  value: 43.1
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: PASTIS-R
  direction: better
  id: guerreroviu2026temporal#c5
  label_ratio: 1.0
  locator: Sec IV-B1
  metric: miou
  model: tessera
  span: at 1Y it reaches 48.548.5 mIoU, beating every from-scratch UNet by over 21%21\%
  span_sha256: 47fef98823bcb531a020e7214efb63a5f15bef34b304b86baee85cb04003d4e1
  task: crop_type_mapping
  value: 48.5
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: null
  dataset: PASTIS-R
  direction: better
  id: guerreroviu2026temporal#c6
  label_ratio: 0.01
  locator: Sec IV-B3
  metric: miou
  model: tessera
  span: With only 1%1\% of the labels, TESSERA-UNet already reaches ∼24{\sim}24 mIoU
  span_sha256: 7e76968185bedac88810c2537af5548b13b56b66dab9f3d3b5d22cbdb7ea7719
  task: crop_type_mapping
  value: 24.0
- axis: G1_label_rich_parity
  baseline: alphaearth
  baseline_value: 51.08
  dataset: PASTIS-R
  direction: better
  id: guerreroviu2026temporal#c7
  label_ratio: 1.0
  locator: Sec IV-B2
  metric: miou
  model: tessera
  span: a 15%15\% improvement over the 50.6850.68 reported for Tessera and 14%14\%
    over the 51.0851.08 of AlphaEarth
  span_sha256: 883c6fea86955c3ebf624ea2392e4edadae2d9b4efd30499bb70ab065c910114
  task: crop_type_mapping
  value: 58.3
- axis: G9_ecological_fine_scale
  baseline: null
  baseline_value: 50.8
  dataset: LUCAS
  direction: worse
  id: guerreroviu2026temporal#c8
  label_ratio: 1.0
  locator: Sec IV-B1
  metric: balanced_accuracy
  model: tessera
  span: to 36.8%36.8\% at a 1-day window (27.6%27.6\% below the yearly baseline),
    yet still 3.4×3.4\times above the 12.5%12.5\% chance level
  span_sha256: 4397b6e26e5788ebd9f523bb3cc04dd404236fafe24fc82114bdc38781f3fe1d
  task: land_cover_classification
  value: 36.8
date: '2026-08-27'
doi: 10.48550/arxiv.2608.27175
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-17T00:09:17.157815Z'
key: guerreroviu2026temporal
limitations:
- temporal_transfer
- benchmark_narrowness
- mixed_pixels
- compute_cost
models:
- tessera
- alphaearth
proposed_tags:
- temporal_window_sensitivity
- linear_probe_vs_unet
- phenology_vs_spectral_stability
- class_adaptive_temporal_windows
regions:
- global
- fr
self_evaluation: false
tasks:
- land_cover_classification
- crop_type_mapping
- semantic_segmentation
- representation_probing
title: Temporal Sensitivity Analysis of Tessera Embeddings
venue: arXiv
---

## summary

This paper studies how the Tessera Earth observation foundation model's frozen embeddings degrade in downstream land-cover mapping performance as the observation window used to compute embeddings is shrunk from a full year down to a single day. It finds embedding value is highly task-dependent: decisive for phenology-driven crop-type mapping (PASTIS-R) but only marginal for spectrally distinct, temporally stable classes (DynamicEarthNet), while embeddings remain markedly more label-efficient than from-scratch models in both cases. Degradation under shorter windows is gradual and class-dependent, with LUCAS single-day embeddings still classifying land cover well above chance.

## setup

Frozen Tessera embeddings are recomputed over observation windows from 1 day to 1 year and fed to a linear probe or UNet segmentation head, evaluated on LUCAS (sparse polygons, 8 classes), DynamicEarthNet (dense monthly land-cover labels, 6 classes), and PASTIS-R (crop-type segmentation, 19 classes), benchmarked against from-scratch UNets trained on per-window Sentinel-1/2 composites.

## caveats

The authors note the framework only varies inference-time window of an encoder pretrained on full-year sequences, so degradation reflects the deployed representation rather than evidence about short-window pretraining; the study covers only three LULC benchmarks and a single foundation model; LUCAS has no official split so results aren't directly comparable to prior work; and full implementation details of the original Tessera PASTIS-R result were unavailable, so their reproduction is validated via ablations rather than exact replication.
