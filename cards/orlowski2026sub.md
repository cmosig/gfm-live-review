---
arxiv_id: '2607.08945'
authors:
- Kasimir Orlowski
- Filip Sabo
- Michele Meroni
- Astrid Verhegghen
- Mariana Belgiu
- Felix Rembold
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G9_ecological_fine_scale
- G5_cost
claims:
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.92
  dataset: COLD-CI stratified reference points
  direction: worse
  id: orlowski2026sub#c1
  label_ratio: null
  locator: Abstract
  metric: f1
  model: tessera
  span: TESSERA performed best (F1 = 0.86)
  span_sha256: 452caa8e7d425423bffc0bd28a3a713b77d278b7597d70140be37d8faf8a27a2
  task: crop_type_mapping
  value: 0.86
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.92
  dataset: COLD-CI stratified reference points
  direction: worse
  id: orlowski2026sub#c2
  label_ratio: null
  locator: Abstract
  metric: f1
  model: alphaearth
  span: followed by AEF (F1 = 0.82) and Sentinel-2 (F1 = 0.76)
  span_sha256: 1d091eaf17213aa81e9a8be5e366f453b21f41c3d7a3fabfe8b7f27c079ba80d
  task: crop_type_mapping
  value: 0.82
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.83
  dataset: Kalischek cocoa probability layer
  direction: worse
  id: orlowski2026sub#c3
  label_ratio: null
  locator: Abstract
  metric: f1
  model: alphaearth
  span: the Kalischek product performed best (F1 = 0.83), comparable to the internally
    trained AEF model
  span_sha256: 0c5ac682201fc1ff2c5cbcdc0dd76267ef503b20ae8b18ff4cccc218c3f33b5b
  task: crop_type_mapping
  value: 0.82
- axis: G3_spatial_transfer
  baseline: alphaearth
  baseline_value: 0.64
  dataset: FDaP v2025b (AlphaEarth-based)
  direction: better
  id: orlowski2026sub#c4
  label_ratio: null
  locator: Sec 4.4
  metric: f1
  model: alphaearth
  span: "the internally trained AEF model achieved substantially higher performance\
    \ than FDaP v2025b (F1 = \n0.82 vs 0.64)"
  span_sha256: 9e045b9f8620fbd08432dfe14ced57d90d65fdb75c561c474d2422e8b70d06fb
  task: crop_type_mapping
  value: 0.82
- axis: G9_ecological_fine_scale
  baseline: null
  baseline_value: null
  dataset: COLD-CI stratified reference points, overall weighted
  direction: parity
  id: orlowski2026sub#c5
  label_ratio: null
  locator: Results
  metric: accuracy
  model: tessera
  span: followed by TESSERA (OA = 0.90; F1 = 0.86)
  span_sha256: 8f634d4a61083877208920949ab02fab45cef06fe7531077d8758e8b4fdb54a1
  task: crop_type_mapping
  value: 0.9
date: '2026-07-09'
doi: 10.48550/arxiv.2607.08945
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:05:13.327724Z'
key: orlowski2026sub
limitations:
- benchmark_narrowness
- mixed_pixels
- spatial_transfer
- data_bias
models:
- alphaearth
- tessera
proposed_tags:
- cocoa_mapping
- VHR_imagery
- landscape_stratification
- tree_cover_density
- patch_density_fragmentation
- geotessera
- canopy_height_model
regions:
- ci
self_evaluation: false
tasks:
- crop_type_mapping
title: Is sub-metre resolution necessary for cocoa mapping? A landscape-stratified
  evaluation of very high resolution imagery, decametric Earth Observation inputs,
  and operational products in Cote d'Ivoire
venue: arXiv
---

## summary

This study compares VHR (0.5m Pléiades) imagery, a Sentinel-2 composite, and TESSERA/AlphaEarth Foundations embeddings for cocoa mapping in Côte d'Ivoire, using a landscape-stratified accuracy assessment across tree cover density and fragmentation gradients. VHR achieved the highest and most stable performance (F1=0.92), while among decametric inputs TESSERA (F1=0.86) outperformed AlphaEarth (F1=0.82) and Sentinel-2 (F1=0.76). Foundation-model embeddings substantially improved on conventional Sentinel-2 but did not close the gap to VHR, especially in low/high canopy-density and fragmented landscapes.

## setup

Internally trained U-Net (EfficientNet-B5 encoder) ensembles were developed per EO input (VHR, Sentinel-2 annual composite, TESSERA, AlphaEarth Foundations embeddings) using the COLD-CI reference dataset (176,935 tiles) for training/validation, then evaluated against an independent stratified sample of 2,821 photo-interpreted reference points across 9 tree-cover-density x patch-density strata, alongside four existing cocoa mapping products (BNETD, Kalischek, FDaP v2025a/b).

## caveats

Authors note the study area was constrained to 56 Pléiades scenes (not nationally representative), the spectral ablation could not fully isolate spatial resolution from other sensor/acquisition differences between VHR and S2, and a single fixed probability threshold (p≥0.5) was applied across all internally trained models rather than per-model optimized thresholds.
