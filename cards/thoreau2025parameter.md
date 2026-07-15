---
arxiv_id: '2503.09493'
authors:
- Romain Thoreau
- Valerio Marsocci
- Dawa Derksen
axes:
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G3_spatial_transfer
claims:
- axis: G5_cost
  baseline: null
  baseline_value: null
  dataset: BurnScars
  direction: parity
  id: thoreau2025parameter#c1
  label_ratio: null
  locator: Table 2
  metric: miou
  model: scalemae
  span: DEFLECT (ours) 0.2% 53.2 97.8 44.1 77.3 50.6
  span_sha256: 5b1b62db9e7d6b3a2daf726e388cdbff016cfe59e120171808d5af702d7d1e68
  task: semantic_segmentation
  value: 77.3
- axis: G6_compactness
  baseline: null
  baseline_value: 52.6
  dataset: So2Sat
  direction: better
  id: thoreau2025parameter#c2
  label_ratio: null
  locator: Table 2
  metric: f1
  model: scalemae
  span: DEFLECT (ours) 0.2% 53.2 97.8 44.1 77.3 50.6
  span_sha256: 5b1b62db9e7d6b3a2daf726e388cdbff016cfe59e120171808d5af702d7d1e68
  task: land_cover_classification
  value: 53.2
- axis: G5_cost
  baseline: null
  baseline_value: 30.2
  dataset: MADOS
  direction: better
  id: thoreau2025parameter#c3
  label_ratio: null
  locator: Table 4
  metric: miou
  model: scalemae
  span: DEFLECT attains 51.3 mIoU (MADOS) and 77.3 IoU (BurnScars) while tuning only
    0.28% of parameters, compared to 30.2
  span_sha256: 406725880b36d15f369d1fed9480ccc0b93f6c0bb1126280eba3275634bdafbf
  task: semantic_segmentation
  value: 51.3
date: '2025-03-12'
doi: 10.48550/arxiv.2503.09493
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:50:44.635569Z'
key: thoreau2025parameter
limitations:
- compute_cost
- benchmark_narrowness
- spatial_transfer
models:
- scalemae
proposed_tags:
- parameter_efficient_finetuning
- multispectral_adaptation
- embedding_deflection
- untangled_attention
- LoRA
- DINO-MC
- Cross-Scale MAE
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- urban_signal_mapping
title: Parameter-Efficient Adaptation of Geospatial Foundation Models through Embedding
  Deflection
venue: arXiv
---

## summary



## setup



## caveats


