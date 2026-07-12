---
arxiv_id: '2508.09453'
authors:
- Abdul Matin
- Tanjim Bin Faruk
- Shrideep Pallickara
- Sangmi Lee Pallickara
axes:
- G2_label_scarce_efficiency
- G5_cost
- G11_complementarity
claims:
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 75.42
  dataset: NLCD
  direction: better
  id: matin2025hyperkd#c1
  label_ratio: null
  locator: Table IV
  metric: accuracy
  model: prithvi
  span: Mean 75.42 55.46 75.49 55.62
  span_sha256: 4c71d17877c054f0c95d22ef40d2d8da3aec7842240c9990041103b795c2d33a
  task: land_cover_classification
  value: 75.49
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 55.46
  dataset: NLCD
  direction: better
  id: matin2025hyperkd#c2
  label_ratio: null
  locator: Table IV
  metric: miou
  model: prithvi
  span: Mean 75.42 55.46 75.49 55.62
  span_sha256: 4c71d17877c054f0c95d22ef40d2d8da3aec7842240c9990041103b795c2d33a
  task: land_cover_classification
  value: 55.62
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 67.41
  dataset: CDL
  direction: better
  id: matin2025hyperkd#c3
  label_ratio: null
  locator: Table VI
  metric: accuracy
  model: prithvi
  span: Mean 67.41 41.66 73.27 48.60
  span_sha256: 99dea50398fb7e03195e5a9dde6f57d07fcc13078ce7aa16ed6e4169726a6c3e
  task: crop_type_mapping
  value: 73.27
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 41.66
  dataset: CDL
  direction: better
  id: matin2025hyperkd#c4
  label_ratio: null
  locator: Table VI
  metric: miou
  model: prithvi
  span: Mean 67.41 41.66 73.27 48.60
  span_sha256: 99dea50398fb7e03195e5a9dde6f57d07fcc13078ce7aa16ed6e4169726a6c3e
  task: crop_type_mapping
  value: 48.6
date: '2025-08-13'
doi: 10.48550/arxiv.2508.09453
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:46:53.468904Z'
key: matin2025hyperkd
limitations:
- temporal_transfer
- data_bias
- compute_cost
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- knowledge_distillation
- hyperspectral_imaging
- EnMAP
- masked_autoencoder
- soil_organic_carbon_prediction
- cross_spectral_domain_adaptation
regions:
- us
self_evaluation: false
tasks:
- land_cover_classification
- crop_type_mapping
- representation_probing
title: 'HyperKD: Distilling Cross-Spectral Knowledge in Masked Autoencoders via Inverse
  Domain Shift with Spatial-Aware Masking and Specialized Loss'
venue: arXiv
---

## summary

HyperKD is a knowledge distillation framework that transfers representations from the Prithvi multispectral foundation model (teacher) into a masked-autoencoder student built for EnMAP hyperspectral imagery, using spectral band alignment, spatial-feature-guided masking, and a combined MSE+SSIM+KLD loss. The approach improves reconstruction fidelity over a non-KD student and a baseline KD model, and boosts downstream land cover classification, crop type identification, and soil organic carbon prediction performance.

## setup

EnMAP hyperspectral tiles (224x224, 218 bands after cleaning) from California, later extended to Colorado and Kansas, are used to pretrain a ViT-based masked autoencoder student distilled from Prithvi-100M (trained on 6-band HLS data); downstream evaluation uses NLCD land cover, CDL crop type, and gNATSGO soil organic carbon labels with a frozen encoder plus a CNN head.

## caveats

Authors note NLCD and CDL labels are noisy and imbalanced in the study region, EnMAP's 27-day revisit forces a single-timestamp input versus Prithvi's three-timestamp design, ablations were run on reduced data subsets due to computational constraints, and teacher/student were trained at the same spatial resolution only, leaving cross-resolution generalization for future work.
