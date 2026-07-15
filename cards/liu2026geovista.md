---
arxiv_id: '2605.14406'
authors:
- Yuhao Liu
- Sadeer Al-Kindi
- Ashok Veeraraghavan
- Guha Balakrishnan
axes:
- G11_complementarity
- G1_label_rich_parity
- G3_spatial_transfer
- G9_ecological_fine_scale
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.569
  dataset: CDC WONDER mortality (All causes, Washington held-out)
  direction: better
  id: liu2026geovista#c1
  label_ratio: null
  locator: Table 2
  metric: r2
  model: alphaearth
  span: Results demonstrate that GeoViSTA yields superior zero-shot downstream metric
    performance
  span_sha256: b9e63f77f309f8a88862a7f7e9982011aa3ff2e508e56a10e433074081cbc773
  task: socioeconomic_estimation
  value: 0.611
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.671
  dataset: FireCCI51 (Ndays)
  direction: better
  id: liu2026geovista#c2
  label_ratio: null
  locator: Table 3
  metric: r2
  model: alphaearth
  span: GeoViSTA outperforms baselines on Ndays
  span_sha256: 5e6c1e13b2c0154fd6207079610f1c12a33bc3c6161d132e9936eb3dd1e474a2
  task: socioeconomic_estimation
  value: 0.792
date: '2026-05-14'
doi: 10.48550/arxiv.2605.14406
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:37:01.680217Z'
key: liu2026geovista
limitations:
- benchmark_narrowness
- mixed_pixels
- spatial_transfer
models:
- alphaearth
proposed_tags:
- vision_tabular_fusion
- mortality_prediction
- fire_hazard_prediction
- climate_vulnerability_index
- masked_autoencoding
- cross_attention
regions:
- us
self_evaluation: false
tasks:
- socioeconomic_estimation
- representation_probing
title: 'GeoViSTA: Geospatial Vision-Tabular Transformer for Multimodal Environment
  Representation'
venue: arXiv
---

## summary



## setup



## caveats


