---
arxiv_id: '2503.23844'
authors:
- Xuyang Li
- Chenyu Li
- Pedram Ghamisi
- Danfeng Hong
axes:
- G3_spatial_transfer
- G5_cost
- G9_ecological_fine_scale
claims:
- axis: G3_spatial_transfer
  baseline: dofa
  baseline_value: 88.59
  dataset: EuroSAT-SAR
  direction: better
  id: li2025fleximo#c1
  label_ratio: null
  locator: Table III
  metric: accuracy
  model: dofa
  span: modifying the patch size yields a 1.37% improvement in accuracy
  span_sha256: 07acddbff3f91c28ef4410fa4b1a35500547938703eb9a852d09c091ad2a10ae
  task: land_cover_classification
  value: 89.96
- axis: G9_ecological_fine_scale
  baseline: dofa
  baseline_value: 47.6
  dataset: SegMunich
  direction: better
  id: li2025fleximo#c2
  label_ratio: null
  locator: Table IV
  metric: miou
  model: dofa
  span: outperforming the second-best method by 1.4 in terms of mIoU
  span_sha256: 767eedf5d15b30419fc4a9902c5c5989e259ebef7ca991c3c7ba2e2a0e59770f
  task: land_cover_classification
  value: 52.7
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 92.2
  dataset: WHU-Building
  direction: better
  id: li2025fleximo#c3
  label_ratio: null
  locator: Table V
  metric: miou
  model: dofa
  span: achieves SOTA performance, with an mIoU of 94.8, which is 1.2 points higher
    than the second-best method
  span_sha256: 3497d59eefdec5cf7713d89c59a8be7ad9db68f1f4eb5a1b5dc6b3cc6a70c30e
  task: semantic_segmentation
  value: 94.8
- axis: G9_ecological_fine_scale
  baseline: dofa
  baseline_value: 93.2
  dataset: GF12MS-WHU-GF1
  direction: better
  id: li2025fleximo#c4
  label_ratio: null
  locator: Table VI
  metric: miou
  model: dofa
  span: Compared to DOFA, our model improves the mIoU by 0.6 points
  span_sha256: c6409472849a771db65c91ed5c6f85b2b89571ef78900a9dc7474edaaebd4649
  task: semantic_segmentation
  value: 93.8
date: '2025-03-31'
doi: 10.48550/arxiv.2503.23844
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:03:50.042082Z'
key: li2025fleximo
limitations:
- compute_cost
- spatial_transfer
models:
- dofa
proposed_tags:
- scene_classification
- building_extraction
- cloud_detection
- flexible_patch_size
- wavelength_embedding
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
title: 'FlexiMo: A Flexible Remote Sensing Foundation Model'
venue: arXiv
---

## summary

FlexiMo augments the pre-trained DOFA remote sensing foundation model with a parameter-free spatial resolution-aware module (PI-Resize) and a wavelength-guided dynamic channel adaptation mechanism, enabling flexible input resolution, patch size, and channel count without architectural changes. It is evaluated on scene classification, land cover segmentation, building extraction, and cloud detection across MSI, SAR, and RGB datasets, consistently improving over the fixed-configuration DOFA baseline and other RSFMs.

## setup

Experiments fine-tune a DOFA ViT-Base backbone on EuroSAT and EuroSAT-SAR (image classification), and SegMunich, WHU-Building, and GF12MS-WHU (pixel-level segmentation/building/cloud detection), comparing against RSFMs (SatMAE, SpectralGPT, CROMA, SeaMo, DOFA) and task-specific segmentation networks under varying image sizes, patch sizes, and channel configurations.

## caveats

The authors note the dynamic weight generator requires extensive large-scale pre-training and underperforms a standard Transformer if fine-tuned directly on small datasets without it; smaller patch sizes improve accuracy but substantially increase token sequence length and computational cost, requiring a performance/cost trade-off.
