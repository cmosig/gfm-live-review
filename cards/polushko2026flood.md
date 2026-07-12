---
arxiv_id: '2606.24120'
authors:
- Vladyslav Polushko
- Tilman Bucher
- Ronald Rösch
- Thomas März
- Markus Rauhut
- Andreas Weinmann
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 90.6
  dataset: BlessemFlood21
  direction: worse
  id: polushko2026flood#c1
  label_ratio: null
  locator: Table I
  metric: miou
  model: prithvi
  span: '89.1'
  span_sha256: 09fc45830f429d81892f6ec50d523835a29978b4da0f11f0e1fea24fd1820cc8
  task: flood_mapping
  value: 89.1
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 95.1
  dataset: BlessemFlood21
  direction: worse
  id: polushko2026flood#c2
  label_ratio: null
  locator: Table I
  metric: f1
  model: prithvi
  span: '94.3'
  span_sha256: efc9c3940668c3b3f0672eccd92aa2321c6dbd5e6d76da064adb4e7878ebe72a
  task: flood_mapping
  value: 94.3
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 99.3
  dataset: BlessemFlood21
  direction: better
  id: polushko2026flood#c3
  label_ratio: null
  locator: Table I
  metric: accuracy
  model: prithvi
  span: '99.6'
  span_sha256: d105f4f09e3cd4d134bca1acd8ead10b5b405650e177b4aa5433b41cf4bc7847
  task: flood_mapping
  value: 99.6
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 93.1
  dataset: NeuenahrFlood
  direction: worse
  id: polushko2026flood#c4
  label_ratio: null
  locator: Table II
  metric: miou
  model: prithvi
  span: '90.3'
  span_sha256: bfff61e0263f63a6d5252b33affe666d3170765585db2c7079f557d6aeb807bb
  task: flood_mapping
  value: 90.3
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 96.4
  dataset: NeuenahrFlood
  direction: worse
  id: polushko2026flood#c5
  label_ratio: null
  locator: Table II
  metric: f1
  model: prithvi
  span: '94.6'
  span_sha256: 9ebe1773ccb4638a8381830535a2a2de97baf15d39ead3ac3c4cf9726e8e0a2a
  task: flood_mapping
  value: 94.6
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 99.1
  dataset: NeuenahrFlood
  direction: better
  id: polushko2026flood#c6
  label_ratio: null
  locator: Table II
  metric: accuracy
  model: prithvi
  span: '99.5'
  span_sha256: b725d20650649a5221675144bab5946e013616d1ba7a25afc394f43e05e82052
  task: flood_mapping
  value: 99.5
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 34.14
  dataset: NeuenahrFlood
  direction: better
  id: polushko2026flood#c7
  label_ratio: null
  locator: Table III
  metric: f1
  model: prithvi
  span: '34.85'
  span_sha256: 180f179d1c241b18888678ea709822d9f80e9e804ff60ff1fad2b3433c87c4fc
  task: flood_mapping
  value: 34.85
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 80.43
  dataset: NeuenahrFlood
  direction: better
  id: polushko2026flood#c8
  label_ratio: 0.095
  locator: Table IV / Sec IV Exp. 3
  metric: f1
  model: prithvi
  span: 91.34 % vs. 80.43 %
  span_sha256: cd0fb945bd52e47b078f980ea395f7093405b0c71914354e4aa4aeacfa791eeb
  task: flood_mapping
  value: 91.34
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 66.81
  dataset: NeuenahrFlood
  direction: better
  id: polushko2026flood#c9
  label_ratio: 0.006
  locator: Table IV
  metric: f1
  model: prithvi
  span: '73.52'
  span_sha256: fd1311687faaed982ca310a3044aaddae606fa51390643c9bb68d08767b5f28b
  task: flood_mapping
  value: 73.52
date: '2026-06-23'
doi: 10.48550/arxiv.2606.24120
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:30:50.868001Z'
key: polushko2026flood
limitations:
- benchmark_narrowness
- spatial_transfer
- data_bias
models:
- prithvi
proposed_tags:
- airborne_RGB_imagery
- UPerNet_decoder
- domain_gap_satellite_to_rgb
- decision_threshold_sensitivity
regions:
- de
self_evaluation: false
tasks:
- flood_mapping
title: Flood Mapping from RGB imagery using a Vision Foundation Model
venue: arXiv
---

## summary

The paper adapts the satellite-pretrained Prithvi-EO-2.0-600M vision foundation model with a UPerNet decoder (Prithvi-2.0-UPN) to binary flood-water segmentation from centimeter-scale airborne RGB imagery. It compares Prithvi-2.0-UPN against CNN/ViT task-specific baselines (DeepLabV3+, UNet++, SegFormer-b5) for in-domain training, zero-shot cross-event transfer, and fine-tuning on small labeled subsets of a second flood event. Prithvi-2.0-UPN matches baseline performance in-domain, outperforms baselines in zero-shot transfer, and reaches near-fully-trained performance fastest when fine-tuned on small data shares.

## setup

Two high-resolution (0.15 m/px) airborne RGB flood datasets, BlessemFlood21 and NeuenahrFlood, are used with 512x512 tiles and pixel-wise water/non-water masks, split 80/20 train/test via water-coverage-stratified sampling. Experiment 1 trains/evaluates each model per dataset; Experiment 2 trains on BlessemFlood21 and evaluates zero-shot on NeuenahrFlood; Experiment 3 fine-tunes the BlessemFlood21-trained model on NeuenahrFlood subsets of 128-2048 tiles, reporting IoU, Dice, and pixel accuracy.

## caveats

The authors note that zero-shot transfer performance, while better than the baselines, still leaves clear room for improvement and remains below in-domain training scores. They also flag that the labeled datasets are small and tied to individual flood events, and state future work should include further ablation studies, robustness analysis, and investigation of automatic parameter adaptation.
