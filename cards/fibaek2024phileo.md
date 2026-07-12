---
arxiv_id: '2401.04464'
authors:
- Casper Fibaek
- Luke Camilleri
- Andreas Luyts
- Nikolaos Dionelis
- Bertrand Le Saux
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G7_interpretability
- G9_ecological_fine_scale
claims: []
date: '2024-01-09'
doi: 10.48550/arxiv.2401.04464
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:50:37.980529Z'
key: fibaek2024phileo
limitations:
- benchmark_narrowness
- spatial_transfer
- mixed_pixels
models:
- prithvi
proposed_tags:
- building_density_estimation
- road_segmentation
- phileo_bench
regions:
- dk
- eg
- gn
- gh
- il
- jp
- ng
- sn
- tz
- ug
- global
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
title: 'PhilEO Bench: Evaluating Geo-Spatial Foundation Models'
venue: arXiv
---

## summary

PhilEO Bench introduces a 400GB global Sentinel-2 dataset with labels for building density, road segmentation, and land cover classification, plus a standardized evaluation framework with a common decoder head to fairly compare EO foundation models. Experiments across n-shot settings show that pre-trained models (including Prithvi and SatMAE) underperform a simple U-Net on image-to-image tasks like building density estimation, though Prithvi achieves the lowest MSE due to being evaluated at coarser 30m resolution.

## setup

The PhilEO downstream dataset spans diverse global regions (Denmark, East Africa, Egypt, Guinea, Ghana, Israel, Japan, Nigeria, Senegal, Tanzania, Uganda, North/South America) with 11-band 10m Sentinel-2 tiles labeled for roads, buildings, and land cover; models are evaluated via linear probing and fine-tuning with a shared U-Net-style decoder across n-shot training set sizes.

## caveats

The authors note that fairly evaluating models trained at different resolutions (e.g. Prithvi's 30m vs others' 10m) is unresolved and skews MSE comparisons, and that the bottleneck in encoder-decoder FM architectures limits low-level detail needed for image-to-image tasks, an issue left as future work.
