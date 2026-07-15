---
arxiv_id: '2602.23678'
authors:
- Dingqi Ye
- Daniel Kiv
- Wei Hu
- Jimeng Shi
- Shaowen Wang
axes:
- G1_label_rich_parity
- G11_complementarity
- G12_openness
claims: []
date: '2026-02-27'
doi: 10.48550/arxiv.2602.23678
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:58:00.105499Z'
key: ye2026any
limitations:
- benchmark_narrowness
models:
- alphaearth
proposed_tags:
- rs-embed
- embedding_library
- ROI_centric_interface
- AgriFM
regions:
- us
- cn
self_evaluation: false
tasks:
- crop_yield_estimation
- representation_probing
title: 'Any Model, Any Place, Any Time: Get Remote Sensing Foundation Model Embeddings
  On Demand'
venue: arXiv
---

## summary

The paper introduces rs-embed, a Python library providing a unified ROI-centric interface to retrieve embeddings from many remote-sensing foundation models for any location/time with a single line of code. It addresses fragmentation in model release formats, input specs, and interfaces, and provides batch processing infrastructure for large-scale embedding generation. It is not itself a foundation model paper but a tooling/infrastructure contribution demonstrated via a maize yield mapping use case and embedding visualization.

## setup

A regression experiment predicts maize yield in Illinois using SPAM2020V2 as labels, with 991 sampling points from cropland areas (Maize Area > 2500 ha), extracting embeddings from multiple RSFMs via rs-embed for June-Aug 2019 and training a Random Forest regressor. A separate qualitative visualization compares embeddings from 16 models over Shanghai (lon=121.5, lat=31.2) using PCA-based pseudo-RGB.

## caveats

The authors note that even the best-performing model (AgriFM) struggles to fit samples with extremely high or low yields, failing to accurately capture outliers.
