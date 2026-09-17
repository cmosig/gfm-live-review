---
arxiv_id: '2608.26088'
authors:
- Evelyn Ma
- Rama Kumar Pasumarthi
- Kishwar Shafin
- Mandar Sharma
- Mimi Sun
- Hamed Sadeghi
- Dav M. Ebengo
- Mbulayi Onesime
- Rouslan Solomakhin
- John Wamburu
- William Ogallo
- Aisha Walcott-Bryant
- Sanxing Chen
- Arbaaz Muslim
- Yael Mayer
- Ronald Ho
- Roy Lee
- Ruth Alcantara
- Abdoulaye Diack
- Monica Bharel
- Lambert Rosique
- Jeremy Amez-Droz
- Christopher Haire
- James Manyika
- Yossi Matias
- Niv Efron
- Gautam Prasad
- Shravya Shetty
axes:
- G11_complementarity
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 60.0
  dataset: CDC Health Variables
  direction: better
  id: ma2026planetary#c1
  label_ratio: null
  locator: Table 5
  metric: r2
  model: alphaearth
  span: PPE’s intelligent data selection and multimodal fusion drive mean R2R^{2}
    to 76.8%
  span_sha256: 1ca84776d6f49e5850c3a94353801a4e761b0ae51b713b2a31a04aab8d86aad8
  task: socioeconomic_estimation
  value: 76.8
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 59.9
  dataset: FEMA National Risk Index
  direction: better
  id: ma2026planetary#c2
  label_ratio: null
  locator: Sec 2.4.2
  metric: r2
  model: alphaearth
  span: the performance further scales to a nationwide mean R2R^{2} of 64.9%64.9\%
    from 59.9%59.9\% mean from the hand-curated model
  span_sha256: 0404d377217c61c30ad6d125436956d21e35d50d9afd1803619de50399f5aca3
  task: socioeconomic_estimation
  value: 64.9
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 58.6
  dataset: Social Vulnerability Index (spatial regression)
  direction: better
  id: ma2026planetary#c3
  label_ratio: null
  locator: Abstract/Table 7
  metric: r2
  model: alphaearth
  span: the Social Vulnerability Index (66.2% vs. 58.6%)
  span_sha256: 649c86327e0d6b0bfd85f0a0a75ed181698edac015da550647cde6eabd43e9aa
  task: socioeconomic_estimation
  value: 66.2
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 31.5
  dataset: Nigeria FCG Insecurity
  direction: better
  id: ma2026planetary#c4
  label_ratio: null
  locator: Table 3
  metric: r2
  model: alphaearth
  span: the complete Planetary Prediction Engine achieves an R2R^{2} of 66.1%, doubling
    the baseline accuracy
  span_sha256: 5873bc02c6140c39209e7f591bf6b8d31b3bc3dd4cf3737f78303c0b25e7663c
  task: poverty_mapping
  value: 66.1
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 11.0
  dataset: US SVI (county to ZCTA)
  direction: better
  id: ma2026planetary#c5
  label_ratio: null
  locator: Table 4
  metric: r2
  model: alphaearth
  span: drives the overall R2R^{2} to 37.6%
  span_sha256: ae5576c309c9748d1898fa6e80a4b30eb84db9568753134fabb3828f4168199a
  task: socioeconomic_estimation
  value: 37.6
date: '2026-08-26'
doi: 10.48550/arxiv.2608.26088
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-17T00:08:13.441698Z'
key: ma2026planetary
limitations:
- benchmark_narrowness
- spatial_transfer
- mixed_pixels
models: []
proposed_tags:
- epidemiological_nowcasting
- spatial_regression
- super_resolution_downscaling
- autonomous_agent_pipeline
- PDFM
- intelligent_data_selection
regions:
- us
- ng
- cd
- global
self_evaluation: false
tasks:
- poverty_mapping
- socioeconomic_estimation
title: 'Planetary Prediction Engine: Autonomous Geospatial Prediction via Intelligent
  Data Selection and Foundation Model Embeddings'
venue: arXiv
---

## summary

This paper introduces the Planetary Prediction Engine (PPE), an autonomous LLM-orchestrated agent that discovers, curates, and fuses multimodal geospatial data (including PDFM and AlphaEarth foundation model embeddings) to build predictive models from natural-language queries. PPE is evaluated on epidemiological nowcasting, spatial super-resolution downscaling, and spatial regression tasks across the US, Nigeria, and DRC, consistently outperforming manual expert baselines.

## setup

Benchmarks include 21 CDC health indicators and FEMA National Risk Index at census-tract level, SVI at county/ZCTA level, Nigeria Food Consumption Group downscaling from ADM1 to ADM2, and DRC Ebola outbreak hotspot prediction across 519 health zones, using ablation tiers comparing raw covariates, PDFM/AlphaEarth embeddings, and the full autonomous pipeline.

## caveats

The authors note a noise-resolution trade-off where adding high-resolution AlphaEarth features to the PDFM+covariate stack degrades performance on SVI super-resolution downscaling (R2 40.1% vs 52.0%), and flag that performance in geophysical/hydrological FEMA risk categories lags behind other categories.
