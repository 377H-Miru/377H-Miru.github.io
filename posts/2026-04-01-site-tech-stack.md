---
layout: default
title: サイト構築の技術仕様
---

<div data-lang-content="ja" markdown="1">

# このサイトの構成

このサイトをどのように作り、更新しているかのメモです。

## 1. 方針
- **費用をかけない**: GitHub Pages で公開しています。
- **表示崩れを減らす**: 主要なページは Markdown ではなく HTML で書いています。
- **日本語と英語のページを分ける**: 英語のページは `/en/` 以下に置いています。
- **機能**: コメント欄、実績の絞り込み表示、お問い合わせフォーム。

## 2. 構成
- **基盤**: GitHub Pages + Jekyll
- **実績データ**: `_data/achievements.json` にまとめ、実績ページはこのデータから表示しています。
- **ディレクトリ**:
    - `/`: 日本語のページ
    - `/en/`: 英語のページ
    - `_layouts/`: 共通レイアウト（言語の切り替えボタン、表示テーマ）
- **公開**: リポジトリに push すると、GitHub Pages が自動でビルドします。

## 3. 工夫した点
### 言語の切り替え
最初は1つのファイルの中で JavaScript で表示を切り替えていましたが、言語ごとにディレクトリを分ける方式に変えました。レイアウト側で `page.url` から対応するページへのリンクを作っています。

### 実績データの管理
受賞歴や発表などを JSON にまとめて管理しています。追加が簡単になり、表示の形もそろえやすくなりました。

### 外部サービス
- **giscus**: GitHub Discussions を使ったコメント欄。
- **Formspree**: お問い合わせフォームの送信。
- **Google Analytics (GA4)**: アクセス数の確認。

## 4. 更新の手順
1. **実績の追加**: `_data/achievements.json` に追記します。
2. **記事の追加**: `posts/` に Markdown ファイルを追加します。
3. **公開**: 変更したファイルを commit して push します。
   ```bash
   git add _data/achievements.json
   git commit -m "update: add achievement"
   git push origin main
   ```

---
このサイトのソースコードは [GitHub リポジトリ](https://github.com/377H-Miru/377H-Miru.github.io) にあります。

</div>

<div data-lang-content="en" markdown="1">

# How This Site Is Built

Notes on how I build and update this site.

## 1. Policy
- **No cost**: hosted on GitHub Pages.
- **Fewer rendering problems**: main pages are written in HTML rather than Markdown.
- **Separate Japanese and English pages**: English pages live under `/en/`.
- **Features**: comments, filtering on the achievements page, and a contact form.

## 2. Structure
- **Platform**: GitHub Pages + Jekyll.
- **Achievement data**: kept in `_data/achievements.json`; the achievements page is generated from it.
- **Directories**:
    - `/`: Japanese pages.
    - `/en/`: English pages.
    - `_layouts/`: shared layout (language switch button, display theme).
- **Publishing**: pushing to the repository triggers an automatic GitHub Pages build.

## 3. Notes
### Language switching
I first switched languages with JavaScript inside a single file, and later moved to separate directories per language. The layout builds the link to the matching page from `page.url`.

### Achievement data
Awards and presentations are kept in JSON, which makes adding entries easy and keeps the display consistent.

### External services
- **giscus**: comments backed by GitHub Discussions.
- **Formspree**: contact form submission.
- **Google Analytics (GA4)**: visitor statistics.

## 4. Update workflow
1. **Add data**: append entries to `_data/achievements.json`.
2. **Write posts**: add Markdown files to `posts/`.
3. **Publish**: commit the changed files and push.
   ```bash
   git add _data/achievements.json
   git commit -m "update: add achievement"
   git push origin main
   ```

---
The source code of this site is in my [GitHub repository](https://github.com/377H-Miru/377H-Miru.github.io).

</div>
