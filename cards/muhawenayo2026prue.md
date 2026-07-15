---
arxiv_id: '2603.27101'
authors:
- Gedeon Muhawenayo
- Caleb Robinson
- Subash Khanal
- Zhanpei Fang
- Isaac Corley
- Alexander Wollam
- Tianyi Gao
- Leonard Strnad
- Ryan Avery
- Lyndon Estes
- Ana M. Tárano
- Nathan Jacobs
- Hannah Kerner
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
- G7_interpretability
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.7
  dataset: FTW
  direction: worse
  id: muhawenayo2026prue#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: clay
  span: Clay (ViT-L) was the best GFM performer (IoU=0.67, F1=0.36)
  span_sha256: 75285d675b7c65a9df36ab6d94ed8f0451949d898fba1d0eba3fee84e3b2e9d2
  task: semantic_segmentation
  value: 0.67
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.7
  dataset: FTW
  direction: worse
  id: muhawenayo2026prue#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: galileo
  span: 'Galileo


    ViT-Base


    0.66'
  span_sha256: 4afef38c630b47290af89f4d354808f41ab0eefab207d068d6c3e7e8994675d7
  task: semantic_segmentation
  value: 0.66
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.7
  dataset: FTW
  direction: worse
  id: muhawenayo2026prue#c3
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: 'Prithvi 2.0


    ViT-Large


    0.56'
  span_sha256: 3b69e12f2db5fd7648567d1460335fc847afc4fc36984a8b8691578a77fa443d
  task: semantic_segmentation
  value: 0.56
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.7
  dataset: FTW
  direction: worse
  id: muhawenayo2026prue#c4
  label_ratio: null
  locator: Table 1
  metric: miou
  model: croma
  span: 'CROMA


    ViT-Base


    0.52'
  span_sha256: 552bb5fd823ab6f47b72fb613258b3f53f2fe3466fb9999e3ef5d4608317e72a
  task: semantic_segmentation
  value: 0.52
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.7
  dataset: FTW
  direction: worse
  id: muhawenayo2026prue#c5
  label_ratio: null
  locator: Table 1
  metric: miou
  model: dofa
  span: 'DOFA-v1


    ViT-Large


    0.49'
  span_sha256: 4e4b4da2fadbde93f7ca618465ecc5dfddc84322441508a8c693e9e28e996791
  task: semantic_segmentation
  value: 0.49
- axis: G5_cost
  baseline: task_specific
  baseline_value: 623.28
  dataset: FTW
  direction: worse
  id: muhawenayo2026prue#c6
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: clay
  span: 'Clay: 11 km2/s vs. PRUE: 307 km2/s'
  span_sha256: 6be06c783663ef15fd011fcf71e04e5a5e3ac0e837a59eb0741d64ae8fb5d1c5
  task: semantic_segmentation
  value: 10.98
date: '2026-03-28'
doi: 10.48550/arxiv.2603.27101
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:40:37.198611Z'
key: muhawenayo2026prue
limitations:
- benchmark_narrowness
- compute_cost
- spatial_transfer
- mixed_pixels
- time_sensitivity
- interpretability
models:
- clay
- croma
- dofa
- galileo
- prithvi
- satmae
proposed_tags:
- field_boundary_delineation
- translation_consistency
- input_order_sensitivity
- preprocessing_robustness
- scale_sensitivity
- instance_segmentation
- panoptic_segmentation
regions:
- global
- jp
- mx
- rw
- za
- ch
self_evaluation: false
tasks:
- crop_type_mapping
- semantic_segmentation
title: 'PRUE: A Practical Recipe for Field Boundary Segmentation at Scale'
venue: arXiv
---

## summary

PRUE benchmarks 18 segmentation, instance, and geospatial foundation models on the Fields of The World (FTW) field boundary delineation task, finding that a systematically optimized U-Net (PRUE) with EfficientNet-B7 backbone outperforms all GFM and instance segmentation alternatives on pixel IoU and object F1. GFMs such as Clay and Galileo underperform specialized U-Net architectures despite having far more parameters, due to coarser effective spatial resolution. The paper also introduces new deployment-oriented robustness metrics (consistency under translation, input-order sensitivity, preprocessing robustness, scale sensitivity) and deploys PRUE at country scale in five countries.

## setup

Models are evaluated on the FTW benchmark (24 countries, bi-temporal Sentinel-2 RGBN imagery, 1.5M+ field polygons) using pixel-level IoU/F1 and object-level precision/recall/F1/AP metrics, with GFM encoders frozen and paired with a trained convolutional decoder over concatenated bi-temporal tokens. Deployment-oriented robustness metrics (translation consistency, input-order sensitivity, preprocessing sensitivity, scale sensitivity) are computed on the same test splits to assess real-world reliability.

## caveats

Authors note GFM encoders produce coarse patch-wise embeddings limiting fine-scale boundary accuracy, that Galileo did not fit into VRAM at any batch size, that consistency metrics only weakly correlate with performance (R2=0.48 and 0.30) so should not be sole reliability indicators, that latitude-based season heuristics and greedy scene selection are approximations, and that change detection analysis lacks ground-truth labels and relies on photo-interpretation rather than quantitative accuracy assessment.
