---
arxiv_id: '2606.12218'
authors:
- Sk Muhammad Asif
- Orhun Aydin
axes:
- G2_label_scarce_efficiency
- G5_cost
- G9_ecological_fine_scale
claims:
- axis: G5_cost
  baseline: prithvi
  baseline_value: 0.7541
  dataset: HLS T13TGE CDL fallow
  direction: better
  id: asif2026adapting#c1
  label_ratio: null
  locator: Table 4 / Abstract
  metric: accuracy
  model: prithvi
  span: achieves a mAP@50 of 0.9479 with the Diou loss
  span_sha256: ec5ff3538661675995d1795e7a7d2d80778d64f5fbe4daaa67e602363ceaffe9
  task: crop_type_mapping
  value: 0.9479
- axis: G2_label_scarce_efficiency
  baseline: prithvi
  baseline_value: 0.7541
  dataset: HLS T13TGE CDL fallow
  direction: better
  id: asif2026adapting#c2
  label_ratio: null
  locator: Sec 4.2
  metric: accuracy
  model: prithvi
  span: the DIoU-trained FCOS variant reaches mAP@50 = 0.8025 (+6.42% relative over
    the FR-CNN DIoU baseline)
  span_sha256: 5b668f666b0aee9118bfe1ff4870c1e8bd65145e6ba7b6176a0f96eb098fab2a
  task: crop_type_mapping
  value: 0.8025
- axis: G5_cost
  baseline: task_specific
  baseline_value: 0.607
  dataset: EuroCrops
  direction: better
  id: asif2026adapting#c3
  label_ratio: null
  locator: Sec 5.4
  metric: accuracy
  model: prithvi
  span: Their best result on EuroCrops achieves mAP@50 = 0.607
  span_sha256: abb83b9e3e50f291bde83b0c3e7dabe9b9f33d9116bfc931edb4ecd0ca713f43
  task: crop_type_mapping
  value: 0.7603
date: '2026-06-10'
doi: 10.48550/arxiv.2606.12218
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:38:43.121630Z'
key: asif2026adapting
limitations:
- benchmark_narrowness
- data_bias
- spatial_transfer
- temporal_transfer
- compute_cost
models:
- prithvi
proposed_tags:
- fallow_detection
- object_detection
- ViT-Adapter
- LoRA
- PEFT
- food_water_nexus
- FCOS
- Faster_RCNN
regions:
- us
self_evaluation: false
tasks:
- crop_type_mapping
title: 'Adapting Prithvi-EO for Fallow Detection for Food-Water Nexus: ViT-Adapter
  Necks and Parameter-Efficient Backbone tuning of Geospatial Foundation Model'
venue: arXiv
---

## summary



## setup



## caveats


