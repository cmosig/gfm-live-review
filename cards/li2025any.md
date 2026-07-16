---
arxiv_id: '2512.17224'
authors:
- Xuyang Li
- Chenyu Li
- Danfeng Hong
axes:
- G3_spatial_transfer
- G2_label_scarce_efficiency
- G11_complementarity
claims:
- axis: G3_spatial_transfer
  baseline: dofa
  baseline_value: 53.8
  dataset: m-cashew-plant.
  direction: better
  id: li2025any#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: alphaearth
  span: 68.3 (+12.7)
  span_sha256: 04c9531b7c7966f582f14640fe9d2f8c87e7c138416fa556440da602322989ed
  task: semantic_segmentation
  value: 68.3
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 57.6
  dataset: SPARCS
  direction: better
  id: li2025any#c2
  label_ratio: null
  locator: Table 2
  metric: miou
  model: alphaearth
  span: 68.5 (+10.9)
  span_sha256: 14b213a00d3f87f0f3df1acea0b7b30215b4e3559fc8a368064f6139e82037d0
  task: semantic_segmentation
  value: 68.5
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 82.4
  dataset: HLS Burn Scars
  direction: better
  id: li2025any#c3
  label_ratio: null
  locator: Table 2
  metric: miou
  model: alphaearth
  span: 85.4 (+3.0)
  span_sha256: 9a9b62c5ae7d46d599f6459c9cb6e4f55f63825c720d39b59bfcb9dfde171a32
  task: semantic_segmentation
  value: 85.4
- axis: G1_label_rich_parity
  baseline: dofa
  baseline_value: 90.09
  dataset: UCM
  direction: better
  id: li2025any#c4
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: alphaearth
  span: 93.57 (+3.48)
  span_sha256: 72a5d1eb684a129584c2f01a7cc4773de4f6ecaf6271d461191f3b25f1e90686
  task: land_cover_classification
  value: 93.57
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 83.41
  dataset: BigEarthNet
  direction: better
  id: li2025any#c5
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: alphaearth
  span: 85.02 (+1.61)
  span_sha256: 9687d3969b1641057ea6674d34df4cc6bf17346edea86dad0d20e13478047b1f
  task: land_cover_classification
  value: 85.02
date: '2025-12-19'
doi: 10.48550/arxiv.2512.17224
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:59:19.240417Z'
key: li2025any
limitations:
- spatial_transfer
- data_bias
- benchmark_narrowness
models:
- croma
- dofa
proposed_tags:
- cross_sensor_generalization
- band_missing_robustness
- multi_scale_patch_embedding
- cloud_shadow_detection
- burn_scar_mapping
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- crop_type_mapping
title: 'Any-Optical-Model: A Universal Foundation Model for Optical Remote Sensing'
venue: arXiv
---

## summary

The paper introduces Any-Optical-Model (AOM), a remote sensing foundation model that handles arbitrary spectral bands and resolutions via a spectrum-independent tokenizer and multi-scale adaptive patch embedding. AOM is pretrained with a combined masked reconstruction and multi-scale semantic alignment objective on Sentinel-2, Landsat, and high-resolution RGB corpora. It outperforms prior RSFMs (SatMAE, CROMA, SpectralGPT, DOFA, AnySat, GFM, Scale-MAE, SenPaMAE) on Geo-Bench segmentation tasks, cross-sensor segmentation, and classification benchmarks.

## setup

Pretraining uses ~1.56M multi-sensor images from SSL4EO-S12 (Sentinel-2), Activefire (Landsat-8), and GeoPile/fMoW/OpenEarthMap (high-res RGB), spanning 0.1-100m resolution; ViT-Base encoder trained 220 epochs with masked reconstruction + InfoNCE alignment losses. Downstream evaluation uses partial fine-tuning (frozen backbone, UPerNet head) on Geo-Bench segmentation datasets, SPARCS and HLS Burn Scars, and linear probing on UCM and BigEarthNet classification.

## caveats

Authors note AOM's robustness to out-of-distribution modalities like hyperspectral imagery and SAR remains unevaluated, and its performance on broader tasks such as object detection and temporal prediction is underexplored.
