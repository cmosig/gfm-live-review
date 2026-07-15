---
arxiv_id: '2604.21104'
authors:
- Amandeep Kaur
- Mirali Purohit
- Gedeon Muhawenayo
- Esther Rolf
- Hannah Kerner
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G12_openness
claims:
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: 0.23
  dataset: FMoW-Sentinel
  direction: better
  id: kaur2026pretrain#c1
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: satmae
  span: One-hot-Europe improved over Global pretraining by 10% on FMoW (33% vs. 23%)
  span_sha256: 25436d57f60b2c89580a0d22b0f548e3b962bdadbdbd8ee23042b7b9cd339344
  task: representation_probing
  value: 0.33
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: 0.17
  dataset: MOSAIKS Population
  direction: better
  id: kaur2026pretrain#c2
  label_ratio: null
  locator: Table 2
  metric: r2
  model: satmae
  span: 0.06 R² points on MOSAIKS population density estimation (0.23 vs. 0.17)
  span_sha256: bd97e8a45019a69dda5e788fd892dfe4f91c3d69f9a1e921bff5784c96302421
  task: population_density
  value: 0.23
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: 0.35
  dataset: ForTy
  direction: better
  id: kaur2026pretrain#c3
  label_ratio: null
  locator: Table 2
  metric: f1
  model: satmae
  span: 0.02 F1 points on ForTy (0.37 vs. 0.35)
  span_sha256: 022117554e63ddc66df841b23afa1c948e0eb4ba29a9bc6fdc368b5b4c9e07c4
  task: semantic_segmentation
  value: 0.37
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: 0.46
  dataset: GEO-Bench
  direction: better
  id: kaur2026pretrain#c4
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: satmae
  span: 0.05 points on the GEO-Bench aggregate score (0.51 vs. 0.46)
  span_sha256: 53383701062336564b841a2f2e7cae39f003536d6b6f054d5ca5ef4408703480
  task: representation_probing
  value: 0.51
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.12
  dataset: FMoW-Sentinel
  direction: better
  id: kaur2026pretrain#c5
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: satmae
  span: 'One-hot-Europe


    0.33'
  span_sha256: a1f218c7a3c1ad6fc9f2a3854eddf3fcca13b2ba7aa32cbde0ff2e5407982a09
  task: representation_probing
  value: 0.33
date: '2026-04-22'
doi: 10.48550/arxiv.2604.21104
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:38:52.323983Z'
key: kaur2026pretrain
limitations:
- data_bias
- benchmark_narrowness
- compute_cost
- spatial_transfer
models: []
proposed_tags:
- pretraining_data_diversity
- spectral_entropy
- SatMAE
- continent_sampling
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- population_density
- crop_type_mapping
- representation_probing
title: Pretrain Where? Investigating How Pretraining Data Diversity Impacts Geospatial
  Foundation Model Performance
venue: arXiv
---

## summary

This paper systematically studies how the geographic and spectral composition of pretraining data affects downstream performance of a SatMAE-based geospatial foundation model, finding that a Europe-only pretraining dataset consistently outperforms globally balanced and other continent-specific pretraining datasets across global and local downstream tasks. Correlation analysis across ten pretraining datasets shows per-sample spectral entropy is strongly correlated with downstream performance while continent, biome, and landcover diversity are only weakly correlated.

## setup

The authors pretrain SatMAE (ViT-Base) from scratch on seven newly constructed 700k-sample pretraining datasets (six single-continent and one global) sampled via QGIS from Sentinel-2 imagery, then evaluate via linear probing (plus kNN and full finetuning for FMoW) on global and per-continent subsets of FMoW-Sentinel, MOSAIKS population density, ForTy segmentation, and six GEO-Bench Sentinel-2 tasks. They additionally analyze diversity (continent, biome, landcover, spectral entropy) across these plus three published pretraining datasets (FMoW, SSL4EO-S12, SSL4Eco) and correlate it with mean downstream performance.

## caveats

The authors note the study is limited to a single architecture (SatMAE) due to compute cost, and that findings may not generalize to other RSFM architectures; they also note the diversity-performance correlation analysis used only ten pretraining datasets, so a broader set would strengthen generality, and correlations for continent/biome/landcover diversity had low statistical significance (p>0.2) given the small sample size.
