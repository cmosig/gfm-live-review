---
arxiv_id: '2407.13862'
authors:
- Michael J. Bianco
- David Eigen
- Michael Gormish
axes:
- G3_spatial_transfer
- G11_complementarity
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: Im2GPS3k
  direction: better
  id: bianco2024enhancing#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: geoclip
  span: GeoCLIP
  span_sha256: d289faea852729f23a98fce2fd4586e5960b58cb446204577227eca575a5fdb7
  task: representation_probing
  value: 79.81
- axis: G11_complementarity
  baseline: null
  baseline_value: 81.14
  dataset: Street View
  direction: better
  id: bianco2024enhancing#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: geoclip
  span: +LS
  span_sha256: 3140e5bb839716d13670ade48ef5511dc527d6daec9404c674ddbc6242c55b97
  task: representation_probing
  value: 83.33
date: '2024-07-18'
doi: 10.48550/arxiv.2407.13862
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T09:22:58.105825Z'
key: bianco2024enhancing
limitations:
- benchmark_narrowness
- data_bias
- spatial_transfer
models:
- geoclip
proposed_tags:
- image_geolocation
- recall_vs_area_metric
- landscan_population_density
- esa_cci_land_cover
- geoestimation
- ensembling
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: Enhancing Worldwide Image Geolocation by Ensembling Satellite-Based Ground-Level
  Attribute Predictors
venue: arXiv
---

## summary

This paper introduces a Recall vs Area (RvA) metric for evaluating image geolocation systems and an ensembling approach combining geolocation models (GeoEstimation, GeoCLIP) with satellite-derived ground-level attribute predictors (LandScan population density, ESA-CCI Land Cover). The approach improves recall over larger, non-contiguous search areas especially in under-sampled rural regions, tested on Im2GPS3k and a Street View dataset.

## setup

Attribute predictors (ResNet-50v2 BiT-M) are trained on MP-16 imagery relabeled with LandScan population-density buckets and ESA-CCI land cover classes, then ensembled via elementwise probability product with rasterized GeoEstimation/GeoCLIP outputs on a common lat-lon grid; evaluated on Im2GPS3k and a Street View panorama dataset using RvA and conventional GCD thresholds.

## caveats

The authors note their common grid resolution (~4km) prevents locating images within the 1km GCD threshold, GCD evaluation fails to capture the gains from limiting search area since it only considers the top-1 point, and recall at smaller area scales is sometimes reduced on Im2GPS3k due to its urban-biased distribution.
