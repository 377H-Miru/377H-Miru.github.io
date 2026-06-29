---
layout: default
title: Tools
lang: en
permalink: /en/tools/
---

<h1>Software & Tools</h1>

<p><a href="/en/">[← Back to Home]</a></p>

<p>Open-source software and tools developed for cheminformatics and data analysis during my research.</p>

<hr>

<h2><a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">ecfp_cli (`ecfp-gen`)</a></h2>
<p><b>High-performance & Robust ECFP Fingerprint Generator CLI</b></p>
<ul>
    <li><b>Key Features</b>: 
        <ul>
            <li>Intuitive CLI interface (`ecfp-gen --input ... --output ...`).</li>
            <li>Fast parallel computation and streaming chunk execution for large-scale datasets.</li>
            <li>Built-in desalting (`--desalt`) and optional standardization (`--standardize`).</li>
            <li>Flexible column naming options (custom bit prefix and zero-indexed bit columns).</li>
            <li>Multi-stage structured error logging (`.errors.tsv` / `.errors.csv`) for full workflow transparency.</li>
        </ul>
    </li>
    <li><b>Track Record</b>: Used for data preprocessing in the 146th Annual Meeting of the Pharmaceutical Society of Japan.</li>
    <li><b>Links</b>: <a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">[GitHub Repository]</a> ｜ <a href="https://github.com/377H-Miru/ecfp_cli/releases/latest" target="_blank">[Latest Release (v0.2.0)]</a></li>
</ul>

<hr>

<h2><a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">mordred_descriptor_calculator (`mordred-desc`)</a></h2>
<p><b>Reproducible Descriptor Calculator CLI with π-Conjugation Support</b></p>
<ul>
    <li><b>Key Features</b>: 
        <ul>
            <li>Intuitive CLI interface (`mordred-desc --input ... --output ...`).</li>
            <li>Reproducible 3D descriptors via fixed seeds and force field optimization (MMFF & UFF).</li>
            <li>Custom algorithms for calculating π-conjugation features.</li>
            <li>Multi-stage structured error logging (`.errors.csv`) for complete workflow transparency.</li>
        </ul>
    </li>
    <li><b>Track Record</b>: Used for feature extraction in the EUOS25 challenge (Winner, Fluorescence track).</li>
    <li><b>Links</b>: <a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">[GitHub Repository]</a> ｜ <a href="https://github.com/377H-Miru/mordred_descriptor_calculator/releases/latest" target="_blank">[Latest Release (v0.1.0)]</a></li>
</ul>

<hr>

<h3>Installation</h3>
<p>You can install and use these CLI tools by cloning the repository and running editable installation (Python 3.10 recommended):</p>
<pre><code>git clone https://github.com/377H-Miru/[repository-name].git
cd [repository-name]
pip install -e .</code></pre>
