---
arxiv_id: '2403.13430'
authors:
- Di Wang
- Jing Zhang
- Minqiang Xu
- Lin Liu
- Dongsheng Wang
- Erzhong Gao
- Chengxi Han
- Haonan Guo
- Bo Du
- Dacheng Tao
- Liangpei Zhang
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 96.32
  dataset: RESISC-45
  direction: parity
  id: wang2024mtp#c1
  label_ratio: 0.2
  locator: Sec IV-A4
  metric: accuracy
  model: dofa
  span: MTP boosts the performance of InterImage-XL close to the Swin-H-based SkySense
    (96.27 v.s. 96.32)
  span_sha256: 2485dc8668e7589a39df4548daa2f7106f8178a1cc0323ad5698778c9e37702d
  task: land_cover_classification
  value: 96.27
- axis: G5_cost
  baseline: null
  baseline_value: null
  dataset: MTP Pretraining (ViT-B + RVSA)
  direction: parity
  id: wang2024mtp#c2
  label_ratio: null
  locator: Table II
  metric: rmse
  model: dofa
  span: 'ViT-B + RVSA


    86


    16


    3.0'
  span_sha256: 254cbf00c2d10c31a24c68a2761014dd62332cc3bbd1177fab9476e14a38cf3a
  task: representation_probing
  value: 3.0
- axis: G5_cost
  baseline: null
  baseline_value: null
  dataset: MTP Pretraining (ViT-L + RVSA)
  direction: parity
  id: wang2024mtp#c3
  label_ratio: null
  locator: Table II
  metric: rmse
  model: dofa
  span: 'ViT-L + RVSA


    305


    32


    6.3'
  span_sha256: 7145c7516e344aae4cddf264f5f8a34c6f1d1eefc540dbcedf4057a32751c011
  task: representation_probing
  value: 6.3
date: '2024-03-20'
doi: 10.48550/arxiv.2403.13430
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:06:32.081500Z'
key: wang2024mtp
limitations:
- compute_cost
- benchmark_narrowness
models: []
proposed_tags:
- MTP
- multi-task-pretraining
- RVSA
- InternImage
- SAMRS
- scene_classification
- rotated_object_detection
- horizontal_object_detection
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- change_detection
title: 'MTP: Advancing Remote Sensing Foundation Model via Multi-Task Pretraining'
venue: arXiv
---

## summary



## setup



## caveats


