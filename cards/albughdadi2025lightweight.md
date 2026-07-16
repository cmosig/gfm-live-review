---
arxiv_id: '2509.10919'
authors:
- Mohanad Albughdadi
axes:
- G5_cost
- G6_compactness
- G2_label_scarce_efficiency
- G7_interpretability
claims:
- axis: G6_compactness
  baseline: null
  baseline_value: null
  dataset: BigEarthNet-LS
  direction: better
  id: albughdadi2025lightweight#c1
  label_ratio: null
  locator: Sec 4.4
  metric: accuracy
  model: prithvi
  span: Our all-token mAP of 0.767 outperforms SSL4EO-L ResNet-50 MoCo v2 (0.761)
  span_sha256: ae4d012cdbb1070f7962cf91cc2827731fd95c7b8464a0973c251e55a86eaa82
  task: land_cover_classification
  value: 0.767
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 89.8
  dataset: EuroSAT-LS
  direction: worse
  id: albughdadi2025lightweight#c2
  label_ratio: null
  locator: Table 7
  metric: accuracy
  model: dofa
  span: Our CLS-token accuracy of 84.2% outperforms many larger models
  span_sha256: ef9b0ea0551dacb95ee956f61344cdbf30c6371e98dbcc089c0a17b0d654b97b
  task: land_cover_classification
  value: 84.2
- axis: G6_compactness
  baseline: null
  baseline_value: 91.9
  dataset: EuroSAT-LS
  direction: worse
  id: albughdadi2025lightweight#c3
  label_ratio: null
  locator: Table 7
  metric: accuracy
  model: prithvi
  span: Prithvi-EO-2.0 600M
  span_sha256: 40ad3a26c60a3ea92f19157e0f47062a360fc4c75cead0de0fe9008aac85388e
  task: representation_probing
  value: 84.2
date: '2025-09-13'
doi: 10.48550/arxiv.2509.10919
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:11:25.880700Z'
key: albughdadi2025lightweight
limitations:
- compute_cost
- benchmark_narrowness
- interpretability
models:
- prithvi
- dofa
proposed_tags:
- mixture_of_experts
- masked_autoencoder
- geo_temporal_conditioning
- linear_probe
- expert_routing
- Landsat
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- representation_probing
title: Lightweight Metadata-Aware Mixture-of-Experts Masked Autoencoder for Earth
  Observation
venue: arXiv
---

## summary

The paper introduces a ~2.5M-parameter metadata-aware Mixture-of-Experts Masked Autoencoder (MoE-MAE) for Earth Observation, pretrained on BigEarthNet-Landsat with geo-temporal conditioning. Despite being orders of magnitude smaller than models like Prithvi and DOFA, frozen-encoder linear probes achieve competitive multi-label classification on BEN-LS and transfer reasonably to EuroSAT-LS even without metadata.

## setup

Pretrained via masked reconstruction (75% masking) plus MoE load-balancing losses on BigEarthNet-Landsat (590K patches, 7 bands, multi-label CLC classes); evaluated via frozen-encoder logistic regression linear probes on BEN-LS test split and cross-dataset transfer to EuroSAT-Landsat (27K patches, single-label, no metadata), compared against LandsatBench baselines including SSL4EO-L, DOFA, and Prithvi variants.

## caveats

Authors note the model still falls behind larger foundation models (e.g., Prithvi-EO-2.0 600M) on EuroSAT-LS accuracy, was only pretrained on a single dataset (BEN-LS) rather than large-scale multi-sensor archives, and suggest further pretraining on larger/diverse datasets and temporal modeling are needed for broader comparison to state-of-the-art systems.
