---
arxiv_id: '2604.14756'
authors:
- Nori Nakata
- Jingxiao Liu
- Guodong Chen
- Rie Nakata
- Charuleka Varadharajan
axes:
- G2_label_scarce_efficiency
- G5_cost
- G7_interpretability
- G11_complementarity
claims: []
date: '2026-04-16'
doi: 10.48550/arxiv.2604.14756
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:42:55.829766Z'
key: nakata2026subsurface
limitations:
- spatial_transfer
- data_bias
- uncertainty
- interpretability
models:
- alphaearth
proposed_tags:
- vs30_estimation
- seismic_site_characterization
- subsurface_temperature_mapping
- geothermal_gradient
- surface_to_subsurface_inference
- near_surface_seismic_velocity
regions:
- us
self_evaluation: false
tasks: []
title: Subsurface Property Mapping using Google AlphaEarth Foundations
venue: arXiv
---

## summary

The paper uses fixed AlphaEarth 64-dimensional embeddings as a surface representation to infer two subsurface targets over the conterminous US: shallow seismic velocity (VS30) and subsurface temperature. Embedding-informed models (tree ensembles for VS30, an MLP for temperature) outperform simpler terrain-only or no-embedding baselines and recover physically plausible regional patterns. The authors stress that domain covariates stabilize VS30 regression while temperature relies primarily on embeddings, and that random splits may inflate apparent skill.

## setup

VS30 uses 2886 conterminous US stations from the USGS Updated VS30 compilation with an 80/20 split, comparing four feature sets (AlphaEarth, log-slope+tectonic status, and combinations) across linear regression, random forest, and XGBoost, reported via RMSE/MAE/R2. Subsurface temperature uses >400,000 borehole measurements over a 20 km grid (20,971 cells), training an MLP on 64-dim embeddings at 1000 m depth with an 80/20 region-stratified split. Both extract the 2024 annual AlphaEarth layer from Google Earth Engine at a 1 km scale.

## caveats

The authors flag potential overestimation of generalization from uneven station distribution, mixed measurement protocols, and random train-test splits that allow spatial interpolation/leakage within densely observed regions. They note the temperature model's latent representations are less interpretable, and call for spatial block cross-validation, leave-region-out tests, and explicit uncertainty quantification.
