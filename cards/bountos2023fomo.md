---
arxiv_id: '2312.10114'
authors:
- Nikolaos Ioannis Bountos
- Arthur Ouaknine
- Ioannis Papoutsis
- David Rolnick
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
- G9_ecological_fine_scale
claims:
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 78.09
  dataset: BigEarthNet
  direction: worse
  id: bountos2023fomo#c1
  label_ratio: null
  locator: Table 2
  metric: f1
  model: dofa
  span: FoMo-Net1 66.39 73.42
  span_sha256: 2905825cc5e8e9d72b19b0444410baacd69d261185fd6befbb745c608e66925d
  task: land_cover_classification
  value: 73.42
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 51.49
  dataset: Sen12MS
  direction: worse
  id: bountos2023fomo#c2
  label_ratio: null
  locator: Table 2
  metric: f1
  model: dofa
  span: FoMo-Net1 66.39 42.87
  span_sha256: 1b6cc9bf95806e1b6a7376d8b725ee3085540dfceef217ca9546c8f5fec05c00
  task: land_cover_classification
  value: 42.87
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 27.31
  dataset: TalloS
  direction: worse
  id: bountos2023fomo#c3
  label_ratio: null
  locator: Table 2
  metric: f1
  model: dofa
  span: FoMo-Net1 67.27 18.50
  span_sha256: 0db851746c449b390d6d98fd4fbb46d1317af0884b7b9d4d4c7eaf9ba6022ab8
  task: crop_type_mapping
  value: 18.5
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 64.07
  dataset: RapidAI4EO
  direction: worse
  id: bountos2023fomo#c4
  label_ratio: null
  locator: Table 2
  metric: f1
  model: dofa
  span: FoMo-Net1 66.40 54.69
  span_sha256: a45cf308219cd98fad7069f2b0590e9b78a5ec10fbc72bdde3305d209330b2e4
  task: land_cover_classification
  value: 54.69
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 95.26
  dataset: ForestNet
  direction: worse
  id: bountos2023fomo#c5
  label_ratio: null
  locator: Table 3
  metric: f1
  model: dofa
  span: FoMo-Net1 79.31 95.22
  span_sha256: b52194b17764d55364bbdc4f101709542dc461fd84154dcaaae2189112d62c57
  task: semantic_segmentation
  value: 95.22
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 59.24
  dataset: FiveBillionPixels
  direction: worse
  id: bountos2023fomo#c6
  label_ratio: null
  locator: Table 3
  metric: miou
  model: dofa
  span: FoMo-Net1 82.85 72.75
  span_sha256: 08acd2088cfb560c2907598003f33317f5bc3427c62fda0bba6aec8b65b8035b
  task: semantic_segmentation
  value: 57.18
date: '2023-12-15'
doi: 10.48550/arxiv.2312.10114
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:07:21.404516Z'
key: bountos2023fomo
limitations:
- compute_cost
- benchmark_narrowness
- data_bias
- spatial_transfer
models: []
proposed_tags:
- forest_monitoring
- tree_species_classification
- multi_modal_pretraining
- object_detection
- point_cloud_segmentation
- FoMo-Bench
- TalloS
- FoMo-Net
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
- representation_probing
title: 'FoMo: Multi-Modal, Multi-Scale and Multi-Task Remote Sensing Foundation Models
  for Forest Monitoring'
venue: arXiv
---

## summary

The paper introduces FoMo-Bench, a global benchmark of 15 forest-monitoring datasets spanning satellite, aerial and inventory data, along with TalloS, a new global tree-species multi-label classification dataset, and FoMo-Net, a masked-autoencoder pretraining framework designed to flexibly process arbitrary combinations of spectral bands and modalities. FoMo-Net is evaluated against supervised task-specific baselines (ResNet50, ViT, ConvNext, UNet, DeepLabv3, UPerNet, Faster R-CNN) across classification, segmentation and object detection tasks. FoMo-Net achieves competitive but generally lower performance than specialized supervised models, while offering broad flexibility across sensors and tasks.

## setup

Evaluation uses FoMo-Bench's 15 datasets (BigEarthNet-MM, Sen12MS, RapidAI4EO, ForestNet, FiveBillionPixels, TreeSatAI, TalloS, NeonTree, Woody, ReforesTree, Spekboom, Waititu, FLAIR#1, FLAIR#2, FORinstance) covering classification, segmentation, and object detection tasks for forest monitoring. FoMo-Net is pretrained via masked autoencoding on a mixture of satellite (RapidAI4EO, TalloS, SSL4EO-Landsat, FiveBillionPixels) and aerial/UAV datasets using a ViT-12-layer backbone with random spectral-band sampling and gradient accumulation, then finetuned per downstream task with a task-specific head.

## caveats

The authors note FoMo-Net is still outperformed by specialized supervised models in most tasks, that tokenizing spectral bands independently creates a computational/memory bottleneck due to quadratic attention complexity as bands increase, that point-cloud data is excluded from pretraining and deferred to future work, and that TalloS's extreme class imbalance and skewed global species distribution make evaluation difficult.
