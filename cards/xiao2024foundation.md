---
arxiv_id: '2410.16602'
authors:
- Aoran Xiao
- Weihao Xuan
- Junjue Wang
- Jiaxing Huang
- Dacheng Tao
- Shijian Lu
- Naoto Yokoya
axes: []
claims: []
date: '2024-10-22'
doi: 10.48550/arxiv.2410.16602
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:05:59.508755Z'
key: xiao2024foundation
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
- human_semantics
- spatial_transfer
- temporal_transfer
- interpretability
models:
- croma
- scalemae
- geoclip
- satclip
- satmae
- dofa
proposed_tags:
- survey
- taxonomy
- pre-training-datasets
- SAM-for-RS
- VLM-for-RS
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- crop_type_mapping
- population_density
- change_detection
title: 'Foundation Models for Remote Sensing and Earth Observation: A Survey'
venue: arXiv
---

## summary

This is a survey paper systematically reviewing Remote Sensing Foundation Models (RSFMs), covering visual foundation models (VFMs), vision-language models (VLMs), LLMs, and generative models for RS/EO applications. It categorizes pre-training strategies (supervised, contrastive SSL, masked image modeling), reviews pre-training datasets and downstream RS tasks, and discusses future research directions. It does not introduce a new foundation model but benchmarks and analyzes existing ones qualitatively.

## setup

The survey reviews numerous datasets (e.g., FMoW, BigEarthNet, SSL4EO-S12, SatlasPretrain, MMEarth) and existing RSFMs (e.g., SatMAE, Scale-MAE, CROMA, GeoCLIP, SatCLIP, msGFM) across VFM, VLM, and other categories, summarizing their modalities, pre-training objectives, and typical RS interpretation tasks such as scene classification, semantic segmentation, object detection, change detection, VQA, captioning, and visual grounding.

## caveats

The authors note that RS pre-training datasets still lag general-domain FMs in scale and modality diversity, that no RSFM yet exhibits zero-shot capabilities as robust as general-domain FMs, that most VFM frameworks are trained/tested on single modalities rather than true multimodal fusion, and that current RSFM studies have not yet fundamentally reshaped RS applications the way GPT-4 or SAM did in general domains.
