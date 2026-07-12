---
arxiv_id: '2606.20034'
authors:
- Htet Yamin Ko Ko
- Clement Atzberger
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
claims:
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: WUDAPT LCZ
  direction: better
  id: ko2026exploring#c1
  label_ratio: null
  locator: Table 6 / Sec 5.1
  metric: miou
  model: tessera
  span: TESSERA achieved the best test results with a test IoU of 0.69 and accuracy
    of 0.80
  span_sha256: 588fcc829fc4b216476a42af9efd665f9c9f64621deab858731a0f975de7925e
  task: local_climate_zone_classification
  value: 0.69
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Bern LCZ
  direction: better
  id: ko2026exploring#c2
  label_ratio: null
  locator: Table 7 / Sec 5.2
  metric: miou
  model: alphaearth
  span: followed by AlphaEarth (0.81) and the model using annual composites
  span_sha256: 9d60801a7c194b4f2088103a625f8dce8d4010fdaa7ff05e6b69e8710caea32d
  task: local_climate_zone_classification
  value: 0.81
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: 73.9
  dataset: WUDAPT LCZ
  direction: worse
  id: ko2026exploring#c3
  label_ratio: null
  locator: Table 10 / Sec 6.4
  metric: accuracy
  model: alphaearth
  span: notable drops in Bern (73.9% to 60.1%) and Basel (77.4% to 68.8%)
  span_sha256: 604d8302746107b1a86719dd29b7574e4e3d9873ad4979eb991c1ce5b7e16d35
  task: local_climate_zone_classification
  value: 60.1
date: '2026-06-18'
doi: null
doi_status: no_doi_found
extractor_version: '1'
ingested_at: '2026-07-12T16:35:57.653092Z'
key: ko2026exploring
limitations:
- temporal_transfer
- mixed_pixels
- benchmark_narrowness
- data_bias
models:
- alphaearth
- tessera
proposed_tags:
- lcz_upscaling
- urban_morphology
- attention_unet
- wudapt
- embeddings_vs_composites
- reference_data_resolution
- coarse_label_training
regions:
- ch
self_evaluation: false
tasks:
- local_climate_zone_classification
title: 'Exploring the potential of AlphaEarth and TESSERA embeddings for Fine-scale
  Local Climate Zone Mapping: A case study across five cities in Switzerland'
venue: arXiv
---

## summary

The paper benchmarks precomputed TESSERA and AlphaEarth embeddings against Sentinel-1/2 seasonal composites for upscaling coarse WUDAPT LCZ maps to 10 m resolution across five Swiss cities using an attention U-Net. TESSERA consistently gives the best same-year performance (test IoU 0.59-0.69 multi-city, 0.77-0.82 single-city Bern), while S1S2 composites transfer most stably across years. Year-to-year temporal transfer without retraining remains an open challenge, and reference-data resolution is identified as the strongest lever for accuracy.

## setup

Three experiments train separate attention U-Nets on S1S2 (14-16 feat), AlphaEarth (64D) and TESSERA (128D) inputs at 10 m, using WUDAPT 100 m (five cities, 13 classes) and Bern LCZ 78 m (14 classes) reference labels; evaluation uses stratified 60/20/20 patch splits with IoU and accuracy. Exp I is multi-city (2024), Exp II is single-city Bern with higher-resolution labels, and Exp III applies 2024-trained models to 2025 data.

## caveats

Authors flag that the 100 m WUDAPT reference resolution and severe class imbalance (rare classes like LCZ 3, C, F, 9 poorly predicted, mixed within single-pixel footprints) limit accuracy and evaluation; the study is restricted to a single country (five Swiss cities); and temporal transfer from one year to another declines because embeddings capture weather-driven phenology drift, remaining an open challenge.
