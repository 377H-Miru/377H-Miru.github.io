---
layout: default
title: ツール
lang: ja
permalink: /tools/
---

# 公開ツール (Software & Tools)

<p><a href="/">[← ホームに戻る]</a></p>

<p>研究活動の中で開発した、ケモインフォマティクスやデータ解析のためのソフトウェアを公開しています。</p>

<hr>

<h2><a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">ecfp_cli</a></h2>
<p><b>SMILESからECFPフィンガープリントを高速・堅牢に生成</b></p>
<ul>
    <li><b>主な機能</b>: 
        <ul>
            <li>マルチプロセスによる大規模データの高速並列計算。</li>
            <li>不正なSMILESの自動検知と詳細なエラーログ出力。</li>
            <li>脱塩処理（Salt removal）の標準搭載。</li>
        </ul>
    </li>
    <li><b>活用実績</b>: 日本薬学会第146年会でのポスター発表におけるデータ前処理に使用。</li>
    <li><b>リンク</b>: <a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">[GitHub Repository]</a> ｜ <a href="https://github.com/377H-Miru/ecfp_cli/releases/latest" target="_blank">[Latest Release (v0.1.1)]</a></li>
</ul>

<hr>

<h2><a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">mordred_descriptor_calculator</a></h2>
<p><b>π共役系対応・再現性を重視した記述子算出ツール</b></p>
<ul>
    <li><b>主な機能</b>: 
        <ul>
            <li>3D構造生成のシード固定とMMFFエネルギー最小化による高い再現性。</li>
            <li>π共役系の品質（Conjugation Features）を独自アルゴリズムで算出。</li>
            <li>Mordred記述子（1,800次元超）の一括計算に対応。</li>
        </ul>
    </li>
    <li><b>活用実績</b>: EUOS25 challenge 蛍光予測部門（優勝）での特徴量抽出に使用。</li>
    <li><b>リンク</b>: <a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">[GitHub Repository]</a> ｜ <a href="https://github.com/377H-Miru/mordred_descriptor_calculator/releases/latest" target="_blank">[Latest Release (v0.1.1)]</a></li>
</ul>

<hr>

<h3>インストール方法 (General Installation)</h3>
<p>各ツールは、リポジトリをクローン後に以下のコマンドで依存関係をインストールして使用できます。</p>
<pre><code>git clone https://github.com/377H-Miru/[リポジトリ名].git
cd [リポジトリ名]
pip install -r requirements.txt</code></pre>
