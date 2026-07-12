---
arxiv_id: '2511.02923'
authors:
- Ivan Zvonkov
- Gabriel Tseng
- Inbal Becker-Reshef
- Hannah Kerner
axes:
- G1_label_rich_parity
- G5_cost
- G12_openness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.75
  dataset: CropHarvest Togo test set
  direction: better
  id: zvonkov2025cropland#c1
  label_ratio: null
  locator: Table 2
  metric: f1
  model: presto
  span: '0.808'
  span_sha256: e93790adbbc06fed79e2bbbee4595e1e9ae6c921dd46b3d3508b5f45ad3065f4
  task: land_cover_classification
  value: 0.808
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.88
  dataset: CropHarvest Togo test set
  direction: better
  id: zvonkov2025cropland#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: presto
  span: '0.897'
  span_sha256: c29699d04c899bb3ddb5bd406ee08397c32b1e1c5c7a8b024f95d815b9556394
  task: land_cover_classification
  value: 0.897
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.75
  dataset: CropHarvest Togo test set
  direction: worse
  id: zvonkov2025cropland#c3
  label_ratio: null
  locator: Table 2
  metric: f1
  model: alphaearth
  span: '0.745'
  span_sha256: 8b14326916baf426879fad321e2a16a1ddd584cba694d976ba71bac7484a6298
  task: land_cover_classification
  value: 0.745
- axis: G11_complementarity
  baseline: alphaearth
  baseline_value: 0.745
  dataset: CropHarvest Togo test set
  direction: better
  id: zvonkov2025cropland#c4
  label_ratio: null
  locator: Table 2
  metric: f1
  model: presto
  span: '0.808'
  span_sha256: e93790adbbc06fed79e2bbbee4595e1e9ae6c921dd46b3d3508b5f45ad3065f4
  task: land_cover_classification
  value: 0.808
date: '2025-11-04'
doi: 10.48550/arxiv.2511.02923
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:48:57.697387Z'
key: zvonkov2025cropland
limitations:
- benchmark_narrowness
- spatial_transfer
models:
- presto
- alphaearth
proposed_tags:
- cropland_mapping
- google_earth_engine
- embedding_clustering
- worldcover_comparison
- glad_comparison
- workflow_simplicity
regions:
- tg
self_evaluation: false
tasks:
- land_cover_classification
title: Cropland Mapping using Geospatial Embeddings
venue: arXiv
---

## summary

The authors evaluate geospatial embeddings from Presto and AlphaEarth for cropland mapping in Togo, training a simple Random Forest classifier on top of the embeddings. Presto-based maps achieved the highest overall accuracy and F1 score, outperforming AlphaEarth embeddings and existing GLAD/WorldCover cropland products. They argue embeddings simplify and accelerate mapping workflows for land-use-change monitoring.

## setup

Presto embeddings (128-dim, 10m, from Sentinel-1/2, ERA5, SRTM) were generated for all of Togo (Mar 2019–Mar 2020) via Vertex AI and Google Earth Engine, and compared to globally-available AlphaEarth embeddings. A GEE Random Forest (100 trees, 0.7 probability threshold) was trained on CropHarvest Togo labels and evaluated against the CropHarvest Togo test set and existing GLAD/WorldCover maps.

## caveats

The authors note experiments are limited to a single country (Togo) as a case study, that both Presto and AlphaEarth embeddings were benchmarked against data in the Togo test set, and that future work is needed to extend the evaluation across additional regions and applications.
