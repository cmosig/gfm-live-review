---
arxiv_id: '2609.29151'
authors:
- Peiwen Zhang
- Kristie Hu
- Jovana Knezevic
- Shunde Yin
- Kyle Gao
axes:
- G3_spatial_transfer
- G7_interpretability
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 391.9
  dataset: Global Renewables Watch solar farms (284 European farms, 2024)
  direction: better
  id: zhang2026recoverable#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: alphaearth
  span: All three representations substantially outperformed the uniform random baseline
    (1,350.5 km)
  span_sha256: 9dbe97f189314e0759a7562e6fbc88ab9ea75c4817861bac85644c7098271471
  task: representation_probing
  value: 179.7
date: '2026-09-24'
doi: 10.48550/arxiv.2609.29151
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-27T00:16:12.091516Z'
key: zhang2026recoverable
limitations:
- benchmark_narrowness
- data_bias
- spatial_transfer
models:
- alphaearth
- tessera
proposed_tags:
- geographic-information-leakage
- coordinate-probing
- embedding-auditing
- solar-farms
- spatial-cross-validation
- permutation-test
regions:
- es
- fr
- gb
- de
- ie
- nl
- pt
- ro
self_evaluation: true
tasks:
- representation_probing
title: Recoverable Geographic Location Information in Earth-Observation Embeddings
venue: arXiv
---

## summary

The paper tests whether geographic coordinates can be recovered from Tessera v1, Tessera v1.1 and AlphaEarth embeddings of 284 European solar farms. All three encode recoverable location information, beating a uniform random baseline and Sentinel-2 controls, with AlphaEarth strongest. Prediction error grows as nearby training farms are excluded and varies across held-out countries.

## setup

284 solar farms from Global Renewables Watch (81.3% in Spain) with pixel embeddings median-aggregated per farm. Coordinates in EPSG:3035 were predicted with linear, ridge and MLP probes under five-fold spatial CV with 25 km dependency grouping, plus permutation tests, exclusion-distance sweeps and leave-one-country-out evaluation.

## caveats

Geographic coverage is uneven (81.3% Spain, only two farms each for Portugal and Romania). Larger exclusion distances and country holdouts reduce training data. Predictability may reflect country- or dataset-specific patterns rather than fine-grained geographic information, so the authors do not claim coordinates are explicitly encoded.
