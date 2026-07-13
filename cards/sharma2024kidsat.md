---
arxiv_id: '2407.05986'
authors:
- Makkunda Sharma
- Fan Yang
- Duy-Nhat Vo
- Esra Suel
- Swapnil Mishra
- Samir Bhatt
- Oliver Fiala
- William Rudgard
- Seth Flaxman
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.2436
  dataset: KidSat spatial benchmark
  direction: better
  id: sharma2024kidsat#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: satmae
  span: SatMAE (Fine-tuned) LandSat 0.2125
  span_sha256: 3b534a6170ef5cf838507d22365b0925bd8992cc0088de673bb7fd92ffdb9975
  task: poverty_mapping
  value: 0.2125
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.5656
  dataset: KidSat temporal benchmark
  direction: better
  id: sharma2024kidsat#c2
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: satmae
  span: SatMAE (Fine-tuned) LandSat
  span_sha256: 4625ab4214294366c1f36ecfe9aa9bbac979ac1fb3b289e244fe4557284ea387
  task: poverty_mapping
  value: 0.3376
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: KidSat spatial benchmark
  direction: better
  id: sharma2024kidsat#c3
  label_ratio: null
  locator: Sec 5.1
  metric: rmse
  model: satmae
  span: the SatMAE architecture achieved errors of 0.2347 and 0.2093 before and after
    the fine-tuning
  span_sha256: 04b437b2f00653a46889c260f206607799f53150dd6776132fe0561ad9b5d679
  task: poverty_mapping
  value: 0.2093
date: '2024-07-08'
doi: 10.48550/arxiv.2407.05986
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T09:23:37.021642Z'
key: sharma2024kidsat
limitations:
- temporal_transfer
- compute_cost
- benchmark_narrowness
models:
- satmae
proposed_tags:
- MOSAIKS
- DINOv2
- child_poverty
- DHS_survey
regions:
- global
self_evaluation: false
tasks:
- poverty_mapping
title: 'KidSat: satellite imagery to map childhood poverty dataset and benchmark'
venue: arXiv
---

## summary

The paper introduces KidSat, a dataset of 33,608 satellite image tiles paired with DHS survey-derived child poverty measures across 19 Eastern/Southern African countries (1997-2022), and benchmarks foundation and non-foundation models on spatial and temporal generalization. Fine-tuned DINOv2 (a generic vision foundation model) using Sentinel-2 imagery achieves the best spatial MAE, outperforming SatMAE, MOSAIKS, Gaussian Process regression, and mean-prediction baselines, while all models struggle more on the temporal forecasting benchmark.

## setup

33,608 10km x 10km Landsat/Sentinel-2 image tiles matched to DHS cluster locations and severe_deprivation child poverty scores; spatial benchmark uses 5-fold cross-validation over held-out clusters, temporal benchmark trains on pre-2020 data and tests on 2020-2022; models (MOSAIKS, DINOv2, SatMAE) are evaluated raw and fine-tuned on 17 DHS variables followed by ridge regression to predict severe_deprivation, measured via MAE.

## caveats

Authors note the temporal benchmark is much harder and fine-tuned models often overfit to historical data; MOSAIKS features were unreliable/unavailable before 2013 and had API issues; SatMAE's fixed 224x224 input constrains use of high-resolution Sentinel-2 imagery and its temporal/multispectral capabilities were underused; fine-tuning targeted DHS variables rather than severe_deprivation directly, which may be suboptimal; large models could not fit in 32GB GPU memory with full-resolution Sentinel-2 data; spatial evaluation used random cluster holdout rather than stricter leave-one-country-out evaluation.
