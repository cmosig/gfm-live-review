---
arxiv_id: '2509.03816'
authors:
- Aman Gupta
- Aditi Sheshadri
- Sujit Roy
- Johannes Schmude
- Vishal Gaur
- Wei Ji Leong
- Manil Maskey
- Rahul Ramachandran
axes:
- G2_label_scarce_efficiency
- G11_complementarity
- G3_spatial_transfer
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.116
  dataset: ERA5 gravity wave flux (daily-sampled)
  direction: better
  id: gupta2025finetuning#c1
  label_ratio: null
  locator: Sec 3.3
  metric: rmse
  model: prithvi
  span: daily sampled flux distributions from both attn unet and the fine-tuned models
    produce higher Hellinger distances of 0.116 and 0.062
  span_sha256: 50db0257361144b34048431e597848c693bd36b3341bb7deecf67ff54e62edb5
  task: representation_probing
  value: 0.062
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.005
  dataset: ERA5 gravity wave flux (monthly-averaged)
  direction: better
  id: gupta2025finetuning#c2
  label_ratio: null
  locator: Sec 3.3
  metric: rmse
  model: prithvi
  span: baseline and the fine-tuned model have a Hellinger distance of 0.005 and 0.003
    from the underlying training
  span_sha256: dcf50fb14fac2b2a052b40b06cc71f88451be15b82edfbbab1a464a62ada13a4
  task: representation_probing
  value: 0.003
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.84
  dataset: ERA5 GW flux, Drake Passage
  direction: better
  id: gupta2025finetuning#c3
  label_ratio: null
  locator: Sec 3.1
  metric: r2
  model: prithvi
  span: the Pearson correlation coefficients of the predictions from the fine-tuned
    model (vs. ERA5) are as high as 0.99 and 0.97
  span_sha256: 46c62c7c515a54ee2bd1e5ec71e4c31159d0657f77cba10b208ecbbecf1a7606
  task: representation_probing
  value: 0.99
date: '2025-09-04'
doi: 10.48550/arxiv.2509.03816
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:46:32.446287Z'
key: gupta2025finetuning
limitations:
- benchmark_narrowness
- data_bias
- spatial_transfer
- interpretability
models:
- prithvi
proposed_tags:
- gravity_wave_flux_parameterization
- climate_model_subgrid_scale
- prithvi_wxc
- atmospheric_science
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: 'Finetuning AI Foundation Models to Develop Subgrid-Scale Parameterizations:
  A Case Study on Atmospheric Gravity Waves'
venue: arXiv
---

## summary



## setup



## caveats


