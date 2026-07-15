---
arxiv_id: '2502.09356'
authors:
- Gabriel Tseng
- Anthony Fuller
- Marlena Reil
- Henry Herzog
- Patrick Beukema
- Favyen Bastani
- James R. Green
- Evan Shelhamer
- Hannah Kerner
- David Rolnick
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 85.6
  dataset: m-EuroSat
  direction: better
  id: tseng2025galileo#c1
  label_ratio: 1.0
  locator: Table 3
  metric: accuracy
  model: galileo
  span: Galileo-Base is the best model for im- age classification (%) by kNN
  span_sha256: e076d7c00dd12a8fa480255234124c59c1c18b40e634d80cebcc1796264028f2
  task: land_cover_classification
  value: 93.0
- axis: G2_label_scarce_efficiency
  baseline: croma
  baseline_value: 51.3
  dataset: m-EuroSat
  direction: better
  id: tseng2025galileo#c2
  label_ratio: 0.01
  locator: Table 3
  metric: accuracy
  model: galileo
  span: Galileo-Base is the best model for im- age classification (%) by kNN
  span_sha256: e076d7c00dd12a8fa480255234124c59c1c18b40e634d80cebcc1796264028f2
  task: land_cover_classification
  value: 56.6
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 78.9
  dataset: Sen1Floods11
  direction: better
  id: tseng2025galileo#c3
  label_ratio: 1.0
  locator: Table 5
  metric: miou
  model: galileo
  span: The Galileo models excel at image segmentation measured by % mIoU via lin-
    ear probing
  span_sha256: 39cc80f25cee8597ea2834a0522eef6aa357b98003185042847459302d52634c
  task: flood_mapping
  value: 79.4
- axis: G9_ecological_fine_scale
  baseline: croma
  baseline_value: 64.2
  dataset: MADOS
  direction: better
  id: tseng2025galileo#c4
  label_ratio: 1.0
  locator: Table 5
  metric: miou
  model: galileo
  span: The Galileo models excel at image segmentation measured by % mIoU via lin-
    ear probing
  span_sha256: 39cc80f25cee8597ea2834a0522eef6aa357b98003185042847459302d52634c
  task: semantic_segmentation
  value: 67.6
- axis: G11_complementarity
  baseline: presto
  baseline_value: 84.0
  dataset: CropHarvest
  direction: better
  id: tseng2025galileo#c5
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: galileo
  span: The Galileo models are the best (-Base) and second-best (-Tiny) models for
    pixel timeseries classification
  span_sha256: 07089362ee16bac847972d374c70da83706efe31a1502e4f500e551baf922f6a
  task: crop_type_mapping
  value: 84.2
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 58.91
  dataset: EuroSat
  direction: better
  id: tseng2025galileo#c6
  label_ratio: null
  locator: Table 7
  metric: accuracy
  model: galileo
  span: Deep targets combined with structured space-time mask- ing excels in global
    feature extraction
  span_sha256: af73c23b684909c8c3e623b1e96599dbcad9aebedd8924f8c6178c288cae2dd5
  task: representation_probing
  value: 89.5
date: '2025-02-13'
doi: 10.48550/arxiv.2502.09356
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T22:44:54.963760Z'
key: tseng2025galileo
limitations:
- benchmark_narrowness
- compute_cost
- human_semantics
models:
- galileo
- presto
- croma
- satmae
- dofa
- scalemae
proposed_tags:
- multimodal_pretraining
- self_supervised_learning
- global_local_features
- masked_modeling
- patch_size_tradeoff
regions:
- global
self_evaluation: true
tasks:
- land_cover_classification
- crop_type_mapping
- flood_mapping
- semantic_segmentation
- representation_probing
- local_climate_zone_classification
title: 'Galileo: Learning Global & Local Features of Many Remote Sensing Modalities'
venue: arXiv
---

## summary

Galileo is a multimodal, multi-scale self-supervised transformer trained on nine remote sensing modalities (optical, SAR, elevation, weather, pseudo-labels, etc.) using dual global (deep, structured-masked) and local (shallow, unstructured-masked) contrastive objectives. Across eleven benchmarks spanning image classification, segmentation, and pixel time series, Galileo-Base outperforms specialist image models (CROMA, SatMAE) and pixel time-series models (Presto) with a single set of weights.

## setup

Pretrained on 127,155 globally sampled instances (24 monthly timesteps, 96x96px, 10m/pixel) covering Sentinel-1/2, elevation, Dynamic World, World Cereal, weather (ERA5, TerraClimate), nightlights, and population data. Evaluated via kNN, linear probing, and finetuning on GeoBench (m-EuroSat, m-BigEarthNet, m-So2Sat, m-Brick-Kiln, m-Cashew-Plant, m-SA-Crop-Type), MADOS, Sen1Floods11, PASTIS, Breizhcrops, and CropHarvest.

## caveats

The PatchDisc contrastive loss alone is prone to collapse/shortcut exploitation of position embeddings, requiring the batch-negative PatchDiscB fix; single global or local objectives alone excel at only classification or segmentation respectively, not both, and single-objective training is less consistent across runs (63% success vs 100% for the dual objective).
