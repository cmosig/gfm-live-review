---
arxiv_id: '2409.13598'
authors:
- Johannes Schmude
- Sujit Roy
- Will Trojak
- Johannes Jakubik
- Daniel Salles Civitarese
- Shraddha Singh
- Julian Kuehnert
- Kumar Ankur
- Aman Gupta
- Christopher E Phillips
- Romeo Kienzler
- Daniela Szwarcman
- Vishal Gaur
- Rajat Shinde
- Rohit Lal
- Arlindo Da Silva
- Jorge Luis Guevara Diaz
- Anne Jones
- Simon Pfreundschuh
- Amy Lin
- Aditi Sheshadri
- Udaysankar Nair
- Valentine Anantharaj
- Hendrik Hamann
- Campbell Watson
- Manil Maskey
- Tsengdar J Lee
- Juan Bernabe Moreno
- Rahul Ramachandran
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G2_label_scarce_efficiency
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 3.08
  dataset: MERRA-2 T2m downscaling
  direction: better
  id: schmude2024prithvi#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: prithvi
  span: sp. RMSE tp. RMSE tp. corr.
  span_sha256: 7c4d1f296eaeb15ff9b5fe8fc181673e5c747bc0921ddb542028d05ecb202d31
  task: representation_probing
  value: 0.73
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 1.47
  dataset: CORDEX tas downscaling
  direction: better
  id: schmude2024prithvi#c2
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: prithvi
  span: '1.47'
  span_sha256: 41671744528237151ca58cfca8264fe854054d3e25fae6eee53361c3ef4e53c5
  task: representation_probing
  value: 0.44
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 201.939
  dataset: HURDAT hurricane tracks (Atlantic 2017-2023)
  direction: better
  id: schmude2024prithvi#c3
  label_ratio: null
  locator: Sec 2.5.3
  metric: rmse
  model: prithvi
  span: significantly outperforming the MERRA-2 trained FourCastNet (201.939 km)
  span_sha256: d007bf311e242ed4737d549c2bdb9e63ee0b6b403c232a5eba6f76b89deb1bf5
  task: representation_probing
  value: 63.9
date: '2024-09-20'
doi: 10.48550/arxiv.2409.13598
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:48:33.778375Z'
key: schmude2024prithvi
limitations:
- compute_cost
- time_sensitivity
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- weather_forecasting
- downscaling
- gravity_wave_flux_parameterization
- hurricane_track_forecasting
- masked_reconstruction
- MERRA-2
- CORDEX
- ERA5
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: 'Prithvi WxC: Foundation Model for Weather and Climate'
venue: arXiv
---

## summary

Prithvi WxC is a 2.3 billion parameter transformer foundation model pretrained on 160 MERRA-2 atmospheric variables using a masked-reconstruction-plus-forecasting objective with climatology conditioning. It is validated zero-shot on reconstruction, forecasting, and hurricane track prediction, and fine-tuned for downscaling (MERRA-2 and CORDEX), and gravity wave flux parameterization.

## setup

Pretrained on MERRA-2 reanalysis data (1980-2019, 160 variables) using a scalable ViT-based encoder-decoder with local/global windowed attention; downstream tasks fine-tune the frozen backbone with new embedding/output layers for downscaling (MERRA-2 and EURO-CORDEX) and ERA5-derived gravity wave flux parameterization, plus zero-shot hurricane track forecasting evaluated against HURDAT and FourCastNet baselines.

## caveats

Authors note zero-shot forecasting performance decays after ~66 hours lead time falling below Pangu; comparisons to WeatherBench2 models are confounded by different reference datasets and resolutions; the CORDEX downscaling changes dataset, temporal step, and domain simultaneously making isolation of effects difficult; gravity wave fine-tuning uses ERA5 rather than the MERRA-2 pretraining data, introducing distribution shift.
