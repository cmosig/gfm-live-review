---
arxiv_id: '2602.19608'
authors:
- Girmaw Abebe Tadesse
- Titien Bartette
- Andrew Hassanali
- Allen Kim
- Jonathan Chemla
- Andrew Zolli
- Yves Ubelmann
- Caleb Robinson
- Inbal Becker-Reshef
- Juan Lavista Ferres
axes:
- G1_label_rich_parity
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.926
  dataset: Afghanistan looted sites (PlanetScope, 2023 imagery)
  direction: worse
  id: tadesse2026satellite#c1
  label_ratio: null
  locator: Table 3 / Sec 6.1
  metric: f1
  model: satclip
  span: SatCLIP-V+RF+Mean, i.e., location and vision embeddings fed into a Random
    Forest with mean-based temporal aggregation
  span_sha256: 001d1910963edc66c9c83aff648d62bb85ce9e243ae3cb7156a9d690c97f6632
  task: representation_probing
  value: 0.71
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.69
  dataset: Afghanistan looted sites (PlanetScope, 2023 imagery)
  direction: worse
  id: tadesse2026satellite#c2
  label_ratio: null
  locator: Table 3
  metric: f1
  model: satmae
  span: SatMAE + GB + Concat
  span_sha256: cce22acf09f7b26b50d6efafa8a18b9f88d8d352d7a46025b018fc404f5b4417
  task: representation_probing
  value: 0.565
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.69
  dataset: Afghanistan looted sites (PlanetScope, 2023 imagery)
  direction: better
  id: tadesse2026satellite#c3
  label_ratio: null
  locator: Table 3
  metric: f1
  model: satclip
  span: Handcrafted + XGB + PCA
  span_sha256: 33477412dcbcafd40a303090fe1f96de9a6fccda91663dcee663ee31404e2094
  task: representation_probing
  value: 0.71
date: '2026-02-23'
doi: 10.48550/arxiv.2602.19608
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T19:06:45.002192Z'
key: tadesse2026satellite
limitations:
- benchmark_narrowness
- spatial_transfer
- human_semantics
- time_sensitivity
models:
- satmae
- satclip
proposed_tags:
- archaeological_looting_detection
- handcrafted_spectral_texture_features
- GLCM
- SHAP_feature_importance
- spatial_masking
- PlanetScope
- GeoRSCLIP
- DINOv3
- SatlasPretrain
- CNN_transfer_learning
regions:
- af
self_evaluation: false
tasks:
- representation_probing
title: Satellite-Based Detection of Looted Archaeological Sites Using Machine Learning
venue: arXiv
---

## summary

This paper builds a satellite-based CNN and traditional-ML pipeline to detect looted archaeological sites in Afghanistan using PlanetScope imagery, comparing ImageNet-pretrained CNNs, handcrafted spectral/texture features, and embeddings from several remote-sensing foundation models (SatMAE, SatCLIP, GeoRSCLIP, DINOv3, Prithvi-EO 2.0, Satlas-Pretrain). ImageNet-pretrained CNNs with spatial masking (best: ResNet-50, F1=0.926) substantially outperform the best foundation-model-embedding pipeline (SatCLIP-V+RF+Mean, F1=0.710), which itself performs only comparably to handcrafted features. The authors conclude that looting signatures are highly localized and texture-based, favoring end-to-end learned representations over off-the-shelf geospatial embeddings.

## setup

1,943 archaeological sites in Afghanistan (898 looted, 1,045 preserved), PlanetScope RGB+NIR monthly mosaics at 4.7m/pixel from 2016-2023, with manually annotated spatial footprint masks; stratified 70/10/20 site-level train/val/test split with 5-fold cross-validation, evaluated primarily on 2023 imagery.

## caveats

Authors note the study focuses on a single country (Afghanistan) and performance may not generalize to different geology, land use, or imaging conditions; PlanetScope's 4.7m/pixel resolution can miss very small disturbances and monthly compositing can smooth short-lived events; temporal label noise exists since labels reflect December 2023 status while earlier-year imagery may show sites still appearing intact.
