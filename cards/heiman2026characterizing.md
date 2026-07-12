---
arxiv_id: '2605.05547'
authors:
- Alice Heiman
axes:
- G7_interpretability
- G9_ecological_fine_scale
- G10_human_semantics
- G11_complementarity
- G12_openness
claims: []
date: '2026-05-07'
doi: 10.48550/arxiv.2605.05547
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:40:18.841817Z'
key: heiman2026characterizing
limitations:
- benchmark_narrowness
- temporal_transfer
- uncertainty
models:
- alphaearth
proposed_tags:
- forest_restoration_monitoring
- reforestation
- reference_trajectory_embedding
- cosine_similarity_metric
- umap_visualization
- ndvi_saturation
- restoration_strategy_prediction
- atlantic_forest
- proprietary_model
- lulc_misclassification_detection
regions:
- br
self_evaluation: false
tasks:
- land_cover_classification
- change_detection
- representation_probing
title: Characterizing Brazilian Atlantic Forest Restoration Outcomes with Geospatial
  AlphaEarth Embeddings
venue: arXiv
---

## summary

The paper uses AlphaEarth Foundations satellite embeddings to characterize early restoration success at 1,729 reforestation sites in São Paulo, Brazil, introducing a 'Reference Trajectory Embedding' metric based on cosine similarity to mature secondary forest reference sites. Embeddings form interpretable LULC clusters and capture change vectors, and improve prediction of future reference similarity over NDVI/EVI, but do not improve restoration-strategy prediction and can be noisy. The authors conclude embeddings may need further fine-tuning to capture site metadata beyond LULC.

## setup

Data from 1,729 ORR restoration polygons (2017–2024, ≥1 ha) plus MapBiomas-sampled stable and changing LULC reference points, with 64-dim annual AlphaEarth embeddings, Sentinel-2 NDVI/EVI, and environmental covariates extracted in Google Earth Engine. Prediction tasks (future similarity at Δt=+3 and restoration strategy) use Logistic Regression and Random Forest with 5-fold spatial k-means cross-validation across feature sets.

## caveats

AlphaEarth is proprietary and results may not generalize to open models like Clay or SatMAE; the short 2017–2024 window captures only early restoration stages; the similarity signal can be noisy; and remote sensing should complement rather than replace community engagement.
