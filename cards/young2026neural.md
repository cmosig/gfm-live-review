---
arxiv_id: '2604.03874'
authors:
- Robin Young
- Srinivasan Keshav
axes:
- G8_uncertainty
- G4_temporal_transfer
- G3_spatial_transfer
- G9_ecological_fine_scale
claims:
- axis: G8_uncertainty
  baseline: task_specific
  baseline_value: 0.7
  dataset: GEDI L4A (Guaviare, Colombia)
  direction: better
  id: young2026neural#c1
  label_ratio: null
  locator: Table 1
  metric: r2
  model: tessera
  span: 0.75 in Guaviare, 0.50 in Queensland, 0.42 in Ucayali
  span_sha256: 1c4ffcc7b4a7200e1864864290833aaa3b6e25850b3eae1e1fc0609fcd263740
  task: biomass_estimation
  value: 0.75
- axis: G8_uncertainty
  baseline: task_specific
  baseline_value: 0.49
  dataset: GEDI L4A (Queensland, Australia)
  direction: better
  id: young2026neural#c2
  label_ratio: null
  locator: Table 1
  metric: r2
  model: tessera
  span: 0.75 in Guaviare, 0.50 in Queensland, 0.42 in Ucayali
  span_sha256: 1c4ffcc7b4a7200e1864864290833aaa3b6e25850b3eae1e1fc0609fcd263740
  task: biomass_estimation
  value: 0.5
- axis: G8_uncertainty
  baseline: task_specific
  baseline_value: 0.39
  dataset: GEDI L4A (Ucayali, Peru)
  direction: better
  id: young2026neural#c3
  label_ratio: null
  locator: Table 1
  metric: r2
  model: tessera
  span: 0.75 in Guaviare, 0.50 in Queensland, 0.42 in Ucayali
  span_sha256: 1c4ffcc7b4a7200e1864864290833aaa3b6e25850b3eae1e1fc0609fcd263740
  task: biomass_estimation
  value: 0.42
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: -0.165
  dataset: GEDI L4A (Ucayali, Peru, disturbed stratum)
  direction: better
  id: young2026neural#c4
  label_ratio: null
  locator: Table 2 / Sec 3.2
  metric: r2
  model: tessera
  span: the QRF achieves negative R2R^{2} (−0.17-0.17) in the disturbed stratum
  span_sha256: 43efa85031b03ee3f8c06655bf5cfa91fe422ce0252e2a449e24bf155dbebc40
  task: biomass_estimation
  value: 0.201
- axis: G8_uncertainty
  baseline: task_specific
  baseline_value: 13.03
  dataset: GEDI L4A (Guaviare, Colombia, disturbed stratum)
  direction: better
  id: young2026neural#c5
  label_ratio: null
  locator: Sec 3.2
  metric: rmse
  model: tessera
  span: XGBoost’s ZZ-score standard deviation reaches 13.03
  span_sha256: f8eceaed31b2531be911c866de2c074c8b993b5e3c9975fa684909e6b0f477e8
  task: biomass_estimation
  value: 0.94
date: '2026-04-04'
doi: 10.48550/arxiv.2604.03874
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:40:08.003673Z'
key: young2026neural
limitations:
- temporal_transfer
- spatial_transfer
- uncertainty
- benchmark_narrowness
models:
- tessera
proposed_tags:
- neural_processes
- calibration
- GEDI_gap_filling
- disturbance_stratification
regions:
- co
- pe
- au
self_evaluation: true
tasks:
- biomass_estimation
title: Neural Processes Maintain Calibrated Biomass Estimates Across Spatiotemporal
  Gaps and Disturbance
venue: arXiv
---

## summary

The paper extends the Attentive Neural Process framework for spatial GEDI biomass gap-filling to joint spatiotemporal interpolation using frozen Tessera foundation model embeddings, evaluated on three ecologically distinct regions. The ANP outperforms Quantile Random Forest and XGBoost baselines in log-space R2 and produces near-ideal uncertainty calibration (Z-score std close to 1.0), with the calibration advantage growing under disturbance conditions where baselines become severely overconfident or fail. The authors argue this supports space-for-time substitution for reconstructing biomass during GEDI's 13-month hibernation gap and future coverage interruptions.

## setup

GEDI L4A AGBD observations (2019-2023, log-transformed) paired with frozen 128-dim Tessera embeddings (3x3 patches) extracted from Sentinel-1/2 imagery for three regions (Guaviare Colombia, Ucayali Peru, Queensland Australia); model trained on 2019/2020/2022/2023 and evaluated on held-out 2021 via spatiotemporal cross-validation with spatial buffering, using 10 seeds, and compared against QRF and XGBoost quantile regression baselines with the same input features.

## caveats

Authors note disturbance stratification is coarse (tile-level, ~11km, coarser than individual disturbance events), sensor saturation in Sentinel-1/2 imposes an information ceiling in dense Amazonian forest limiting Ucayali performance, and the marginal contribution of temporal coordinates versus embeddings is not isolated, left for future work.
