---
arxiv_id: '2601.16900'
authors:
- Madeline C. Lisaius
- Srinivasan Keshav
- Andrew Blake
- Clement Atzberger
axes:
- G1_label_rich_parity
- G4_temporal_transfer
- G5_cost
- G6_compactness
- G10_human_semantics
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.946
  dataset: JECAM Senegal (2018)
  direction: better
  id: lisaius2026embedding#c1
  label_ratio: null
  locator: Table 7
  metric: accuracy
  model: tessera
  span: 0.965 ±\pm 0.007
  span_sha256: f20bad856dbbee2890a9acaa64bed9c74c117c2d05a9bafee69f56f5632411fa
  task: land_cover_classification
  value: 0.965
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.786
  dataset: JECAM Senegal (2018, 5 crops)
  direction: better
  id: lisaius2026embedding#c2
  label_ratio: null
  locator: Table 12
  metric: accuracy
  model: tessera
  span: 0.846 ±\pm 0.033
  span_sha256: 06b71b1c92d36f869c61dc0cf5203256853e44306553e0e66a6076039260a680
  task: crop_type_mapping
  value: 0.846
- axis: G1_label_rich_parity
  baseline: alphaearth
  baseline_value: 0.784
  dataset: JECAM Senegal (2018, 5 crops)
  direction: better
  id: lisaius2026embedding#c3
  label_ratio: null
  locator: Table 12
  metric: accuracy
  model: tessera
  span: 0.846 ±\pm 0.033
  span_sha256: 06b71b1c92d36f869c61dc0cf5203256853e44306553e0e66a6076039260a680
  task: crop_type_mapping
  value: 0.846
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.647
  dataset: JECAM Senegal (2019, 5 crops)
  direction: better
  id: lisaius2026embedding#c4
  label_ratio: null
  locator: Table 12
  metric: accuracy
  model: tessera
  span: 0.694 ±\pm 0.045
  span_sha256: 69b20c16f694c3e8709e4eebc20bbd8317665154683652cccd5b37aa42e7321e
  task: crop_type_mapping
  value: 0.694
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.516
  dataset: JECAM Senegal (2021, 8 crops)
  direction: better
  id: lisaius2026embedding#c5
  label_ratio: null
  locator: Table 12
  metric: accuracy
  model: tessera
  span: 0.567 ±\pm 0.036
  span_sha256: efcddfd0307f986ecdda183dbf132dbb0c4cbcf4f4055aa315c98106eb3d7c9b
  task: crop_type_mapping
  value: 0.567
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.172
  dataset: JECAM Senegal (train 2018, predict 2019)
  direction: better
  id: lisaius2026embedding#c6
  label_ratio: null
  locator: Table 13
  metric: accuracy
  model: tessera
  span: 0.626 ±\pm 0.001
  span_sha256: 838d8ffd5c0c468cc6a591b014b06ec5ebf9467fdc41f350db2baf794abe356a
  task: crop_type_mapping
  value: 0.626
- axis: G4_temporal_transfer
  baseline: alphaearth
  baseline_value: 0.364
  dataset: JECAM Senegal (train 2018, predict 2019)
  direction: better
  id: lisaius2026embedding#c7
  label_ratio: null
  locator: Table 13
  metric: accuracy
  model: tessera
  span: 0.626 ±\pm 0.001
  span_sha256: 838d8ffd5c0c468cc6a591b014b06ec5ebf9467fdc41f350db2baf794abe356a
  task: crop_type_mapping
  value: 0.626
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.187
  dataset: JECAM Senegal (train 2019, predict 2018)
  direction: better
  id: lisaius2026embedding#c8
  label_ratio: null
  locator: Table 13
  metric: accuracy
  model: tessera
  span: 0.555 ±\pm 0.001
  span_sha256: cf48e47619311bc839bfba5eb6b04106cfa1ea2b8da0b505f048a23478bbc482
  task: crop_type_mapping
  value: 0.555
- axis: G4_temporal_transfer
  baseline: task_specific
  baseline_value: 0.837
  dataset: JECAM Senegal (train 2018, predict 2021)
  direction: better
  id: lisaius2026embedding#c9
  label_ratio: null
  locator: Table 8
  metric: accuracy
  model: tessera
  span: 0.850 ±\pm 0.003
  span_sha256: a2dc0b6752f3f9da7963c568860c1e0cc02a068fbe9e0cf3322faea6aa8b32a7
  task: land_cover_classification
  value: 0.85
date: '2026-01-23'
doi: 10.48550/arxiv.2601.16900
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:47:56.657294Z'
key: lisaius2026embedding
limitations:
- spatial_transfer
- temporal_transfer
- data_bias
- mixed_pixels
- uncertainty
- benchmark_narrowness
- human_semantics
models:
- tessera
- alphaearth
proposed_tags:
- smallholder_agriculture
- intercropping
- west_africa
- spectral_temporal_metrics
- feature_engineering_free
- embedding_clustering_umap
- sentinel-1
- sentinel-2
regions:
- sn
self_evaluation: true
tasks:
- crop_type_mapping
- land_cover_classification
title: Embedding -based Crop Type Classification in the Groundnut Basin of Senegal
venue: arXiv
---

## summary

The paper evaluates TESSERA and AlphaEarth foundation-model embeddings against hand-engineered baselines (raw Sentinel-1/2 time series and spectral-temporal metrics) for land cover and crop type classification in the smallholder groundnut basin of Senegal. TESSERA best satisfies the authors' four criteria (performance, plausibility, transferability, accessibility), matching or exceeding baselines and showing strong temporal transfer, while AlphaEarth performs comparably for land cover but notably worse for crop type. Authored partly by the TESSERA creators, so this is a self-evaluation.

## setup

JECAM ground-truth polygons for Fatick/Niakhar (734 in 2018, 669 in 2019, 1870 in 2021) with land cover and crop labels were classified using ensembles of two best-performing heads (from RF, XGBoost, SVM, LR, MLP) over TESSERA, AlphaEarth, raw, and STM inputs. Ensembles were trained/evaluated 20 times with different seeds; temporal transfer trained on one year and predicted others (5 runs).

## caveats

Authors note the study covers only one Senegalese region (untested transferability to other smallholder areas), varying and lower-quality labels between years (especially 2019 and 2021) that degrade accuracy, inability to disentangle intercropped/secondary crops, and the absence of systematic spatial and per-crop error quantification; they also acknowledge large label-class overlap and high pretraining compute costs.
