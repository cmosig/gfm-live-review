---
arxiv_id: '2404.11797'
authors:
- Yiqun Xie
- Zhihao Wang
- Weiye Chen
- Zhili Li
- Xiaowei Jia
- Yanhua Li
- Ruichen Wang
- Kangyang Chai
- Ruohan Li
- Sergii Skakun
axes:
- G1_label_rich_parity
- G9_ecological_fine_scale
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 47.7
  dataset: multi-temporal crop classification (HLS/Sentinel)
  direction: worse
  id: xie2024when#c1
  label_ratio: null
  locator: Table I
  metric: miou
  model: prithvi
  span: RFaug outperformed Prithvi by about 4%
  span_sha256: fdd73446562ba08378e3d2a88aa064967cd80cbc1977def5ee78a2dbb9ec21c6
  task: crop_type_mapping
  value: 42.69
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 77.12
  dataset: HLS Burn Scars
  direction: better
  id: xie2024when#c2
  label_ratio: null
  locator: Table III
  metric: miou
  model: prithvi
  span: both foundation models and regular convolutional networks showed significant
    advantages over traditional models such as random forest
  span_sha256: f157d816d409530be38549ff7fe5e05468c681339805b7167ed5d8e7395412ad
  task: semantic_segmentation
  value: 85.53
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 91.47
  dataset: Sen1Floods11
  direction: worse
  id: xie2024when#c3
  label_ratio: null
  locator: Table IV
  metric: f1
  model: prithvi
  span: with XGBaug presenting the highest F1 and IoU among all models
  span_sha256: 1c70211037a82542f09fb780779a86fffd21892e74d2e75fcb78aa32a65e78f4
  task: flood_mapping
  value: 88.9
date: '2024-04-17'
doi: 10.48550/arxiv.2404.11797
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:49:46.635193Z'
key: xie2024when
limitations:
- benchmark_narrowness
- human_semantics
- compute_cost
models:
- prithvi
proposed_tags:
- burn_scar_mapping
- masked_autoencoder_task_alignment
- traditional_ML_vs_foundation_model
regions:
- us
- global
self_evaluation: false
tasks:
- crop_type_mapping
- land_cover_classification
- flood_mapping
- semantic_segmentation
title: When are Foundation Models Effective? Understanding the Suitability for Pixel-Level
  Classification Using Multispectral Imagery
venue: arXiv
---

## summary

This paper compares three foundation models (ViT, SegFormer, Prithvi) against regular-size deep learning models (U-Net, DeepLabV3+, FCN) and traditional ML models (RF, RFaug, XGB, XGBaug) on three pixel-level multispectral classification tasks: crop mapping, burn scar mapping, and flood mapping. It finds that traditional ML often matches or beats foundation models, especially where texture is uninformative (e.g., flood mapping), while deep learning models (not necessarily foundation models) do better where texture matters (e.g., burn scar).

## setup

Evaluation reuses Prithvi's original datasets and splits: multi-temporal crop classification (Sentinel/HLS, USDA CDL labels, 3,083 train/771 test images), HLS Burn Scars (804 chips, 67/33 split), and Sen1Floods11 (252/89/90 train/val/test chips), comparing RF, RFaug, XGB, XGBaug, FCN, U-Net, DeepLabv3+, ViT, SegFormer, and Prithvi using mIoU/mF1.

## caveats

Authors note the masked-autoencoder SSL pretext task is misaligned with pixel-level classification when texture is uninformative, that foundation models did not show a paradigm shift over traditional/regular deep learning models, and that stability varied notably when clouds were treated as a class rather than masked as no-data.
