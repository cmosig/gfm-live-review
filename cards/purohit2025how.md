---
arxiv_id: '2501.12535'
authors:
- Mirali Purohit
- Gedeon Muhawenayo
- Esther Rolf
- Hannah Kerner
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G1_label_rich_parity
claims:
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: 0.68
  dataset: CropHarvest
  direction: better
  id: purohit2025how#c1
  label_ratio: null
  locator: Table 1
  metric: f1
  model: presto
  span: 0.71 ±plus-or-minus\pm± 0.02
  span_sha256: aac5ba6a497cf75eda9bec2367abac370a42e818118fa316de68fc22a5cea420
  task: crop_type_mapping
  value: 0.71
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: 0.66
  dataset: EcoRegions
  direction: better
  id: purohit2025how#c2
  label_ratio: null
  locator: Table 1
  metric: f1
  model: satclip
  span: 0.78 ±plus-or-minus\pm± 0.01
  span_sha256: c4e66fcb2e0d9078c39c7a528d241846482fe9b8561837d74f26e5722ac54a0e
  task: representation_probing
  value: 0.78
date: '2025-01-21'
doi: 10.48550/arxiv.2501.12535
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:51:17.999969Z'
key: purohit2025how
limitations:
- benchmark_narrowness
- data_bias
- spatial_transfer
models:
- presto
- satclip
proposed_tags:
- pretraining_data_composition
- geographic_sampling_strategy
- continent_wise_finetuning
regions:
- global
self_evaluation: false
tasks:
- crop_type_mapping
- representation_probing
title: How Does the Spatial Distribution of Pre-training Data Affect Geospatial Foundation
  Models?
venue: arXiv
---

## summary

The paper studies how the geographic distribution of pre-training data affects two GFMs, Presto and SatCLIP, evaluated on CropHarvest (crop vs. non-crop classification) and EcoRegions (biome classification) respectively. Across five pre-training data sampling strategies plus a zero-pretraining baseline, balanced/globally representative sampling (UAR, stratified continent, stratified biome) generally outperforms clustered sampling (Natural Forest, World Cities) in few-shot continent-wise finetuning. Performance differences between compositions shrink as finetuning data increases, and the relative ranking of sampling strategies depends on model architecture.

## setup

Two GFMs (Presto pixel-timeseries model, SatCLIP location encoder) were each pre-trained from scratch on five data compositions (UAR, Stratified Continent, Stratified Biome, Natural Forest, World Cities) plus a zero-pretraining baseline, then finetuned on continent-wise subsets (Africa, Asia, Europe, North America, Oceania, South America) of CropHarvest (Presto) and EcoRegions (SatCLIP) using n=100 few-shot samples, repeated 50 times with parametric and non-parametric classifiers (MLP, logistic regression, Random Forest, KNN).

## caveats

Authors note the study covers only two GFMs and one downstream task per GFM, uses continent-level (not country-level) groupings due to insufficient country-level sample sizes, does not explore intentionally biased sampling for regional specialization, and does not investigate the separate effect of pre-training data quantity.
