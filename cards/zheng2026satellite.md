---
arxiv_id: '2604.23166'
authors:
- Zhuo Zheng
- Iván Higuera-Mendieta
- Richard Lee
- David Newhouse
- Talip Kilic
- Stefano Ermon
- Marshall Burke
- David B. Lobell
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G1_label_rich_parity
- G5_cost
- G7_interpretability
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: null
  dataset: Malawi census
  direction: better
  id: zheng2026satellite#c1
  label_ratio: null
  locator: Results/Static and dynamic wealth measurement
  metric: r2
  model: tessera
  span: Tempov yields the highest coefficient of determination
  span_sha256: 28a9bc1d371935f1dc8d5bb92b7cfbc6ed031cb2b2577b725adb0c9593366b66
  task: wealth_mapping
  value: 0.87
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: null
  dataset: Malawi decadal census
  direction: better
  id: zheng2026satellite#c2
  label_ratio: null
  locator: Fig. 2a,b
  metric: r2
  model: tessera
  span: our model maintained robust predictive power (average 69% for Malawi and 46%
    for Mozambique
  span_sha256: 29dbb9130fb145c9eb6e97f8d34b3e7b2c5f11a78f32ef53af4200927ad49234
  task: change_detection
  value: 0.69
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: null
  dataset: Mozambique decadal census
  direction: better
  id: zheng2026satellite#c3
  label_ratio: null
  locator: Fig. 2a,b
  metric: r2
  model: tessera
  span: our model maintained robust predictive power (average 69% for Malawi and 46%
    for Mozambique
  span_sha256: 29dbb9130fb145c9eb6e97f8d34b3e7b2c5f11a78f32ef53af4200927ad49234
  task: change_detection
  value: 0.46
- axis: G4_temporal_transfer
  baseline: null
  baseline_value: null
  dataset: Malawi census hindcast
  direction: better
  id: zheng2026satellite#c4
  label_ratio: 0.05
  locator: Results/Wealth measurement in data-scarce environments
  metric: r2
  model: tessera
  span: Tempov reconstructs the past wealth distribution (R2=0.62R^{2}=0.62 and 0.510.51
    for Malawi 2008 and Mozambique 2007, respectively)
  span_sha256: 19f90513399a7d81adee90a8da1191d83dd06e78733d95ae48ffd62279cf47ea
  task: wealth_mapping
  value: 0.62
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: DHS Kenya/Nigeria/Bangladesh
  direction: better
  id: zheng2026satellite#c5
  label_ratio: null
  locator: Scalability to standardized DHS surveys
  metric: r2
  model: tessera
  span: achieving the highest R2R^{2} (average 0.66) among state-of-the-art geospatial
    foundation models
  span_sha256: b26c49aaac7f275a7c237b8d277cb6d1babd3e51d394fe7172a0f58451d50e86
  task: wealth_mapping
  value: 0.66
- axis: G3_spatial_transfer
  baseline: null
  baseline_value: null
  dataset: All-African DHS
  direction: parity
  id: zheng2026satellite#c6
  label_ratio: null
  locator: Continent-wide wealth maps for Africa
  metric: r2
  model: tessera
  span: achieves strong predictive accuracy (R2=0.63,r2=0.68R^{2}=0.63,r^{2}=0.68)
  span_sha256: 0fd70151300003f01d73e505cad541fd6a2117ea0ca8b87afc6830e92d377262
  task: wealth_mapping
  value: 0.63
- axis: G2_label_scarce_efficiency
  baseline: prithvi
  baseline_value: 0.36
  dataset: Malawi 2016 survey
  direction: better
  id: zheng2026satellite#c7
  label_ratio: 0.5
  locator: Supplementary Information C
  metric: r2
  model: tessera
  span: reaching an average R2R^{2} of 39%, which even exceeds the performance of
    Prithvi-v2 fine-tuned on 50% of survey data (average R2R^{2} of 36%)
  span_sha256: 4c319927a5a20ec40a2fa05c50460680928958b295378ce13b346c0b84ae992f
  task: wealth_mapping
  value: 0.39
date: '2026-04-25'
doi: 10.48550/arxiv.2604.23166
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:38:31.093264Z'
key: zheng2026satellite
limitations:
- temporal_transfer
- benchmark_narrowness
- data_bias
- time_sensitivity
- uncertainty
models:
- prithvi
- clay
- dofa
proposed_tags:
- tempov
- nowcasting
- hindcasting
- asset_wealth_index
- dhs_survey
- lora_finetuning
- bitemporal_ssl
- dinov3_rgb_sat
regions:
- mw
- mz
- ke
- ng
- bd
- global
self_evaluation: false
tasks:
- wealth_mapping
- poverty_mapping
- socioeconomic_estimation
- change_detection
- representation_probing
title: A satellite foundation model for improved wealth monitoring
venue: arXiv
---

## summary



## setup



## caveats


