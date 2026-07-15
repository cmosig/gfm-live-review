---
arxiv_id: '2409.09907'
authors:
- Karthick Panner Selvam
- Raul Ramos-Pollan
- Freddie Kalaitzis
axes:
- G2_label_scarce_efficiency
- G5_cost
- G3_spatial_transfer
claims:
- axis: G5_cost
  baseline: clay
  baseline_value: 84.2
  dataset: WorldFlood (Sentinel-1)
  direction: better
  id: selvam2024rapid#c1
  label_ratio: null
  locator: Table 1
  metric: f1
  model: clay
  span: LoRA Fine-tuning r-256 90.86
  span_sha256: e8dc9566b6291be8e64cd65b9cf7e225c81bfaa0ae11223642bf0798bece3853
  task: flood_mapping
  value: 90.86
- axis: G5_cost
  baseline: clay
  baseline_value: 0.72
  dataset: WorldFlood (Sentinel-1)
  direction: better
  id: selvam2024rapid#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: clay
  span: improving F1 score by 6.66 points and IoU by 0.11
  span_sha256: 7ee0c46b67b38e9f56cdfa48f1c70425a297428cb4fab40c6450bf054fd0388c
  task: flood_mapping
  value: 0.83
- axis: G3_spatial_transfer
  baseline: clay
  baseline_value: 41.09
  dataset: Luxembourg flood event (OOD)
  direction: better
  id: selvam2024rapid#c3
  label_ratio: null
  locator: Table 2
  metric: f1
  model: clay
  span: LoRA r-1024 achieved the best overall OOD performance with an F1 score of
    48.60 and IoU of 32.10
  span_sha256: 768bb7e3968f911d6e64969b9f76803d60ce01ae5d92387302e7fa5f44a16645
  task: flood_mapping
  value: 48.6
date: '2024-09-16'
doi: 10.48550/arxiv.2409.09907
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:56:22.272296Z'
key: selvam2024rapid
limitations:
- compute_cost
- spatial_transfer
- data_bias
models:
- clay
proposed_tags:
- LoRA
- parameter_efficient_fine_tuning
regions:
- lu
self_evaluation: false
tasks:
- flood_mapping
title: Rapid Adaptation of Earth Observation Foundation Models for Segmentation
venue: arXiv
---

## summary

The paper applies LoRA to the Clay EO foundation model's encoder for Sentinel-1 SAR flood segmentation, comparing full fine-tuning, frozen-encoder, and LoRA at various ranks. LoRA (rank 256) achieves the best in-distribution performance while using far fewer trainable parameters than full fine-tuning, which is infeasible on a 40GB GPU. Out-of-distribution testing on a Luxembourg flood event shows LoRA generally generalizes better than the frozen-encoder baseline, though performance drops substantially compared to in-distribution results.

## setup

Experiments use the WorldFlood dataset (originally Sentinel-2, adapted to Sentinel-1 SAR VV/VH ascending/descending) with original train/val/test splits, plus an out-of-distribution test set from the July 2021 Luxembourg flood event; the Clay ViT encoder is combined with a custom deconvolution decoder and adapted via LoRA applied to attention layers.

## caveats

Authors note full fine-tuning caused out-of-memory errors even on a 40GB GPU; OOD accuracy is misleading due to class imbalance (predominance of non-flood pixels); performance gap between in-distribution and OOD results highlights generalization challenges across geographic contexts; higher LoRA rank trades recall for precision in OOD settings.
