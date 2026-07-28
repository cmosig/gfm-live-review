---
arxiv_id: '2607.18504'
authors:
- Frederick Schindlegger
- Kenzo Bounegta
- Eva Gmelich Meijling
- Johannes Jakubik
- Arnt-Børre Salberg
- Theodor Forgaard
- Nicolas Longepe
- Valerio Marsocci
axes:
- G3_spatial_transfer
- G5_cost
- G6_compactness
- G11_complementarity
- G1_label_rich_parity
- G2_label_scarce_efficiency
claims:
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 0.879
  dataset: Sen1Floods11
  direction: better
  id: schindlegger2026now#c1
  label_ratio: 1.0
  locator: Table 12
  metric: miou
  model: prithvi
  span: Sen1Floods11 0.879 0.907 0.910
  span_sha256: c7110a9647f5b84e0d996b5ccfb3470f1f8e07e50282b5245b58e91a8b4e1fd4
  task: flood_mapping
  value: 0.91
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 0.901
  dataset: HLS Burn Scars
  direction: worse
  id: schindlegger2026now#c2
  label_ratio: 1.0
  locator: Table 12
  metric: miou
  model: prithvi
  span: HLS Burn Scars 0.901 0.865 0.891
  span_sha256: 3abe297bf23632f2c91453aa1e83ce610b77ee423e884a73ed94c37ba1fa5f25
  task: land_cover_classification
  value: 0.891
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 0.785
  dataset: CocoaMining
  direction: better
  id: schindlegger2026now#c3
  label_ratio: 1.0
  locator: Table 12
  metric: miou
  model: prithvi
  span: CocoaMining 0.785 0.820 0.817
  span_sha256: e41599f252efc62a62f25c18ab704caf8481b2046624eb4787018c5933a937b7
  task: land_cover_classification
  value: 0.817
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.871
  dataset: Sen1Floods11
  direction: better
  id: schindlegger2026now#c4
  label_ratio: 0.05
  locator: Sec 6.8
  metric: miou
  model: prithvi
  span: it achieves mIoU = 0.888. This is equivalent to what UNet reaches at 50%
  span_sha256: 0cc04467a069f3c4f87c6a4ee0e9df4e71363ef3a1a7f7590d886ca1f5effd3b
  task: flood_mapping
  value: 0.888
- axis: G3_spatial_transfer
  baseline: prithvi
  baseline_value: 0.504
  dataset: Sea Ice
  direction: better
  id: schindlegger2026now#c5
  label_ratio: 1.0
  locator: Table 5
  metric: miou
  model: prithvi
  span: TerraMind Base 0.904 0.828 0.813 0.823 9.190 0.646 0.504
  span_sha256: cb6c7aea77c1ad31865b77fbb6a7ffcd216ac95686fa88bf478d91b1c16e1d17
  task: semantic_segmentation
  value: 0.755
- axis: G6_compactness
  baseline: prithvi
  baseline_value: 0.86
  dataset: Flood Zone
  direction: worse
  id: schindlegger2026now#c6
  label_ratio: 1.0
  locator: Sec 6.1
  metric: f1
  model: prithvi
  span: THOR’s best configuration reaches pixel-wise F1 = 0.86 against TerraMind’s
    best of 0.33
  span_sha256: b84633b589e83a6af67157d18a91b2ae68ccbd392311fb46591afd0f0d9784ed
  task: flood_mapping
  value: 0.33
- axis: G9_ecological_fine_scale
  baseline: prithvi
  baseline_value: 1.037
  dataset: HYPERVIEW
  direction: better
  id: schindlegger2026now#c7
  label_ratio: 1.0
  locator: Sec 6.10.2
  metric: rmse
  model: prithvi
  span: TerraMind at ps4 with full fine-tuning achieves the best RMSE (0.965)
  span_sha256: 3b5e8d1fa6f6c5920b9497d286282cfff3c13247c87f3039abc6f4f669e3572b
  task: crop_yield_estimation
  value: 0.965
date: '2026-07-20'
doi: 10.48550/arxiv.2607.18504
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-28T00:15:36.023523Z'
key: schindlegger2026now
limitations:
- benchmark_narrowness
- compute_cost
- spatial_transfer
- mixed_pixels
- time_sensitivity
models:
- prithvi
- satmae
- scalemae
- croma
- dofa
proposed_tags:
- THOR
- TerraMind
- patch_size_ablation
- decoder_ablation
- Thinking-in-Modalities
- TerraTorch
- PANGAEA_protocol
regions:
- global
- gh
- us
- 'no'
- pl
- gl
self_evaluation: true
tasks:
- flood_mapping
- change_detection
- semantic_segmentation
- land_cover_classification
title: Now We Know? A Systematic Comparison of TerraMind and THOR
venue: arXiv
---

## summary

This paper is a controlled comparative ablation of two ESA-funded geospatial foundation models, THOR and TerraMind, across ten EO use cases, isolating the effects of patch size, decoder complexity, fine-tuning regime, input modality, and model scale rather than producing a single leaderboard.

## setup

Ten use cases (five from FAST-EO, five from FM4CS consortia) spanning segmentation and regression tasks are evaluated under TerraTorch with fixed hyperparameters (PANGAEA-style protocol), varying decoder type (Linear/UperNet/PixelShuffle/MLP), THOR patch size (4/8/16/32), backbone freeze state, input modality, and model scale (Tiny/Base), plus a from-scratch UNet baseline on three FAST-EO datasets.

## caveats

Authors flag single-seed evaluation with gaps under ~1pp potentially non-reproducible, an inherently asymmetric search space favoring THOR's tunable patch size, spatial-fairness confounds from differing input resizing (e.g. CocoaMining), unresolved consortium-provenance confounding pretraining-domain effects, and split-instability/class-imbalance issues on Sea Ice Mapping limiting ranking reliability.
