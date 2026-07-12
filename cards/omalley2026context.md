---
arxiv_id: '2605.16665'
authors:
- Daniel O'Malley
- Christopher W. Johnson
- Javier E. Santos
- Pablo Lara
- Sandro Malusà
- Bharat Srikishan
- John Kath
- Arnab Mazumder
- Mohamed Mehana
- David Coblentz
- Nathan DeBardeleben
- Earl Lawrence
- Hari Viswanathan
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G6_compactness
- G7_interpretability
- G8_uncertainty
claims: []
date: '2026-05-15'
doi: 10.48550/arxiv.2605.16665
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:38:44.092790Z'
key: omalley2026context
limitations:
- uncertainty
- spatial_transfer
- data_bias
models:
- alphaearth
proposed_tags:
- subsurface_temperature_prediction
- geothermal_resource_assessment
- in_context_learning
- borehole_data
- universal_kriging_baseline
- world_model_representation
- calibration
- physics_informed_baseline
- mean_absolute_error_metric
regions:
- us
- ca
- au
- gb
self_evaluation: false
tasks:
- representation_probing
title: In-context learning enables continental-scale subsurface temperature prediction
  from sparse local observations
venue: arXiv
---

## summary

In-Context Earth is an encoder-only transformer that uses sparse local borehole temperature observations as in-context conditioning to predict continental-scale subsurface temperature-at-depth with calibrated uncertainty. In the contiguous US it achieves an MAE of 4.7 °C, outperforming the Stanford Thermal Model, an AlphaEarth-embeddings model, Transparent Earth, and universal kriging, and transfers without finetuning to Alberta, Australia, and the UK using only 20 local observations. Interpretability analyses show its internal representations linearly encode unobserved subsurface properties (seismic velocities, geochemistry, crustal structure) and use them in physically consistent ways.

## setup

Trained on a compilation of contiguous-US borehole bottomhole temperature measurements with a 90/10 train/validation split, using M=20 nearest-neighbor context points selected via KD-tree and Earth-tailored data augmentation; temperature is binned into 128 discrete bins and predicted as an ordinal-classification distribution. Out-of-distribution testing uses frozen weights on independent datasets from Alberta (Canada), Australia (OZTemp), and the UK (UKOGL), with MAE as the error metric and PIT/KS statistics for calibration.

## caveats

The authors note predictive uncertainty systematically increases with depth due to sparser deep training data, that overall performance is bounded by the representativeness of training temperature patterns so some out-of-distribution regions could still confound the model, that the method requires in-context observations (not prediction in a vacuum), and that the most extreme UK/Australia residuals stem from data-quality issues (measured-while-drilling, assigned temperatures, depth errors).
