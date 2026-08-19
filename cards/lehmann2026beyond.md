---
arxiv_id: '2608.16614'
authors:
- Nils Lehmann
- Jakob Gawlikowski
- Burak Ekim
- Isaac Corley
- Xiao Xiang Zhu
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G7_interpretability
- G8_uncertainty
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: four-dataset classification canon
  direction: worse
  id: lehmann2026beyond#c1
  label_ratio: null
  locator: Table IV
  metric: accuracy
  model: clay
  span: Clay V1.5 0.849 0.025
  span_sha256: 377dd0a9babfdea0a42b4c4556f9f096c7c7e0be10fe0697a68983c0ddcb482b
  task: representation_probing
  value: 0.849
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: four-dataset classification canon
  direction: worse
  id: lehmann2026beyond#c2
  label_ratio: null
  locator: Table IV
  metric: accuracy
  model: prithvi
  span: Prithvi-v2-300 0.825 0.062
  span_sha256: d664b63461783fcf5edc3460af28eb91a2820dc4da3bada0b448a8fe8174d6dc
  task: representation_probing
  value: 0.825
- axis: G8_uncertainty
  baseline: dofa
  baseline_value: null
  dataset: four-dataset classification canon (cloud severity 3)
  direction: worse
  id: lehmann2026beyond#c3
  label_ratio: null
  locator: Table IV / Sec IV-B
  metric: accuracy
  model: clay
  span: Clay and TerraMind are the worst of the learned encoders
  span_sha256: edd953695c863a0823d2b787818128a550f6ffef9f1c9ac38c97c83c1b1a64f1
  task: representation_probing
  value: 0.5
- axis: G5_cost
  baseline: null
  baseline_value: null
  dataset: four-dataset classification canon
  direction: parity
  id: lehmann2026beyond#c4
  label_ratio: null
  locator: Sec III-C
  metric: accuracy
  model: clay
  span: 'clean ECE is

    indistinguishable (0.0230.023 vs. 0.0240.024; Table IV'
  span_sha256: f7ad62df234e7dfecf58ddf1f6dba7be75d013fe14c57573dfefb59ad7ecf0ff
  task: representation_probing
  value: 0.023
date: '2026-08-17'
doi: 10.48550/arxiv.2608.16614
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-19T00:13:08.844707Z'
key: lehmann2026beyond
limitations:
- benchmark_narrowness
- compute_cost
- interpretability
- temporal_transfer
- uncertainty
- spatial_transfer
models: []
proposed_tags:
- calibration
- expected_calibration_error
- distribution_shift_robustness
- temperature_scaling
- deep_ensembles
- gaussian_process_probe
- selective_prediction
- representation_drift_CKA
- training_data_budget_sweep
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
- crop_type_mapping
- urban_signal_mapping
- representation_probing
title: 'Beyond Accuracy: Assessing Calibration of Geospatial Foundation Models and
  Their Sensitivity to Distribution Shifts'
venue: arXiv
---

## summary



## setup



## caveats


