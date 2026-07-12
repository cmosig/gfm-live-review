---
arxiv_id: '2409.18536'
authors:
- Jose Sosa
- Mohamed Aloulou
- Danila Rukhovich
- Rim Sleimi
- Boonyarit Changaival
- Anis Kacem
- Djamila Aouada
axes:
- G2_label_scarce_efficiency
- G5_cost
claims:
- axis: G5_cost
  baseline: task_specific
  baseline_value: 0.025
  dataset: Multi-Temporal Cloud Gap Imputation
  direction: better
  id: sosa2024how#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: prithvi
  span: Scratch + hyp ViT-Large 0.025 0.964
  span_sha256: 307ecfafb4bcdefdb825459c0824a8d67cb9704807ed9293e7605b5bf11758dd
  task: representation_probing
  value: 0.02
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 47.42
  dataset: Multi-Temporal Crop Segmentation
  direction: worse
  id: sosa2024how#c2
  label_ratio: null
  locator: Sec 4.2
  metric: miou
  model: prithvi
  span: the average mIoU from 42.0 to 47.42
  span_sha256: 89b980113496d1d90b724474dbbda897a13c5935a20fa60698f1da3c0f911a66
  task: crop_type_mapping
  value: 42.0
- axis: G5_cost
  baseline: task_specific
  baseline_value: 90.16
  dataset: Sen1Floods11
  direction: better
  id: sosa2024how#c3
  label_ratio: null
  locator: Table 4
  metric: miou
  model: prithvi
  span: Scratch + hyp 400 83.11 90.78 90.24 94.72 95.03
  span_sha256: 7d2d9ceff833817a84fa63c7fb50d1069cae79da76e0b6ea11b3752709427a26
  task: flood_mapping
  value: 90.24
- axis: G5_cost
  baseline: task_specific
  baseline_value: 84.84
  dataset: Wildfire Scar Mapping
  direction: better
  id: sosa2024how#c4
  label_ratio: null
  locator: Table 6
  metric: miou
  model: prithvi
  span: Scratch + hyp 100 73.99 85.05 85.41 91.72 93.79
  span_sha256: e6655bc42b0ccd875ea355e6e1b9b30325b81f40194792e78844877d5f9ea650
  task: change_detection
  value: 85.41
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 98.98
  dataset: EuroSAT
  direction: worse
  id: sosa2024how#c5
  label_ratio: null
  locator: Table 7
  metric: accuracy
  model: prithvi
  span: SatMAE Multi Spectral 50 98.98
  span_sha256: 31df73d16b9e60d733a40297c3e9221df92080ffc1af3828ff117df498b90073
  task: land_cover_classification
  value: 98.44
date: '2024-09-27'
doi: 10.48550/arxiv.2409.18536
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:48:14.194413Z'
key: sosa2024how
limitations:
- compute_cost
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- masked_autoencoder
- training_from_scratch
- hyperparameter_tuning
- satmae
- cloud_gap_imputation
- wildfire_scar_mapping
regions:
- global
self_evaluation: false
tasks:
- change_detection
- crop_type_mapping
- flood_mapping
- land_cover_classification
- semantic_segmentation
title: How Effective is Pre-training of Large Masked Autoencoders for Downstream Earth
  Observation Tasks?
venue: arXiv
---

## summary

The paper studies whether pre-training large ViT-based MAEs (Prithvi and SatMAE) actually helps downstream EO tasks compared to training the same architectures from scratch with tuned hyperparameters. Across reconstruction, segmentation, and classification tasks, pre-training only clearly helps when the fine-tuning task closely matches the pre-training task (reconstruction/cloud imputation); for segmentation and classification, training from scratch with hyperparameter tuning matches or beats pre-trained initialisation.

## setup

Experiments use Prithvi's encoder on Multi-Temporal Cloud Gap Imputation, Multi-Temporal Crop Segmentation, Sen1Floods11 flood mapping, and Wildfire Scar Mapping datasets, and SatMAE's encoder on EuroSAT for land cover classification, comparing models initialised from pre-trained weights (Setting 1) against the same architectures trained from scratch with hyperparameter search (Setting 2).

## caveats

The authors note the study is relatively small in scope, covering limited datasets and mostly a single foundation model (Prithvi) plus SatMAE, and call for future work with additional datasets and models, particularly for classification tasks.
