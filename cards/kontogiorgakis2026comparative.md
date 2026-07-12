---
arxiv_id: '2602.18083'
authors:
- Ioannis Kontogiorgakis
- Athanasios Askitopoulos
- Iason Tsardanidis
- Dimitrios Bormpoudakis
- Ilias Tsoumas
- Fotios Balampanis
- Charalampos Kontoes
axes:
- G2_label_scarce_efficiency
- G9_ecological_fine_scale
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.514
  dataset: ISMN (113 stations, Europe)
  direction: parity
  id: kontogiorgakis2026comparative#c1
  label_ratio: null
  locator: Abstract / Table II
  metric: r2
  model: prithvi
  span: Foundation model (Prithvi) embeddings provide negligible improvement over
    hand-crafted features (R²=0.515 vs. 0.514)
  span_sha256: 20be36cef54565ab6a7ecdae9bd6271fba21e84bcebc7266a89271326356d825
  task: representation_probing
  value: 0.515
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.5066
  dataset: ISMN (113 stations, Europe)
  direction: parity
  id: kontogiorgakis2026comparative#c2
  label_ratio: null
  locator: Table II
  metric: r2
  model: prithvi
  span: Prithvi_S2
  span_sha256: e1b3f207a6c0ee3498d1d89ea8f292c658e357db2514beebad3dbd73f976c9cb
  task: representation_probing
  value: 0.5091
date: '2026-02-20'
doi: 10.48550/arxiv.2602.18083
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:42:14.401996Z'
key: kontogiorgakis2026comparative
limitations:
- benchmark_narrowness
- spatial_transfer
- data_bias
models:
- prithvi
proposed_tags:
- soil_moisture_estimation
- multimodal_fusion
- sar_orbit_geometry
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: Comparative Assessment of Multimodal Earth Observation Data for Soil Moisture
  Estimation
venue: arXiv
---

## summary

This paper builds a high-resolution soil moisture estimation framework for Europe combining Sentinel-1, Sentinel-2 and ERA5 data with Random Forest regression, and tests whether Prithvi foundation model embeddings improve over hand-crafted spectral features. It finds that hybrid temporal matching and a 10-day ERA5 lookback window optimize performance, while Prithvi embeddings offer negligible gains over traditional features.

## setup

113 ISMN stations across Europe (2019-2025) with 5cm depth soil moisture measurements are matched to Sentinel-1 SAR, Sentinel-2 optical, and ERA5-Land reanalysis data; Random Forest models are trained and evaluated with group-based 5-fold spatial cross-validation using R², RMSE and MAE. Prithvi 2.0 (300M) frozen encoder embeddings from 224x224 S2 patches are compared against hand-crafted spectral indices (NDVI, NDWI, NDMI, MSI) as input features.

## caveats

The authors note that averaging embeddings over 224x224 patches may dilute the signal from the smaller station footprint, that only 113 stations may cause high-dimensional embeddings to overfit relative to compact hand-crafted indices, and that the Prithvi-only configuration without S1 underperformed, showing embeddings alone cannot replace SAR's complementary information.
