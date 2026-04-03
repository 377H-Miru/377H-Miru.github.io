---
layout: default
title: Tools
lang: en
permalink: /en/tools/
---

# Software & Tools

[← Back to Home](/en/)

Open-source software and tools developed for cheminformatics and data analysis during my research.

---

## [ecfp_cli](https://github.com/377H-Miru/ecfp_cli){:target="_blank"}
**High-performance & Robust ECFP Fingerprint Generator**

- **Key Features**: 
    - Fast parallel computation for large-scale datasets using multiprocessing.
    - Automatic detection of invalid SMILES with detailed error logging.
    - Built-in molecular desalting (standardization) options.
- **Track Record**: Used for data preprocessing in the 146th Annual Meeting of the Pharmaceutical Society of Japan.
- **Links**: [[GitHub Repository]](https://github.com/377H-Miru/ecfp_cli){:target="_blank"} ｜ [[Latest Release (v0.1.1)]](https://github.com/377H-Miru/ecfp_cli/releases/latest){:target="_blank"}

## [mordred_descriptor_calculator](https://github.com/377H-Miru/mordred_descriptor_calculator){:target="_blank"}
**Reproducible Descriptor Calculator with $\pi$-Conjugation Support**

- **Key Features**: 
    - Reproducible 3D descriptors via fixed seeds and MMFF energy minimization.
    - Custom algorithms for calculating $\pi$-conjugation features.
    - Supports batch calculation of over 1,800 Mordred descriptors.
- **Track Record**: Used for feature extraction in the EUOS25 challenge (Winner, Fluorescence track).
- **Links**: [[GitHub Repository]](https://github.com/377H-Miru/mordred_descriptor_calculator){:target="_blank"} ｜ [[Latest Release (v0.1.1)]](https://github.com/377H-Miru/mordred_descriptor_calculator/releases/latest){:target="_blank"}

---

### Installation
You can use these tools by cloning the repository and installing the dependencies:
```bash
git clone https://github.com/377H-Miru/[repository-name].git
cd [repository-name]
pip install -r requirements.txt
```
