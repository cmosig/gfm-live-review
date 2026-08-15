---
arxiv_id: '2608.03959'
authors:
- Simon Pfreundschuh
- Christian D. Kummerow
- Johannes Schmude
- Sujit Roy
- Rahul Ramachandran
- Tsengdar Lee
- Valentine Anantharaj
- Katherine H. Breen
axes:
- G1_label_rich_parity
- G4_temporal_transfer
- G5_cost
claims: []
date: '2026-08-04'
doi: 10.48550/arxiv.2608.03959
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-15T00:10:07.660422Z'
key: pfreundschuh2026prithvi
limitations:
- data_bias
- compute_cost
- temporal_transfer
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- precipitation_forecasting
- numerical_weather_prediction
- satellite_observation_assimilation
- medium_range_forecasting
- atmospheric_foundation_model
regions:
- global
- us
- br
self_evaluation: false
tasks:
- representation_probing
title: 'Prithvi-Precip: Integrating Satellite Observations into an Atmospheric AI
  Foundation Model for Precipitation Forecasting'
venue: arXiv
---

## summary

Prithvi-Precip finetunes the Prithvi-WxC atmospheric foundation model for global precipitation forecasting, comparing training on MERRA-2 reanalysis vs IMERG V07 satellite-derived precipitation targets and testing direct ingestion of raw satellite observations. The authors find autoregressive rollout training beats continuous forecasting, IMERG-trained targets generalize better to independent radar/gauge data than MERRA-2 targets, and satellite observation ingestion improves short-lead-time skill especially in tropics/subtropics, substantially narrowing the gap to AIFS relative to a GEOS-FP baseline.

## setup

The model is finetuned on MERRA-2 atmospheric fields (2000-2020) with precipitation targets from either MERRA-2 or IMERG V07, plus raw satellite brightness temperature/radiance observations from multiple passive microwave and geostationary sensors, evaluated against independent MRMS radar data over CONUS and INMET gauge data over Brazil, with GEOS-FP and AIFS as operational baselines.

## caveats

The authors note that large-model results likely remain undertrained given compute constraints, that discrete 0Z/12Z initialization times interact with the diurnal cycle causing accuracy oscillations, that IMERG remains affected by retrieval uncertainties, that gauge-based validation over Brazil is less representative at grid scale due to point-measurement character, and that AIFS retains a substantial advantage at longer lead times likely due to its more advanced data assimilation system.
