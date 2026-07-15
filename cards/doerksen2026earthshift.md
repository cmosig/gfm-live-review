---
arxiv_id: '2605.29330'
authors:
- Kelsey Doerksen
- Hannah Kerner
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G1_label_rich_parity
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 16.39
  dataset: FTW Germany-Cambodia
  direction: better
  id: doerksen2026earthshift#c1
  label_ratio: null
  locator: Table 12
  metric: miou
  model: galileo
  span: Germany-Cambodia
  span_sha256: 8f0c8715f24387a65cefaf0b9ba061bccc9855bba459eaa6ec411eb171f14697
  task: crop_type_mapping
  value: 17.21
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 36.23
  dataset: FTW Germany-Denmark
  direction: worse
  id: doerksen2026earthshift#c2
  label_ratio: null
  locator: Table 12
  metric: miou
  model: croma
  span: Germany-Denmark
  span_sha256: 52c7305bfcad834f1471ed6066511d749a8a8b104f0fb9e2b8ceedba4211fdc0
  task: crop_type_mapping
  value: 35.21
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 52.89
  dataset: FTW Germany Year-to-Year
  direction: better
  id: doerksen2026earthshift#c3
  label_ratio: null
  locator: Table 13
  metric: miou
  model: dofa
  span: Germany Year-to-Year
  span_sha256: 9dc790b6e4b4003c75a5646045a691d60bc2a01ccd5be2b08f00aa080e033470
  task: crop_type_mapping
  value: 53.36
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 36.83
  dataset: Sen1Floods11 S2-S1
  direction: worse
  id: doerksen2026earthshift#c4
  label_ratio: null
  locator: Table 14
  metric: miou
  model: prithvi
  span: Sen1Floods11 S2 - S1
  span_sha256: 9422f341349c806f42e5c4e9cadbef881f6a8f1dc068b475cbf18581fabf8793
  task: flood_mapping
  value: 7.96
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 86.41
  dataset: RESISC45-UCMerced
  direction: worse
  id: doerksen2026earthshift#c5
  label_ratio: null
  locator: Table 10
  metric: accuracy
  model: dofa
  span: RESISC45-UCMerced
  span_sha256: 392417612b2124c24447a9ed8c4e8db0835e166477553614e20a774640604d5e
  task: land_cover_classification
  value: 34.19
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 53.19
  dataset: DeepGlobe-DFC2022
  direction: worse
  id: doerksen2026earthshift#c6
  label_ratio: null
  locator: Table 11
  metric: miou
  model: croma
  span: DeepGlobe-DFC2022
  span_sha256: 4529ccdd47d01c7f2a7c9ccffa95cd82e2dd96e180ba37c7f875e022355c9a6f
  task: semantic_segmentation
  value: 32.63
date: '2026-05-28'
doi: 10.48550/arxiv.2605.29330
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:36:20.468284Z'
key: doerksen2026earthshift
limitations:
- benchmark_narrowness
- spatial_transfer
- temporal_transfer
models:
- dofa
- croma
- prithvi
- galileo
proposed_tags:
- distributional_robustness
- effective_robustness
- scale_shift
- sensor_shift
- data_source_shift
regions:
- de
- za
- kh
- dk
- global
self_evaluation: false
tasks:
- crop_type_mapping
- land_cover_classification
- flood_mapping
- semantic_segmentation
- representation_probing
title: 'EarthShift: a benchmark for measuring robustness to real-world distribution
  shifts in Earth observation'
venue: arXiv
---

## summary

EarthShift is a benchmark testbed measuring distributional robustness of geospatial foundation models (GFMs), generic vision foundation models, and fully-supervised models across five real-world distribution shift types (scale, temporal, geographic, sensor, source) spanning 11 tasks. The paper finds GFMs show no robustness advantage over generic vision models or even randomly-initialized supervised baselines, with models losing 15-20% performance out-of-distribution on average regardless of architecture, size, or pre-training strategy. Models are notably robust to temporal shifts but fragile to sensor and scale shifts.

## setup

Models are fine-tuned on in-distribution (ID) data and evaluated on both an ID held-out test set and an out-of-distribution (OOD) test set drawn from paired datasets (e.g., RESISC45-UCMerced, FTW country/season subsets, BigEarthNetv2 S2-S1, Sen1Floods11 S2-S1, DeepGlobe-DFC2022) under full fine-tuning and frozen-backbone protocols across 5 random seeds. Effective robustness (Taori et al. 2020) is computed as OOD score minus a linear-regression-predicted baseline from ID score, evaluated over 8 GFMs, several VFMs, and randomly-initialized ResNet50/ViT models.

## caveats

The authors note EarthShift does not include an exhaustive analysis of distribution shifts across all task scenarios, limiting broad claims about robustness in general without a more extensive experiment suite, though they argue additional datasets are unlikely to change findings given consistent trends across models and tasks.
