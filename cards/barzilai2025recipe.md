---
arxiv_id: '2503.08722'
authors:
- Aviad Barzilai
- Yotam Gigi
- Amr Helmy
- Vered Silverman
- Yehonathan Refael
- Bolous Jaber
- Tomer Shekel
- George Leifman
- Genady Beryozkin
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 33.33
  dataset: RSITMD
  direction: better
  id: barzilai2025recipe#c1
  label_ratio: null
  locator: Table 1
  metric: accuracy
  model: geoclip
  span: 38.64 39.85
  span_sha256: 1b11363b3037081b3ab4d6bb6425ec2d791f59f480b1454d9245cfe728c6a7b7
  task: representation_probing
  value: 42.63
date: '2025-03-10'
doi: 10.48550/arxiv.2503.08722
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:05:04.821958Z'
key: barzilai2025recipe
limitations:
- benchmark_narrowness
- human_semantics
models:
- geoclip
- satclip
proposed_tags:
- VLM
- MaMMUT
- zero_shot_cross_modal_retrieval
- image_text_retrieval
- zero_shot_classification
- pseudo_labeling_segmentation
- RemoteCLIP
- SkyScript
- GeoRSCLIP
- GeoChat
- LHRS-Bot
- PIR-ITR
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: A Recipe for Improving Remote Sensing VLM Zero Shot Generalization
venue: arXiv
---

## summary

The paper introduces two new remote-sensing image-caption datasets (RS-WebLI from filtered web images, RS-Landmarks with Gemini-generated captions from Google Maps) used to fine-tune the MaMMUT VLM, achieving state-of-the-art zero-shot cross-modal retrieval and classification on public RS benchmarks. It also proposes a self-supervised iterative pseudo-labeling scheme with a Smooth-Attention-Operation to distill image-level VLM knowledge into patch-level segmentation ability.

## setup

Models (MT-WebLI, MT-RSWebLI, MT-RSLandmarks, MT-RSWebLI-RSLandmarks) are evaluated via nearest-neighbor zero-shot image-text retrieval on RSICD, UCM Captions, NWPU, and RSITMD (Table 1), and zero-shot classification on FMOW, SkyScript, RESISC45, UCM Classification, and AID (Table 3), compared against RemoteCLIP, SkyScript, GeoRSCLIP, GeoChat, LHRS-Bot and PIR-ITR baselines.

## caveats

The authors note the localization/segmentation work is ongoing and preliminary, attention maps are noisy requiring the proposed Smooth-Attention-Operation to mitigate, and prior RS-VLM efforts (and by extension their own) remain constrained by dataset scale and semantic diversity.
