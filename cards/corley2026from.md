---
arxiv_id: '2603.02080'
authors:
- Isaac Corley
- Caleb Robinson
- Inbal Becker-Reshef
- Juan M. Lavista Ferres
axes:
- G3_spatial_transfer
- G6_compactness
claims:
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: EuroSAT
  direction: better
  id: corley2026from#c1
  label_ratio: null
  locator: Sec 5
  metric: accuracy
  model: alphaearth
  span: 'AEF: 91.0%, Tessera: 94.4%'
  span_sha256: d80d9661e219129b646cf4755d361482dca88657c2c22749211c21b64e52e7ff
  task: land_cover_classification
  value: 91.0
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: EuroSAT
  direction: better
  id: corley2026from#c2
  label_ratio: null
  locator: Sec 5
  metric: accuracy
  model: tessera
  span: 'AEF: 91.0%, Tessera: 94.4%'
  span_sha256: d80d9661e219129b646cf4755d361482dca88657c2c22749211c21b64e52e7ff
  task: land_cover_classification
  value: 94.4
date: '2026-03-02'
doi: 10.48550/arxiv.2603.02080
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:44:34.668760Z'
key: corley2026from
limitations:
- benchmark_narrowness
models:
- alphaearth
- tessera
proposed_tags:
- pooling_strategies
- mean_pooling
- covariance_pooling
- stats_pooling
- fixed_embedding_products
- pixel_to_patch_aggregation
- zonal_statistics
- input_label_resolution_mismatch
- EuroSAT-Embed
- olmoearth
- generalization_gap
regions: []
self_evaluation: false
tasks:
- land_cover_classification
- representation_probing
title: 'From Pixels to Patches: Pooling Strategies for Earth Embeddings'
venue: arXiv
---

## summary

The paper studies post-hoc pooling of fixed pixel-level GFM embedding products into patch-level representations, releasing EuroSAT-Embed derived from AlphaEarth, OlmoEarth, and Tessera. It benchmarks 11 training-free pooling methods plus 2 fitted baselines under random and geographically disjoint splits, finding that distributional statistics (stats, covariance) cut the spatial generalization gap by over 50% and improve spatial-split accuracy by up to ~6% versus mean pooling. It recommends mean as a baseline, stats (4×) as the default, and covariance for peak accuracy.

## setup

EuroSAT-Embed provides aligned pixel embeddings from AlphaEarth (64-d), OlmoEarth-Nano (128-d), and Tessera (128-d) over the 10-class EuroSAT Sentinel-2 land-cover dataset. Thirteen pooling methods are evaluated with kNN (k=5, cosine) and multinomial logistic-regression probes under the standard random split and a longitude-based geographically disjoint spatial split.

## caveats

The authors evaluate on only a single benchmark (EuroSAT, 10 classes) with three embedding sources, noting broader datasets like BigEarthNet/fMoW and multi-label settings would strengthen conclusions. They study only training-free pooling and state their guidance applies to post-hoc pooling of fixed embedding products, not end-to-end learned aggregation with encoder access.
