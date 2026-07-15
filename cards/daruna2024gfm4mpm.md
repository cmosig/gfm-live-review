---
arxiv_id: '2406.12756'
authors:
- Angel Daruna
- Vasily Zadorozhnyy
- Georgina Lukoczki
- Han-Pang Chiu
axes:
- G2_label_scarce_efficiency
- G9_ecological_fine_scale
- G7_interpretability
- G8_uncertainty
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 51.4
  dataset: MVT Lead-Zinc (North America)
  direction: better
  id: daruna2024gfm4mpm#c1
  label_ratio: null
  locator: Table 2
  metric: f1
  model: satmae
  span: WoE 51.4
  span_sha256: 63888ae58529d797bf5b200bcdc886185ebe4ef6d26ddf5b49f95f389bd4608b
  task: representation_probing
  value: 80.3
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 52.1
  dataset: CD Lead-Zinc (Australia)
  direction: better
  id: daruna2024gfm4mpm#c2
  label_ratio: null
  locator: Table 3
  metric: f1
  model: satmae
  span: GBM 52.1
  span_sha256: dad97ebab0a002a3eed3d255b97ee2613889acaf958346d2db653262774e5566
  task: representation_probing
  value: 75.3
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 54.9
  dataset: MVT Lead-Zinc (North America), sparse input
  direction: better
  id: daruna2024gfm4mpm#c3
  label_ratio: null
  locator: Table 4
  metric: f1
  model: satmae
  span: ViT 54.9
  span_sha256: 92cca6a15726be11d8956310ffdb9b24e8fbef2eff2942a9ef862782ebc8f2e0
  task: representation_probing
  value: 79.8
date: '2024-06-18'
doi: 10.48550/arxiv.2406.12756
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:53:09.363729Z'
key: daruna2024gfm4mpm
limitations:
- benchmark_narrowness
- data_bias
- interpretability
- uncertainty
models: []
proposed_tags:
- mineral_prospectivity_mapping
- masked_image_modeling
- positive_unlabeled_learning
- integrated_gradients
- monte_carlo_dropout
regions:
- global
- us
- ca
- au
self_evaluation: false
tasks:
- representation_probing
title: 'GFM4MPM: Towards Geospatial Foundation Models for Mineral Prospectivity Mapping'
venue: arXiv
---

## summary



## setup



## caveats


