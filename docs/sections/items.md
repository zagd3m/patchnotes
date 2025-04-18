---
layout: default
title: Items Changes
---

{% assign section = site.patchnotes | where: "title", "Items Changes" | first %}
{{ section.content }}
