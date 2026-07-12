---
arxiv_id: '2602.19190'
authors:
- Xiaokun Zhang
- Yi Yang
- Ziqi Ye
- Baiyun
- Xiaorong Guo
- Qingchen Fang
- Ruyi Zhang
- Xinpeng Zhou
- Haipeng Wang
axes:
- G11_complementarity
claims: []
date: '2026-02-22'
doi: 10.48550/arxiv.2602.19190
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:45:13.892025Z'
key: zhang2026fusar
limitations:
- temporal_transfer
models:
- alphaearth
- prithvi
proposed_tags:
- SAR imagery
- vision-language model
- object counting
- target detection
- spatial localization
- spatiotemporal feature embedding
- geospatial prior as world knowledge
- AlphaEarth feature fusion
- feature-wise linear modulation
- two-stage SFT
- SAR-text-feature triplet dataset
regions: []
self_evaluation: false
tasks: []
title: 'FUSAR-GPT : A Spatiotemporal Feature-Embedded and Two-Stage Decoupled Visual
  Language Model for SAR Imagery'
venue: arXiv
---

## summary

FUSAR-GPT is a SAR-specific vision-language model built on Qwen2.5-VL-7B that injects AlphaEarth (AEF) geospatial embeddings as 'world knowledge' priors via a Token-wise Linear Modulation (TLM) fusion module and a two-stage decoupled supervised fine-tuning strategy. It reports state-of-the-art results over general VLM and remote-sensing baselines on SAR target counting, spatial localization, classification, detection, and captioning. The authors use AEF as a component rather than being its creators.

## setup

Data come from the FUSAR-GEOVL dataset within FUSAR-KLIP (10k AEF-image-text triplets, with a 2k annotated subset for downstream tasks); Stage-1 (30 epochs, lr 1e-4) jointly trains an AEF-embedding MLP and LoRA adapters, Stage-2 (5 epochs, lr 1e-5) tunes only LoRA. All baselines were fine-tuned in MS-SWIFT under identical settings on four A100 GPUs, evaluated on counting, 3x3 grid localization, classification, detection, and captioning.

## caveats

The authors note they do not explicitly model temporal dynamics, using AEF only as a stable annual-scale geospatial prior; detection performance is only a preliminary comparison since the framework is not designed for detection, with more comprehensive evaluation left to future work.
