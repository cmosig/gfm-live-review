---
arxiv_id: '2509.01910'
authors:
- Furong Jia
- Lanxin Liu
- Ce Hou
- Fan Zhang
- Xinyan Liu
- Yu Liu
axes:
- G7_interpretability
- G1_label_rich_parity
- G10_human_semantics
claims:
- axis: G1_label_rich_parity
  baseline: geoclip
  baseline_value: 10.8
  dataset: Im2GPS3k
  direction: better
  id: jia2025towards#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: geoclip
  span: GeoCLIP 10.8 31.1 48.7 67.6 83.2 Ours 13.2 34.0 49.8 68.2 83.5
  span_sha256: c8bf2be1adabb54573873b6b14e9e89eea2f335c8242856104a969f802cfab8b
  task: representation_probing
  value: 13.2
- axis: G10_human_semantics
  baseline: geoclip
  baseline_value: 0.4983
  dataset: Median income
  direction: better
  id: jia2025towards#c2
  label_ratio: null
  locator: Table 2
  metric: r2
  model: geoclip
  span: Median income USA 0.5468 0.4983
  span_sha256: f55d35a42289004dee088c9292feb06bb236de99787d59a2b6a970e283d78a96
  task: socioeconomic_estimation
  value: 0.5468
- axis: G10_human_semantics
  baseline: geoclip
  baseline_value: 62.01
  dataset: iNaturalist
  direction: better
  id: jia2025towards#c3
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: geoclip
  span: iNaturalist Global 65.94 62.01
  span_sha256: 29a9c64b2efc2d8dfc1e96e69d1c244aab924934a1682ab3b59660e67d5b2b94
  task: representation_probing
  value: 65.94
- axis: G10_human_semantics
  baseline: geoclip
  baseline_value: 0.7257
  dataset: Air temperature
  direction: better
  id: jia2025towards#c4
  label_ratio: null
  locator: Table 2
  metric: r2
  model: geoclip
  span: Air temperature Global 0.7538 0.7257
  span_sha256: c37bb0421314832713467ae00a38912971a69f629afbe0de2c60f0d536ab9143
  task: representation_probing
  value: 0.7538
date: '2025-09-02'
doi: 10.48550/arxiv.2509.01910
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:20:20.263321Z'
key: jia2025towards
limitations:
- interpretability
- benchmark_narrowness
models:
- geoclip
proposed_tags:
- image_geolocalization
- concept_bottleneck_model
- geo_localization_accuracy_by_distance_threshold
regions:
- us
- global
self_evaluation: false
tasks:
- representation_probing
- socioeconomic_estimation
title: 'Towards Interpretable Geo-localization: a Concept-Aware Global Image-GPS Alignment
  Framework'
venue: arXiv
---

## summary

The paper introduces a Concept-Aware Alignment Module built on top of GeoCLIP that projects image and location embeddings into an interpretable geography-driven concept subspace, improving both geo-localization accuracy and interpretability. It evaluates on Im2GPS3k and several downstream geospatial prediction tasks derived from location embeddings.

## setup

Trained on a 5% subset of MP-16 (from YFCC100M) using contrastive image-GPS alignment plus a concept-space divergence loss; evaluated on Im2GPS3k for geo-localization and on downstream tasks (income, education, country classification, air temperature, species classification) using MLPs on the learned location/image embeddings.

## caveats

Authors note that concept activation values do not directly indicate causal influence on predictions, only correlation/reliance strength; the concept set relies on manual refinement and LLM-based enrichment which could introduce bias or incompleteness.
