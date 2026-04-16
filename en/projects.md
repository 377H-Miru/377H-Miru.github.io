---
layout: default
title: Projects
lang: en
permalink: /en/projects/
---

# Projects

[← Back to Home](/en/)

## Adverse Event Analysis via Kolmogorov-Arnold Networks (KAN)
- **Summary:** Utilizing KAN to enhance the interpretability of chemical structures contributing to adverse events.
- **Addressing Technical Trade-offs:** 
  This project investigates overcoming the scalability-interpretability trade-off of KAN when applied to high-dimensional chemical datasets through specialized regularization and architectural optimizations.
- **Status:** Presented at the PSJ Annual Meeting.
- **Tools:** [ecfp_cli](https://github.com/377H-Miru/ecfp_cli) ｜ [Technical Review](/en/posts/2026-04-02-kan-research-overview)

---

## EUOS25 challenge: Optical Property Prediction
- **Summary:** Winner of the Fluorescence track in a large-scale competition involving ~100k compounds.
- **Technical Approach:**
    - **Massive Informatics:** Expanded PathCounts (up to 50th order) beyond 1,800+ Mordred descriptors. Integrated Conjugation Features to evaluate π-conjugated systems, constructing a specialized feature space for fluorescence prediction.
    - **GNN Feature Generation:** Integrated graph-based embeddings using a custom GINE-Net.
    - **Sequential Stacking:** Chained architecture modeling biophysical dependencies from transmittance to fluorescence.
- **Result:** Winner of the Fluorescence track (February 2026)
- **Outlook:** To be submitted to "SLAS Technology". [Status: In preparation]
- **Tools:** [mordred_descriptor_calculator](https://github.com/377H-Miru/mordred_descriptor_calculator) ｜ [Official News](https://www.eu-openscreen.eu/resources/eu-openscreen-news/ansicht/eu-openscreen-and-slas-announce-winners-of-the-second-joint-machine-learning-challenge-at-slas-2026.html) ｜ [Challenge Info](https://ochem.eu/static/challenge2025.do) ｜ [Technical Review](/en/posts/2026-02-25-euos25-review)
