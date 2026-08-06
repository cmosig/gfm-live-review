---
arxiv_id: '2608.03410'
authors:
- Adam J. Stewart
- Heng Fang
- Isaac A. Corley
- Xiao Xiang Zhu
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G6_compactness
- G7_interpretability
- G8_uncertainty
- G11_complementarity
- G12_openness
claims: []
date: '2026-08-04'
doi: 10.48550/arxiv.2608.03410
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-06T00:17:53.463875Z'
key: stewart2026earth
limitations:
- spatial_transfer
- temporal_transfer
- interpretability
- uncertainty
- compute_cost
- benchmark_narrowness
- mixed_pixels
- data_bias
models:
- alphaearth
- tessera
- presto
- clay
- geoclip
- satclip
- dofa
proposed_tags:
- embedding_products
- license_openness
- quantization
- storage_cost
- reproducibility
- implicit_location_embeddings
- patch_embeddings
- pixel_embeddings
- search_and_retrieval
regions:
- global
- tw
- hk
- it
- tg
- us
- de
- br
self_evaluation: false
tasks:
- crop_type_mapping
- crop_yield_estimation
- landslide_susceptibility
- poverty_mapping
- land_cover_classification
- representation_probing
- urban_signal_mapping
- change_detection
- semantic_segmentation
title: Earth Embeddings
venue: arXiv
---

## summary

This chapter surveys the emerging landscape of Earth embeddings, categorizing them into implicit location encoders, explicit patch embeddings, and explicit pixel embeddings, and compares their coverage, resolution, dimensionality, storage cost, licenses, and reproducibility. It reviews evidence from downstream studies on land cover, agriculture, hazard, ecological, and socioeconomic applications, and provides case studies plus guidance on choosing, storing, and publishing embeddings. The authors close with open problems around oceanic/atmospheric coverage, uncertainty quantification, and the need for shared benchmarking protocols.

## setup

The paper is a review/case-study chapter (not a controlled experimental study) that synthesizes results from many cited papers using products such as Google Satellite Embedding (AlphaEarth), Tessera, Presto, Clay, GeoCLIP, and SatCLIP across tasks including cropland mapping, tree species classification, crop yield/tillage prediction, landslide susceptibility, poverty mapping, and scene classification (e.g., EuroSAT-Embed). It also presents two worked TorchGeo code examples (search/retrieval and land cover mapping) rather than novel benchmark experiments.

## caveats

The authors note that current embeddings show inconsistent gains, are less robust under spatial transfer (e.g., GSE for crop yield/tillage mapping), and that annual/snapshot embeddings poorly capture event-level change detection or temporally sensitive agricultural signals. They also flag major coverage gaps (oceans, atmosphere, snow/ice), lack of uncertainty quantification in embedding products, proprietary/non-reproducible pipelines for some pixel embeddings (e.g., AlphaEarth, ESDNet), and inconsistent benchmarking practices across the field with reported accuracy differences exceeding ten points for identical models on the same benchmark.
