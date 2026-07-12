---
arxiv_id: '2604.11444'
authors:
- Yongxiang Liu
- Jie Zhou
- Yafei Song
- Tianpeng Liu
- Li Liu
axes:
- G5_cost
claims: []
date: '2026-04-13'
doi: 10.48550/arxiv.2604.11444
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:43:28.795043Z'
key: liu2026huiyanearth
limitations:
- temporal_transfer
- time_sensitivity
models:
- alphaearth
proposed_tags:
- sar_image_generation
- diffusion_model
- generative_foundation_model
- geo_conditioned_generation
- scattering_mechanism_constraint
- data_augmentation
- controlnet
- lora_finetuning
regions:
- global
self_evaluation: false
tasks:
- land_cover_classification
title: 'HuiYanEarth-SAR: A Foundation Model for High-Fidelity and Low-Cost Global
  Remote Sensing Imagery Generation'
venue: arXiv
---

## summary

The paper introduces HuiYanEarth-SAR, a diffusion-based generative foundation model that produces global high-fidelity SAR imagery from geographic coordinates alone, using AlphaEarth geospatial embeddings as conditioning and implicit SAR scattering-mechanism constraints. It reports qualitative fidelity, ablations, a human visual deception study, and downstream SAR scene-classification augmentation gains. The model uses AlphaEarth only as a conditioning prior and is not itself one of the tracked geospatial foundation models.

## setup

A globally aligned multi-modal dataset was built from Sentinel-1 GRD, Sentinel-2 Harmonized, and 64-D AlphaEarth embeddings reprojected to 10 m and cropped to 512x512 patches; a Stable Diffusion U-Net with ControlNet and LoRA (rank 32) was trained on 8 NVIDIA 4090D GPUs. Evaluation used ablations (FSIM/SSIM/radiometric similarity), a hierarchical double-blind human study (24 participants), and a five-class SAR scene-classification downstream task with VGG/ResNet/ViT classifiers.

## caveats

The authors note limited output resolution and detail insufficient for fine-grained objects like individual buildings, reliance on static annual geographic embeddings that cannot model short-cycle dynamics such as flood evolution or rapid crop growth, and scattering enhancement that operates only at scene-category level, failing to capture subtle intra-class scattering variations from material, structure, or moisture.
