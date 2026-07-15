---
arxiv_id: '2411.17000'
authors:
- Caleb S. Spradlin
- Jordan A. Caraballo-Vega
- Jian Li
- Mark L. Carroll
- Jie Gong
- Paul M. Montesano
axes:
- G5_cost
- G9_ecological_fine_scale
- G2_label_scarce_efficiency
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.2185
  dataset: CloudSat/CALIPSO curtain (ABI 3D cloud retrieval)
  direction: better
  id: spradlin2024satvision#c1
  label_ratio: null
  locator: Table 2
  metric: miou
  model: prithvi
  span: SVTOA-Giant 100M 0.4638 0.9574
  span_sha256: f212ac645d75a8966f4a29d7d4c9aadbb512b81f2c4d9a758262a344f0c561c9
  task: semantic_segmentation
  value: 0.4638
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.932
  dataset: CloudSat/CALIPSO curtain (ABI 3D cloud retrieval)
  direction: better
  id: spradlin2024satvision#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: prithvi
  span: achieving an mIOU of 0.4638 and accuracy of 0.9574 compared to the FCN baseline
  span_sha256: c7cdff387b752311b1478778075de88c87cee94e06c05de83645674be560e800
  task: semantic_segmentation
  value: 0.9574
date: '2024-11-26'
doi: 10.48550/arxiv.2411.17000
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:52:05.316895Z'
key: spradlin2024satvision
limitations:
- time_sensitivity
- benchmark_narrowness
- data_bias
models: []
proposed_tags:
- SatVision-TOA
- 3D_cloud_retrieval
- MODIS_TOA
- SwinV2
- masked_image_modeling
- all_sky_imagery
regions:
- global
self_evaluation: false
tasks: []
title: 'SatVision-TOA: A Geospatial Foundation Model for Coarse-Resolution All-Sky
  Remote Sensing Imagery'
venue: arXiv
---

## summary

The paper introduces SatVision-TOA, a 3-billion-parameter SwinV2 vision transformer pre-trained via masked image modeling on 100 million MODIS L1B Top-Of-Atmosphere image chips spanning all-sky (cloudy and clear) conditions. It achieves high image reconstruction fidelity (SSIM 0.9289) and, when fine-tuned on GOES-ABI data, substantially outperforms an FCN baseline on a 3D cloud retrieval downstream task. This is presented as the largest foundation model trained solely on satellite remote sensing imagery to date.

## setup

Pre-training used 100 million 128x128 pixel, 14-band MODIS TOA image chips (daily composites, ~270 days/year over 10 years, 2000-present) with 8x8 patch masking under the SimMIM framework and SwinV2 Giant architecture. The 3D cloud retrieval downstream task fine-tuned the pretrained encoder with an FCN decoder on 7000 training / 1300 validation ABI image chips labeled with CloudSat/CALIPSO vertical cloud masks, compared against an FCN trained from scratch with identical decoder and data.

## caveats

Authors note the model was trained only on daytime Terra-MODIS imagery at a fixed local time, limiting its ability to capture diurnal variations such as cloud life cycle; transferring to ABI required using unaligned channel matching and excluded full recalibration/re-gridding; and thin low clouds, deep convective clouds with cirrus above, and overlapping/multi-layer clouds remain especially hard to predict accurately.
