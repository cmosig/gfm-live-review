---
arxiv_id: '2601.01558'
authors:
- Pengfei Qu
- Wenyu Ouyang
- Chi Zhang
- Yikai Chai
- Shuolong Xu
- Lei Ye
- Yongri Piao
- Miao Zhang
- Huchuan Lu
axes:
- G1_label_rich_parity
- G3_spatial_transfer
- G4_temporal_transfer
- G6_compactness
- G7_interpretability
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.706
  dataset: CAMELS
  direction: parity
  id: qu2026utilizing#c1
  label_ratio: null
  locator: Sec 6
  metric: nse
  model: alphaearth
  span: median NSE values of 0.708 for the AEF embeddings and 0.706 for the model
    using CAMELS attributes
  span_sha256: 22fc6f4527d934be973d362d0732156cbe0537028437d31af703ba943e8d5502
  task: hydrological_modeling
  value: 0.708
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.553
  dataset: CAMELS
  direction: better
  id: qu2026utilizing#c2
  label_ratio: null
  locator: Sec 6
  metric: nse
  model: alphaearth
  span: the median NSE of the AEF embeddings rose to 0.612, while the model relying
    on CAMELS attributes reached only 0.553
  span_sha256: 23f8f1e9265630dac95c60394d21f7c142c7fdb95ecce392a4112a2bd451507d
  task: hydrological_modeling
  value: 0.612
date: '2026-01-04'
doi: null
doi_status: no_doi_found
extractor_version: '1'
ingested_at: '2026-07-12T16:42:58.547763Z'
key: qu2026utilizing
limitations:
- temporal_transfer
- spatial_transfer
- interpretability
- benchmark_narrowness
models:
- alphaearth
proposed_tags:
- prediction_in_ungauged_basins
- streamflow_prediction
- rainfall_runoff_modeling
- donor_basin_selection
- basin_similarity
- regionalization
- LSTM
- satellite_embeddings
- subsurface_heterogeneity
- granularity_generalization_tradeoff
- mutual_information_analysis
regions:
- us
self_evaluation: false
tasks:
- hydrological_modeling
title: Utilizing Earth Foundation Models to Enhance the Simulation Performance of
  Hydrological Models with AlphaEarth Embeddings
venue: arXiv
---

## summary

The study evaluates 64-dimensional AlphaEarth Foundation (AEF) satellite embeddings as static basin descriptors for streamflow prediction in the CAMELS-US dataset. AEF embeddings match CAMELS attributes in-sample but are more robust out-of-sample and enable better similarity-based donor-basin selection for prediction in ungauged basins. However, AEF's high discriminative power hurts cross-regime extrapolation, and excessively large heterogeneous donor pools reduce accuracy.

## setup

All 671 CAMELS-US basins with daymet meteorological forcings were used to train LSTM models comparing 17 CAMELS attributes versus 64-dim AEF embeddings, evaluated by NSE/KGE under in-sample and spatial out-of-sample settings with five seeds and five-fold cross-validation. Experiment B ranked donors for 150 target basins via cosine similarity (attributes, MLP fusion embeddings, AEF) across pool sizes k in {100..600, all 670}.

## caveats

The authors flag that the AEF embedding period (2017-2024) does not overlap the streamflow record (1980-2014), a temporal inconsistency; that surface-based embeddings miss subsurface heterogeneity, creating a granularity-generalization trade-off that weakens cross-regime extrapolation; and that findings are limited to CAMELS-US reference basins with minimal human disturbance, leaving global generalization an open question.
