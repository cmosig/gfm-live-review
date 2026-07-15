---
arxiv_id: '2511.05461'
authors:
- Olivier Dietrich
- Merlin Alfredsson
- Emilia Arens
- Nando Metzger
- Torben Peters
- Linus Scheibenreif
- Jan Dirk Wegner
- Konrad Schindler
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G11_complementarity
- G5_cost
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.761
  dataset: xBD-S12 (xView2 split)
  direction: parity
  id: dietrich2025potential#c1
  label_ratio: null
  locator: Table 4
  metric: f1
  model: prithvi
  span: Prithvi achieves a slightly higher overall score than our 2-step model
  span_sha256: 4751af927106a600f6c21adf3cafe2d9cb99f7cbacba68554703773c579f21b7
  task: change_detection
  value: 0.764
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.71
  dataset: xBD-S12 (event-based split)
  direction: worse
  id: dietrich2025potential#c2
  label_ratio: null
  locator: Table 4
  metric: f1
  model: prithvi
  span: However, that performance plummets as one shifts to the event-based split
  span_sha256: 481225105ca6ce90c33e716cceac5140d05bcaafac8edb75af97f04105f97d5b
  task: change_detection
  value: 0.634
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.71
  dataset: xBD-S12 (event-based split)
  direction: worse
  id: dietrich2025potential#c3
  label_ratio: null
  locator: Table 4
  metric: f1
  model: dofa
  span: generalizing poorly to unseen events (respectively, locations)
  span_sha256: 910f844c2713927c8e3e1df2b922191be99b2ec0dccd5630b4d4f09e56f7210e
  task: change_detection
  value: 0.533
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.746
  dataset: Woolsey fire -> Santa Rosa fire
  direction: worse
  id: dietrich2025potential#c4
  label_ratio: null
  locator: Table 4
  metric: f1
  model: prithvi
  span: Overall, the U-Net maintains the best overall performance, driven by superior
    building localization
  span_sha256: 2d45ae0c74d9cac66a0dcaa2c9c0fbfd3d68293155c887c8356b3a826b89c2b0
  task: change_detection
  value: 0.725
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.143
  dataset: hurr. Michael -> hurr. Matthew
  direction: better
  id: dietrich2025potential#c5
  label_ratio: null
  locator: Table 4
  metric: f1
  model: prithvi
  span: For hurricanes, the two GeoFMs do achieve notable improvements over the U-Net
    baseline
  span_sha256: 6dde384140f8756e55cadc4a1ce07781132cd17141cdef35db1b9aec221cbc4e
  task: change_detection
  value: 0.271
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.143
  dataset: hurr. Michael -> hurr. Matthew
  direction: better
  id: dietrich2025potential#c6
  label_ratio: null
  locator: Table 4
  metric: f1
  model: dofa
  span: For hurricanes, the two GeoFMs do achieve notable improvements over the U-Net
    baseline
  span_sha256: 6dde384140f8756e55cadc4a1ce07781132cd17141cdef35db1b9aec221cbc4e
  task: change_detection
  value: 0.255
date: '2025-11-07'
doi: 10.48550/arxiv.2511.05461
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:44:53.113366Z'
key: dietrich2025potential
limitations:
- spatial_transfer
- benchmark_narrowness
- mixed_pixels
- compute_cost
models:
- prithvi
- dofa
proposed_tags:
- building_damage_assessment
- xBD-S12
- sentinel1_sentinel2_fusion
regions:
- gt
- us
- mx
- id
- np
self_evaluation: false
tasks:
- change_detection
- semantic_segmentation
title: 'The Potential of Copernicus Satellites for Disaster Response: Retrieving Building
  Damage from Sentinel-1 and Sentinel-2'
venue: arXiv
---

## summary

The paper introduces xBD-S12, a dataset pairing Sentinel-1/2 imagery with the xBD building damage benchmark, and shows that a simple U-Net achieves strong building damage segmentation at 10m GSD. It finds that architectural sophistication (e.g. ChangeMamba) overfits and generalizes poorly to unseen disasters, while geospatial foundation models (Prithvi, DOFA) as frozen feature extractors bring little practical benefit over a lightweight task-specific U-Net, especially under spatial transfer to new events.

## setup

xBD-S12 pairs 10,315 pre/post-disaster Sentinel-1 (VV/VH GRD) and Sentinel-2 (12-band L2A) image patches, spatiotemporally aligned to the xBD VHR damage-assessment dataset across 16 disasters, evaluated on both the original xView2 split and an event-based (geographically separated) split. Models are evaluated as 3-class semantic segmentation (background/intact/damaged) using F1 for localization and damage, with GeoFMs (Prithvi-EO-2.0-300M, DOFA-Base) used as frozen backbones with a finetuned UperNet decoder.

## caveats

Authors note the Mexico earthquake case shows a fundamental resolution limitation where sparse, small-scale damage is invisible at 10m GSD even to human interpreters; label simplification to 3 classes was needed since fine-grained damage classes are ambiguous at this resolution; GeoFMs' encoders were kept frozen due to compute cost, so full finetuning might change results; and the Palisades wildfire validation is only qualitative since ground truth data was not publicly available.
