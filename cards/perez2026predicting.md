---
arxiv_id: '2607.08449'
authors:
- Jorge Ignacio Perez
- Hwaai Kang Kee
- Lucas Rassbach
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G4_temporal_transfer
- G11_complementarity
claims:
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 66.25
  dataset: AgriPotential
  direction: better
  id: perez2026predicting#c1
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: prithvi
  span: Ensemble (U-Net + Prithvi)
  span_sha256: 4e5d94a90d6795470657559a0d9186df18717360f98ccff3d441db1ec44c8249
  task: crop_type_mapping
  value: 68.32
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 66.25
  dataset: AgriPotential
  direction: worse
  id: perez2026predicting#c2
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: prithvi
  span: U-Net and Prithvi models achieving 66.25% and 65.51%
  span_sha256: 44f1f7c532bf92f38446192957c658e65db78a8d318919998db4c8dc7930f274
  task: crop_type_mapping
  value: 65.51
date: '2026-07-09'
doi: 10.48550/arxiv.2607.08449
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:06:03.268811Z'
key: perez2026predicting
limitations:
- benchmark_narrowness
- data_bias
- spatial_transfer
- temporal_transfer
- compute_cost
models:
- prithvi
proposed_tags:
- viticulture_potential
- ordinal_classification
- teacher_student_pseudo_labeling
- ensemble_learning
- U-Net
regions:
- fr
self_evaluation: false
tasks:
- crop_type_mapping
title: Predicting Viticulture Potential through an Ensemble of U-Net and a Geospatial
  Foundation Model
venue: arXiv
---

## summary

The DS@GT ARC team tackled ImageCLEF AI4Agri 2026 Subtask 1 (viticulture potential prediction on Sentinel-2 imagery) with an ensemble of a U-Net trained on stacked multi-temporal channels and a finetuned Prithvi-EO-2.0 foundation model on seasonal-aggregated inputs, combined via weighted logit ensembling with U-Net-generated pseudo-labels for unlabeled pixels. The ensemble achieved 68.32% ±1 test accuracy, ranking 2nd of 7 teams, outperforming the standalone U-Net (66.25%) and Prithvi (65.51%). Explicit temporal modeling (Prithvi and other transformer architectures like TSViT, U-TAE, Swin-V2, Presto) underperformed the simpler channel-stacking U-Net approach, contradicting the authors' initial hypothesis.

## setup

AgriPotential dataset: 34-timestep multispectral Sentinel-2 patches (128x128, 10 bands) from Southern France (2017-2019), labeled 1-5 for viticulture potential with ~50-60% labeled pixels per patch; 6329 train / 781 val / 800 test patches. Models trained with ordinal (binary cross-entropy) loss on labeled pixels, evaluated via ±1 and exact accuracy, with test accuracy reported from the public leaderboard.

## caveats

Authors note a persistent generalization gap between validation and test accuracy across all models, especially the transformer-based ones, with the cause (overfitting vs. distribution shift) undetermined; larger Prithvi variants (300M) increased train-validation gap without improving test performance, suggesting overfitting; ensemble improvements were inconsistent across patches and could inherit errors from both models.
