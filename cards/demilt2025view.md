---
arxiv_id: '2510.03316'
authors:
- Ryan P. Demilt
- Nicholas LaHaye
- Karis Tenneson
axes:
- G3_spatial_transfer
- G11_complementarity
- G7_interpretability
claims:
- axis: G11_complementarity
  baseline: dofa
  baseline_value: 28.2
  dataset: Landsat 9 & HLS
  direction: worse
  id: demilt2025view#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: prithvi
  span: 28.5 / 30. 5/ 33.1
  span_sha256: 110f6fcc9727e182f095d116cba15a803256461249fc675320eb864410dee91e
  task: representation_probing
  value: 30.5
- axis: G9_ecological_fine_scale
  baseline: dofa
  baseline_value: 69.3
  dataset: USDA Crop Data Layer
  direction: worse
  id: demilt2025view#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: prithvi
  span: 'Landsat 8


    24.1


    57.0


    69.3'
  span_sha256: b149b4f07b8b1f060922690784a8a73c787aab2d61b46355cd589287e4d32f60
  task: crop_type_mapping
  value: 57.0
- axis: G7_interpretability
  baseline: task_specific
  baseline_value: null
  dataset: Crop Data Layer patch embeddings
  direction: worse
  id: demilt2025view#c3
  label_ratio: null
  locator: Table 3 / Sec 4
  metric: accuracy
  model: prithvi
  span: a simple Random Forest classifier can still get a shocking 90.7% and 88.7%
    accuracy for Prithvi and DOFA embeddings
  span_sha256: 4dfc198222ec0dfa5487971ec5c5c2dd83d3412fdc6920698b4b7f0de85cdd16
  task: representation_probing
  value: 90.7
- axis: G7_interpretability
  baseline: task_specific
  baseline_value: null
  dataset: Crop Data Layer patch embeddings
  direction: worse
  id: demilt2025view#c4
  label_ratio: null
  locator: Table 3 / Sec 4
  metric: accuracy
  model: dofa
  span: a shocking 90.7% and 88.7% accuracy for Prithvi and DOFA embeddings respectively
  span_sha256: 34c77558148ae3e73a9452a6458dc6decd35033c4ba07d1f28d93e7cd2c677c4
  task: representation_probing
  value: 88.7
date: '2025-10-01'
doi: 10.48550/arxiv.2510.03316
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:55:27.150841Z'
key: demilt2025view
limitations:
- spatial_transfer
- data_bias
- benchmark_narrowness
models:
- prithvi
- dofa
proposed_tags:
- sensor_modality_sensitivity
- embedding_space_clustering
- instrumentation_bias
regions:
- us
self_evaluation: false
tasks:
- representation_probing
- crop_type_mapping
title: 'The View From Space: Navigating Instrumentation Differences with EOFMs'
venue: arXiv
---

## summary

The paper evaluates Prithvi and DOFA foundation model embeddings on paired multi-sensor optical/SAR imagery (HLS, Landsat-8/9, Sentinel-2, Sentinel-1) over Indiana, finding that embedding spaces cluster strongly by sensor modality rather than by semantic content. Local neighborhood and TSNE analyses show that modality identity can be predicted from patch embeddings with over 88% accuracy, indicating sensor architecture heavily biases EOFM representations. DOFA shows somewhat greater but incomplete resilience to modality shifts compared to Prithvi.

## setup

600 randomly sampled points from Indiana, USA, with paired 224x224 2-month mosaic composites at 30m resolution across HLS, Landsat-8, Landsat-9, Sentinel-2 (optical) and Sentinel-1 (SAR-GRD), cloud-masked and aligned to the USDA Crop Data Layer as a semantic reference. Frozen Prithvi and DOFA encoders (via PANGAEA) are analyzed unsupervised using TSNE visualization and k-nearest-neighbor overlap of cls tokens and patch embeddings across modality pairs.

## caveats

The authors restrict analysis to frozen encoders and note fine-tuning effects are left to future work; the study uses only two models (Prithvi, DOFA) and a single geographic region (Indiana), and acknowledges that acquisition period misalignment across modalities introduces additional uncertainty into the comparison.
