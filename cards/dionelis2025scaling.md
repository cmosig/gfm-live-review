---
arxiv_id: '2506.14765'
authors:
- Nikolaos Dionelis
- Riccardo Musto
- Jente Bosmans
- Simone Sarti
- Giancarlo Paoletti
- Peter Naylor
- Valerio Marsocci
- Sébastien Lefèvre
- Bertrand Le Saux
- Nicolas Longépé
axes:
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G5_cost
- G6_compactness
claims:
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 0.063
  dataset: PhilEO Bench (road density)
  direction: worse
  id: dionelis2025scaling#c1
  label_ratio: null
  locator: Sec 4.6 / Table 3
  metric: rmse
  model: prithvi
  span: Geo-Aware U-Net 44M trained on 23TB achieves an RMSE of 0.067
  span_sha256: fc734e221542be4752392fc7363af63a3711f4e5dce1faf44acec5cdb25bd3ea
  task: urban_signal_mapping
  value: 0.071
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.68
  dataset: PhilEO Bench (land cover, ESA WorldCover)
  direction: worse
  id: dionelis2025scaling#c2
  label_ratio: null
  locator: Table 3
  metric: accuracy
  model: prithvi
  span: 0.0920.092 / 0.071¯\underline{0.071} / 0.5390.539
  span_sha256: 853907bbea0380f9f4dc1529422eccae4321dfa32bced4ef1defbe73886af687
  task: land_cover_classification
  value: 0.539
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 0.68
  dataset: PhilEO Bench (land cover, ESA WorldCover)
  direction: better
  id: dionelis2025scaling#c3
  label_ratio: null
  locator: Sec 5 / Conclusion
  metric: accuracy
  model: prithvi
  span: 70%70\% accuracy at n=500n=500 vs. 68%68\% for U-Net 44M GlobeEO
  span_sha256: d34136716709a3bc4a0e6253efea4d8a79c2542e9aa2e088aa9b651553f6a5f1
  task: land_cover_classification
  value: 0.7
date: '2025-06-17'
doi: 10.48550/arxiv.2506.14765
doi_status: verified
extractor_version: '1'
ingested_at: '2026-07-12T18:47:31.241954Z'
key: dionelis2025scaling
limitations:
- compute_cost
- benchmark_narrowness
- temporal_transfer
- data_bias
models:
- prithvi
proposed_tags:
- road_density_estimation
- building_density_estimation
- scaling_laws
- geo_aware_unet
- vit_upernet
- mamba_ssm
- flops_analysis
- terramind
regions:
- global
self_evaluation: false
tasks:
- semantic_segmentation
- land_cover_classification
- urban_signal_mapping
title: 'Scaling Laws for Geospatial Foundation Models: A case study on PhilEO Bench'
venue: arXiv
---

## summary

This paper studies scaling laws for Geospatial Foundation Models by pretraining CNN (Geo-Aware U-Net), ViT-UPerNet, and Mamba architectures on three dataset scales (0.5TB, 2TB, 23TB) and evaluating on PhilEO Bench. It finds CNNs remain competitive in low-shot regression settings while ViTs excel at semantic segmentation with large-scale pretraining, and compares results against existing GFMs TerraMind and Prithvi-EO-2.0.

## setup

Models are pretrained on Sentinel-2 imagery at three scales (GlobeEO 0.5TB, FastTOM 2TB introduced in this paper, MajorTOM 23TB) and fine-tuned/evaluated on PhilEO Bench using an n-shot protocol across building density regression, road density regression, and 11-class land cover segmentation (RMSE and overall accuracy metrics).

## caveats

The authors note that resampling all bands to 10m prevents leveraging native spectral resolutions; that including oceans/ice/deserts in MajorTOM pretraining introduces temporal and geographical domain shift that can hurt LULC performance compared to seasonally curated GlobeEO; and that Mamba models remain experimental with limited benchmarks and require further large-scale pretraining to match CNNs/ViTs.
