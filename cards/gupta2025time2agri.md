---
arxiv_id: '2507.04366'
authors:
- Moti Rattan Gupta
- Anupam Sobti
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G9_ecological_fine_scale
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.65442
  dataset: SICKLE
  direction: worse
  id: gupta2025time2agri#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: dofa
  span: '0.58363'
  span_sha256: 645942f3aa385bd3422db29e285f2ba38c84a6d06347b8f63a5e4afabac3f4f8
  task: crop_type_mapping
  value: 0.58363
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.527783
  dataset: FTW India
  direction: worse
  id: gupta2025time2agri#c2
  label_ratio: null
  locator: Table 3
  metric: miou
  model: dofa
  span: '0.38059'
  span_sha256: 514cd11062dc529c995789241d8ced2ae96123027f875f87201126c398d55344
  task: semantic_segmentation
  value: 0.38059
date: '2025-07-06'
doi: 10.48550/arxiv.2507.04366
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:22:11.857625Z'
key: gupta2025time2agri
limitations:
- benchmark_narrowness
- spatial_transfer
- time_sensitivity
models:
- dofa
proposed_tags:
- temporal_pretext_tasks
- future_frame_prediction
- field_boundary_delineation
- phenological_date_prediction
- regional_vs_national_pretraining
regions:
- in
self_evaluation: false
tasks:
- crop_type_mapping
- crop_yield_estimation
- semantic_segmentation
title: 'Time2Agri: Temporal Pretext Tasks for Agricultural Monitoring'
venue: arXiv
---

## summary

The paper introduces three agriculture-specific temporal pretext tasks (Time-Difference, Temporal-Frequency, and Future-Frame Prediction) for self-supervised pretraining on satellite image time series, evaluated on the SICKLE dataset (Tamil Nadu) and Fields of the World India dataset. Future Frame Prediction achieves 69.6% IoU on crop mapping and 54.2% IoU on national-scale field boundary delineation, outperforming MAE, DoFA, and supervised baselines, while Frequency Prediction achieves the lowest yield MAPE. The authors also find regional-scale pretraining substantially outperforms national-scale pretraining for regional downstream tasks.

## setup

Regional pretraining uses a custom monthly Sentinel-2 SITS dataset built over SICKLE's Tamil Nadu extent (2018-2021); national pretraining uses an expanded FTW India dataset (3x3 neighboring chip grids, 2016-2019). Downstream evaluation is on SICKLE (crop type IoU, crop yield/date MAPE) and FTW India (field instance segmentation IoU/pixel/object recall), using a ViT-S encoder compared against DoFA, MAE, supervised ViT-S, and UNet3D baselines.

## caveats

The authors note neither FF nor FP beats supervised baselines on date prediction tasks, suggesting supervised approaches remain superior for precise event detection; FF also fails to fully anticipate irregular events like flood irrigation.
