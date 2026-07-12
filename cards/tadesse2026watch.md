---
arxiv_id: '2605.08160'
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
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G7_interpretability
- G11_complementarity
claims:
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: WATCH Afghanistan archaeological sites (test split)
  direction: better
  id: tadesse2026watch#c1
  label_ratio: null
  locator: Table II / Abstract
  metric: accuracy
  model: satmae
  span: TED with SatMAE achieves the highest exact-month recall (55% at m=0m{=}0)
  span_sha256: 7f20c5cf84843c38537ec1bf310a35b87e02aa8fab78a4267bd534aa3266bd51
  task: change_detection
  value: 55.0
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 42.5
  dataset: WATCH Afghanistan archaeological sites (test split)
  direction: better
  id: tadesse2026watch#c2
  label_ratio: null
  locator: Sec V-B / Table III
  metric: accuracy
  model: satclip
  span: GeoRSCLIP exceeds Handcrafted by 10 percentage points at m=0m{=}0 under TED
    (52.5% vs. 42.5%)
  span_sha256: 4af91b12e6c2b39db27a9af2c930b4f0f23c57883767a632bb9df060dece6374
  task: change_detection
  value: 52.5
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 15.0
  dataset: WATCH Afghanistan archaeological sites (test split)
  direction: better
  id: tadesse2026watch#c3
  label_ratio: null
  locator: Sec V-B
  metric: accuracy
  model: clay
  span: CLIP nearly doubles Handcrafted recall under SSCD (27.5% vs. 15.0%)
  span_sha256: 8dcecae2d6065b06412696e7a35e10660842cf2d36d076ef983787342ae8f7bf
  task: change_detection
  value: 27.5
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 97.5
  dataset: WATCH Afghanistan archaeological sites (test split)
  direction: worse
  id: tadesse2026watch#c4
  label_ratio: null
  locator: Sec V-B
  metric: accuracy
  model: satclip
  span: Satlas-Pretrain overtakes it from m≥1m{\geq}1 onward and gains 7.5 points
    by m=6m{=}6 (97.5% vs. 90.0%)
  span_sha256: 0bdfb9c3719b9ec03813704f1531c8c55d613b266806c75e823371c19d33e84b
  task: change_detection
  value: 90.0
date: '2026-05-04'
doi: 10.48550/arxiv.2605.08160
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:40:26.962605Z'
key: tadesse2026watch
limitations:
- benchmark_narrowness
- data_bias
- time_sensitivity
- spatial_transfer
models: []
proposed_tags:
- archaeological_site_monitoring
- looting_detection
- temporal_embedding_distance
- self_supervised_change_scoring
- weakly_supervised_temporal_localization
- clip
- georsclip
- satlas_pretrain
- dinov3
- handcrafted_spectral_texture_features
- recall_at_k_temporal_margin
regions:
- af
- sy
- tr
- pk
- eg
self_evaluation: false
tasks:
- change_detection
title: 'WATCH: Wide-Area Archaeological Site Tracking for Change Detection'
venue: arXiv
---

## summary

WATCH is a framework for month-level archaeological looting change detection over PlanetScope satellite mosaics of Afghan sites, comparing six foundation-model embeddings (CLIP, GeoRSCLIP, SatMAE, Prithvi-EO-2.0, DINOv3, Satlas-Pretrain) against handcrafted spectral/texture features using three scoring approaches: training-free TED, self-supervised SSCD, and weakly supervised temporal localization.

## setup

1,943 Afghanistan archaeological sites (898 looted, 1,045 preserved) are represented as monthly PlanetScope embedding time series (2017-2024); recall@K with symmetric and directional temporal margins is evaluated against the 117 sites with known looting months, with additional qualitative cross-regional transfer tests on Syria, Turkey, Pakistan, and Egypt.

## caveats

Authors note reliable month-level ground truth is extremely scarce (only 117 of 898 looted sites), the single-dominant-event-per-site assumption oversimplifies repeated disturbances, global transfer relies on Afghanistan-derived normalization/parameters risking distribution shift, and monthly mosaics may miss short-lived events between acquisitions.
