---
arxiv_id: '2604.12159'
authors:
- Parth Parag Kulkarni
- Rohit Gupta
- Prakash Chandra Chhipa
- Mubarak Shah
axes:
- G3_spatial_transfer
- G4_temporal_transfer
- G7_interpretability
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: Mapillary (MSLS)
  direction: worse
  id: kulkarni2026vidtag#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: geoclip
  span: GeoCLIP[54]-FineTuned
  span_sha256: 2d437f39df59625d0a92e114799165a65b22890429418da547454da7a4f657e5
  task: representation_probing
  value: 22.5
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: GAMa (BDD100k)
  direction: worse
  id: kulkarni2026vidtag#c2
  label_ratio: null
  locator: Table 2
  metric: accuracy
  model: geoclip
  span: GeoCLIP[54]-FineTuned
  span_sha256: 2d437f39df59625d0a92e114799165a65b22890429418da547454da7a4f657e5
  task: representation_probing
  value: 28.3
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: CityGuessr68k
  direction: worse
  id: kulkarni2026vidtag#c3
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: geoclip
  span: GeoCLIP[54]
  span_sha256: b1af5a9767d3dfd075d96ab5053fb858fdde02498af05bc9b1f200c91721ba3c
  task: representation_probing
  value: 57.8
date: '2026-04-14'
doi: 10.48550/arxiv.2604.12159
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-13T08:19:46.587525Z'
key: kulkarni2026vidtag
limitations:
- benchmark_narrowness
- temporal_transfer
- compute_cost
models:
- geoclip
proposed_tags:
- video_geolocalization
- trajectory_prediction
- frame_to_gps_retrieval
- temporal_consistency
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: 'VidTAG: Temporally Aligned Video to GPS Geolocalization with Denoising Sequence
  Prediction at a Global Scale'
venue: arXiv
---

## summary

VidTAG introduces a dual-encoder (CLIP + DINOv2) frame-to-GPS retrieval framework for video geolocalization, with TempGeo for temporal alignment and GeoRefiner for denoising GPS predictions, evaluated on MSLS, GAMa, and CityGuessr68k. It outperforms GeoCLIP and other classification-based baselines by large margins across fine-grained and city-level thresholds.

## setup

Evaluations use Mapillary (MSLS) frame-level GPS sequences, GAMa (BDD100k-derived) video frames, and CityGuessr68k city-level video dataset, comparing against classification baselines (PlaNet, ISNs, GeoDecoder) and retrieval-based GeoCLIP (zero-shot and fine-tuned) using a uniform grid GPS gallery.

## caveats

Authors note performance depends heavily on gallery resolution (coarser galleries hurt accuracy, finer ones increase retrieval cost), and even at state-of-the-art the model has not reached satisfactory accuracy at sub-500m thresholds; failure analysis shows near-miss confusions among visually similar locales.
