---
arxiv_id: '2601.16011'
authors:
- Theodor Forgaard
- Jarle H. Reksten
- Anders U. Waldeland
- Valerio Marsocci
- Nicolas Longépé
- Michael Kampffmeyer
- Arnt-Børre Salberg
axes:
- G2_label_scarce_efficiency
- G1_label_rich_parity
- G3_spatial_transfer
- G5_cost
- G6_compactness
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 88.55
  dataset: Sen1Floods11
  direction: worse
  id: forgaard2026thor#c1
  label_ratio: 0.1
  locator: Table 1
  metric: miou
  model: prithvi
  span: '86.29'
  span_sha256: 20bb5acc25f097da4e334c79562da5eacb6a1e50322f1feace115c983ffd76e2
  task: semantic_segmentation
  value: 86.28
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 63.0
  dataset: Cloud-S3
  direction: worse
  id: forgaard2026thor#c2
  label_ratio: null
  locator: Table 2
  metric: miou
  model: dofa
  span: 58.2 ± 0.1
  span_sha256: fab44adf85dd17da8ae4006c4a8caa57cd23e2a482ba70322d3da2b7df26505b
  task: semantic_segmentation
  value: 58.2
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 68.1
  dataset: Biomass-S3
  direction: worse
  id: forgaard2026thor#c3
  label_ratio: null
  locator: Table 2
  metric: rmse
  model: dofa
  span: 74.1 ± 0.1
  span_sha256: 4b47c42db2c0ab3c4a4923d2088e3cdf8ceeb59debc37afcd40ba7fd4403ab42
  task: biomass_estimation
  value: 74.1
date: '2026-01-22'
doi: 10.48550/arxiv.2601.16011
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:55:07.525163Z'
key: forgaard2026thor
limitations:
- compute_cost
- benchmark_narrowness
- data_bias
models: []
proposed_tags:
- compute_adaptive_patching
- multi_sensor_fusion
- flexible_patch_size
- snow_cover_regression
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- flood_mapping
- change_detection
- crop_type_mapping
- land_cover_classification
- biomass_estimation
- representation_probing
title: 'THOR: A Versatile Foundation Model for Earth Observation Climate and Society
  Applications'
venue: arXiv
---

## summary

THOR is a compute-adaptive, multi-sensor foundation model unifying Sentinel-1, -2, and -3 (OLCI & SLSTR) data at 10m-1000m GSD, using randomized patch and image size sampling during MAE pre-training to enable a single set of weights to be deployed at variable patch sizes at inference. It achieves state-of-the-art or competitive results on PANGAEA benchmarks especially in low-label regimes and on Sentinel-3 tasks from Copernicus-Bench.

## setup

Pre-trained on THOR Pretrain (22TB, 6273 locations, 18332 tile-date combos spanning Sentinel-1/2/3 OLCI/SLSTR, DEM, land cover, ERA5-Land) using extended MAE with contrastive and map-prediction losses; evaluated on PANGAEA (9 segmentation tasks, 10/50/100% label splits) and Copernicus-Bench Sentinel-3 OLCI tasks against DOFA, Copernicus-FM, TerraMind, CROMA, Prithvi, Scale-MAE, and others.

## caveats

Authors note THOR-Large underperforms and is prone to overfitting in the 10% data-scarce regime; performance varies strongly per dataset; the flexible patching/token-budget heuristic and multi-modal alignment add engineering complexity not evaluated for robustness across all sensor dropout scenarios.
