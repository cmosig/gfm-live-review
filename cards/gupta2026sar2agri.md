---
arxiv_id: '2608.11142'
authors:
- Moti Rattan Gupta
- Anupam Sobti
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 82.67
  dataset: SICKLE
  direction: worse
  id: gupta2026sar2agri#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: dofa
  span: DoFA S1 61.215
  span_sha256: a983d628b2a2c033a54af767235e0aa348712ad1cdc2bbe483b7b8e247e8f00c
  task: crop_type_mapping
  value: 61.215
date: '2026-08-11'
doi: 10.48550/arxiv.2608.11142
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-14T00:16:31.924109Z'
key: gupta2026sar2agri
limitations:
- benchmark_narrowness
- compute_cost
- time_sensitivity
models: []
proposed_tags:
- SAR_intensity_pretraining
- temporal_pretext_tasks
- curriculum_learning
- masking
- SICKLE_benchmark
- phenology_prediction
regions:
- in
self_evaluation: false
tasks:
- crop_type_mapping
- crop_yield_estimation
title: 'SAR2Agri: Learning SAR Intensity Representations for Agricultural Monitoring'
venue: arXiv
---

## summary

SAR2Agri adapts phenology-inspired temporal pretext tasks (time difference and future frame prediction) from optical to SAR intensity imagery, adding masking and curriculum learning to pretrain a ViT-S encoder on Sentinel-1 over Tamil Nadu. The final curriculum model (TD then FF+TD with 90% masking) achieves 84.9% IoU on crop type mapping on the SICKLE benchmark, outperforming optical pretraining, supervised baselines, and existing multimodal and SAR foundation models.

## setup

Pretraining uses 242,590 Sentinel-1 RTC chips (224x224, VV/VH) over Tamil Nadu spanning Jan 2018-Mar 2021, paired bitemporally for TD and FF pretext tasks. Evaluation uses the SICKLE benchmark (crop type, yield, sowing/transplanting/harvest date) over the Cauvery Delta, comparing against supervised ViT-S/UNet3D, S2 SSL baselines, and pretrained multimodal (DoFA, CopernicusFM, TerraMind) and SAR (SAR-JEPA, SARATR-X, SAR-W-MixMAE, SARMAE) foundation models.

## caveats

The authors note their pipeline shows slight deterioration on sowing, transplanting, and especially harvest date prediction compared to optical pretraining, suggesting a spatial learning bias; masking degrades TD (a global summarization objective) while helping FF (a dense prediction objective); and the work is scoped to regional (Tamil Nadu) pretraining rather than a general foundation model, with future work needed to assess regional variance across diverse geographies.
