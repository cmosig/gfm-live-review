---
arxiv_id: '2512.01181'
authors:
- Andrew Du
- Roberto Del Prete
- Alejandro Mousist
- Nick Manser
- Fabrice Marre
- Andrew Barton
- Carl Seubert
- Gabriele Meoni
- Tat-Jun Chin
axes:
- G5_cost
- G6_compactness
- G2_label_scarce_efficiency
- G3_spatial_transfer
claims:
- axis: G6_compactness
  baseline: prithvi
  baseline_value: null
  dataset: Sentinel-2 Cloud Mask Catalogue
  direction: parity
  id: du2025first#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: Workstation GPU FP32 90.14 94.80 95.18
  span_sha256: 2fd77d0c8a4b58695df2a8a2d2ca429dfb018830f75e4d1a729c986bee8d9e50
  task: semantic_segmentation
  value: 90.14
- axis: G5_cost
  baseline: prithvi
  baseline_value: 97.22
  dataset: Sentinel-2 Cloud Mask Catalogue
  direction: parity
  id: du2025first#c2
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: prithvi
  span: Hardware emulator XE1 (Myriad-2) FP16 97.10
  span_sha256: 070ba615d523298e9888d6f8344db2f456d49c1ba51d1ec532c99826388260ea
  task: semantic_segmentation
  value: 97.1
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: Kanyini mission imagery
  direction: worse
  id: du2025first#c3
  label_ratio: 1.0
  locator: Fig 4(c)
  metric: miou
  model: prithvi
  span: 'Baseline: mIoU = 82.40%, mF1 = 90.05%, IoU (water) = 72.87%, F1 (water) =
    84.31%'
  span_sha256: 3a108361333978d663527a022900193a8ac0a80a8baf9cad7e8036d15f2f407b
  task: flood_mapping
  value: 82.4
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: Kanyini cloud detection tile-level
  direction: worse
  id: du2025first#c4
  label_ratio: 1.0
  locator: Fig 4(a)
  metric: accuracy
  model: prithvi
  span: 'Baseline: Acc = 39.77%, F1 = 57.70%, FP = 47.41%'
  span_sha256: b6c471d87802e1de46cb8c1653ff14f19f6fd2666a0a55021c41ebfca8e73301
  task: crop_type_mapping
  value: 39.77
date: '2025-12-01'
doi: 10.48550/arxiv.2512.01181
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:43:57.478618Z'
key: du2025first
limitations:
- compute_cost
- spatial_transfer
- benchmark_narrowness
models:
- prithvi
proposed_tags:
- cloud_detection
- onboard_inference
- knowledge_distillation
- domain_adaptation
- flight_hardware_validation
- on_orbit_demonstration
regions:
- global
self_evaluation: false
tasks:
- flood_mapping
- landslide_susceptibility
- biomass_estimation
- semantic_segmentation
title: First On-Orbit Demonstration of a Geospatial Foundation Model
venue: arXiv
---

## summary

The paper compresses Prithvi-EO-2.0-300M via dual-MAE knowledge distillation into a 16x smaller variant (256-MAE-D) that retains performance across five downstream EO tasks. It identifies a domain gap between source (Sentinel-2/HLS) and target (Kanyini) data, shows domain adaptation and pretrained heads reduce labelled data needs, validates FP16 execution on flight-representative hardware (Myriad-2, Raspberry Pi 4), and demonstrates on-orbit inference aboard the ISS via IMAGIN-e.

## setup

Prithvi-EO-2.0-300M is distilled into compact ViT variants (512/256 embedding dim) via a dual-MAE distillation pretrained on HLS, then fine-tuned with task heads on Sentinel-2 Cloud Mask Catalogue, Sen1Floods11, Landslide4Sense, and BioMassters datasets; domain adaptation and hardware validation were performed using Kanyini mission imagery and IMAGIN-e ISS payload data.

## caveats

Authors note domain gap causes substantial performance degradation on Kanyini data (especially cloud detection) due to spatial resolution and radiometric mismatches with pretraining data; some tasks (landslide, AGB) could not be evaluated on Kanyini due to lack of ground truth; IMAGIN-e imager fault prevented live acquisition and domain adaptation for that mission.
