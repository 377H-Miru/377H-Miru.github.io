---
layout: default
title: Achievements
lang: ja
permalink: /achievements/
---

{% assign data = site.data.achievements %}

# 研究実績

[← ホームに戻る](/)

これまでに関わってきた主な実績をご紹介します。

## 受賞歴
{% for award in data.awards %}
- **[{{ award.title_ja }}]({{ award.url }}){:target="_blank"}** ({{ award.date }})
    - 共同研究者: {{ award.authors_ja }}
    - [[公式結果 (Official News)]]({{ award.result_url }}){:target="_blank"} 
    {% if award.blog_url %}｜ [[技術解説ブログはこちら]]({{ award.blog_url }}){% endif %}
    - {{ award.description_ja }}
{% endfor %}

## 学会発表
{% for pres in data.presentations %}
- {{ pres.authors_ja }}. "{{ pres.title_ja }}". **{{ pres.event_ja }}**, {{ pres.role_ja }}, {{ pres.date }}.
    - [[要旨PDF(準備中)](#)] ｜ [[ポスターPDF(準備中)](#)]
{% endfor %}

{% if data.publications.size > 0 %}
## 論文
{% for pub in data.publications %}
- {{ pub.authors_ja }}. "{{ pub.title_ja }}". *{{ pub.journal_ja }}*, {{ pub.year }}. [{{ pub.doi }}]({{ pub.url }})
{% endfor %}
{% endif %}

## ソフトウェア公開
- **[ecfp_cli](https://github.com/377H-Miru/ecfp_cli){:target="_blank"}** (v0.1.0)
    - ECFPフィンガープリント高速生成ツール
- **[mordred_descriptor_calculator](https://github.com/377H-Miru/mordred_descriptor_calculator){:target="_blank"}** (v0.1.0)
    - $\pi$共役系記述子対応・記述子算出ツール

## 学歴・略歴
{% for edu in data.education %}
- {{ edu.period_ja }}: {{ edu.institution_ja }}
{% endfor %}
- [[履歴書/CV PDF(準備中)](#)]
