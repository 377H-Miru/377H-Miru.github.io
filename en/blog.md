---
layout: default
title: Blog
lang: en
permalink: /en/blog/
---

# Blog

[← Back to Home](/en/)

Monthly logs of research progress and daily thoughts.

<div class="filter-controls">
    <button class="filter-btn active" data-filter="all" onclick="filterBlog('all')">All</button>
    <button class="filter-btn" data-filter="research" onclick="filterBlog('research')">Research</button>
    <button class="filter-btn" data-filter="personal" onclick="filterBlog('personal')">Daily Life</button>
</div>

<hr>

<div class="blog-list">
    {% assign posts = site.posts | sort: 'date' | reverse %}
    {% for post in posts %}
    <a href="{{ post.url }}" class="blog-item" data-category="{{ post.category | default: 'research' }}">
        <span class="tag tag-{{ post.category | default: 'research' }}">
            {% if post.category == 'personal' %}Daily Life{% else %}Research{% endif %}
        </span>
        <span class="blog-date">{{ post.date | date: "%Y-%m-%d" }}</span>
        <div class="blog-title">{{ post.title_en | default: post.title }}</div>
        <p>{{ post.excerpt_en | default: post.excerpt | strip_html | truncate: 100 }}</p>
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
