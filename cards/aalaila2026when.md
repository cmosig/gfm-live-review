---
arxiv_id: '2607.01082'
authors:
- Yahya Aalaila
- Mouad Elhamdi
- Gerrit Großmann
- Daniel Jenson
- Elizaveta Semenova
- Sebastian Vollmer
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G11_complementarity
claims: []
date: '2026-07-01'
doi: 10.48550/arxiv.2607.01082
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T17:35:07.021401Z'
key: aalaila2026when
limitations:
- benchmark_narrowness
- interpretability
models:
- alphaearth
proposed_tags:
- spatio_temporal_point_process
- log_gaussian_cox_process
- emergency_medical_services_forecasting
- event_demand_forecasting
- exogenous_spatial_context
- point_process_intensity
regions:
- us
self_evaluation: false
tasks: []
title: 'When Context Compensates for Sparse Event History: AlphaEarth for Spatio-Temporal
  Point-Process Forecasting'
venue: arXiv
---

## summary

The paper tests whether AlphaEarth (AE) embeddings, used as linear exogenous spatial context in a fixed log-Gaussian Cox process backbone, can compensate for sparse event history when forecasting emergency medical services (EMS) call demand under spatial transfer. Across eight held-out regions in Montgomery County, Pennsylvania, the AE-augmented model consistently improves out-of-region held-out predictive density over an event-only baseline for every history length, with the largest gains (~2-6x multiplicative) at 1-2 weeks of history, tapering to ~10-20% at 20-104 weeks. AE is shown to accelerate early intensity-level correction and produce smoother posterior spatial fields.

## setup

MontcoAlert 911 EMS dispatch incidents (2017-2020) in Montgomery County, PA, modeled as an LGCP with PriorVAE-reparameterized GP prior fit via SVI; spatial transfer evaluated over 8 disjoint spatial masks x 5 anchors in July 2020, sweeping history windows w in {1,...,104} weeks, using 64-d annual AE embedding slices strictly preceding each anchor. Held-out predictive performance is measured by ELPD and per-event log-density contrasts / multiplicative density ratios (mean 5.42x at 1 week, 2.37x at 2 weeks).

## caveats

The authors note evaluation relies on proper predictive scores (ELPD, per-event log-density) rather than operational/decision-facing outcomes, so probabilistic gains do not by themselves establish deployment value. They treat AE as a compact external representation without interpreting individual dimensions causally, and call for context-tailored importance measures; the study is confined to a single county and a transparent linear LGCP backbone, and across-mask uncertainty bands are descriptive rather than formal population intervals.
