---
arxiv_id: '2608.04792'
authors:
- Ghjulia Sialellia
- Linus Scheibenreif
- Jan Dirk Wegner
- Konrad Schindler
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G9_ecological_fine_scale
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 53.73
  dataset: AGBD
  direction: better
  id: sialellia2026above#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: alphaearth
  span: fcn_film AEF 50.92
  span_sha256: 8647746554c70454d33b756155399a0a9050bac507930358f87fc1e8a9eec17f
  task: biomass_estimation
  value: 50.92
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 53.73
  dataset: AGBD
  direction: better
  id: sialellia2026above#c2
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: alphaearth
  span: fcn_film AEF+ 50.79
  span_sha256: b4b81ee0458590364d87784604670301799863bd548a473ced6872cae34e428f
  task: biomass_estimation
  value: 50.79
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 53.73
  dataset: AGBD
  direction: better
  id: sialellia2026above#c3
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: alphaearth
  span: MLP AEF 52.22
  span_sha256: 37c76b5e245c397606b44cd23db124111f2c4ea6abbd6d0bbf62f9f7fca2e3e8
  task: biomass_estimation
  value: 52.22
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 53.73
  dataset: AGBD Lite
  direction: worse
  id: sialellia2026above#c4
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: prithvi
  span: GFM (best) SSL4EO-MoCo S2 only 60.56
  span_sha256: dbe1cc77ccc7ea61f162fcdf34458ce555e55bbbe5d23f5a7d6609d43bc8b49a
  task: biomass_estimation
  value: 60.56
- axis: G2_label_scarce_efficiency
  baseline: prithvi
  baseline_value: 64.34
  dataset: AGBD Lite
  direction: better
  id: sialellia2026above#c5
  label_ratio: 0.05
  locator: Sec 6.2
  metric: rmse
  model: alphaearth
  span: a simple MLP reaches 53.91 Mg/ha on AEF embeddings
  span_sha256: 9a1de67384b33865bc20efd301d97297d0588c02fb502aab45c2e97415965e2e
  task: biomass_estimation
  value: 53.91
- axis: G2_label_scarce_efficiency
  baseline: prithvi
  baseline_value: 64.34
  dataset: AGBD Lite
  direction: better
  id: sialellia2026above#c6
  label_ratio: 0.05
  locator: Sec 6.2
  metric: rmse
  model: tessera
  span: and 59.79 Mg/ha on TESSERA embeddings
  span_sha256: e20d7a77792a4b465b319224df2606834cc7628a61a622de023f0ac9857f5539
  task: biomass_estimation
  value: 59.79
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 53.73
  dataset: AGBD
  direction: better
  id: sialellia2026above#c7
  label_ratio: 0.05
  locator: Sec 6.2
  metric: rmse
  model: alphaearth
  span: a 20-fold reduction in labels, at no cost in performance
  span_sha256: 147b5a53d07c6334468e7020b273fdbbf8776716566da248017aab3bf220cc27
  task: biomass_estimation
  value: 52.72
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 40.79
  dataset: AGBD (Africa, cross-region)
  direction: better
  id: sialellia2026above#c8
  label_ratio: null
  locator: Sec 5.2
  metric: rmse
  model: alphaearth
  span: AEF+ reduces RMSE from 40.79 to 33.72 Mg/ha (17.3%)
  span_sha256: b295777d7a5988c5d7c4b07891492363438be1a2314a57a1d7d3dd3f199348fd
  task: biomass_estimation
  value: 33.72
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 79.28
  dataset: AGBD (South Asia, cross-region)
  direction: worse
  id: sialellia2026above#c9
  label_ratio: null
  locator: Sec 5.2
  metric: rmse
  model: alphaearth
  span: AEF under cross-region produces an RMSE of 99.34 Mg/ha, 25% worse than AGBD
    (79.28 Mg/ha)
  span_sha256: 6895fb3dbe76644508449b881ad035610609ead14b4f73b1c1346013a0376d17
  task: biomass_estimation
  value: 99.34
- axis: G9_ecological_fine_scale
  baseline: task_specific
  baseline_value: 45.77
  dataset: AGBref
  direction: better
  id: sialellia2026above#c10
  label_ratio: null
  locator: Table 5 / Sec 5.5
  metric: rmse
  model: alphaearth
  span: ESA CCI has the smaller absolute bias on the All set
  span_sha256: 04a8bac88a14668b7e6d342b79fa5f6819972eead2969cad5826bdd79b5b7be3
  task: biomass_estimation
  value: 27.2
date: '2026-08-05'
doi: 10.48550/arxiv.2608.04792
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-07T00:17:31.760670Z'
key: sialellia2026above
limitations:
- benchmark_narrowness
- compute_cost
- data_bias
- spatial_transfer
- temporal_transfer
- mixed_pixels
models:
- prithvi
- croma
- dofa
- scalemae
- satmae
- alphaearth
- tessera
proposed_tags:
- above_ground_biomass_regression
- frozen_encoder_evaluation
- pre_computed_embedding_products
- PANGAEA_benchmark
- AGBD_dataset
- AGBref_reference_dataset
- ESA_CCI_biomass_comparison
- GEDI_L4A
regions:
- us
- cu
- gf
- py
- at
- gr
- gh
- tz
- nz
- np
- cn
- global
self_evaluation: false
tasks:
- biomass_estimation
title: Above-ground Biomass Estimation with Geospatial Foundation Models
venue: arXiv
---

## summary



## setup



## caveats


