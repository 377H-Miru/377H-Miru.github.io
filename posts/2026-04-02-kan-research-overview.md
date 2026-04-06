---
layout: default
title: "Kolmogorov-Arnold Networks (KAN) による有害事象解析のアプローチ"
title_en: "Adverse Event Analysis Approach using Kolmogorov-Arnold Networks (KAN)"
date: 2026-04-02
---

<div data-lang-content="ja" markdown="1">

# Kolmogorov-Arnold Networks (KAN) による有害事象解析のアプローチ


現在取り組んでいる主要な研究テーマである、**Kolmogorov-Arnold Networks (KAN)** を用いた有害事象誘発に関与する化学構造の解釈性向上について、その背景と技術的なアプローチを紹介します。

## KANとは何か？
KANは、従来のMulti-Layer Perceptron (MLP) がノード（ニューロン）に活性化関数を持つのに対し、エッジ（結合重み）上にスプラインベースの活性化関数を持つ新しいニューラルネットワークアーキテクチャです。理論上、少ないパラメータ数で高い関数近似能力を持ち、特に**解釈性**において大きなアドバンテージを持つと期待されています。

## ケモインフォマティクスにおける技術的課題
しかし、KANをケモインフォマティクス、特に有害事象（副作用）予測という高次元・スパースなデータセットに適用する際には、いくつかの公知の課題に直面します。

1. **計算コストの増大**: ECFP（Extended-Connectivity Fingerprints）のような数千次元のスパースな入力を扱う際、エッジ上に複雑な関数を持つKANは計算コストが急激に増大します。
2. **過学習への脆弱性**: 表現力が高すぎるため、ノイズの多い実臨床データ（FAERS等）を学習させると、容易に過学習を引き起こします。

## 解決へのアプローチ：解釈性とスケーラビリティのトレードオフ
私たちの研究では、この**「解釈性とスケーラビリティのトレードオフ」**を克服するための手法を検証しています。具体的には、特定の正則化手法（スパース性誘導ペナルティなど）の導入や、アーキテクチャレイヤーの工夫により、高次元入力時でもKANの解釈性を維持しつつ計算効率を上げるためのフレームワークを構築しています。

このアプローチにより、医薬品の構造から「なぜその副作用が誘発されるのか」を局所的な部分構造（Toxicophore）レベルで特定し、分子・受容体レベルでの安全性評価基盤へと発展させることを目指しています。

本研究の初期成果については、第146年会 日本薬学会にてポスター発表を行いました。現在、本内容に関する論文およびソースコードの公開準備を進めています。

</div>

<div data-lang-content="en" markdown="1">

# Adverse Event Analysis Approach using Kolmogorov-Arnold Networks (KAN)


This post introduces the background and technical approach of my primary research theme: enhancing the interpretability of chemical structures contributing to adverse events using **Kolmogorov-Arnold Networks (KAN)**.

## What is KAN?
Unlike traditional Multi-Layer Perceptrons (MLPs) that place activation functions on nodes (neurons), KANs place spline-based activation functions on edges (weights). Theoretically, they offer high function approximation capabilities with fewer parameters and are expected to have significant advantages in **interpretability**.

## Technical Challenges in Cheminformatics
However, applying KAN to cheminformatics—especially for predicting adverse events using high-dimensional and sparse datasets—presents several well-documented challenges.

1. **Computational Overhead**: When dealing with sparse inputs of thousands of dimensions like ECFP (Extended-Connectivity Fingerprints), having complex functions on edges causes a rapid increase in computational cost.
2. **Susceptibility to Overfitting**: Due to their extreme expressive power, learning from noisy real-world clinical data (such as FAERS) easily leads to overfitting.

## Our Approach: The Interpretability vs. Scalability Trade-off
Our research investigates methods to overcome this **"interpretability vs. scalability trade-off"**. Specifically, we are constructing a framework to maintain KAN's interpretability while improving computational efficiency even with high-dimensional inputs. This is achieved by introducing specific regularization techniques (e.g., sparsity-inducing penalties) and architectural layer optimizations.

Through this approach, we aim to identify *why* a particular adverse event is triggered from a drug's structure at the level of local substructures (Toxicophores), ultimately developing a safety assessment foundation at the molecular and receptor levels.

Initial results from this research were presented as a poster at the 146th Annual Meeting of the Pharmaceutical Society of Japan. We are currently preparing to publish the manuscript and the corresponding source code.

</div>
