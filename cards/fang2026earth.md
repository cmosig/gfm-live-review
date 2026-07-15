---
arxiv_id: '2601.13134'
authors:
- Heng Fang
- Adam J. Stewart
- Isaac Corley
- Xiao Xiang Zhu
- Hossein Azizpour
axes:
- G5_cost
- G6_compactness
- G7_interpretability
- G11_complementarity
- G12_openness
claims: []
date: '2026-01-19'
doi: 10.48550/arxiv.2601.13134
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:43:03.316097Z'
key: fang2026earth
limitations:
- compute_cost
- interpretability
- benchmark_narrowness
- uncertainty
models:
- clay
- presto
- tessera
- satclip
- dofa
- alphaearth
proposed_tags:
- embedding_products
- taxonomy
- torchgeo
- data_standardization
- search_retrieval
regions:
- global
- tg
self_evaluation: false
tasks:
- crop_type_mapping
- poverty_mapping
- representation_probing
- land_cover_classification
title: 'Earth Embeddings as Products: Taxonomy, Ecosystem, and Standardized Access'
venue: arXiv
---

## summary

This paper is a survey and infrastructure contribution that formalizes a taxonomy of Earth embedding products (Data, Tools, Value layers), reviews seven existing embedding products (Clay, Major TOM, Earth Index, Copernicus-Embed, Presto, Tessera, Google Satellite Embedding) for reproducibility and interoperability, and extends the TorchGeo library with standardized data loaders for these products. It does not run new downstream benchmark evaluations but instead surveys the ecosystem and identifies adoption barriers (distribution formats, reproducibility, generating new embeddings).

## setup

The authors compile a metadata atlas (Table I/II) of seven embedding products, comparing spatial/temporal resolution, dimensions, license, architecture, SSL pretraining method, and data provenance; they demonstrate TorchGeo integration via search/retrieval (Earth Index + Sentinel-2) and land cover mapping (Google Satellite Embedding + EuroCrops) code examples rather than reporting new benchmark numbers.

## caveats

The authors flag fragmented distribution formats (GeoParquet, GeoTIFF, NumPy/PyTorch files lacking geospatial metadata, upside-down rasters for Google embeddings), poor reproducibility (unmaintained repos, no tests/CI, training data scraped from continuously-updated sources like Planetary Computer/GEE that may no longer match original versions), limited documented tutorials for generating new embeddings, overrepresentation of Sentinel 1/2 relative to other modalities, and insufficient uncertainty quantification/explainability in embedding products.
