---
arxiv_id: '2511.10177'
authors:
- Tishya Chhabra
- Manisha Bajpai
- Walter Zesk
- Skylar Tibbits
axes:
- G2_label_scarce_efficiency
- G6_compactness
claims:
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: Maldives Sentinel-2 Coastline Dataset
  direction: better
  id: chhabra2025utilizing#c1
  label_ratio: null
  locator: Table 1
  metric: f1
  model: prithvi
  span: '5 images


    0.8509


    0.7977


    0.9612'
  span_sha256: d86d1959b0441644f467114f04ee54c6ff1a455ad1b42d51b9582d131b860dab
  task: semantic_segmentation
  value: 0.9612
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Maldives Sentinel-2 Coastline Dataset
  direction: better
  id: chhabra2025utilizing#c2
  label_ratio: null
  locator: Table 1
  metric: f1
  model: prithvi
  span: 125 images
  span_sha256: 3ef577400166abf34fb78e2c0f86140d498a1dbfbb9815025e38105b40deb99a
  task: semantic_segmentation
  value: 0.9913
- axis: G6_compactness
  baseline: prithvi
  baseline_value: 0.9912
  dataset: Maldives Sentinel-2 Coastline Dataset
  direction: parity
  id: chhabra2025utilizing#c3
  label_ratio: null
  locator: Results Sec 4
  metric: f1
  model: prithvi
  span: Our highest F1 score is Prithvi 600M at 0.9912, with Prithvi 300M closely
    following at 0.9908
  span_sha256: 3fda308bd3c09c09c5a523428b4f07afcfdea0ec54fcb3a9788c7068f64d427f
  task: semantic_segmentation
  value: 0.9908
date: '2025-11-13'
doi: 10.48550/arxiv.2511.10177
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:43:50.181047Z'
key: chhabra2025utilizing
limitations:
- benchmark_narrowness
- spatial_transfer
models:
- prithvi
proposed_tags:
- shoreline_delineation
- coastline_monitoring
regions:
- mv
self_evaluation: false
tasks:
- semantic_segmentation
title: Utilizing a Geospatial Foundation Model for Coastline Delineation in Small
  Sandy Islands
venue: arXiv
---

## summary

The paper fine-tunes Prithvi-EO-2.0 (300M and 600M) on a newly curated, hand-labeled dataset of 225 Sentinel-2 images of two Maldivian islands for shoreline/coastline segmentation. Even with as few as 5 training images, both models achieve F1 > 0.94 and IoU > 0.79, with minimal difference between the two model sizes.

## setup

225 multispectral Sentinel-2 GeoTIFFs (10m resolution) of two Maldivian islands, hand-labeled for water/land via Kili Technology, split into 181 train / 22 val / 22 test images, with smaller training subsets (5-150 images) used to study label efficiency; ViT backbone frozen and a U-Net-style decoder fine-tuned for 30 epochs.

## caveats

Authors note possible overfitting since training data covers only two islands in the Maldives, and flag that generalization beyond this narrow region, causes of the performance peak at 125 images, and comparison to other segmentation approaches remain unexplored.
