---
arxiv_id: '2311.00566'
authors:
- Anthony Fuller
- Koreen Millard
- James R. Green
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G7_interpretability
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: satmae
  baseline_value: 99.35
  dataset: EuroSAT
  direction: better
  id: fuller2023croma#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: croma
  span: '99.35/

    98.98*'
  span_sha256: b2a31b72befcf468cd93c0a688d0063726e796f36efe4b80d155323b46eeebd8
  task: land_cover_classification
  value: 99.46
- axis: G1_label_rich_parity
  baseline: satmae
  baseline_value: 74.06
  dataset: Canadian Cropland
  direction: better
  id: fuller2023croma#c2
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: croma
  span: '74.06'
  span_sha256: 137d0efeabce90d4e1394bb608b1c731a19721deb27953a04be321bc86c7dda7
  task: crop_type_mapping
  value: 78.07
- axis: G9_ecological_fine_scale
  baseline: satmae
  baseline_value: 58.17
  dataset: MARIDA
  direction: better
  id: fuller2023croma#c3
  label_ratio: null
  locator: Table 3
  metric: miou
  model: croma
  span: '65.56'
  span_sha256: fb6c4e638f229fe87c6b31eed8150b529d36f11b8a3ba5199e2917766ab4e683
  task: semantic_segmentation
  value: 65.56
- axis: G9_ecological_fine_scale
  baseline: satmae
  baseline_value: 51.03
  dataset: DW-Expert
  direction: better
  id: fuller2023croma#c4
  label_ratio: null
  locator: Table 3
  metric: miou
  model: croma
  span: '58.55'
  span_sha256: 42f7652b3b6a83227b8360ac24017af3c52bfbb897979e6dd07bdc70426e0734
  task: semantic_segmentation
  value: 58.55
- axis: G9_ecological_fine_scale
  baseline: satmae
  baseline_value: 45.53
  dataset: DFC2020
  direction: better
  id: fuller2023croma#c5
  label_ratio: null
  locator: Table 3
  metric: miou
  model: croma
  span: '45.53'
  span_sha256: 072db43323c7150fb298e9305255afca8dcea2d2a952ef46edc77dcc9c82fda6
  task: semantic_segmentation
  value: 46.67
- axis: G11_complementarity
  baseline: null
  baseline_value: null
  dataset: BigEarthNet
  direction: better
  id: fuller2023croma#c6
  label_ratio: null
  locator: Table 4
  metric: f1
  model: croma
  span: 'SatViT-V2 [74]

    79.80'
  span_sha256: c56f4c75f40feb4c56e3846c9b76ade29865fcacdcd50b23efa85c1402cfe796
  task: land_cover_classification
  value: 86.24
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: 79.4
  dataset: BigEarthNet (1%)
  direction: better
  id: fuller2023croma#c7
  label_ratio: 0.01
  locator: Table 5
  metric: f1
  model: croma
  span: 'DeCUR

    73.7

    79.4'
  span_sha256: 693a063c3cb5a7a9ce74a7c8aab397ee4ebeec4224d6062b245cd230d0227dbf
  task: representation_probing
  value: 81.8
date: '2023-11-01'
doi: 10.48550/arxiv.2311.00566
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T09:24:57.258646Z'
key: fuller2023croma
limitations:
- data_bias
- benchmark_narrowness
- interpretability
models:
- croma
- satmae
proposed_tags:
- radar_optical_fusion
- input_size_extrapolation
- relative_position_encoding
- contrastive_reconstruction_pretraining
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- crop_type_mapping
- representation_probing
title: 'CROMA: Remote Sensing Representations with Contrastive Radar-Optical Masked
  Autoencoders'
venue: arXiv
---

## summary

CROMA is a self-supervised framework combining contrastive and masked-reconstruction objectives to learn unimodal and multimodal representations from spatially aligned Sentinel-1 SAR and Sentinel-2 optical imagery. It introduces 2D-ALiBi and X-ALiBi relative position biases that improve representation quality and allow extrapolation to much larger test-time image sizes. CROMA outperforms SatMAE and other baselines across classification, segmentation, and multimodal probing benchmarks.

## setup

Models are pretrained on the SSL4EO-S12 dataset (1M paired Sentinel-1/2 samples) and evaluated on BigEarthNet, fMoW-Sentinel, EuroSAT, Canadian Cropland (classification), and DFC2020, DW-Expert, MARIDA (segmentation), plus multimodal probing benchmarks, all under standardized finetuning/probing/kNN/K-means protocols.

## caveats

The authors note SSL4EO's geographic sampling is biased toward human settlements, underrepresenting sparsely populated regions like the Amazon, Sahara, and Australian outback, which could degrade representation quality there; they also flag distribution shift between finetuning and inference geography as a concern for downstream decision-making.
