---
layout: default
title: Builds & Guides
description: Browse all custom builds and guides for Project Diablo 2
permalink: /builds/
---

# Builds & Guides

Welcome to the builds/guides section!

I decided to move the builds I wrote for Project Diablo 2 here, to keep stuff up to date within my IDE. Lazy man.

{% assign sorted_builds = site.builds | sort: 'order' %}
<ul>
{% for build in sorted_builds %}
  <li>
    <a href="{{ site.baseurl }}{{ build.url }}">{{ build.title }}</a>{% if build.summary %} – {{ build.summary }}{% endif %}
  </li>
{% endfor %}
</ul>

## Other guides

If you want better builds, consider checking the [PD2 wiki](https://wiki.projectdiablo2.com/wiki/Links#Builds) !

- [Main website](https://www.projectdiablo2.com/)
- [Discord](https://discord.gg/projectdiablo2)
- [Reddit](https://www.reddit.com/r/ProjectDiablo2/)
- [Mark's PD2 Resources (aka Hiim)](https://maaaaaarrk.github.io/Hiim-PD2-Resources/index.html)
- [Support FAQ](https://wiki.projectdiablo2.com/wiki/Support_FAQ)
