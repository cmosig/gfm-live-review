---
arxiv_id: '2411.17984'
authors:
- Huiyang Hu
- Peijin Wang
- Hanbo Bi
- Boyuan Tong
- Zhaozhi Wang
- Wenhui Diao
- Hao Chang
- Yingchao Feng
- Ziqi Zhang
- Yaowei Wang
- Qixiang Ye
- Kun Fu
- Xian Sun
axes:
- G1_label_rich_parity
- G5_cost
- G6_compactness
claims:
- axis: G1_label_rich_parity
  baseline: scalemae
  baseline_value: 65.77
  dataset: iSAID
  direction: better
  id: hu2024vheat#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: scalemae
  span: its 1.28% and 2.95% improvement over Scale-MAE
  span_sha256: 867fd889286f03c077b53f6b48d665c41a6af701c3e1a9757f86db7745ed340e
  task: semantic_segmentation
  value: 68.72
date: '2024-11-27'
doi: 10.48550/arxiv.2411.17984
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-16T00:05:43.389945Z'
key: hu2024vheat
limitations:
- compute_cost
- interpretability
models: []
proposed_tags:
- heat_conduction_operator
- object_detection
- image_classification
- multi_modal_optical_sar
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- change_detection
- land_cover_classification
title: 'RS-vHeat: Heat Conduction Guided Efficient Remote Sensing Foundation Model'
venue: arXiv
---

## summary

RS-vHeat is a heat-conduction-inspired multi-modal remote sensing foundation model that uses a Heat Conduction Operator with O(N^1.5) complexity and frequency-domain hierarchical masking for self-supervised pre-training on optical and SAR data. It is evaluated against attention-based and CNN-based RSFMs across semantic segmentation, object detection, change detection, and classification tasks on 10 datasets, showing competitive or superior accuracy with substantially lower memory, FLOPs, and higher throughput.

## setup

Pre-trained on ~3 million optical/SAR image pairs (450k matched pairs) following RingMo's methodology, using a Swin-B-configured heat-conduction visual encoder trained on 8 A100 GPUs for 200 epochs. Fine-tuned and evaluated on 10 datasets across semantic segmentation (Potsdam, iSAID, AIR-PolSAR-Seg, WHU-OPT-SAR), object detection (FAIR1M, DIOR, SAR-AIRcraft-1.0), change detection (LEVIR-CD), and classification (AID, NWPU-RESISC45).

## caveats

The authors note that Mamba-based architectures (a related efficient alternative) suffer from limited interpretability, and that prior RSFMs struggle to balance efficiency with large receptive fields and lack physical interpretability for how object features propagate, motivating their heat-conduction approach; many RSFMs also do not support SAR input, restricting fair comparison for those tasks.
