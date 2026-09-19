---
arxiv_id: '2609.20441'
authors:
- Fabian Schmalstieg
- Karsten Mueller
- Wojciech Samek
axes:
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G3_spatial_transfer
claims:
- axis: G6_compactness
  baseline: null
  baseline_value: null
  dataset: Sen1Floods11
  direction: parity
  id: schmalstieg2026cross#c1
  label_ratio: null
  locator: Sec III-A
  metric: miou
  model: prithvi
  span: On the S11 test split we measure 0.897 mIoU and 0.822 water IoU
  span_sha256: cab1147bcebeb3af10a67da199340716bfcba14740e561ca6275d791f8e2c205
  task: flood_mapping
  value: 0.897
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.789
  dataset: Sen1Floods11
  direction: better
  id: schmalstieg2026cross#c2
  label_ratio: 1.0
  locator: Sec IV
  metric: miou
  model: prithvi
  span: 0.789 mIoU and 0.650 water IoU on the Sen1Floods11 test split, against 0.877
    and 0.787
  span_sha256: 4154fa058778a05aaad92ac1a597b4bcb8497a5da0211f07cc41323d46c2d306
  task: flood_mapping
  value: 0.897
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: STURM-Flood
  direction: better
  id: schmalstieg2026cross#c3
  label_ratio: null
  locator: Sec I
  metric: miou
  model: prithvi
  span: reaches 0.755 mean intersection over union (mIoU) on our protocol of the STURM
    out-of-distribution (OOD) benchmark
  span_sha256: 8bd25bc2d3792b85c8eeb49b55ac9373db449292dc7b91480e6421e34a689a46
  task: flood_mapping
  value: 0.755
date: '2026-09-17'
doi: 10.48550/arxiv.2609.20441
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-19T00:05:58.919729Z'
key: schmalstieg2026cross
limitations:
- benchmark_narrowness
- data_bias
- compute_cost
- time_sensitivity
- mixed_pixels
models:
- prithvi
proposed_tags:
- knowledge_distillation
- edge_deployment
- quantization_aware_training
- pseudo_labeling
- TensorRT
- Jetson_Xavier_NX
- EfficientViT
- OFA_distillation
- MNDWI
regions:
- global
self_evaluation: false
tasks:
- flood_mapping
title: Cross-Architecture Foundation-Model Distillation for Edge Flood Segmentation
venue: arXiv
---

## summary

The paper distills a 300M-parameter Prithvi-EO-2.0 flood-segmentation teacher into a 0.7M-parameter EfficientViT-B0 student using OFA distillation on a teacher-labeled pool of unlabeled Sentinel-2 tiles, enabling deployment on edge hardware. At the matched 252-scene budget the student is competitive with direct supervision, and scaling to 2,500 teacher-labeled scenes narrows the student-teacher gap on Sen1Floods11 and STURM-Flood while remaining behind on WorldFloods-v2. The quantized student runs as a 1.5MB INT8 TensorRT engine on a Jetson Xavier NX at 5.57ms/image, though a fixed MNDWI threshold remains competitive on the clean external benchmarks.

## setup

Prithvi-EO-2.0-300M-TL-Sen1Floods11 (frozen, publicly released checkpoint) is used as teacher to pseudo-label GDACS Sentinel-2 tiles; EfficientViT-B0 student is trained via OFA distillation on curated subsets (N=252 matched budget, N=2,500 scaled pool) and evaluated on Sen1Floods11, STURM-Flood, and WorldFloods-v2 with water IoU/mIoU, then quantized and deployed on a Jetson Xavier NX via TensorRT INT8.

## caveats

Authors flag that the two label sources differ in acquisition geometry (not isolated as a cause), that a fixed MNDWI threshold is competitive with both foundation models on the clean external benchmarks (so external accuracy reflects generalization rather than learned-model superiority), that Sen1Floods11 is a surface-water rather than flood-increment dataset so results reflect water segmentation not new-inundation detection, that STURM evaluation protocol differs from the published one making absolute scores incomparable, and that the student reproduces the teacher's surface-water annotation-convention biases (including false positives on pre-event permanent water) rather than learning flood semantics independently.
