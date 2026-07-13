---
arxiv_id: '2509.21573'
authors:
- Boyi Chen
- Zhangyu Wang
- Fabian Deuser
- Johann Maximilian Zollner
- Martin Werner
axes:
- G9_ecological_fine_scale
- G3_spatial_transfer
claims:
- axis: G9_ecological_fine_scale
  baseline: geoclip
  baseline_value: 19.8
  dataset: OSV5M
  direction: better
  id: chen2025enhancing#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: geoclip
  span: It achieves 52.1% and 21.5% accuracy at the region (200km) and city level
    (25km)
  span_sha256: 47e0eaef099d991a660423631b5cf1ac64666f9987b66c47f586953eae68bc75
  task: representation_probing
  value: 21.5
- axis: G3_spatial_transfer
  baseline: geoclip
  baseline_value: 50.1
  dataset: OSV5M
  direction: better
  id: chen2025enhancing#c2
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: geoclip
  span: improving upon GeoCLIP’s 50.1% and 19.8%
  span_sha256: 9aba8e967c4fe59fb1eb4797d982432f97232913f87c41815447be4592c8a888
  task: representation_probing
  value: 52.1
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 76.2
  dataset: OSV-5M
  direction: worse
  id: chen2025enhancing#c3
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: geoclip
  span: models like RFM perform 4% better at country level
  span_sha256: f32365bd7d1912b47014568f0cc2c1782b1505f1fbf55b8c647a121ea269549d
  task: representation_probing
  value: 72.1
date: '2025-09-25'
doi: 10.48550/arxiv.2509.21573
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:20:02.741448Z'
key: chen2025enhancing
limitations:
- benchmark_narrowness
- human_semantics
models:
- geoclip
proposed_tags:
- image_geolocalization
- contrastive_learning_reweighting
- semivariogram
- hard_negative_mining
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: Enhancing Contrastive Learning for Geolocalization by Discovering Hard Negatives
  on Semivariograms
venue: arXiv
---

## summary

The paper introduces a semivariogram-based reweighting strategy that models spatial autocorrelation between image embedding distance and geographic distance to better distinguish hard negatives from false negatives in contrastive geo-localization training. Integrated into GeoCLIP and evaluated on OSV5M, it improves city- and region-level retrieval accuracy over the original GeoCLIP while remaining competitive at the country level.

## setup

Evaluated on OpenStreetView-5M (OSV5M), ~5M geo-tagged Mapillary street-view images; a semivariogram is fit between pairwise cosine distances of frozen CLIP image embeddings and haversine distances, then used to reweight GeoCLIP's InfoNCE loss over hard/false negatives; retrieval accuracy measured at 25km, 200km, and 750km thresholds against a GPS gallery.

## caveats

Authors note that while their method achieves the highest city and region level accuracy, other baselines like RFM S2 perform better (4%) at the coarse country level, indicating a trade-off between fine and coarse spatial granularity.
