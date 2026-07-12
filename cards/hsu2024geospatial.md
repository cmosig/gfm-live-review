---
arxiv_id: '2409.00489'
authors:
- Chia-Yu Hsu
- Wenwen Li
- Sizhe Wang
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.793
  dataset: Mars crater
  direction: better
  id: hsu2024geospatial#c1
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: prithvi
  span: Prithvi 0.859
  span_sha256: 226eec7bb073cb87f313e793271a8027c5c31aa7ba65a8d2ca7c63475d5a4d8c
  task: semantic_segmentation
  value: 0.859
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.515
  dataset: Earth's natural feature
  direction: better
  id: hsu2024geospatial#c2
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: prithvi
  span: mAP50 score of 0.550
  span_sha256: fcd0097ae9ed3d0b9842bb1a9d20eab655744a614083963e0799abd3d127822d
  task: semantic_segmentation
  value: 0.55
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.486
  dataset: Ice-wedge polygon
  direction: better
  id: hsu2024geospatial#c3
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: prithvi
  span: mAP50 scores of 0.859 and 0.505 for Mars crater and ice-wedge polygons
  span_sha256: c5d8faa6ad52459b5343fc52ff4aca2a48013061f9ef31f79098078acfbfb1b9
  task: semantic_segmentation
  value: 0.505
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.561
  dataset: EuroCrops
  direction: better
  id: hsu2024geospatial#c4
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: prithvi
  span: a score of 0.607 for the EuroCrops dataset
  span_sha256: 45657eeac3fd30164c7dd2269cc9edbd7b7e192a3ec59d94766e0e6d10095099
  task: crop_type_mapping
  value: 0.607
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: 0.607
  dataset: EuroCrops
  direction: worse
  id: hsu2024geospatial#c5
  label_ratio: 0.25
  locator: Table 6
  metric: accuracy
  model: prithvi
  span: 0.848 0.444 0.458 0.580
  span_sha256: 5dfa1910c34a37b299fd3bc261d77195d1c22b6f70e552e1c5f3c9356f6e59ae
  task: crop_type_mapping
  value: 0.58
- axis: G5_cost
  baseline: task_specific
  baseline_value: 0.097
  dataset: averaged over 4 datasets
  direction: worse
  id: hsu2024geospatial#c6
  label_ratio: null
  locator: Table 4
  metric: r2
  model: prithvi
  span: Prithvi 0.297 0.657
  span_sha256: de1dd6975b5146274c45b5313bee3fee52974eb7b1c7e8abab8203e4cac8fe13
  task: semantic_segmentation
  value: 0.297
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: 0.607
  dataset: EuroCrops
  direction: worse
  id: hsu2024geospatial#c7
  label_ratio: null
  locator: Table 5
  metric: accuracy
  model: prithvi
  span: 0.607 0.430 (-29.16%)
  span_sha256: 45bc1ebfe0dbd079d724c304618f2045be317243d8bb722659464e46373c0b21
  task: crop_type_mapping
  value: 0.43
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 0.708
  dataset: EuroCrops
  direction: worse
  id: hsu2024geospatial#c8
  label_ratio: null
  locator: Table 7
  metric: accuracy
  model: prithvi
  span: MViTv2-Optimal N/A 0.708
  span_sha256: 59675b875fdb11256ec3798dcb23d9d5a95ef71677892d3455af681889b10594
  task: crop_type_mapping
  value: 0.657
date: '2024-08-31'
doi: 10.48550/arxiv.2409.00489
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:48:58.730537Z'
key: hsu2024geospatial
limitations:
- compute_cost
- benchmark_narrowness
- spatial_transfer
models:
- prithvi
proposed_tags:
- object_detection
- instance_segmentation
- band_adaptation
- mars_crater_detection
- ice_wedge_polygon_mapping
regions:
- global
- dk
self_evaluation: false
tasks:
- semantic_segmentation
- crop_type_mapping
- representation_probing
title: 'Geospatial foundation models for image analysis: evaluating and enhancing
  NASA-IBM Prithvi''s domain adaptability'
venue: arXiv
---

## summary

This paper evaluates NASA-IBM's Prithvi geospatial foundation model against task-specific and general-purpose transformer/CNN baselines on object detection and instance segmentation across four remote sensing datasets. It introduces band adaptation, multi-scale feature generation, and fine-tuning strategies to improve Prithvi's domain adaptability, showing Prithvi generally outperforms ViT, MViTv2, and ResNet-50 in accuracy but is slower and lacks a fully pre-trained task-specific pipeline.

## setup

Four datasets used: Mars crater (object detection), Earth's natural feature (object detection), Ice-wedge polygon (instance segmentation), and EuroCrops (instance segmentation), evaluated using a Mask R-CNN-style pipeline built on Prithvi's ViT encoder with mAP-based metrics.

## caveats

The authors note Prithvi lacks a fully trained task-specific pipeline (only the backbone is pre-trained), limiting its ability to reach state-of-the-art performance and few-shot efficiency compared to models like MViTv2-Optimal that are fully pre-trained end-to-end; they also flag the need for standardized benchmarking and safeguards against data leakage in future GFM evaluation.
