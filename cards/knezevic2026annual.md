---
arxiv_id: '2609.25731'
authors:
- Jovana Knezevic
- Clement Atzberger
- Zhengpeng Feng
- Adam F. A. Pellegrini
- Srinivasan Keshav
- David Coomes
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G4_temporal_transfer
- G11_complementarity
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.905
  dataset: HLS Burn Scars (single-fire subset, 559 chips)
  direction: better
  id: knezevic2026annual#c1
  label_ratio: null
  locator: Sec 4.2, Figure 4
  metric: f1
  model: tessera
  span: Tessera with the full U-Net achieved the strongest overall performance (F1
    = 0.916, IoU = 0.845)
  span_sha256: 7b9e48bb9c5ba70716d662ff8ebf6f1ec219087fbe6350b4f4ea29e2cf27d134
  task: semantic_segmentation
  value: 0.916
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: European EMSR fires 2024-2025 (88 fires)
  direction: parity
  id: knezevic2026annual#c2
  label_ratio: null
  locator: Sec 4.5, Table 5
  metric: f1
  model: tessera
  span: achieving micro F1 = 0.882 and IoU = 0.789
  span_sha256: f5c018ddf9136a0c2abe6088c47dd192df6f6718f8b535d4338fd384d53d0251
  task: semantic_segmentation
  value: 0.882
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: HLS Burn Scars (793 chips, annual-fire labels)
  direction: parity
  id: knezevic2026annual#c3
  label_ratio: null
  locator: Sec 4.3, Table 3
  metric: f1
  model: tessera
  span: Across 793 chips containing 1,162 distinct MTBS fires, the Tessera lightweight
    U-Net achieved F1 = 0.896
  span_sha256: 5c54fa9a8f7881100233a99c67cc34fb05f11735e165f9ce8f8b412e0b9a92b6
  task: semantic_segmentation
  value: 0.896
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.845
  dataset: HLS Burn Scars (PANGAEA protocol, single-fire subset)
  direction: better
  id: knezevic2026annual#c4
  label_ratio: null
  locator: Sec S8.2, Table S3
  metric: miou
  model: tessera
  span: Tessera with the lightweight U-Net (mIoU = 0.922, m-F1 = 0.959)
  span_sha256: 62db0143209f08ded699f39dd80aae1232cddaf475bfd73d54997f4c06d89e32
  task: change_detection
  value: 0.922
date: '2026-09-22'
doi: 10.48550/arxiv.2609.25731
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-25T00:04:45.157590Z'
key: knezevic2026annual
limitations:
- time_sensitivity
- spatial_transfer
- data_bias
models:
- tessera
- alphaearth
- prithvi
proposed_tags:
- burned-area-mapping
- annual-embeddings
- fire-timing-prediction
- wall-to-wall-mapping
regions:
- us
- gr
- es
- pt
self_evaluation: true
tasks:
- semantic_segmentation
- change_detection
- representation_probing
title: Annual Earth-observation embeddings encode wildfire disturbance and support
  simplified burned area mapping
venue: arXiv
---

## summary

Annual Tessera embeddings strongly encode wildfire disturbance, letting simple downstream models map burned area, matching or beating paired pre/post-fire HLS imagery. The approach transferred zero-shot across California and to European fires and recovered ignition timing (MAE 13 days for well-detected fires). AlphaEarth showed a much weaker disturbance signal.

## setup

HLS Burn Scars benchmark (793 chips, US 2018-2021) with MTBS-refined labels and spatially blocked 3-fold CV; California 2021 wall-to-wall evaluation against MTBS/CAL FIRE, GABAM and MCD64A1; 88 European EMSR fires from 2024-2025 for transfer. Downstream models were logistic regression, Random Forest and U-Nets on frozen embeddings.

## caveats

Recall drops for fires ignited late in the calendar year. Wall-to-wall deployment yields systematic false positives in snow-covered, mountainous, urban-fringe and agricultural areas. Annual embeddings also detect same-year fires missing from single-fire labels, and MTBS provides fire-level rather than pixel-level dates, so timing labels are noisy.
