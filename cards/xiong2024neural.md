---
arxiv_id: '2403.15356'
authors:
- Zhitong Xiong
- Yi Wang
- Fahong Zhang
- Adam J. Stewart
- Joëlle Hanna
- Damian Borth
- Ioannis Papoutsis
- Bertrand Le Saux
- Gustau Camps-Valls
- Xiao Xiang Zhu
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G6_compactness
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 90.1
  dataset: m-eurosat
  direction: better
  id: xiong2024neural#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: dofa
  span: DOFA ViT-L 67.5 54.6 96.9 97.3 60.1 97.1
  span_sha256: e6f33aad7a32b921507ecf4d3f32fe26b952b00e849995f708dd361b318d4a57
  task: land_cover_classification
  value: 97.1
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 63.8
  dataset: m-chesapeake
  direction: better
  id: xiong2024neural#c2
  label_ratio: null
  locator: Table 2
  metric: miou
  model: dofa
  span: DOFA+ ViT-L 95.7 83.5 63.8 60.2 33.2 71.6
  span_sha256: ce89ab05a6c47bba5daf28d56bf1448a3140de12f5321402f44e9662107df2b8
  task: semantic_segmentation
  value: 71.6
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 81.03
  dataset: Sen1Floods11
  direction: better
  id: xiong2024neural#c3
  label_ratio: null
  locator: Table 6
  metric: f1
  model: dofa
  span: RGB + CA + RE1 + RE2 + RE3 + NIR Broad + NIR Narrow + Water Vapor + Cirrus
    + SWIR1 + SWIR2
  span_sha256: 2837f6e28a6ffbc55bf44113aa49151d0528af3649ffe682f6233aefeb5ad0dd
  task: flood_mapping
  value: 92.51
- axis: G1_label_rich_parity
  baseline: croma
  baseline_value: 55.72
  dataset: PANGEA (Avg. mIoU)
  direction: better
  id: xiong2024neural#c4
  label_ratio: null
  locator: Table 3
  metric: miou
  model: dofa
  span: DOFA+ attains the highest average mIoU of 59.81
  span_sha256: ca6c0a73c6f7d06f6a6dac96fbd05b06c5cdf3172283d9fe6a63a5ed95f037cf
  task: semantic_segmentation
  value: 59.81
- axis: G5_cost
  baseline: task_specific
  baseline_value: null
  dataset: RESISC-45
  direction: better
  id: xiong2024neural#c5
  label_ratio: null
  locator: Sec 4.5
  metric: accuracy
  model: dofa
  span: DOFA+ achieves SOTA performance on the RESISC-45 classification benchmark
    with 98.1% accuracy
  span_sha256: 2a4542841b029063ef283cb679db4744510e512f05565f408d96107c593aa7b6
  task: land_cover_classification
  value: 98.1
date: '2024-03-22'
doi: 10.48550/arxiv.2403.15356
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:28:00.638332Z'
key: xiong2024neural
limitations:
- compute_cost
- benchmark_narrowness
- spatial_transfer
models:
- dofa
- clay
- croma
- presto
- satmae
- scalemae
proposed_tags:
- hypernetwork
- wavelength_conditioning
- continual_pretraining
- knowledge_distillation
- object_detection
- DIOR
- RESISC45
- PANGEA_benchmark
- GEO-Bench
regions:
- global
self_evaluation: true
tasks:
- land_cover_classification
- semantic_segmentation
- crop_type_mapping
- flood_mapping
- representation_probing
title: Neural Plasticity-Inspired Multimodal Foundation Model for Earth Observation
venue: arXiv
---

## summary

The paper introduces DOFA, a wavelength-conditioned hypernetwork-based foundation model that flexibly processes five EO sensor modalities within a single Transformer backbone, and DOFA+, a lightweight distillation-based variant seeded from DINOv2. Both models are evaluated across GEO-Bench classification/segmentation, PANGEA benchmark, RESISC45 classification, and DIOR object detection, consistently outperforming prior EO foundation models while using substantially less pretraining data and compute. Ablations show performance scales with number of spectral bands used and pretraining epochs.

## setup

Pretraining uses ~11.5M images across Sentinel-1, Sentinel-2, Gaofen, NAIP, and EnMAP with masked image modeling and feature distillation from an ImageNet-pretrained teacher (DOFA) or DINOv2 (DOFA+). Downstream evaluation covers GEO-Bench (6 classification + 6 segmentation datasets), PANGEA benchmark (8 tasks), RESISC45 classification, and DIOR object detection, under linear probing, decoder fine-tuning, or full fine-tuning protocols.

## caveats

The authors note some datasets/models have missing values due to inability to adapt to certain domains; TerraMindv1-L still outperforms DOFA+ on the MADOS dataset; and DOFA+ relies on hyperparameters tuned per dataset via index selection for intermediate layer combination in PANGEA experiments.
