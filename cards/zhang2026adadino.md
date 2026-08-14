---
arxiv_id: '2608.07982'
authors:
- Xu Zhang
- Xinqing Li
- Jianpeng Xie
- Zeshuai Zhu
- Xin He
- Yun Liu
axes:
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
claims:
- axis: G5_cost
  baseline: null
  baseline_value: null
  dataset: SYSU-CD
  direction: better
  id: zhang2026adadino#c1
  label_ratio: null
  locator: Abstract
  metric: f1
  model: dofa
  span: AdaDINO still achieves an F1 score of 85.29% on SYSU-CD while delivering a
    1.41
  span_sha256: 8d0d58b51c56b2b3427cabf51b949f9d0e21182d56967700339c33ffdf2ef452
  task: change_detection
  value: 85.29
date: '2026-08-08'
doi: 10.48550/arxiv.2608.07982
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-14T00:17:02.592874Z'
key: zhang2026adadino
limitations:
- compute_cost
- benchmark_narrowness
models: []
proposed_tags:
- DINO
- DINOv3
- bi-temporal-interaction
- FFN-pruning
- parameter-efficient-adaptation
regions: []
self_evaluation: false
tasks:
- change_detection
title: 'AdaDINO: Pair-Aware In-Backbone Adaptation of Frozen DINO for Efficient Remote
  Sensing Change Detection'
venue: arXiv
---

## summary

AdaDINO adapts a frozen DINOv3 backbone with pair-aware in-backbone modules (CGLA, BSCS, CPGR) for efficient bi-temporal remote sensing change detection. It achieves competitive or superior F1 scores against VFM-based baselines on four benchmarks while substantially reducing FFN computation.

## setup

Evaluated on SYSU-CD, WHU-CD, LEVIR-CD, and LEVIR-CD+ change detection benchmarks with 256x256 image pairs, using a frozen DINOv3 ViT-L/16 pretrained on SAT-493M, training only the added adaptation and decoder modules.

## caveats

The authors note their evidence for improved FFN prunability rests on a matched comparison of separately trained models rather than a strict causal isolation, and leave extending the approach to semantic/multi-class change as future work.
