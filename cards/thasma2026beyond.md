---
arxiv_id: '2606.29134'
authors:
- Sanjay Thasma
- Yu-Hsuan Ho
- Ali Mostafavi
axes:
- G3_spatial_transfer
- G5_cost
- G11_complementarity
claims:
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.041
  dataset: ImpactMesh-Flood (EMSR311 Hurricane Florence)
  direction: better
  id: thasma2026beyond#c1
  label_ratio: 1.0
  locator: Table I
  metric: miou
  model: alphaearth
  span: DINOv3 SAR+AE achieves the best Florence IoU (0.078)
  span_sha256: 1bb2be6133b178124628524e2a6543f0381cbfc7ddacb7dde6e47371c47b2306
  task: flood_mapping
  value: 0.078
- axis: G11_complementarity
  baseline: task_specific
  baseline_value: 0.103
  dataset: ImpactMesh-Flood (EMSR176 Louisiana floods)
  direction: better
  id: thasma2026beyond#c2
  label_ratio: 1.0
  locator: Sec III-C
  metric: miou
  model: alphaearth
  span: followed by DINOv3 SAR+AE (0.172)
  span_sha256: c8edeff7d15a9f99fb1a1ab8d0e51b6e1113954d2eb0bb75386ee99347d1c207
  task: flood_mapping
  value: 0.172
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: 0.046
  dataset: ImpactMesh-Flood (EMSR311 Hurricane Florence)
  direction: better
  id: thasma2026beyond#c3
  label_ratio: 1.0
  locator: Sec III-C
  metric: miou
  model: alphaearth
  span: 'the best mean IoU is 0.078 (DINOv3

    SAR+AE), followed by TerraMind SAR+AE (0.072)'
  span_sha256: ff6cfee0893b3c3a43e8c57b9518b5ab42138cee95177ecdae31f3a3a4fd6f0d
  task: flood_mapping
  value: 0.072
date: '2026-06-28'
doi: 10.48550/arxiv.2606.29134
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:36:24.348350Z'
key: thasma2026beyond
limitations:
- benchmark_narrowness
- spatial_transfer
- data_bias
- mixed_pixels
- time_sensitivity
- uncertainty
models:
- alphaearth
proposed_tags:
- SAR flood segmentation
- auxiliary land-cover prior
- DEM prior
- single-temporal post-event SAR
- multimodal fusion
- seed stability
- frozen backbone
- TerraMind
- DINOv3
- event-stratified split
- AlphaEarth embeddings as auxiliary input
regions:
- us
self_evaluation: false
tasks:
- flood_mapping
- semantic_segmentation
title: 'Beyond Backscatter: AlphaEarth Land-Cover Priors for Rapid SAR Flood Segmentation
  Across Foundation Backbones'
venue: arXiv
---

## summary

Using the CONUS subset of ImpactMesh-Flood, the paper evaluates whether stable land-context priors—learned AlphaEarth embeddings versus a Copernicus DEM—improve single-temporal post-event SAR flood segmentation across four backbones (from-scratch CNN UNet, ImageNet-UNet, frozen TerraMind, frozen DINOv3). Both auxiliary priors improve over SAR-only baselines on all backbones, with AlphaEarth exceeding DEM on the harder Florence event for every backbone (best Florence IoU 0.078) while DEM is competitive and best on Louisiana (0.198). AlphaEarth offers higher peak performance and higher recall but greater seed sensitivity, whereas DEM is more stable and cheaper.

## setup

Event-stratified split of the ImpactMesh-Flood CONUS subset (Sentinel-1 RTC VV/VH, 256x256 tiles): train on three Gulf/Atlantic hurricane events, validate on Central US floods, and test on held-out Florence (756 tiles) and Louisiana (336 tiles). Each of four backbones is run in SAR-only, SAR+DEM, and SAR+AE configurations under an identical fusion design, AdamW, weighted CE+Dice loss, model selection by validation flood-class IoU, with three seeds (42, 7, 19) for auxiliary configs.

## caveats

Authors flag: coarse Copernicus EMS labels cap achievable IoU; permanent water was not masked so some detections may be permanent water bodies; only two held-out test events, all within CONUS, limit cross-event/regional claims; SAR-only baselines are single-seed and small per-backbone AE-vs-DEM differences are indicative not confirmed (no significance testing); the single 2024 AlphaEarth layer reflects contemporary rather than at-event land conditions; and no comparison against operational baselines (thresholding, permanent-water masks, bi-temporal change detection).
