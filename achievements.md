---
layout: default
title: Achievements
---

{% assign data = site.data.achievements %}

<div data-lang-content="ja" markdown="1">
# 研究実績

[← ホームに戻る](/index)

これまでに関わってきた主な実績をご紹介します。

## 受賞歴
{% for award in data.awards %}
- **[{{ award.title_ja }}]({{ award.url }}){:target="_blank"}** ({{ award.date }})
    - [[公式結果 (LinkedIn)]]({{ award.result_url }}){:target="_blank"}
    - {{ award.description_ja }}
{% endfor %}

## 学会発表
{% for pres in data.presentations %}
- {{ pres.authors }}. "{{ pres.title_ja }}". **{{ pres.event_ja }}**, {{ pres.role_ja }}, {{ pres.date }}.
{% endfor %}

{% if data.publications.size > 0 %}
## 論文
{% for pub in data.publications %}
- {{ pub.authors }}. "{{ pub.title_ja }}". *{{ pub.journal_ja }}*, {{ pub.year }}. [{{ pub.doi }}]({{ pub.url }})
{% endfor %}
{% endif %}

## 学歴・略歴
{% for edu in data.education %}
- {{ edu.period_ja }}: {{ edu.institution_ja }}
{% endfor %}
</div>

<div data-lang-content="en" markdown="1">
# Achievements

[← Back to Home](/index)

A summary of my research activities and contributions.

## Awards
{% for award in data.awards %}
- **[{{ award.title_en }}]({{ award.url }}){:target="_blank"}** ({{ award.date }})
    - [[Official Results (LinkedIn)]]({{ award.result_url }}){:target="_blank"}
    - {{ award.description_en }}
{% endfor %}

## Presentations
{% for pres in data.presentations %}
- {{ pres.authors }}. "{{ pres.title_en }}". **{{ pres.event_en }}**, {{ pres.role_en }}, {{ pres.date }}.
{% endfor %}

{% if data.publications.size > 0 %}
## Publications
{% for pub in data.publications %}
- {{ pub.authors }}. "{{ pub.title_en }}". *{{ pub.journal_en }}*, {{ pub.year }}. [{{ pub.doi }}]({{ pub.url }})
{% endfor %}
{% endif %}

## Education
{% for edu in data.education %}
- {{ edu.period_en }}: {{ edu.institution_en }}
{% endfor %}
</div>
