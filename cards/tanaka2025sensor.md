---
arxiv_id: '2509.23035'
authors:
- Tomohiro Tanaka
- Narumasa Tsutsumida
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: prithvi
  baseline_value: 0.876
  dataset: Sen1Floods11
  direction: better
  id: tanaka2025sensor#c1
  label_ratio: null
  locator: Table 2
  metric: f1
  model: presto
  span: Ours (MS+SAR) 12 0.886 0.880 0.913 0.896
  span_sha256: ce5426ed89a8acf69cbc887b1b584cca218f7ee3d0fc482754da610314a46793
  task: flood_mapping
  value: 0.896
- axis: G1_label_rich_parity
  baseline: prithvi
  baseline_value: 0.867
  dataset: Sen1Floods11
  direction: better
  id: tanaka2025sensor#c2
  label_ratio: null
  locator: Table 2
  metric: miou
  model: presto
  span: Prithvi-100M 6 0.867 0.865 0.887 0.876
  span_sha256: 31b83bd9fe82d55069d4daf59546183886c6696dc505b9626e4c215110f713fd
  task: flood_mapping
  value: 0.886
- axis: G11_complementarity
  baseline: prithvi
  baseline_value: 0.876
  dataset: Sen1Floods11
  direction: better
  id: tanaka2025sensor#c3
  label_ratio: null
  locator: Table 2
  metric: f1
  model: presto
  span: Ours (MS) 10 0.884 0.881 0.906 0.893
  span_sha256: 875b2cd9258415797b6e2f6fc38ee5319306617654e9fd6d43276a7bd04ae3a6
  task: flood_mapping
  value: 0.893
- axis: G11_complementarity
  baseline: prithvi
  baseline_value: 0.876
  dataset: Sen1Floods11
  direction: worse
  id: tanaka2025sensor#c4
  label_ratio: null
  locator: Table 2
  metric: f1
  model: presto
  span: Ours (SAR) 2 0.736 0.826 0.636 0.718
  span_sha256: 1bcbef20e0a40c5f5e7290c700189083836a60da6f6626e8e5b48dc6a89af732
  task: flood_mapping
  value: 0.718
- axis: G6_compactness
  baseline: prithvi
  baseline_value: 0.876
  dataset: Sen1Floods11
  direction: better
  id: tanaka2025sensor#c5
  label_ratio: null
  locator: Abstract
  metric: f1
  model: presto
  span: F1 score of 0.896 and mIoU of 0.886 in the optimal sensor-fusion scenario
  span_sha256: b6c854b9a40fd640329c2f3201f6acfc9de43175a9cf1ad028838710f9d12dc3
  task: flood_mapping
  value: 0.896
date: '2025-09-27'
doi: 10.48550/arxiv.2509.23035
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:45:53.869624Z'
key: tanaka2025sensor
limitations:
- data_bias
- mixed_pixels
- benchmark_narrowness
models:
- presto
- prithvi
proposed_tags:
- sensor_flexibility
- SAR_MS_fusion
- channel_masking
regions:
- gh
- in
- pk
- py
- us
- bo
self_evaluation: false
tasks:
- flood_mapping
title: Sensor-Adaptive Flood Mapping with Pre-trained Multi-Modal Transformers across
  SAR and Multispectral Modalities
venue: arXiv
---

## summary

The paper fine-tunes Presto, a lightweight ~0.4M-parameter multi-modal transformer pre-trained on Sentinel-1 and Sentinel-2 data, for pixel-level flood mapping that flexibly handles SAR-only, MS-only, or combined inputs. On a Sen1Floods11 subset, the fine-tuned Presto outperforms the much larger Prithvi-100M baseline in MS+SAR and MS-only scenarios, while remaining functional but weaker in SAR-only conditions.

## setup

Models were trained on a curated Sen1Floods11 subset (six flood events, 50 train/20 val/15 test 512x512 chips) with S1/S2 acquisition dates within one day of each other, using focal loss and AdamW; evaluation used mIoU, precision, recall, and F1 across SAR-only, MS-only, and MS+SAR scenarios on a held-out Bolivia test set, compared against a Prithvi-100M baseline fine-tuned on HLS data.

## caveats

Authors note the SAR-only performance drop may partly reflect label bias since Sen1Floods11 ground truth is derived primarily from S2 imagery, unfairly penalizing SAR-detected water obscured by clouds in optical labels; pixel-wise predictions also show salt-and-pepper noise in SAR-only maps, and a processing artifact affected one test chip's SAR-inclusive predictions.
