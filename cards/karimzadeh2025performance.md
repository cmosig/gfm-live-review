---
arxiv_id: '2505.18461'
authors:
- Morteza Karimzadeh
- Zhongying Wang
- James L. Crooks
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.73
  dataset: AQS PM2.5 (WR random split)
  direction: better
  id: karimzadeh2025performance#c1
  label_ratio: null
  locator: Table 2
  metric: r2
  model: geoclip
  span: GeoCLIP Location Embeddings (Hadamard)
  span_sha256: 495788031904e9de9535148f133b570a9c49714c6ea7df847cec1c152e4a9bc3
  task: socioeconomic_estimation
  value: 0.79
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.62
  dataset: AQS PM2.5 (WR spatial split)
  direction: better
  id: karimzadeh2025performance#c2
  label_ratio: null
  locator: Table 3
  metric: r2
  model: geoclip
  span: GeoCLIP Location Embeddings
  span_sha256: a7191f05916469c5475d2357b9f62dd04ff9c8b61390c6cc1f4ab5ef9a68c8ac
  task: socioeconomic_estimation
  value: 0.67
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 7.43
  dataset: AQS PM2.5 checkerboard delta=30 (West->East)
  direction: better
  id: karimzadeh2025performance#c3
  label_ratio: null
  locator: Sec 3.3
  metric: rmse
  model: geoclip
  span: a lower average RMSE of 6.90 (vs. 7.43
  span_sha256: 524b8170bead8f72dbce0f3f047d83ff2d6c7db7c9697db1388d8b6595e70b90
  task: socioeconomic_estimation
  value: 6.9
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.59
  dataset: AQS PM2.5 checkerboard delta=8
  direction: better
  id: karimzadeh2025performance#c4
  label_ratio: null
  locator: Table 4
  metric: r2
  model: geoclip
  span: GeoCLIP Location Embeddings
  span_sha256: a7191f05916469c5475d2357b9f62dd04ff9c8b61390c6cc1f4ab5ef9a68c8ac
  task: socioeconomic_estimation
  value: 0.6
- axis: G11_complementarity
  baseline: satclip
  baseline_value: 0.68
  dataset: AQS PM2.5 (WR random split)
  direction: better
  id: karimzadeh2025performance#c5
  label_ratio: null
  locator: Table 2
  metric: r2
  model: geoclip
  span: SatCLIP Location Embeddings (Hadamard)
  span_sha256: b22264a214efcfccbd09c2252ee28c8656feb2d990d36b6c2c9f04cba1e8f9f5
  task: socioeconomic_estimation
  value: 0.79
date: '2025-05-24'
doi: 10.48550/arxiv.2505.18461
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T19:07:08.584818Z'
key: karimzadeh2025performance
limitations:
- spatial_transfer
- data_bias
- time_sensitivity
- uncertainty
- benchmark_narrowness
models:
- geoclip
- satclip
proposed_tags:
- pm2.5_estimation
- location_encoder
- geolocation_features
- bi_lstm_attention
- within_region_vs_out_of_region
regions:
- us
self_evaluation: false
tasks:
- socioeconomic_estimation
title: Performance and Generalizability Impacts of Incorporating Location Encoders
  into Deep Learning for Dynamic PM2.5 Estimation
venue: arXiv
---

## summary

The paper evaluates three ways of incorporating geolocation (none, raw/sinusoidal coordinates, pretrained location encoders) into a Bi-LSTM+Attention PM2.5 estimation model, finding GeoCLIP embeddings improve both within-region and out-of-region performance while raw coordinates hurt out-of-region generalization. The authors also compare GeoCLIP and SatCLIP in an ablation, finding GeoCLIP generally outperforms SatCLIP for this task.

## setup

Base model is a Bi-LSTM with Luong attention predicting daily surface PM2.5 across CONUS for 2021 using AOD, meteorology, wildfire smoke, elevation, NDVI, KNN-IDW PM2.5, temporal encodings, and geolocation variants (none, lat/lon, sinusoidal lat/lon, or frozen GeoCLIP/SatCLIP embeddings fused via Hadamard or concatenation). Evaluation uses within-region random/spatial holdouts and out-of-region checkerboard partitioning at multiple degree widths, plus a case study on the 2021 Dixie Fire.

## caveats

Authors note GeoCLIP embeddings introduce speckle/noise artifacts in rural or topographically complex areas due to high-frequency Fourier positional encoding and sparse/uneven Flickr pretraining coverage; GeoCLIP-enhanced model still underpredicts PM2.5 in smoke-affected areas due to static embeddings that cannot reflect evolving fire behavior; and at the largest checkerboard partition (delta=16 degrees) the no-geolocation model outperformed GeoCLIP in one partition, showing diminishing benefits under extreme spatial disjointness.
