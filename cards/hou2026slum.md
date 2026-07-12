---
arxiv_id: '2605.10029'
authors:
- Shuyang Hou
- Ziqi Liu
- Haoyue Jiao
- Zhangyan Xu
- Xiaopu Zhang
- Lutong Xie
- Yaxian Qing
- Jianyuan Liang
- Xuefeng Guan
- Huayi Wua
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G6_compactness
- G7_interpretability
- G9_ecological_fine_scale
- G10_human_semantics
- G11_complementarity
claims:
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: 0.538
  dataset: GRAM pseudo-masks
  direction: better
  id: hou2026slum#c1
  label_ratio: null
  locator: Sec 4.1.1
  metric: f1
  model: alphaearth
  span: the median spatial F1 of TorchMLP increases from 0.538 to 0.616
  span_sha256: 26d0ca5d4e2d81ef45c8dcbca71caa0d744f5fbb386248875532beddc7d3f762
  task: slum_detection
  value: 0.616
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: GRAM pseudo-masks
  direction: parity
  id: hou2026slum#c2
  label_ratio: null
  locator: Sec 6.2
  metric: f1
  model: alphaearth
  span: the median F1 of S1 TorchMLP is 0.763
  span_sha256: 3ada097f94ee99268b8cf0d00f9a171ba6bdaf355c8599de9781a109c22963cf
  task: slum_detection
  value: 0.763
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: 0.299
  dataset: GRAM pseudo-masks
  direction: better
  id: hou2026slum#c3
  label_ratio: null
  locator: Sec 4.1.2
  metric: r2
  model: alphaearth
  span: increases from 0.299 under S1 to 0.466 under
  span_sha256: 30cbc474730b0a71efc0f7d53de70f732aea5f6ef3fe43560dc5e7b1701d43cb
  task: slum_detection
  value: 0.466
- axis: G9_ecological_fine_scale
  baseline: null
  baseline_value: 0.0
  dataset: GRAM pseudo-masks
  direction: worse
  id: hou2026slum#c4
  label_ratio: null
  locator: Sec 4.1.4
  metric: r2
  model: alphaearth
  span: with a median of −2.00
  span_sha256: 1bc3e4954ee158123e59084ca13e1918fd1d28e7963a93ed10ccaa9d63df7cd2
  task: slum_detection
  value: -2.0
date: '2026-05-11'
doi: 10.48550/arxiv.2605.10029
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T16:40:58.866090Z'
key: hou2026slum
limitations:
- spatial_transfer
- mixed_pixels
- human_semantics
- data_bias
- benchmark_narrowness
models:
- alphaearth
proposed_tags:
- sub-pixel density estimation
- pseudo-label supervision
- spatial block cross-validation
- PCA dimensional saturation
- SHAP dimension importance
- POI auxiliary features
- nighttime lights
- SSIM structural fidelity
- Moran's I clustering
- informal settlements
- city-scale representation drift
- AlphaEarth Foundations
regions:
- pk
- ht
- eg
- bf
- hn
- in
- co
- ke
- ve
- br
- za
- lk
self_evaluation: false
tasks:
- slum_detection
title: 'Slum Detection and Density Mapping with AlphaEarth Foundations: A Representation
  Learning Evaluation Across 12 Global Cities'
venue: arXiv
---

## summary

The paper evaluates AlphaEarth Foundations (AEF) 64-dim 10 m embeddings for slum classification and sub-pixel density estimation across 12 cities and 69 city-year pairs, using GRAM pseudo-masks as labels under random and spatial block cross-validation. Same-city cross-year training (S2) performs best (median spatial F1 = 0.616, R² = 0.466), while cross-city transfer degrades due to city-scale representation drift. Positive-pixel R² is consistently negative, indicating AEF cannot model intra-pixel density gradients at 10 m.

## setup

Twelve cities across Africa, Latin America, and Asia (69 city-year pairs, 2017-2024) with AEF embeddings and GRAM pseudo-mask labels; five lightweight baselines (LogReg/Ridge, HistGBT, RF, TorchMLP), four training strategies (S1-S4), six auxiliary feature configurations (C0-C5), evaluated under 80/20 random split and 3x3 spatial block CV, plus PCA/SHAP analyses and full-AOI inference.

## caveats

Authors flag that all labels are GRAM pseudo-masks rather than field data (so accuracy measures consistency between two model products), the 0.6 m-to-10 m aggregation and consistently negative positive-pixel R² suggest intra-pixel density modeling nears the resolution limit, auxiliary factors are fused by simple concatenation causing occasional negative interactions, five cities fail dual-task usability thresholds, and residual Moran's I shows spatially clustered errors.
