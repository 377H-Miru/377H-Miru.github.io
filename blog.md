---
layout: default
title: Blog
---

<style>
    .filter-controls { margin-bottom: 30px; display: flex; gap: 10px; }
    .filter-btn { 
        background: var(--nav-bg); border: 1px solid var(--border-color); 
        color: var(--text-color); padding: 5px 15px; border-radius: 15px; 
        cursor: pointer; font-size: 0.9em; transition: 0.2s;
    }
    .filter-btn.active { background: var(--link-color) !important; color: #fff !important; border-color: var(--link-color) !important; }
    .blog-item { display: block; text-decoration: none; color: inherit; margin-bottom: 20px; padding: 15px; background: var(--card-bg); border: 1px solid var(--border-color); border-radius: 8px; transition: transform 0.2s; }
    .blog-item:hover { transform: translateY(-2px); border-color: var(--link-color); }
    .blog-item .blog-date { font-size: 0.85em; color: #8b949e; }
    .blog-item .blog-title { font-size: 1.2em; font-weight: bold; margin: 5px 0; color: var(--link-color); }
</style>

<div data-lang-content="ja" markdown="1">
# ブログ

研究の進捗や日々のちょっとした気づきをカテゴリ別にまとめています。

<div class="filter-controls">
    <button class="filter-btn active" data-filter="all" onclick="filterBlog('all')">すべて</button>
    <button class="filter-btn" data-filter="research" onclick="filterBlog('research')">研究・技術</button>
    <button class="filter-btn" data-filter="personal" onclick="filterBlog('personal')">日々の雑記</button>
</div>

<hr>

## 2026年 4月
<div class="blog-list">
    <a href="/posts/2026-04-01-site-tech-stack" class="blog-item" data-category="research">
        <span class="tag tag-research">研究・技術</span>
        <span class="blog-date">2026-04-01</span>
        <div class="blog-title">ポートフォリオサイトの技術仕様について</div>
        <p>このサイトをどのように構築し、運用しているかについての技術メモです。</p>
    </a>
    <a href="/posts/2026-04-01-launch" class="blog-item" data-category="research">
        <span class="tag tag-research">研究・技術</span>
        <span class="blog-date">2026-04-01</span>
        <div class="blog-title">サイトを公開しました</div>
        <p>研究実績や活動をゆるやかに発信していく場所を作りました。</p>
    </a>
</div>

## 2026年 2月
<div class="blog-list">
    <a href="/posts/2026-02-25-euos25-review" class="blog-item" data-category="research">
        <span class="tag tag-research">研究・技術</span>
        <span class="blog-date">2026-02-25</span>
        <div class="blog-title">EUOS25 challengeを振り返って</div>
        <p>優勝をいただいたコンテストの技術的な背景（Multimodal Strategy と Sequential Stacking）について解説します。</p>
    </a>
</div>
</div>

<div data-lang-content="en" markdown="1">
# Blog

Monthly logs of research progress and daily thoughts.

<div class="filter-controls">
    <button class="filter-btn active" data-filter="all" onclick="filterBlog('all')">All</button>
    <button class="filter-btn" data-filter="research" onclick="filterBlog('research')">Research</button>
    <button class="filter-btn" data-filter="personal" onclick="filterBlog('personal')">Daily Life</button>
</div>

<hr>

## April 2026
<div class="blog-list">
    <a href="/posts/2026-04-01-site-tech-stack" class="blog-item" data-category="research">
        <span class="tag tag-research">Research</span>
        <span class="blog-date">2026-04-01</span>
        <div class="blog-title">Technical Specifications of This Site</div>
        <p>A technical note on how I built and maintain this portfolio.</p>
    </a>
    <a href="/posts/2026-04-01-launch" class="blog-item" data-category="research">
        <span class="tag tag-research">Research</span>
        <span class="blog-date">2026-04-01</span>
        <div class="blog-title">Site Launch</div>
        <p>Created a space to share my research progress and activities.</p>
    </a>
</div>

## February 2026
<div class="blog-list">
    <a href="/posts/2026-02-25-euos25-review" class="blog-item" data-category="research">
        <span class="tag tag-research">Research</span>
        <span class="blog-date">2026-02-25</span>
        <div class="blog-title">Reflections on EUOS25 Challenge</div>
        <p>A technical dive into the winning architecture (Multimodal Strategy & Sequential Stacking).</p>
    </a>
</div>
</div>

<script>
    function filterBlog(category) {
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
            if(btn.getAttribute('data-filter') === category) {
                btn.classList.add('active');
            }
        });
        document.querySelectorAll('.blog-item').forEach(item => {
            if (category === 'all' || item.getAttribute('data-category') === category) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }
</script>
