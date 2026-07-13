---
arxiv_id: '2605.21804'
authors:
- Mohammadreza Narimani
- Alireza Pourreza
- Parastoo Farajpoor
axes:
- G1_label_rich_parity
- G9_ecological_fine_scale
- G8_uncertainty
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: LandIQ 2018 tomato/non-tomato fields
  direction: parity
  id: narimani2026mapping#c1
  label_ratio: null
  locator: Table 1
  metric: f1
  model: alphaearth
  span: 'F1 Score


    99.04'
  span_sha256: e291af5295982d1c488bb3bd64d1f0b08a7c8847412a7f865eaf5f53e5f7361b
  task: crop_type_mapping
  value: 99.04
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: LandIQ 2018 tomato/non-tomato fields
  direction: parity
  id: narimani2026mapping#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: alphaearth
  span: 'Intersection over Union (IoU)


    98.11'
  span_sha256: 8bdc1a9fe9ba52fb25bae399fdd71064e9f6d53aa558e43b2c95e4b00c0de900
  task: semantic_segmentation
  value: 98.11
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: LandIQ 2018 tomato/non-tomato fields
  direction: parity
  id: narimani2026mapping#c3
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: alphaearth
  span: 'Pixel Accuracy


    99.19'
  span_sha256: dbaa2e83c0b90fb721b766a8a2c3c7b6de1b292e211a805c28a130dc8e943e8a
  task: crop_type_mapping
  value: 99.19
date: '2026-05-20'
doi: 10.48550/arxiv.2605.21804
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T09:22:11.214169Z'
key: narimani2026mapping
limitations:
- benchmark_narrowness
- time_sensitivity
- compute_cost
- mixed_pixels
models:
- alphaearth
proposed_tags:
- tomato_mapping
- monte_carlo_dropout
- u_net_segmentation
regions:
- us
self_evaluation: false
tasks:
- crop_type_mapping
- semantic_segmentation
title: Mapping Tomato Cropping Systems in California Using AlphaEarth Geospatial Embeddings
  and Deep Learning Analysis
venue: arXiv
---

## summary

The paper trains a U-Net segmentation model on 64-band AlphaEarth embeddings to distinguish processing tomato fields from non-tomato fields across California using LandIQ 2018 labels. On a spatially independent test set the model achieves high accuracy (99.19%) and F1 (99.04%), with Monte Carlo dropout uncertainty highest near field edges. The authors conclude AlphaEarth embeddings retain crop-relevant spatiotemporal structure without manual feature engineering.

## setup

9,484 LandIQ 2018 field polygons (4,742 tomato, 4,742 balanced non-tomato) were spatially split into training (6,638), validation (1,422), and test (1,424) sets; 64-band AlphaEarth embedding chips were extracted per polygon and used to train a U-Net with masked BCE + soft Dice loss, evaluated with Monte Carlo dropout (100 passes) for uncertainty.

## caveats

Authors note supervision is anchored to a single labeled year (2018) limiting temporal robustness assessment, the negative class was artificially balanced unlike real statewide class imbalance, and Monte Carlo dropout increases inference cost at scale.
