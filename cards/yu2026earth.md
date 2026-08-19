---
arxiv_id: '2608.15282'
authors:
- Yi Yu
- Jian Peng
- Yucheng Lin
- Trevor F. Keenan
- Thomas F. A. Bishop
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G7_interpretability
- G8_uncertainty
- G9_ecological_fine_scale
claims:
- axis: G2_label_scarce_efficiency
  baseline: null
  baseline_value: null
  dataset: OpenET
  direction: better
  id: yu2026earth#c1
  label_ratio: null
  locator: Sec IV-C3
  metric: r2
  model: alphaearth
  span: AlphaEarth also achieved R2=0.58±0.01R^{2}=0.58\pm 0.01 for monthly OpenET
    labels
  span_sha256: 8382f1b7580fb9de16228572cffe11e8cb158aca7703becf10941308dd201d92
  task: hydrological_modeling
  value: 0.58
- axis: G9_ecological_fine_scale
  baseline: null
  baseline_value: null
  dataset: FLUXNET urban ET
  direction: better
  id: yu2026earth#c2
  label_ratio: null
  locator: Sec IV-C3
  metric: r2
  model: alphaearth
  span: reaching temporally held-out FLUXNET R2=0.92R^{2}=0.92 and RMSE=0.37=0.37
    mm d-1
  span_sha256: 033a096fcb389671e50dcf6b2c82d295c72cd68c04c002d7910f289efdcf2fa7
  task: hydrological_modeling
  value: 0.92
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.514
  dataset: SM (Sentinel-1/2/ERA5, pan-European)
  direction: parity
  id: yu2026earth#c3
  label_ratio: null
  locator: Sec IV-B2
  metric: r2
  model: prithvi
  span: found almost no incremental benefit from Prithvi features over handcrafted
    predictors under spatial cross-validation (R2=0.515R^{2}=0.515 versus 0.514)
  span_sha256: e9c9b51ab1d63c89b44ab0f497aac3c2320852b4b2efb647b7694aea69066653
  task: biomass_estimation
  value: 0.515
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.75
  dataset: eddy-covariance NEE-partitioned GPP (37 sites)
  direction: better
  id: yu2026earth#c4
  label_ratio: null
  locator: Sec IV-C4
  metric: r2
  model: prithvi
  span: a fused Prithvi–MERRA-2 model averaged R2=0.81R^{2}=0.81, compared with 0.75
    for a same-input ResNet
  span_sha256: c0e764e2928de12eb0bf52a47fa5367716996a90e8d45586bdf783e05cfb0d3b
  task: crop_yield_estimation
  value: 0.81
date: '2026-08-15'
doi: 10.48550/arxiv.2608.15282
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-19T00:13:59.204101Z'
key: yu2026earth
limitations:
- benchmark_narrowness
- data_bias
- spatial_transfer
- temporal_transfer
- uncertainty
- mixed_pixels
- human_semantics
models:
- alphaearth
- presto
- prithvi
- dofa
- galileo
- scalemae
- clay
- satmae
- tessera
proposed_tags:
- ecohydrology
- observation-to-inference hierarchy
- meta-analysis of EOFMs
- flux-tower evaluation
- AlphaEarth embeddings
regions:
- global
- us
- au
- dk
- cn
- pt
self_evaluation: false
tasks:
- biomass_estimation
- canopy_height_estimation
- crop_type_mapping
- flood_mapping
- hydrological_modeling
- landslide_susceptibility
- land_cover_classification
- socioeconomic_estimation
title: 'Earth Observation Foundation Models for Terrestrial Ecohydrology: From Representation
  Learning to Process Inference'
venue: arXiv
---

## summary

This is a review/meta-analysis of Earth observation foundation models (EOFMs) for terrestrial ecohydrology, not an original model paper; it proposes an observation-to-inference hierarchy and synthesizes evidence from 60 EOFM releases and 71 application studies.

## setup

The authors conducted a systematic literature search (OpenAlex, arXiv, Semantic Scholar, DBLP) yielding 722 screened candidates and 60 eligible EOFM model/version releases plus 71 application records, coded for input pathways, spatiotemporal scale, adaptation routes, and ecohydrological relevance.

## caveats

The authors note that most EOFM evaluations rely on retrieved/model-derived reference products rather than independent field or flux-tower data, evidence weakens with inference depth (T1 to T3), spatial and temporal transfer often degrades performance, and physical consistency and uncertainty quantification remain weakly covered by existing benchmarks.
