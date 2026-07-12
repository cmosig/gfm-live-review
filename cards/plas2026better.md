---
arxiv_id: '2605.18667'
authors:
- Thijs L van der Plas
- Jacob JW Bakermans
- Vishal Nedungadi
- Gabrielė Tijūnaitytė
- Marc Rußwurm
- Ioannis N Athanasiadis
axes:
- G11_complementarity
- G3_spatial_transfer
- G9_ecological_fine_scale
claims:
- axis: G11_complementarity
  baseline: tessera
  baseline_value: 70.6
  dataset: Dynamic World
  direction: better
  id: plas2026better#c1
  label_ratio: null
  locator: Sec 5.1, Fig 1b
  metric: r2
  model: alphaearth
  span: their fused score (76.7%) is significantly greater than any of their individual
    scores (71.1% and 70.6%, respectively)
  span_sha256: db408888512a4e9cefbd1fadedb714315ac54f8cd2a9d744904886e400a33984
  task: land_cover_classification
  value: 76.7
- axis: G1_label_rich_parity
  baseline: tessera
  baseline_value: 70.6
  dataset: Dynamic World
  direction: better
  id: plas2026better#c2
  label_ratio: null
  locator: Table 3
  metric: r2
  model: alphaearth
  span: any of their individual scores (71.1% and 70.6%, respectively)
  span_sha256: cfd8854cb4dc079c8be664358e947b0d4c1fe465ff2344de5cd246a02e6c7f76
  task: land_cover_classification
  value: 71.1
date: '2026-05-18'
doi: 10.48550/arxiv.2605.18667
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T16:39:05.797573Z'
key: plas2026better
limitations:
- benchmark_narrowness
models:
- alphaearth
- tessera
- geoclip
- satclip
proposed_tags:
- embedding_complementarity
- embedding_fusion
- location_embeddings
- pixel_embeddings
- bioclimatic_variable_prediction
- distance_to_road_prediction
- CCA_CKA_similarity
- spatial_scale_of_classes
- platonic_representation_hypothesis
regions:
- global
self_evaluation: false
tasks:
- crop_type_mapping
- biomass_estimation
- land_cover_classification
- population_density
title: 'Better Together: Evaluating the Complementarity of Earth Embedding Models'
venue: arXiv
---

## summary

The authors propose evaluating Earth embedding models by their complementarity, the performance gain of fused embeddings over the best single-model baseline, via a complementarity index. Evaluating AlphaEarth, Tessera, GeoCLIP and SatCLIP in isolation, pairs, and jointly across six tasks, fused embeddings beat the best single model on four of six tasks. Complementarity is task- and location-dependent, and for land cover regression is partially explained by the spatial scale of land cover classes.

## setup

Six downstream tasks (CropHarvest crop type, MMEarth-Bench biomass, Dynamic World land cover, WorldClim bioclimatic, WorldPop population density, GRIP4 distance-to-road) evaluated with linear/logistic regression (L2, lambda=1) on z-scored embeddings, 95/5 train/test across 20 folds. Embeddings (AlphaEarth, Tessera pixel; GeoCLIP, SatCLIP location) are fused by concatenation; scored with R2 for regression and accuracy for classification.

## caveats

The authors note this is not a comprehensive overview: only four pre-computed embedding models and six tasks are assessed. They extract a single pixel embedding per location to match location embeddings, so they do not use pixel embeddings' full capabilities (e.g., segmentation), and concatenating all embeddings (960 dims) can hurt performance via overfitting given only 3.5k-9k data points.
