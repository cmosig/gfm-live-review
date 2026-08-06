---
arxiv_id: '2608.03804'
authors:
- Robin Young
- Artyom Gabtraupov
- Kenzy Soror
- Srinivasan Keshav
axes:
- G5_cost
- G7_interpretability
- G8_uncertainty
- G12_openness
claims: []
date: '2026-08-04'
doi: 10.48550/arxiv.2608.03804
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-06T00:16:51.737818Z'
key: young2026how
limitations:
- compute_cost
- interpretability
- uncertainty
- benchmark_narrowness
- data_bias
models:
- prithvi
- scalemae
- satmae
- dofa
- presto
- galileo
- croma
- alphaearth
- tessera
proposed_tags:
- usability_evaluation
- access_deployment
- interaction_customization
- trust_transparency
- community_support
- scientific_permanence
- multilingual_support
- offline_usability
- inter_rater_reliability
regions:
- global
self_evaluation: true
tasks: []
title: How Usable Are Geospatial Foundation Models? A Systematic Evaluation of 89
  Models
venue: arXiv
---

## summary

This paper introduces a seven-dimension HCI-grounded usability evaluation framework for geospatial foundation models (GeoFMs), motivated by a pilot expert elicitation survey with 11 ecology/conservation researchers. Two calibrated raters applied the framework to 89 GeoFMs, finding that nearly a third provide no usable access beyond source code, and that trust-building features like uncertainty quantification are almost universally absent despite being the top priority for domain experts.

## setup

89 GeoFMs were sourced from four existing surveys (Feng et al. 2026, Zhu et al. 2026, Lu et al. 2025b, Xiao et al. 2025) and evaluated by two raters between October 2025 and January 2026 across seven dimensions: Access & Deployment, Interaction & Customization, Trust & Transparency, Community & Support, Scientific Permanence & Reproducibility, Multilingual Support, and Offline Usability. Inter-rater reliability was computed on a 20-model calibration sample using Cohen's Kappa and Gwet's AC1.

## caveats

The authors note the pilot survey (N=11) is exploratory and cannot support strong claims; the 89-model corpus is bounded by an October 2025–January 2026 evaluation window and the four source surveys, so it is not exhaustive; and dimensions with low variance (e.g. Trust, Multilingual, Offline) may reflect field-wide uniformity rather than framework insensitivity, though the authors acknowledge this is difficult to fully disentangle.
