---
arxiv_id: '2608.01751'
authors:
- Xingyan Li
- Jordan A. Caraballo-Vega
- Jie Gong
- Mark L. Carroll
- Jianwu Wang
axes:
- G2_label_scarce_efficiency
- G5_cost
- G3_spatial_transfer
- G6_compactness
claims:
- axis: G5_cost
  baseline: task_specific
  baseline_value: 85.1
  dataset: Sen1Floods11
  direction: better
  id: li2026spectra#c1
  label_ratio: null
  locator: Table 4
  metric: miou
  model: prithvi
  span: 86.39\pm 0.85
  span_sha256: 987b8c9540bf7af1a6b1c61e0747f1bf27db114cd0c730f8bdbc260885933dcf
  task: flood_mapping
  value: 86.39
- axis: G5_cost
  baseline: task_specific
  baseline_value: 77.17
  dataset: Sen1Floods11
  direction: better
  id: li2026spectra#c2
  label_ratio: null
  locator: Table 4/5.2
  metric: miou
  model: scalemae
  span: 'SPECTRA improves

    macro mIoU from 77.1777.17 with LoRA-64 and 75.4175.41 with Full-FT to 85.4585.45'
  span_sha256: a957325e859e5288ee53ae1236ea63a41f46ffacdaca08035db5379a82ac1b52
  task: flood_mapping
  value: 85.45
- axis: G5_cost
  baseline: task_specific
  baseline_value: 69.03
  dataset: FireScars
  direction: better
  id: li2026spectra#c3
  label_ratio: null
  locator: Sec 5.2
  metric: miou
  model: scalemae
  span: 'it improves macro mIoU from 69.0369.03 with LoRA-64 and 72.3072.30

    with Full-FT to 82.0582.05'
  span_sha256: edc73dd8e4a176ce0e629abb51ed910a55deb1f298c4d76ce47b353384e07c35
  task: flood_mapping
  value: 82.05
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 66.36
  dataset: matched GeoFM-dataset-policy cells
  direction: better
  id: li2026spectra#c4
  label_ratio: null
  locator: Table 5
  metric: miou
  model: presto
  span: 'BRE

    raises mean macro mIoU from 66.3666.36 to 69.2469.24 (+2.88+2.88 points)'
  span_sha256: 6b7cde3a260d1b41733a710031dadf57095bad6e9fce571b8f12976d044e3aea
  task: semantic_segmentation
  value: 69.24
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 86.58
  dataset: Sen1Floods11
  direction: worse
  id: li2026spectra#c5
  label_ratio: null
  locator: Table 6
  metric: miou
  model: prithvi
  span: ST-LoRA [8,16,16,8]
  span_sha256: 63fcfe3082c946ec5760558c5e6585947956de2fee65ef4b2dae455c79451df1
  task: flood_mapping
  value: 85.88
date: '2026-08-03'
doi: 10.48550/arxiv.2608.01751
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-05T00:20:02.682736Z'
key: li2026spectra
limitations:
- benchmark_narrowness
- compute_cost
- spatial_transfer
models: []
proposed_tags:
- cross_sensor_adaptation
- band_routed_embedding
- LoRA_rank_allocation
- spectral_mismatch
- Prithvi-EO-2.0
- ScaleMAE
- SatMAE
- LogME_transferability
regions:
- global
self_evaluation: false
tasks:
- flood_mapping
- landslide_susceptibility
- crop_type_mapping
- semantic_segmentation
title: 'SPECTRA: Band-Routed Embedding and Stage-Wise LoRA for Cross-Sensor Fine-Tuning
  of Geospatial Foundation Models'
venue: arXiv
---

## summary

SPECTRA is a parameter-efficient fine-tuning framework for geospatial foundation models that addresses spectral mismatch via Band-Routed Embedding (BRE) and reduces fine-tuning cost via Stage-wise Transferability-aware LoRA (ST-LoRA). Across three EO-pretrained GeoFMs (Prithvi-EO-2.0, ScaleMAE, SatMAE) and four segmentation datasets, BRE improves mean macro mIoU by +2.88 points over band-selection baselines while a naive MLP projector hurts performance, and ST-LoRA reduces trainable parameters relative to full fine-tuning and uniform LoRA.

## setup

Evaluated on Sen1Floods11, FireScars, Landslide4Sense, and GEO-Bench SA Crop Type segmentation datasets using UPerNet decoders, comparing linear probing, uniform LoRA (ranks 8-64), Surgical fine-tuning, Full-FT, and SPECTRA across 3 seeds. Trainable-parameter percentages and macro mIoU/F1/foreground IoU are reported for 12 backbone-dataset combinations.

## caveats

The authors note BRE gains are not universal and shrink when pretrained and downstream bands are already well-matched (e.g., Prithvi-FireScars); ST-LoRA evidence is strongest only on Sen1Floods11 and broader validation across datasets is still needed; the study uses constrained hyperparameters and a single decoder architecture, so results are not claimed as state-of-the-art.
