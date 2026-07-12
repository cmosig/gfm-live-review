---
arxiv_id: '2604.16841'
authors:
- Yiheng Chen
- Zihui Ma
- Peishi Jiang
- Yilong Dai
- Qikai Hu
- Xinyue Ye
- Lingyao Li
- Rita Sousa
- Runlong Yu
axes:
- G11_complementarity
- G9_ecological_fine_scale
- G5_cost
claims:
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 0.3421
  dataset: HLS Landsat LST benchmark (Water)
  direction: better
  id: chen2026when#c1
  label_ratio: null
  locator: Table 5.1
  metric: rmse
  model: prithvi
  span: EFDiff-x0x_{0} reduces Water RMSE to 0.29∘\,{}^{\circ}C, a 16% improvement
    over the best non-EFM baseline
  span_sha256: 992b824bfb0853d1040c7366a6092c7e0cfebef5f2e12bbb017a361d309babba
  task: representation_probing
  value: 0.2892
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.5336
  dataset: HLS Landsat LST benchmark (Forest)
  direction: better
  id: chen2026when#c2
  label_ratio: null
  locator: Table 5.1
  metric: rmse
  model: prithvi
  span: EFDiff-x0x_{0}
  span_sha256: 75c5a790c35a67f4f1a6e28dce3a014ee0124ad4ace6580bfef758f7a86da632
  task: representation_probing
  value: 0.466
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.648
  dataset: HLS Landsat LST benchmark (Low Vegetation)
  direction: better
  id: chen2026when#c3
  label_ratio: null
  locator: Table 5.1
  metric: rmse
  model: prithvi
  span: EFDiff-x0x_{0}
  span_sha256: 75c5a790c35a67f4f1a6e28dce3a014ee0124ad4ace6580bfef758f7a86da632
  task: representation_probing
  value: 0.5629
date: '2026-04-18'
doi: 10.48550/arxiv.2604.16841
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:41:27.466134Z'
key: chen2026when
limitations:
- benchmark_narrowness
- compute_cost
- mixed_pixels
models:
- prithvi
proposed_tags:
- land_surface_temperature_super_resolution
- diffusion_model
- cross_attention_conditioning
- EFM_guided_generative_reconstruction
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: 'When Earth Foundation Models Meet Diffusion: An Application to Land Surface
  Temperature Super-Resolution'
venue: arXiv
---

## summary

The paper proposes EFDiff, a diffusion-based framework for extreme 32x LST super-resolution that uses a frozen Prithvi-EO-2.0 encoder to inject geospatial embeddings into a denoising UNet via cross-attention. Two variants, EFDiff-epsilon and EFDiff-x0, trade off perceptual realism versus pixel-level fidelity and both outperform deterministic, adversarial, and HLS-concatenation diffusion baselines on a globally diverse 242,416-patch Landsat benchmark. This is an application paper using Prithvi-EO-2.0 as a frozen conditioning encoder, not a foundation model paper itself.

## setup

Benchmark built from NASA HLS Landsat-only (HLSL30) six-band reflectance paired with Landsat Collection 2 ST_B10 LST, spanning 3,094 MGRS tiles (2,943 train/151 test) and 242,416 co-registered 256x256 patches (2014-2026), globally sampled via Prithvi-EO-2.0's stratified tile strategy. LR thermal inputs synthesized via Wald's protocol at 32x degradation (7x7 coarse field bicubically upsampled to 224x224); models predict the residual to the HR LST field and are evaluated separately by Forest/Low Vegetation/Water land-cover groups using RMSE, SSIM, LPIPS, and FID.

## caveats

Authors note perceptual metrics are notably worse over Water since spectrally uniform but thermally heterogeneous water surfaces give the Prithvi encoder less discriminative context; all models exhibit 7x7 checkerboard artifacts from the extreme 32x scale gap; EFDiff-epsilon incurs moderately higher pixel-wise error and heavier compute (1000-step native schedule) compared to EFDiff-x0's few-step efficiency.
