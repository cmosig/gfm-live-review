---
arxiv_id: '2503.12843'
authors:
- Haozhe Si
- Yuxuan Wan
- Minh Do
- Deepak Vasisht
- Han Zhao
- Hendrik F. Hamann
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 98.83
  dataset: EuroSAT
  direction: worse
  id: si2025towards#c1
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: satmae
  span: '98.78'
  span_sha256: bb1165cecc4700e0359df44c3ec43881d001c3a95dced9950039252816a637a2
  task: land_cover_classification
  value: 98.78
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 49.48
  dataset: DFC2020
  direction: better
  id: si2025towards#c2
  label_ratio: null
  locator: Table 3
  metric: miou
  model: satmae
  span: '52.84'
  span_sha256: cdd9d795aa7b41f35d3ba7904c71c83fcb3c4a765c2b812cd63357c1ad8e55bf
  task: semantic_segmentation
  value: 52.84
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 43.04
  dataset: MARIDA
  direction: better
  id: si2025towards#c3
  label_ratio: null
  locator: Table 3
  metric: miou
  model: satmae
  span: '54.33'
  span_sha256: 361d99805e3ed1056cd3eb490a0363bebd275384f5414bca9ff73cffa16fc0d8
  task: semantic_segmentation
  value: 54.33
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: NLCD-L
  direction: worse
  id: si2025towards#c4
  label_ratio: null
  locator: Table 4
  metric: miou
  model: satmae
  span: '18.05'
  span_sha256: 4859f5f978a913f4965bbf5e4b974e9e364bc32b341a2d6b23ed5a0728e9b5cf
  task: semantic_segmentation
  value: 18.05
- axis: G1_label_rich_parity
  baseline: satmae
  baseline_value: 85.84
  dataset: BigEarthNet
  direction: better
  id: si2025towards#c5
  label_ratio: 0.1
  locator: Table 3
  metric: f1
  model: croma
  span: '87.57'
  span_sha256: 3a54b7dd0b129857f564fce7fc64cc81c1049bc3ce6f221fe19dcf94a273d3f1
  task: crop_type_mapping
  value: 87.57
date: '2025-03-17'
doi: 10.48550/arxiv.2503.12843
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:50:29.454170Z'
key: si2025towards
limitations:
- compute_cost
- spatial_transfer
- benchmark_narrowness
models:
- satmae
- croma
proposed_tags:
- hyperspectral
- multi-modal-fusion
- low-rank-attention
- masked-autoencoder
- cross-satellite-generalization
- SAR
- spectral-attention
- Kronecker-product-attention
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- local_climate_zone_classification
- semantic_segmentation
- representation_probing
title: Towards Scalable Foundation Model for Multi-modal and Hyperspectral Geospatial
  Data
venue: arXiv
---

## summary

The paper introduces LESS ViT, a low-rank efficient spatial-spectral attention architecture and Hyper-MAE pretraining framework for hyperspectral, multi-modal geospatial data, plus GFM-Bench, a standardized benchmark. It compares against SatMAE, CROMA, SpectralGPT, Scale-MAE, SatMAE++, and Channel-ViT baselines on classification, segmentation, and cross-satellite generalization tasks.

## setup

Pretrained on SSL4EO-S12 (Sentinel-1 SAR + Sentinel-2 MSI, 250K locations, 4 seasons) using Hyper-MAE with 75% spatial and 50% spectral masking; evaluated via fine-tuning and linear probing on GFM-Bench, which includes EuroSAT, BigEarthNet, So2Sat, SegMunich, DFC2020, MARIDA, and NLCD-L (Landsat, cross-satellite generalization).

## caveats

Authors note performance gaps on So2Sat and DFC2020 due to distribution shift between train/test; multi-modal zero-shot (linear probing) features underperform CROMA due to single shared backbone dominated by optical input; extending LESS attention to additional dimensions (e.g., temporal) reduces per-dimension embedding capacity; approach is limited to raster data and does not integrate vector-based domain knowledge.
