---
arxiv_id: '2511.21194'
authors:
- Selene Cerna
- Sara Si-Moussi
- Wilfried Thuiller
- Hadrien Hendrikx
- Vincent Miele
axes:
- G2_label_scarce_efficiency
- G11_complementarity
- G3_spatial_transfer
claims:
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.45
  dataset: Plant presence (French Alps relevés)
  direction: better
  id: cerna2025botaclip#c1
  label_ratio: null
  locator: Table 1 / Sec 5.1
  metric: balanced_accuracy
  model: dofa
  span: all DOFA-based BotaCLIP variants increased TSS relative to Raw (0.45), with
    the best median achieved by BLS (0.53)
  span_sha256: f9f2942f8de9bdf275312980739d888f5887b1b6a62c635296ef9611356ad591
  task: representation_probing
  value: 0.53
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.68
  dataset: Butterfly occurrence (French Alps)
  direction: better
  id: cerna2025botaclip#c2
  label_ratio: null
  locator: Sec 5.1
  metric: balanced_accuracy
  model: dofa
  span: the best median Boyce Index obtained by BASR (0.74) compared to Raw (0.68)
  span_sha256: 205d24f1c5b80cf5844dcc6656161e7b96f4d0ba36be75ba92791ed52d75fec9
  task: representation_probing
  value: 0.74
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.46
  dataset: Plant presence (French Alps relevés)
  direction: better
  id: cerna2025botaclip#c3
  label_ratio: null
  locator: Table 5 Block II
  metric: balanced_accuracy
  model: dofa
  span: BLSR significantly outperformed BotaSP for plants across all backbones
  span_sha256: bed25dff23a4ba6c3b889eacf042ca4b5bd8e9f7821d7bdcb8622436014d5ac4
  task: representation_probing
  value: 0.52
date: '2025-11-26'
doi: 10.48550/arxiv.2511.21194
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:26:36.431494Z'
key: cerna2025botaclip
limitations:
- benchmark_narrowness
- spatial_transfer
- data_bias
- mixed_pixels
models:
- dofa
proposed_tags:
- biodiversity_monitoring
- plant_presence_prediction
- butterfly_occurrence_prediction
- soil_trophic_group_abundance
- contrastive_alignment
- vegetation_survey_supervision
- habitat_retrieval
regions:
- fr
self_evaluation: false
tasks:
- representation_probing
- land_cover_classification
title: 'BotaCLIP: Contrastive Learning for Botany-Aware Representation of Earth Observation
  Data'
venue: arXiv
---

## summary

BotaCLIP aligns frozen EO vision backbones (DOFA, FLAIR, DINOv3) with in-situ vegetation relevés via a regularized sigmoid contrastive loss and lightweight adapters, injecting botany-aware semantics into image embeddings. Evaluated on three French Alps ecological tasks (plant presence, butterfly occurrence, soil trophic-group abundance), BotaCLIP embeddings generally outperform raw frozen backbone features and a supervised baseline (BotaSP), especially with the DOFA backbone. Gains are large for plants and butterflies but minimal for soil trophic groups, attributed to the limited information RGB imagery carries about belowground processes.

## setup

28,418 paired 100x100m RGB orthophotos (BD ORTHO, 20cm resolution) and vegetation relevés (3,587 species) from the French Alps were used to train lightweight contrastive adapters atop frozen DOFA/FLAIR/DINOv3 image encoders and a VEGETA tabular encoder, under spatial k-fold cross-validation. Downstream evaluation used Random Forests on extracted image embeddings for plant presence (TSS/F1/Sensitivity), butterfly occurrence (TSS/BI/F1/Sensitivity), and soil trophic-group abundance (MAE/Spearman's rho), each with repeated stratified cross-validation.

## caveats

Authors note evaluation is limited to a single mountain region with unassessed geographic transfer under domain shift, relevé quality depends on uneven sampling effort and taxonomic uncertainty, soil trophic-group gains are small due to a physical ceiling on what RGB optical imagery can reveal about belowground processes, and VEGETA itself was not ablated as a component.
