---
arxiv_id: '2606.02374'
authors:
- Steffen Knoblauch
- Hao Li
- Gengchen Mai
- Konstantin Klemmer
- Song Gao
- WenWen Li
axes:
- G10_human_semantics
- G11_complementarity
- G12_openness
- G7_interpretability
- G8_uncertainty
claims: []
date: '2026-06-01'
doi: 10.48550/arxiv.2606.02374
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:35:41.803107Z'
key: knoblauch2026spatial
limitations:
- human_semantics
- benchmark_narrowness
- data_bias
- interpretability
- uncertainty
- mixed_pixels
models:
- satclip
- prithvi
- presto
proposed_tags:
- raster_vector_fusion
- vector_data_representation_learning
- OpenStreetMap_integration
- earth_embeddings
- spatial_fairness
- world_models
regions:
- global
self_evaluation: false
tasks:
- wealth_mapping
- representation_probing
title: 'Spatial Representation Learning Beyond Pixels: Unifying Raster Data and Vector
  Semantics for Human-Centric Geospatial Foundation Models'
venue: arXiv
---

## summary

This is a perspective/position paper arguing that current Earth Observation Foundation Models remain confined to raster modalities and overlook structured vector data (OpenStreetMap, Overture), and calls for unified Spatial Representation Learning (SRL) that integrates raster perception with vector-based reasoning. It surveys existing raster-based EOFMs and vector/polymorphic representation methods, critiques lossy raster-vector conversion strategies, and proposes a research agenda covering methodology, fairness, evaluation, and uncertainty quantification for human-centric geospatial foundation models.

## setup

No new experiments are conducted; this is a perspective/position paper synthesizing and critiquing existing literature on raster-based EOFMs (e.g., SatCLIP, Prithvi-EO-2.0, AlphaEarth) and vector-based SRL approaches (e.g., S2Vec, Poly2Vec, GeoLink), and outlining a research agenda for unified raster-vector spatial foundation models.

## caveats

The authors note that vector-to-raster conversion causes irreversible information loss and modifiable areal unit problems, that no holistic benchmark exists for joint raster-vector reasoning, that vector data (e.g., OpenStreetMap) exhibits strong geographic coverage bias favoring high-income countries, and that sparse-autoencoder interpretability findings for Earth embeddings remain preliminary and require further validation.
