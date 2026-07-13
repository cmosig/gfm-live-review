---
arxiv_id: '2309.16020'
authors:
- Vicente Vivanco Cepeda
- Gaurav Kumar Nayak
- Mubarak Shah
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G10_human_semantics
- G11_complementarity
claims: []
date: '2023-09-27'
doi: 10.48550/arxiv.2309.16020
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:21:25.458537Z'
key: cepeda2023geoclip
limitations:
- compute_cost
- benchmark_narrowness
models:
- geoclip
proposed_tags:
- worldwide_geolocalization
- image_to_gps_retrieval
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: 'GeoCLIP: Clip-Inspired Alignment between Locations and Images for Effective
  Worldwide Geo-localization'
venue: arXiv
---

## summary

GeoCLIP is a CLIP-inspired image-to-GPS retrieval model for worldwide geo-localization that aligns image and GPS features via a hierarchical Random-Fourier-Feature location encoder, avoiding the fixed geographic classes used by prior classification-based approaches. It achieves state-of-the-art accuracy on Im2GPS3k, GWS15k, and YFCC26k benchmarks, and remains competitive even with only 20% of training data.

## setup

Trained on the 4.72M-image MP-16 dataset with a frozen CLIP ViT-L/14 image encoder and a novel hierarchical location encoder using equal earth projection and random Fourier features; evaluated via image-to-GPS retrieval against GPS galleries on Im2GPS3k, GWS15k, and YFCC26k, reporting % of predictions within 1/25/200/750/2500 km thresholds.

## caveats

Authors note precomputing CLIP image features on the large training set is time-consuming, and a single sigma value in the Random Fourier Features encoding is insufficient to perform well at both small and large spatial scales simultaneously (motivating their hierarchical approach).
