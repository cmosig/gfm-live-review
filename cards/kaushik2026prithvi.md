---
arxiv_id: '2601.02315'
authors:
- Saurabh Kaushik
- Lalit Maurya
- Beth Tellman
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G2_label_scarce_efficiency
- G5_cost
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 90.8
  dataset: Sen1Floods11
  direction: worse
  id: kaushik2026prithvi#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: U-Net Base [li2023assessment] 84.03 90.80 95.40 31
  span_sha256: 45289fdc1f29a16ce6881cf72d3731512d57a942c674d40026d9638f06431700
  task: flood_mapping
  value: 90.5
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 82.54
  dataset: Sen1Floods11 Bolivia
  direction: better
  id: kaushik2026prithvi#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: Prithvi-CAFE surpasses the baseline U-Net by 10.8 IoU
  span_sha256: 09a68072d93c1a6d0182db86408ed6b1fc0ba7cd1d0b07683af3ce1c278f04e2
  task: flood_mapping
  value: 88.87
- axis: G3_spatial_transfer
  baseline: prithvi
  baseline_value: 82.89
  dataset: Sen1Floods11 Bolivia
  direction: better
  id: kaushik2026prithvi#c3
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: and the original Prithvi by 9
  span_sha256: 1063c2f1e5c36bbf905d2f6de59b15486fb00104bf31bbff04196a1e922e87c7
  task: flood_mapping
  value: 88.87
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 64.56
  dataset: FloodPlanet
  direction: better
  id: kaushik2026prithvi#c4
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: TerraMind also shows competitive performance with 62.33 IoU, whereas U-Net
    falls short at 60.14
  span_sha256: 34553d869445790c0d3eb9f130d39b1ebec04dca845c5306085e35925ab31ad6
  task: flood_mapping
  value: 68.74
- axis: G1_label_rich_parity
  baseline: dofa
  baseline_value: 61.52
  dataset: FloodPlanet
  direction: better
  id: kaushik2026prithvi#c5
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: DOFA 59.15 (0.03) 61.52 (0.02) 74.22 (0.02) 116
  span_sha256: 0532af99518ea5528b99a72c08f9db67a9fcd6d1763c78a819466a45852517a5
  task: flood_mapping
  value: 68.74
- axis: G5_cost
  baseline: prithvi
  baseline_value: 65.05
  dataset: FloodPlanet
  direction: better
  id: kaushik2026prithvi#c6
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: using only 45.5M trainable parameters
  span_sha256: c5b4e5516f968c9668ceed2db0b83926b40583dd2746cfd3e7f95d263cff1142
  task: flood_mapping
  value: 68.74
date: '2026-01-05'
doi: 10.48550/arxiv.2601.02315
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:43:16.460044Z'
key: kaushik2026prithvi
limitations:
- benchmark_narrowness
- spatial_transfer
- compute_cost
models:
- prithvi
- dofa
proposed_tags:
- adapter_fine_tuning
- cnn_transformer_fusion
- cloud_cover_failure
regions:
- global
- bo
self_evaluation: false
tasks:
- flood_mapping
title: 'Prithvi-Complimentary Adaptive Fusion Encoder (CAFE): unlocking full-potential
  for flood inundation mapping'
venue: arXiv
---

## summary

The paper proposes Prithvi-CAFE, which fuses a parameter-efficiently adapted Prithvi transformer encoder with a parallel CNN branch (Residual Blocks + Convolutional Attention Modules) via a multi-scale multi-level attention fusion module and a UperNet decoder, targeting flood inundation mapping. It addresses the observation that GFMs including Prithvi underperform U-Net on Sen1Floods11 flood segmentation, especially on spatially held-out test sites. Prithvi-CAFE achieves state-of-the-art IoU/mIoU on both Sen1Floods11 (including the Bolivia hold-out site) and FloodPlanet while using far fewer trainable parameters (45.5M) than fully fine-tuned GFMs.

## setup

Evaluated on Sen1Floods11 (446 hand-labeled Sentinel-1/2 image pairs, official train/val/test split, plus a geographically held-out Bolivia site) and FloodPlanet (19 flood events, 298 Sentinel-2 images with PlanetScope-derived labels, 4-fold cross-validation with 70/10/20 splits). Metrics: IoU (foreground/water class), mIoU, and mean Dice/m-F1; models trained with AdamW, StepLR, cross-entropy loss, fixed seed 42, batch size 8 on an RTX A6000.

## caveats

Authors note Prithvi-CAFE still struggles under dense cloud cover, with significant misclassification in cloud-shadow regions, and suggest incorporating SAR data as a future improvement to address this limitation.
