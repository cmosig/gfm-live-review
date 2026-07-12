---
arxiv_id: '2601.13751'
authors:
- Daniel Kyselica
- Jonáš Herec
- Oliver Kutis
- Rado Pitoňák
axes:
- G5_cost
- G6_compactness
- G4_temporal_transfer
claims:
- axis: G6_compactness
  baseline: null
  baseline_value: null
  dataset: STTORM-CD-Floods
  direction: parity
  id: kyselica2026towards#c1
  label_ratio: null
  locator: Sec 7
  metric: f1
  model: prithvi
  span: the model achieves an F1-score of 0.479 on the STTORM-CD-Floods test set
  span_sha256: 3fffffbde97556e12cbceab481e60fcc9c4a08b30094b2b22a613d0a548bfd28
  task: change_detection
  value: 0.479
- axis: G5_cost
  baseline: task_specific
  baseline_value: 0.46
  dataset: STTORM-CD-Floods
  direction: worse
  id: kyselica2026towards#c2
  label_ratio: null
  locator: Table 2
  metric: f1
  model: prithvi
  span: ContUrbanCD 0.46 ±\pm 0.26
  span_sha256: d081bb85c241cbd96c503b63eac8a69ed4de782c6027916ab64ae87a776418f7
  task: change_detection
  value: 0.38
date: '2026-01-20'
doi: 10.48550/arxiv.2601.13751
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:42:55.192976Z'
key: kyselica2026towards
limitations:
- compute_cost
- benchmark_narrowness
- time_sensitivity
models:
- prithvi
proposed_tags:
- onboard_satellite_inference
- history_injection_mechanism
- continual_change_detection
regions:
- global
self_evaluation: false
tasks:
- flood_mapping
- change_detection
title: Towards Onboard Continuous Change Detection for Floods
venue: arXiv
---

## summary

The paper introduces HiT, a History Injection mechanism that embeds compact historical context into a ViT block, enabling continuous multi-temporal flood change detection onboard small satellites without storing raw past images. HiT-PrithVi, built on distilled PrithVi-EO-2.0-tiny, reduces storage by up to 99.6% versus raw Sentinel-2 tiles while maintaining performance comparable to a bi-temporal PrithVi baseline, running at 43 FPS on Jetson Orin Nano. It is compared against a bi-temporal PrithVi baseline and ContUrbanCD, a larger urban change detection model.

## setup

Models were trained and tested on STTORM-CD-Floods and RaVAEn-Floods multi-temporal Sentinel-2 flood datasets (256x256 tiles), with continuity simulated via a modified CutMix augmentation; evaluation used F1/precision/recall averaged over five runs on the STTORM-CD-Floods hand-picked test set.

## caveats

The authors note HiT-PrithVi and the baseline failed to detect small/fine-grained changes, generalization to unseen biomes (e.g., Niger scene) was poor, and no dedicated dataset exists for continuous change detection, limiting thorough evaluation of temporal persistence; ContUrbanCD showed high training instability (±0.26 F1 std) and exceeds onboard memory constraints.
