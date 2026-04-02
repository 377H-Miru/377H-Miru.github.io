---
layout: default
title: サイト構築の技術仕様
---

<div data-lang-content="ja" markdown="1">

# ポートフォリオサイトの技術仕様と再現性について

本サイトは、研究者が最小限のコストで「能力の証明（Proof of Work）」を世界に発信することを目的に構築されています。ここでは、本サイトの設計思想と、同様のサイトを構築・運用するための技術的仕様を記録します。

## 1. 設計要件
- **運用コストゼロ**: GitHub Pagesによるホスティング。
- **コンテンツ重視**: 執筆はすべてMarkdown (.md) で完結。
- **グローバル対応**: 日本語と英語の動的な切り替え。
- **プロフェッショナルな視認性**: ダークモード/ライトモードの搭載。

## 2. システム構成
- **基盤**: GitHub Pages + Jekyll
- **管理形式**: テンプレート（HTML/CSS/JS）とコンテンツ（Markdown）の分離。
- **デプロイ**: Gitによるプッシュ時にGitHub Actionsで自動ビルド。

## 3. 実装の工夫
### 多言語切り替えの仕組み
Markdown内にカスタム属性 `data-lang-content` を付与したタグを配置し、JavaScriptで表示/非表示を制御しています。これにより、1つのMarkdownファイルで多言語管理が可能になります。

### ダークモードの実装
CSS変数（Custom Properties）を使用し、`body` タグの属性を切り替えることで配色を瞬時に変更します。

## 4. 日々の更新手順
新しい実績やプロジェクトを追加する際は、以下の手順のみで完結します。

1. **Markdownファイルを編集**: `index.md` や `achievements.md` を開いて内容を追記。
2. **プッシュ**: ターミナルで以下を実行。
   ```bash
   git add .
   git commit -m "update: 実績の追加"
   git push origin main
   ```

## 5. 再現のためのリポジトリ構造
このサイトの構成を流用する場合、以下の構成を維持することが重要です。
- `_layouts/`: サイトの骨格となるテンプレート。
- `index.md`: トップページの内容。
- `blog.md`: 記事一覧。
- `posts/`: 個別記事の格納先。

---
本サイトのソースコードは、私の [GitHubリポジトリ](https://github.com/377H-Miru/377H-Miru.github.io) で公開されています。

</div>

<div data-lang-content="en" markdown="1">

# Technical Specifications & Reproducibility of This Site

This site is designed for researchers to showcase their "Proof of Work" globally with minimal overhead. This post documents the design philosophy and technical specifications required to build and operate a similar site.

## 1. Design Requirements
- **Zero Operating Cost**: Hosted on GitHub Pages.
- **Content-Centric**: All writing is done in Markdown (.md).
- **Global Ready**: Dynamic toggling between Japanese and English.
- **Professional Visibility**: Dark/Light mode support.

## 2. System Architecture
- **Infrastructure**: GitHub Pages + Jekyll.
- **Management**: Decoupling of templates (HTML/CSS/JS) and content (Markdown).
- **Deployment**: Automatic builds via GitHub Actions upon Git push.

## 3. Implementation Details
### Multilingual Logic
By using custom attributes like `data-lang-content` within Markdown and controlling visibility via JavaScript, we manage multiple languages in a single file.

### Dark Mode
Implemented using CSS Variables (Custom Properties). Color schemes are swapped instantly by toggling attributes on the `body` tag.

## 4. Maintenance Workflow
Updating achievements or projects only requires these steps:

1. **Edit Markdown**: Update `index.md` or `achievements.md`.
2. **Push**:
   ```bash
   git add .
   git commit -m "update: add achievement"
   git push origin main
   ```

## 5. Repository Structure for Reproducibility
To reuse this setup, maintain the following structure:
- `_layouts/`: Main site templates.
- `index.md`: Homepage content.
- `blog.md`: Post listings.
- `posts/`: Individual blog posts.

---
The source code is available at my [GitHub Repository](https://github.com/377H-Miru/377H-Miru.github.io).

</div>
