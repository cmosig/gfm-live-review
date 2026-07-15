---
arxiv_id: '2604.02719'
authors:
- Mirali Purohit
- Bimal Gajera
- Irish Mehta
- Bhanu Tokas
- Jacob Adler
- Steven Lu
- Scott Dickenshied
- Serina Diniega
- Brian Bue
- Umaa Rebbapragada
- Hannah Kerner
axes:
- G3_spatial_transfer
- G5_cost
- G1_label_rich_parity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: Boulder
  direction: worse
  id: purohit2026momo#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: 0.04 ±\pm 0.051
  span_sha256: af33feea7fe906e13ccc7216b32f1cd1a963125c6946953da86f5357e042778f
  task: semantic_segmentation
  value: 0.04
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: MMLS
  direction: worse
  id: purohit2026momo#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: croma
  span: 0.14 ±\pm 0.014
  span_sha256: c0f79e3d6b09666baa60f8e00afed7879db54c26cb0fa68ac3debc4058f7728c
  task: semantic_segmentation
  value: 0.14
date: '2026-04-03'
doi: 10.48550/arxiv.2604.02719
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:54:48.010324Z'
key: purohit2026momo
limitations:
- compute_cost
- benchmark_narrowness
models:
- satmae
- croma
- prithvi
proposed_tags:
- mars_orbital
- model_merging
- checkpoint_selection
- task_arithmetic
- planetary_science
- multi_sensor
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- landslide_susceptibility
title: 'MOMO: Mars Orbital Model Foundation Model for Mars Orbital Applications'
venue: arXiv
---

## summary

MOMO is the first foundation model for Mars orbital remote sensing, pre-trained on ~12M samples from HiRISE, CTX, and THEMIS sensors, and merged via a novel Equal Validation Loss checkpoint-selection strategy before task-arithmetic fusion. It is evaluated against ImageNet pre-training, several Earth-observation foundation models, sensor-specific pre-training, and other merging strategies on 9 Mars-Bench downstream tasks, showing particularly strong gains on segmentation.

## setup

Three sensor-specific ViT-Base masked autoencoders are pre-trained independently on HiRISE, CTX, and THEMIS Mars orbital imagery, then merged using EVL-aligned checkpoints via task arithmetic; evaluation uses 9 Mars-Bench classification and segmentation tasks (AtmosDust, DoMars16k, Frost, Landmark, Boulder, ConeQuest, Crater Binary, Crater Multi, MMLS) with weighted F1 for classification and mIoU for segmentation.

## caveats

The authors note they did not include additional model-merging baselines due to computational constraints, did not explore alignment-based techniques that could further improve performance, and their method assumes linear mode connectivity between models, which may not hold when models are trained on highly divergent data distributions.
