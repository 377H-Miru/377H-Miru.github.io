---
layout: default
title: ツール
lang: ja
permalink: /tools/
---

<h1>公開ツール (Software & Tools)</h1>

<p><a href="/">[← ホームに戻る]</a></p>

<p>研究活動の中で開発した、ケモインフォマティクスやデータ解析のためのソフトウェアを公開しています。</p>

<hr>

<h2><a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">ecfp_cli (`ecfp-gen`)</a></h2>
<p><b>SMILESからECFPフィンガープリントを高速・堅牢に生成するCLIツール</b></p>
<ul>
    <li><b>主な機能</b>: 
        <ul>
            <li>マルチプロセスによる大規模データの高速並列計算。</li>
            <li>不正なSMILESの自動検知と詳細なエラーログ出力。</li>
            <li>脱塩処理（Salt removal）の標準搭載。</li>
        </ul>
    </li>
    <li><b>活用実績</b>: 日本薬学会第146年会でのポスター発表におけるデータ前処理に使用。</li>
    <li><b>リンク</b>: <a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">[GitHub Repository]</a> ｜ <a href="https://github.com/377H-Miru/ecfp_cli/releases/latest" target="_blank">[Latest Release (v0.2.0)]</a></li>
</ul>

<hr>

<h2><a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">mordred_descriptor_calculator (`mordred-desc`)</a></h2>
<p><b>SMILES表からMordred記述子・π共役系カスタム記述子を一括算出する堅牢な研究用CLIツール</b></p>
<ul>
    <li><b>主な機能</b>: 
        <ul>
            <li>`mordred-desc` CLIによる直感的な操作（`--input`, `--output`, `--only-2d`）。</li>
            <li>3D構造生成のシード固定とMMFF/UFF力場最適化による高い再現性。</li>
            <li>π共役系の網羅的探索（Conjugation Features）を自動算出。</li>
            <li>多段階構造化エラーログ（`.errors.csv`）により失敗原因を透過的に記録。</li>
        </ul>
    </li>
    <li><b>活用実績</b>: EUOS25 challenge 蛍光予測部門（優勝）での特徴量抽出に使用。</li>
    <li><b>リンク</b>: <a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">[GitHub Repository]</a> ｜ <a href="https://github.com/377H-Miru/mordred_descriptor_calculator/releases/latest" target="_blank">[Latest Release (v0.1.0)]</a></li>
</ul>

<hr>

<h3>インストール方法 (General Installation)</h3>
<p>各ツールは、リポジトリをクローン後に以下のコマンドでインストールして CLI コマンドとして使用できます（Python 3.10 推奨）。</p>
<pre><code>git clone https://github.com/377H-Miru/[リポジトリ名].git
cd [リポジトリ名]
pip install -e .</code></pre>
