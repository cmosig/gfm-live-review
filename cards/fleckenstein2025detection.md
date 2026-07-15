---
arxiv_id: '2510.18773'
authors:
- Jannis Fleckenstein
- David Kreismann
- Tamara Rosemary Govindasamy
- Thomas Brunschwiler
- Etienne Vos
- Mattia Rigotti
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G9_ecological_fine_scale
claims:
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: 0.257
  dataset: Internal Cooling (Granite-GFM cooling gradient experiment)
  direction: better
  id: fleckenstein2025detection#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: prithvi
  span: Internal Cooling 0.240 0.257
  span_sha256: 24d6fbd900cd8ea66ccb3db1842a057df840262ff0983b8d682fd6a41e19a63d
  task: urban_signal_mapping
  value: 0.249
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: 0.339
  dataset: Spillover Cooling (Granite-GFM cooling gradient experiment)
  direction: better
  id: fleckenstein2025detection#c2
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: prithvi
  span: Spillover Cooling 0.302 0.339
  span_sha256: b4d38c0025e1518a571ad5885dafb89b3c450357523bf21ed0b37c1465019045
  task: urban_signal_mapping
  value: 0.243
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: Brașov High-Heat Scenario (90th percentile LST)
  direction: parity
  id: fleckenstein2025detection#c3
  label_ratio: 0.9
  locator: Table 2
  metric: rmse
  model: prithvi
  span: High-Heat Scenario (90th) 1.96 7.05 2.66 1.74 6.37 2.52
  span_sha256: e069d25dfb523b4ef8235e010c623edeae79366fb191fb0f4d63cfef45911acd
  task: urban_signal_mapping
  value: 2.52
date: '2025-10-21'
doi: 10.48550/arxiv.2510.18773
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:45:22.172846Z'
key: fleckenstein2025detection
limitations:
- spatial_transfer
- temporal_transfer
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- urban_heat_island
- land_surface_temperature
- inpainting_simulation
- climate_projection_RCP
regions:
- cz
- ro
- global
self_evaluation: false
tasks:
- urban_signal_mapping
title: Detection and Simulation of Urban Heat Islands Using a Fine-Tuned Geospatial
  Foundation Model for Microclimate Impact Prediction
venue: arXiv
---

## summary



## setup



## caveats


