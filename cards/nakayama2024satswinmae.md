---
arxiv_id: '2405.02512'
authors:
- Yohei Nakayama
- Jiawei Su
- Luis M. Pazos-Outón
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 81.06
  dataset: Sen1Floods11
  direction: better
  id: nakayama2024satswinmae#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: 'ViT-base [12]


    67.58


    81.06


    88.82'
  span_sha256: 5160d6291546dd57f2f3f2d7db6a47b256e73b7d52a5d68b9bf30e015787724f
  task: flood_mapping
  value: 90.16
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: Sen1Floods11
  direction: better
  id: nakayama2024satswinmae#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: 'Prithvi [6]


    82.99


    90.16


    94.60'
  span_sha256: 67fcb04732dce0e8ce7b4e0e91ec4358e1cd67afdc7e4ee7e4a9bae9aafba4b5
  task: flood_mapping
  value: 90.16
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.42
  dataset: USDA Crop Data Layer (CDL) multi-temporal crop segmentation
  direction: better
  id: nakayama2024satswinmae#c3
  label_ratio: null
  locator: Table 3
  metric: miou
  model: prithvi
  span: 'U-Net (DeepLabV3) [25]


    0.420


    61.91'
  span_sha256: 778ec5f78a8d3bf6bd605a25960b73b0364ff9ec359d19c9298f9e5537a622e5
  task: crop_type_mapping
  value: 0.426
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: null
  dataset: PhilEO Bench
  direction: better
  id: nakayama2024satswinmae#c4
  label_ratio: null
  locator: Abstract
  metric: accuracy
  model: prithvi
  span: it outpeforms other geospatial foundation models with a 10.4% higher accuracy
  span_sha256: ed0c0edb3db7c7041f6145589ea66ac3e3e1a524b30750a1cf0bd232c01d7a80
  task: land_cover_classification
  value: 10.4
date: '2024-05-03'
doi: 10.48550/arxiv.2405.02512
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:53:48.323112Z'
key: nakayama2024satswinmae
limitations:
- benchmark_narrowness
- human_semantics
models:
- prithvi
proposed_tags:
- swin_transformer
- video_swin_transformer
- masked_autoencoder
- swinunet
- building_density_estimation
- wildfire_scar_mapping
- satswinmae
regions:
- global
- us
self_evaluation: false
tasks:
- land_cover_classification
- flood_mapping
- crop_type_mapping
- semantic_segmentation
title: 'SatSwinMAE: Efficient Autoencoding for Multiscale Time-series Satellite Imagery'
venue: arXiv
---

## summary

SatSwinMAE extends SwinMAE and SwinUNet with a temporal component to pretrain a hierarchical 3D Masked Autoencoder on multi-seasonal Sentinel imagery, then finetunes via a Swin-UNet architecture with skip connections for downstream Earth observation tasks. The model outperforms existing foundation models such as SatMAE, SeCo and Prithvi on land cover segmentation, building density, flood mapping, wildfire scar mapping and multi-temporal crop segmentation.

## setup

Pretrained on SSL4EO-S12 (250,000 global locations, multi-seasonal Sentinel-1/2 imagery, 6 spectral bands used) with a window-masking MAE objective; evaluated on PhilEO Bench (land cover, building density) and the Prithvi benchmark suite (Sen1Floods11 flood mapping, MTBS wildfire scars, USDA CDL multi-temporal crop segmentation).

## caveats

Authors note the Geo-Aware UNet on PhilEO Bench, which uses supervised geo-aware pretraining (coordinates, capture time, climate zone), performs similarly or slightly better on land cover, suggesting their purely self-supervised approach could benefit from incorporating geo-aware pretext tasks in future work.
