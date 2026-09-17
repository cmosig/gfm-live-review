---
arxiv_id: '2608.25858'
authors:
- Victor Nascimento Ribeiro
- Jorge Guevara
- Jorge Sebastian Moraga
- Chris Lucas
- Natalie Lord
- Andrew Taylor
- Edward Lockhart
- Will Trojak
- Johannes Schmude
- Anne Jones
axes:
- G2_label_scarce_efficiency
- G5_cost
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 5.934
  dataset: ERA5-Land Colorado River Basin
  direction: worse
  id: ribeiro2026precipitation#c1
  label_ratio: null
  locator: Table 2
  metric: rmse
  model: prithvi
  span: the CC model achieves the lowest raw CRPS (0.511) and MSE (4.282)
  span_sha256: d32d48c02d064d3bb9f5190ade3f461e9626d3368d7318c0ec547122d33a682d
  task: hydrological_modeling
  value: 4.282
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 7.522
  dataset: ERA5-Land Colorado River Basin annual maxima
  direction: better
  id: ribeiro2026precipitation#c2
  label_ratio: null
  locator: Table 4
  metric: rmse
  model: prithvi
  span: CA-PWC achieves both the lowest CRPS (5.730) and the lowest distribution bias
    (0.062)
  span_sha256: fbbd2e8b5894e58cad6ad6cead6a043c9a01edf0c6d7ce98716caced9e7aa8c0
  task: hydrological_modeling
  value: 5.73
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 5.94
  dataset: ERA5-Land Colorado River Basin
  direction: better
  id: ribeiro2026precipitation#c3
  label_ratio: 1.0
  locator: Sec 4.2
  metric: rmse
  model: prithvi
  span: Prithvi WxC falls below the Concatenation threshold (5.94) already at 10 years
    and reaches 5.23 at 25 years
  span_sha256: ea58f3074d1ccb947c2eb726e87dd89c0cd2904d8d1fcbe0a3658da0f29e22b6
  task: hydrological_modeling
  value: 5.23
date: '2026-08-26'
doi: 10.48550/arxiv.2608.25858
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-17T00:10:29.350551Z'
key: ribeiro2026precipitation
limitations:
- compute_cost
- benchmark_narrowness
- uncertainty
- spatial_transfer
- temporal_transfer
models:
- prithvi
proposed_tags:
- precipitation_downscaling
- diffusion_model
- conditioning_mechanism
- extreme_event_representation
regions:
- us
self_evaluation: false
tasks: []
title: Precipitation Downscaling Using Foundation Model-Conditioned Diffusion
venue: arXiv
---

## summary

This paper compares three conditioning strategies—channel concatenation, cross-attention with a learned convolutional encoder, and cross-attention with the frozen Prithvi WxC weather foundation model encoder—for diffusion-based daily precipitation downscaling over the Colorado River Basin. Concatenation achieves the lowest pointwise CRPS/MSE but oversmooths extremes, while cross-attention conditioning (especially with Prithvi WxC) improves distributional realism, spectral fidelity, and extreme-event representation, and shows better data efficiency with limited training years. The authors are not the original Prithvi WxC creators but reuse its frozen pretrained encoder as a conditioning module.

## setup

A UNet-based EDM diffusion model is trained to downscale ERA5 0.25° atmospheric/static predictors to ERA5-Land 0.1° daily precipitation over the Colorado River Basin (1985-2009 train, 2010-2012 val, 2013-2015 test), evaluated with CRPS, MSE, bias, distribution bias, RAPSD/RALSD, FSS, and extreme-event frequency ratios across four conditioning variants (unconditioned, concatenation, conv-encoder cross-attention, Prithvi-WxC cross-attention).

## caveats

Authors note the study covers only a single domain and variable, relies on ERA5 reanalysis that may not generalize to GCM projections, uses a short 3-year test period making extreme-event statistics (especially annual maxima) highly uncertain, and leaves open whether fine-tuning the frozen foundation model backbone or using more training data for concatenation could narrow observed gaps.
