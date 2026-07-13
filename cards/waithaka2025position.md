---
arxiv_id: '2506.06852'
authors:
- John Waithaka
- Moise Busogi
axes:
- G1_label_rich_parity
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Sen1Floods11
  direction: better
  id: waithaka2025position#c1
  label_ratio: null
  locator: Table 7
  metric: miou
  model: presto
  span: Satellite LOCA (ours)
  span_sha256: ecd9b47f60a5987da9dc93957c245f9bdfbaba4b0db32e3eb0c7d1d8845d8e42
  task: flood_mapping
  value: 85.49
date: '2025-06-07'
doi: 10.48550/arxiv.2506.06852
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T09:23:14.518279Z'
key: waithaka2025position
limitations:
- compute_cost
- benchmark_narrowness
models: []
proposed_tags:
- LOCA
- position_prediction_ssl
- channel_grouping
- same_group_attention_masking
- SatMAE
- MMEarth
- Sen1Floods11
regions:
- global
self_evaluation: false
tasks:
- flood_mapping
- semantic_segmentation
- representation_probing
title: Position Prediction Self-Supervised Learning for Multimodal Satellite Imagery
  Semantic Segmentation
venue: arXiv
---

## summary

The paper adapts LOCA, a position-prediction self-supervised pretraining method, to multimodal satellite imagery by extending SatMAE-style channel grouping to multiple modalities (MSI, SAR, DEM) and adding same-group attention masking to encourage cross-modal interaction. Pretrained on MMEarth and evaluated by end-to-end fine-tuning on Sen1Floods11 flood mapping, the method outperforms MAE-based satellite SSL baselines (SatMAE, SatMAE++, ScaleMAE, MMEarth's ConvNext-T scheme).

## setup

Models are pretrained on 300,000 samples from the MMEarth dataset using Sentinel-2, Sentinel-1, and Aster DEM modalities, then evaluated via end-to-end fine-tuning with a lightweight decoder on the Sen1Floods11 flood segmentation dataset, averaging results over three runs (single run for the comparison table).

## caveats

The authors note that adding modalities as separate channel groups increases pretraining task difficulty and can reduce position-prediction accuracy substantially; they only evaluate on a single downstream task/dataset (Sen1Floods11) and flag future work needed for scale-invariance, temporal dimension exploitation, additional modalities, and more diverse downstream tasks.
