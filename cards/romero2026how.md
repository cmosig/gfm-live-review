---
arxiv_id: '2606.13896'
authors:
- Julia Romero
- Qin Lv
- Morteza Karimzadeh
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G6_compactness
- G7_interpretability
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 86.12
  dataset: Sen1Floods11
  direction: better
  id: romero2026how#c1
  label_ratio: 1.0
  locator: Table 5
  metric: miou
  model: prithvi
  span: '88.90'
  span_sha256: 5a013be83829d599b2334851fcf9841fdf4bfa6261da9b0d2ad244116d36975c
  task: semantic_segmentation
  value: 88.9
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 23.87
  dataset: PASTIS
  direction: better
  id: romero2026how#c2
  label_ratio: 0.1
  locator: Table 5
  metric: miou
  model: croma
  span: '38.61'
  span_sha256: 9aa5eb68ade96bd3f6e5208e4d74ba53490c43c631300504a312631c63997295
  task: crop_type_mapping
  value: 38.61
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 80.66
  dataset: Sen1Floods11
  direction: better
  id: romero2026how#c3
  label_ratio: 0.1
  locator: Table 5
  metric: miou
  model: prithvi
  span: '83.95'
  span_sha256: 78690b82433bd028b5eaeefa28ae22080caf9daa3e1595060e422460f5a0de8e
  task: flood_mapping
  value: 83.95
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 40.95
  dataset: PASTIS
  direction: better
  id: romero2026how#c4
  label_ratio: 0.1
  locator: Table 5
  metric: miou
  model: croma
  span: '43.31'
  span_sha256: b45af66b87c4b1cbaa1aab670a0bdc1494559efff53ea1bc33cf05eb1a553054
  task: crop_type_mapping
  value: 43.31
date: '2026-06-11'
doi: 10.48550/arxiv.2606.13896
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:35:09.489552Z'
key: romero2026how
limitations:
- benchmark_narrowness
- compute_cost
- mixed_pixels
- interpretability
- data_bias
models:
- prithvi
- croma
proposed_tags:
- layerwise_linear_probing
- CKA_representation_shift
- decoder_design
- SSL_pretraining_objective
- fine_tuning_vs_frozen
- ImageNet_baseline
regions:
- global
- fr
self_evaluation: false
tasks:
- crop_type_mapping
- flood_mapping
- land_cover_classification
- semantic_segmentation
- biomass_estimation
- representation_probing
title: How do Self-Supervised Remote Sensing Vision Models Transfer to Downstream
  Tasks?
venue: arXiv
---

## summary

The paper benchmarks six SSL geospatial foundation models (MoCo, MAE, DINO, Prithvi, CROMA, TerraMind) against each other and an ImageNet ViT-B/16 baseline across classification, regression, and segmentation tasks under varying label availability and adaptation strategies. Model rankings shift substantially across tasks, and layerwise probing shows task-relevant information is often more accessible in intermediate transformer blocks than final layers. CKA analysis reveals fine-tuning induces model-specific, depth-localized representation shifts concentrated in the first MLP linear layer.

## setup

Six SSL GeoFMs (MoCo, MAE, DINO from SSL4EO; Prithvi v1, CROMA, TerraMind) are evaluated on EuroSAT (classification), NeuCo-Bench (regression), and PANGAEA-Bench segmentation datasets (HLSBurnScars, Sen1Floods11, MADOS, AI4SmallFarms) plus case studies on PASTIS and Sen1Floods11 with varying decoder designs, frozen vs fine-tuned encoders, and label ratios (10%/100%). Layerwise linear probes and CKA similarity analysis characterize how representations evolve across ViT block depth and change under fine-tuning.

## caveats

Authors note GeoFM rankings are highly inconsistent across tasks and adaptation settings, standard multi-scale decoders (UPerNet) may be poorly matched to how GeoFMs organize information over depth, larger pretraining scale (e.g., TerraMind at 2B params) does not consistently translate to better performance, and a supervised ImageNet baseline remains competitive after fine-tuning, especially on Sen1Floods11, indicating current downstream transfer pipelines may not align well with GeoFM representations.
