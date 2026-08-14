---
arxiv_id: '2608.12271'
authors:
- Pedro Sousa
- Will Tebbutt
- Sadiq Jaffer
- Robin Young
- Anil Madhavapeddy
- Richard E. Turner
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G7_interpretability
- G9_ecological_fine_scale
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 1.67
  dataset: GHCNh Europe
  direction: better
  id: sousa2026earth#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: tessera
  span: ConvCNP with Tessera 1.10 1.58 0.79
  span_sha256: b28129ecd0457f2f244e0c35ab316ffe0513f5ccc2b04dbb9d81b2dd8cef16a0
  task: representation_probing
  value: 1.58
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 1.87
  dataset: GHCNh East Asia
  direction: better
  id: sousa2026earth#c2
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: tessera
  span: ConvCNP with Tessera 1.10 1.53 0.79
  span_sha256: 1bd1451bedd6a2f8d7db9e10fb41ede12d18efa9f15f3914541a3929ee5d0049
  task: representation_probing
  value: 1.53
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 2.1
  dataset: GHCNh All regions
  direction: better
  id: sousa2026earth#c3
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: tessera
  span: ConvCNP with Tessera 1.32 1.90 0.96
  span_sha256: b912c1621c8ea82e7f930988b532ccc71134b5aa4f9c29b3258cc218a7906780
  task: representation_probing
  value: 1.9
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 1.69
  dataset: Norwegian probe stations (wind speed, cold start)
  direction: better
  id: sousa2026earth#c4
  label_ratio: null
  locator: Sec 3.5
  metric: rmse
  model: tessera
  span: ConvCNP with Tessera is 16.7%16.7\% better before a single Norwegian probe
    is deployed (1.411.41 against 1.69
  span_sha256: e14d3dc7ccf5a4d4009c2ee874fe0cca4b9eff4006fe66693d4062f192327db4
  task: representation_probing
  value: 1.41
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.65
  dataset: ERA5-interpolation residual, Europe (wind speed)
  direction: worse
  id: sousa2026earth#c5
  label_ratio: null
  locator: Sec 3.3 / Figure 5
  metric: r2
  model: tessera
  span: highest cross-validated R2R^{2} in both Europe (0.270.27) and the United States
  span_sha256: 485bb1fd98e9743fe574329cf3c8311450e0d42c553d376149c7d1e3a66909ba
  task: representation_probing
  value: 0.27
date: '2026-08-12'
doi: 10.48550/arxiv.2608.12271
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-14T00:16:11.189529Z'
key: sousa2026earth
limitations:
- benchmark_narrowness
- spatial_transfer
- temporal_transfer
- time_sensitivity
- interpretability
models:
- tessera
proposed_tags:
- weather_downscaling
- conditional_neural_process
- CRPS
- sub_grid_correction
- wind_speed_downscaling
- temperature_downscaling
- forecast_lead_robustness
regions:
- global
- es
- 'no'
- us
self_evaluation: true
tasks:
- representation_probing
title: Earth observation embeddings are effective sub-grid descriptors for probabilistic
  weather downscaling
venue: arXiv
---

## summary



## setup



## caveats


