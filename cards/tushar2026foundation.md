---
arxiv_id: '2605.00678'
authors:
- Zahid Hassan Tushar
- Sanjay Purushotham
axes:
- G1_label_rich_parity
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.2063
  dataset: PACE OCI L1B/L2 AOD
  direction: better
  id: tushar2026foundation#c1
  label_ratio: null
  locator: Table I
  metric: rmse
  model: prithvi
  span: PrithviEO1 [10]
  span_sha256: fded10569b97cd64b881924fa3b3780d98fd3c65367f7deb920491c1dfb0a132
  task: representation_probing
  value: 0.1925
- axis: G5_cost
  baseline: null
  baseline_value: null
  dataset: PACE OCI L1B/L2 AOD
  direction: worse
  id: tushar2026foundation#c2
  label_ratio: null
  locator: Table I
  metric: rmse
  model: prithvi
  span: ViTCG contains 8.82 M parameters, approximately
  span_sha256: 1e4e36efe0ac8a5da25ad6463df5548242ca14c78cbea6a06233b602d1b67435
  task: representation_probing
  value: 0.1925
date: '2026-05-01'
doi: 10.48550/arxiv.2605.00678
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:40:46.223192Z'
key: tushar2026foundation
limitations:
- compute_cost
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- aerosol_optical_depth_estimation
- hyperspectral_foundation_model
- PACE_OCI
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: Foundation AI Models for Aerosol Optical Depth Estimation from PACE Satellite
  Data
venue: arXiv
---

## summary

The paper proposes ViTCG, a compact hyperspectral vision transformer with channel-wise grouping for Aerosol Optical Depth (AOD) retrieval from PACE OCI radiance, and compares it against pixel-wise DNN baselines and multiple foundation models including the multispectral PrithviEO1 and hyperspectral HyperFree, HyperSigma, and SpectralEarth. ViTCG achieves a 62% MSE reduction and higher index of agreement than PrithviEO1 and other baselines while using ~10x fewer parameters and lower inference time. Validation against AERONET observations shows strong global agreement with larger deviations in high-AOD regions like South America and the Indian subcontinent.

## setup

Data consists of PACE OCI Level-1B TOA radiance (291 bands) and Level-2 AOD products from 2024-2025, processed into 96x96 patches (1800 train, 250 val, 2000 test), with additional AERONET-collocated validation on Feb/Mar 2025 dates. Models are compared using MSE, RMSE, MBE, and IOA metrics against PACE L2 AOD and AERONET ground truth.

## caveats

The authors note ViTCG has isolated failure cases despite overall spatial coherence, and that validation against AERONET shows larger deviations in high-AOD regions due to spatial representativeness error between point measurements and satellite footprint averages; foundation models including PrithviEO1 were not originally designed or evaluated for AOD estimation.
