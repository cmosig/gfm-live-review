---
arxiv_id: '2511.01408'
authors:
- Markus B. Pettersson
- Adel Daoud
axes:
- G6_compactness
- G5_cost
- G11_complementarity
- G3_spatial_transfer
- G8_uncertainty
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: DHS (37 surveys, 2017-2023)
  direction: parity
  id: pettersson2025leveraging#c1
  label_ratio: null
  locator: Table 1
  metric: r2
  model: alphaearth
  span: (A) DHS Points
  span_sha256: 1b3c3819c08e3f37ae5b111bf18c57a6ff9364dc7079db52baa9b821bab04f0d
  task: wealth_mapping
  value: 0.546
date: '2025-11-03'
doi: 10.48550/arxiv.2511.01408
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T16:32:04.911460Z'
key: pettersson2025leveraging
limitations:
- data_bias
- uncertainty
- spatial_transfer
- benchmark_narrowness
models:
- alphaearth
proposed_tags:
- graph_neural_network
- coordinate_displacement
- fuzzy_label_loss
- DHS_surveys
- GeoNames
- IWI
- Sub-Saharan_Africa
- spatial_autocorrelation
regions:
- ke
- rw
- gn
- et
- sn
- ng
- zm
- cm
- lr
- bf
- ml
- tg
- mr
- sl
- ug
- ne
- mg
- bj
- gh
- tz
- ci
- ga
- gm
- mz
- mw
self_evaluation: false
tasks:
- poverty_mapping
- wealth_mapping
title: Leveraging Compact Satellite Embeddings and Graph Neural Networks for Large-Scale
  Poverty Mapping
venue: arXiv
---

## summary

The authors propose a graph neural network approach using compact 64-dimensional AlphaEarth satellite embeddings to predict cluster-level International Wealth Index across Sub-Saharan Africa. Modeling spatial relations between surveyed and unlabeled GeoNames settlements, with a fuzzy-label loss to account for DHS coordinate displacement, slightly improves accuracy over image-only baselines. Ego graphs constrained to the plausible displacement radius perform best, while fuzzy-label variants perform worse.

## setup

37 DHS surveys (2017-2023) across 25 Sub-Saharan African countries (~16,600 clusters) with mean IWI labels, plus >167,000 GeoNames populated places, each with a 64-dim AlphaEarth embedding (500m buffer). Six methods (MLP/GCN variants) evaluated via cross-validation across surveys to test generalization to unseen countries, reporting MAE and R2.

## caveats

The GeoNames dataset is incomplete and biased toward larger or more accessible settlements; the probabilistic weighting ignores the population prior of the DHS displacement mechanism, and fuzzy-label models perform notably worse, suggesting displaced coordinates still provide more reliable supervision.
