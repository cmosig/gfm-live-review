---
arxiv_id: '2510.09894'
authors:
- Junyuan Liu
- Quan Qin
- Guangsheng Dong
- Xinglei Wang
- Jiazhuang Feng
- Zichao Zeng
- Tao Cheng
axes:
- G10_human_semantics
- G11_complementarity
- G12_openness
- G7_interpretability
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: satclip
  baseline_value: 0.122
  dataset: NLUD (Verisk National Land Use Database)
  direction: better
  id: liu2025beyond#c1
  label_ratio: null
  locator: Table 1
  metric: f1
  model: alphaearth
  span: 'AlphaEarth


    55.9 ±\pm 1.5'
  span_sha256: 3ad7193cb8b7ab4a6c2cf0d8a2c3d737c3689e442d1853599e4814f3a3f7d4ad
  task: land_cover_classification
  value: 0.559
- axis: G1_label_rich_parity
  baseline: satclip
  baseline_value: 0.317
  dataset: downscaled gridded global GDP per capita (PPP) (2020)
  direction: better
  id: liu2025beyond#c2
  label_ratio: null
  locator: Table 2
  metric: r2
  model: alphaearth
  span: 'AlphaEarth


    64.0 ±\pm 2.8'
  span_sha256: a040cc706ed7dc5826aded3fbe2657ee7d154cd75d28a09e8b743546beab720b
  task: socioeconomic_estimation
  value: 0.706
date: '2025-10-10'
doi: 10.48550/arxiv.2510.09894
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:51:03.303594Z'
key: liu2025beyond
limitations:
- data_bias
- spatial_transfer
- benchmark_narrowness
models:
- alphaearth
- satclip
proposed_tags:
- poi_guided_alignment
- contrastive_learning
- natural_language_spatial_retrieval
- urban_representation_learning
- multimodal_alignment
- language_accessible_embeddings
- gdp_mapping
- land_use_distribution_mapping
regions:
- gb
- sg
self_evaluation: false
tasks:
- land_cover_classification
- socioeconomic_estimation
- representation_probing
title: 'Beyond AlphaEarth: Toward Human-Centered Geospatial Foundation Models via
  POI-Guided Contrastive Learning'
venue: arXiv
---

## summary

AETHER adapts frozen AlphaEarth EO embeddings for human-centered urban analysis by aligning them with POI text embeddings via multimodal contrastive learning. Across four urban tasks in Greater London and Singapore it outperforms EO, POI, and coordinate baselines (including AlphaEarth and SatCLIP) with relative improvements of 4.5%-21.9%. The aligned space also enables natural language-conditioned spatial retrieval of urban functions.

## setup

Frozen 10m AlphaEarth embeddings are pooled in multi-scale windows around POIs and aligned to OpenAI text-embedding-3-large POI text via InfoNCE, then a lightweight MLP head is trained per task (land-use classification, socioeconomic/land-use distribution mapping, GDP regression) over five random seeds. Baselines include Random, LDA, Place2Vec, Doc2Vec, SPPE, Space2Vec, CaLLiPer, SatCLIP, and AlphaEarth.

## caveats

Authors note POI data have strong spatial heterogeneity and uneven cross-city/country coverage that may affect alignment stability, that the study covers only two metropolitan regions with cross-city/global scaling left to future work, that other modalities (street imagery, mobility) are not yet incorporated, and that the language-retrieval evaluation is only an initial demonstration.
