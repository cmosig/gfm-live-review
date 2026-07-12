---
arxiv_id: '2606.29664'
authors:
- Zhuocheng Shang
- Sanmay Das
- Ahmed Eldawy
axes:
- G3_spatial_transfer
claims:
- axis: G3_spatial_transfer
  baseline: prithvi
  baseline_value: 12.02
  dataset: Iowa
  direction: better
  id: shang2026benchmarking#c1
  label_ratio: null
  locator: Table 4; Sec 4.1
  metric: miou
  model: satmae
  span: from 45.68 crop mIoU in Iowa to 3.20 in Minnesota
  span_sha256: efd187d33d9cd0bfb5a0f0c8019de19e17aa71ae0537e5ea93d6b264bfc855e7
  task: crop_type_mapping
  value: 45.68
- axis: G3_spatial_transfer
  baseline: prithvi
  baseline_value: 3.57
  dataset: Minnesota
  direction: worse
  id: shang2026benchmarking#c2
  label_ratio: null
  locator: Table 4; Sec 4.1
  metric: miou
  model: satmae
  span: from 45.68 crop mIoU in Iowa to 3.20 in Minnesota
  span_sha256: efd187d33d9cd0bfb5a0f0c8019de19e17aa71ae0537e5ea93d6b264bfc855e7
  task: crop_type_mapping
  value: 3.2
- axis: G3_spatial_transfer
  baseline: satmae
  baseline_value: 41.1
  dataset: Iowa
  direction: better
  id: shang2026benchmarking#c3
  label_ratio: null
  locator: Table 3
  metric: f1
  model: prithvi
  span: '55.03'
  span_sha256: fbdf7ae1b68e5160c2d7e2703c677daf7e8fe38cc0607755bfd61560b8c62b52
  task: change_detection
  value: 55.03
- axis: G3_spatial_transfer
  baseline: prithvi
  baseline_value: 53.8
  dataset: North Carolina
  direction: better
  id: shang2026benchmarking#c4
  label_ratio: null
  locator: Table 3
  metric: f1
  model: satmae
  span: '55.65'
  span_sha256: 221268a072b2e35e33216cf0ba279eab732b84ab9c5d89b242342999a205909e
  task: change_detection
  value: 55.65
- axis: G3_spatial_transfer
  baseline: prithvi
  baseline_value: 23.64
  dataset: California
  direction: better
  id: shang2026benchmarking#c5
  label_ratio: null
  locator: Table 3; Sec 4.2
  metric: f1
  model: satmae
  span: F1 falls to 18.73 for SpectralGPT and 27.00 for SatMAE
  span_sha256: 694757a45a10b6a649b64ecc26be1758871c7e4e60a4b9461e2129d69ea8f034
  task: change_detection
  value: 27.0
- axis: G3_spatial_transfer
  baseline: satmae
  baseline_value: 67.89
  dataset: Minnesota
  direction: better
  id: shang2026benchmarking#c6
  label_ratio: null
  locator: Table 3
  metric: f1
  model: prithvi
  span: '83.26'
  span_sha256: 1e33316d5ae15faa6a098b3e9c9e3d7d15e79acf75f1982ef881a2b19e8878f1
  task: change_detection
  value: 83.26
date: '2026-06-29'
doi: 10.48550/arxiv.2606.29664
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:29:04.195083Z'
key: shang2026benchmarking
limitations:
- spatial_transfer
- benchmark_narrowness
- uncertainty
models:
- prithvi
- satmae
proposed_tags:
- regional_distribution_shift
- minority_crop_detection
- input_format_adaptation
- geographic_generalization
- input_adaptation_confound
regions:
- us
self_evaluation: false
tasks:
- crop_type_mapping
- land_cover_classification
- change_detection
title: Benchmarking Geospatial Foundation Models for Agriculture Applications
venue: arXiv
---

## summary

This benchmark fine-tunes Prithvi, SpectralGPT, and SatMAE on Sentinel-2 crop segmentation and change detection across four U.S. states using strict, non-overlapping train/val/test regions per state. All three geospatial foundation models degrade sharply under regional distribution shift, collapsing on minority crop classes while still fitting dominant ones. Adapting each model's pretrained architecture to a shared 18-band input configuration affects them unevenly, which the authors argue confounds direct cross-model comparison.

## setup

Sentinel-2 L2A imagery (six bands, three seasonal time points, 18-band stacked input) from the 2024 growing season, labeled with the 2024 USDA Cropland Data Layer mapped to 13 crop/land-cover classes, across Iowa, North Carolina, California, and Minnesota. Each state is split into three non-overlapping ~800-1,300 km2 regions (train/val/test); models are fine-tuned per state and evaluated only on the held-out test region for segmentation (mIoU) and bitemporal 2023-2024 change detection (F1).

## caveats

The authors note each model was run only once, so reported differences reflect observation rather than statistical significance; SatMAE segmentation was completed only for Iowa and Minnesota, with the large Iowa-to-Minnesota gap flagged as needing further auditing before being interpreted as a real model effect; and because the models differ in decoder heads and how they adapt to the shared input format, the authors caution against treating absolute cross-model differences as a clean architectural comparison.
