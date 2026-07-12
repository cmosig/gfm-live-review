---
arxiv_id: '2605.10949'
authors:
- Usman Nazir
- I-Han Cheng
- Sara Khalid
axes:
- G4_temporal_transfer
- G7_interpretability
- G9_ecological_fine_scale
- G11_complementarity
claims: []
date: '2026-04-29'
doi: 10.48550/arxiv.2605.10949
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:41:08.883602Z'
key: nazir2026alphaearth
limitations:
- time_sensitivity
- data_bias
- spatial_transfer
models:
- alphaearth
proposed_tags:
- malaria_prediction
- respiratory_infection_prediction
- child_undernutrition_stunting
- population_health
- disease_surveillance
- climate_sensitive_disease
- dhs_survey
- tabular_feature_augmentation
regions:
- ng
- in
- pk
- ke
- np
- mz
- bd
- kh
- lb
- tj
- ph
self_evaluation: false
tasks: []
title: AlphaEarth Satellite Embeddings for Modelling Climate Sensitive Diseases Towards
  Global Health Resilience
venue: arXiv
---

## summary

The paper evaluates AlphaEarth Foundations 64-dim satellite embeddings as predictive features for three LMIC health outcomes: malaria case counts in Nigeria, childhood ARI across 11 DHS countries, and child undernutrition (WHZ) across 35 DHS countries. Appending embeddings to climate/pollution baselines raises test R2 at cluster/location granularity (malaria 0.201->0.245; ARI pooled 0.157->0.206), while a country-level broadcast for stunting is neutral due to collinearity with country fixed effects. The authors argue embeddings add value only when merged at sufficient spatial granularity and request access to cluster-level and Population Dynamics data.

## setup

AlphaEarth V1 embeddings (via Google Earth Engine) are appended to tabular baselines and evaluated with tree-based estimators and MLPs: Nigeria NMEP malaria (2000-2023 train, 2024 test) vs climate-only baseline; 9,271 DHS clusters for ARI (5-fold x2-repeat CV) vs gaseous-pollutant baseline; 389,035 children/35 DHS countries for WHZ vs tabular/fixed-effects baseline using country-broadcast embeddings.

## caveats

Authors note DHS cluster coordinates are privacy-displaced up to 5-10 km (measurement error attenuating effects), embeddings are static annual composites unable to capture intra-annual/outbreak dynamics, WHZ is only a proxy for undernutrition (height-for-age untested), and country-level pooling may mask agroecological heterogeneity; the cluster-level stunting experiment remains blocked on data access.
