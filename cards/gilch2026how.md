---
arxiv_id: '2603.10658'
authors:
- Luis Gilch
- Isabelle Wittmann
- Maximilian Nitsche
- Johannes Jakubik
- Arne Ewald
- Thomas Brunschwiler
axes:
- G1_label_rich_parity
- G6_compactness
- G7_interpretability
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: SSL4EO-S12-downstream (Biomass Mean)
  direction: better
  id: gilch2026how#c1
  label_ratio: null
  locator: Sec 4.2
  metric: r2
  model: prithvi
  span: 0.50 on Biomass Mean and 0.69 on Clouds
  span_sha256: b4b96d442cb2d2665b95636ec7a2479cadc4163602b65ec0589da2e478a87a5c
  task: biomass_estimation
  value: 0.53
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: -0.2
  dataset: SSL4EO-S12-downstream (Clouds)
  direction: better
  id: gilch2026how#c2
  label_ratio: null
  locator: Sec 4.2
  metric: r2
  model: prithvi
  span: 0.50 on Biomass Mean and 0.69 on Clouds
  span_sha256: b4b96d442cb2d2665b95636ec7a2479cadc4163602b65ec0589da2e478a87a5c
  task: representation_probing
  value: 0.69
date: '2026-03-11'
doi: 10.48550/arxiv.2603.10658
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:41:14.728678Z'
key: gilch2026how
limitations:
- benchmark_narrowness
- uncertainty
models: []
proposed_tags:
- embedding_design
- spatial_pooling
- layer_depth_analysis
- SSL_objective_comparison
- embedding_concatenation
- ResNet_vs_ViT
- TerraMind
- NeuCo-Bench
regions:
- global
self_evaluation: false
tasks:
- representation_probing
- biomass_estimation
- crop_type_mapping
- land_cover_classification
title: 'How to Embed Matters: Evaluation of EO Embedding Design Choices'
venue: arXiv
---

## summary

This paper systematically evaluates how embedding design choices—backbone architecture, pretraining SSL objective, spatial pooling, intermediate-layer depth, and representation concatenation—affect downstream performance of frozen GeoFM embeddings using the NeuCo-Bench benchmark. It finds transformer backbones with mean pooling are strong defaults, intermediate ResNet layers can outperform final layers, SSL objectives show task-specific strengths, and concatenating embeddings from different objectives improves robustness.

## setup

Embeddings are extracted from frozen SSL4EO-pretrained ResNet-50 and ViT-Small backbones (various SSL objectives: DINO, MoCo, DECUR, SoftCon, MAE, FGMAE) plus TerraMind ViT-Small, evaluated via linear probing on eight regression tasks from the SSL4EO-S12-downstream dataset (biomass, crops, clouds, land-cover, heat island) using 50 repeated train/test splits, measured with R2 and the NeuCo-Bench Quality Score.

## caveats

Authors note regression targets, especially continuous biophysical variables, contain inherent label uncertainty limiting absolute performance; benchmark tasks are limited to NeuCo-Bench's fixed set (land cover, biomass, clouds, heat island), and linear probing on 1D embeddings constrains downstream model complexity, isolating representation quality but not reflecting full end-to-end fine-tuning performance.
