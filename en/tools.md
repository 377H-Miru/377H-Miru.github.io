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

<h2><a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">ecfp_cli</a></h2>
<p><b>High-performance & Robust ECFP Fingerprint Generator</b></p>
<ul>
    <li><b>Key Features</b>: 
        <ul>
            <li>Fast parallel computation for large-scale datasets using multiprocessing.</li>
            <li>Automatic detection of invalid SMILES with detailed error logging.</li>
            <li>Built-in molecular desalting (standardization) options.</li>
        </ul>
    </li>
    <li><b>Track Record</b>: Used for data preprocessing in the 146th Annual Meeting of the Pharmaceutical Society of Japan.</li>
    <li><b>Links</b>: <a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">[GitHub Repository]</a> ｜ <a href="https://github.com/377H-Miru/ecfp_cli/releases/latest" target="_blank">[Latest Release (v0.1.1)]</a></li>
</ul>

<hr>

<h2><a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">mordred_descriptor_calculator</a></h2>
<p><b>Reproducible Descriptor Calculator with π-Conjugation Support</b></p>
<ul>
    <li><b>Key Features</b>: 
        <ul>
            <li>Reproducible 3D descriptors via fixed seeds and MMFF energy minimization.</li>
            <li>Custom algorithms for calculating π-conjugation features.</li>
            <li>Supports batch calculation of over 1,800 Mordred descriptors.</li>
        </ul>
    </li>
    <li><b>Track Record</b>: Used for feature extraction in the EUOS25 challenge (Winner, Fluorescence track).</li>
    <li><b>Links</b>: <a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">[GitHub Repository]</a> ｜ <a href="https://github.com/377H-Miru/mordred_descriptor_calculator/releases/latest" target="_blank">[Latest Release (v0.1.1)]</a></li>
</ul>

<hr>

<h3>Installation</h3>
<p>You can use these tools by cloning the repository and installing the dependencies:</p>
<pre><code>git clone https://github.com/377H-Miru/[repository-name].git
cd [repository-name]
pip install -r requirements.txt</code></pre>
