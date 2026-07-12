---
arxiv_id: '2406.13193'
authors:
- He Cao
- Yanjun Shao
- Zhiyuan Liu
- Zijing Liu
- Xiangru Tang
- Yuan Yao
- Yu Li
axes: []
claims: []
date: '2024-06-19'
doi: 10.48550/arxiv.2406.13193
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:56:07.198784Z'
key: cao2024presto
limitations: []
models:
- presto
proposed_tags:
- synthetic_chemistry
- reaction_prediction
- retrosynthesis
- reaction_condition_prediction
- reagent_selection
- reaction_type_classification
- yield_regression
- multimodal_LLM
- molecule_text_modeling
regions: []
self_evaluation: false
tasks:
- representation_probing
title: 'PRESTO: Progressive Pretraining Enhances Synthetic Chemistry Outcomes'
venue: arXiv
---

## summary

PRESTO is a progressive pretraining framework for multimodal LLMs that bridges molecule graph and text modalities via a two-stage pretraining (alignment then domain incremental pretraining) followed by supervised finetuning for synthetic chemistry tasks. It is not a tracked geospatial foundation model and evaluates no tracked GFM.

## setup

PRESTO uses a GIN molecule encoder pretrained by MoleculeSTM and Vicuna v1.5-7B as the base LLM, pretrained on PubChem captions, USPTO-Application interleaved molecule-text data, and name-conversion datasets, then evaluated on reaction prediction, reaction condition prediction, reagent selection, reaction type classification, and yield regression benchmarks with scaffold-based non-overlapping splits.

## caveats

The authors note PRESTO still underperforms in SMILES generation validity compared to domain expert models, is limited to generating only 1D sequence representations, and could benefit from replacing SMILES with SELFIES and expanding dataset diversity for dialogue capability.
