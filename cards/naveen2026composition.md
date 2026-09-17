---
arxiv_id: '2608.30817'
authors:
- Aryan Kashyap Naveen
- Abhishek Srinivas
- Pranav Moothedath
- Shrutilipi Bhattacharjee
axes:
- G1_label_rich_parity
- G6_compactness
- G3_spatial_transfer
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.864
  dataset: UC Merced
  direction: better
  id: naveen2026composition#c1
  label_ratio: null
  locator: Sec 4.2.2
  metric: accuracy
  model: prithvi
  span: our method achieves an Accuracy of 0.928, significantly outperforming the
    DynamicVis baseline (0.864)
  span_sha256: e0885f80946255fa865f70c6fe492a1df1657a7b7f4c23225df5ddc56394f0c8
  task: land_cover_classification
  value: 0.928
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.829
  dataset: NWPU-RESISC45
  direction: worse
  id: naveen2026composition#c2
  label_ratio: null
  locator: Sec 4.2.2
  metric: accuracy
  model: prithvi
  span: the proposed method achieves 81.60% accuracy, which represents a substantial
    improvement over the DynamicVis-B baseline (0.692) but falls marginally below
    the SatMAE (0.829) model
  span_sha256: 88391e6829937127409e8ccd926c28e149f143709420cc9ada08f05550425781
  task: land_cover_classification
  value: 0.816
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.805
  dataset: LEVIR-CD
  direction: parity
  id: naveen2026composition#c3
  label_ratio: null
  locator: Table 3
  metric: f1
  model: prithvi
  span: our composition-aware method achieves an F1-score of 0.806 and an Intersection
    over Union (IoU) of 0.680
  span_sha256: 723ac525a575e330b9eef040cad25a97eb3cf658ebef43b12a9e15fac4236332
  task: change_detection
  value: 0.806
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.925
  dataset: WHU Building
  direction: worse
  id: naveen2026composition#c4
  label_ratio: null
  locator: Table 5
  metric: f1
  model: prithvi
  span: Proposed Method 36.8M 0.934 0.908 0.921 0.853
  span_sha256: 875ee3f56df32c9f6d8f5a7c64bc385822d795af22674c5f0c44f5a8e13efbea
  task: semantic_segmentation
  value: 0.921
date: '2026-08-31'
doi: 10.1145/3841645.3843041
doi_status: unresolved
extractor_version: '1'
ingested_at: '2026-09-17T00:10:04.457671Z'
key: naveen2026composition
limitations:
- benchmark_narrowness
- mixed_pixels
- compute_cost
models: []
proposed_tags:
- zero_shot_image_retrieval
- scene_classification
- tiny_object_detection
- composition_aware_pretraining
- DynamicVis
- fMoW
regions:
- global
self_evaluation: false
tasks:
- representation_probing
- change_detection
- semantic_segmentation
- land_cover_classification
title: A Composition-Aware Pretraining Framework for Geospatial Foundation Models
venue: arXiv
---

## summary

The paper introduces a composition-aware pretraining framework that trains a DynamicVis-based geospatial foundation model to predict fractional land-cover composition histograms (a 'visual vocabulary' derived from clustering DINOv3 patch embeddings) via Sinkhorn EMD, alongside bidirectional MIL and auxiliary classification losses. Using only a 36.8M-parameter backbone, the method substantially outperforms much larger SatMAE and Prithvi-EO-2.0 models on region-level retrieval and scene classification tasks, while remaining competitive but slightly behind vanilla DynamicVis on pixel-level dense prediction tasks (change detection, segmentation, tiny ship detection).

## setup

Pretraining uses the fMoW dataset tiled into 512x512 cells, each subdivided into 256 32x32 patches embedded via frozen DINOv3 and clustered (K-means, k=512) to form composition target histograms; the DynamicVis-base backbone (36.8M params) is trained with frozen-backbone evaluation on downstream tasks including AID/ForestNet retrieval, UC Merced/NWPU-RESISC45 classification, LEVIR-CD change detection, LEVIR-Ship detection, and WHU building segmentation.

## caveats

The authors note a resolution-semantics trade-off: the composition-aware EMD objective biases the backbone toward holistic distributional summaries over entire cells, modestly reducing sub-pixel boundary precision on dense prediction tasks like change detection and segmentation compared to vanilla DynamicVis; the framework is also currently restricted to 3-channel RGB imagery and relies on static offline K-means clustering rather than learnable vocabularies.
