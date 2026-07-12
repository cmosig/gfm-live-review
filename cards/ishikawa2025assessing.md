---
arxiv_id: '2508.18829'
authors:
- Takayuki Ishikawa
- Carmelo Bonannella
- Bas J. W. Lerink
- Marc Rußwurm
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G9_ecological_fine_scale
- G11_complementarity
- G12_openness
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 69.48
  dataset: SIMB
  direction: better
  id: ishikawa2025assessing#c1
  label_ratio: null
  locator: Sec 5.2
  metric: accuracy
  model: presto
  span: achieved an overall accuracy of 73.02% (±1.55)
  span_sha256: d391f251d2e2bb92da3bf7b5ca5201a6ceae8c33042161ee5f03751bf34a6659
  task: land_cover_classification
  value: 73.02
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 51.03
  dataset: SIMB
  direction: better
  id: ishikawa2025assessing#c2
  label_ratio: null
  locator: Sec 5.2
  metric: f1
  model: presto
  span: an F1 macro score of 57.60% (±1.74)
  span_sha256: 388a5cacc5e915cddb79c9b7e9ddbd5b5001244820a8b384985db66a647aca62
  task: land_cover_classification
  value: 57.6
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 62.8
  dataset: COMB
  direction: better
  id: ishikawa2025assessing#c3
  label_ratio: null
  locator: Sec 5.2
  metric: accuracy
  model: presto
  span: reached 65.91% (±1.72) overall accuracy
  span_sha256: 58f8437210f4d73aa9559560db0e96c2bdaff61f8b9fc201a84cc016b6599597
  task: land_cover_classification
  value: 65.91
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 38.95
  dataset: COMB
  direction: better
  id: ishikawa2025assessing#c4
  label_ratio: null
  locator: Sec 5.2
  metric: f1
  model: presto
  span: 46.11% (±3.00) F1 macro
  span_sha256: 71baecabbd137f3b37e1217bbd7085a7fe60a1b8d3229f82f8c507fb8395b9aa
  task: land_cover_classification
  value: 46.11
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 84.47
  dataset: SIBA
  direction: better
  id: ishikawa2025assessing#c5
  label_ratio: null
  locator: Sec 5.2
  metric: accuracy
  model: presto
  span: achieved 93.37% (±0.69) accuracy
  span_sha256: 9a995e254fc0c25aadf3cecb6914e8ae1b885bcb0b203aeea6d98d3076128be2
  task: land_cover_classification
  value: 93.37
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 84.4
  dataset: SIBA
  direction: better
  id: ishikawa2025assessing#c6
  label_ratio: null
  locator: Sec 5.2
  metric: f1
  model: presto
  span: 93.33% (±0.69) F1 macro
  span_sha256: 43115394aab98ef640da052fa5d874f9b5e3af1109a84cfe5df7f6d436940501
  task: land_cover_classification
  value: 93.33
date: '2025-08-26'
doi: 10.48550/arxiv.2508.18829
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:02:30.701546Z'
key: ishikawa2025assessing
limitations:
- spatial_transfer
- temporal_transfer
- benchmark_narrowness
- interpretability
- data_bias
models:
- presto
- tessera
- alphaearth
proposed_tags:
- tree_species_classification
- national_forest_inventory
- fine_tuning
- frozen_vs_finetuned_embeddings
- harmonic_medoid_features
- random_forest
- class_imbalance
- spatial_autocorrelation
- sentinel-1_sentinel-2_fusion
regions:
- nl
self_evaluation: false
tasks:
- land_cover_classification
- representation_probing
title: Assessing the Effectiveness of Deep Embeddings for Tree Species Classification
  in the Dutch Forest Inventory
venue: arXiv
---

## summary

The paper evaluates deep pre-trained remote sensing embeddings (Presto, Tessera, AlphaEarth) against hand-crafted harmonic + medoid features with Random Forest/MLP classifiers for Dutch NFI tree species classification. Fine-tuned Presto embeddings consistently outperform the state-of-the-art hand-crafted features by roughly 2-9 percentage points across three datasets of varying difficulty. The lightweight open Presto model, despite its small size, gives the best results, especially in the small-label regime.

## setup

Three Dutch National Forest Inventory datasets (COMB: 13 classes/1,462 samples; SIMB: 7 classes/1,479; SIBA: 7 balanced classes/13,790) with Sentinel-1/2, ERA5, and SRTM time series from 2020 extracted via Google Earth Engine. Models compared with RF (500 trees) and a 3-layer MLP under a 70/30 train-test split repeated over five random seeds, reporting overall accuracy and macro/weighted F1.

## caveats

Authors note embeddings come from models pre-trained on a limited temporal/spatial range (2020-2021 global), that data derive exclusively from Dutch NFI and may not generalize to other bioclimatic zones, residual spatial autocorrelation (15 m may be insufficient vs recommended 45 m), class imbalance strongly driving performance, limited interpretability of deep features, hyperparameter sensitivity, and inherent limits discriminating species with overlapping phenology.
