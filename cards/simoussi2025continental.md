---
arxiv_id: '2507.09732'
authors:
- Sara Si-Moussi
- Stephan Hennekens
- Sander Mucher
- Stan Los
- Yoann Cartier
- Borja Jiménez-Alfaro
- Fabio Attorre
- Jens-Christian Svenning
- Wilfried Thuiller
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G9_ecological_fine_scale
- G12_openness
claims: []
date: '2025-07-13'
doi: 10.48550/arxiv.2507.09732
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:55:46.886370Z'
key: simoussi2025continental
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
- spatial_transfer
models:
- prithvi
- dofa
proposed_tags:
- habitat_distribution_modelling
- EUNIS_classification
- vegetation_plots
- ensemble_machine_learning
- class_imbalance_correction
- multimodal_EO_fusion
- SSL4EO
- SECO
- hierarchical_classification
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
- representation_probing
title: Continental-scale habitat distribution modelling with multimodal earth observation
  foundation models
venue: arXiv
---

## summary

The paper compares multiple habitat distribution modelling strategies (multi-class vs hierarchical, multiple environmental modalities) for mapping EUNIS Level 3 habitats across Europe at 100m resolution, using vegetation plots from the European Vegetation Archive. It evaluates several Earth Observation foundation models (including DOFA and Prithvi) to extract embeddings from Sentinel-1/2 imagery and compares them against a custom supervised CNN baseline (EO4B) and finds self-supervised EO-FMs outperform the supervised baseline. Ensemble machine learning with imbalance correction and hierarchical classification schemes further improved habitat classification accuracy at continental scale.

## setup

Training used 597,810 vegetation plots from the European Vegetation Archive (EVA) classified into 243 EUNIS Level 3 habitat classes, validated against independent datasets from the Netherlands, Portugal, France (IFN), and Austria. Environmental predictors combined bioregion, abiotic (climate/soil/terrain), remote sensing products, and Sentinel-1/2 image patches embedded via various EO foundation models, evaluated with 5-fold spatial block cross-validation.

## caveats

The authors note they did not fine-tune the EO-FMs for computational parsimony, potentially losing class-specific sensitivity; labels correspond to plot centroids rather than polygons, introducing positional noise; and observational density is higher in central/northern Europe than in Mediterranean or boreal regions, so absolute accuracies may be optimistic in under-sampled ecoregions.
