---
arxiv_id: '2606.05368'
authors:
- Sayan Mandal
- Rocco Sedona
- Simon Besnard
- Mikhail Urbazaev
- Morris Riedel
- Ehsan Zandi
- Gabriele Cavallaro
axes:
- G9_ecological_fine_scale
- G11_complementarity
- G6_compactness
- G5_cost
claims: []
date: '2026-06-03'
doi: 10.48550/arxiv.2606.05368
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:37:26.667662Z'
key: mandal2026biomazon
limitations:
- benchmark_narrowness
- data_bias
- temporal_transfer
models:
- prithvi
- alphaearth
proposed_tags:
- rh_profile_prediction
- vertical_forest_structure
- gedi_lidar_supervision
- monotone_ordered_quantile_output
- structure_biomass_coupling
- multimodal_sensor_fusion
- alphaearth_late_fusion
- agbd
- amazon_basin
- dataset_paper
regions:
- br
self_evaluation: false
tasks:
- biomass_estimation
- canopy_height_estimation
title: 'Biomazon: A Multimodal Dataset for 3D Forest Structure and Biomass Modeling
  in the Amazon Basin'
venue: arXiv
---

## summary

Biomazon is a 20 m multimodal benchmark over the Amazon Basin pairing GEDI full RH profiles and AGBD targets with Sentinel-1/2, ALOS-2 PALSAR-2, DEM, LULC, and AlphaEarth embeddings under standardized spatial splits. Using a shared Prithvi-EO-2.0 encoder-decoder with task-specific heads, the authors benchmark backbone scale, modality contributions, and raw modalities versus AlphaEarth embeddings, and propose an anchored monotone parameterization enforcing physically consistent RH ordering. Baselines are contextualized against gridded products such as GEDI L4D imputed RH/AGBD and canopy-height/biomass maps.

## setup

1,329,397 patches (953k train / 127k val / 249k test) of 256x256 pixels tiled across 913 HLS-MGRS tiles over April 2019-March 2023, split at tile level to avoid leakage. Prithvi-5M/100M/300M encoders with DPT decoder and monotone RH + AGBD heads, trained with sparse Huber loss and Label Distribution Smoothing on 64 GPUs; test metrics (RMSE, RMSE%, MAE, bias, R2) reported over RH25/50/75/95/98 and AGBD.

## caveats

Authors note AlphaEarth embeddings do not uniformly outperform strong domain-specific baselines, that the RH98/RH25/AGBD capping and filtering discard genuine extreme returns, that the strict-positive RH100 anchor would need revisiting for near-zero/bare-ground cases, and that inputs are multi-year composites so temporal-location encodings are frozen; validation/test tiles cluster in denser forest, introducing distributional bias relative to training.
