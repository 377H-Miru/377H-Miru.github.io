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
  While KAN provides superior function approximation, it faces well-documented challenges such as computational overhead and susceptibility to overfitting when applied to high-dimensional datasets (e.g., ECFP). This project investigates **overcoming the scalability-interpretability trade-off** through specialized regularization techniques and architectural optimizations.
- **Status:** Presented at the PSJ Annual Meeting; [Manuscript in preparation].
- **Tools & Resources:** [ecfp_cli](https://github.com/377H-Miru/ecfp_cli) {:target="_blank"} ｜ [Technical Review](/en/posts/2026-04-02-kan-research-overview)

## EUOS25 challenge: Optical Property Prediction
- **Summary:** A machine learning competition for predicting optical properties of ~100k compounds. Our team won the Fluorescence track.
- **Technical Approach:**
    - **Multimodal Strategy:** Integrated pre-calculated quantum chemistry results (e.g., MACE-xTB) and 1,800+ descriptors. Specifically, developed a specialized feature space for fluorescence prediction by introducing unique Conjugation Features to evaluate the quality of π-conjugated systems.
    - **Sequential Stacking:** Developed a chaining architecture that models the biophysical dependency from transmittance to fluorescence.
- **Result:** Winner of the Fluorescence track (February 2026)
- **Outlook:** Technical details and code to be submitted to "SLAS Technology". [Status: In preparation]
- **Tools & Resources:** [mordred_descriptor_calculator](https://github.com/377H-Miru/mordred_descriptor_calculator) {:target="_blank"} ｜ [Official News](https://www.eu-openscreen.eu/resources/eu-openscreen-news/ansicht/eu-openscreen-and-slas-announce-winners-of-the-second-joint-machine-learning-challenge-at-slas-2026.html) {:target="_blank"} ｜ [Challenge Info](https://ochem.eu/static/challenge2025.do) {:target="_blank"} ｜ [Technical Review](/en/posts/2026-02-25-euos25-review)
