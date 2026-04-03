---
layout: default
title: Achievements
lang: en
permalink: /en/achievements/
---

{% assign data = site.data.achievements %}

# Achievements

[← Back to Home](/en/)

A summary of my research activities and contributions.

## Awards
{% for award in data.awards %}
- **[{{ award.title_en }}]({{ award.url }}){:target="_blank"}** ({{ award.date }})
    - Collaborators: {{ award.authors_en }}
    - [[Official Results (News)]]({{ award.result_url }}){:target="_blank"}
    {% if award.blog_url %}｜ [[Technical Review Blog]]({{ award.blog_url }}){% endif %}
    - {{ award.description_en }}
{% endfor %}

## Presentations
{% for pres in data.presentations %}
- {{ pres.authors_en }}. "{{ pres.title_en }}". **{{ pres.event_en }}**, {{ pres.role_en }}, {{ pres.date }}.
    - [[Abstract PDF (In prep)](#)] ｜ [[Poster PDF (In prep)](#)]
{% endfor %}

{% if data.publications.size > 0 %}
## Publications
{% for pub in data.publications %}
- {{ pub.authors_en }}. "{{ pub.title_en }}". *{{ pub.journal_en }}*, {{ pub.year }}. [{{ pub.doi }}]({{ pub.url }})
{% endfor %}
{% endif %}

## Software & Tools
- **[ecfp_cli](https://github.com/377H-Miru/ecfp_cli){:target="_blank"}** (v0.1.0)
    - High-speed ECFP fingerprint generator.
- **[mordred_descriptor_calculator](https://github.com/377H-Miru/mordred_descriptor_calculator){:target="_blank"}** (v0.1.0)
    - Descriptor calculator with $\pi$-conjugated system support.

## Education
{% for edu in data.education %}
- {{ edu.period_en }}: {{ edu.institution_en }}
{% endfor %}
- [[Download CV/Resume PDF (In prep)](#)]
