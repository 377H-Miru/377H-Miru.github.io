---
layout: default
title: ブログ
lang: ja
permalink: /blog/
---

# ブログ

[← ホームに戻る](/)

研究の進捗や日々のちょっとした気づきをカテゴリ別にまとめています。

<div class="filter-controls">
    <button class="filter-btn active" data-filter="all" onclick="filterBlog('all')">すべて</button>
    <button class="filter-btn" data-filter="research" onclick="filterBlog('research')">研究・技術</button>
    <button class="filter-btn" data-filter="personal" onclick="filterBlog('personal')">日々の雑記</button>
</div>

<hr>

<div class="blog-list">
    {% assign posts = site.posts | sort: 'date' | reverse %}
    {% for post in posts %}
    <a href="{{ post.url }}" class="blog-item" data-category="{{ post.category | default: 'research' }}">
        <span class="tag tag-{{ post.category | default: 'research' }}">
            {% if post.category == 'personal' %}日々の雑記{% else %}研究・技術{% endif %}
        </span>
        <span class="blog-date">{{ post.date | date: "%Y-%m-%d" }}</span>
        <div class="blog-title">{{ post.title }}</div>
        <p>{{ post.excerpt | strip_html | truncate: 100 }}</p>
    </a>
    {% endfor %}
</div>

<script>
    function filterBlog(category) {
        document.querySelectorAll('.filter-btn').forEach(btn => {
            btn.classList.remove('active');
            if(btn.getAttribute('data-filter') === category) btn.classList.add('active');
        });
        document.querySelectorAll('.blog-item').forEach(item => {
            item.style.display = (category === 'all' || item.getAttribute('data-category') === category) ? 'block' : 'none';
        });
    }
</script>
