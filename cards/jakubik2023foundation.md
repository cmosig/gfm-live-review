---
arxiv_id: '2310.18660'
authors:
- Johannes Jakubik
- Sujit Roy
- C. E. Phillips
- Paolo Fraccaro
- Denys Godwin
- Bianca Zadrozny
- Daniela Szwarcman
- Carlos Gomes
- Gabby Nyirjesy
- Blair Edwards
- Daiki Kimura
- Naomi Simumba
- Linsong Chu
- S. Karthik Mukkavilli
- Devyani Lambhate
- Kamal Das
- Ranjini Bangalore
- Dario Oliveira
- Michal Muszynski
- Kumar Ankur
- Muthukumaran Ramasubramanian
- Iksha Gurung
- Sam Khallaghi
- Hanxi
- Li
- Michael Cecil
- Maryam Ahmadi
- Fatemeh Kordi
- Hamed Alemohammad
- Manil Maskey
- Raghu Ganti
- Kommy Weldemariam
- Rahul Ramachandran
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G1_label_rich_parity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 24.21
  dataset: Sen1Floods11
  direction: better
  id: jakubik2023foundation#c1
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: 'Baseline [55]

    24.21'
  span_sha256: df6a49d71c5ca65c16ec4e7113df4a2953fffbecae96af2a630c1c597178bbc8
  task: flood_mapping
  value: 81.26
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Sen1Floods11
  direction: better
  id: jakubik2023foundation#c2
  label_ratio: null
  locator: Sec 6.2.2
  metric: miou
  model: prithvi
  span: Prithvi achieves an IoU score of 82.99 on the target class
  span_sha256: a5e01eed2fc0ab80dfe9703551a34d5458cf41449635d9da437cc1806d1b37c2
  task: flood_mapping
  value: 82.99
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 71.01
  dataset: MTBS wildfire scars
  direction: better
  id: jakubik2023foundation#c3
  label_ratio: null
  locator: Table 3
  metric: miou
  model: prithvi
  span: surpassing a U-Net-based baseline by 2.61pp and a ViT-based baseline by 4.58pp
  span_sha256: 8a8ab734f03e062e21ec2f1a41eea4006cec28aa736643e7dedf384d4f127749
  task: change_detection
  value: 73.62
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 61.91
  dataset: Multi-Temporal Crop Segmentation (CDL)
  direction: better
  id: jakubik2023foundation#c4
  label_ratio: null
  locator: Table 4
  metric: accuracy
  model: prithvi
  span: The mean accuracy for Prithvi of 13 classes is 64.06%, and for U-Net is 61.91%
  span_sha256: 84bcc177f35f05c79c975935807e5f743f80e41da44d4aa72315bec9f0a60522
  task: crop_type_mapping
  value: 64.06
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: Sen1Floods11
  direction: better
  id: jakubik2023foundation#c5
  label_ratio: 0.1
  locator: Sec 6.2.2
  metric: miou
  model: prithvi
  span: the models still converge to an IoU of over 80% on average
  span_sha256: f2961ae8f203856e3f61ac27c4d2b26d4382f831af735ba1cfc3a96f7a38d6cd
  task: flood_mapping
  value: 80.0
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: Sen1Floods11
  direction: better
  id: jakubik2023foundation#c6
  label_ratio: null
  locator: Sec 7
  metric: miou
  model: prithvi
  span: Prithvi strongly outperforms the U-Net on data from unseen geographical regions
    (i.e., 8.6% in the IoU on the water class)
  span_sha256: 7df3e4cb2749224891694c3a37d2800cc18d457025186b2a4679221edd8a02ef
  task: flood_mapping
  value: 8.6
date: '2023-10-28'
doi: 10.48550/arxiv.2310.18660
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:51:04.420379Z'
key: jakubik2023foundation
limitations:
- benchmark_narrowness
- temporal_transfer
- compute_cost
- spatial_transfer
models:
- prithvi
proposed_tags:
- cloud_gap_imputation
- wildfire_scar_mapping
- masked_autoencoder_pretraining
- HLS_dataset
regions:
- us
self_evaluation: true
tasks:
- flood_mapping
- change_detection
- crop_type_mapping
- semantic_segmentation
title: Foundation Models for Generalist Geospatial Artificial Intelligence
venue: arXiv
---

## summary

This paper introduces Prithvi, a 100M-parameter transformer-based masked autoencoder foundation model pretrained on over 1TB of Harmonized Landsat-Sentinel 2 (HLS) multispectral imagery, along with a scalable framework for geospatial foundation model pretraining and fine-tuning. Prithvi is fine-tuned on four downstream tasks—multi-temporal cloud gap imputation, flood mapping, wildfire scar segmentation, and multi-temporal crop segmentation—showing accelerated fine-tuning, strong data efficiency, and competitive or superior performance versus task-specific baselines and off-the-shelf ViT/Swin architectures.

## setup

Pretraining used stratified-sampled, cloud-filtered HLS L30 tiles (6 spectral bands, 3D ViT-based MAE) trained on up to 64 A100 GPUs; downstream evaluation used Sen1Floods11 for flood mapping, MTBS-derived chips for wildfire scars, USDA CDL-labeled Sentinel scenes for crop segmentation, and a custom HLS dataset for cloud gap imputation, comparing fine-tuned Prithvi against non-pretrained Prithvi, off-the-shelf ViT/Swin, U-Net, and a CGAN baseline.

## caveats

The authors note the model does not significantly improve on handling seasonal changes, was pretrained only on US-region data with a fixed one-year, 3-timestep sampling assumption, occasionally underperforms dedicated task-specific U-Nets on in-distribution data (e.g., flood mapping IoU 2.5pp lower per follow-up study), and the crop segmentation results show no significant IoU improvement over U-Net.
