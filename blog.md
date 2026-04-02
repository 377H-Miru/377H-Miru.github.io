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
# 活動記録 / ブログ

研究の進捗や技術的な知見、日々の雑記をカテゴリ別にまとめています。

<div class="filter-controls">
    <button class="filter-btn active" data-filter="all" onclick="filterBlog('all')">すべて</button>
    <button class="filter-btn" data-filter="research" onclick="filterBlog('research')">研究関連</button>
    <button class="filter-btn" data-filter="personal" onclick="filterBlog('personal')">個人・雑記</button>
</div>

<hr>

## 2026年 4月
<div class="blog-list">
    <a href="/posts/2026-04-01-site-tech-stack" class="blog-item" data-category="research">
        <span class="tag tag-research">研究関連</span>
        <span class="blog-date">2026-04-01</span>
        <div class="blog-title">ポートフォリオサイトの技術仕様と再現性について</div>
        <p>サイトの設計思想、多言語対応・ダークモードの実装についての技術メモ。</p>
    </a>
    <a href="/posts/2026-04-01-launch" class="blog-item" data-category="research">
        <span class="tag tag-research">研究関連</span>
        <span class="blog-date">2026-04-01</span>
        <div class="blog-title">ポートフォリオサイトの設計思想と公開</div>
        <p>専門家向けのProof of Workとしてのサイト構築について。</p>
    </a>
</div>

## 2026年 2月
<div class="blog-list">
    <div class="blog-item" data-category="research">
        <span class="tag tag-research">研究関連</span>
        <span class="blog-date">2026-02-25</span>
        <div class="blog-title">EUOS25 challenge 優勝の技術的背景</div>
        <p>量子化学計算とKANを組み合わせた予測アプローチの詳解。（執筆予定）</p>
    </div>
</div>
</div>

<div data-lang-content="en" markdown="1">
# Blog & Logs

Monthly logs of research, technology, and personal thoughts.

<div class="filter-controls">
    <button class="filter-btn active" data-filter="all" onclick="filterBlog('all')">All</button>
    <button class="filter-btn" data-filter="research" onclick="filterBlog('research')">Research</button>
    <button class="filter-btn" data-filter="personal" onclick="filterBlog('personal')">Personal</button>
</div>

<hr>

## April 2026
<div class="blog-list">
    <a href="/posts/2026-04-01-site-tech-stack" class="blog-item" data-category="research">
        <span class="tag tag-research">Research</span>
        <span class="blog-date">2026-04-01</span>
        <div class="blog-title">Technical Specifications & Reproducibility</div>
        <p>Technical notes on design philosophy, multilingual/dark mode implementation.</p>
    </a>
    <a href="/posts/2026-04-01-launch" class="blog-item" data-category="research">
        <span class="tag tag-research">Research</span>
        <span class="blog-date">2026-04-01</span>
        <div class="blog-title">Portfolio Site: Design Philosophy & Launch</div>
        <p>Constructing a site as a 'Proof of Work' for experts.</p>
    </a>
</div>

## February 2026
<div class="blog-list">
    <div class="blog-item" data-category="research">
        <span class="tag tag-research">Research</span>
        <span class="blog-date">2026-02-25</span>
        <div class="blog-title">Technical Review: EUOS25 Challenge Win</div>
        <p>In-depth review of the predictive approach combining quantum chemistry and KAN. (Coming soon)</p>
    </div>
</div>
</div>

<script>
    function filterBlog(category) {
        // Update button states by data-filter attribute
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
            if(btn.getAttribute('data-filter') === category) {
                btn.classList.add('active');
            }
        });
        
        // Filter items
        document.querySelectorAll('.blog-item').forEach(item => {
            if (category === 'all' || item.getAttribute('data-category') === category) {
                item.style.display = 'block';
            } else {
                item.style.display = 'none';
            }
        });
    }
</script>
