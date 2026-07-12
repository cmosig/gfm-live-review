---
arxiv_id: '2602.10354'
authors:
- Mashrekur Rahman
axes:
- G7_interpretability
- G3_spatial_transfer
- G4_temporal_transfer
- G10_human_semantics
claims:
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: CONUS 12.1M-sample environmental variables
  direction: parity
  id: rahman2026physically#c1
  label_ratio: null
  locator: Sec 3.1.2
  metric: r2
  model: alphaearth
  span: dew point temperature (R2=0.97R^{2}=0.97)
  span_sha256: 44d2eeccd80da3530d4a8b920d40bbadf114aba40a4e49ea2d97bc9f128cb67b
  task: representation_probing
  value: 0.97
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: CONUS 12.1M-sample environmental variables
  direction: parity
  id: rahman2026physically#c2
  label_ratio: null
  locator: Sec 3.1.2
  metric: r2
  model: alphaearth
  span: Elevation (R2=0.96R^{2}=0.96)
  span_sha256: 50a61f2c75ddb9b8dd88885417a74a01383e00f927b11d0cf62ee9c533c81993
  task: representation_probing
  value: 0.96
- axis: G7_interpretability
  baseline: null
  baseline_value: null
  dataset: CONUS 12.1M-sample environmental variables
  direction: parity
  id: rahman2026physically#c3
  label_ratio: null
  locator: Sec 3.1.2
  metric: r2
  model: alphaearth
  span: NDVI (R2=0.94R^{2}=0.94)
  span_sha256: 48739ae59562bcbcac6b89717b570281aeb7ffe37fb29d4465d9859ce06697fd
  task: representation_probing
  value: 0.94
- axis: G7_interpretability
  baseline: null
  baseline_value: 0.83
  dataset: CONUS annual precipitation (PRISM)
  direction: better
  id: rahman2026physically#c4
  label_ratio: null
  locator: Sec 3.1.3
  metric: r2
  model: alphaearth
  span: annual precipitation increases from R2=0.83R^{2}=0.83 (RF) to R2=0.92R^{2}=0.92
  span_sha256: 427d4879520fef67ff7d38df7147b4c1fc51926137ad3419ac2cd2df7ba883f2
  task: representation_probing
  value: 0.92
date: '2026-02-10'
doi: 10.48550/arxiv.2602.10354
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:46:50.852950Z'
key: rahman2026physically
limitations:
- spatial_transfer
- temporal_transfer
- mixed_pixels
models:
- alphaearth
proposed_tags:
- embedding_interpretability
- retrieval_augmented_generation
- llm_as_judge
- natural_language_query
- faiss_similarity_search
- dimension_dictionary
- environmental_variable_regression
- attention_probing
regions:
- us
self_evaluation: false
tasks:
- representation_probing
title: Physically Interpretable AlphaEarth Foundation Model Embeddings Enable LLM-Based
  Land Surface Intelligence
venue: arXiv
---

## summary

Using 12.1M CONUS samples (2017-2023), the authors probe Google AlphaEarth's 64-D embeddings against 26 environmental variables with Spearman correlation, Random Forest, and a multi-task Transformer, showing individual dimensions map to specific land-surface properties and the full space reconstructs most variables with high fidelity (12 of 26 exceed R2>0.90). These relationships stay robust under spatial block cross-validation (mean ΔR2=0.017) and temporally stable across seven years (mean r=0.963). The validated interpretations power a FAISS-based retrieval-augmented-generation Land Surface Intelligence system evaluated via LLM-as-Judge over 360 query-response cycles.

## setup

12.1M embedding vectors were extracted over a CONUS grid at 1 km scale and co-located with 26 environmental variables from sources like SRTM, MODIS, PRISM, ERA5-Land, and VIIRS. Interpretability used Spearman ρ, Random Forest, and a TabTransformer with 5-fold and 2°×2° spatial block cross-validation; the RAG system was assessed by four LLMs rotating generator/system/judge roles on a weighted 1-5 rubric.

## caveats

The authors note the analysis is restricted to the Continental United States and to seven years of annual composites, limiting geographic and temporal generality. They flag that single annual composites hinder change detection, that soil and urban/fine-scale terrain variables are weakly encoded, and that evaluation relies on LLM-based judges and the author's own expertise, which introduces bias despite the rotating-role design.
