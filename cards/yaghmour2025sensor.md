---
arxiv_id: '2505.01558'
authors:
- Anan Yaghmour
- Melba M. Crawford
- Saurabh Prasad
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G11_complementarity
claims:
- axis: G3_spatial_transfer
  baseline: prithvi
  baseline_value: 0.4109
  dataset: C2Seg-AB
  direction: better
  id: yaghmour2025sensor#c1
  label_ratio: null
  locator: Table 4
  metric: f1
  model: prithvi
  span: mF1 (Avg)
  span_sha256: 768150277cf8f5f94b57ee2b7050078d38976b594237caca12652e675ff1964c
  task: semantic_segmentation
  value: 0.5255
- axis: G3_spatial_transfer
  baseline: prithvi
  baseline_value: 0.2704
  dataset: C2Seg-AB
  direction: better
  id: yaghmour2025sensor#c2
  label_ratio: null
  locator: Table 4
  metric: miou
  model: prithvi
  span: mIoU (Avg)
  span_sha256: 9721101a8ad67360abd8f613dfc1b2fdde6a59cd5e7f8465c1e63a6df24727fa
  task: semantic_segmentation
  value: 0.3835
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: null
  dataset: C2Seg-AB
  direction: better
  id: yaghmour2025sensor#c3
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: prithvi
  span: MA(Avg)
  span_sha256: b8188a4ba98c08acd8d9b084d8207d7a513d3f6c990fb332d14d4281964ab01c
  task: semantic_segmentation
  value: 0.6381
date: '2025-05-02'
doi: 10.48550/arxiv.2505.01558
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:49:10.091491Z'
key: yaghmour2025sensor
limitations:
- spatial_transfer
- data_bias
- uncertainty
models:
- prithvi
proposed_tags:
- domain_adaptation
- masked_autoencoder
- pseudo_labeling
- sensor_agnostic_adaptation
regions:
- de
- fr
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
title: 'A Sensor Agnostic Domain Generalization Framework for Leveraging Geospatial
  Foundation Models: Enhancing Semantic Segmentation viaSynergistic Pseudo-Labeling
  and Generative Learning'
venue: arXiv
---

## summary

The paper proposes a domain generalization framework built on the frozen Prithvi geospatial foundation model, combining soft pseudo-labeling (entropy-based domain alignment) with source-to-target MAE generative pre-training to adapt semantic segmentation across sensors and geographies. It introduces adapter tuning and a Conv2D spectral adaptation layer to extend Prithvi to hyperspectral and multispectral data unseen during its original pre-training, and provides a mathematical analysis of how MAE-based reconstruction dynamically weights unlabeled target pixels during segmentation learning.

## setup

Experiments use two cross-domain segmentation benchmarks: C2Seg-AB (hyperspectral/multispectral/SAR data over Berlin as source and Augsburg as target, Germany) and FLAIR (very-high-resolution and Sentinel-2 time series across 50 French sub-regions, with an open-set class shift). A small number of labeled target pixels (2,000/class for C2Seg-AB, 600/class for FLAIR) are used for fine-tuning alongside fully labeled source data.

## caveats

The authors note that adding the MAE loss alone (without domain alignment) degrades performance relative to the segmentation-only baseline because the dynamic weighting mechanism can be harmed when the model is mistakenly overconfident about unlabeled target pixels; they also observe certain classes (e.g., Street, Open spaces with no vegetation) show persistently low precision across all compared methods.
