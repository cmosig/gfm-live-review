---
arxiv_id: '2503.07890'
authors:
- Yuru Jia
- Valerio Marsocci
- Ziyang Gong
- Xue Yang
- Maarten Vergauwen
- Andrea Nascetti
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 58.1
  dataset: m-NeonTree
  direction: better
  id: jia2025can#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: dofa
  span: particularly large gains on m-NeonTree, m-cashew-plantation, and m-chesapeake-landcover
  span_sha256: 033a600a9c8e3774b70ef568af08d7950e8cad2f977d41173a8174ceede5810f
  task: semantic_segmentation
  value: 63.4
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 65.7
  dataset: m-chesapeake-landcover
  direction: better
  id: jia2025can#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: dofa
  span: 5.7%, 4.3%, and 5.9% improvements over the strongest baselines
  span_sha256: 256585ff1dcbb353768dafebc86f3d390b7ebabb1cbd9f1ed406cfdb5b49a6f0
  task: semantic_segmentation
  value: 71.6
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 58.3
  dataset: m-bigearthnet
  direction: better
  id: jia2025can#c3
  label_ratio: null
  locator: Table 2
  metric: f1
  model: dofa
  span: improvements of up to +7.9% on m-bigearthnet, +5.9% on m-forestnet, and +3.9%
    on m-so2sat
  span_sha256: 1626569cb3bbca6aa9d350ae420ee9daca9683c9d01464002ad56151297aa718
  task: land_cover_classification
  value: 66.2
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 34.3
  dataset: m-cashew-plantation
  direction: better
  id: jia2025can#c4
  label_ratio: 0.1
  locator: Table 6
  metric: miou
  model: dofa
  span: SatDiFuser maintains robust performance in limited-data scenarios
  span_sha256: 271368bf0e11b5b93730bd7dfdd8c4f8a9a9f3f57fcf289738f8fc8f31da902b
  task: semantic_segmentation
  value: 39.6
date: '2025-03-10'
doi: 10.48550/arxiv.2503.07890
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:51:00.253537Z'
key: jia2025can
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
models: []
proposed_tags:
- diffusion_model
- DiffusionSat
- GEO-Bench
- feature_fusion
- mixture_of_experts
- self_supervised_representation_learning
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- crop_type_mapping
- representation_probing
title: Can Generative Geospatial Diffusion Models Excel as Discriminative Geospatial
  Foundation Models?
venue: arXiv
---

## summary



## setup



## caveats


