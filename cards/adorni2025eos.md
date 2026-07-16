---
arxiv_id: '2511.21523'
authors:
- Pierre Adorni
- Minh-Tan Pham
- Stéphane May
- Sébastien Lefèvre
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G5_cost
- G6_compactness
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 40.39
  dataset: Pangaea benchmark (avg across 11 datasets)
  direction: worse
  id: adorni2025eos#c1
  label_ratio: null
  locator: Table 1
  metric: miou
  model: prithvi
  span: UNet (∼\sim8M) [33]
  span_sha256: abc79ac2a89500d7c1e47bbe5c9598372b47f813ea77ede140136cc6b740055d
  task: semantic_segmentation
  value: 39.99
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 62.09
  dataset: SpaceNet7 Change Detection
  direction: worse
  id: adorni2025eos#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: croma
  span: SN7
  span_sha256: a294a8ec18166c737b09470c818d045996b7a5398247d123a0dc708e8f272bb9
  task: change_detection
  value: 59.28
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 40.39
  dataset: Pangaea benchmark (avg across 11 datasets, 10% labels)
  direction: better
  id: adorni2025eos#c3
  label_ratio: 0.1
  locator: Table 2
  metric: miou
  model: dofa
  span: using only 10% of the training data
  span_sha256: 6ccd4f8bc4976687df798219e24ae7c4f19272f175384bdcda35820ecd8537c8
  task: semantic_segmentation
  value: 46.03
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: null
  dataset: BioMassters
  direction: parity
  id: adorni2025eos#c4
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: scalemae
  span: BM ↓\downarrow
  span_sha256: d78d60d8e55973f929eee69724e08e6bf78e668e7daad5bc70014dee0b8c00eb
  task: biomass_estimation
  value: 47.15
date: '2025-11-26'
doi: 10.48550/arxiv.2511.21523
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:59:40.644318Z'
key: adorni2025eos
limitations:
- compute_cost
- benchmark_narrowness
- interpretability
models:
- prithvi
- scalemae
- croma
- dofa
proposed_tags:
- ensemble_of_specialists
- encoder_selection
- top_k_pruning
- Pangaea_benchmark
- Avg_DTB_metric
- feature_fusion
- federated_learning
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- crop_type_mapping
- flood_mapping
- change_detection
- biomass_estimation
- land_cover_classification
- representation_probing
title: 'EoS-FM: Can an Ensemble of Specialist Models act as a Generalist Feature Extractor?'
venue: arXiv
---

## summary

EoS-FM builds a remote sensing foundation model by ensembling many small, individually pretrained ConvNeXtV2-Atto specialist encoders with a learned top-k selection and fusion layer, rather than scaling a single large backbone. Evaluated on the Pangaea benchmark, it achieves the lowest Average Distance-To-Best across 11 tasks, matching TerraMind Large despite far fewer parameters, and retains this advantage under 10% label scarcity.

## setup

22 ConvNeXtV2-Atto encoders are trained individually on 17 torchgeo datasets across RGB, SAR, multispectral and IR modalities, then frozen and fused via a learned selection+1x1 conv layer; downstream evaluation follows the Pangaea benchmark protocol with a fine-tuned UperNet decoder on full and 10%-label regimes across 11 tasks including segmentation, change detection, crop mapping, flood mapping and biomass regression.

## caveats

Authors note the raw concatenation of all encoder features is too large for direct standalone embedding use, encoder selection choices are not always intuitively interpretable (e.g., on SpaceNet7 CD), inference throughput does not scale linearly with FLOPs due to scheduling overhead from combining many independent encoders, and the 22-encoder configuration was chosen arbitrarily rather than systematically optimized.
