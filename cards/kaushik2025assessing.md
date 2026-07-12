---
arxiv_id: '2511.01990'
authors:
- Saurabh Kaushik
- Lalit Maurya
- Elizabeth Tellman
- ZhiJie Zhang
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.68
  dataset: FloodPlanet PlanetScope
  direction: better
  id: kaushik2025assessing#c1
  label_ratio: null
  locator: Table III
  metric: miou
  model: clay
  span: Clay outperforms others on PlanetScope (0.79 mIoU)
  span_sha256: 96b1579bc261b0f62264d3ae3f725124b973d8556eeeaecad6d578ce9924793f
  task: flood_mapping
  value: 0.79
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.69
  dataset: FloodPlanet Sentinel-2
  direction: better
  id: kaushik2025assessing#c2
  label_ratio: null
  locator: Table III
  metric: miou
  model: clay
  span: "and Sentinel-2 \n(0.72), while Prithvi leads on Sentinel-1 (0.57)"
  span_sha256: 7f1403f75aa5734ca74ee831b572a398b330d722007bcb51dac0db8fa2044d01
  task: flood_mapping
  value: 0.72
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.51
  dataset: FloodPlanet Sentinel-1
  direction: better
  id: kaushik2025assessing#c3
  label_ratio: null
  locator: Table III
  metric: miou
  model: prithvi
  span: while Prithvi leads on Sentinel-1 (0.57)
  span_sha256: de336a3f4a1ac20bc1bfc0c9501d7bd10ad6b84756f5d121bcb5bf67a8ecc11b
  task: flood_mapping
  value: 0.57
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: FloodPlanet (leave-one-region-out)
  direction: better
  id: kaushik2025assessing#c4
  label_ratio: null
  locator: Sec III.B
  metric: miou
  model: clay
  span: "Clay shows \nslightly better performance across all sensors, with mIoU scores\
    \ \nof 0.72, 0.66, and 0.51"
  span_sha256: 7a99099e7605ad41c7c143916c96c1f628131d9edc89a95b23777992848f9c4c
  task: flood_mapping
  value: 0.72
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.69
  dataset: FloodPlanet (19 sites, leave-one-region-out)
  direction: better
  id: kaushik2025assessing#c5
  label_ratio: null
  locator: Table VI
  metric: miou
  model: clay
  span: "Across all 19 sites, cross-validation reveals a 4% \nimprovement by Clay\
    \ over U-Net"
  span_sha256: f4feab44ec018ed19f50390017679ced9bf36dd96acc0a98aa0d1263b3337bef
  task: flood_mapping
  value: 0.73
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: FloodPlanet PlanetScope
  direction: better
  id: kaushik2025assessing#c6
  label_ratio: null
  locator: Sec III.C
  metric: miou
  model: clay
  span: "Clay achieves 0.64 mIoU on PlanetScope with \njust five training images,\
    \ outperforming Prithvi (0.24) and DOFA \n(0.35)"
  span_sha256: b0655d07ad957ee53b22d37e4c4054269497fe7304757c23e7f53df990c0e462
  task: flood_mapping
  value: 0.64
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: FloodPlanet PlanetScope
  direction: worse
  id: kaushik2025assessing#c7
  label_ratio: null
  locator: Sec III.C
  metric: miou
  model: prithvi
  span: "Clay achieves 0.64 mIoU on PlanetScope with \njust five training images,\
    \ outperforming Prithvi (0.24) and DOFA \n(0.35)"
  span_sha256: b0655d07ad957ee53b22d37e4c4054269497fe7304757c23e7f53df990c0e462
  task: flood_mapping
  value: 0.24
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: FloodPlanet PlanetScope
  direction: worse
  id: kaushik2025assessing#c8
  label_ratio: null
  locator: Sec III.C
  metric: miou
  model: dofa
  span: "outperforming Prithvi (0.24) and DOFA \n(0.35)"
  span_sha256: 3f5d8aa90e4d705f7bbbe285f5b3562e8084d84b24fb2a605d13605bc1dc60c1
  task: flood_mapping
  value: 0.35
- axis: G6_compactness
  baseline: prithvi
  baseline_value: 650.0
  dataset: FloodPlanet PlanetScope
  direction: better
  id: kaushik2025assessing#c9
  label_ratio: null
  locator: Sec III.C / Abstract
  metric: miou
  model: clay
  span: "approximately 3× faster than Prithvi (650M) and 2× faster than \nDOFA (410M)"
  span_sha256: 1e6451f3d0e181cb6daed7d715af5f918280850cf4d33228ad7ef72fc2eb5608
  task: flood_mapping
  value: 26.0
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.68
  dataset: FloodPlanet PlanetScope
  direction: better
  id: kaushik2025assessing#c10
  label_ratio: null
  locator: Table III
  metric: miou
  model: dofa
  span: "DOFA and \nPrithvi 2.0 achieve mIoU of 0.78 and 0.75, respectively"
  span_sha256: 2e6adcede5c223abc385bd7079fea7c20885a17c40d164797e26fa841e0041e3
  task: flood_mapping
  value: 0.78
date: '2025-11-03'
doi: 10.1109/jstars.2026.3656855
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:44:46.297171Z'
key: kaushik2025assessing
limitations:
- mixed_pixels
- spatial_transfer
- benchmark_narrowness
- data_bias
models:
- prithvi
- clay
- dofa
proposed_tags:
- FloodPlanet
- leave-one-region-out
- few-shot
- cloud_cover
- encoder_freezing
regions:
- global
- es
- gh
- so
- kh
- bd
self_evaluation: false
tasks:
- flood_mapping
title: 'Assessing the value of Geo-Foundational Models for Flood Inundation Mapping:
  Benchmarking models for Sentinel-1, Sentinel-2, and Planetscope for end-users'
venue: arXiv
---

## summary

The paper benchmarks three geo-foundation models (Prithvi 2.0, Clay V1.5, DOFA) against CNN and ViT baselines trained from scratch (U-Net, Attention U-Net, DeepLabv3+, TransNorm, UViT) for flood inundation mapping across PlanetScope, Sentinel-1, and Sentinel-2 using the FloodPlanet dataset. Clay generally performs best, especially in few-shot settings and computational efficiency, while Prithvi leads on Sentinel-1.

## setup

Uses the FloodPlanet dataset (366 PlanetScope tiles, 362 Sentinel-1, 298 Sentinel-2 images across 19 globally sampled flood events), with random 75/10/15 train/val/test splits, leave-one-region-out cross-validation across 5 sites (Spain, Ghana, Somalia, Cambodia, Bangladesh), and few-shot experiments with as few as 2-5 training images.

## caveats

Authors note persistent spectral ambiguity/mixed-pixel confusion for shallow water and small land parcels, cloud cover/shadow errors, limited spatial transferability to some regions (Kansas, Uzbekistan), reliance on optical-only imagery lacking topographic data, and possible human annotation uncertainty in the FloodPlanet labels.
