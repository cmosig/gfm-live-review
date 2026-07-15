---
arxiv_id: '2404.01260'
authors:
- Boran Han
- Shuai Zhang
- Xingjian Shi
- Markus Reichstein
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G11_complementarity
- G3_spatial_transfer
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 89.5
  dataset: BigEarthNet
  direction: better
  id: han2024bridging#c1
  label_ratio: 1.0
  locator: Table 3
  metric: accuracy
  model: presto
  span: IN-22k [36] 85.7 89.5
  span_sha256: 934676d74b6c8ba62a608455bf5784f6313a333c227508ddf4be0a65a2cbec64
  task: land_cover_classification
  value: 92.9
date: '2024-04-01'
doi: 10.48550/arxiv.2404.01260
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:54:07.611724Z'
key: han2024bridging
limitations:
- temporal_transfer
- compute_cost
- data_bias
models: []
proposed_tags:
- cross_sensor_pretraining
- cloud_removal
- pan_sharpening
- multisensor_fusion
- SAR
- DSM
- msGFM
- mixture_of_experts
- masked_image_modeling
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- change_detection
title: Bridging Remote Sensors with Multisensor Geospatial Foundation Models
venue: arXiv
---

## summary

The paper introduces msGFM, a multisensor geospatial foundation model pretrained on ~2M paired/unpaired images spanning RGB, Sentinel-2, SAR, and DSM sensors using a cross-sensor masked image modeling approach. It outperforms existing single-sensor geospatial and vision pretraining methods on scene classification, segmentation, cloud removal, and pan-sharpening downstream tasks. None of the tracked foundation models (clay, croma, dofa, galileo, presto, prithvi, satclip, satmae, scalemae, alphaearth, geoclip, tessera) are evaluated in this paper.

## setup

Pretraining data (GeoPile-2) combines GeoPile, MillionAID, SEN12MS (paired SAR/Sentinel-2), and MDAS (paired DSM/RGB) totaling ~2M images; downstream evaluation uses BigEarthNet (classification), Vaihingen (segmentation), SEN12MS-CR (cloud removal), and SpaceNet2 (pan-sharpening) with a Swin-base backbone and SimMIM-style masked reconstruction plus Mixture-of-Experts layers.

## caveats

The authors note SAR self/cross-reconstruction is challenging due to noisy, unprocessed SAR images and MIM's tendency to reconstruct only low-frequency components; they also flag that incorporating temporal information would substantially increase pretraining cost and requires rethinking methodological design rather than just adding data.
