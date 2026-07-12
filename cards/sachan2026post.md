---
arxiv_id: '2606.10658'
authors:
- Swati Sachan
- Dale Fickett
- Richard Buchinger
- Theo Miller
axes: []
claims: []
date: '2026-06-09'
doi: 10.1109/cai68641.2026.11536585
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:39:01.481578Z'
key: sachan2026post
limitations:
- uncertainty
models:
- prithvi
proposed_tags:
- post-quantum-cryptography
- federated-defi
- homomorphic-encryption
- dempster-shafer-fusion
- credit-lending
- land-fertility-classification
regions:
- us
self_evaluation: false
tasks: []
title: Post-Quantum Secure Federated DeFi for Inclusive Banking
venue: arXiv
---

## summary

This paper proposes a post-quantum secure federated DeFi framework using lattice-based FHE (RLWE/TRLWE) to let multiple banks jointly make lending decisions while keeping data encrypted. The server fuses encrypted local probabilistic assessments, human expert beliefs, and GFM-derived evidence (via Dempster-Shafer theory), using the pre-trained IBM-NASA Prithvi GFM to classify land fertility from satellite imagery as auxiliary evidence for agricultural lending decisions in rural Virginia.

## setup

A consortium of four regional Virginia banks ran a sandboxed pilot on agricultural lending; Prithvi (pre-trained, not fine-tuned or benchmarked) was applied to NASA HLS v2.0 imagery to classify land-fertility conditions into categories (moderate, high, low, open water, wetland) as one input signal fused with bank data and expert judgment.

## caveats

The authors note that homomorphically processed decision confidence remains slightly below that of unprocessed/plaintext-retrained model performance due to residual encrypted-decrypted noise inherent in the FHE computation.
