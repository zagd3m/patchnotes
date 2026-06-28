---
layout: default
title: Blog
description: Blog posts about PD2 game design, patch notes, and project updates
permalink: /blog/
---

# Blog

{% assign sorted_posts = site.posts | sort: 'date' | reverse %}
<ul>
{% for post in sorted_posts %}
  <li>
    <a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a> – {{ post.date | date: "%B %-d, %Y" }}
  </li>
{% endfor %}
</ul>
