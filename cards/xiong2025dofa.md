---
arxiv_id: '2503.06312'
authors:
- Zhitong Xiong
- Yi Wang
- Weikang Yu
- Adam J Stewart
- Jie Zhao
- Nils Lehmann
- Thomas Dujardin
- Zhenghang Yuan
- Pedram Ghamisi
- Xiao Xiang Zhu
axes:
- G3_spatial_transfer
- G11_complementarity
- G7_interpretability
- G1_label_rich_parity
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 70.89
  dataset: AID
  direction: better
  id: xiong2025dofa#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: dofa
  span: DOFA-CLIP-L-384
  span_sha256: 92f663301dda8c32becb8c14cee231ce4560a3a0d3be249ea4a4d828b35a50d1
  task: land_cover_classification
  value: 76.83
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 54.3
  dataset: EuroSAT
  direction: better
  id: xiong2025dofa#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: dofa
  span: DOFA-CLIP-L-384
  span_sha256: 92f663301dda8c32becb8c14cee231ce4560a3a0d3be249ea4a4d828b35a50d1
  task: land_cover_classification
  value: 59.04
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 10.78
  dataset: m-forestnet
  direction: better
  id: xiong2025dofa#c3
  label_ratio: null
  locator: Table 3
  metric: f1
  model: dofa
  span: DOFA-CLIP-B (224)
  span_sha256: f6e46c9a58857cfecc98f99edff07d0c421ca4d753f1f7df948e10b4e286e17d
  task: land_cover_classification
  value: 13.6
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 71.6
  dataset: AID
  direction: better
  id: xiong2025dofa#c4
  label_ratio: null
  locator: Table 5
  metric: accuracy
  model: dofa
  span: DOFA-CLIP-B (Merging) (ours)
  span_sha256: f6ffddef5e917a218134c6c94ec4a68c8e7b9b850e77637f4d97d079442d835e
  task: representation_probing
  value: 77.6
- axis: G7_interpretability
  baseline: null
  baseline_value: 61.7
  dataset: MADOS
  direction: better
  id: xiong2025dofa#c5
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: dofa
  span: DOFA-CLIP-B w/ MaKA
  span_sha256: aa3a3940e9acdce6fe8a4bed3cb77605220f33592a91bbd571ad65dc46adc265
  task: semantic_segmentation
  value: 62.3
date: '2025-03-08'
doi: 10.48550/arxiv.2503.06312
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:27:38.290479Z'
key: xiong2025dofa
limitations:
- benchmark_narrowness
- human_semantics
- compute_cost
models:
- dofa
proposed_tags:
- zero_shot_classification
- cross_modal_retrieval
- vision_language_pretraining
- multimodal_clip
- weight_merging
regions:
- global
self_evaluation: true
tasks:
- representation_probing
- land_cover_classification
- semantic_segmentation
title: 'DOFA-CLIP: Multimodal Vision-Language Foundation Models for Earth Observation'
venue: arXiv
---

## summary

DOFA-CLIP introduces a unified vision-language foundation model for Earth observation that dynamically adapts to heterogeneous EO modalities (RGB, SAR, multispectral, hyperspectral, elevation, infrared) through a single Transformer backbone. It is trained on a newly constructed GeoLangBind-2M dataset using a vision-model-enhanced contrastive training strategy (VECT) and a Modality-aware Knowledge Agglomeration (MaKA) module. The model achieves state-of-the-art zero-shot classification and cross-modal retrieval performance across diverse EO benchmarks, including unseen modalities and sensors.

## setup

Evaluated via zero-shot classification on eleven RGB scene/fine-grained datasets (AID, EuroSAT, fMoW, Million-AID, PatternNet, RESISC45, RSI-CB, SkyScript, roof attribute datasets) and GEO-Bench multispectral datasets (m-bigearthnet, m-so2sat, m-forestnet), plus cross-modal retrieval on RSICD, RSITMD, and UCM-caption, and segmentation ablations on MADOS, m-nz-cattle, and m-NeonTree.

## caveats

Authors note performance decreases slightly on m-so2sat when using five spectral bands due to significantly less multispectral training data compared to RGB, and results on the roof-smoothness attribute remain modest compared to other fine-grained tasks; they also note weight merging uses a simple linear approach, leaving more sophisticated merging strategies for future work.
