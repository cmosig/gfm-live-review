---
arxiv_id: '2507.22291'
authors:
- Christopher F. Brown
- Michal R. Kazmierski
- Valerie J. Pasquarella
- William J. Rucklidge
- Masha Samsikova
- Chenhui Zhang
- Evan Shelhamer
- Estefania Lahera
- Olivia Wiles
- Simon Ilyushchenko
- Noel Gorelick
- Lihui Lydia Zhang
- Sophia Alj
- Emily Schechter
- Sean Askay
- Oliver Guinan
- Rebecca Moore
- Alexis Boukouvalas
- Pushmeet Kohli
axes:
- G2_label_scarce_efficiency
- G6_compactness
- G5_cost
- G4_temporal_transfer
- G11_complementarity
claims:
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: OpenET ensemble
  direction: better
  id: brown2025alphaearth#c1
  label_ratio: null
  locator: Sec 6
  metric: r2
  model: alphaearth
  span: achieving R2=0.58±0.01R^{2}=0.58\pm 0.01
  span_sha256: 639cfece8c31c5c93901a83c36a19da45d97d25a18b2787f6196d4056e80c520
  task: hydrological_modeling
  value: 0.58
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: 72.0
  dataset: LCMAP land cover change
  direction: better
  id: brown2025alphaearth#c2
  label_ratio: null
  locator: Sec 7
  metric: balanced_accuracy
  model: alphaearth
  span: achieving 78.4%±1.1178.4\%\pm 1.11 balanced accuracy (BA) (linear)
  span_sha256: ec9eb11c4c15a500346ab11d20d2e20a4186fc852d32e5931b9775addff8f82a
  task: change_detection
  value: 78.4
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: null
  dataset: LCMAP land use change
  direction: better
  id: brown2025alphaearth#c3
  label_ratio: null
  locator: Sec 7
  metric: balanced_accuracy
  model: alphaearth
  span: 79.3%±1.6779.3\%\pm 1.67 BA (kNN, k=3)
  span_sha256: e799f37e6b658f33555e1e311dc0ab00b49f73daed9ab1e8d60b7408af960e52
  task: change_detection
  value: 79.3
date: '2025-07-29'
doi: null
doi_status: no_doi_found
extractor_version: '1'
ingested_at: '2026-07-12T16:33:46.916817Z'
key: brown2025alphaearth
limitations:
- benchmark_narrowness
models:
- alphaearth
- satclip
- prithvi
- clay
proposed_tags:
- embedding_field_model
- continuous_time_modeling
- MOSAIKS
- CCDC_harmonics
- evapotranspiration_estimation
- surface_emissivity
- low_shot_transfer
- global_annual_embeddings
- multi_source_fusion
- tree_genera_classification
- oil_palm_plantation_mapping
regions:
- us
- ca
- et
- global
self_evaluation: true
tasks:
- land_cover_classification
- crop_type_mapping
- change_detection
- semantic_segmentation
- hydrological_modeling
title: 'AlphaEarth Foundations: An embedding field model for accurate and efficient
  global mapping from sparse label data'
venue: arXiv
---

## summary

AlphaEarth Foundations (AEF) is a geospatial embedding field model that fuses multi-source, multi-temporal Earth observation data into compact 64-byte, 10m-resolution annual embeddings supporting continuous time. Across 15 evaluations spanning classification, regression, and change detection, AEF consistently outperforms designed (composites, CCDC, MOSAIKS) and learned (SatCLIP, Prithvi, Clay) featurization baselines without retraining, reducing error magnitudes by ~23.9% on average in the max-trial setting. The authors release global annual embedding fields (2017-2024) and the evaluation suite under an open license.

## setup

The authors built a suite of 15 evaluations from 11 openly available datasets (LCMAP, LUCAS, GLaNCE, Africa/Canada/Ethiopia crops, US trees, Descals oil palm, OpenET, ASTER GED), balancing samples per class and testing low-shot (n=1, 10, max) transfer via kNN and linear probes. AEF is compared against controls (XY, XYZ, ViT), designed features (composites, CCDC, MOSAIKS), and learned models (SatCLIP, Prithvi, Clay) with identical inputs where applicable, reporting Balanced Accuracy for classification/change and R2 for regression.

## caveats

The authors flag that adequate 1-shot and 10-shot performance remains an unsolved research frontier given extreme variability (error reductions >1.0x for only 8/15 and 5/15 evaluations respectively), that Ethiopia crops is particularly challenging due to sparsity and fine scale, that US trees requires ~100x more observations than SatCLIP because AEF receives no coordinate information, that unsupervised change detection did not beat baselines for land use change, and that regression evaluations involve small sample sizes.
