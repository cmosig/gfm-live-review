---
arxiv_id: '2309.14500'
authors:
- Wenwen Li
- Hyunho Lee
- Sizhe Wang
- Chia-Yu Hsu
- Samantha T. Arundel
axes:
- G1_label_rich_parity
- G3_spatial_transfer
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 90.8
  dataset: Sen1Floods11
  direction: worse
  id: li2023assessment#c1
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: IBM-NASA’s Prithvi 89.59
  span_sha256: 9c301e8cb716ef613c9f25252dac39ee613e608b5f0807f95ddf1eb2631dd4ae
  task: flood_mapping
  value: 89.59
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 82.54
  dataset: Sen1Floods11 (unseen Bolivia)
  direction: better
  id: li2023assessment#c2
  label_ratio: null
  locator: Table 3
  metric: miou
  model: prithvi
  span: IBM-NASA’s Prithvi 86.02
  span_sha256: 843d43b3b663d3e52f8278cb3ea22e6d0441a15c90d8008a44ac00880a06640a
  task: flood_mapping
  value: 86.02
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 73.73
  dataset: Sen1Floods11 (unseen Bolivia)
  direction: better
  id: li2023assessment#c3
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: prithvi
  span: with a nearly 4% gap in both mIoU and mAcc compared to Prithvi
  span_sha256: e370103f721c484aed5e79d39d0ca75160005a1de774d58ee16275f8c4c69ed4
  task: flood_mapping
  value: 82.12
date: '2023-09-25'
doi: 10.1145/3615886.3627747
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:51:28.030713Z'
key: li2023assessment
limitations:
- benchmark_narrowness
- interpretability
models:
- prithvi
proposed_tags:
- multi_scale_representation_learning
- end_to_end_pipeline
- input_band_flexibility
regions:
- bo
- gh
- in
- ng
- pk
- py
- so
- es
- lk
- us
- vn
self_evaluation: false
tasks:
- flood_mapping
title: Assessment of a new GeoAI foundation model for flood inundation mapping
venue: arXiv
---

## summary

This paper independently evaluates IBM-NASA's Prithvi geospatial foundation model on flood inundation mapping using Sen1Floods11, comparing it against U-Net and Segformer baselines. Prithvi underperforms U-Net on in-distribution test data but outperforms both U-Net and Segformer on completely unseen Bolivia data, indicating stronger spatial transferability. The authors identify limitations including lack of multi-scale features, no end-to-end architecture for downstream tasks, and rigid 6-band input requirements.

## setup

Sen1Floods11 dataset (446 Sentinel-1/Sentinel-2 image pairs, 512x512 px, 10m resolution, 11 flood events across 11 countries, 2016-2019) is used to fine-tune Prithvi, U-Net, and Segformer (B0 and B5) for 3-class semantic segmentation (flood, non-flood, no data) using the MMSegmentation framework, evaluated on both in-region test data and an entirely unseen Bolivia dataset over 10 runs each.

## caveats

The authors note Prithvi underperforms on test data with narrow flood features (e.g., rivers) due to its single-level ViT backbone lacking multi-scale representation learning; it requires 6 fixed spectral bands limiting flexibility; and it lacks an end-to-end architecture for high-level tasks, requiring additional decoder heads that may limit adoption by non-expert users.
