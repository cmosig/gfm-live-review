---
arxiv_id: '2605.10184'
authors:
- Paul Vermeeren
- Heysem Kaya
axes:
- G2_label_scarce_efficiency
- G6_compactness
- G3_spatial_transfer
- G4_temporal_transfer
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 55.6
  dataset: Vegetation Monitoring
  direction: better
  id: vermeeren2026developing#c1
  label_ratio: null
  locator: Table II
  metric: f1
  model: dofa
  span: 'Reed

    61

    65'
  span_sha256: abc5bb3e4cec42a40b0ce2f7cea6f8cf7e244e534e545513a8291f024f747efc
  task: semantic_segmentation
  value: 68.3
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: RESISC-45
  direction: parity
  id: vermeeren2026developing#c2
  label_ratio: null
  locator: Table III
  metric: accuracy
  model: dofa
  span: 'Foundation Model

    -

    0.28M

    30M (Swin-T)

    91.27

    95.59'
  span_sha256: 28597328d622128d13af77c97bc4a050da6e5e64338cc8f9f053d792d5051029
  task: land_cover_classification
  value: 95.59
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: UC-Merced
  direction: parity
  id: vermeeren2026developing#c3
  label_ratio: null
  locator: Table IV
  metric: accuracy
  model: dofa
  span: 'Foundation Model

    -

    0.28M

    32M (Swin-T)

    98.10'
  span_sha256: c8425935e8b948608af09e92e51f88820a52fe936625ccc7eafe44949d1cc097
  task: land_cover_classification
  value: 98.1
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 86.68
  dataset: Potsdam
  direction: worse
  id: vermeeren2026developing#c4
  label_ratio: null
  locator: Table V
  metric: miou
  model: dofa
  span: 'Foundation Model

    -

    0.28M

    31M (Swin-T)

    72.87

    87.48

    87.94'
  span_sha256: a0fc64d73416e39a6e33e90df38b44169b0cf4c1166c5993904d83a333302f0a
  task: semantic_segmentation
  value: 72.87
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 91.93
  dataset: LEVIR-CD
  direction: worse
  id: vermeeren2026developing#c5
  label_ratio: null
  locator: Table VI
  metric: f1
  model: dofa
  span: 'Foundation model

    -

    0.28M

    33M (Swin-T)

    78.74

    88.10

    98.83'
  span_sha256: 5d6652e97dcf8c1756a0a4dd6429042d660bd8defa4dc6cf84161734ead26b05
  task: change_detection
  value: 88.1
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 89.85
  dataset: RESISC-45
  direction: worse
  id: vermeeren2026developing#c6
  label_ratio: 0.1
  locator: Table III
  metric: accuracy
  model: dofa
  span: 'Foundation Model

    -

    0.28M

    32M (Swin-T)

    82.71

    88.81'
  span_sha256: 3a4bb8ace688744b1c35a07ece0dc999b92b0d438dac29b3f0a0fb3d71230d6d
  task: land_cover_classification
  value: 82.71
date: '2026-05-11'
doi: 10.48550/arxiv.2605.10184
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:08:50.361529Z'
key: vermeeren2026developing
limitations:
- compute_cost
- spatial_transfer
- benchmark_narrowness
- data_bias
models:
- dofa
proposed_tags:
- hybrid_vit_cnn_swin
- temporal_multitemporal_pretraining
- vegetation_monitoring_netherlands
- high_resolution_pleiades_superview
regions:
- nl
- global
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
- change_detection
title: Developing a foundation model for high-resolution remote sensing data of the
  Netherlands
venue: arXiv
---

## summary



## setup



## caveats


