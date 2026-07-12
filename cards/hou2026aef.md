---
arxiv_id: '2606.20697'
authors:
- Shuyang Hou
- Ziqi Liu
- Haoyue Jiao
- Lutong Xie
- Yaxian Qing
- Xiaopu Zhang
- Qingyang Xu
- Zhangyan Xu
- Xuefeng Guan
- Huayi Wu
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G5_cost
- G6_compactness
- G10_human_semantics
- G11_complementarity
claims:
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: CHN-Econ
  direction: worse
  id: hou2026aef#c1
  label_ratio: null
  locator: Abstract; Table 7
  metric: r2
  model: alphaearth
  span: AEF achieves R² values of only 0.301 for cross-region and 0.160 for cross-tier
    evaluation.
  span_sha256: 5b7810532c9b40ade20b80232d6775d15f87849bd0bd70848fd2c1f361f660f2
  task: representation_probing
  value: 0.301
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: CHN-Econ
  direction: worse
  id: hou2026aef#c2
  label_ratio: null
  locator: Abstract; Table 7
  metric: r2
  model: alphaearth
  span: AEF achieves R² values of only 0.301 for cross-region and 0.160 for cross-tier
    evaluation.
  span_sha256: 5b7810532c9b40ade20b80232d6775d15f87849bd0bd70848fd2c1f361f660f2
  task: representation_probing
  value: 0.16
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: CHN-Econ
  direction: worse
  id: hou2026aef#c3
  label_ratio: null
  locator: Sec 4.2.1; Table 7
  metric: r2
  model: alphaearth
  span: reaches only 0.461 on E1, compared with 0.635 for BL1
  span_sha256: e02c34cd9054f0a4721b951ef21d896467be52974356fbe473d3e7edfb65485b
  task: representation_probing
  value: 0.635
date: '2026-06-15'
doi: null
doi_status: no_doi_found
extractor_version: '1'
ingested_at: '2026-07-12T16:44:31.279594Z'
key: hou2026aef
limitations:
- human_semantics
- spatial_transfer
- benchmark_narrowness
models:
- alphaearth
proposed_tags:
- capacity_adaptive_reconstruction
- multi_source_self_supervised_fusion
- cross_lingual_poi_text_embedding
- nighttime_lights
- points_of_interest
- urban_morphology
- housing_price_estimation
- cross_tier_generalization
- embedding_dimension_compression
- functional_zone_retrieval
- socioeconomic_foundation_embedding
- inter_stream_capacity_competition
regions:
- cn
self_evaluation: true
tasks:
- land_cover_classification
- population_density
- urban_signal_mapping
- wealth_mapping
- socioeconomic_estimation
- representation_probing
title: 'AEF-Econ: Toward Plug-and-Play Socioeconomic Foundation Embeddings from AlphaEarth
  for Urban Remote Sensing'
venue: arXiv
---

## summary

The authors build AEF-Econ, a socioeconomic foundation embedding that fuses AlphaEarth (AEF) embeddings with six socioeconomic data streams via multi-source self-supervised learning and a proposed Capacity-Adaptive Reconstruction (CAR) mechanism. Evaluated by linear probing on their CHN-Econ benchmark (16 labels, 36 Chinese cities, eight years), AEF alone yields weak cross-region/cross-tier R² (0.301/0.160), which their full framework raises to 0.848/0.693. They release 256d/128d/64d embedding products and validate them with self-diagnostics and urban case studies.

## setup

CHN-Econ benchmark: 36 mainland-China cities over 2017–2024, 14.4M pixel-year samples, seven training streams (AEF, population, NTL, RS indices, POIs, urban morphology, cross-lingual POI text) and 16 downstream labels. Embedding quality is assessed by linear probes (RidgeCV regression, logistic-regression classification, cosine retrieval) under three splits: within-city (E1), cross-region (E2), and leave-one-tier-out cross-tier (E3).

## caveats

The authors note cross-domain generalization remains limited (E3 housing-price R² only 0.317, indicating pixel-scale compression cannot fully capture some signals), experiments were run at a single 100 m resolution rather than native 10 m or coarser scales, and AEF's pretraining lacks socioeconomic semantics so its embeddings underperform on socioeconomic tasks without auxiliary signals.
