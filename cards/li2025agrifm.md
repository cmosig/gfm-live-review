---
arxiv_id: '2505.21357'
authors:
- Wenyuan Li
- Shunlin Liang
- Keyan Chen
- Yongzhe Chen
- Han Ma
- Jianglei Xu
- Yichuan Ma
- Shikang Guan
- Husheng Fang
- Zhenwei Shi
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G1_label_rich_parity
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 80.39
  dataset: EuroCrops (ARA, agricultural land mapping)
  direction: worse
  id: li2025agrifm#c1
  label_ratio: null
  locator: Table 3 / Sec 3
  metric: f1
  model: prithvi
  span: CNN-LSTM leading at 80.39% F1-score
  span_sha256: ffa10c0ef913e768c02506c41fa4e18be58a9f58d88aff6d9683283633ef3ec2
  task: crop_type_mapping
  value: 73.69
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 72.2
  dataset: EuroCrops (ARA, boundary delineation)
  direction: worse
  id: li2025agrifm#c2
  label_ratio: null
  locator: Table 4 / Sec 3
  metric: f1
  model: prithvi
  span: 'Prithvi: 53.45% F1'
  span_sha256: 4115cc54676059e6951ac3885fa2860c47c106cbdef4a1985ccb230b80465fee
  task: semantic_segmentation
  value: 53.45
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 72.2
  dataset: EuroCrops (ARA, boundary delineation)
  direction: worse
  id: li2025agrifm#c3
  label_ratio: null
  locator: Table 4 / Sec 3
  metric: f1
  model: satmae
  span: 'SatMAE: 62.50% F1'
  span_sha256: d08ee0a06f38bca88a13a0f398b1e92cc4afe560dca141169333dab2a0d2db99
  task: semantic_segmentation
  value: 62.5
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: EuroCrops (ARA, agri land use/cover)
  direction: worse
  id: li2025agrifm#c4
  label_ratio: null
  locator: Table 5
  metric: f1
  model: prithvi
  span: '43.50

    36.71

    40.12'
  span_sha256: bf46a80dc61fa2b188a43a5c8ddfce00cb7777995a4ada3e123b2c9a0c05cc01
  task: land_cover_classification
  value: 40.12
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Paddy rice mapping (Monsoon Asia)
  direction: worse
  id: li2025agrifm#c5
  label_ratio: null
  locator: Sec 7.1 table
  metric: f1
  model: prithvi
  span: '82.64

    81.61

    80.74'
  span_sha256: ea0fbe128a50554bbbc3c31e604d72d84d9cd9c8901247195604f85953fd0c79
  task: crop_type_mapping
  value: 80.74
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Winter wheat mapping (Asia)
  direction: worse
  id: li2025agrifm#c6
  label_ratio: null
  locator: Sec 7.1 table
  metric: f1
  model: prithvi
  span: '66.61

    57.88

    62.73'
  span_sha256: 64f1d377e22a55391fd42591f90ace79f57f5b8d4e012a9f25e7af8e038af148
  task: crop_type_mapping
  value: 62.73
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: null
  dataset: EuroCrops (ARA, agri land use/cover, 24 frames)
  direction: worse
  id: li2025agrifm#c7
  label_ratio: null
  locator: Table 11
  metric: f1
  model: prithvi
  span: 'Prithvi

    42.10

    43.01

    41.60

    38.93

    39.85'
  span_sha256: e8d3f9638a1172ad91622399abb2abd867e9693064fb7ca7275a1c3d67ab7f0b
  task: land_cover_classification
  value: 42.1
date: '2025-05-27'
doi: 10.1016/j.rse.2026.115234
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:02:48.282247Z'
key: li2025agrifm
limitations:
- benchmark_narrowness
- compute_cost
- spatial_transfer
- human_semantics
models:
- prithvi
- satmae
proposed_tags:
- field_boundary_delineation
- paddy_rice_mapping
- winter_wheat_mapping
- video_swin_transformer
- synchronized_spatiotemporal_downsampling
- land_cover_fraction_supervision
- mean_teacher
regions:
- fr
- global
self_evaluation: false
tasks:
- crop_type_mapping
- land_cover_classification
- semantic_segmentation
- representation_probing
title: 'AgriFM: A Multi-source Temporal Remote Sensing Foundation Model for Agriculture
  Mapping'
venue: arXiv
---

## summary

AgriFM is a multi-source, multi-temporal remote sensing foundation model built on a modified Video Swin Transformer with synchronized spatiotemporal downsampling, pre-trained on 25M+ MODIS/Landsat/Sentinel-2 samples using land cover fraction supervision. It is compared against ViT-based RSFMs (Prithvi, SatMAE, Galileo, SMARTIES), Swin-based non-temporal models (PIS, GFM), and conventional deep learning baselines across five agriculture mapping tasks in France, Monsoon Asia, and Asia. AgriFM consistently outperforms all compared foundation models and baselines, particularly in low-data regimes and long-sequence temporal generalization.

## setup

Pretraining uses 25,244,211 images from MODIS (250/500m), Landsat-8/9 (30m), and Sentinel-2 (10/20m), supervised with GLC_FCS30D land cover fractions via a mean-teacher framework. Downstream evaluation covers agricultural land mapping, field boundary delineation, and 16-class agricultural land use/cover mapping (EuroCrops, Auvergne-Rhône-Alpes, France, 2018-2020), paddy rice mapping (Monsoon Asia, HLS30+MODIS, 2019), and winter wheat mapping (Asia, MODIS, 2020-2021), compared against CNN/CNN-LSTM/3DCNN baselines and ViT/Swin-based RSFMs (Prithvi, SatMAE, Galileo, SMARTIES, PIS, GFM).

## caveats

Authors note the non-paired multi-source pretraining lacks spatial alignment across sensors (relying on land cover fraction supervision as a semantic bridge); the versatile decoder is limited to dense spatial prediction and doesn't generalize to site-based regression or point prediction tasks; and the pretraining data's geographical coverage is limited relative to global satellite systems, leaving open questions about spatial generalization.
