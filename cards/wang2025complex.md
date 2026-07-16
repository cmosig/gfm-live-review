---
arxiv_id: '2504.11999'
authors:
- Mengyu Wang
- Hanbo Bi
- Yingchao Feng
- Linlin Xin
- Shuo Gong
- Tianqi Wang
- Zhiyuan Yan
- Peijin Wang
- Wenhui Diao
- Xian Sun
axes:
- G7_interpretability
- G2_label_scarce_efficiency
- G1_label_rich_parity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 57.28
  dataset: SARSegL1
  direction: better
  id: wang2025complex#c1
  label_ratio: null
  locator: Table I
  metric: miou
  model: presto
  span: 61.52%, 70.69%, and 81.33% for the mIoU, mAcc, and OA metrics
  span_sha256: e497eb0f066242a3491a091e8b22d19c666a16e3f8ad70aa0466930cb9e840aa
  task: semantic_segmentation
  value: 61.52
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 19.96
  dataset: SARSegL1
  direction: better
  id: wang2025complex#c2
  label_ratio: null
  locator: Table II
  metric: miou
  model: presto
  span: outperforming other models by 4.93% in mIoU and 3.61% in FB-IoU
  span_sha256: 61a15d6af4326dde6ff8c682fa7575276dee2ce4592009d14ca4d31b0983bfeb
  task: semantic_segmentation
  value: 24.89
- axis: G7_interpretability
  baseline: task_specific
  baseline_value: 50.2
  dataset: SARClsL1
  direction: better
  id: wang2025complex#c3
  label_ratio: null
  locator: Table IV
  metric: accuracy
  model: presto
  span: outperforming the second-best model by 16.6% and 7.1% respectively
  span_sha256: 6b693b2f8b868355e6dd8e6642feb7bc8e680dc06592dea14a33e81f5a8a6c03
  task: representation_probing
  value: 66.8
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 67.8
  dataset: HRSID
  direction: better
  id: wang2025complex#c4
  label_ratio: null
  locator: Table V
  metric: auc
  model: presto
  span: 70.3(+2.5)
  span_sha256: c0f64145323fa66917250df6753b547dc7767101aee8f5339c60e943793caa35
  task: change_detection
  value: 70.3
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 64.04
  dataset: AIR-PolSAR-Seg
  direction: better
  id: wang2025complex#c5
  label_ratio: null
  locator: Table VII
  metric: miou
  model: presto
  span: surpassing the second best mIoU by 1.68%
  span_sha256: c81b07bf10535cf0af5a93c925b295701816bd7ed84ee546d2a64b1efc73a41c
  task: semantic_segmentation
  value: 65.72
date: '2025-04-16'
doi: 10.48550/arxiv.2504.11999
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:03:15.126795Z'
key: wang2025complex
limitations:
- interpretability
- benchmark_narrowness
- mixed_pixels
models: []
proposed_tags:
- complex_valued_SAR
- polarimetric_decomposition
- ship_detection
- aircraft_detection
- few_shot_segmentation
- unsupervised_classification
regions:
- cn
- us
- th
self_evaluation: false
tasks:
- semantic_segmentation
- change_detection
title: A Complex-valued SAR Foundation Model Based on Physically Inspired Representation
  Learning
venue: arXiv
---

## summary

The paper introduces a self-supervised foundation model for complex-valued SAR imagery that simulates the physical process of polarimetric decomposition using learnable 'scattering queries' to produce physically interpretable feature representations. It is pre-trained on 400,000 GF3 QPSI images and evaluated on six downstream tasks spanning complex-valued and general (amplitude-only) SAR datasets. The model achieves state-of-the-art results across semantic segmentation, few-shot segmentation, unsupervised classification, ship detection, aircraft detection, and general SAR segmentation.

## setup

Pre-training uses 400,000 GF3 QPSI complex-valued SAR images (8-channel real/imaginary HH/HV/VH/VV) with a Swin-B backbone, supervised only by polarimetric decomposition loss (against Yamaguchi coefficients) and a power self-supervised loss. Downstream evaluation covers SARSegL1 and SARClsL1 (complex-valued) and HRSID, SAR-AIRcraft-1.0, and AIR-PolSAR-Seg (amplitude-only general SAR) datasets, compared against Swin-ImageNet-1K, RingMo, and FGMAE pretrained backbones.

## caveats

The authors note fitting each pixel's scattering values individually would be computationally burdensome and risk overfitting, requiring binarization via a distribution-based threshold; some scattering components (S.F. and Vol) converge more slowly and their reconstruction quality (~70% OA) is notably lower than others (~90%+). The paper is limited to SAR modality and the authors state future work should extend to a multi-modal foundation model.
