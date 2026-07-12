---
arxiv_id: '2101.07152'
authors:
- Ilie Sarpe
- Fabio Vandin
axes: []
claims: []
date: '2021-01-18'
doi: 10.48550/arxiv.2101.07152
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T19:01:41.860841Z'
key: sarpe2021presto
limitations: []
models:
- presto
proposed_tags:
- temporal_motif_counting
- graph_sampling
- concentration_inequalities
regions: []
self_evaluation: false
tasks: []
title: 'PRESTO: Simple and Scalable Sampling Techniques for the Rigorous Approximation
  of Temporal Motif Counts'
venue: arXiv
---

## summary

This paper introduces PRESTO, an algorithm for rigorously approximating temporal motif counts in temporal networks using uniform sampling of time windows, with two variants (PRESTO-A and PRESTO-E) that provide (ε,η)-approximation guarantees via Bennett's inequality. Experiments on networks up to 2.3 billion edges show PRESTO is more accurate and memory-efficient than prior sampling algorithms (LS, ES). This is a graph-algorithms paper unrelated to geospatial foundation models; the model key 'presto' appears in the tracked list but refers to an entirely different method (this PRESTO is a temporal motif counting algorithm, not the geospatial foundation model).

## setup

Evaluated on four temporal network datasets (Stackoverflow, Bitcoin, Reddit, EquinixChicago) with 12 motif topologies, comparing approximation error (MAPE) and memory usage against sampling baselines LS and ES under fixed running time.

## caveats

Authors note the exact enumerator subroutine has exponential worst-case complexity in motif edges, and PRESTO-A vs PRESTO-E performance depends on how skewed the edge timestamp distribution is.
