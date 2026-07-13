---
arxiv_id: '2401.15855'
authors:
- Maofeng Tang
- Andrei Cozma
- Konstantinos Georgiou
- Hairong Qi
axes:
- G3_spatial_transfer
- G1_label_rich_parity
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: RESISC45
  direction: worse
  id: tang2024cross#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: scalemae
  span: 'RESISC45

    WHU-RS19

    UC Merced

    EuroSAT

    SatMAE

    66.3'
  span_sha256: dd631c6ab1cd681d115a8113ad922e9efab9611bd6ad01abe884298de28c45c3
  task: representation_probing
  value: 70.0
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Potsdam
  direction: parity
  id: tang2024cross#c2
  label_ratio: 1.0
  locator: Table 4
  metric: miou
  model: scalemae
  span: 'Scale-MAE

    ViT-Base

    0.6853'
  span_sha256: 07486a10c42607a398a5ae2052330ade3b1444f02fd256e539424b21e11d73d7
  task: semantic_segmentation
  value: 0.7507
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.7438
  dataset: Vaihingen
  direction: better
  id: tang2024cross#c3
  label_ratio: 1.0
  locator: Table 4
  metric: miou
  model: scalemae
  span: 'Supervised Baseline

    ResNet50

    0.4518'
  span_sha256: e1ba0a5cb7019cd192db29044640f5c87f32e6beebf3ea9c6f7a6c5265515bf2
  task: semantic_segmentation
  value: 0.7512
date: '2024-01-29'
doi: 10.48550/arxiv.2401.15855
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T09:23:51.566125Z'
key: tang2024cross
limitations:
- spatial_transfer
- compute_cost
models: []
proposed_tags:
- cross-scale-mae
- scale-mae
- satmae
- multi-scale-representation-learning
- knn-classification
- xformers
regions:
- global
self_evaluation: false
tasks:
- representation_probing
- land_cover_classification
- semantic_segmentation
title: 'Cross-Scale MAE: A Tale of Multi-Scale Exploitation in Remote Sensing'
venue: arXiv
---

## summary



## setup



## caveats


