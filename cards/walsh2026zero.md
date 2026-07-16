---
arxiv_id: '2605.05405'
authors:
- James Walsh
- William Fawcett
- Grace Colverd
- Raúl Ramos-Pollán
axes:
- G2_label_scarce_efficiency
- G12_openness
- G11_complementarity
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 2.0
  dataset: GeoQuery 76-query disaster retrieval benchmark (UK floods)
  direction: better
  id: walsh2026zero#c1
  label_ratio: null
  locator: Sec 4 / Table 1
  metric: accuracy
  model: clay
  span: UK flood detection was the strongest, with 50% of queries within 50 km and
    70% within 100 km
  span_sha256: 60eb1f5e1856f2395d426c38d57f1b756663c98c9285082d6a1385843f3d5b6b
  task: representation_probing
  value: 50.0
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: GeoQuery 76-query disaster retrieval benchmark (overall)
  direction: better
  id: walsh2026zero#c2
  label_ratio: null
  locator: Abstract / Sec 4
  metric: accuracy
  model: clay
  span: GeoQuery achieves 31.6% accuracy within 50 km, with the strongest performance
    on floods
  span_sha256: dbd8bd388413df83f1b2f4ef7de48bca2875308e7c323d86b2d00e27fc166739
  task: representation_probing
  value: 31.6
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: GeoQuery 76-query disaster retrieval benchmark (US droughts)
  direction: better
  id: walsh2026zero#c3
  label_ratio: null
  locator: Sec 4
  metric: accuracy
  model: clay
  span: Drought detection achieved 25% success within 50 km
  span_sha256: e341ab10fafa243c14732573e2c46056a418f3e20f376da749b459f8e6f02c46
  task: representation_probing
  value: 25.0
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: GeoQuery 76-query disaster retrieval benchmark (US wildfires)
  direction: worse
  id: walsh2026zero#c4
  label_ratio: null
  locator: Sec 4
  metric: accuracy
  model: clay
  span: wildfire detection achieved 0% within 50 km but reached 40% within 100 km
  span_sha256: dbdcd3707122298eee7c86034bf8b072cd988851641dd10c4576cbb6992b0a15
  task: representation_probing
  value: 0.0
date: '2026-05-06'
doi: 10.56272/a2c9ee39
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:09:13.365475Z'
key: walsh2026zero
limitations:
- benchmark_narrowness
- time_sensitivity
- data_bias
models:
- clay
proposed_tags:
- zero_shot_retrieval
- text_image_alignment
- prompt_optimization
- crisis_response
- geolocation_retrieval
regions:
- global
- gb
- us
- au
self_evaluation: false
tasks:
- representation_probing
- flood_mapping
title: 'Zero-Shot Satellite Image Retrieval through Joint Embeddings: Application
  to Crisis Response'
venue: arXiv
---

## summary

GeoQuery is a zero-shot satellite image retrieval system that aligns frozen CLAY visual embeddings with text embeddings via prompt-optimized descriptions of a 100k proxy tile subset, enabling natural-language search over global Sentinel-2 imagery without contrastive training. Evaluated on 76 disaster queries (UK floods, US wildfires, US droughts), it achieves 31.6% accuracy within 50km overall, with floods performing best. It is deployed within ECHO, an agentic crisis-response system, and was used during Cyclone Alfred's 2025 approach to Brisbane.

## setup

76 disaster-location queries (40 UK flood, 20 US wildfire, 16 US drought) evaluated against real 2024 disaster events using PlaNet-style geolocation accuracy at 50km/100km radius, across four text/image result-count configurations built on frozen CLAY embeddings of Sentinel-2 tiles and Gemini-1.5-generated proxy descriptions.

## caveats

Authors note the two-stage proxy search is suboptimal indirect alignment rather than true contrastive training; wildfire detection fails due to temporally ephemeral, spectrally subtle burn scars without near-infrared bands; performance shows urban-vs-rural bias (65% vs 35%); results depend on proxy subset size and text/image configuration balance; benchmark is limited to three disaster types in UK/US regions.
