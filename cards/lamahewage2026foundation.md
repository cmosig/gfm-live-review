---
arxiv_id: '2607.27217'
authors:
- Shashika Lamahewage
- Chandi Witharana
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G7_interpretability
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: NEFIN CFI (Scenario I, combined LiDAR+GSE)
  direction: better
  id: lamahewage2026foundation#c1
  label_ratio: null
  locator: Table 5 / Results
  metric: r2
  model: alphaearth
  span: Combined LiDAR-GSE models achieved an R² of 0.79 for AGB estimation
  span_sha256: 245591fb07d3aed037699e394ac13a6722cc24dc7a331ef991ea807978c09271
  task: biomass_estimation
  value: 0.79
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: null
  dataset: NEFIN CFI (Scenario II, GSE-only, growth-adjusted)
  direction: better
  id: lamahewage2026foundation#c2
  label_ratio: null
  locator: Scenario II Results
  metric: r2
  model: alphaearth
  span: achieved the highest predictive accuracy exhibiting an R² of 0.82 and an MAE
    of 245.23 Mg ha⁻¹
  span_sha256: 1ce916e980097123eaeb615fdbf117044f73c4b830236225c36fcb927f43b6b2
  task: biomass_estimation
  value: 0.82
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.79
  dataset: NEFIN CFI (Scenario I, GSE-only)
  direction: worse
  id: lamahewage2026foundation#c3
  label_ratio: null
  locator: Discussion
  metric: r2
  model: alphaearth
  span: we achieved R2 of 0.67-0.79 using GSE features, LiDAR and ML algorithms
  span_sha256: 82ffe8a700ce6cd306ea873ac4ef2d471f67147cd12d033c1d5d7806b2a94dd9
  task: biomass_estimation
  value: 0.67
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: NEFIN CFI (Scenario I, LiDAR-only tuned)
  direction: parity
  id: lamahewage2026foundation#c4
  label_ratio: null
  locator: Table 5
  metric: r2
  model: alphaearth
  span: RF1_T model achieved the best R2 (0.79) and lowest RMSE and MAE values
  span_sha256: 0a73aeaf8b79b4e8479b69f3174023bbae6b52360fc21f95643030b451e597c7
  task: biomass_estimation
  value: 0.79
date: '2026-06-25'
doi: 10.48550/arxiv.2607.27217
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-01T00:12:28.988908Z'
key: lamahewage2026foundation
limitations:
- interpretability
- mixed_pixels
- data_bias
- benchmark_narrowness
- uncertainty
models:
- alphaearth
proposed_tags:
- forest_aboveground_biomass
- google_satellite_embeddings
- lidar_fusion
- spatial_autocorrelation
- monte_carlo_stability
regions:
- us
self_evaluation: false
tasks:
- biomass_estimation
title: Foundation-Model Earth Representations Enable Regional-Scale Forest Aboveground
  Biomass Monitoring Across the Northeastern United States
venue: arXiv
---

## summary

The paper evaluates Google Satellite Embeddings (GSE), produced by the AlphaEarth Foundation Model, for regional forest aboveground biomass (AGB) estimation across the northeastern US, combining them with airborne LiDAR and continuous forest inventory (NEFIN-CFI) data. Combined LiDAR-GSE models reached R²=0.79, and expanding training data via annual GSE observations (growth-adjusted) increased R² to 0.82 while reducing bias by over 70%. Spatial autocorrelation and Monte Carlo analyses showed GSE-LiDAR integration reduced residual spatial dependence and improved model stability.

## setup

NEFIN continuous forest inventory plots (589 for Scenario I overlapping LiDAR+GSE; 6801 for Scenario II using growth-adjusted GSE-only data, 2017-2025) across seven northeastern US states were combined with airborne LiDAR metrics and 64-band annual Google Satellite Embedding (AlphaEarth) features, reduced via PCA, to train RF, XGBoost, and ExtraTrees regressors with 80/20 train-test split and 10-fold cross-validation.

## caveats

Authors note the black-box nature of GSE embeddings limits direct ecological interpretation, allometric equation uncertainty (20-75% of total uncertainty) was not evaluated, high AGB plots (>600 Mgha⁻¹) increased prediction error/uncertainty, CFI plot geolocation uncertainty may exceed 30m, and GSE-only models underperformed LiDAR-only models by ~17.9% in R² under limited sample size conditions.
