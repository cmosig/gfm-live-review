---
arxiv_id: '2603.07463'
authors:
- Xiaokang Zhang
- Bo Li
- Chufeng Zhou
- Weikang Yu
- Lefei Zhang
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G7_interpretability
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 54.23
  dataset: FOD
  direction: better
  id: zhang2026sigmae#c1
  label_ratio: null
  locator: Table 4
  metric: miou
  model: dofa
  span: SIGMAE 61.21 68.87 76.54 64.72
  span_sha256: 676788c740f1ece60925dfc69c3812ed989a3491c488cbcebf09ff2bb80e376e
  task: semantic_segmentation
  value: 61.21
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 85.79
  dataset: Wildfire Detection
  direction: better
  id: zhang2026sigmae#c2
  label_ratio: null
  locator: Table 4
  metric: miou
  model: scalemae
  span: SIGMAE 61.21 68.87 76.54 64.72 91.10 91.02
  span_sha256: 5625fa22fdb3dfd4e97010f8bc3d65634a551f849c4d09b63764df0e048a1fd7
  task: semantic_segmentation
  value: 91.1
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 55.81
  dataset: OSCD
  direction: better
  id: zhang2026sigmae#c3
  label_ratio: null
  locator: Table 4
  metric: miou
  model: dofa
  span: SIGMAE 61.21 68.87 76.54 64.72 91.10 91.02 92.92 90.21 66.72 76.33
  span_sha256: 3223b1d8a8d2a8ca28f81ccfdd6919bd4b3875f42864c61cc99a6225fb8161e6
  task: change_detection
  value: 66.72
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 94.55
  dataset: EuroSAT
  direction: better
  id: zhang2026sigmae#c4
  label_ratio: null
  locator: Table 4
  metric: miou
  model: scalemae
  span: SIGMAE 61.21 68.87 76.54 64.72 91.10 91.02 92.92 90.21 66.72 76.33 78.29 74.65
    96.09
  span_sha256: 5e77d0a9653c5a3c4d51a97af6a1a15a0ad922c983ffe1935ad7afd598d27009
  task: land_cover_classification
  value: 96.09
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 59.8
  dataset: SegMunich
  direction: better
  id: zhang2026sigmae#c5
  label_ratio: null
  locator: Table 5
  metric: f1
  model: dofa
  span: SIGMAE 90.14 81.09 32.71 63.65 89.37 85.09 22.26 48.88 55.15 50.51 31.31 77.05
    64.47 60.90
  span_sha256: 219e9f2bafb2fc162a3dc9940643f87918783f3a1cffa39e645ddca9132bf4ae
  task: land_cover_classification
  value: 60.9
date: '2026-03-08'
doi: 10.48550/arxiv.2603.07463
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:41:34.697789Z'
key: zhang2026sigmae
limitations:
- benchmark_narrowness
- compute_cost
- interpretability
models: []
proposed_tags:
- spectral_index_guided_masking
- curriculum_masking
- MAE_pretraining
- floating_objects_detection
- wildfire_detection
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- change_detection
- land_cover_classification
- representation_probing
title: 'SIGMAE: A Spectral-Index-Guided Foundation Model for Multispectral Remote
  Sensing'
venue: arXiv
---

## summary

SIGMAE is a spectral-index-guided masked autoencoder for multispectral remote sensing that uses NDVI/NDWI/NDBI-derived saliency to dynamically mask informative patches during pretraining. It is pretrained on BigEarthNet-S2 and evaluated across five downstream datasets spanning classification, segmentation, and change detection, generally outperforming other geospatial foundation model baselines while being smaller and using less pretraining data.

## setup

Pretraining uses BigEarthNet-S2 (590,326 Sentinel-2 patches, 10 bands). Downstream evaluation covers FOD (floating object segmentation), Wildfire Detection, EuroSAT (classification), SegMunich (segmentation), and OSCD (change detection), compared against CROMA, S12-MAE, SatlasNet, ScaleMAE, SpectralGPT, DOFA, and SoftCon foundation models.

## caveats

The authors note SIGMAE is designed for a single modality (multispectral only) unlike multimodal foundation models, its performance inherently depends on the quality of the chosen spectral indices as domain knowledge, and evaluation is limited to mainstream multispectral datasets, with multimodal pretraining left to future work.
