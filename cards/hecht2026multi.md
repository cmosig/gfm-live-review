---
arxiv_id: '2606.20167'
authors:
- Jonathan Hecht
- Lukas Arzoumanidis
- Ziyue Li
- Youness Dehbi
axes:
- G2_label_scarce_efficiency
- G6_compactness
- G11_complementarity
claims:
- axis: G2_label_scarce_efficiency
  baseline: geoclip
  baseline_value: 53.8
  dataset: GADM country codes
  direction: better
  id: hecht2026multi#c1
  label_ratio: null
  locator: Table I
  metric: accuracy
  model: satclip
  span: SatCLIP-Org
  span_sha256: 9d24cb156c7b2b556238776317e0adc335fe633021d37347b569d1ceb0b77297
  task: representation_probing
  value: 65.4
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.3
  dataset: GPW v4 population density
  direction: better
  id: hecht2026multi#c2
  label_ratio: null
  locator: Table I
  metric: r2
  model: satclip
  span: Mosaiks
  span_sha256: c8fce45185c10da7f618972b527adee1200080254aae4fa3b9db84c801309ac9
  task: representation_probing
  value: 0.47
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 53.0
  dataset: Terrestrial ecoregions (biomes)
  direction: better
  id: hecht2026multi#c3
  label_ratio: null
  locator: Table I
  metric: accuracy
  model: satclip
  span: Mosaiks
  span_sha256: c8fce45185c10da7f618972b527adee1200080254aae4fa3b9db84c801309ac9
  task: representation_probing
  value: 66.8
date: '2026-06-18'
doi: 10.48550/arxiv.2606.20167
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T19:06:25.620279Z'
key: hecht2026multi
limitations:
- benchmark_narrowness
- compute_cost
- interpretability
models:
- satclip
- geoclip
proposed_tags:
- location_encoder
- multimodal_contrastive_learning
- elevation_regression
- population_density_regression
- country_classification
- biome_classification
- melt
- salt
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: Multi-Modal Contrastive Learning for Implicit Earth Embeddings via Location
  Tying
venue: arXiv
---

## summary

The paper proposes melt and salt, two multimodal contrastive learning architectures that use geographic location as a shared anchor to align a location encoder with multiple unpaired non-location modalities (satellite imagery, natural images, text). Both approaches match the strongest two-modality baseline (SatCLIP) across four downstream tasks, but adding modalities or pre-training volume does not consistently improve performance, indicating the location encoder itself is the performance bottleneck.

## setup

Location encoder (spherical harmonics + SIREN MLP) pre-trained via NT-Xent contrastive loss against frozen encoders for Sentinel-2 imagery (S2-100K), Flickr images (MP-16/YFCC100M), and geotagged Wikipedia text, then evaluated on frozen-embedding downstream MLP probes for elevation, population density, country classification, and biome classification across varying label amounts (243 to 100,000 samples).

## caveats

Authors note a fixed one-size-fits-all hyperparameter strategy across variants, testing only a single location encoder architecture, evaluation restricted to four global tasks without geographically stratified or few-shot settings, and reliance on the NT-Xent objective which may induce a low-complexity alignment task unsuited to capturing modality-specific information.
