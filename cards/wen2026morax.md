---
arxiv_id: '2608.17848'
authors:
- Ya Wen
- Jixuan Cai
- Yulun Zhou
- Alec Kirkley
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G11_complementarity
- G12_openness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.361
  dataset: Shanghai NTL
  direction: better
  id: wen2026morax#c1
  label_ratio: null
  locator: Table 1
  metric: r2
  model: alphaearth
  span: AlphaEarth 0.548 0.638 0.508 0.506
  span_sha256: 383500d3ef3b1c3008454b1e10deb7253a773b14135d86c4a6aa83dbf4c51640
  task: urban_signal_mapping
  value: 0.638
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.421
  dataset: NYC Crime
  direction: worse
  id: wen2026morax#c2
  label_ratio: null
  locator: Table 1
  metric: r2
  model: alphaearth
  span: RemoteCLIP 0.168 0.341 0.232 0.271
  span_sha256: 2bf63baab294293c83873496dd4ef10e8dde0e50b45483c7b530da4b0cbb184d
  task: socioeconomic_estimation
  value: 0.179
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.323
  dataset: Shanghai CO2
  direction: better
  id: wen2026morax#c3
  label_ratio: null
  locator: Table 1
  metric: r2
  model: alphaearth
  span: AlphaEarth 0.548 0.638 0.508 0.506
  span_sha256: 383500d3ef3b1c3008454b1e10deb7253a773b14135d86c4a6aa83dbf4c51640
  task: urban_signal_mapping
  value: 0.508
date: '2026-08-18'
doi: 10.48550/arxiv.2608.17848
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-20T00:13:24.559122Z'
key: wen2026morax
limitations:
- benchmark_narrowness
- human_semantics
- spatial_transfer
models:
- alphaearth
proposed_tags:
- human_mobility_augmentation
- feature_wise_modulation
- teacher_student_distillation
- cross_country_transfer
- remoteclip_backbone
regions:
- cn
- us
self_evaluation: false
tasks:
- socioeconomic_estimation
- urban_signal_mapping
title: 'MoRAX: Mobility-based Representation Augmentation for Geospatial Foundation
  Models'
venue: arXiv
---

## summary

MoRAX augments frozen geospatial foundation embeddings (AlphaEarth, RemoteCLIP) with mobility-induced feature-wise modulation via a teacher-student distillation framework, enabling zero-shot deployment with or without target-city mobility data. Across Chinese and US cities, MoRAX-Teacher and MoRAX-Student outperform pretrained GFM embeddings and urban representation baselines on socioeconomic and environmental prediction tasks.

## setup

Trained on five Chinese source cities with observed mobility graphs (WeChat Pay transactions), evaluated zero-shot on Shanghai, Guangzhou, New York City, and Chicago using Ridge regression with five-fold cross-validation on tasks including crime, nighttime light, CO2, PM2.5, check-ins, house price, and income; AlphaEarth embeddings serve as the main geospatial foundation representation, with RemoteCLIP tested for generalization.

## caveats

The authors note larger teacher-student gaps on crime and check-in prediction indicate some fine-grained human interaction patterns are hard to recover without direct mobility access, and mobility data itself is limited to cities with dedicated collection infrastructure, restricting representativeness.
