---
arxiv_id: '2605.04989'
authors:
- Ali Shibli
- Andrea Nascetti
- Yifang Ban
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G6_compactness
claims:
- axis: G6_compactness
  baseline: null
  baseline_value: 69.43
  dataset: MTBS/NBAC Wildfire Events
  direction: better
  id: shibli2026low#c1
  label_ratio: null
  locator: Table II
  metric: miou
  model: prithvi
  span: Prithvi-v2 Full fine-tuning 69.43 81.96 Decoder-only 71.98 83.71 LoRA 78.78
    88.13
  span_sha256: 6282b04ed8bd0119f0c1f503ca9e8db4d75a263c47b3aea20d6ebc4b690b3fa7
  task: change_detection
  value: 78.78
- axis: G5_cost
  baseline: null
  baseline_value: 81.96
  dataset: MTBS/NBAC Wildfire Events
  direction: better
  id: shibli2026low#c2
  label_ratio: null
  locator: Table II
  metric: f1
  model: prithvi
  span: Prithvi-v2 Full fine-tuning 69.43 81.96 Decoder-only 71.98 83.71 LoRA 78.78
    88.13
  span_sha256: 6282b04ed8bd0119f0c1f503ca9e8db4d75a263c47b3aea20d6ebc4b690b3fa7
  task: change_detection
  value: 88.13
date: '2026-05-06'
doi: 10.48550/arxiv.2605.04989
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:40:06.396498Z'
key: shibli2026low
limitations:
- benchmark_narrowness
- compute_cost
- mixed_pixels
- spatial_transfer
- temporal_transfer
models:
- prithvi
proposed_tags:
- burned_area_mapping
- LoRA
- parameter_efficient_fine_tuning
- TerraMind
- DINOv3
- wildfire_mapping
regions:
- us
- ca
self_evaluation: false
tasks:
- change_detection
title: Low-Rank Adaptation of Geospatial Foundation Models for Wildfire Mapping Using
  Sentinel-2 Data
venue: arXiv
---

## summary

The paper evaluates full fine-tuning, decoder-only fine-tuning, and LoRA for adapting Prithvi-v2, TerraMind, and DINOv3 geospatial foundation models to wildfire burned-area mapping in the US and Canada. LoRA consistently outperforms both other adaptation strategies while updating less than 1% of encoder parameters, with Prithvi-v2+LoRA achieving the best overall accuracy.

## setup

3,800 wildfire events (2017-2023) from MTBS (US) and NBAC (Canada) inventories, using Sentinel-2 bands B4/B8/B12 at 10-20m resolution, patched to 128x128; data split temporally/biome-wise into source (2017-2020, non-Boreal/Tundra) and target (2021-2023, Boreal/Tundra) domains for spatiotemporal generalization testing.

## caveats

Authors note patch-based sliding-window inference may introduce boundary artifacts or reduce spatial coherence, and that the study is geographically limited to US and Canada, with future work needed to extend to other regions (e.g., Africa, Australia) and incorporate SAR imagery.
