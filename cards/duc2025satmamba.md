---
arxiv_id: '2502.00435'
authors:
- Chuc Man Duc
- Hiromichi Fukui
axes:
- G1_label_rich_parity
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 66.34
  dataset: OpenEarthMap
  direction: worse
  id: duc2025satmamba#c1
  label_ratio: null
  locator: Table II
  metric: miou
  model: prithvi
  span: EfficientNet-B7 achieving an mIoU of 66.34%
  span_sha256: eac65397031e0e35974eddbe62b5d948722f59897c5b7a3fa4620ea457fb961c
  task: land_cover_classification
  value: 65.62
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 80.08
  dataset: xBD
  direction: worse
  id: duc2025satmamba#c2
  label_ratio: null
  locator: Table III
  metric: f1
  model: prithvi
  span: EfficientNet-B7 achieved the second-highest overall F1 score
  span_sha256: f53ed24a12700d3f110cab4cab948f1923b3ad570f99a01905c1473da95a983a
  task: change_detection
  value: 79.45
date: '2025-02-01'
doi: 10.48550/arxiv.2502.00435
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:12:11.341419Z'
key: duc2025satmamba
limitations:
- compute_cost
- interpretability
models:
- prithvi
proposed_tags:
- state_space_model
- mamba
- masked_autoencoder
- building_damage_assessment
- SatMamba
- ViTMAE
- ResNet50
- EfficientNet-B7
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- change_detection
title: 'SatMamba: Development of Foundation Models for Remote Sensing Imagery Using
  State Space Models'
venue: arXiv
---

## summary

SatMamba is a new masked-autoencoder pretraining framework that replaces the ViT backbone with a Mamba (state space model) encoder/decoder, aiming for linear rather than quadratic computational scaling on remote sensing imagery. Pretrained on the fMoW dataset and fine-tuned on OpenEarthMap semantic segmentation and xBD building damage assessment, SatMamba-B (without positional encodings) achieves competitive or slightly better results than ViTMAE-B/L, ResNet50, and EfficientNet-B7 baselines. The paper positions SatMamba as a viable alternative backbone for foundation models rather than introducing a new tracked foundation model itself.

## setup

Pretraining used the fMoW RGB dataset (363,572 train / 53,042 val images, 224x224, patch size 16, 75% masking ratio). Fine-tuning evaluated on OpenEarthMap (land cover semantic segmentation, 8 classes) and xBD (building localization and damage classification via UNet-style architectures) against ResNet50, EfficientNet-B7, ViTMAE-B, and ViTMAE-L backbones.

## caveats

Authors note SatMamba incurs higher initial computational cost and greater GPU memory usage than ViTMAE at smaller input sizes (224x224), only becoming advantageous at longer sequence lengths; positional encoding necessity remains unresolved; evaluation is limited to RGB high-resolution imagery with multispectral/multitemporal/medium-resolution domains left to future work; and pretraining loss does not necessarily transfer linearly to fine-tuning performance.
