---
arxiv_id: '2601.08882'
authors:
- Thomas Snyder
- H. Lexie Yang
- Stefan Schnake
- Steffen Schotthöfer
axes:
- G5_cost
- G6_compactness
- G1_label_rich_parity
claims:
- axis: G6_compactness
  baseline: dofa
  baseline_value: 98.13
  dataset: UCM
  direction: worse
  id: snyder2026compressing#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: dofa
  span: '98.13'
  span_sha256: a8c82eb2a98fcda55b584ace7ed3369bc4734952af4edfea510626cf1eef7a32
  task: land_cover_classification
  value: 97.67
date: '2026-01-12'
doi: 10.48550/arxiv.2601.08882
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:43:21.476161Z'
key: snyder2026compressing
limitations:
- compute_cost
- benchmark_narrowness
models: []
proposed_tags:
- model_compression
- low_rank_training
- DLRT
- LoRA
- vision_transformer
- OReole-MR
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
title: Compressing Vision Transformers in Geospatial Transfer Learning with Manifold-Constrained
  Optimization
venue: arXiv
---

## summary

This paper applies dynamical low-rank training (DLRT), a manifold-constrained optimization method, to compress ViT-based geospatial foundation models (ImageNet21k-pretrained ViTs and OReole-MR) during transfer learning on land-cover classification benchmarks. DLRT achieves substantial parameter reduction (64-82%) while preserving accuracy closer to baseline than LoRA. The paper does not evaluate any of the tracked geospatial foundation models.

## setup

Experiments use UCM, AID, and NWPU aerial image classification datasets with small train/validation ratios (50%, 20%, 10% respectively). Models tested are ViT-B16/H14 pretrained on ImageNet-21k and OReole-MR (ViT-B16/H14/G14) self-supervised MAE models, compressed via DLRT vs. LoRA vs. uncompressed baseline during transfer learning, averaged over 10 runs.

## caveats

Authors note OReole-MR models are harder to compress in low-rank format than ImageNet-based models, and that self-supervised pretraining appears less aligned with the low-rank subspace requiring a warm-up epoch; they also flag that accuracy drops more on the more challenging AID/NWPU benchmarks with smaller label ratios.
