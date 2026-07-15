---
arxiv_id: '2607.00638'
authors:
- Max Gaber
- Dimitri Gominski
- Jaime C. Revenga
- Stefan Oehmcke
- Rasmus Fensholt
- Martin Brandt
axes:
- G1_label_rich_parity
- G8_uncertainty
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 5.65
  dataset: CHC
  direction: worse
  id: gaber2026uncertainty#c1
  label_ratio: null
  locator: Table 2
  metric: rmse
  model: prithvi
  span: Prithvi and DOFA achieved the best overall results among the GFMs, with an
    RMSE of 5.90
  span_sha256: 5692eb609db2ae4ad032472c28dfd82ee154d3394aed6c8ac7f82eba59204751
  task: canopy_height_estimation
  value: 5.9
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 5.65
  dataset: CHC
  direction: worse
  id: gaber2026uncertainty#c2
  label_ratio: null
  locator: Table 2
  metric: rmse
  model: dofa
  span: and 5.99 m5.99\text{\,}\mathrm{m}, respectively
  span_sha256: 17f4d2068e45b7619abc626ad23ae58f8d2b3303863b8b17fe8375feaf8ab3c7
  task: canopy_height_estimation
  value: 5.99
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 5.65
  dataset: CHC
  direction: worse
  id: gaber2026uncertainty#c3
  label_ratio: null
  locator: Table 2
  metric: rmse
  model: croma
  span: achieved an RMSE of 5.65
  span_sha256: e30ffa186b9d23fbcbef8822dd75a41dd5271e8c5d842974a5dd788e9b08cf26
  task: canopy_height_estimation
  value: 6.61
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 5.65
  dataset: CHC
  direction: worse
  id: gaber2026uncertainty#c4
  label_ratio: null
  locator: Table 2
  metric: rmse
  model: scalemae
  span: Scale-MAE was inferior to the baseline of a randomly initialized and non-fine-tuned
    ResNet-50 encoder
  span_sha256: 6a4f20321795aea6560898593f99bf42691d7f11c78a5a3a4b874c16f25875dd
  task: canopy_height_estimation
  value: 7.83
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.83
  dataset: CHC
  direction: better
  id: gaber2026uncertainty#c5
  label_ratio: null
  locator: Table 3
  metric: f1
  model: croma
  span: CROMA outperformed the supervised baselines with an F1 score of 0.85
  span_sha256: c9d07bfa6d208fce5bff13d16e82ad7590e12e860f83d048dd4347f27f77bc4d
  task: change_detection
  value: 0.85
date: '2026-07-01'
doi: 10.48550/arxiv.2607.00638
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:34:30.113886Z'
key: gaber2026uncertainty
limitations:
- benchmark_narrowness
- uncertainty
- time_sensitivity
models:
- dofa
- prithvi
- croma
- scalemae
proposed_tags:
- canopy_height_change_regression
- heteroscedastic_regression
- ALS_lidar
- PlanetScope
regions:
- es
self_evaluation: false
tasks:
- canopy_height_estimation
- change_detection
title: Uncertainty-aware tree height change regression
venue: arXiv
---

## summary

The paper introduces the CHC dataset for continuous, uncertainty-aware canopy height change regression in Spain and benchmarks several GFMs against supervised baselines using the PANGAEA framework.

## setup

GFM encoders were frozen and paired with a trainable UPerNet decoder (with LTAE for time series), trained on PlanetScope image time series to predict canopy height change on the CHC dataset (592/262/269 train/val/test tiles), evaluated with RMSE/MAE/R2 and direction-of-change F1.

## caveats

The authors note none of the GFMs could outperform a supervised UNet baseline or the task-specific ECHOSAT product, that fine-grained subpixel structural cues for continuous height change remain challenging for frozen encoders, and that GFMs generally struggle with regression/pixel-level tasks compared to classification.
