---
arxiv_id: '2501.02035'
authors:
- Stella Girtsou
- Emiliano Diaz Salas-Porras
- Lilli Freischem
- Joppe Massant
- Kyriaki-Margarita Bintsi
- Guiseppe Castiglione
- William Jones
- Michael Eisinger
- Emmanuel Johnson
- Anna Jungbluth
axes:
- G4_temporal_transfer
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 3.73
  dataset: MSG/SEVIRI + CloudSat/CPR profiles
  direction: better
  id: girtsou2025cloud#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: satmae
  span: '3.73'
  span_sha256: e5f1b17e201583091ae8669c78ff8c1f3a7bb8a6ec7168b404c17a9c295e0318
  task: representation_probing
  value: 3.18
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 3.73
  dataset: MSG/SEVIRI + CloudSat/CPR profiles
  direction: better
  id: girtsou2025cloud#c2
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: presto
  span: MAE ViT-small 8
  span_sha256: bcbd1d4963debfcfb0bd00538904844c57da979e7b96110a2fd70434e11377ab
  task: representation_probing
  value: 3.22
date: '2025-01-03'
doi: 10.48550/arxiv.2501.02035
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:22:57.144988Z'
key: girtsou2025cloud
limitations:
- benchmark_narrowness
- data_bias
- uncertainty
models: []
proposed_tags:
- 3d_cloud_reconstruction
- masked_autoencoder
- satmae_adaptation
- cloudsat_radar_reflectivity
- msg_seviri_imagery
- vision_transformer
- u_net_baseline
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: 3D Cloud reconstruction through geospatially-aware Masked Autoencoders
venue: arXiv
---

## summary

This paper applies Masked Autoencoders and a geospatially-aware SatMAE variant to MSG/SEVIRI imagery, pre-training self-supervised and fine-tuning on paired CloudSat/CPR radar reflectivity data to reconstruct 3D cloud structures. The SatMAE model with added temporal and spatial coordinate encodings outperforms both a standard MAE and a U-Net baseline, particularly in the tropical convection belt.

## setup

Pre-training uses hourly MSG/SEVIRI 11-channel imagery split into 256x256 patches (1.2M patches) from 2010; fine-tuning uses ~47k image-profile pairs matching MSG/SEVIRI images to CloudSat/CPR radar reflectivity profiles (125 vertical bins), with temporal train/val/test splits by day groupings. Models compared: U-Net (Brüning et al. baseline), standard MAE (ViT-S/ViT-B), and SatMAE with time/coordinate encodings, evaluated via RMSE, PSNR, SSIM, and segmentation F1.

## caveats

The authors note the reported mean/std metrics in Table 1 do not represent actual model uncertainties; largest errors occur for Nimbostratus and deep convection cloud types; clear-sky measurements remain vastly over-represented even after filtering to tracks with ≥20% cloud cover; the study only covers one year of CloudSat data and improvements are described as moderate on average.
