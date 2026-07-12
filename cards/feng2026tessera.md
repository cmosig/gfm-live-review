---
arxiv_id: '2607.03949'
authors:
- Zhengpeng Feng
- Sadiq Jaffer
- Ira Shokar
- Jovana Knezevic
- Mark Elvers
- Clement Atzberger
- Robin Young
- Aneesh Naik
- Niall Robinson
- Andrew Blake
- David Coomes
- Anil Madhavapeddy
- Srinivasan Keshav
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G4_temporal_transfer
- G5_cost
- G6_compactness
- G12_openness
claims: []
date: '2026-07-04'
doi: 10.48550/arxiv.2607.03949
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:03:30.364714Z'
key: feng2026tessera
limitations:
- benchmark_narrowness
- compute_cost
- spatial_transfer
- temporal_transfer
- data_bias
models:
- tessera
- alphaearth
- presto
- galileo
- croma
- scalemae
proposed_tags:
- matryoshka-embeddings
- downstream-driven-scaling-laws
- knowledge-distillation
- embeddings-as-data
- pretraining-loss-vs-downstream
- compute-optimal-allocation
- pixel-wise-foundation-model
- sentinel-1-2-fusion
- barlow-twins
- nested-embeddings
- storage-adaptive
regions:
- global
self_evaluation: true
tasks:
- land_cover_classification
- semantic_segmentation
- change_detection
- biomass_estimation
- crop_type_mapping
- population_density
- socioeconomic_estimation
- urban_signal_mapping
title: 'TESSERA v2: Scaling Pixel-wise Earth Foundation Models'
venue: arXiv
---

## summary

TESSERA v2 is a pixel-wise Sentinel-1/2 Earth-observation foundation model built from a 395-run downstream-driven scaling study showing that pretraining loss poorly predicts downstream performance and that compute should go to encoder capacity and data rather than the projector. A 1B pixel-wise teacher is distilled into a family of compact Matryoshka students (N/S/M/L) serving nested 16/32/64/128-dimensional embeddings-as-data. The 21M-parameter TESSERA v2-1B-M achieves the best composite score (0.611) on a 29-task suite, outperforming AlphaEarth, TESSERA v1, and OlmoEarth.

## setup

Every one of 395 pretraining runs is evaluated on a 15-task AlphaEarth suite (classification, segmentation, change detection, regression from 10 source datasets) with chance-adjusted metrics averaged into a composite; the distilled students are additionally tested on 14 held-out datasets (vegetation and urban groups) for a 29-task suite at 1/30/100% label budgets. Each task uses a fixed lightweight head (2-layer MLP for pixel tasks, small CNN for patch tasks), comparing against AlphaEarth, TESSERA v1, OlmoEarth, Presto, MOSAIKS, and other RSFM backbones.

## caveats

The authors flag that the scaling laws are empirical and specific to pixel-wise Sentinel-1/2 encoders, one self-supervised objective, and one 15-task suite; that the teacher is computationally expensive to train; and that benchmarks come from well-studied regions, leaving generalisation to under-represented climates and unseen seasons unevaluated.
