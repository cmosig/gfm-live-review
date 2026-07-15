---
arxiv_id: '2412.02732'
authors:
- Daniela Szwarcman
- Sujit Roy
- Paolo Fraccaro
- Þorsteinn Elí Gíslason
- Benedikt Blumenstiel
- Rinki Ghosal
- Pedro Henrique de Oliveira
- Joao Lucas de Sousa Almeida
- Rocco Sedona
- Yanghui Kang
- Srija Chakraborty
- Sizhe Wang
- Carlos Gomes
- Ankur Kumar
- Myscon Truong
- Denys Godwin
- Hyunho Lee
- Chia-Yu Hsu
- Rohit Lal
- Ata Akbari Asanjan
- Besart Mujeci
- Disha Shidham
- Trevor Keenan
- Paulo Arevalo
- Wenwen Li
- Hamed Alemohammad
- Pontus Olofsson
- Christopher Hain
- Robert Kennedy
- Bianca Zadrozny
- David Bell
- Gabriele Cavallaro
- Campbell Watson
- Manil Maskey
- Rahul Ramachandran
- Juan Bernabe Moreno
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 42.6
  dataset: US multi-temporal crop segmentation
  direction: better
  id: szwarcman2024prithvi#c1
  label_ratio: null
  locator: Table IX
  metric: miou
  model: prithvi
  span: the 600M variant achieved the best performance, with a mIoU of 50.7% and mAcc
    of 68.8%
  span_sha256: 69d132364e8ab5527d4769fb7cb87a76b8db5fa3e65544e7cc45292caea722be
  task: crop_type_mapping
  value: 50.7
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 27.49
  dataset: BioMassters
  direction: worse
  id: szwarcman2024prithvi#c2
  label_ratio: null
  locator: Table XIII
  metric: rmse
  model: prithvi
  span: It achieved an RMSE of 27.49 in the holdout test set.
  span_sha256: a16f28e09954d948f45e8e07ccfaf364ec66a5b5bdb7c25a5de15b791c6519a7
  task: biomass_estimation
  value: 33.4
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 52.9
  dataset: PASTIS
  direction: better
  id: szwarcman2024prithvi#c3
  label_ratio: 1.0
  locator: Table XII
  metric: miou
  model: prithvi
  span: '53.4'
  span_sha256: 09d0b824eb721156f8091b8aded4879102d0c41b31467c9572db71fdb90e0cdd
  task: crop_type_mapping
  value: 53.4
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.68
  dataset: FLUXNET/AmeriFlux/ICOS GPP flux towers
  direction: better
  id: szwarcman2024prithvi#c4
  label_ratio: null
  locator: Table XV
  metric: r2
  model: prithvi
  span: '0.88'
  span_sha256: e2819fbe22224ae04f453ed6e908e2f66e42d761b045db7c5f8b213411e68f9f
  task: representation_probing
  value: 0.88
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 81.5
  dataset: Sen4Map crop type classification
  direction: better
  id: szwarcman2024prithvi#c5
  label_ratio: 1.0
  locator: Table XI
  metric: f1
  model: prithvi
  span: '84.6'
  span_sha256: 55be7e59f59dc7e34676667768618236a96b808b7948b8558e8fa447d4c16f6e
  task: crop_type_mapping
  value: 84.6
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 72.7
  dataset: Sen4Map land cover classification
  direction: better
  id: szwarcman2024prithvi#c6
  label_ratio: 1.0
  locator: Table X
  metric: f1
  model: prithvi
  span: '76.1'
  span_sha256: 25d6ca607c2382de858b2c365ec4b35e5602411b4a02554ccbde89dc33f744bf
  task: land_cover_classification
  value: 76.1
date: '2024-12-03'
doi: 10.48550/arxiv.2412.02732
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T22:33:47.273351Z'
key: szwarcman2024prithvi
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
- spatial_transfer
- temporal_transfer
- mixed_pixels
models:
- prithvi
- dofa
- scalemae
- presto
proposed_tags:
- multi_temporal_pretraining
- location_time_embeddings
- GEO-Bench
- GPP_estimation
- eddy_covariance
- LoRA_finetuning
- BAER_burn_intensity
regions:
- global
- us
- fr
- fi
self_evaluation: true
tasks:
- flood_mapping
- landslide_susceptibility
- crop_type_mapping
- land_cover_classification
- biomass_estimation
- semantic_segmentation
- representation_probing
title: 'Prithvi-EO-2.0: A Versatile Multi-Temporal Foundation Model for Earth Observation
  Applications'
venue: arXiv
---

## summary

Prithvi-EO-2.0 is a multi-temporal geospatial foundation model pretrained on 4.2M global HLS time series samples with added temporal and location embeddings, scaled up to 600M parameters. It outperforms its US-only predecessor by 8% on GEO-Bench and beats six other GFMs across benchmarking and SME-led downstream tasks in disaster response, land cover/crop mapping, and ecosystem dynamics. The models and TerraTorch tooling are released openly on Hugging Face and GitHub.

## setup

Evaluated via GEO-Bench (six classification + six segmentation datasets, ten hyperparameter trials, ten repeated seeded runs) against six other GFMs and Prithvi-EO-1.0, plus SME-led downstream benchmarks (Sen1Floods11, HLS burn scars, BAER burn intensity, Landslide4Sense, US crop segmentation, Sen4Map, PASTIS, BioMassters, and FLUXNET/AmeriFlux/ICOS GPP data). Fine-tuning used UPerNet/FCN decoders, LoRA for some tasks, and task-specific baselines (U-Net, U-TAE, ViViT, random forest/XGBoost/ResNet18).

## caveats

Authors note optical-only Prithvi-EO underperforms multimodal (SAR+optical) baselines in high-biomass regions due to canopy reflectance saturation; the m-cashew-plant benchmark score is skewed by a train/test class mismatch; and no single timestamp-selection strategy is optimal globally given regionally varying temporal dynamics.
