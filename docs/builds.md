---
layout: default
title: PD2 Builds & Guides — Project Diablo 2
description: Unofficial Project Diablo 2 build guides and seasonal tips — tested builds for Assassin, Paladin, Sorceress and more.
permalink: /builds/
---

# Builds & Guides

Real Project Diablo 2 builds I've actually played — skills, gear, and honest notes on what each one is good (and bad) at. You'll find a Travincal zealer for early ladder, a Naj's-set poison necro, several kicksin flavors, and a guide to chill team reset runs.

These are personal builds, not meta gospel — for the official wiki's build list, see the links at the bottom.

{% assign sorted_builds = site.builds | sort: 'order' %}
<ul>
{% for build in sorted_builds %}
  <li>
    <a href="{{ site.baseurl }}{{ build.url }}">{{ build.title }}</a>{% if build.description %} – {{ build.description }}{% endif %}
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
