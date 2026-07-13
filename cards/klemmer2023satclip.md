---
arxiv_id: '2311.17179'
authors:
- Konstantin Klemmer
- Esther Rolf
- Caleb Robinson
- Lester Mackey
- Marc Rußwurm
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: geoclip
  baseline_value: 0.79
  dataset: Population
  direction: better
  id: klemmer2023satclip#c1
  label_ratio: null
  locator: Table 2
  metric: r2
  model: satclip
  span: Population
  span_sha256: 5b828861aec15d606e690189228b9b0f3af3d1a6048ea5f730935b02a746b699
  task: population_density
  value: 0.82
- axis: G1_label_rich_parity
  baseline: geoclip
  baseline_value: 90.72
  dataset: Countries
  direction: better
  id: klemmer2023satclip#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: satclip
  span: Countries
  span_sha256: 8faf7ec7ab20ca1cb49b159bf28c95e43895aad06e2727e3227524e82a9cc6e1
  task: representation_probing
  value: 96.0
- axis: G3_spatial_transfer
  baseline: geoclip
  baseline_value: 0.32
  dataset: Pop. Density (Africa, zero-shot)
  direction: worse
  id: klemmer2023satclip#c3
  label_ratio: null
  locator: Table 3
  metric: r2
  model: satclip
  span: Pop. Density∗
  span_sha256: 749e67387bad9d8f0c9a0e9b23d91ecc6c9480b9a2218036629be8f7a0adfe8f
  task: population_density
  value: 0.18
- axis: G3_spatial_transfer
  baseline: geoclip
  baseline_value: 12.41
  dataset: Ecoregions (Africa, few-shot)
  direction: better
  id: klemmer2023satclip#c4
  label_ratio: 0.01
  locator: Table 3
  metric: accuracy
  model: satclip
  span: Ecoregions†
  span_sha256: df321e0da3838af6b2810587d248888519694f7c3413fcd6bae069f9fe461506
  task: representation_probing
  value: 32.03
date: '2023-11-28'
doi: 10.48550/arxiv.2311.17179
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:19:29.396118Z'
key: klemmer2023satclip
limitations:
- data_bias
- spatial_transfer
- benchmark_narrowness
models:
- satclip
- geoclip
proposed_tags:
- location_encoder
- geographic_generalization
- air_temperature_prediction
- biome_classification
- ecoregion_classification
- country_classification
- elevation_prediction
- median_income_prediction
- california_housing_prediction
- inaturalist_species_classification
- contrastive_pretraining
regions:
- global
self_evaluation: false
tasks:
- population_density
- representation_probing
title: 'SatCLIP: Global, General-Purpose Location Embeddings with Satellite Imagery'
venue: arXiv
---

## summary

SatCLIP is a global, general-purpose location encoder pretrained via contrastive matching of Sentinel-2 satellite imagery with geographic coordinates, using a new uniformly-sampled S2-100K dataset. It is evaluated on nine downstream regression/classification tasks and compared against other location encoders (CSP, GPS2Vec, GeoCLIP) and location-only/image-only baselines.

## setup

SatCLIP is pretrained on 100k globally uniformly-sampled Sentinel-2 tiles (S2-100K) using a CLIP-style contrastive loss between a spherical-harmonics+SirenNet location encoder and a frozen pretrained CNN/ViT image encoder. Downstream MLP models are trained using SatCLIP embeddings (and raw coordinates for comparison methods) on nine tasks including air temperature, income, housing prices, elevation, population density, and biome/ecoregion/country/species classification, under both random splits and continent-held-out geographic generalization splits.

## caveats

The authors note SatCLIP underperforms GeoCLIP on regionally-constrained, US/California-specific tasks (Median Income, Cali. Housing) since GeoCLIP's MP-16 pretraining data is US-centric; combining embeddings from different location encoders does not improve performance over the best single embedding; and the framework currently marginalizes over time rather than explicitly modeling a space-time encoder.
