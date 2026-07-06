---
layout: default
title: プロジェクト
lang: ja
permalink: /projects/
---

# プロジェクト

[← ホームに戻る](/)

## FiDES: Kolmogorov-Arnold Networks (KAN) による有害事象解析
- **概要:** 最新のニューラルネットワークアーキテクチャであるKANを用い、有害事象誘発に寄与する化学構造の解釈性を高める研究に取り組んでいます。
- **技術的課題へのアプローチ:** 
  KANは高い関数近似能力を持つ一方で、多次元入力（ECFP等）に対する計算コストの急激な増大や、過学習への脆弱性が公知の課題として存在します。本プロジェクトでは、特定の正則化手法やアーキテクチャの工夫を導入し、**「解釈性とスケーラビリティのトレードオフ」**をどのように克服できるかという観点から検証を進めています。
- **取り組み:** 第146年会 日本薬学会、第9回フレッシャーズ・カンファランス、および第53回日本毒性学会学術年会にて発表
- **論文情報:** Preprint: [Preprints.org (Fragment–Molecular Evidence Stacking)](https://www.preprints.org/manuscript/202606.2071)
- **使用ツール:** [ecfp_cli](https://github.com/377H-Miru/ecfp_cli) ｜ [技術解説ブログ](/posts/2026-04-02-kan-research-overview)

---

## EUOS25 challenge 光学特性予測部門
- **概要:** 約10万化合物のライブラリを用いた光学特性予測コンテスト。私たちは蛍光予測部門で優勝しました。
- **技術的アプローチ:**
    - **Massive Informatics (大規模記述子):** 1,800次元超の Mordred 記述子に加え、長距離相関を捉えるための PathCounts（最大50次）を独自拡張。π共役系の品質を評価する Conjugation Features を統合し、蛍光予測に特化した特徴量空間を構築しました。
    - **GNN Feature Generation (グラフニューラルネットワーク):** カスタムの GINE-Net を活用し、グラフ構造から抽出されたエムベディングを特徴量として統合しました。
    - **Sequential Stacking:** 透過率から蛍光への物性的依存関係をモデル化する、連鎖的なスタッキングアーキテクチャを構築。
- **結果:** 蛍光予測部門 優勝（2026年2月）
- **今後:** 学術誌「SLAS Technology」へ投稿準備中です。
- **使用ツール:** [mordred_descriptor_calculator](https://github.com/377H-Miru/mordred_descriptor_calculator) ｜ [公式ニュース](https://www.eu-openscreen.eu/resources/eu-openscreen-news/ansicht/eu-openscreen-and-slas-announce-winners-of-the-second-joint-machine-learning-challenge-at-slas-2026.html) ｜ [コンテスト概要](https://ochem.eu/static/challenge2025.do) ｜ [技術解説ブログ](/posts/2026-02-25-euos25-review)
