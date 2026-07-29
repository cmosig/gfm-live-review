---
arxiv_id: '2607.23908'
authors:
- Syed Roshaan Ali Shah
- Kristof Van Tricht
- Christina Butsko
- Jeroen Degerickx
- Zoltan Szantoi
axes:
- G2_label_scarce_efficiency
- G9_ecological_fine_scale
- G7_interpretability
- G8_uncertainty
claims:
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: null
  dataset: WorldCereal (Eastern Africa)
  direction: better
  id: shah2026embeddings#c1
  label_ratio: null
  locator: Table 1
  metric: auc
  model: presto
  span: Eastern Africa 0.66 2.5 0.67 2.6
  span_sha256: 04b8d77837143e59719b5074929461c65b0f325865a126124931238d6e82e064
  task: crop_type_mapping
  value: 0.66
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: null
  dataset: WorldCereal (South-Eastern Asia)
  direction: better
  id: shah2026embeddings#c2
  label_ratio: null
  locator: Table 1
  metric: auc
  model: presto
  span: South-Eastern Asia 0.84 5.0 0.66 3.0
  span_sha256: 52c659d93b9d5ae10648850da3d8e1df38de15769226ca57592206dad656c79a
  task: crop_type_mapping
  value: 0.84
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.786
  dataset: WorldCereal regional (Middle Africa)
  direction: better
  id: shah2026embeddings#c3
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: presto
  span: Middle Africa CT 0.786 0.820 +3.4
  span_sha256: 47927459242394cc7251c8cfb8c8316ea1377157f18453fae8ce72f771b8efb8
  task: crop_type_mapping
  value: 0.82
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.905
  dataset: WorldCereal regional (South-Eastern Asia)
  direction: better
  id: shah2026embeddings#c4
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: presto
  span: South-Eastern Asia CT 0.905 0.926 +2.2
  span_sha256: 7d7053f6e17827848552fd8a90d9299c35d6ce1076fdd534968f5552e590fb42
  task: crop_type_mapping
  value: 0.926
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.804
  dataset: WorldCereal regional (South-Eastern Asia)
  direction: better
  id: shah2026embeddings#c5
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: presto
  span: South-Eastern Asia LC 0.804 0.821 +1.7
  span_sha256: 25625bbf2457e5218e457e3a637aacb2016cd11b055867060e031f5d7222cfa3
  task: land_cover_classification
  value: 0.821
date: '2026-07-27'
doi: 10.48550/arxiv.2607.23908
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-29T00:17:24.817987Z'
key: shah2026embeddings
limitations:
- data_bias
- mixed_pixels
- interpretability
- uncertainty
- benchmark_narrowness
models:
- alphaearth
proposed_tags:
- label_noise_cleaning
- anomaly_detection
- WorldCereal
- Presto_embeddings
- reference_data_quality
regions:
- global
self_evaluation: false
tasks:
- crop_type_mapping
- land_cover_classification
title: Embeddings based Anomaly Detection for Cleaning Global Crop Type Reference
  Datasets
venue: arXiv
---

## summary

The paper proposes EBA, a locality-aware anomaly detection framework built on Presto-style Earth-observation embeddings to identify and clean mislabelled samples in the WorldCereal crop-type/land-cover reference dataset. Flagged points are validated via synthetic noise injection (AUROC up to 0.84, enrichment 2.5-5x) and a model-independent real-data test, and removing/down-weighting flagged points improves downstream crop-type and land-cover model macro-F1 across five macro-regions. The authors also demonstrate the pipeline transfers to AlphaEarth embeddings qualitatively.

## setup

Reference data comes from the WorldCereal Reference Data Module, with samples paired to 12-monthly composited multi-modal EO signals and embedded via a pretrained Presto-style encoder (d=128) into local H3-grid, same-class slices scored by centroid and kNN cosine distance. Evaluation spans synthetic label-noise recovery, a model-independent held-out-set test, a fast CatBoost proxy sweep, and full dual-head WorldCereal finetuning across five macro-regions (Eastern Africa, Middle Africa, South-Eastern Asia, South America, Southern Asia).

## caveats

Authors note the detector fails against whole-dataset systematic corruption (near-chance AUROC ~0.50); embeddings inherit biases of the frozen pretrained encoder and may lack separability in some regions (e.g., Eastern Africa, weakest at 2.5x/AUROC 0.66); some flagged points may reflect legitimate rare practices or mixed pixels rather than true errors; over-cleaning (removing all flagged points) hurts performance; and a full benchmark across other geospatial foundation models is left to future work.
