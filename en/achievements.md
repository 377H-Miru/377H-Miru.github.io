---
layout: default
title: Achievements
lang: en
permalink: /en/achievements/
---

{% assign data = site.data.achievements %}

# Achievements

<p><a href="/en/">[← Back to Home]</a></p>

<p>A summary of my research activities and contributions.</p>

<hr>

<h2>Awards</h2>
<ul>
{% for award in data.awards %}
    <li>
        <b><a href="{{ award.url }}" target="_blank">{{ award.title_en }}</a></b> ({{ award.date }})
        <ul>
            <li>Collaborators: {{ award.authors_en }}</li>
            <li><a href="{{ award.result_url }}" target="_blank">[Official Results (News)]</a>
            {% if award.blog_url %}｜ <a href="{{ award.blog_url }}">[Technical Review Blog]</a>{% endif %}</li>
            <li>{{ award.description_en }}</li>
            <li>Tools used: <a href="/en/tools">mordred_descriptor_calculator</a></li>
        </ul>
    </li>
{% endfor %}
</ul>

<hr>

<h2>Presentations</h2>
<ul>
{% for pres in data.presentations %}
    <li>
        {{ pres.authors_en }}. "{{ pres.title_en }}". <b>{{ pres.event_en }}</b>, {{ pres.role_en }}, {{ pres.date }}.
        <ul>
            <li>Tools used: <a href="/en/tools">ecfp_cli</a></li>
        </ul>
    </li>
{% endfor %}
</ul>

<hr>

{% if data.publications.size > 0 %}
<h2>Publications</h2>
<ul>
{% for pub in data.publications %}
    <li>{{ pub.authors_en }}. "{{ pub.title_en }}". <i>{{ pub.journal_en }}</i>, {{ pub.year }}. <a href="{{ pub.url }}" target="_blank">[{{ pub.doi }}]</a></li>
{% endfor %}
</ul>
<hr>
{% endif %}

<h2>Software & Tools</h2>
<p><a href="/en/tools">For detailed specifications, see the <b>Software & Tools page</b>.</a></p>
<ul>
    <li>
        <b><a href="https://github.com/377H-Miru/ecfp_cli" target="_blank">ecfp_cli</a></b> (v0.1.1)
        <br>High-speed ECFP fingerprint generator. Used for data preprocessing in PSJ 146th annual meeting.
    </li>
    <li>
        <b><a href="https://github.com/377H-Miru/mordred_descriptor_calculator" target="_blank">mordred_descriptor_calculator</a></b> (v0.1.1)
        <br>Descriptor calculator with π-conjugated system support. Used for feature extraction in EUOS25 challenge.
    </li>
</ul>

<hr>

<h2>Education</h2>
<ul>
{% for edu in data.education %}
    <li>{{ edu.period_en }}: {{ edu.institution_en }}</li>
{% endfor %}
</ul>
