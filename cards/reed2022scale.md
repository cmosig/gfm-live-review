---
arxiv_id: '2212.14532'
authors:
- Colorado J. Reed
- Ritwik Gupta
- Shufan Li
- Sarah Brockman
- Christopher Funk
- Brian Clipp
- Kurt Keutzer
- Salvatore Candido
- Matt Uyttendaele
- Trevor Darrell
axes:
- G3_spatial_transfer
- G2_label_scarce_efficiency
- G6_compactness
claims:
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: RESISC-45/UC Merced/AiRound/CV-BrCT/EuroSAT/MLRSNet/Optimal-31/WHU-RS19
    (avg)
  direction: better
  id: reed2022scale#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: scalemae
  span: The average improvement across all datasets for Scale-MAE com- pared to SatMAE
    is 5.6%
  span_sha256: 3ac1205395107628f40b0490d931176ed152aaddc089824c03d1e490b44160e2
  task: representation_probing
  value: 5.6
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 71.6
  dataset: SpaceNet v1
  direction: better
  id: reed2022scale#c2
  label_ratio: null
  locator: Table 4
  metric: miou
  model: scalemae
  span: 'Sup. (Scratch)

    ViT-Large

    PSANet

    74.7'
  span_sha256: 1feaea5939e52b265cdf6ed8cfa21fe2f99beead5f1ade7e9bbdf4a28830ab5d
  task: semantic_segmentation
  value: 78.9
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 71.55
  dataset: FMoW-RGB
  direction: better
  id: reed2022scale#c3
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: scalemae
  span: 'GASSL [4]

    ResNet-50

    71.55/-'
  span_sha256: 2515b0baae708304dd3922948e6e99aa90115087fa1acaca3d8d78f0080ea150
  task: representation_probing
  value: 77.9
date: '2022-12-30'
doi: 10.48550/arxiv.2212.14532
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:25:39.486519Z'
key: reed2022scale
limitations:
- benchmark_narrowness
- spatial_transfer
- compute_cost
models:
- scalemae
proposed_tags:
- scale_aware_positional_encoding
- laplacian_pyramid_decoder
- gsd_conditioning
- multiscale_kNN_evaluation
regions:
- global
self_evaluation: true
tasks:
- land_cover_classification
- semantic_segmentation
- representation_probing
title: 'Scale-MAE: A Scale-Aware Masked Autoencoder for Multiscale Geospatial Representation
  Learning'
venue: arXiv
---

## summary

Scale-MAE introduces a Ground Sample Distance (GSD)-based positional encoding and a Laplacian-pyramid decoder into the Masked Autoencoder framework to explicitly learn scale-aware, multiscale representations for remote sensing imagery. Pretrained on FMoW-RGB with a ViT-Large backbone, it outperforms SatMAE and ConvMAE on kNN classification across eight datasets and on SpaceNet semantic segmentation, with gains growing at coarser GSDs.

## setup

ViT-Large pretrained on FMoW RGB (363.6k images) for 800 epochs; evaluated via frozen-encoder kNN classification on eight land-use datasets at multiple synthetically downsampled GSDs, plus linear probing/finetuning on RESISC-45 and FMoW-RGB, and UperNet semantic segmentation transfer on SpaceNet v1/v2, INRIA, and GID-15.

## caveats

Authors note Scale-MAE cannot handle input bands with differing GSDs or SAR imagery, has higher GPU memory usage than vanilla MAE despite fewer decoder parameters, and evaluation is limited to a curated set of ten datasets chosen for scale diversity rather than the full breadth of available remote sensing benchmarks.
