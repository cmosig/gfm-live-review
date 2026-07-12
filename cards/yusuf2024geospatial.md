---
arxiv_id: '2403.06860'
authors:
- Ibrahim Salihu Yusuf
- Mukhtar Opeyemi Yusuf
- Kobby Panford-Quainoo
- Arnu Pretorius
axes:
- G1_label_rich_parity
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 75.76
  dataset: UN-FAO Locust Hub / HLS
  direction: better
  id: yusuf2024geospatial#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: prithvi
  span: achieving the highest accuracy, F1 and ROC-AUC scores (83.03%, 81.53% and
    87.69%, respectively)
  span_sha256: fcb56effcaac1fdb2e5918e9515f29e25e6a0e1abc78bf3ab07309c024cac407
  task: landslide_susceptibility
  value: 83.03
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 67.34
  dataset: UN-FAO Locust Hub / HLS
  direction: better
  id: yusuf2024geospatial#c2
  label_ratio: null
  locator: Table 2
  metric: f1
  model: prithvi
  span: It achieved an accuracy, F1-score, and ROC-AUC score of 75.76%, 67.34%, and
    63.61%
  span_sha256: b9ac3d8c0658b4180e1b22927519e96062790696b0708c7618dfd5952010d2bf
  task: landslide_susceptibility
  value: 81.53
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 63.61
  dataset: UN-FAO Locust Hub / HLS
  direction: better
  id: yusuf2024geospatial#c3
  label_ratio: null
  locator: Table 2
  metric: auc
  model: prithvi
  span: It achieved an accuracy, F1-score, and ROC-AUC score of 75.76%, 67.34%, and
    63.61%
  span_sha256: b9ac3d8c0658b4180e1b22927519e96062790696b0708c7618dfd5952010d2bf
  task: landslide_susceptibility
  value: 87.69
date: '2024-03-11'
doi: 10.48550/arxiv.2403.06860
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:50:06.759089Z'
key: yusuf2024geospatial
limitations:
- data_bias
- time_sensitivity
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- desert_locust_breeding_prediction
- species_distribution_modeling
- pseudo_absence_generation
regions:
- global
self_evaluation: false
tasks:
- landslide_susceptibility
title: A Geospatial Approach to Predicting Desert Locust Breeding Grounds in Africa
venue: arXiv
---

## summary

The paper curates a desert-locust breeding-ground dataset from UN-FAO observations and compares classical models, custom deep spatio-temporal architectures (PLAN-LB, Conv3D, ConvLSTM) on remotely-sensed features against a fine-tuned Prithvi foundation model on HLS multi-spectral imagery. Prithvi-LB, fine-tuned on HLS chips, achieved the best accuracy, F1, and ROC-AUC scores, outperforming all custom deep learning and classical baselines.

## setup

Binary classification of breeding vs non-breeding locations using UN-FAO Locust Hub records (2020-2023) with pseudo-absence sampling; remotely-sensed environmental/climate variables (TerraClimate, SoilGrid, Copernicus land cover, ALOS elevation) feed classical and custom deep models, while NASA HLS multi-spectral imagery (30m, 3 temporal steps) feeds a fine-tuned Prithvi encoder with a custom segmentation decoder.

## caveats

Authors note many samples were lost to missing values during preprocessing of remotely-sensed variables, and low update frequency of those variable sources limits suitability for operational deployment; predictions have not yet been ground-truthed and the authors plan future field verification with UN-FAO.
