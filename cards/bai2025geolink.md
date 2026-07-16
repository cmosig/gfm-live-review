---
arxiv_id: '2509.26016'
authors:
- Lubian Bai
- Xiuyuan Zhang
- Siqi Zhang
- Zepeng Zhang
- Haoyu Wang
- Wei Qin
- Shihong Du
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G10_human_semantics
- G11_complementarity
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: MLRSNet
  direction: worse
  id: bai2025geolink#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: dofa
  span: GASSL
  span_sha256: 9998a27d82d89d6e11649a7b601567b4f951c98f5c323075584e69f292652938
  task: land_cover_classification
  value: 96.36
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: AI4Smallfarms
  direction: worse
  id: bai2025geolink#c2
  label_ratio: null
  locator: Table 2
  metric: miou
  model: scalemae
  span: AI4Smallfarms
  span_sha256: d2d2074bee981df68ad32516c88adc9cf3d635bea5ae5a24e3289affc99647e8
  task: semantic_segmentation
  value: 45.98
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: AI4Smallfarms
  direction: worse
  id: bai2025geolink#c3
  label_ratio: null
  locator: Table 2
  metric: miou
  model: croma
  span: AI4Smallfarms
  span_sha256: d2d2074bee981df68ad32516c88adc9cf3d635bea5ae5a24e3289affc99647e8
  task: semantic_segmentation
  value: 45.89
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: AI4Smallfarms
  direction: worse
  id: bai2025geolink#c4
  label_ratio: null
  locator: Table 2
  metric: miou
  model: dofa
  span: AI4Smallfarms
  span_sha256: d2d2074bee981df68ad32516c88adc9cf3d635bea5ae5a24e3289affc99647e8
  task: semantic_segmentation
  value: 45.94
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: UV identification
  direction: parity
  id: bai2025geolink#c5
  label_ratio: null
  locator: Table 3
  metric: miou
  model: scalemae
  span: 'Scale-MAE


    90.29


    58.21


    74.25'
  span_sha256: 0afefc5dcb57e5fc1d1e9edc139ac3c324f518928b3864d4e2877d08e3bf8709
  task: urban_signal_mapping
  value: 74.25
- axis: G11_complementarity
  baseline: null
  baseline_value: null
  dataset: POP
  direction: worse
  id: bai2025geolink#c6
  label_ratio: null
  locator: Table 4
  metric: r2
  model: scalemae
  span: 'Scale-MAE


    47.18


    59.12'
  span_sha256: 649f70a90552c9afcb8bac95ef26d07f42b98e96981fd59870b36b756af01af7
  task: socioeconomic_estimation
  value: 47.18
- axis: G11_complementarity
  baseline: null
  baseline_value: null
  dataset: CO2
  direction: worse
  id: bai2025geolink#c7
  label_ratio: null
  locator: Table 4
  metric: r2
  model: scalemae
  span: 'Scale-MAE


    47.18


    59.12'
  span_sha256: 649f70a90552c9afcb8bac95ef26d07f42b98e96981fd59870b36b756af01af7
  task: socioeconomic_estimation
  value: 59.12
date: '2025-09-30'
doi: 10.48550/arxiv.2509.26016
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:49:54.970069Z'
key: bai2025geolink
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
models:
- croma
- dofa
- scalemae
proposed_tags:
- OSM_integration
- multimodal_fusion
- urban_function_zone_mapping
- urban_village_identification
- carbon_emission_estimation
regions:
- global
- sg
- cn
- us
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
- change_detection
- urban_signal_mapping
- population_density
- socioeconomic_estimation
- representation_probing
title: 'GeoLink: Empowering Remote Sensing Foundation Model with OpenStreetMap Data'
venue: arXiv
---

## summary

GeoLink is a multimodal remote sensing foundation model that integrates OpenStreetMap vector data into self-supervised pretraining via a heterogeneous graph encoder, cross-modal contrastive alignment, and object-patch fusion. It is evaluated against unimodal RS FMs (Scale-MAE, CROMA, DOFA, and others) on classification, segmentation, change detection, and comprehensive geographic tasks (UFZ, UV, POP, CO2), consistently outperforming baselines especially under label-scarce and multimodal settings.

## setup

Pretrained on 1.27M RS-OSM pairs derived from SkyScript-top30 using a ViT-L RS encoder and GATConv-based OSM encoder with masked reconstruction, contrastive, and spatial consistency losses. Downstream evaluation spans seven classification benchmarks (kNN/linear probing/fine-tuning), four PANGAEA-bench segmentation/change-detection datasets, and custom multimodal benchmarks for UFZ segmentation, UV identification, POP and CO2 estimation across Chicago, Singapore, Shenzhen, and Beijing.

## caveats

Authors note sinusoidal position embeddings are not inherently suited to polyline/polygon geometries, requiring key-point sampling approximations that can over-smooth spatial signal; OSM data completeness varies by region and performance degrades under high (50%) simulated OSM sparsity, particularly for multimodal UFZ segmentation; no fully modality-aligned baseline exists for direct comparison; no error bars reported due to resource limitations.
