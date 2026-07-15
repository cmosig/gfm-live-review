---
arxiv_id: '2603.23408'
authors:
- Joelle Hanna
- Damian Falk
- Stella X. Yu
- Damian Borth
axes:
- G1_label_rich_parity
- G6_compactness
- G11_complementarity
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: RESISC45
  direction: parity
  id: hanna2026geosane#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: scalemae
  span: "99.1\t95.7"
  span_sha256: 6a319e948ad7689ab16d6822e1e6c71826125bdd6bffc35728e44a4f2d03f090
  task: land_cover_classification
  value: 95.7
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Sen1Floods11
  direction: parity
  id: hanna2026geosane#c2
  label_ratio: null
  locator: Table 2
  metric: miou
  model: croma
  span: '90.9'
  span_sha256: c8f55e046b68ccd4861a11021e01f1e07c8000427f911f11cd1debd30aff8ac7
  task: flood_mapping
  value: 90.9
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: fMoW
  direction: parity
  id: hanna2026geosane#c3
  label_ratio: 0.1
  locator: Table 2
  metric: accuracy
  model: croma
  span: '59.0'
  span_sha256: 4bf4f525504cc0a2c514f8cfd5d73ea65c50af4bbcd047c0f01fd331ed3ef051
  task: crop_type_mapping
  value: 59.0
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: m-eurosat
  direction: parity
  id: hanna2026geosane#c4
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: croma
  span: '96.6'
  span_sha256: 0222cab8c50caeec6349f706ba3524ec41bb0c980f8e4cb887489adc70a518c0
  task: land_cover_classification
  value: 96.6
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: m-brick-kiln
  direction: parity
  id: hanna2026geosane#c5
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: dofa
  span: '98.6'
  span_sha256: f8efe2ccc64d2e3298a152075e9a66ae7a1b55064f1018f2dd590716bdd31017
  task: land_cover_classification
  value: 98.6
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: m-so2sat
  direction: parity
  id: hanna2026geosane#c6
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: galileo
  span: '63.3'
  span_sha256: 6175e0c0dc7959abeb138948c98885ae7ff0ef23d77ea93657fb3fe9d40434ab
  task: representation_probing
  value: 63.3
date: '2026-03-24'
doi: 10.48550/arxiv.2603.23408
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:57:45.412509Z'
key: hanna2026geosane
limitations:
- compute_cost
- benchmark_narrowness
models:
- satmae
- scalemae
- croma
- dofa
- presto
- galileo
proposed_tags:
- weight_space_learning
- model_generation
- model_foundry
- weight_space_autoencoder
- model_merging
- pruning_distillation_baseline
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
- flood_mapping
- crop_type_mapping
- change_detection
- representation_probing
title: 'GeoSANE: Learning Geospatial Representations from Models, Not Data'
venue: arXiv
---

## summary

GeoSANE learns a shared latent representation from the weights of 103 diverse remote sensing (foundation) models via a weight-space encoder-decoder, then generates new model weights on-demand for target architectures and downstream tasks. Generated models outperform training from scratch, match or surpass existing RSFMs, and outperform pruning/distillation baselines when producing lightweight networks. The paper is a weight-space model-generation approach, not a new data-pretrained RSFM.

## setup

GeoSANE is trained on a collection of 103 HuggingFace remote sensing models (~38B parameters, ~165M tokens) using a GPT-2-style transformer encoder-decoder with reconstruction and contrastive losses on tokenized weights; it is evaluated by generating ViT-L/Swin-B (and smaller CNN) weights fine-tuned on 10 datasets (EuroSAT, RESISC45, fMoW, BigEarthNet, Sen12Flood, California Wildfires, DFC2020, Sen1Floods11, SpaceNet1, DIOR) plus GEO-Bench, comparing against training from scratch, existing RSFMs, DARE model merging, and pruning/distillation baselines.

## caveats

The authors note that stabilizing training required runtime loss normalization (vs. layer-wise weight normalization used in prior work) to handle heterogeneous architectures, and that for very small model budgets (3.5M params) pruning/variational dropout required relaxing sparsity targets to 5M due to instability; they also note fMoW at 3.5M params underperforms baselines (-7.8).
