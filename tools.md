---
layout: default
title: ツール
lang: ja
permalink: /tools/
---

# 公開ツール (Software & Tools)

[← ホームに戻る](/)

研究活動の中で開発した、ケモインフォマティクスやデータ解析のためのソフトウェアを公開しています。

---

## [ecfp_cli](https://github.com/377H-Miru/ecfp_cli){:target="_blank"}
**SMILESからECFPフィンガープリントを高速・堅牢に生成**

- **主な機能**: 
    - マルチプロセスによる大規模データの高速並列計算。
    - 不正なSMILESの自動検知と詳細なエラーログ出力。
    - 脱塩処理（Salt removal）の標準搭載。
- **活用実績**: 日本薬学会第146年会でのポスター発表におけるデータ前処理に使用。
- **リンク**: [[GitHub Repository]](https://github.com/377H-Miru/ecfp_cli){:target="_blank"} ｜ [[Latest Release (v0.1.1)]](https://github.com/377H-Miru/ecfp_cli/releases/latest){:target="_blank"}

## [mordred_descriptor_calculator](https://github.com/377H-Miru/mordred_descriptor_calculator){:target="_blank"}
**$\pi$共役系対応・再現性を重視した記述子算出ツール**

- **主な機能**: 
    - 3D構造生成のシード固定とMMFFエネルギー最小化による高い再現性。
    - $\pi$共役系の品質（Conjugation Features）を独自アルゴリズムで算出。
    - Mordred記述子（1,800次元超）の一括計算に対応。
- **活用実績**: EUOS25 challenge 蛍光予測部門（優勝）での特徴量抽出に使用。
- **リンク**: [[GitHub Repository]](https://github.com/377H-Miru/mordred_descriptor_calculator){:target="_blank"} ｜ [[Latest Release (v0.1.1)]](https://github.com/377H-Miru/mordred_descriptor_calculator/releases/latest){:target="_blank"}

---

### インストール方法 (一般)
各ツールは、リポジトリをクローン後に以下のコマンドで依存関係をインストールして使用できます。
```bash
git clone https://github.com/377H-Miru/[リポジトリ名].git
cd [リポジトリ名]
pip install -r requirements.txt
```
