---
arxiv_id: '2506.17302'
authors:
- Yijun Lin
- Theresa Chen
- Colby Brungard
- Grunwald Sabine
- Sue Ives
- Matt Macander
- Timm Nawrocki
- Yao-Yi Chiang
- Nic Jelinski
axes:
- G3_spatial_transfer
- G2_label_scarce_efficiency
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 94.87
  dataset: NSP presence-absence (Random split)
  direction: better
  id: lin2025fine#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: prithvi
  span: MiSo 97.38 98.26 93.90 90.98 96.61
  span_sha256: b1b454fab99bac6b95597262a1434f83679cc09ee6ed7a5113cac2bbc3e5f4e9
  task: landslide_susceptibility
  value: 96.61
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 92.2
  dataset: NSP presence-absence (SH-1km split)
  direction: worse
  id: lin2025fine#c2
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: prithvi
  span: MiSo 95.33 92.17 76.17 84.87 90.48
  span_sha256: caefb5dfc795223d0f21b4202d69b0102b3348fdc4f0def0447c1e8f198960bb
  task: landslide_susceptibility
  value: 90.48
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 83.44
  dataset: NSP presence-absence (SH-10km split)
  direction: worse
  id: lin2025fine#c3
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: prithvi
  span: MiSo 91.27 82.68 58.62 75.93 81.06
  span_sha256: 5ddbe930689616cfeacb26928495e504172ba55e290fbac1422256d6e8e99369
  task: landslide_susceptibility
  value: 81.06
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 64.67
  dataset: Soil taxonomy classification (Random split)
  direction: better
  id: lin2025fine#c4
  label_ratio: null
  locator: Table 2
  metric: f1
  model: prithvi
  span: MiSo 66.16 66.31 65.89
  span_sha256: 740defa2a0d3f1fe964c48db294e0f6f77f49b7aca81e84a50a7d2639cf131c1
  task: land_cover_classification
  value: 65.89
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 54.88
  dataset: Soil taxonomy classification (SH-10km split)
  direction: better
  id: lin2025fine#c5
  label_ratio: null
  locator: Table 2
  metric: f1
  model: prithvi
  span: MiSo 55.86 55.61 55.11
  span_sha256: 08f5645b0216f58f61eb6a56231ccdae18210787515d87c67e901a94ba5bf867
  task: land_cover_classification
  value: 55.11
date: '2025-06-17'
doi: 10.48550/arxiv.2506.17302
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:47:25.768914Z'
key: lin2025fine
limitations:
- spatial_transfer
- data_bias
- benchmark_narrowness
- time_sensitivity
models: []
proposed_tags:
- soil_taxonomy_classification
- permafrost_mapping
- implicit_image_function
- SATLASNET
- SWIN_Transformer
- random_forest_baseline
regions:
- us
self_evaluation: false
tasks:
- landslide_susceptibility
title: Fine-Scale Soil Mapping in Alaska with Multimodal Machine Learning
venue: arXiv
---

## summary

The paper introduces MiSo, a computer vision model combining a pretrained SWIN-Transformer-based geospatial foundation model (SATLASNET/SatMAE-style), implicit image functions, and contrastive multimodal/geo alignment, to produce statewide 10-meter soil maps for near-surface permafrost and soil taxonomy in Alaska. MiSo is compared against a Random Forest baseline across three spatial data splits, showing higher recall for permafrost presence and generally better soil taxonomy classification, though not uniformly across all spatial holdouts or MLRAs.

## setup

Uses ~38,000 field observations from the Alaska Soil Data Bank (15,000 for near-surface permafrost, 32,000 for soil taxonomy) combined with Sentinel-2 imagery, topographic derivatives, and 30-year climate normals, all at 10m resolution; evaluated via 5-fold cross-validation under Random, SH-1km, and SH-10km spatial holdout splits.

## caveats

Authors note MiSo produces sharper/more decisive but potentially overconfident probability distributions limiting uncertainty identification, does not uniformly outperform RF in every MLRA or spatial split (notably worse overall accuracy on SH-1km/SH-10km splits and worse on Andisols), ground-truth labels have known spatial biases/underestimation relative to established permafrost zone definitions, and the model does not currently account for temporal/forecasting aspects of permafrost thaw despite fieldwork dates spanning 1952-2023.
