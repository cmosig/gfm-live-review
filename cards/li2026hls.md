---
arxiv_id: '2606.18115'
authors:
- Junjie Li
- Hankui K. Zhang
- David P. Roy
axes: []
claims: []
date: '2026-06-16'
doi: 10.48550/arxiv.2606.18115
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:31:54.620023Z'
key: li2026hls
limitations:
- compute_cost
- spatial_transfer
models:
- prithvi
proposed_tags:
- reflectance_reconstruction
- gap_filling
- time_series_reconstruction
- cloud_gap_imputation
- surface_reflectance
- red_edge_reconstruction
regions:
- us
self_evaluation: false
tasks: []
title: 'HLS-GPT: A Generative Pretrained Transformer (GPT) for Continental-Scale NASA
  Harmonized Landsat and Sentinel-2 (HLS) Reflectance Reconstruction Across All Bands
  on Arbitrary Dates'
venue: arXiv
---

## summary

HLS-GPT is a hierarchical Transformer trained with a masked temporal reconstruction strategy on nine years of single-pixel CONUS HLS reflectance time series to reconstruct all Landsat and Sentinel-2 reflectance bands, including red-edge, for any date. Evaluated on 62,590 held-out test pixels and nine independent CONUS tiles, it achieves band RMSE <0.026 and outperforms two conventional time-series fitting methods (HANTS, Savitzky-Golay) and the NASA-IBM Prithvi-EO-2.0 foundation model on reconstruction RMSE and SSIM across tiles and land cover classes. The paper is primarily a domain-specific reconstruction model paper, not a downstream GFM benchmarking study, and uses Prithvi only as one comparison baseline for reflectance gap-filling.

## setup

Trained on single-pixel 9-year (2015-2023) HLS reflectance time series extracted from 96 CONUS 109x109 km tiles (312,950 pixel locations; >130 million good-quality observations; 80/20 train/test split), using random 12-month cropping with 50% observation masking for self-supervised training. Evaluated via leave-one-observation-out and fixed-proportion random-masking tests on test pixels, plus full-tile image reconstruction on 9 independent CONUS tiles compared against HANTS, Savitzky-Golay filtering, and Prithvi-EO-2.0-600M-TL.

## caveats

Authors note that scaling the model globally is an open question because of diverse and hemisphere-shifted phenological regimes across biomes, uncertain whether one unified model or region-specific models would be needed. They also note substantial computational cost: ~66 minutes of GPU inference per 12-month tile reconstruction and ~170 minutes total end-to-end runtime dominated by tile I/O.
