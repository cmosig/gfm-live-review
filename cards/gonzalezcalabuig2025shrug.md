---
arxiv_id: '2511.10370'
authors:
- Maria Gonzalez-Calabuig
- Kai-Hendrik Cohrs
- Vishal Nedungadi
- Zuzanna Osika
- Ruben Cartuyvels
- Steffen Knoblauch
- Joppe Massant
- Shruti Nath
- Patrick Ebel
- Vasileios Sitokonstantinou
axes:
- G8_uncertainty
- G3_spatial_transfer
- G7_interpretability
claims:
- axis: G8_uncertainty
  baseline: task_specific
  baseline_value: null
  dataset: ExEBench
  direction: better
  id: gonzalezcalabuig2025shrug#c1
  label_ratio: null
  locator: Table 2
  metric: auc
  model: presto
  span: SHRUG-FM (Ours) 0.160 ±\pm 0.045
  span_sha256: 166f3d2dae5c92d535b33f2f27ef3feb0eb0f82f5634baf16c5ae12f50bef8c3
  task: change_detection
  value: 0.16
- axis: G8_uncertainty
  baseline: task_specific
  baseline_value: null
  dataset: WorldFloods
  direction: better
  id: gonzalezcalabuig2025shrug#c2
  label_ratio: null
  locator: Sec 5.1
  metric: auc
  model: presto
  span: the framework achieves the lowest overall Area Under the Risk-Coverage Curve
    (AURC) of 0.115
  span_sha256: 38555d041e0edf709d877b32c35d789ecc48720d90fd63a049d2e2468e12944f
  task: flood_mapping
  value: 0.115
date: '2025-11-13'
doi: 10.48550/arxiv.2511.10370
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:44:30.858376Z'
key: gonzalezcalabuig2025shrug
limitations:
- compute_cost
- data_bias
- uncertainty
- interpretability
- spatial_transfer
- benchmark_narrowness
models: []
proposed_tags:
- selective_prediction
- out_of_distribution_detection
- risk_coverage_curve
- SSL4EO-S12
- ensemble_uncertainty
- glass_box_decision_tree
- reliability_flagging
regions:
- global
- us
self_evaluation: false
tasks:
- change_detection
- flood_mapping
- landslide_susceptibility
- semantic_segmentation
title: 'SHRUG-FM: Reliability-Aware Foundation Models for Earth Observation'
venue: arXiv
---

## summary



## setup



## caveats


