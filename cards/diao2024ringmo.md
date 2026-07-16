---
arxiv_id: '2409.13366'
authors:
- Wenhui Diao
- Haichen Yu
- Kaiyue Kang
- Tong Ling
- Di Liu
- Yingchao Feng
- Hanbo Bi
- Libo Ren
- Xuexue Li
- Yongqiang Mao
- Xian Sun
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G9_ecological_fine_scale
claims:
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: null
  dataset: FloodNet
  direction: better
  id: diao2024ringmo#c1
  label_ratio: null
  locator: Sec 5.2
  metric: miou
  model: prithvi
  span: significant gains in semantic segmentation (e.g., +4.66 mIoU on FloodNet)
  span_sha256: 961cb6748748df1566f5fccfb45815d9131fdf69f61f13c1cc296cc361da0c74
  task: semantic_segmentation
  value: 4.66
- axis: G5_cost
  baseline: task_specific
  baseline_value: 100.0
  dataset: UAVid/DroneVehicle
  direction: worse
  id: diao2024ringmo#c2
  label_ratio: null
  locator: Sec 5.3.2
  metric: miou
  model: prithvi
  span: requires a similar proportion of parameters(0.41%) to be adjusted as Adapter(0.39%)
  span_sha256: fedd20d23c15b9429b0e7e6b2e9db07af3a483adf72f1acee7be03e8710b5fc2
  task: semantic_segmentation
  value: 0.41
date: '2024-09-20'
doi: 10.48550/arxiv.2409.13366
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:06:16.506787Z'
key: diao2024ringmo
limitations:
- benchmark_narrowness
- compute_cost
- spatial_transfer
models: []
proposed_tags:
- aerial_remote_sensing
- object_detection
- object_tracking
- 3d_reconstruction
- scene_classification
- affine_transformation_contrastive_learning
- parameter_efficient_finetuning
- ringmo
regions:
- cn
- global
self_evaluation: true
tasks:
- semantic_segmentation
- change_detection
- flood_mapping
- land_cover_classification
title: 'RingMo-Aerial: An Aerial Remote Sensing Foundation Model With Affine Transformation
  Contrastive Learning'
venue: arXiv
---

## summary



## setup



## caveats


