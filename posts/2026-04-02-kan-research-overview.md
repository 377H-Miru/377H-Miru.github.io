---
layout: default
title: Kolmogorov-Arnold Networks (KAN) による有害事象解析のアプローチ
title_en: "Adverse Event Analysis Approach using Kolmogorov-Arnold Networks (KAN)"
date: 2026-04-02
description: "Kolmogorov-Arnold Networks (KAN) を用いた有害事象予測の背景、高次元入力での課題、取り組んでいる検証の紹介。"
---

<div data-lang-content="ja" markdown="1">

# Kolmogorov-Arnold Networks (KAN) を用いた有害事象予測の取り組み

現在取り組んでいるテーマの一つである、**Kolmogorov-Arnold Networks (KAN)** を用いた有害事象の予測と、その予測に関わる化学構造の検討について、背景と方針を紹介します。

## KAN とは
KAN は、従来の多層パーセプトロン（MLP）がノードに活性化関数を持つのに対し、エッジ（結合）上にスプラインなどの学習可能な関数を持つニューラルネットワークです。学習した関数を個別に確認できるため、解釈のしやすさの面で注目されています。

## ケモインフォマティクスで使うときの課題
有害事象の予測のように高次元でスパースなデータに KAN を使うと、次のような課題があります。

1. **計算コスト**: ECFP のような数千次元の入力では、エッジごとに関数を持つ KAN の計算コストが大きくなります。
2. **過学習**: 表現力が高いため、FAERS のようなノイズの多いデータでは過学習しやすくなります。

## 取り組んでいること
スパース性を促す正則化などの工夫によって、これらの課題がどこまで軽減できるかを検証しています。

初期の結果は、日本薬学会 第146年会でポスター発表しました。関連する手法は、[Preprints.org のプレプリント](https://www.preprints.org/manuscript/202606.2071)（2026年6月）にまとめています。

</div>

<div data-lang-content="en" markdown="1">

# Adverse Event Prediction with Kolmogorov-Arnold Networks (KAN)

This post introduces the background and approach of one of my current topics: predicting drug adverse events with **Kolmogorov-Arnold Networks (KAN)** and examining the chemical structures related to those predictions.

## What is KAN?
Unlike multi-layer perceptrons (MLPs), which place activation functions on nodes, KANs place learnable functions such as splines on edges. Because each learned function can be inspected, KANs have attracted attention for interpretability.

## Issues in cheminformatics
Applying KAN to high-dimensional, sparse data such as adverse-event prediction raises some issues:

1. **Computational cost**: with inputs of thousands of dimensions, such as ECFP, a KAN with a function on every edge becomes expensive.
2. **Overfitting**: because the model is expressive, it tends to overfit noisy data such as FAERS.

## What I am working on
I am testing how far measures such as sparsity-promoting regularization reduce these issues.

Early results were presented as a poster at the 146th Annual Meeting of the Pharmaceutical Society of Japan. A related method is described in a [preprint on Preprints.org](https://www.preprints.org/manuscript/202606.2071) (June 2026).

</div>
