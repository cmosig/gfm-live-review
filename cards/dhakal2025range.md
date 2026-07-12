---
arxiv_id: '2502.19781'
authors:
- Aayush Dhakal
- Srikumar Sastry
- Subash Khanal
- Adeel Ahmad
- Eric Xing
- Nathan Jacobs
axes:
- G1_label_rich_parity
- G11_complementarity
- G3_spatial_transfer
- G6_compactness
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: satclip
  baseline_value: 68.9
  dataset: Biome
  direction: better
  id: dhakal2025range#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: presto
  span: 'RANGE


    83.3'
  span_sha256: cbc77f3cacf5aaaa2a5e603a11d2c5e867afa1ec79328c778293c1324b6458b9
  task: land_cover_classification
  value: 83.3
- axis: G1_label_rich_parity
  baseline: satclip
  baseline_value: 69.3
  dataset: EcoRegions
  direction: better
  id: dhakal2025range#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: presto
  span: 'SatCLIP


    68.9


    69.3'
  span_sha256: 90762edec24d1844e063048e0068e38839ec018c51256a1440d0c84cd85e29a9
  task: land_cover_classification
  value: 75.7
- axis: G1_label_rich_parity
  baseline: satclip
  baseline_value: 0.684
  dataset: Population Density
  direction: better
  id: dhakal2025range#c3
  label_ratio: null
  locator: Table 2
  metric: r2
  model: presto
  span: '0.666


    0.684'
  span_sha256: b07650a1f7a2b89859861d254f0eb4dc71e8507a1e186a56700651c24899895c
  task: population_density
  value: 0.799
- axis: G1_label_rich_parity
  baseline: satclip
  baseline_value: 0.666
  dataset: Elevation
  direction: better
  id: dhakal2025range#c4
  label_ratio: null
  locator: Table 2
  metric: r2
  model: presto
  span: '0.666


    0.684'
  span_sha256: b07650a1f7a2b89859861d254f0eb4dc71e8507a1e186a56700651c24899895c
  task: representation_probing
  value: 0.844
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 68.9
  dataset: Biome (SatCLIP+SatMAE image)
  direction: better
  id: dhakal2025range#c5
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: satclip
  span: 'loc⊕direct-sum\oplus⊕img


    74.9'
  span_sha256: 0f6ea3ca15082ba5d5e1023b4cc576727d3f8b34ede4f94df2230265bd356bbd
  task: representation_probing
  value: 74.9
- axis: G3_spatial_transfer
  baseline: satclip
  baseline_value: 75.1
  dataset: iNaturalist-2018
  direction: better
  id: dhakal2025range#c6
  label_ratio: null
  locator: Table 4
  metric: accuracy
  model: presto
  span: 'Img+SatCLIP


    75.1'
  span_sha256: cbdcf72049d7ea13cfafedde0ab86b5b9d60f7bdfec887cddb0580bb37a51254
  task: representation_probing
  value: 75.2
date: '2025-02-27'
doi: 10.48550/arxiv.2502.19781
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T19:07:29.383411Z'
key: dhakal2025range
limitations:
- benchmark_narrowness
- time_sensitivity
- compute_cost
models:
- satclip
- geoclip
proposed_tags:
- biome_classification
- ecoregion_classification
- country_classification
- elevation_prediction
- housing_price_prediction
- air_temperature_prediction
- geo_prior
- retrieval_augmented_generation
- checkerboard_resolution_task
- era5_climate_variables
regions:
- global
- us
self_evaluation: false
tasks:
- representation_probing
- population_density
- land_cover_classification
title: 'RANGE: Retrieval Augmented Neural Fields for Multi-Resolution Geo-Embeddings'
venue: arXiv
---

## summary

RANGE augments SatCLIP-style location embeddings with a retrieval mechanism that approximates high-resolution visual features from a database of satellite image embeddings, addressing information loss from contrastive location-image alignment. It outperforms SatCLIP, GeoCLIP, and other location encoders on classification (biome, ecoregion, country) and regression (elevation, population density) tasks, with a smoothness-constrained variant RANGE+ for controllable spatial frequency.

## setup

Retrieval database built from ~82k SatCLIP-dataset locations with paired low-resolution (SatCLIP projection) and high-resolution (SatMAE) image embeddings; linear probes evaluate embeddings on biome/ecoregion/country classification and temperature/elevation/population/housing regression, plus iNaturalist-2018 geo-prior classification and ERA5 climate variable regression.

## caveats

The authors note RANGE underperforms on California housing price prediction, attributing it to a temporal mismatch between the 1990-census housing labels and 2020 Sentinel-derived visual features; they also note the method's benefits are demonstrated specifically for satellite imagery and location alignment rather than all location-image settings, leaving generalization to other image modalities for future work.
