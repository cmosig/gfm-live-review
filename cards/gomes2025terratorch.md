---
arxiv_id: '2503.20563'
authors:
- Carlos Gomes
- Benedikt Blumenstiel
- Joao Lucas de Sousa Almeida
- Pedro Henrique de Oliveira
- Paolo Fraccaro
- Francesc Marti Escofet
- Daniela Szwarcman
- Naomi Simumba
- Romeo Kienzler
- Bianca Zadrozny
axes:
- G1_label_rich_parity
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: prithvi
  baseline_value: 88.62
  dataset: Sen1Floods11
  direction: better
  id: gomes2025terratorch#c1
  label_ratio: null
  locator: Table II
  metric: miou
  model: clay
  span: Clay v1 82.43 89.90
  span_sha256: a661f8449d18d8470a8f5f198b019aeb3d865626a448af5e61a5bf8de973974f
  task: flood_mapping
  value: 89.9
- axis: G1_label_rich_parity
  baseline: clay
  baseline_value: 93.09
  dataset: BurnScars
  direction: better
  id: gomes2025terratorch#c2
  label_ratio: null
  locator: Table II
  metric: miou
  model: prithvi
  span: Prithvi-EO-2.0-300M-TL 80.97 89.06 88.17 93.37
  span_sha256: 1be93ebf0505217b433765ae615ca4a93cb4b121d51a67a2fb1beb0b39ba46b0
  task: change_detection
  value: 93.37
date: '2025-03-26'
doi: 10.48550/arxiv.2503.20563
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:50:10.456080Z'
key: gomes2025terratorch
limitations:
- compute_cost
- benchmark_narrowness
models:
- prithvi
- clay
proposed_tags:
- toolkit
- hyperparameter_optimization
- burn_scar_mapping
regions:
- global
self_evaluation: false
tasks:
- flood_mapping
- change_detection
title: 'TerraTorch: The Geospatial Foundation Models Toolkit'
venue: arXiv
---

## summary

TerraTorch is a PyTorch Lightning-based fine-tuning and benchmarking toolkit for geospatial foundation models, integrating a model factory, generic datasets, GEO-Bench, and a Bayesian HPO extension called Iterate.

## setup

As a demonstration, four EO foundation models (DeCUR, Clay v1, Prithvi-EO-1.0, Prithvi-EO-2.0) are fine-tuned via TerraTorch Iterate on Sen1Floods11 (flood segmentation, S2L1C 13 channels) and BurnScars (HLS 6 channels) using a UPerNet decoder, reporting test-set IoU/mIoU from the best of 10 HPO runs.

## caveats

The authors note no single pre-trained architecture perfectly covers all use cases, as performance depends heavily on matching pre-training data to the downstream sensor (e.g., Prithvi models trained on HLS excel on BurnScars but not necessarily elsewhere), and HPO runs vary substantially in compute cost (4h to 46h on an A100-80G).
