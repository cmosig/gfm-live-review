---
arxiv_id: '2605.08113'
authors:
- Yaw Osei Adjei
axes:
- G3_spatial_transfer
- G2_label_scarce_efficiency
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: -0.093
  dataset: GROW-Africa/HarvestStat maize yield (LOCO)
  direction: better
  id: adjei2026foundation#c1
  label_ratio: null
  locator: Table III
  metric: r2
  model: prithvi
  span: ranging from −0.093-0.093 (Spectral / Ridge) to −0.027-0.027 (Prithvi-EO /
    Ridge)
  span_sha256: 1270f1b8a978104e4eb53b5dcbfab1a51c44fa2add9ad4c47fb71e611e1cea67
  task: crop_yield_estimation
  value: -0.027
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.291
  dataset: GROW-Africa/HarvestStat maize yield (random five-fold CV)
  direction: better
  id: adjei2026foundation#c2
  label_ratio: null
  locator: Table II
  metric: r2
  model: prithvi
  span: best-case Prithvi-EO R=20.300{}^{2}=0.300 vs. spectral R=20.291{}^{2}=0.291
  span_sha256: cff9837440e8c5ff831e60a6c87351944988b595025c559dd100cab08a208355
  task: crop_yield_estimation
  value: 0.3
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: GROW-Africa/HarvestStat maize yield (LOCO)
  direction: worse
  id: adjei2026foundation#c3
  label_ratio: null
  locator: Sec V-J / Table V
  metric: r2
  model: prithvi
  span: 'a single NDVI feature

    (Ridge R=2−0.170{}^{2}=-0.170) performs comparably to the full 768-dimensional

    Prithvi-EO embeddings (Ridge R=2−0.027{}^{2}=-0.027)'
  span_sha256: 2c2466af3ec0f212f269314b5a56a358019db2d1565838092c7da46dd80e2cd7
  task: crop_yield_estimation
  value: -0.17
date: '2026-04-27'
doi: 10.48550/arxiv.2605.08113
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:41:07.143953Z'
key: adjei2026foundation
limitations:
- spatial_transfer
- data_bias
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- leave_one_country_out_CV
- distribution_shift
- label_shift
- frozen_embeddings
- single_frame_composite
regions:
- ke
- mw
- ng
- rw
- tz
self_evaluation: false
tasks:
- crop_yield_estimation
title: Do Foundation Model Embeddings Improve Cross-Country Crop Yield Generalisation?
  A Leave-One-Country-Out Evaluation in Sub-Saharan Africa
venue: arXiv
---

## summary

This paper evaluates whether frozen Prithvi-EO-1.0-100M and ViT-Base embeddings improve cross-country generalisation for smallholder maize yield prediction across five sub-Saharan African countries, compared to hand-engineered Sentinel-2 spectral features. Under a rigorous Leave-One-Country-Out (LOCO) cross-validation scheme, all feature sets — including Prithvi-EO embeddings — yield universally negative R2, essentially matching a naive country-mean baseline and offering no meaningful advantage over spectral features. The authors conclude the primary bottleneck is country-level yield distribution (label) shift rather than deficiencies in feature representation.

## setup

6,404 GPS/admin-centroid smallholder maize yield observations (2017-2022) from Kenya, Malawi, Nigeria, Rwanda, and Tanzania, paired with Sentinel-2 annual growing-season composites, CHIRPS rainfall, and three feature sets (spectral, frozen Prithvi-EO CLS embeddings, frozen ViT-Base CLS embeddings) fed into Ridge/Random Forest/XGBoost regressors under both random five-fold CV and Leave-One-Country-Out CV.

## caveats

Authors flag that Prithvi-EO was applied only as a frozen, single-frame (non-temporal) encoder despite being designed for multi-temporal input, was pre-trained mainly on North American HLS imagery (geographic domain shift), that Nigeria labels are coarser admin-centroid proxies rather than GPS points, that only five LOCO folds are available so per-country R2 variance (0.32-0.70) dwarfs between-condition differences (<0.07) making results only directional, and that no domain adaptation or fine-tuning techniques were tested.
