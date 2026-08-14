---
arxiv_id: '2608.09497'
authors:
- Thomas Lauber
- Mehmet Ozgur Turkoglu
- Sélène Ledain
- Helge Aasen
axes:
- G1_label_rich_parity
- G2_label_scarce_efficiency
- G3_spatial_transfer
- G4_temporal_transfer
- G5_cost
- G8_uncertainty
- G10_human_semantics
claims:
- axis: G1_label_rich_parity
  baseline: task_specific
  baseline_value: 48.1
  dataset: SwissCrop25
  direction: worse
  id: lauber2026swisscrop25#c1
  label_ratio: null
  locator: Table 3
  metric: miou
  model: galileo
  span: Fine-tuned Galileo-nano (30.4% mIoU) falls behind the other models
  span_sha256: 3fbaf8061a729d58c456b2baa0371593cad4cfadb238e1193e697806a9848222
  task: crop_type_mapping
  value: 30.4
- axis: G2_label_scarce_efficiency
  baseline: task_specific
  baseline_value: 30.8
  dataset: SwissCrop25
  direction: worse
  id: lauber2026swisscrop25#c2
  label_ratio: 0.1
  locator: Supp. Table 8
  metric: miou
  model: galileo
  span: Galileo-nano (10%)
  span_sha256: 0cc1474c2ed36f13efd62479766ad5e0e6470074b767e5525d82058c54e37704
  task: crop_type_mapping
  value: 18.4
- axis: G3_spatial_transfer
  baseline: task_specific
  baseline_value: null
  dataset: SwissCrop25
  direction: worse
  id: lauber2026swisscrop25#c3
  label_ratio: null
  locator: Section 4.2
  metric: miou
  model: galileo
  span: 'frozen variants (Galileo-nano: 14.1%; Galileo-base: 20.6%; full results in
    Supp. Table 4)'
  span_sha256: e881f47fbb1970780ecd3d10be763ae2d9adf5ee05160e45c1cf6727da6a737a
  task: crop_type_mapping
  value: 20.6
date: '2026-08-10'
doi: 10.48550/arxiv.2608.09497
doi_status: verified
extractor_version: '1'
ingested_at: '2026-08-14T00:13:43.900785Z'
key: lauber2026swisscrop25
limitations:
- benchmark_narrowness
- temporal_transfer
- compute_cost
- human_semantics
- data_bias
- mixed_pixels
models:
- galileo
proposed_tags:
- leave_one_year_out
- scene_completeness
- in_season_usability
- fine_grained_taxonomy
- grassland_management_types
- thermal_positional_encoding
regions:
- ch
self_evaluation: false
tasks:
- crop_type_mapping
title: 'SwissCrop25: A National Multi-Year Benchmark for Operational Crop Mapping'
venue: arXiv
---

## summary

SwissCrop25 is a national-scale, seven-year (2019-2025) Swiss crop mapping benchmark with a 73-class fine-grained taxonomy and 5 non-crop land-cover classes, paired with Sentinel-2 time series and daily temperature data. Under a leave-one-year-out protocol, the authors benchmark U-TAE, TSViT, and the Galileo EO foundation model, finding both domain-specific architectures outperform Galileo, with TSViT achieving a 12pp macro-mIoU advantage over U-TAE at the leaf taxonomy level. The paper also studies scene completeness, temporal generalisation via thermal encodings, fine-grained/long-tail classification, in-season usability, and efficiency/scalability.

## setup

SwissCrop25 combines LNF parcel-level crop declarations and swissTLM3D land-cover data across Switzerland (2019-2025), rasterised at 10m with 70 modelled classes (65 crop + 5 non-crop), paired with Sentinel-2 image time series and MeteoSwiss-derived cumulative growing degree days. Models (U-TAE, TSViT, Galileo-nano/base) are evaluated under a five-fold leave-one-year-out protocol (2021-2025 test years) on joint cropland delineation and 65-class crop classification, with additional low-resource (10% data), in-season (monthly truncation), and efficiency benchmarks.

## caveats

The authors note that LNF labels reflect declared planting intent rather than confirmed harvest outcomes, introducing label noise especially for crops determined at harvest (e.g., silage vs grain maize); 2019-2020 have incomplete national coverage and are used only for training; results reflect year-to-year generalisation over reused spatial locations rather than transfer to unseen geography; and Galileo-base is described as impractical to fine-tune even on 4 GH200 GPUs, requiring 5x longer inference than TSViT.
