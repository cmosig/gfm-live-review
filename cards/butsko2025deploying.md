---
arxiv_id: '2508.00858'
authors:
- Christina Butsko
- Kristof Van Tricht
- Gabriel Tseng
- Giorgia Milli
- David Rolnick
- Ruben Cartuyvels
- Inbal Becker Reshef
- Zoltan Szantoi
- Hannah Kerner
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.856
  dataset: WorldCereal cropland dataset (Random split)
  direction: better
  id: butsko2025deploying#c1
  label_ratio: null
  locator: Table 1
  metric: f1
  model: presto
  span: Finetuned Presto 0.861
  span_sha256: a65b139b8de30c18e222e8412f712e02e78f738bad516430fa092f428c587913
  task: land_cover_classification
  value: 0.861
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.81
  dataset: WorldCereal cropland dataset (Geographic split)
  direction: better
  id: butsko2025deploying#c2
  label_ratio: null
  locator: Table 1
  metric: f1
  model: presto
  span: Deployed baseline 0.856 0.810 0.830
  span_sha256: 6c6220b294e3acea84cb2b8748569ce8d22ea1c85a9bb0121602a7d37ad8a62e
  task: land_cover_classification
  value: 0.829
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.83
  dataset: WorldCereal cropland dataset (Temporal split)
  direction: better
  id: butsko2025deploying#c3
  label_ratio: null
  locator: Table 1
  metric: f1
  model: presto
  span: Finetuned Presto 0.861 0.829 0.886
  span_sha256: 8a42b102e22c9faf32c6537d08d8bb9b72ace0e0fb9eb846a85dfac8a71833b6
  task: land_cover_classification
  value: 0.886
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.728
  dataset: WorldCereal crop type dataset (Random split)
  direction: better
  id: butsko2025deploying#c4
  label_ratio: null
  locator: Table 3
  metric: f1
  model: presto
  span: Unprocessed CatBoost 0.728 0.563 0.649
  span_sha256: 9a5d621cdc5b1c13eec0b6206da42334324d628650a66371750e24b022fc7adb
  task: crop_type_mapping
  value: 0.809
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.563
  dataset: WorldCereal crop type dataset (Geographic split)
  direction: better
  id: butsko2025deploying#c5
  label_ratio: null
  locator: Table 3
  metric: f1
  model: presto
  span: Finetuned Presto 0.809 0.650 0.686
  span_sha256: 8a86fa31c99b3a4a6a1e14c18c39d2b3e71b3e7c743252ecbd54837d1a492f72
  task: crop_type_mapping
  value: 0.65
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.649
  dataset: WorldCereal crop type dataset (Temporal split)
  direction: better
  id: butsko2025deploying#c6
  label_ratio: null
  locator: Table 3
  metric: f1
  model: presto
  span: Unprocessed CatBoost 0.728 0.563 0.649
  span_sha256: 9a5d621cdc5b1c13eec0b6206da42334324d628650a66371750e24b022fc7adb
  task: crop_type_mapping
  value: 0.686
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.415
  dataset: WorldCereal crop type dataset (millet/sorghum class, Random split)
  direction: better
  id: butsko2025deploying#c7
  label_ratio: null
  locator: Table 5
  metric: f1
  model: presto
  span: Millet / Sorghum (5.2K/0.1K) 0.415 0.429 (+0.014) 0.530 (+0.115)
  span_sha256: ce50c6bf739f2c855dd8036ccd55afa5fd089425aee74cd56945e9b2ea8b5ee4
  task: crop_type_mapping
  value: 0.53
- axis: G5_cost
  baseline: galileo
  baseline_value: 89.4
  dataset: forward-pass MAC comparison
  direction: better
  id: butsko2025deploying#c8
  label_ratio: null
  locator: Sec 2.1
  metric: accuracy
  model: presto
  span: ranging from 38.37M for Presto (Tseng et al., 2024) to 89.40M for Galileo-Nano
  span_sha256: 51700525a15df7aa622213361f65395227b7704a173b650097ebbd09421bc900
  task: representation_probing
  value: 38.37
date: '2025-07-16'
doi: 10.48550/arxiv.2508.00858
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:53:49.497199Z'
key: butsko2025deploying
limitations:
- benchmark_narrowness
- data_bias
- compute_cost
- time_sensitivity
models:
- presto
proposed_tags:
- cropland_classification
- operational_deployment_protocol
- self_supervised_adaptation
- openEO_pipeline
regions:
- es
- ni
- lv
- tz
- et
- ar
- at
- br
- mg
- mz
- ma
- id
- global
self_evaluation: false
tasks:
- crop_type_mapping
- land_cover_classification
title: 'Deploying Geospatial Foundation Models in the Real World: Lessons from WorldCereal'
venue: arXiv
---

## summary

The paper proposes a three-step protocol (requirements/hypotheses, adaptation strategy, empirical testing) for deploying geospatial foundation models operationally, and applies it to the WorldCereal global crop-mapping system using the Presto model.

## setup

Presto was fine-tuned (with and without an additional SSL adaptation step) on WorldCereal's Sentinel-1/Sentinel-2/DEM/weather pixel-timeseries dataset (~1.3M cropland points, 255K crop-type points across many countries), evaluated on random, geographic (held-out countries), and temporal (held-out 2021) splits against CatBoost baselines (deployed WorldCereal classifier and an unprocessed-features variant) using per-class and macro F1.

## caveats

The authors note the additional SSL step did not improve performance and disproved their hypothesis (H3) that it would aid adaptation to distribution shift; task-specific fine-tuning yields only modest gains when the pretrained model already closely matches target data; and label distributions in the dataset are highly spatially and temporally imbalanced, introducing shifts between training and deployment periods.
