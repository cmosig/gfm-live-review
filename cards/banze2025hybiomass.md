---
arxiv_id: '2506.11314'
authors:
- Aaron Banze
- Timothée Stassin
- Nassim Ait Ali Braham
- Rıdvan Salih Kuzu
- Simon Besnard
- Michael Schmitt
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.41
  dataset: HyBiomass (North America)
  direction: worse
  id: banze2025hybiomass#c1
  label_ratio: null
  locator: Table I
  metric: r2
  model: dofa
  span: North America 90.62 ± 0.88 0.41 ± 0.01
  span_sha256: 2df23bf99f9457db0394a0fa5aba608b6a49fc716f48f103443cf293fd568d63
  task: biomass_estimation
  value: 0.33
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.56
  dataset: HyBiomass (Africa)
  direction: worse
  id: banze2025hybiomass#c2
  label_ratio: null
  locator: Table I
  metric: r2
  model: dofa
  span: Africa 65.65 ± 2.55 0.56 ± 0.03
  span_sha256: 495abb7338763998f4d35e6d2b8415eb4c8ff7cdd621dc454dd8ec38ecaf7838
  task: biomass_estimation
  value: 0.54
date: '2025-06-12'
doi: 10.48550/arxiv.2506.11314
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:47:45.182655Z'
key: banze2025hybiomass
limitations:
- benchmark_narrowness
- data_bias
- mixed_pixels
- spatial_transfer
models:
- dofa
proposed_tags:
- hyperspectral_imagery
- EnMAP
- GEDI
- token_patch_size
- SpectralEarth
- Panopticon
- Spectral-ResNet-50
- Spectral-ViT-B
regions:
- global
self_evaluation: false
tasks:
- biomass_estimation
title: 'HyBiomass: Global Hyperspectral Imagery Benchmark Dataset for Evaluating Geospatial
  Foundation Models in Forest Aboveground Biomass Estimation'
venue: arXiv
---

## summary

The paper introduces HyBiomass, a globally distributed benchmark dataset combining co-located EnMAP hyperspectral imagery and GEDI-derived aboveground biomass density labels across seven continental regions, for pixel-wise regression benchmarking of Geo-FMs. It benchmarks DOFA alongside SpectralEarth's Spectral-ResNet-50/Spectral-ViT-B, Panopticon, and a supervised U-Net baseline under frozen and fine-tuned encoder settings. Results show Geo-FMs can match or surpass the U-Net especially when fine-tuned, and highlight ViT token patch size as a key factor for pixel-wise regression accuracy.

## setup

EnMAP hyperspectral tiles (202 spectral bands after removing water-vapor-affected bands) are co-located with GEDI-derived AGBD estimates (quality-filtered per Burns et al. protocol, restricted to forest PFTs) into non-overlapping 128x128 px patches across seven continental regions. Models are evaluated with frozen and fully fine-tuned encoders using a UPerNet decoder, trained with 5 random 70:20:10 splits per region, reporting RMSE and R2.

## caveats

The authors note that varying ViT token patch sizes across models hinder direct comparison of HSI-handling approaches since patch size strongly affects performance; performance varies substantially by region depending on dataset size (e.g., Africa's small dataset shows a larger U-Net/Geo-FM gap) and label/AGBD estimate accuracy; and models systematically overestimate low AGB and underestimate high AGB due to signal saturation.
