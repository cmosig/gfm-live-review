---
arxiv_id: '2511.04474'
authors:
- Wenwen Li
- Sizhe Wang
- Hyunho Lee
- Chenyan Lu
- Sujit Roy
- Rahul Ramachandran
- Chia-Yu Hsu
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 70.44
  dataset: Landslide4Sense
  direction: better
  id: li2025landslide#c1
  label_ratio: 1.0
  locator: Table 3
  metric: miou
  model: prithvi
  span: The 300M variant achieved the highest mIoU and F1 (71.30 / 60.70
  span_sha256: 65c31eaf8c3b3506ade6ac2efc8a9d8569bc28035208cfcbe59814ec43577f7d
  task: landslide_susceptibility
  value: 71.3
- axis: G1_label_rich_parity
  baseline: satmae
  baseline_value: 67.48
  dataset: Landslide4Sense
  direction: better
  id: li2025landslide#c2
  label_ratio: 1.0
  locator: Table 3
  metric: miou
  model: prithvi
  span: SatMAE (multi-spectral) underperformed with 67.48 mIoU and 53.72 F1
  span_sha256: bc2e9853986fdbc457daeb54f77566e23aaa2d8c46285239f9eaf24d9a638016
  task: landslide_susceptibility
  value: 71.3
- axis: G6_compactness
  baseline: task_specific
  baseline_value: 61.2
  dataset: Landslide4Sense
  direction: better
  id: li2025landslide#c3
  label_ratio: 1.0
  locator: Table 4
  metric: miou
  model: prithvi
  span: end-to-end tuning further increased performance to 73.62 mIoU and 65.42 F1
  span_sha256: 7441d20693c2e478723991b90a4ae86fbacbc5108ab6bea525e263bcc002028f
  task: landslide_susceptibility
  value: 73.62
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 59.7
  dataset: Landslide4Sense
  direction: better
  id: li2025landslide#c4
  label_ratio: 0.0125
  locator: Sec 4.4
  metric: miou
  model: prithvi
  span: At 1.25%1.25\% labels, Prithvi-EO-2.0-600M attains 66.96 mIoU, followed by
    Prithvi-300M at 64.45
  span_sha256: 35afc495446ae79c593c9445c419073db517be024b7cc75a20aeb08e909a465f
  task: landslide_susceptibility
  value: 66.96
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 58.23
  dataset: Landslide Reference
  direction: better
  id: li2025landslide#c5
  label_ratio: null
  locator: Table 6
  metric: miou
  model: prithvi
  span: 71.18 for Prithvi-EO-2.0-600M vs. 58.23 for U-Net
  span_sha256: e064e21ac451ce2ad6d2d0a4b2408d1ddc2aa35fc89f4e2b162a436144ef7443
  task: landslide_susceptibility
  value: 71.18
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 53.09
  dataset: GVLM-S2
  direction: better
  id: li2025landslide#c6
  label_ratio: null
  locator: Table 6
  metric: miou
  model: prithvi
  span: Both variants sustained around 70 mIoU on GVLM-S2, while U-Net and U-Net++
    dropped to the high-40s and low-50s
  span_sha256: 7275f0315d24c3bd02067c3e1e1ddf7c4f2b85da0453742b13c74ec2eb4e4569
  task: landslide_susceptibility
  value: 70.75
date: '2025-11-06'
doi: 10.48550/arxiv.2511.04474
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:44:15.683800Z'
key: li2025landslide
limitations:
- compute_cost
- benchmark_narrowness
- data_bias
- mixed_pixels
models:
- prithvi
- satmae
proposed_tags:
- band_adaptability
- mutual_information_band_selection
- landslide_type_vs_geography
regions:
- jp
- np
- tw
- in
- ie
- global
self_evaluation: false
tasks:
- landslide_susceptibility
title: 'Landslide Hazard Mapping with Geospatial Foundation Models: Geographical Generalizability,
  Data Scarcity, and Band Adaptability'
venue: arXiv
---

## summary

The paper systematically evaluates Prithvi-EO-2.0 for landslide mapping across sensor (band adaptability), label (data efficiency), and domain (geographic generalization) axes using the Landslide4Sense, Landslide Reference, and GVLM-S2 datasets. Prithvi consistently outperforms task-specific CNNs (U-Net, U-Net++), vision transformers (SegFormer, SwinV2-B), SAM-based TransLandSeg, and other GeoFMs (SatMAE, TerraMind) on segmentation quality, few-shot robustness, and cross-region/cross-dataset transfer. Lightweight nonlinear adapters and mutual-information-based band selection further improve adaptability to varied spectral inputs.

## setup

Landslide4Sense (4,844 128x128 patches, 14 channels of Sentinel-2 + ALOS PALSAR, standard train/val/test split) is used for baseline, band-adaptability, and data-efficiency experiments; Landslide Reference and an independently derived GVLM-S2 (Sentinel-2, geographically disjoint) are used for cross-domain generalization. Models are fine-tuned with Prithvi-EO-2.0 (300M/600M) encoder plus a lightweight convolutional decoder, using wCE/Lovász/focal losses and evaluated with mIoU, F1, precision, recall, mAcc.

## caveats

Authors note Prithvi-EO-2.0 requires substantially more compute/training time and technical expertise than lighter models like U-Net, lacks a fully developed operational segmentation pipeline (26% misclassification remains), and that reusable AI-ready landslide training data is scarce due to inconsistent metadata; they also flag that a hard test site (Irish peat landslides) distorted in-domain comparisons, showing landslide type can outweigh geography in generalization.
