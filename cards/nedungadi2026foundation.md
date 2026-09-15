---
arxiv_id: '2608.30392'
authors:
- Vishal Nedungadi
- Xingguo Xiong
- Marc Rußwurm
- Ioannis N. Athanasiadis
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G11_complementarity
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.55
  dataset: CY-Bench (US)
  direction: better
  id: nedungadi2026foundation#c1
  label_ratio: null
  locator: Sec 3.2.2
  metric: r2
  model: presto
  span: the unconstrained, tabular-focused TabPFN outperforms all other models with
    an R2R^{2} of 0.650.65
  span_sha256: c99513f55f37383b300c10f8114a7f35597e8e2aa6f91c893cd8311a5a626239
  task: crop_yield_estimation
  value: 0.65
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: -0.15
  dataset: YieldSAT (Argentina)
  direction: better
  id: nedungadi2026foundation#c2
  label_ratio: null
  locator: Sec 3.2.2
  metric: r2
  model: presto
  span: CropFM under full fine-tuning yields the best performance (R2=0.33R^{2}=0.33)
  span_sha256: 6d76b89758b4a85bee5ff20dd4fe024d1a8d46674e8a145317c584cbfef506bf
  task: crop_yield_estimation
  value: 0.33
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.89
  dataset: CropHarvest (Kenya)
  direction: worse
  id: nedungadi2026foundation#c3
  label_ratio: null
  locator: Table 3
  metric: f1
  model: galileo
  span: Galileo suffers performance penalties in both Kenya (Δ​F1≈−0.16\Delta\text{F1}\approx-0.16)
  span_sha256: fa7fb9fdb25e3c9e8d5804fc2b2e49f032d80d090b48128b0bd826905b2c6ae2
  task: crop_type_mapping
  value: 0.7
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.6
  dataset: BreizhCrops
  direction: worse
  id: nedungadi2026foundation#c4
  label_ratio: null
  locator: Table 3
  metric: f1
  model: galileo
  span: and France (Δ​F1≈−0.16\Delta\text{F1}\approx-0.16)
  span_sha256: f40106ce591373495e949959d4b41f04cc17f92e67750fc179743c2bfa09e2e6
  task: crop_type_mapping
  value: 0.34
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: null
  dataset: CY-Bench (Germany)
  direction: worse
  id: nedungadi2026foundation#c5
  label_ratio: null
  locator: Sec 3.2.3
  metric: r2
  model: galileo
  span: R2=−0.85R^{2}=-0.85, and 53.42 MAE
  span_sha256: 446dd2c52c75ec3addbe4ef0a935fa53cf9cdae1219cfbfd0dc9b4cb8c9fba7d
  task: crop_yield_estimation
  value: -0.85
date: '2026-08-31'
doi: 10.48550/arxiv.2608.30392
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-15T00:25:47.176351Z'
key: nedungadi2026foundation
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
- spatial_transfer
- temporal_transfer
models:
- galileo
proposed_tags:
- modality_mismatch
- task_heterogeneity
- tabular_foundation_model
- CropFM
- TabPFN
- rank_instability
- catastrophic_forgetting
regions:
- ke
- fr
- de
- us
- sn
- ar
- global
self_evaluation: false
tasks:
- crop_type_mapping
- crop_yield_estimation
- representation_probing
title: 'Foundation Models Meet Agriculture: Challenges Beyond Pretraining'
venue: arXiv
---

## summary

This paper benchmarks Galileo, an idealized purpose-built EO FM (CropFM), a tabular FM (TabPFN), and supervised baselines across seven agricultural datasets spanning crop type mapping, phenology, and yield estimation. It identifies a pretraining-downstream modality gap and task heterogeneity as two structural barriers causing unstable model rankings and frequent underperformance of EO FMs relative to simple baselines.

## setup

Seven real-world datasets (CropHarvest-Kenya, BreizhCrops-France, BloomBench-Germany, CY-Bench-US/Germany/Senegal, YieldSAT-Argentina) are evaluated with dataset-specific metrics (F1, R2, MAE) using tailored splits, comparing Random Forest/LSTM/Transformer baselines, TabPFN, and Galileo/CropFM under frozen-feature and fine-tuning protocols.

## caveats

Authors note limited EO FM options usable on long/multimodal sequences, non-global regional coverage, reliance on simple supervised baselines rather than domain-specific complex models, and possible unknown confounds like pretraining biases and information leakage.
