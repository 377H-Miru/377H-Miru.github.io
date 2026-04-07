---
layout: default
title: サイト構築の技術仕様
---

<div data-lang-content="ja" markdown="1">

# ポートフォリオサイトの技術仕様と再現性について

本サイトは、研究者が最小限のコストで「能力の証明（Proof of Work）」を世界に発信することを目的に構築されています。当初の設計から、より堅牢で保守性の高いシステムへと進化した現在の技術仕様を記録します。

## 1. 設計要件
- **運用コストゼロ**: GitHub Pagesによるホスティング。
- **堅牢なレンダリング**: Markdown変換エラーを回避するため、主要ページにはHTMLを採用。
- **グローバル最適化**: `/en/` ディレクトリによる言語別の完全なURL分離。
- **インタラクティブな機能**: コメント機能、検索性の高いフィルタリング、Ajaxフォーム。

## 2. システム構成
- **基盤**: GitHub Pages + Jekyll
- **データ管理**: `_data/achievements.json` による実績データの一括管理。
- **ディレクトリ構造**: 
    - `/`: 日本語版コンテンツ
    - `/en/`: 英語版コンテンツ（SEO・UX最適化）
    - `_layouts/`: 共通レイアウト（多言語スイッチ、テーマ制御）
- **デプロイ**: GitHub Actionsによる自動ビルド・デプロイ。

## 3. 実装の工夫
### 多言語・URL分離の仕組み
当初の「1ファイル内でのJS切り替え」から、SEOとクローラ最適化のために「ディレクトリ分離方式」へ移行しました。レイアウト側で `page.url` を解析し、言語間をシームレスに行き来できるトグルボタンを実装しています。

### データ駆動型Achievements
実績データ（受賞歴、発表等）をJSON形式で分離管理しています。これにより、情報の追加が容易になり、サイト全体で一貫した表示形式を保つことができます。

### 外部サービスとの連携
- **giscus**: GitHub Discussionsをバックエンドにしたコメントシステム。
- **Formspree**: Ajaxを利用した、ページ遷移のないセキュアなお問い合わせフォーム。
- **Google Analytics (GA4)**: サイト訪問者の動向解析。

## 4. 日々の更新手順
1. **データの更新**: `_data/achievements.json` に新しい実績を追記。
2. **記事の執筆**: `posts/` フォルダに新しいMarkdownファイルを追加。
3. **プッシュ**:
   ```bash
   git add .
   git commit -m "update: add project details"
   git push origin main
   ```

---
本サイトの最新のソースコードは、私の [GitHubリポジトリ](https://github.com/377H-Miru/377H-Miru.github.io) で公開されています。

</div>

<div data-lang-content="en" markdown="1">

# Technical Specifications & Architecture of This Site

This site is designed for researchers to showcase their "Proof of Work" globally with minimal overhead. This post documents the evolved system architecture, focusing on reliability and maintainability.

## 1. Design Requirements
- **Zero Cost**: Hosted on GitHub Pages.
- **Robust Rendering**: Core pages utilize pure HTML to bypass Markdown parsing inconsistencies.
- **SEO Optimized**: Complete directory separation (`/` vs `/en/`) for multilingual content.
- **Modern Features**: Integrated comment system, interactive filtering, and AJAX contact forms.

## 2. System Architecture
- **Infrastructure**: GitHub Pages + Jekyll.
- **Data-Driven**: Achievements managed via `_data/achievements.json` for consistent rendering.
- **Directory Structure**:
    - `/`: Japanese content.
    - `/en/`: English content (optimized for global SEO).
    - `_layouts/`: Master templates controlling multilingual routing and theme state.

## 3. Implementation Highlights
### Multilingual Routing
Evolved from client-side JS toggling to true directory-based separation. The layout dynamically generates cross-language links, ensuring a seamless user experience across the `/en/` and root paths.

### External Integrations
- **giscus**: Comment system powered by GitHub Discussions.
- **Formspree**: Secure, AJAX-powered contact submission without page reloads.
- **Google Analytics (GA4)**: Visitor traffic and behavioral analysis.

## 4. Maintenance Workflow
1. **Update Data**: Add entries to `_data/achievements.json`.
2. **Write Posts**: Add new `.md` files to the `posts/` directory.
3. **Push**:
   ```bash
   git add .
   git commit -m "update: add research notes"
   git push origin main
   ```

---
Source code is open for reference at my [GitHub Repository](https://github.com/377H-Miru/377H-Miru.github.io).

</div>
