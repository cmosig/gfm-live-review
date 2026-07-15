---
arxiv_id: '2605.12678'
authors:
- Isaac Corley
- Nils Lehmann
- Caleb Robinson
- Gabriel Tseng
- Anthony Fuller
- Hamed Alemohammad
- Evan Shelhamer
- Jennifer Marcus
- Hannah Kerner
axes:
- G12_openness
- G1_label_rich_parity
- G2_label_scarce_efficiency
claims:
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 33.0
  dataset: NWPU-RESISC45
  direction: better
  id: corley2026one#c1
  label_ratio: null
  locator: Sec 1 / Table 1
  metric: accuracy
  model: scalemae
  span: Scale-MAE’s linear-probed accuracy on NWPU-RESISC45 as 33.033.0 and 89.689.6
  span_sha256: 7a7f53b94f39ddbc42955e194568c59f96318559059e51bdd77803fdd1fc4bfa
  task: representation_probing
  value: 89.6
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 27.7
  dataset: m-Cashew
  direction: better
  id: corley2026one#c2
  label_ratio: null
  locator: Table 1
  metric: miou
  model: dofa
  span: DOFA [74] m-Cashew [41] mIoU / linear 3 27.7 56.4
  span_sha256: 93396ae4bd7a5a748e7702090fe5a403e6bd01d2745832806932eb7739aedb55
  task: semantic_segmentation
  value: 56.4
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 25.4
  dataset: m-SACropType
  direction: better
  id: corley2026one#c3
  label_ratio: null
  locator: Table 1
  metric: miou
  model: dofa
  span: DOFA [74] m-SACropType [41] mIoU / linear 3 25.4 51.3
  span_sha256: 67642c4746690b29231228063eb195a73dcc8bc51ca000484dcbe01638d3cbe4
  task: semantic_segmentation
  value: 51.3
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 31.8
  dataset: m-Cashew
  direction: better
  id: corley2026one#c4
  label_ratio: null
  locator: Table 1
  metric: miou
  model: croma
  span: CROMA [25] m-Cashew [41] mIoU / linear 3 31.8 62.2
  span_sha256: 907ff7d13812bd9679bb15e47bb14eb0579ab51557612922f71c32fd1331b8c2
  task: semantic_segmentation
  value: 62.2
- axis: G1_label_rich_parity
  baseline: null
  baseline_value: 54.5
  dataset: m-BigEarthNet
  direction: better
  id: corley2026one#c5
  label_ratio: null
  locator: Table 1
  metric: f1
  model: galileo
  span: AnySat [2] m-BigEarthNet [41] F1 / kNN 3 54.5 85.3
  span_sha256: 21c3ad2e7931e3345f5917acac26d44057982ccc07e22335d608107fb1a804f8
  task: representation_probing
  value: 85.3
date: '2026-05-12'
doi: 10.48550/arxiv.2605.12678
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-15T23:37:21.922501Z'
key: corley2026one
limitations:
- benchmark_narrowness
- interpretability
- data_bias
- uncertainty
models:
- croma
- dofa
- galileo
- presto
- satmae
- scalemae
proposed_tags:
- evaluation_reproducibility
- cross_paper_metric_divergence
- weight_release_audit
- pretraining_data_attribution
- evaluation_harness
regions:
- global
self_evaluation: true
tasks:
- representation_probing
- land_cover_classification
- crop_type_mapping
title: No One Knows the State of the Art in Geospatial Foundation Models
venue: arXiv
---

## summary

This is a meta-scientific position paper auditing 152 geospatial foundation model papers, finding severe inconsistencies in benchmark usage, reported metrics, weight release, and pretraining-data disclosure that make it impossible to determine the true state of the art. It documents 46 cross-paper disagreements of >=10 points for the same model/benchmark/protocol and proposes six recommendations for standardizing GFM evaluation.

## setup

The authors compiled a corpus of 152 GFM papers (2019-2025) via survey seeding plus citation-graph and keyword expansion, extracting structured metadata (models, benchmarks, pretraining data, weight release) via LLM-based extraction (Claude Opus 4.7, GPT 5.5 Codex) from LaTeX/Docling-converted sources with human verification. They analyze benchmark usage distribution, cross-paper metric divergence on fixed (model, benchmark, protocol) tuples, and pretraining dataset configuration overlap across papers.

## caveats

The authors note their analysis relies on LLM-based automated extraction and public APIs/data, which is subject to human error despite manual verification; they also acknowledge a stricter 'top papers only' filter could show different trends, and that variance for segmentation/regression decoders is rarely reported, remaining an open gap.
