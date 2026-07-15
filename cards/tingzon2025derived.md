---
arxiv_id: '2509.18182'
authors:
- Isabelle Tingzon
- Yoji Toriumi
- Caroline Gevaert
axes:
- G2_label_scarce_efficiency
- G1_label_rich_parity
- G3_spatial_transfer
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.858
  dataset: Saint Vincent and the Grenadines (VCT)
  direction: worse
  id: tingzon2025derived#c1
  label_ratio: null
  locator: Table 2
  metric: f1
  model: scalemae
  span: ConvNeXt-base
  span_sha256: a44ed0ae6dfc941b501431432ff783d841ec96751abfc9c53cc5ac6149d222cc
  task: semantic_segmentation
  value: 0.617
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.835
  dataset: Saint Vincent and the Grenadines (VCT)
  direction: worse
  id: tingzon2025derived#c2
  label_ratio: null
  locator: Table 2
  metric: f1
  model: scalemae
  span: ConvNeXt-large
  span_sha256: 71b5ba50392f4914038b9b9ae39bde2e017ae408b2f1b444e065f1d13fd31e9e
  task: semantic_segmentation
  value: 0.598
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.858
  dataset: Combined VCT+LCA+DCA
  direction: better
  id: tingzon2025derived#c3
  label_ratio: null
  locator: Table 3 / Sec 4
  metric: f1
  model: scalemae
  span: the best F1 score increasing from 0.858 (using only local data) to 0.878 (using
    combined, regional data)
  span_sha256: 801360d7ba5bc32e3d636c00e418af3d793d416e135117e12b3be09bd9010ff6
  task: semantic_segmentation
  value: 0.878
date: '2025-09-18'
doi: 10.48550/arxiv.2509.18182
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:46:26.601495Z'
key: tingzon2025derived
limitations:
- data_bias
- human_semantics
- spatial_transfer
models:
- scalemae
proposed_tags:
- rooftop_classification
- roof_pitch_classification
- roof_material_classification
- GASSL
regions:
- vc
self_evaluation: false
tasks:
- semantic_segmentation
title: 'AI-Derived Structural Building Intelligence for Urban Resilience: An Application
  in Saint Vincent and the Grenadines'
venue: arXiv
---

## summary

The paper presents an AI-driven workflow using high-resolution Maxar satellite imagery to classify rooftop material and pitch attributes for Saint Vincent and the Grenadines, comparing geospatial foundation model (Scale-MAE, GASSL) embeddings with shallow classifiers against fine-tuned deep learning models (ConvNeXt, ViT). Fine-tuned ConvNeXt models outperformed foundation-model+shallow-classifier combinations, achieving F1 scores up to 0.858 (roof pitch) and 0.835 (roof material) locally, improving to 0.878 with regional Caribbean training data for roof pitch. The authors release the first building classification map for Saint Vincent and the Grenadines to support urban resilience planning.

## setup

3,243 labeled buildings from Saint Vincent and the Grenadines (augmented with 4,161 from Saint Lucia and 6,238 from Dominica) were annotated for roof pitch and roof material from Maxar/OpenAerialMap imagery and Microsoft Building Footprints, using an 80/20 stratified group split by 500m tiles. Foundation model embeddings (Scale-MAE, GASSL) were fed to shallow classifiers (LR, SVM, MLP) and compared against fine-tuned ConvNeXt/ViT variants pretrained on ImageNet.

## caveats

The authors note EO data cannot capture invisible structural attributes like roof-to-wall connections or internal integrity, limiting reliability for building-level vulnerability assessment; lower resolution imagery and cloud cover reduce classification accuracy and coverage; and the dataset is not suitable for individual building-level decisions without field verification, being better suited to neighborhood-level statistics.
