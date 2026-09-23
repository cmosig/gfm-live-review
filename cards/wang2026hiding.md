---
arxiv_id: '2609.21363'
authors:
- Yining Wang
- Xi Li
- Mi Zhang
- Xiaohan Zhang
- Xiaoyu You
- Zhenxing Qian
- Mi Wen
axes:
- G7_interpretability
- G8_uncertainty
claims: []
date: '2026-09-18'
doi: 10.48550/arxiv.2609.21363
doi_status: verified
extractor_version: '1'
ingested_at: '2026-09-23T00:07:09.290975Z'
key: wang2026hiding
limitations:
- human_semantics
- interpretability
- benchmark_narrowness
models:
- geoclip
proposed_tags:
- geolocation_privacy_protection
- diffusion_based_perturbation
- adversarial_defense
- vision_language_models
- jailbreak_attacks
regions:
- global
self_evaluation: false
tasks:
- representation_probing
title: 'Hiding in Plain Sight: A Diffusion-based Mitigation of Geolocation Privacy
  Leakage in Vision-Language Models'
venue: arXiv
---

## summary

This paper studies geolocation privacy leakage from multimodal large reasoning models (MLRMs) and proposes a diffusion-based latent-space perturbation framework guided by GeoCLIP to disrupt geolocation inference while preserving image fidelity. It also introduces an optional diffusion-based inpainting extension for coarser-grained (region/country-level) privacy protection.

## setup

Experiments use DoxBench and Street View image datasets evaluated against five commercial MLRM APIs (GPT-5, GPT-4.1, Claude Opus 4.5, Gemini 2.5 Pro, Qwen3-VL Plus), with GeoCLIP used as a surrogate model to guide adversarial perturbations during Stable Diffusion's reverse diffusion process.

## caveats

Authors note the method degrades fine-grained visual details like small text, coarse-grained (region/country-level) leakage persists as an open challenge, local inpainting still underperforms standard Stable Diffusion inpainting in defense strength, and robustness may decrease under full white-box adaptive attacks or advanced downstream pipelines (OCR, object recognition, specialized geolocation models).
