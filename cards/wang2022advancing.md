---
arxiv_id: '2208.03987'
authors:
- Di Wang
- Qiming Zhang
- Yufei Xu
- Jing Zhang
- Bo Du
- Dacheng Tao
- Liangpei Zhang
axes:
- G5_cost
- G6_compactness
- G2_label_scarce_efficiency
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: DOTA-V1.0
  direction: better
  id: wang2022advancing#c1
  label_ratio: null
  locator: Abstract
  metric: accuracy
  model: prithvi
  span: achieving 81.24% mAP on the DOTA-V1.0 dataset
  span_sha256: 2f9dd7d4c7c64673ca7a362ef58e43b63bc5e0f67004ec4241ea5fd9e5a2a1cd
  task: semantic_segmentation
  value: 81.24
date: '2022-08-08'
doi: 10.48550/arxiv.2208.03987
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:08:13.125999Z'
key: wang2022advancing
limitations:
- compute_cost
- benchmark_narrowness
models: []
proposed_tags:
- plain_vit
- rotated_varied_size_attention
- MAE_pretraining
- object_detection
- scene_classification
- MillionAID
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- change_detection
title: Advancing Plain Vision Transformer Towards Remote Sensing Foundation Model
venue: arXiv
---

## summary

This paper pretrains plain ViT and ViTAE backbones (~100M params) with MAE on the MillionAID dataset and introduces Rotated Varied-Size Window Attention (RVSA) to adapt plain ViTs for remote sensing tasks. It evaluates on scene classification, object detection, and semantic segmentation, achieving state-of-the-art 81.24% mAP on DOTA-V1.0.

## setup

Models are pretrained via MAE on MillionAID (unsupervised), then finetuned with RVSA replacing MHSA on object detection (DOTA-V1.0, DIOR-R), scene classification (UCM, AID, NWPU), and semantic segmentation (Potsdam, iSAID, LoveDA).

## caveats

Authors note segmentation performance lags detection/classification due to the plain ViT's low-resolution feature maps and the basic UperNet framework; RVSA needs sufficient training data to learn optimal window configurations, underperforming on small datasets like NWPU-19.
