---
layout: default
title: Achievements
lang: ja
permalink: /achievements/
---

{% assign data = site.data.achievements %}

<h1>研究実績</h1>

<p><a href="/">← ホームに戻る</a></p>

<p>これまでに関わってきた主な実績をご紹介します。</p>

<hr>

<h2>受賞歴 (Awards)</h2>
<ul>
{% for award in data.awards %}
    <li>
        <b><a href="{{ award.url }}" target="_blank">{{ award.title_ja }}</a></b> ({{ award.date }})
        <ul>
            <li>共同研究者: {{ award.authors_ja }}</li>
            <li><a href="{{ award.result_url }}" target="_blank">[公式結果 (Official News)]</a> 
            {% if award.blog_url %}｜ <a href="{{ award.blog_url }}">[技術解説ブログはこちら]</a>{% endif %}</li>
            <li>{{ award.description_ja }}</li>
            <li>使用ツール: <a href="/tools/">mordred_descriptor_calculator</a></li>
        </ul>
    </li>
{% endfor %}
</ul>

<hr>

<h2>学会発表 (Presentations)</h2>
<ul>
{% for pres in data.presentations %}
    <li>
        {{ pres.authors_ja }}. "{{ pres.title_ja }}". <b>{{ pres.event_ja }}</b>, {{ pres.role_ja }}, {{ pres.date }}.
        <ul>
            <li>使用ツール: <a href="/tools/">ecfp_cli</a></li>
        </ul>
    </li>
{% endfor %}
</ul>

<hr>

{% if data.publications.size > 0 %}
<h2>論文 (Publications)</h2>
<ul>
{% for pub in data.publications %}
    <li>{{ pub.authors_ja }}. "{{ pub.title_ja }}". <i>{{ pub.journal_ja }}</i>, {{ pub.year }}. <a href="{{ pub.url }}" target="_blank">[{{ pub.doi }}]</a></li>
{% endfor %}
</ul>
<hr>
{% endif %}

<h2>ソフトウェア公開 (Software)</h2>
<p><a href="/tools/">詳細な仕様・機能は <b>ツール紹介ページ</b> をご覧ください。</a></p>
<ul>
    <li>
        <b><a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">ecfp_cli</a></b> (v0.1.1)
        <br>ECFPフィンガープリント高速生成ツール。日本薬学会第146年会でのデータ前処理に使用。
    </li>
    <li>
        <b><a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">mordred_descriptor_calculator</a></b> (v0.1.1)
        <br>π共役系記述子対応・記述子算出ツール。EUOS25 challenge での特徴量抽出に使用。
    </li>
</ul>

<hr>

<h2>所属学会 (Professional Memberships)</h2>
<ul>
{% for member in data.memberships %}
    <li>{{ member.name_ja }}</li>
{% endfor %}
</ul>

<hr>

<h2>学歴・略歴 (Education)</h2>
<ul>
{% for edu in data.education %}
    <li>{{ edu.period_ja }}: {{ edu.institution_ja }}</li>
{% endfor %}
</ul>
