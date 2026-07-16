---
arxiv_id: '2311.07113'
authors:
- Danfeng Hong
- Bing Zhang
- Xuyang Li
- Yuxuan Li
- Chenyu Li
- Jing Yao
- Naoto Yokoya
- Hao Li
- Pedram Ghamisi
- Xiuping Jia
- Antonio Plaza
- Paolo Gamba
- Jon Atli Benediktsson
- Jocelyn Chanussot
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G6_compactness
- G9_ecological_fine_scale
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: EuroSAT
  direction: better
  id: hong2023spectralgpt#c1
  label_ratio: null
  locator: Table I / Sec 3.1
  metric: accuracy
  model: satmae
  span: achieving an impressive accuracy of 99.15%
  span_sha256: 4fb47e6be0b4b64edcbe3aeb9f22c00e6dddf590aff5fa7e2d1089c68e90c6d4
  task: land_cover_classification
  value: 99.15
- axis: G2_label_scarce_efficiency
  baseline: satmae
  baseline_value: 85.21
  dataset: BigEarthNet
  direction: better
  id: hong2023spectralgpt#c2
  label_ratio: 0.1
  locator: Table II
  metric: accuracy
  model: satmae
  span: our SpectralGPT model outperforms them by 0.84% (0.82%) and 0.71% (0.68%)
  span_sha256: f20570207cf46e2ed261e1995a9cdb894456043ec08a8ced1d2137a5ce8571c6
  task: land_cover_classification
  value: 86.03
- axis: G9_ecological_fine_scale
  baseline: satmae
  baseline_value: 48.7
  dataset: SegMunich
  direction: better
  id: hong2023spectralgpt#c3
  label_ratio: null
  locator: Table III
  metric: miou
  model: satmae
  span: a significant lead with a 1.1% (2.3%) higher mIoU than the second-best result
  span_sha256: d64e4c1f5f0365520f118e66dcd9a99e9e711952641c72335d2e417fd4ef8551
  task: semantic_segmentation
  value: 49.8
- axis: G1_label_rich_parity
  baseline: satmae
  baseline_value: 52.76
  dataset: OSCD
  direction: better
  id: hong2023spectralgpt#c4
  label_ratio: null
  locator: Table IV
  metric: f1
  model: satmae
  span: surpassing the second-best model (i.e., SatMAE) by a substantial margin of
    0.75% (1.53%)
  span_sha256: e0ea78c4fb8529418782318c1eb968c4fb455da7e793e0e0196803f0253ee387
  task: change_detection
  value: 53.51
date: '2023-11-13'
doi: 10.1109/tpami.2024.3362475
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:07:46.662192Z'
key: hong2023spectralgpt
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
- spatial_transfer
models:
- satmae
proposed_tags:
- 3d_spectral_masking
- multi_target_reconstruction
- progressive_pretraining
- spectral_reconstruction_fidelity
regions:
- global
- de
self_evaluation: false
tasks:
- land_cover_classification
- semantic_segmentation
- change_detection
- representation_probing
title: 'SpectralGPT: Spectral Remote Sensing Foundation Model'
venue: arXiv
---

## summary

SpectralGPT is a 3D generative pretrained transformer foundation model purpose-built for spectral (multi-band) remote sensing data, using 3D cube masking (90% masking rate) and multi-target reconstruction on over one million Sentinel-2 images. It is progressively pretrained on fMoW-S2 then BigEarthNet-S2, scaling to 600M+ parameters, and outperforms SatMAE, ViT, ResNet50, and SeCo baselines on scene classification, semantic segmentation, and change detection.

## setup

Pretrained on fMoW-S2 (712,874 images, 62 classes) and BigEarthNet-S2 (354,196 images, 19 classes) Sentinel-2 12-band imagery using a ViT-based MAE architecture with 3D spatial-spectral tokens. Evaluated via fine-tuning on EuroSAT (single-label classification), BigEarthNet-S2 (multi-label classification, 10% labels), a newly curated SegMunich dataset (13-class semantic segmentation), and OSCD (change detection).

## caveats

The authors note SpectralGPT achieves higher F1/recall but lower precision on change detection due to extreme class imbalance and potential overfitting of the complex ViT architecture to limited fine-tuning data; they also note raw (non-normalized) reconstruction targets and shallow decoders degrade performance, and larger token sizes reduce fine-grained spatial detail.
