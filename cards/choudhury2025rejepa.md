---
arxiv_id: '2504.03169'
authors:
- Shabnam Choudhury
- Yash Salunkhe
- Sarthak Mehrotra
- Biplab Banerjee
axes:
- G5_cost
- G1_label_rich_parity
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: BEN-14K (S1)
  direction: worse
  id: choudhury2025rejepa#c1
  label_ratio: null
  locator: Table 1
  metric: f1
  model: satmae
  span: SatMAE [13] 329.40 70.86 78.71
  span_sha256: 6da2701308126135d769259728a2fd795f6237f09aed46788bc0560c967b27eb
  task: representation_probing
  value: 70.86
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: BEN-14K (S2)
  direction: worse
  id: choudhury2025rejepa#c2
  label_ratio: null
  locator: Table 1
  metric: f1
  model: scalemae
  span: Scale-MAE [30] 284.35 62.73 NA 64.26 69.56
  span_sha256: 63db20591655eaa00d4f102cc09d556026762a60836a2ea4e84e86b531a9f80f
  task: representation_probing
  value: 69.56
- axis: G5_cost
  baseline: null
  baseline_value: null
  dataset: BEN-14K / FMoW-RGB / FMoW-Sentinel
  direction: better
  id: choudhury2025rejepa#c3
  label_ratio: null
  locator: Table 1
  metric: f1
  model: presto
  span: ReJEPA 197.09 76.38 75.42 73.53 75.87
  span_sha256: d4187b00d0128d4af0aa2d152e83fd51ee4b960291b64fae2d3bc032ff74387b
  task: representation_probing
  value: 197.09
date: '2025-04-04'
doi: 10.48550/arxiv.2504.03169
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:22:38.978315Z'
key: choudhury2025rejepa
limitations:
- compute_cost
- benchmark_narrowness
models:
- satmae
- scalemae
proposed_tags:
- content_based_image_retrieval
- joint_embedding_predictive_architecture
- self_supervised_pretraining
- masking_ratio_ablation
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: 'REJEPA: A Novel Joint-Embedding Predictive Architecture for Efficient Remote
  Sensing Image Retrieval'
venue: arXiv
---

## summary



## setup



## caveats


