---
layout: default
title: Projects
---

<div data-lang-content="ja" markdown="1">

# プロジェクト

[← ホームに戻る](/)

## Kolmogorov-Arnold Networks (KAN) による有害事象解析
- **概要:** 最新のニューラルネットワークアーキテクチャであるKANを用い、有害事象誘発に寄与する化学構造の解釈性を高める研究に取り組んでいます。
- **技術的課題へのアプローチ:** 
  KANは高い関数近似能力を持つ一方で、多次元入力（ECFP等）に対する計算コストの急激な増大や、過学習への脆弱性が公知の課題として存在します。本プロジェクトでは、特定の正則化手法やアーキテクチャの工夫を導入し、**「解釈性とスケーラビリティのトレードオフ」**をどのように克服できるかという観点から検証を進めています。
- **取り組み:** 第146年会 日本薬学会にて発表、および論文投稿に向けた準備を進めています。[Status: In preparation]

## EUOS25 challenge 光学特性予測部門
- **概要:** 約10万化合物のライブラリを用いた光学特性予測コンテスト。部門は透過率（Transmittance）予測と蛍光（Fluorescence）予測の2つのトラックで構成され、私たちは蛍光予測部門で優勝しました。
- **技術的アプローチ:** 
    - **Multimodal Strategy:** 6種類のMOPAC HamiltonianとMACE-xTBを用いた精密な量子化学計算、および1,800次元超の記述子を統合。特に$\pi$共役系の品質を評価する Conjugation Features を独自に導入し、蛍光予測に特化した特徴量空間を構築しました。
    - **Sequential Stacking:** 透過率から蛍光への物性的依存関係をモデル化する、連鎖的なスタッキングアーキテクチャを構築。
- **結果:** 蛍光予測部門 優勝（2026年2月）
- **今後:** 学術誌「SLAS Technology」へ投稿準備中です。[Status: In preparation]
- [[公式ニュース]](https://www.eu-openscreen.eu/resources/eu-openscreen-news/ansicht/eu-openscreen-and-slas-announce-winners-of-the-second-joint-machine-learning-challenge-at-slas-2026.html){:target="_blank"} ｜ [[コンテスト概要]](https://ochem.eu/static/challenge2025.do){:target="_blank"} ｜ [[技術解説ブログ]](/posts/2026-02-25-euos25-review)

</div>

<div data-lang-content="en" markdown="1">

# Projects

[← Back to Home](/)

## Adverse Event Analysis via Kolmogorov-Arnold Networks (KAN)
- **Summary:** Utilizing KAN to enhance the interpretability of chemical structures contributing to adverse events.
- **Addressing Technical Trade-offs:** 
  While KAN provides superior function approximation, it faces well-documented challenges such as computational overhead and susceptibility to overfitting when applied to high-dimensional datasets (e.g., ECFP). This project investigates **overcoming the scalability-interpretability trade-off** through specialized regularization techniques and architectural optimizations.
- **Status:** Presented at the PSJ Annual Meeting; [Manuscript in preparation].

## EUOS25 challenge: Optical Property Prediction
- **Summary:** A machine learning competition for predicting optical properties of ~100k compounds. The challenge consisted of two tracks: Transmittance and Fluorescence prediction. Our team won the Fluorescence track.
- **Technical Approach:**
    - **Multimodal Strategy:** Integrating high-precision quantum chemistry (MOPAC/MACE-xTB) and 1,800+ descriptors. Specifically, integrated specialized Conjugation Features to evaluate the quality of $\pi$-conjugation systems, constructing a feature space specialized for fluorescence prediction.
    - **Sequential Stacking:** Developed a chaining architecture that models the biophysical dependency from transmittance to fluorescence.
- **Result:** Winner of the Fluorescence track (February 2026)
- **Outlook:** Technical details and code to be submitted to "SLAS Technology". [Status: In preparation]
- [[Official News]](https://www.eu-openscreen.eu/resources/eu-openscreen-news/ansicht/eu-openscreen-and-slas-announce-winners-of-the-second-joint-machine-learning-challenge-at-slas-2026.html){:target="_blank"} ｜ [[Challenge Info]](https://ochem.eu/static/challenge2025.do){:target="_blank"} ｜ [[Technical Review]](/posts/2026-02-25-euos25-review)

</div>
