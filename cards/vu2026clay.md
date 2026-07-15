---
arxiv_id: '2606.14081'
authors:
- Huong Binh Vu
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G11_complementarity
- G7_interpretability
- G8_uncertainty
- G6_compactness
claims:
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 59.9
  dataset: Landslide4Sense
  direction: better
  id: vu2026clay#c1
  label_ratio: null
  locator: Table I
  metric: f1
  model: clay
  span: The hybrid U-Net + Clay model with two-stage Low-Rank Adaptation (LoRA) achieved
    the best test F1 of
  span_sha256: 5f9f7918395309d376a1797df01521b11b7c08259f3f8cadb342ce08beb3b378
  task: landslide_susceptibility
  value: 64.5
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 59.9
  dataset: Landslide4Sense
  direction: worse
  id: vu2026clay#c2
  label_ratio: null
  locator: Table I
  metric: f1
  model: clay
  span: surpassing the Clay-only backbone (55.2 ±\pm 3.6%) and the U-Net baseline
    (59.9%)
  span_sha256: d64bbca6e8beb40b6c9a5e6e1127aa5425f3262b885c773e78a07b3d6695d4c1
  task: landslide_susceptibility
  value: 55.2
- axis: G11_complementarity
  baseline: prithvi
  baseline_value: 60.7
  dataset: Landslide4Sense
  direction: better
  id: vu2026clay#c3
  label_ratio: null
  locator: Sec V Discussion
  metric: f1
  model: clay
  span: the Prithvi-EO-2.0 result of 60.7% reported by Szwarcman et al. [12] on the
    same benchmark
  span_sha256: 385eb05bded94278e44abb7ac7e91916951947c242d31a4b934e904afd21c58a
  task: landslide_susceptibility
  value: 64.5
- axis: G8_uncertainty
  baseline: null
  baseline_value: null
  dataset: Landslide4Sense
  direction: parity
  id: vu2026clay#c4
  label_ratio: null
  locator: Fig. 5(B)
  metric: auc
  model: clay
  span: ROC curve with AUC = 0.989, indicating strong discriminative ranking
  span_sha256: cc398e7a779db4b0c1736febe08fb0821dc81aabe41a38cab14852131671fa3f
  task: landslide_susceptibility
  value: 0.989
date: '2026-06-12'
doi: 10.48550/arxiv.2606.14081
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:34:49.415309Z'
key: vu2026clay
limitations:
- benchmark_narrowness
- uncertainty
- interpretability
- spatial_transfer
models:
- clay
- prithvi
proposed_tags:
- landslide_segmentation
- grad_cam
- mc_dropout
- lora_fine_tuning
- terrain_fusion
regions:
- np
- jp
- in
- tw
self_evaluation: false
tasks:
- landslide_susceptibility
- change_detection
title: 'Clay-CNN Hybrids: Leveraging Geospatial Foundation Models as Auxiliary Context
  for Landslide Detection'
venue: arXiv
---

## summary

The paper evaluates Clay v1.5 as both a standalone encoder and as auxiliary bottleneck context fused into a U-Net for landslide segmentation on Landslide4Sense, finding that Clay alone underperforms a U-Net baseline but Clay-U-Net hybrid fusion with two-stage LoRA achieves the best F1 of 64.5%. The authors use MC Dropout uncertainty and Grad-CAM to show Clay acts as a corrective geomorphic/semantic prior rather than a scar detector.

## setup

Landslide4Sense benchmark (3,799 train / 245 val / 800 test chips, 128x128 px, 10m resolution, 14 Sentinel-2 + terrain bands, ~2% positive pixels) with a geographically stratified leave-out-location split; models are trained with BCE+Lovász loss and evaluated via validation-selected threshold on test-set pixel-wise F1.

## caveats

Authors note constant time/geolocation encodings prevent Clay from using geographic/seasonal priors, threshold selection relies on a small 245-chip validation set introducing variance, MC Dropout uncertainty remains small despite calibration (possible overconfidence), and the 128x128 chip size limits spatial context, hurting performance on small isolated landslide patches.
