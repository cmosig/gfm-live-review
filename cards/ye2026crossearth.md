---
arxiv_id: '2603.12008'
authors:
- Ziqi Ye
- Ziyang Gong
- Ning Liao
- Xiaoxing Hu
- Di Wang
- Hongruixuan Chen
- Chen Huang
- Yiguo He
- Yuru Jia
- Xiaoxing Wang
- Haipeng Wang
- Xue Yang
- Junchi Yan
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G6_compactness
- G2_label_scarce_efficiency
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: VV2F
  direction: worse
  id: ye2026crossearth#c1
  label_ratio: null
  locator: Table 2
  metric: miou
  model: satmae
  span: SatMAE
  span_sha256: 160f3ad8cdd6d929647cd0aa6b581f9942061a81b0ca9c495802637e0f85689e
  task: semantic_segmentation
  value: 22.5
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: N2S
  direction: worse
  id: ye2026crossearth#c2
  label_ratio: null
  locator: Table 2
  metric: miou
  model: satmae
  span: '26.2'
  span_sha256: 9ed884cf60b8bb2015ad434983147b0a3da9ff59528d7e08e6ee9a1064e5823a
  task: semantic_segmentation
  value: 26.2
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: N2S
  direction: worse
  id: ye2026crossearth#c3
  label_ratio: null
  locator: Table 2
  metric: miou
  model: scalemae
  span: '26.4'
  span_sha256: 72b318af556bf4f82e16a23e369f7d8084c3489ee18390758abc7d3e936528dc
  task: semantic_segmentation
  value: 26.4
date: '2026-03-12'
doi: 10.48550/arxiv.2603.12008
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:40:56.657229Z'
key: ye2026crossearth
limitations:
- spatial_transfer
- data_bias
- benchmark_narrowness
- mixed_pixels
models:
- scalemae
- satmae
proposed_tags:
- SAR_foundation_model
- physics_guided_MoE
- domain_generalization
- speckle_noise
- polarization_shift
regions:
- global
- cn
- kr
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- change_detection
title: 'CrossEarth-SAR: A SAR-Centric and Billion-Scale Geospatial Foundation Model
  for Domain Generalizable Semantic Segmentation'
venue: arXiv
---

## summary

CrossEarth-SAR is a billion-scale SAR-specific vision foundation model using a physics-guided sparse mixture-of-experts architecture built on DINOv2, targeting domain-generalizable semantic segmentation of SAR imagery. The authors also release CrossEarth-SAR-200K, a 200K-image weakly/fully supervised SAR dataset, and a 22-sub-benchmark suite spanning 8 domain gaps (region, polarization, complex value, platform, microwave band).

## setup

Continuous pre-training of DINOv2 with the physics-guided sparse MoE on CrossEarth-SAR-200K (203K images across 7 classes), then frozen-backbone decoder fine-tuning on source domains and evaluation on unseen target domains across 22 sub-benchmarks derived from AIR-PolSAR-Seg 2.0, DDHR-SK, FUSAR-Map, OpenEarthMap-SAR, SARBuD, and WHU-OPT-SAR. Baselines compared include SatMAE, ScaleMAE, MTP, DOFA, RemoteCLIP, DINOv2/v3, and SARATR-X.

## caveats

The authors note SAR's inherent speckle noise, side-looking geometric distortions (layover, foreshortening, shadow), and backscatter-based semantic ambiguity as core physical challenges; they also report that CrossEarth-SAR does not always beat the DINOv2 baseline on some multi-gap benchmarks (e.g., D2O, D2F), and acknowledge many challenges remain unaddressed in SAR domain-generalization research.
