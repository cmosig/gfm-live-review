---
arxiv_id: '2606.14760'
authors:
- Yu Luo
- Kun Hu
- Mengwei He
- Xiaogang Zhu
- Shan Zeng
- Allen Benter
- Wei Xiang
- Patrick Filippi
- Thomas Francis Bishop
- Zhiyong Wang
axes:
- G3_spatial_transfer
- G5_cost
- G9_ecological_fine_scale
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 73.82
  dataset: GeoBench (Avg.P)
  direction: better
  id: luo2026georope#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: dofa
  span: reaching 84.21, 65.71, and 74.96, respectively, showing the clearest overall
    gains
  span_sha256: 25584753428adad02496d1f1570c516128a415c86680b4dc0dc9fa9438420d8e
  task: representation_probing
  value: 74.96
date: '2026-06-08'
doi: 10.48550/arxiv.2606.14760
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:57:13.332909Z'
key: luo2026georope
limitations:
- spatial_transfer
- data_bias
- interpretability
models:
- scalemae
- dofa
proposed_tags:
- rotary_position_embedding
- GSD_calibration
- parameter_efficient_fine_tuning
- adapter
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
- local_climate_zone_classification
- crop_type_mapping
- representation_probing
title: 'GeoRoPE: Ground-Aware Rotary Adaptation for Remote Sensing Foundation Models'
venue: arXiv
---

## summary

GeoRoPE is a lightweight, ground-aware rotary position embedding adapter for remote sensing foundation models that recalibrates token-grid offsets into physically meaningful ground distances (GCC) and modulates positional sensitivity by scene granularity (GFC).

## setup

Evaluated on GeoBench, comprising six classification datasets and six segmentation datasets spanning GSDs from 0.1m to 15m, injected into ScaleMAE, SatLas, and DOFA backbones via a frozen-backbone attention-parallel adapter, compared against PEFT baselines (BitFit, NormTuning, LoRA, SLR).

## caveats

Authors note physical calibration relies on availability of sensor metadata and does not address terrain relief or temporal changes, and the semantic-guided frequency modulation may be sensitive to dataset-specific spatial textures under limited target data.
