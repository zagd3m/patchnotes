---
layout: default
title: Full Patch Notes
---

<!-- # Complete Patch Notes

This page contains all patch notes sections combined into a single document.

Please remember we are talking about FAKE patch notes. This is a huge feedback thread basically.

--- -->

<!-- * Table of Contents
{:toc}

--- -->

# Complete Patch Notes

> ### Quick links
> 
> - [Classes](#classes-changes)
> - [Items](#items-changes)
> - [Systems](#systems-changes)

{% assign sorted_sections = site.patchnotes | sort: 'order' %}
{% for section in sorted_sections %}
<!-- ## {{ section.title }} -->
{{ section.content }}
---
{% endfor %}