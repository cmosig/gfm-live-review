---
arxiv_id: '2603.01576'
authors:
- Saurabh Kaushik
- Lalit Maurya
- Beth Tellman
- Valerio Marsocci
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 91.58
  dataset: GLID
  direction: better
  id: kaushik2026cryo#c1
  label_ratio: null
  locator: Table 3
  metric: miou
  model: dofa
  span: DOFA achieves the highest performance on GLID and GLD, with mIoU scores of
    92.61 and 90.44
  span_sha256: 919325a51a25ab2acaf5a020544326868ff73c28306f85946584a79a5201b475
  task: semantic_segmentation
  value: 92.61
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 59.82
  dataset: CaFFe
  direction: worse
  id: kaushik2026cryo#c2
  label_ratio: null
  locator: Table 3
  metric: miou
  model: croma
  span: UNet Baseline
  span_sha256: ac91a136d22303011afb097692ce8e437e00925b7d329f5ab2a5c9ce417a3023
  task: semantic_segmentation
  value: 42.03
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 81.49
  dataset: GLID
  direction: better
  id: kaushik2026cryo#c3
  label_ratio: 0.1
  locator: Table 4
  metric: miou
  model: dofa
  span: DOFA remains the top-performing model on GLID and GLD
  span_sha256: df9a893f75bf7a7c073f49262c7df8a376a98529db528f3abfeb76cf46f0526b
  task: semantic_segmentation
  value: 88.21
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 36.48
  dataset: CaFFe
  direction: better
  id: kaushik2026cryo#c4
  label_ratio: 0.1
  locator: Table 4
  metric: miou
  model: prithvi
  span: achieving the highest scores on CaFFe (mIoU 55.00) and SICD (mIoU 24.54)
  span_sha256: 032dea04fc32ef79c188e421e2df1753c7fa0bb6aed7d1ee3d78594b0d6583f3
  task: semantic_segmentation
  value: 55.0
- axis: G5_cost
  baseline: null
  baseline_value: null
  dataset: GLID
  direction: better
  id: kaushik2026cryo#c5
  label_ratio: null
  locator: Sec 5.5
  metric: miou
  model: dofa
  span: DOFA attains the highest mIoU of 93.58 while requiring only 61.42 GFLOPs
  span_sha256: 5b0ff0286ef7a5d114c5debef582fa64e660f557e434acfa088dbd28e33475b4
  task: semantic_segmentation
  value: 93.58
date: '2026-03-02'
doi: 10.48550/arxiv.2603.01576
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:26:15.486684Z'
key: kaushik2026cryo
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
- spatial_transfer
- temporal_transfer
models:
- croma
- dofa
- prithvi
- scalemae
proposed_tags:
- cryosphere
- GFM-Swin
- RemoteCLIP
- SatlasNet
- SpectralGPT
- S12-MoCo
- S12-DINO
- S12-MAE
- S12-Data2Vec
- TerraMind
- RAMEN
- glacial_lake_mapping
- debris_covered_glacier_mapping
- sea_ice_mapping
- calving_front_mapping
- learning_rate_tuning
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- change_detection
- representation_probing
title: 'Cryo-Bench: Benchmarking Foundation Models for Cryosphere Applications'
venue: arXiv
---

## summary

Cryo-Bench is a new benchmark evaluating 14 geo-foundation models plus UNet/ViT baselines on five cryosphere semantic segmentation datasets (debris-covered glaciers, glacial lakes, sea ice, calving fronts). With frozen encoders UNet outperforms all GFMs on average, but GFMs like DOFA and TerraMind excel in few-shot (10% label) settings and benefit substantially from fine-tuning combined with learning-rate optimization.

## setup

Five datasets (GSDD, GLID, GLD, SICD, CaFFe) covering supraglacial debris, glacial lakes, sea ice, and calving fronts were evaluated following the Pangaea protocol, using a frozen encoder + UperNet decoder, few-shot (10% data), full fine-tuning, and learning-rate tuning (GLID, CaFFe) experiments.

## caveats

Authors note fine-tuning produces highly non-monotonic, inconsistent performance across datasets/models, frozen-encoder rank poorly predicts fine-tuning performance (r2=0.06), most GFMs have minimal cryosphere representation in pretraining data, and existing evaluation datasets entirely overlook the cryosphere prior to this work.
