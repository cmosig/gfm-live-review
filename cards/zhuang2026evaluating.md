---
arxiv_id: '2608.12663'
authors:
- Yuan Zhuang
- Sanaa Hobeichi
- Peng Shi
- Fei Huang
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G7_interpretability
- G9_ecological_fine_scale
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.0
  dataset: Canberra–Namadgi transfer site
  direction: better
  id: zhuang2026evaluating#c1
  label_ratio: null
  locator: Abstract
  metric: auc
  model: alphaearth
  span: ROC-AUC improves by around 4% at Canberra and declines by around 2% at Western
    Sydney–Blue Mountains
  span_sha256: 1d956bcc13348f5026ce63dce612cb6458cd5f67a57673e09680d0835ef7a0ad
  task: landslide_susceptibility
  value: 0.0
date: '2026-08-12'
doi: 10.48550/arxiv.2608.12663
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-16T00:09:08.155476Z'
key: zhuang2026evaluating
limitations:
- spatial_transfer
- temporal_transfer
- time_sensitivity
- benchmark_narrowness
- interpretability
models:
- alphaearth
proposed_tags:
- wildfire_susceptibility_mapping
- reconstruction_of_physical_variables
- CNN_neighbourhood_patch
- TabPFN_tabular_foundation_model
- sequence_informed_modelling
regions:
- au
self_evaluation: false
tasks:
- landslide_susceptibility
- representation_probing
title: Evaluating AlphaEarth Foundations Embeddings for Wildfire Susceptibility Mapping
venue: arXiv
---

## summary

The paper evaluates AlphaEarth Foundations (AEF) embeddings against hand-engineered physical variables for wildfire susceptibility mapping in Victoria, Australia, testing tabular models (Random Forest, XGBoost, LightGBM, MLP, TabPFN) and CNNs on both cross-sectional and sequence-informed inputs. AEF embeddings achieve within-region ROC-AUC above 0.92 and, critically, transfer far better than physical variables to nearby Australian regions (e.g. Canberra, Western Sydney), though transfer degrades at more climatically distant sites. A reconstruction analysis shows many physical wildfire drivers (e.g. temperature, precipitation, wind, solar radiation, NDVI) can be recovered from AEF embeddings with high R2.

## setup

Fire occurrence labels from MODIS FIRMS (MCD14ML, confidence ≥80%) rasterised to a 1km grid over Victoria (2017–2025), paired with 22 VIF-screened physical variables or 64-dim AEF embeddings; 10 stratified 70/30 train/test splits, with transferability tested on 8 additional Australian sites.

## caveats

Authors note AEF transfer advantage diminishes with increasing climatic/geographic distance from the source region, sequence-informed (annual) modelling gave only modest gains likely due to 1km aggregation smoothing fine-scale annual variation, fire-season persistence/extreme-condition variables reconstructed poorly and inconsistently across years, susceptibility scores are relative not calibrated ignition probabilities, and the elevated learned weight on 2020 reflects a labelling artifact (Black Summer fires) rather than a causal signal.
