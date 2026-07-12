---
arxiv_id: '2404.19609'
authors:
- Denys Godwin
- Hanxi Li
- Michael Cecil
- Hamed Alemohammad
axes:
- G2_label_scarce_efficiency
- G9_ecological_fine_scale
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.032
  dataset: HLS CONUS cloud imputation dataset
  direction: better
  id: godwin2024seeing#c1
  label_ratio: 1.0
  locator: Table 1
  metric: rmse
  model: prithvi
  span: 6231 0.949 0.919 0.960 0.937 0.024 0.033 0.022 0.032
  span_sha256: 22ccf774f488b06cf7b556e7fe6d52e973619427c6667e84e284eeec021bcc2e
  task: representation_probing
  value: 0.022
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.045
  dataset: HLS CONUS cloud imputation dataset
  direction: better
  id: godwin2024seeing#c2
  label_ratio: 0.0642
  locator: Table 1
  metric: rmse
  model: prithvi
  span: 400 0.947 0.894 0.956 0.912 0.025 0.045 0.024 0.045
  span_sha256: 2a861b641edfe69cb1f23c5f4237640c4bede7047aac2a43cc52a99c44f31937
  task: representation_probing
  value: 0.024
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: HLS CONUS cloud imputation dataset
  direction: better
  id: godwin2024seeing#c3
  label_ratio: null
  locator: Sec 4
  metric: rmse
  model: prithvi
  span: Zero-shot inference by Prithvi achieves an MAE of 0.03 on all masked pixels
    in the validation
  span_sha256: 4f380a33373b0a54e76f8b61519ccaa8c687e81819ae801586cbe90f9c621b13
  task: representation_probing
  value: 0.03
date: '2024-04-30'
doi: 10.48550/arxiv.2404.19609
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:49:26.726046Z'
key: godwin2024seeing
limitations:
- benchmark_narrowness
- time_sensitivity
- mixed_pixels
models:
- prithvi
proposed_tags:
- cloud_gap_imputation
- missing_data_imputation
- CGAN_baseline
regions:
- us
self_evaluation: false
tasks:
- representation_probing
title: 'Seeing Through the Clouds: Cloud Gap Imputation with Prithvi Foundation Model'
venue: arXiv
---

## summary

The paper fine-tunes the Prithvi geospatial foundation model to impute cloud-masked pixels in HLS multispectral time series and compares it against a Conditional GAN trained from scratch. Across nearly all sample sizes and both single-scene and multi-scene masking experiments, Prithvi achieves lower MAE and higher SSIM than the CGAN, including outperforming a fully-trained CGAN in zero-shot mode.

## setup

7,852 cloud-free HLS chips (224x224px, 6 bands, 3 time steps) from CONUS in 2022 were masked with real cloud masks and split into 6,231 training / 1,621 validation chips, with training subsets of 3200/1600/800/400 also tested; two masking configurations were used (middle scene only vs. all time steps), and models were evaluated via MAE and SSIM on validation chips.

## caveats

Authors note reconstructed pixels are only a 'best guess' not true values, Prithvi discards entire patches containing any cloudy pixel (losing usable information), fine-tuning shows unstable loss spikes and collapses to suboptimal local minima, and SSIM values are not adjusted for cloud coverage, limiting cross-experiment comparability.
