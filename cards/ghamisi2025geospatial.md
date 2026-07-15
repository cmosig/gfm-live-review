---
arxiv_id: '2505.24528'
authors:
- Pedram Ghamisi
- Weikang Yu
- Xiaokang Zhang
- Aldino Rizaldy
- Jian Wang
- Chufeng Zhou
- Richard Gloaguen
- Gustau Camps-Valls
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
claims: []
date: '2025-05-30'
doi: 10.48550/arxiv.2505.24528
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:48:18.288089Z'
key: ghamisi2025geospatial
limitations:
- compute_cost
- data_bias
- benchmark_narrowness
models:
- scalemae
- dofa
proposed_tags:
- SustainFM
- SDG-aligned-benchmark
- CROMA
- RemoteCLIP
- SoftCon
- GFM-Swin
- Prithvi
- SpectralGPT
- SSL4EO-S12
- SatlasNet
- energy_efficiency
- carbon_footprint
regions:
- global
self_evaluation: false
tasks:
- change_detection
- flood_mapping
- land_cover_classification
- semantic_segmentation
- wealth_mapping
- poverty_mapping
- population_density
- socioeconomic_estimation
- urban_signal_mapping
title: Geospatial Foundation Models to Enable Progress on Sustainable Development
  Goals
venue: arXiv
---

## summary

The paper introduces SustainFM, a benchmark of 16 EO datasets aligned with the first 16 SDGs, used to evaluate ten geospatial foundation models against traditional deep learning baselines (ViT, ResNet-50) across accuracy, label efficiency, and energy/carbon cost. It finds FMs often but not universally outperform traditional approaches, and argues evaluation should include transferability, generalization, and energy efficiency alongside accuracy.

## setup

16 SDG-aligned EO tasks (regression, classification, segmentation, change detection) spanning sensors like Landsat, Sentinel-1/2, VIIRS, Gaofen-2, HLS, Google Earth, and PlanetScope at 0.5-30m resolution across six continents; ten pretrained FMs (CROMA, DOFA, GFM-Swin, Prithvi, RemoteCLIP, SatlasNet, ScaleMAE, SpectralGPT, SSL4EO-S12, SoftCon) are fine-tuned (decoder-only vs full) and compared to ViT/ResNet-50 trained from scratch, with performance measured via RMSE/mF1 and energy/CO2 tracked via CodeCarbon.

## caveats

The authors note that reported energy figures only reflect fine-tuning (not full pretraining) due to impracticality of training FMs from scratch; they flag that many geospatial FMs are undertrained relative to their scale limiting generalization, that standard CV pretraining objectives poorly match EO data's spectral/temporal/physical properties, and that EO datasets carry geographic, sensor, and socioeconomic biases that can propagate into model predictions.
