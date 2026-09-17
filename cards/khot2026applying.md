---
arxiv_id: '2609.09429'
authors:
- Ayush Khot
- Wen Zhou
- Shaowen Wang
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G7_interpretability
- G11_complementarity
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.106
  dataset: Leefbaarometer (LBM)
  direction: better
  id: khot2026applying#c1
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: alphaearth
  span: aef 0.098
  span_sha256: ad94eb399af7e81fbc9952d4e9ea1497026494a157c87c62e3d462155e5d44c7
  task: socioeconomic_estimation
  value: 0.098
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.106
  dataset: Leefbaarometer (LBM)
  direction: worse
  id: khot2026applying#c2
  label_ratio: null
  locator: Table 1
  metric: rmse
  model: alphaearth
  span: probe-aef 0.116
  span_sha256: 6c353149070390f00f82a242733e7f96e98f75bbf92f91738a1a4a002be1ce81
  task: representation_probing
  value: 0.116
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: 0.078
  dataset: Leefbaarometer (LBM) - Beesel (rural)
  direction: worse
  id: khot2026applying#c3
  label_ratio: null
  locator: Table 2
  metric: rmse
  model: alphaearth
  span: aef 0.082
  span_sha256: 64222fb10082a9545727a2d199d0290d6f7bdc3243c02bab36bf757c2f36ef77
  task: socioeconomic_estimation
  value: 0.082
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.156
  dataset: Leefbaarometer (LBM) - RS ablation
  direction: better
  id: khot2026applying#c4
  label_ratio: null
  locator: Table 5
  metric: rmse
  model: alphaearth
  span: aef substantially reduces the RMSE penalty when RS is zeroed out (from 0.156
    to 0.112
  span_sha256: 64486276d048ecdc27678615940304ea66db0824d43c15fc7be5d72730e1dd8e
  task: socioeconomic_estimation
  value: 0.112
date: '2026-09-08'
doi: 10.1145/3841645.3843316
doi_status: unresolved
extractor_version: '1'
ingested_at: '2026-09-17T00:06:34.980692Z'
key: khot2026applying
limitations:
- spatial_transfer
- benchmark_narrowness
- interpretability
- data_bias
models:
- alphaearth
proposed_tags:
- urban_livability_evaluation
- AnySat
- TerraMind
- multimodal_fusion
- linear_probe
- Grad-CAM
- attention_entropy
regions:
- nl
self_evaluation: false
tasks:
- socioeconomic_estimation
title: Applying foundation model embeddings towards urban livability evaluation
venue: arXiv
---

## summary

The paper augments a transformer-based multimodal livability regression model (TMTMR) with AlphaEarth, AnySat, and TerraMind embeddings to predict Dutch urban livability scores. AlphaEarth consistently provides the strongest improvements, especially compensating for missing modalities like RS and POI, though rural generalization remains weaker unless embeddings are combined. Interpretability analysis via attention entropy and Full Grad-CAM shows AlphaEarth helps integrate cross-modal spatial context and semantic landmarks.

## setup

Models are trained/tested on the Leefbaarometer v3.0 dataset covering 13 Dutch cities (9 train/val, 4 held-out test cities) at 100m grid resolution, combining remote sensing, DSM, nighttime lights, POI text, and foundation model embeddings as inputs to predict six livability scores via RMSE.

## caveats

Authors note all results are limited to the Netherlands/LBM dataset with no validation of transfer to other regions; embeddings pretrained on predominantly urban data may not transfer cleanly to rural areas; RS remains the hardest modality to fully substitute; and combining embeddings' apparent complementarity could instead reflect noise-averaging rather than true complementary information.
