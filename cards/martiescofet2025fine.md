---
arxiv_id: '2504.17397'
authors:
- Francesc Marti-Escofet
- Benedikt Blumenstiel
- Linus Scheibenreif
- Paolo Fraccaro
- Konrad Schindler
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Sen1Floods11
  direction: parity
  id: martiescofet2025fine#c1
  label_ratio: null
  locator: Table 4
  metric: miou
  model: clay
  span: '90.41'
  span_sha256: 242b8c096572fea4bb5b7b07cdb474effb77f5bff3cff2eedf42310f6524aca6
  task: flood_mapping
  value: 90.41
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 34.62
  dataset: reBEN 7k
  direction: better
  id: martiescofet2025fine#c2
  label_ratio: null
  locator: Table 4
  metric: miou
  model: prithvi
  span: '38.84'
  span_sha256: 4ecbc35653d4ca7c867e7158d72e1911b565fc79cc1ceb3ffbb6a1db8b3fab14
  task: crop_type_mapping
  value: 38.84
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: Sen1Floods11
  direction: worse
  id: martiescofet2025fine#c3
  label_ratio: null
  locator: Table 5
  metric: miou
  model: prithvi
  span: '87.57'
  span_sha256: 3a54b7dd0b129857f564fce7fc64cc81c1049bc3ce6f221fe19dcf94a273d3f1
  task: flood_mapping
  value: 87.57
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: reBEN 7k
  direction: worse
  id: martiescofet2025fine#c4
  label_ratio: null
  locator: Table 5
  metric: miou
  model: clay
  span: '28.44'
  span_sha256: dc65549f418eb7b266fec3b44ffaf9cbec189192029f475a5c58ad488e4ab406
  task: crop_type_mapping
  value: 28.44
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 81.81
  dataset: m-Cashew plant.
  direction: worse
  id: martiescofet2025fine#c5
  label_ratio: null
  locator: Table 4
  metric: miou
  model: prithvi
  span: '81.81'
  span_sha256: 2027984d9294cb689131f2e2330e323746ce77a58e9a0c1f81980f8d5781a5d7
  task: land_cover_classification
  value: 80.58
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 34.99
  dataset: SACrop
  direction: better
  id: martiescofet2025fine#c6
  label_ratio: null
  locator: Table 4
  metric: miou
  model: prithvi
  span: '40.35'
  span_sha256: d385c61765d6fe9f45d1c66c2ecd49d487fcfe1a71a864797923601d50dedff4
  task: crop_type_mapping
  value: 40.35
date: '2025-04-24'
doi: 10.48550/arxiv.2504.17397
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:49:51.878602Z'
key: martiescofet2025fine
limitations:
- spatial_transfer
- benchmark_narrowness
- compute_cost
models:
- clay
- prithvi
proposed_tags:
- PEFT
- LoRA
- VPT
- ViT_Adapter
- decoder_architecture
- metadata_ablation
regions:
- global
- bo
- at
- ie
- bj
- za
- us
self_evaluation: false
tasks:
- semantic_segmentation
- flood_mapping
- crop_type_mapping
- land_cover_classification
title: 'Fine-tune Smarter, Not Harder: Parameter-Efficient Fine-Tuning for Geospatial
  Foundation Models'
venue: arXiv
---

## summary

The paper presents the first systematic evaluation of parameter-efficient fine-tuning (PEFT) techniques—LoRA, VPT, and ViT Adapter—applied to geospatial foundation models (Clay, Prithvi 1.0/2.0, DeCUR) across five EO segmentation datasets. LoRA matches or exceeds full fine-tuning performance while reducing memory usage and improving geographic generalization to unseen regions.

## setup

Experiments fine-tune Clay v1, Prithvi 1.0 100M, Prithvi 2.0 300M, and DeCUR (baseline) with linear, FCN, UperNet, and UNet decoders on Sen1Floods11, Burn Scars, reBEN 7k, m-Cashew Plantation, and m-SA Crop Type datasets, using Bayesian HPO and averaging five runs per configuration. Geographic hold-out sets (GHOS) are used to test spatial generalization, and additional ablations cover input band robustness and metadata inclusion.

## caveats

Authors note the study is limited to three GeoFM architectures and results may not generalize to other models or tasks; PEFT methods may struggle under extreme distribution shifts (e.g., sensor modality changes or very high-resolution imagery); geographic generalization remains an open challenge with some PEFT configurations (e.g., LoRA on Prithvi 1.0) showing large GHOS performance drops.
