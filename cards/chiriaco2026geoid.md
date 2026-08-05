---
arxiv_id: '2608.02315'
authors:
- Gaetano Chiriaco
- Luca Barco
- Andrea Bragagnolo
- Claudio Rossi
- Edoardo Arnaudo
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G5_cost
- G6_compactness
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.874
  dataset: Earth Surface Water (ESW)
  direction: better
  id: chiriaco2026geoid#c1
  label_ratio: null
  locator: Table 6
  metric: f1
  model: alphaearth
  span: JRC-GSW achieves F1 = 0.874 without any training on the ESW dataset
  span_sha256: cc248c00fd889dc01f76d49afec6c0f631bc9cdab19d15d50d571ed8e07d3bd0
  task: semantic_segmentation
  value: 0.963
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.773
  dataset: Earth Surface Water (ESW)
  direction: better
  id: chiriaco2026geoid#c2
  label_ratio: null
  locator: Table 6
  metric: f1
  model: tessera
  span: TESSERA MLP 45K 0.911 0.837 0.852 0.980
  span_sha256: 09cbaea33d805d7640ca2e0ada9a6f7b834ce64873d807a0326292e960b8678f
  task: semantic_segmentation
  value: 0.911
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.773
  dataset: Earth Surface Water (ESW)
  direction: better
  id: chiriaco2026geoid#c3
  label_ratio: null
  locator: Sec 0.B.3
  metric: f1
  model: alphaearth
  span: the linear probes reach 0.883 F1 for AEF and 0.902 F1 for TESSERA
  span_sha256: f0052f5a29133cf8f8406c0005bd465966f779f09e7545ac7ff1f7c9435db39f
  task: semantic_segmentation
  value: 0.883
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.873
  dataset: GEOID-Flood
  direction: parity
  id: chiriaco2026geoid#c4
  label_ratio: null
  locator: Table 2
  metric: miou
  model: dofa
  span: DOFA-B 126.92 0.929 0.873 0.975 0.833 0.477 0.761 0.847
  span_sha256: 3d13276228bbbb8023f460e9d93316536f1d850c6b5d610f69ff1305e2b87b6e
  task: flood_mapping
  value: 0.873
date: '2026-08-03'
doi: 10.48550/arxiv.2608.02315
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-05T00:19:38.664286Z'
key: chiriaco2026geoid
limitations:
- benchmark_narrowness
- data_bias
- mixed_pixels
models:
- dofa
- alphaearth
- tessera
proposed_tags:
- permanent_water_layer
- flood_vs_permanent_water_separation
- SAR_optical_fusion
- CEMS_activations
- annual_geospatial_embeddings
regions:
- global
self_evaluation: false
tasks:
- flood_mapping
- semantic_segmentation
- change_detection
title: 'GEOID-Flood: A Large-Scale Multi-Modal Benchmark Dataset for Flood Segmentation'
venue: arXiv
---

## summary

The paper introduces GEOID-Flood, a large multi-modal flood segmentation benchmark built from CEMS activations, and benchmarks geospatial foundation models (including DOFA) against conventional encoders across single-image, paired, and fusion training scenarios. It finds foundation models offer only a modest edge over ImageNet-pretrained backbones, optical-SAR fusion with finetuning best resolves transient flooding, and training on GEOID-Flood transfers better to unseen events than existing benchmarks. AlphaEarth Foundations and TESSERA annual embeddings are also used/evaluated separately to derive a dedicated permanent water layer.

## setup

GEOID-Flood pairs bi-temporal Sentinel-1 (GRD/RTC), pre-event Sentinel-2 composites, and DEM over 14,282 tiles from 219 CEMS flood events across 65 countries (2016-2026), with event-level train/val/test splits and a temporally disjoint 2026 held-out set. Models (TerraMind, DOFA, OlmoEarth, SSL4EO, Satlas, and ImageNet-pretrained CNN/transformer backbones) are trained with a shared U-Net decoder under frozen and finetuned regimes for binary and three-class (background/permanent water/flooded water) segmentation; a separate AlphaEarth/TESSERA-based model is trained on the Earth Surface Water dataset to generate the permanent water layer.

## caveats

The authors note coverage is geographically skewed toward Europe (140 of 219 events), labels inherit residual noise from CEMS delineations and the DL-derived permanent-water layer, flooded water remains the hardest and rarest class throughout, and the cross-dataset comparison is scored against GEOID-Flood's own labels so its claims are anchored on binary water delineation where source conventions converge.
