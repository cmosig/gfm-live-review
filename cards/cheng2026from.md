---
arxiv_id: '2601.07268'
authors:
- Yusen Cheng
- Qinfeng Zhu
- Lei Fan
axes:
- G1_label_rich_parity
- G4_temporal_transfer
- G6_compactness
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.9
  dataset: Nantou County, Taiwan
  direction: better
  id: cheng2026from#c1
  label_ratio: null
  locator: Sec 4.3
  metric: auc
  model: alphaearth
  span: In Nantou, AUC values increased from approximately 0.90 for LCF-based models
    to around 0.99 when AE features were used
  span_sha256: 8b46f671441d17aa31a8ab28d130e35710c3f0af86ea73b32aabfed4e99e394e
  task: landslide_susceptibility
  value: 0.99
date: '2026-01-12'
doi: null
doi_status: no_doi_found
extractor_version: '1'
ingested_at: '2026-07-12T16:32:48.899861Z'
key: cheng2026from
limitations:
- interpretability
- time_sensitivity
- spatial_transfer
- temporal_transfer
models:
- alphaearth
proposed_tags:
- landslide_conditioning_factors
- satellite_embeddings
- PCA_dimensionality_reduction
- CNN1D
- CNN2D
- vision_transformer
- temporal_alignment
- handcrafted_features_vs_embeddings
regions:
- tw
- hk
- it
self_evaluation: false
tasks:
- landslide_susceptibility
title: 'From Landslide Conditioning Factors to Satellite Embeddings: Evaluating the
  Utilisation of Google AlphaEarth for Landslide Susceptibility Mapping using Deep
  Learning'
venue: arXiv
---

## summary

The paper evaluates Google AlphaEarth (AE) embeddings as an alternative to conventional landslide conditioning factors (LCFs) for landslide susceptibility mapping across three study areas using CNN1D, CNN2D, and ViT models. AE-based models (both PCA-reduced and full 64-band) consistently outperformed LCF-based inputs in F1-score, AUC, and error metrics. Gains were largest in Nantou and Emilia and smaller in Hong Kong, attributed to temporal alignment between AE embeddings and landslide inventories.

## setup

Landslide inventories for Nantou County (Taiwan), Hong Kong, and Brisighella/Modigliana (Emilia-Romagna, Italy) with 1:1 landslide/non-landslide sampling were modeled using three deep learning architectures on a 7:3 train/validation split. Inputs compared were 14 LCFs, AE PCA bands (90% variance), and all 64 AE bands, all resampled to 30 m, evaluated via accuracy, precision, recall, specificity, F1, ROC-AUC, MAE, and RMSE.

## caveats

Authors note band-level interpretability of AE embeddings was not analyzed (black-box concern), that temporal mismatch between annual AE embeddings and aggregated multi-year inventories (e.g., Hong Kong) weakens performance, that the AE dataset spans only 2017–2024 limiting temporal analysis, and that cross-region transfer in data-scarce settings remains untested.
