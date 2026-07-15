---
arxiv_id: '2411.06229'
authors:
- Xinglei Wang
- Tao Cheng
- Stephen Law
- Zichao Zeng
- Lu Yin
- Junyuan Liu
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G3_spatial_transfer
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 36.4
  dataset: London LUC dataset
  direction: worse
  id: wang2024multimodal#c1
  label_ratio: null
  locator: Table 7
  metric: f1
  model: satclip
  span: CaLLiPer-SenTrans 38.4 ± 1.5 36.8 ± 1.5 36.4 ± 1.6
  span_sha256: 6e5d773d80efd927d0c9db002178dff19be6fd2a20ec5d6090103fe75e996375
  task: land_cover_classification
  value: 12.2
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 21.65
  dataset: NS-SeC SDM dataset
  direction: worse
  id: wang2024multimodal#c2
  label_ratio: null
  locator: Table 7
  metric: rmse
  model: satclip
  span: SatCLIP 12.2 ± 2.5 16.8 ± 2.0 12.2 ± 1.6 28.89 ± 0.09 8.84 ± 0.03 7.07 ± 0.01
  span_sha256: baf6fe0a4c9a08776ee090d057d62d06869dad52eb217b176d0d2b019ee9b58a
  task: socioeconomic_estimation
  value: 28.89
date: '2024-11-09'
doi: 10.48550/arxiv.2411.06229
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:52:23.463172Z'
key: wang2024multimodal
limitations:
- benchmark_narrowness
- spatial_transfer
- compute_cost
models:
- satclip
proposed_tags:
- POI_representation_learning
- contrastive_language_location_pretraining
- urban_space_embedding
- location_encoding
regions:
- gb
self_evaluation: false
tasks:
- land_cover_classification
- socioeconomic_estimation
- representation_probing
title: Multimodal Contrastive Learning of Urban Space Representations from POI Data
venue: arXiv
---

## summary

CaLLiPer is a multimodal contrastive learning model that aligns location embeddings with POI text descriptions to produce continuous urban space representations, evaluated on land use classification and socioeconomic status distribution mapping in London.

## setup

Uses 339,956 Ordnance Survey POIs in Greater London (March 2022), a 6,697-sample land use classification dataset, and a 4,994-LSOA NS-SeC socioeconomic dataset from the 2021 UK Census; representations are evaluated via linear and MLP probes against baselines including TF-IDF, LDA, Place2Vec, Doc2Vec, SPPE, HGI, Space2Vec, and SatCLIP.

## caveats

The authors note SatCLIP comparison is only a 'rough comparison' using a pre-trained checkpoint not tailored to POI-based tasks, and that HGI's performance is tied to its predefined LSOA spatial delineation, limiting generalisability across scales; the study is confined to a single city (London).
