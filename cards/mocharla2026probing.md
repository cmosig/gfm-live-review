---
arxiv_id: '2607.05207'
authors:
- Rohita Mocharla
- Vishal M. Patel
axes:
- G7_interpretability
- G8_uncertainty
- G6_compactness
claims:
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: SSL4EO ERA5 extension
  direction: parity
  id: mocharla2026probing#c1
  label_ratio: null
  locator: Table 2
  metric: r2
  model: croma
  span: 'CROMA [6]


    0.49


    0.49'
  span_sha256: 317e55de0e7bccaeef7f6de859a29763e09031f1fd282d668c72d72a28619112
  task: representation_probing
  value: 0.49
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: SSL4EO ERA5 extension
  direction: parity
  id: mocharla2026probing#c2
  label_ratio: null
  locator: Table 2
  metric: r2
  model: dofa
  span: 'DOFA [37]


    0.35


    0.39'
  span_sha256: 079e6d77f0bdf1544e1c642f1f57a722a0ad63f4b63ba21a2056a6d72b618dad
  task: representation_probing
  value: 0.35
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: SSL4EO ERA5 extension
  direction: parity
  id: mocharla2026probing#c3
  label_ratio: null
  locator: Table 2
  metric: r2
  model: prithvi
  span: 'PrithviV1 100M [15]


    0.36


    0.39'
  span_sha256: d2bbbd599c1a50e6a0c0700fbbadb4fa02b14c669c3fcf7b203e877da8c1b162
  task: representation_probing
  value: 0.36
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: SSL4EO ERA5 extension
  direction: parity
  id: mocharla2026probing#c4
  label_ratio: null
  locator: Table 2
  metric: r2
  model: scalemae
  span: 'ScaleMAE [27]


    -0.44


    -0.17'
  span_sha256: 022eccb590a4f192ce47197723d7e625d704e81ddc425b7677e97e1a72f5b28d
  task: representation_probing
  value: -0.44
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: SSL4EO ERA5 extension
  direction: parity
  id: mocharla2026probing#c5
  label_ratio: null
  locator: Table 2
  metric: r2
  model: prithvi
  span: 'PrithviV2 300M [31]


    0.38


    0.62'
  span_sha256: fa36c61d30102008c98f684a4b326467a2f868f05ad91c2c69bfbf507952f5c4
  task: representation_probing
  value: 0.38
date: '2026-07-06'
doi: 10.48550/arxiv.2607.05207
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:34:12.363387Z'
key: mocharla2026probing
limitations:
- interpretability
- benchmark_narrowness
- uncertainty
models:
- croma
- dofa
- scalemae
- prithvi
proposed_tags:
- ERA5_probing
- representation_geometry
- effective_rank
- uniformity
- seasonal_alignment
- off_diagonal_covariance
- SSL4EO
- PANGAEA_domain_breakdown
- probe_selectivity
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: Probing Geospatial SSL Representations with Environmental Signals
venue: arXiv
---

## summary

The paper introduces a representation-level evaluation protocol for geospatial SSL models that probes learned embeddings against co-located ERA5 environmental variables and complements this with intrinsic diagnostics (effective rank, uniformity, seasonal alignment, off-diagonal covariance). Applying this to SSL4EO control models (DINO, MAE, MoCo) and several public geospatial foundation models, they find models with similar downstream PANGAEA performance encode very different amounts of environmental signal, and that linear ERA5 decodability correlates with performance on agriculture and disaster tasks. Uniformity is the intrinsic metric most associated with environmental signal encoding and agriculture task performance, while other metrics show weak association with out-of-distribution robustness on EarthShift.

## setup

Authors extend SSL4EO-S12 with co-located ERA5 reanalysis variables (temperature, precipitation, solar radiation, surface pressure, soil water) and train ridge regression and MLP probes on frozen embeddings from a 50K spatially-balanced training subset, evaluating on the held-out SSL4EO validation split. They evaluate SSL4EO-trained DINO/MAE/MoCo ViT-S/16 controls plus public foundation models (CROMA, DOFA, PrithviV1/V2, ScaleMAE, RemoteCLIP, DINOv3 Sat, TerraMind) using Sentinel-2-only inputs, and relate probe R2 and intrinsic metrics to PANGAEA downstream task performance and EarthShift OOD robustness.

## caveats

Authors note the analysis is associative rather than causal, that foundation models differ in architecture/parameters/pretraining data so differences cannot be attributed to individual design choices, and that the OOD robustness analysis uses only 5 models, limiting the strength of conclusions.
