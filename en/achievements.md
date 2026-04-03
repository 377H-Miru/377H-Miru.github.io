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
    - [Official Results (News)]({{ award.result_url }}){:target="_blank"}
    {% if award.blog_url %}｜ [Technical Review Blog]({{ award.blog_url }}){% endif %}
    - {{ award.description_en }}
    - Tools used: **[mordred_descriptor_calculator](/en/tools)**
{% endfor %}

## Presentations
{% for pres in data.presentations %}
- {{ pres.authors_en }}. "{{ pres.title_en }}". **{{ pres.event_en }}**, {{ pres.role_en }}, {{ pres.date }}.
    - Tools used: **[ecfp_cli](/en/tools)**
{% endfor %}

## Software & Tools
[For detailed specifications, see the **Software & Tools page**.](/en/tools)

- **[ecfp_cli](https://github.com/377H-Miru/ecfp_cli){:target="_blank"}** (v0.1.1)
    - High-speed ECFP fingerprint generator. Used for data preprocessing in PSJ 146th annual meeting.
- **[mordred_descriptor_calculator](https://github.com/377H-Miru/mordred_descriptor_calculator){:target="_blank"}** (v0.1.1)
    - Descriptor calculator with $\pi$-conjugated system support. Used for feature extraction in EUOS25 challenge.

## Education
{% for edu in data.education %}
- {{ edu.period_en }}: {{ edu.institution_en }}
{% endfor %}
