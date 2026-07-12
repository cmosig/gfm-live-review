---
arxiv_id: '2510.25954'
authors:
- Lynn Metz
- Rachel Haggard
- Michael Moszczynski
- Samer Asbah
- Chris Mwase
- Patricia Khomani
- Tyler Smith
- Hannah Cooper
- Annie Mwale
- Arbaaz Muslim
- Gautam Prasad
- Mimi Sun
- Tomer Shekel
- Joydeep Paul
- Anna Carter
- Shravya Shetty
- Dylan Green
axes:
- G10_human_semantics
- G11_complementarity
- G5_cost
- G2_label_scarce_efficiency
claims:
- axis: G10_human_semantics
  baseline: task_specific
  baseline_value: 0.44
  dataset: Malawi health catchment areas
  direction: better
  id: metz2025application#c1
  label_ratio: null
  locator: Sec Results (Embedding-based Models)
  metric: r2
  model: alphaearth
  span: with R² values of 0.58 and 0.18 from cross-validation, respectively
  span_sha256: ed17ed78a8363414967e8deaa2a902461645ad1c4798212d51333d5a1fa81079
  task: population_density
  value: 0.58
- axis: G10_human_semantics
  baseline: task_specific
  baseline_value: 0.47
  dataset: Malawi health catchment areas
  direction: better
  id: metz2025application#c2
  label_ratio: null
  locator: Sec Results (Embedding-based Models)
  metric: r2
  model: alphaearth
  span: 'while test set R² values were

    0.53 and 0.16, respectively'
  span_sha256: beb1d1746b0a36a013aa7a8ebde26e40d368121570ac5d6526e9eafb8aa2cba8
  task: population_density
  value: 0.53
date: '2025-10-29'
doi: 10.48550/arxiv.2510.25954
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:50:04.094203Z'
key: metz2025application
limitations:
- spatial_transfer
- data_bias
- benchmark_narrowness
models:
- alphaearth
proposed_tags:
- health_facility_outputs
- LMIC
- PDFM
- call_detail_records
- mobile_phone_data
- internet_search_embeddings
- XGBoost
- multi_source_embedding_integration
- routine_health_information_systems
- HIV_prediction
- malaria_prediction
- disease_surveillance
- geostatistical_interpolation_baseline
regions:
- mw
self_evaluation: false
tasks:
- population_density
title: Application and Validation of Geospatial Foundation Model Data for the Prediction
  of Health Facility Programmatic Outputs -- A Case Study in Malawi
venue: arXiv
---

## summary

The study evaluated three GeoFM embedding sources (Google PDFM, Google AlphaEarth, and mobile phone CDR) for predicting 15 routine health programmatic outputs across 552 catchments in Malawi using XGBoost. Embedding-based approaches beat traditional geostatistical baselines (IDW, kriging) in 13 of 15 indicators, and a Multi-GeoFM model integrating all three sources produced the most robust predictions. Population density was the most accurately predicted indicator, while TB and malnutrition were poorly predicted due to low primary data availability.

## setup

Prediction targets came from DHIS2 and LIMS routine health data (Jan 2021-May 2023) aggregated to 552 government health catchment areas; models used an 80/20 train/test split with 5-fold cross-validation and grid-searched XGBoost. AlphaEarth (64-dim satellite embeddings), PDFM (16-dim search/maps/weather embeddings), and CDR (10-dim mobile embeddings) were each modeled separately and combined into a Multi-GeoFM model, compared against IDW and ordinary kriging baselines, evaluated with R².

## caveats

Authors note the analysis is restricted to Malawi and may not generalize to other LMICs; prediction targets depend on variable-quality routine DHIS2/LIMS reporting, with poorly-reported indicators (TB, malnutrition) predicted poorly; excluding facilities with high missing/zero values may introduce bias; and several count targets lack proper population denominators to compute rates.
