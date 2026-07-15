---
arxiv_id: '2406.19888'
authors:
- Michal Muszynski
- Levente Klein
- Ademir Ferreira da Silva
- Anjani Prasad Atluri
- Carlos Gomes
- Daniela Szwarcman
- Gurkanwar Singh
- Kewen Gu
- Maciel Zortea
- Naomi Simumba
- Paolo Fraccaro
- Shraddha Singh
- Steve Meliksetian
- Campbell Watson
- Daiki Kimura
- Harini Srinivasan
axes:
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G3_spatial_transfer
claims:
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 65.5
  dataset: Brazil 2022 GEDI dataset (all eco-regions)
  direction: worse
  id: muszynski2024fine#c1
  label_ratio: null
  locator: Sec 5
  metric: rmse
  model: prithvi
  span: the U-Net slightly outperforms the GFMs by achieving an RMSE of 65.5 Mg/ha
    compared to 68.7 Mg/ha and 70.9 Mg/ha
  span_sha256: 83d6634b99aa2347e50486e38f7a86c03d46f1bc31b9f4f63d048f38ba6de9e6
  task: biomass_estimation
  value: 68.7
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 65.5
  dataset: Brazil 2022 GEDI dataset (all eco-regions)
  direction: worse
  id: muszynski2024fine#c2
  label_ratio: null
  locator: Sec 5
  metric: rmse
  model: prithvi
  span: the U-Net slightly outperforms the GFMs by achieving an RMSE of 65.5 Mg/ha
    compared to 68.7 Mg/ha and 70.9 Mg/ha
  span_sha256: 83d6634b99aa2347e50486e38f7a86c03d46f1bc31b9f4f63d048f38ba6de9e6
  task: biomass_estimation
  value: 70.9
date: '2024-06-28'
doi: 10.48550/arxiv.2406.19888
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:52:55.842696Z'
key: muszynski2024fine
limitations:
- benchmark_narrowness
- spatial_transfer
- mixed_pixels
models:
- prithvi
proposed_tags:
- Swin-B backbone
- GEDI labels
- eco-region transfer
regions:
- br
self_evaluation: false
tasks:
- biomass_estimation
title: Fine-tuning of Geospatial Foundation Models for Aboveground Biomass Estimation
venue: arXiv
---

## summary

The paper fine-tunes a Prithvi-based geospatial foundation model (Swin-B backbone) with a frozen encoder to estimate above-ground biomass (AGB) from HLS imagery across three Brazilian eco-regions, comparing it to a U-Net trained from scratch. The fine-tuned GFM achieves comparable RMSE to the U-Net despite using 13 times fewer tunable parameters (0.6M vs 7.8M). The study also examines generalization of the GFM across different eco-regions.

## setup

Uses GEDI aboveground biomass measurements from 2022 across three merged Brazilian eco-regions (EC1, EC2, EC3) paired with cloud-filtered Harmonized Landsat-8 Sentinel-2 (HLS) 6-band imagery; a Prithvi-style GFM with Swin-B encoder (frozen) and UPerNet+PixelShuffle decoder is fine-tuned per eco-region and compared against a U-Net baseline trained from scratch, evaluated via bin-wise RMSE on held-out validation data.

## caveats

Authors note the U-Net slightly outperforms the GFMs overall on RMSE, especially for moderate AGB bins (100-200 Mg/ha) in EC2/EC3, and that only sparse GEDI labels are available, limiting evaluation; they flag the need to test under more realistic conditions such as persistent cloud cover using radar in future work.
