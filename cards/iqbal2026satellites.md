---
arxiv_id: '2609.00661'
authors:
- Ashiq Shukoor Iqbal
- Wilson Wongso
- Flora D. Salim
axes:
- G3_spatial_transfer
- G5_cost
- G6_compactness
- G2_label_scarce_efficiency
- G10_human_semantics
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.32
  dataset: LODES US counties
  direction: better
  id: iqbal2026satellites#c1
  label_ratio: null
  locator: Sec 5.3
  metric: accuracy
  model: alphaearth
  span: classical Gravity models report CPC ≈0.32\approx 0.32 on comparable US commuting
    data
  span_sha256: ebdd53d71df73c77052117cc8ed946d347e695b221403a3981bac31a27478380
  task: representation_probing
  value: 0.602
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: UK Local Authority Districts
  direction: better
  id: iqbal2026satellites#c2
  label_ratio: null
  locator: Sec 5.2
  metric: accuracy
  model: alphaearth
  span: AlphaEarth reaches 0.515±0.0150.515\pm 0.015 and SatCLIP 0.513±0.0340.513\pm
    0.034
  span_sha256: 9265711d642e58af3748cb1c902fc074e5ec1527baeb0291a27576c8ec46d053
  task: representation_probing
  value: 0.515
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: UK Local Authority Districts
  direction: parity
  id: iqbal2026satellites#c3
  label_ratio: null
  locator: Sec 5.2
  metric: accuracy
  model: satclip
  span: AlphaEarth reaches 0.515±0.0150.515\pm 0.015 and SatCLIP 0.513±0.0340.513\pm
    0.034
  span_sha256: 9265711d642e58af3748cb1c902fc074e5ec1527baeb0291a27576c8ec46d053
  task: representation_probing
  value: 0.513
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: 14 Global cities
  direction: worse
  id: iqbal2026satellites#c4
  label_ratio: null
  locator: Sec 5.3
  metric: accuracy
  model: alphaearth
  span: AlphaEarth (0.111±0.0170.111\pm 0.017) and SatCLIP (0.104±0.0240.104\pm 0.024)
    following in close proximity
  span_sha256: 48f85078a24b575301e4f24538f26afd596651d9b16a0e23712212523536ebb6
  task: representation_probing
  value: 0.111
- axis: G8_uncertainty
  baseline: null
  baseline_value: 0.515
  dataset: UK Local Authority Districts
  direction: worse
  id: iqbal2026satellites#c5
  label_ratio: null
  locator: Sec 5.4
  metric: accuracy
  model: alphaearth
  span: its UK CPC falls from 0.515 at η=0\eta=0 to 0.249 at η=1\eta=1
  span_sha256: 19dc61dfd23198ef07f2d7da4ea0b1107362981d9c59e2740a448c776dcf67b1
  task: representation_probing
  value: 0.249
date: '2026-09-01'
doi: 10.48550/arxiv.2609.00661
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-17T00:07:22.442680Z'
key: iqbal2026satellites
limitations:
- spatial_transfer
- temporal_transfer
- benchmark_narrowness
- compute_cost
- time_sensitivity
models:
- satclip
- alphaearth
proposed_tags:
- origin_destination_generation
- graph_diffusion
- remoteclip
- dinov3
- commuting_flow_prediction
- census_noise_parameter
regions:
- us
- gb
- cn
- fr
- br
- sn
- au
- jp
- global
self_evaluation: false
tasks:
- representation_probing
title: Do Satellites See Commuters? A Critical Benchmark of Vision Foundation Models
venue: arXiv
---

## summary



## setup



## caveats


