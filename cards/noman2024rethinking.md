---
arxiv_id: '2403.05419'
authors:
- Mubashir Noman
- Muzammal Naseer
- Hisham Cholakkal
- Rao Muhammad Anwar
- Salman Khan
- Fahad Shahbaz Khan
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: fMoW-RGB
  direction: better
  id: noman2024rethinking#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: satclip
  span: SatMAE++ (Ours)
  span_sha256: da6ab586905b0dc7010dd99a2037afe8e534e25d329e350b887abe32443a92e0
  task: land_cover_classification
  value: 78.14
date: '2024-03-08'
doi: 10.48550/arxiv.2403.05419
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:23:37.046466Z'
key: noman2024rethinking
limitations:
- benchmark_narrowness
- compute_cost
models: []
proposed_tags:
- multi-scale-pretraining
- masked-autoencoder
- SatMAE++
- fMoW-RGB
- fMoW-Sentinel
- BigEarthNet
- EuroSAT
- RESISC-45
- UC-Merced
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- representation_probing
title: Rethinking Transformers Pre-training for Multi-Spectral Satellite Imagery
venue: arXiv
---

## summary

SatMAE++ rethinks transformer pre-training for multi-spectral satellite imagery by reconstructing masked images at multiple scale levels using convolutional upsampling blocks, avoiding the complex GSD-based positional encodings of ScaleMAE. It works for both optical (fMoW-RGB) and multi-spectral (fMoW-Sentinel) data and sets new state-of-the-art results across six datasets.

## setup

Pre-training on fMoW-RGB and fMoW-Sentinel using ViT-Large with masked autoencoding at 2-3 scale levels; downstream evaluation via finetuning on EuroSAT, RESISC-45, UC-Merced (land cover classification) and BigEarthNet (multi-label classification, 10% training data).

## caveats

The authors note their approach struggles in some cases to reconstruct fine-grained structural details, and observe diminishing returns from adding more scale levels (only 0.37% gain going from two to three scales).
