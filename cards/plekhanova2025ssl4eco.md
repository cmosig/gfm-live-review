---
arxiv_id: '2504.18256'
authors:
- Elena Plekhanova
- Damien Robert
- Johannes Dollinger
- Emilia Arens
- Philipp Brun
- Jan Dirk Wegner
- Niklaus Zimmermann
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G9_ecological_fine_scale
- G2_label_scarce_efficiency
claims:
- axis: G9_ecological_fine_scale
  baseline: null
  baseline_value: null
  dataset: Biomes
  direction: better
  id: plekhanova2025ssl4eco#c1
  label_ratio: null
  locator: Table 3
  metric: f1
  model: prithvi
  span: 'SeCo-Eco (ours)

    56.1 ± 0.7'
  span_sha256: 173a434c4f120bbf6644b89967f71e580d598f88c32600784272cd6be671f5f5
  task: land_cover_classification
  value: 56.1
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: CAVM
  direction: better
  id: plekhanova2025ssl4eco#c2
  label_ratio: null
  locator: Table 3
  metric: f1
  model: prithvi
  span: 59.4 ± 1.0
  span_sha256: 72b1ef8ecc9f7e2ae9bcc872fd2a0d3de7a374168a326db61f573c26281c91ca
  task: land_cover_classification
  value: 59.4
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 80.7
  dataset: BigEarthNet-10%
  direction: better
  id: plekhanova2025ssl4eco#c3
  label_ratio: 0.1
  locator: Table 4
  metric: accuracy
  model: prithvi
  span: 'SeCo-Eco (ours)

    85.3 ± 0.0'
  span_sha256: f014ce292761a7682c4055e6d8f6925f6aeb0f71a20879baa01fdf4b934fb987
  task: crop_type_mapping
  value: 85.3
- axis: G9_ecological_fine_scale
  baseline: null
  baseline_value: null
  dataset: BioMassters
  direction: better
  id: plekhanova2025ssl4eco#c4
  label_ratio: null
  locator: Table 5
  metric: r2
  model: prithvi
  span: 'SeCo-Eco (ours)

    75.3 ± 0.3'
  span_sha256: 603283bda3aa9fa742a2879f205b499c7f84b6eb96f3b0b459bab1883cdaf6b4
  task: biomass_estimation
  value: 75.3
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: null
  dataset: CHELSA
  direction: better
  id: plekhanova2025ssl4eco#c5
  label_ratio: null
  locator: Table 5
  metric: r2
  model: prithvi
  span: 81.1 ± 0.4
  span_sha256: 317693d9fe0cb43a66ee206d8846a53359c4235605f8fbe694d97f0cd595733d
  task: hydrological_modeling
  value: 81.1
date: '2025-04-25'
doi: 10.48550/arxiv.2504.18256
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:49:31.787294Z'
key: plekhanova2025ssl4eco
limitations:
- data_bias
- temporal_transfer
- benchmark_narrowness
- time_sensitivity
models:
- croma
- prithvi
- satmae
- dofa
proposed_tags:
- SSL4Eco
- SeCo-Eco
- MoCo-Eco
- phenology_informed_sampling
- SeCo
- SSL4EO-S12
- Satlas
- BigEarthNet
- GeoLifeCLEF
- EU-Forest
- TreeSatAI
- BioMassters
- CHELSA_climate_regression
- Biomes_classification
- CAVM_arctic_vegetation
regions:
- global
- fi
- fr
- gb
- de
self_evaluation: false
tasks:
- land_cover_classification
- crop_type_mapping
- biomass_estimation
- representation_probing
title: 'SSL4Eco: A Global Seasonal Dataset for Geospatial Foundation Models in Ecology'
venue: arXiv
---

## summary

SSL4Eco is a globally uniform, phenology-informed multi-date Sentinel-2 pretraining dataset addressing geographic and seasonal biases in existing geospatial foundation model datasets. The authors train SeCo-Eco (a SeCo model) on SSL4Eco and show it outperforms other GFMs on 7 of 8 ecological downstream tasks including classification and regression.

## setup

250k globally uniform locations with 4 phenology-derived seasonal Sentinel-2 patches (256x256px, 12 bands + NDVI) sampled via EVI-based Greenup/Maturity/Senescence/Dormancy variables from MODIS MCD12Q2. Evaluated via linear probing and k-NN against SeCo, SatMAE, Satlas, CROMA, SSL4EO, and DOFA on 8 downstream tasks (Biomes, CAVM, BigEarthNet, GeoLifeCLEF, EU-Forest, TreeSatAI, BioMassters, CHELSA climate regression).

## caveats

Images span 2017-2024 to reduce cloud cover, creating large temporal gaps unsuitable for fine-grained temporal tasks; only one SSL method combination (SeCo/MoCo) tested besides pretraining data; limited to Sentinel-2 optical modality; TreeSatAI performance worse than SatMAE due to small patch size mismatch with pretraining resolution.
