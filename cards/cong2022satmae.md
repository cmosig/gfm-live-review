---
arxiv_id: '2207.08051'
authors:
- Yezhen Cong
- Samar Khanna
- Chenlin Meng
- Patrick Liu
- Erik Rozi
- Yutong He
- Marshall Burke
- David B. Lobell
- Stefano Ermon
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 71.55
  dataset: fMoW RGB
  direction: better
  id: cong2022satmae#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: satmae
  span: SatMAE ViT-Large 65.94/77.84
  span_sha256: a4741035b83a40049f6f2fe936e7d93f24f1eddd7aa44fba05085a3a9977e2ae
  task: land_cover_classification
  value: 77.84
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 74.11
  dataset: fMoW RGB (temporal)
  direction: better
  id: cong2022satmae#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: satmae
  span: SatMAE ViT-Large 81.49/93.26
  span_sha256: e1f162c34f4a8ebc1423eb50260e61452a317c0d2b168694aa2121e9135c6531
  task: land_cover_classification
  value: 81.49
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 54.46
  dataset: fMoW Sentinel
  direction: better
  id: cong2022satmae#c3
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: satmae
  span: Sup. Learning‡ ResNet152 54.46/78.99
  span_sha256: b76ff2d258350a51b5ce2fc320a279150733fffd166f0e77b0d1e8d582bb79ce
  task: land_cover_classification
  value: 61.48
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 57.63
  dataset: NAIP
  direction: better
  id: cong2022satmae#c4
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: satmae
  span: GASSL [34] ResNet50 57.63
  span_sha256: abeb95ec5369f119c62f251ffbb734d29f5c3eb4765e728f8022678228d5ef6f
  task: land_cover_classification
  value: 71.77
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 78.51
  dataset: SpaceNet v1
  direction: worse
  id: cong2022satmae#c5
  label_ratio: null
  locator: Table 7
  metric: miou
  model: satmae
  span: GASSL [34] ResNet50 78.51
  span_sha256: 2746a8d9ccc29d50a5f1f8a8aa8340a922f82525e2fe47229e7f1fab8c0fc29d
  task: semantic_segmentation
  value: 78.07
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 93.14
  dataset: EuroSAT
  direction: better
  id: cong2022satmae#c6
  label_ratio: null
  locator: Table 8
  metric: accuracy
  model: satmae
  span: SeCo [35] ResNet18 93.14
  span_sha256: 62140bbac7ada01ff734763b2ae8cd3f97a3d8e57ca61ec8d2818eb8de7eff38
  task: land_cover_classification
  value: 98.94
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 82.62
  dataset: BigEarthNet
  direction: worse
  id: cong2022satmae#c7
  label_ratio: 0.1
  locator: Table 9
  metric: auc
  model: satmae
  span: SeCo [35] ResNet50 82.62
  span_sha256: 9d30c8edc5c3ba97e7e273c48076d5ce229598c7e2541c8d467f621c54f944db
  task: land_cover_classification
  value: 82.13
date: '2022-07-17'
doi: 10.48550/arxiv.2207.08051
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:23:59.952089Z'
key: cong2022satmae
limitations:
- compute_cost
- temporal_transfer
- data_bias
models:
- satmae
proposed_tags:
- masked_autoencoder
- multi_spectral_encoding
- temporal_positional_encoding
- fMoW_Sentinel_dataset
regions:
- global
self_evaluation: true
tasks:
- land_cover_classification
- semantic_segmentation
- representation_probing
title: 'SatMAE: Pre-training Transformers for Temporal and Multi-Spectral Satellite
  Imagery'
venue: arXiv
---

## summary

SatMAE adapts masked autoencoders to satellite imagery by adding temporal and spectral-group positional encodings and independent masking across time/spectral groups, enabling pre-training on temporal and multi-spectral data. It introduces fMoW-Sentinel, a new Sentinel-2 dataset, and shows strong gains over prior SSL methods (GASSL, SeCo) and supervised baselines on fMoW classification, land cover, segmentation, and multi-label classification tasks.

## setup

Pre-training uses fMoW RGB (temporal and non-temporal) and the newly created fMoW-Sentinel (13-band Sentinel-2) datasets with ViT backbones; downstream evaluation covers fMoW classification, NAIP and EuroSAT land cover, BigEarthNet multi-label classification, and SpaceNet v1 building segmentation.

## caveats

Authors note the increased token sequence length from temporal/spectral inputs strains compute resources, that optimal positional encodings and band groupings remain unexplored, that ViT backbones are harder to finetune from scratch than ResNets, and that geographically imbalanced training data (fMoW skewed toward North America/Europe) could bias the learned representations.
