---
arxiv_id: '2608.29553'
authors:
- Hao Tian
- Heng Cai
- Yifan Yang
axes:
- G1_label_rich_parity
- G10_human_semantics
- G11_complementarity
claims:
- axis: G11_complementarity
  baseline: null
  baseline_value: 0.379
  dataset: Median household income
  direction: better
  id: tian2026beacon#c1
  label_ratio: null
  locator: Sec 3.2
  metric: r2
  model: alphaearth
  span: R2R^{2} improves from 0.379 to 0.463 for median household income
  span_sha256: e32a74a761f8168194f98524333283914eac456f603ed01bd45a3af59e19c90b
  task: socioeconomic_estimation
  value: 0.463
- axis: G11_complementarity
  baseline: null
  baseline_value: 0.431
  dataset: Obesity prevalence
  direction: better
  id: tian2026beacon#c2
  label_ratio: null
  locator: Sec 3.2
  metric: r2
  model: alphaearth
  span: from 0.431 to 0.614 for obesity prevalence (+43%)
  span_sha256: 34551977838d36031f1f87925674ee11d32b9be372b76493267553828d4b0b6b
  task: socioeconomic_estimation
  value: 0.614
- axis: G11_complementarity
  baseline: null
  baseline_value: 0.393
  dataset: Poor mental health
  direction: better
  id: tian2026beacon#c3
  label_ratio: null
  locator: Sec 3.2
  metric: r2
  model: alphaearth
  span: from 0.393 to 0.528 for poor mental health (+34%)
  span_sha256: 462fb03713428d6e2a3705c1dee7381f1f5b1eef23cd17dcdc4b3612e9c9ecea
  task: socioeconomic_estimation
  value: 0.528
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 0.567
  dataset: Land cover (15 classes)
  direction: better
  id: tian2026beacon#c4
  label_ratio: null
  locator: Table 3
  metric: f1
  model: alphaearth
  span: AlphaEarth achieves the highest Macro-F1 (0.584), with BEACON second (0.567)
  span_sha256: b23b178b21bc180a7f6f996fac9c4fee01ece167b52e5a7656a034ba6eee0256
  task: land_cover_classification
  value: 0.584
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 0.845
  dataset: PM2.5
  direction: parity
  id: tian2026beacon#c5
  label_ratio: null
  locator: Sec 3.2
  metric: r2
  model: alphaearth
  span: PM2.5 improves only marginally from 0.845 to 0.856 (+1.3%)
  span_sha256: 137ffb9a346d977022dcba4c060c4f47938713b343b7dc734536269aaf6d8a51
  task: urban_signal_mapping
  value: 0.856
date: '2026-08-30'
doi: 10.1145/3841645.3843383
doi_status: unresolved
extractor_version: '1'
ingested_at: '2026-09-17T00:07:47.014825Z'
key: tian2026beacon
limitations:
- human_semantics
- benchmark_narrowness
- data_bias
models:
- alphaearth
- satclip
- clay
- tessera
proposed_tags:
- POI_semantics
- mobility_patterns
- tri_modal_contrastive_learning
- obesity_prevalence
- mental_health_prediction
regions:
- us
self_evaluation: false
tasks:
- socioeconomic_estimation
- population_density
- land_cover_classification
- urban_signal_mapping
- representation_probing
title: 'BEACON: Behavioral and Semantic Enrichment of AlphaEarth Embeddings through
  Tri-Modal Contrastive Learning'
venue: arXiv
---

## summary

BEACON augments frozen AlphaEarth embeddings with POI text and hourly mobility signals via tri-modal contrastive learning, producing an image-only representation that better captures human-centered urban semantics. Evaluated on nine Houston-area downstream tasks, BEACON substantially improves R2 for socioeconomic/health targets (income, obesity, mental health) over AlphaEarth while remaining near-parity on physical/environmental tasks like LST and PM2.5, and on land-cover classification AlphaEarth still edges out BEACON.

## setup

Study area is the Houston-Woodlands-Sugar Land MSA (2024 data); POIs are anchors aligning AlphaEarth embeddings, POI text descriptions, and 184-dim hourly/monthly mobility profiles via a symmetric CLIP-style InfoNCE loss. Downstream evaluation uses frozen linear/MLP probes over five seeds on nine tasks (7 regression, 2 classification) against six baselines (coordinates, Space2Vec, SatCLIP, TESSERA, Clay, AlphaEarth).

## caveats

Authors note the mobility supervision dominates alignment, human-target gains are strongest under linear probes suggesting improved linear decodability rather than new information, and physical/environmental performance is largely unchanged, indicating the approach primarily surfaces already-latent human signal rather than fundamentally altering physical representations; generality across cities, time periods, and mobility data sources remains untested.
