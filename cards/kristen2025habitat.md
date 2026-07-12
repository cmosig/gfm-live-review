---
arxiv_id: '2511.00073'
authors:
- Harald Kristen
- Daniel Kulmer
- Manuela Hirschmugl
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G4_temporal_transfer
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.41
  dataset: HabitAlp (Gesäuse NP)
  direction: better
  id: kristen2025habitat#c1
  label_ratio: null
  locator: Table 5
  metric: accuracy
  model: clay
  span: Clay 1.0 achieving the highest performance with 51% overall accuracy and 0.19
    macro IoU
  span_sha256: a8aae7ca708500e29baa8740680638590f158f9852281e8ad57418f12c1cfa62
  task: change_detection
  value: 0.51
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.14
  dataset: HabitAlp (Gesäuse NP)
  direction: better
  id: kristen2025habitat#c2
  label_ratio: null
  locator: Table 5
  metric: miou
  model: clay
  span: outperforming both the U-Net baseline (41% accuracy, 0.14 IoU)
  span_sha256: 260f3951f40cf69142e32a2e24de1893854e04a9428051f5392c78abc3b38554
  task: change_detection
  value: 0.19
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.41
  dataset: HabitAlp (Gesäuse NP)
  direction: better
  id: kristen2025habitat#c3
  label_ratio: null
  locator: Table 5
  metric: accuracy
  model: prithvi
  span: Prithvi (46% accuracy, 0.15 IoU)
  span_sha256: 6a2718e2c1ef7b590abfd4615cd1ea6fc6d7b2466ba468f10bc9705777f2720c
  task: change_detection
  value: 0.46
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.67
  dataset: HabitAlp (Gesäuse NP)
  direction: parity
  id: kristen2025habitat#c4
  label_ratio: null
  locator: Sec 4.1.1
  metric: accuracy
  model: clay
  span: both the baseline and foundation model approaches in the post-classification
    CD achieved 67% overall accuracy
  span_sha256: 717ce0c7b3b72fe41b86444c3a0e28330e286802f5ff280b489cf0ef34253aef
  task: change_detection
  value: 0.67
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.23
  dataset: HabitAlp (Gesäuse NP), 2013-2020
  direction: better
  id: kristen2025habitat#c5
  label_ratio: null
  locator: Sec 4.1.2
  metric: accuracy
  model: clay
  span: Prithvi achieved the highest multi-class overall accuracy at 37%, followed
    by Clay 1.0 at 33% and U-Net at 23%
  span_sha256: a61793cc6ea1c7c0c35da082a07c12ff95932d55136d57e56a1bf7955276d771
  task: change_detection
  value: 0.33
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.49
  dataset: HabitAlp (Gesäuse NP), 2013-2020
  direction: better
  id: kristen2025habitat#c6
  label_ratio: null
  locator: Table 6
  metric: accuracy
  model: clay
  span: U-Net post-classification showed the largest degradation at 18 points (from
    67% to 49%)
  span_sha256: 56514c1d4ae2e7fe6486350337ccf3da83fb5af5f257f37a8cc81cd40856482a
  task: change_detection
  value: 0.56
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.3
  dataset: HabitAlp (Gesäuse NP)
  direction: better
  id: kristen2025habitat#c7
  label_ratio: null
  locator: Table 8 / Sec 4.2
  metric: accuracy
  model: clay
  span: Integrating LiDAR improves semantic segmentation from 30% to 50% accuracy
  span_sha256: b12b0b2615d89ad87855d8af1ac0842af7a2127b3faef5af5fce548603e73421
  task: semantic_segmentation
  value: 0.5
date: '2025-10-29'
doi: 10.48550/arxiv.2511.00073
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:45:19.772874Z'
key: kristen2025habitat
limitations:
- benchmark_narrowness
- data_bias
- time_sensitivity
- mixed_pixels
models:
- prithvi
- clay
proposed_tags:
- alpine_habitat_monitoring
- post_classification_vs_direct_change_detection
- multimodal_lidar_fusion
- changevit
- unet_baseline
regions:
- at
self_evaluation: false
tasks:
- change_detection
- land_cover_classification
- semantic_segmentation
title: 'Habitat and Land Cover Change Detection in Alpine Protected Areas: A Comparison
  of AI Architectures'
venue: arXiv
---

## summary

The paper compares post-classification change detection using GFMs Prithvi-EO-2.0 and Clay v1.0 versus U-Net CNN baselines, and direct change detection using ChangeViT versus U-Net, for multi-class alpine habitat change mapping in Gesäuse National Park, Austria. Clay v1.0 modestly outperforms U-Net and Prithvi on multi-class accuracy in-domain and shows better robustness under cross-temporal (2020) evaluation, while direct CD (U-Net) achieves higher IoU for binary change detection. Adding LiDAR-derived nDSM and terrain attributes substantially improves single-date semantic segmentation but has limited effect on change detection accuracy.

## setup

Ground truth is the HabitAlp dataset (30,241 polygons, 23 reclassified habitat classes, 8 change-transition classes) for Gesäuse National Park, Austria, using 2003, 2013 and partial 2020 aerial RGB/CIR imagery plus LiDAR-derived DTM/DSM/nDSM and terrain attributes at up to 20cm-1m resolution. Post-classification models (U-Net, Prithvi-EO-2.0 300M, Clay v1.0) are fine-tuned on 2013 multimodal data and evaluated in-domain (2013 test split) and cross-temporally (2020); direct change models (U-Net, ChangeViT) are trained on 2003-2013 RGB-only transitions and evaluated on binary and multi-class change detection.

## caveats

Authors note overall accuracies remain far below literature benchmarks and are not yet sufficient for standalone operational monitoring; direct CD was restricted to RGB-only due to missing multimodal data for 2003, preventing fair comparison with post-classification; ChangeViT could not produce multi-class results, suggesting architectural limitations; severe class imbalance caused IoU below 0.2 for most rare (<2% area) transition classes; cross-temporal evaluation showed substantial performance degradation for multi-class detection, indicating limited temporal generalization.
