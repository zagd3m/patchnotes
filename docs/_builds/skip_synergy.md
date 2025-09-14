---
layout: build
title: Should you skip that synergy ?
summary: The cost of saving 20 points.
order: 8
---

## TLDR : read them graf

How much (in % of max dmg) is lost when skipping one (or several) synergies ?

<img src="{{ site.baseurl }}/assets/img/skip.png" alt="Skip Synergy Analysis" style="width: 100%; max-width: 800px; height: auto; display: block; margin: 0 auto;">

## Why this question ?

I often find myself wondering if I can skip a synergy, for example :

- You want to level a defensive spell (ex: Grizzly on Creeper Druid, or Bone Armor on Nova Necromancer)
- You want to level a utility spell (ex: Teleport on ... any sorc ^^)
- You're theorycrafting some bullshit meme build <-- this is me
- You're leveling, and can't max synergies yet

You know you are losing damage, but how much ? Can you afford to do so ?

Just read the graph:

- X axis shows the % of the synergy, for example 7% for Charged Bolt
- Y axis shows your total damage divided by the total damage if all synergies were maxxed

## Key takeaways

I'll express the takeaways in "damage lost", since that's probably how you think about it.

- Skipping all synergies is always a bad idea.
- Skipping one synergy on Nova removes ~30% of your total damage. On Chain Lightning that would be ~35%, and on Fireball that’s ~45%.
- Skipping 2 synergies on Blessed Hammer means doing almost no damage (~83% of damage is lost) vs ~31% at one skept.
- On 3-synergies spells, skipping one is a bit less abrupt, with for example Twister losing ~31% damage, and Vulcano ~29%. As we can see the synergy % doesn’t have a strong impact in this case (red line becomes flat fast).

## Small % synergies : still impactful !

I suppose the math here clearly shows that synergies play a very impactful role in PD2. They would be extremely impactful at 2-4% already, and most of them sit around 15-20%. This isn't a feedback post, but if you're interested in such a post, [check it here]({{ site.baseurl }}/full-notes#synergies).

<img src="{{ site.baseurl }}/assets/img/skip_few.png" alt="Skip Synergy Analysis" style="width: 100%; max-width: 800px; height: auto; display: block; margin: 0 auto;">

A spell at 2% synergies would have :

- 19% damage lost on 3-synergies spells (for 1 skipped)
- 23% damage lost on 2-synergies spells (for 1 skipped)

It still seems fair ! This shows how impactful synergies are, even at low percentage.

## Clean graphs

### 3 synergies spells

<img src="{{ site.baseurl }}/assets/img/skip_3.png" alt="Skip Synergy Analysis" style="width: 100%; max-width: 800px; height: auto; display: block; margin: 0 auto;">

### 2 synergies spells

<img src="{{ site.baseurl }}/assets/img/skip_2.png" alt="Skip Synergy Analysis" style="width: 100%; max-width: 800px; height: auto; display: block; margin: 0 auto;">

### 1 synergy spells

<img src="{{ site.baseurl }}/assets/img/skip_1.png" alt="Skip Synergy Analysis" style="width: 100%; max-width: 800px; height: auto; display: block; margin: 0 auto;">

## Case studies (of builds with unmaxed synergies)

### Blizzard + Ice Barrage sorc

Some sorcs use IB in combination with Blizzard, but they only share one synergy, wich means IB will deal less damage.

- IB with one synergy (skip one for a two-synergy spell at 8%) : 62%

This is pretty honorable as a seconday skill, which is why people do that. Also, IB will benefit from facets, skillets, ... making the combination easy to leverage.

### Vlada's hybrid trapsing

Vlada made a [guide for a hybrid trapsin](https://www.reddit.com/r/ProjectDiablo2/comments/1kncedb/wake_of_firelightning_sentry_tech_for_early_game/), where he argues you should level both WoF and Lightning Sentry.

- WoF with 1 synergy means skipping one of two, with 8% --> you still deal 61.90% of the skill's potential damage (if fully synergized)
- LS with 1 synergy means skipping two of three, with 16% --> you still deal 39.62% of the skill's potential damage (if fully synergized)

This might seem awful, but it's not. Actually, that's one of the "ok" scenarios, because at least trap skillers will buff both skills. If you did the same thing on a sorc, you'd also have to level 2 Masteries, which makes bi-elem sorc a thing of the past. #RIP

### Najova Necromancer

If we look at [my own guide here]({{ site.baseurl }}/builds/guide-najova/), with maxxed Nova + Fire Golems.

- Nova would do 100% of its damage, but as you level up you'll temporarily miss a synergy, which means retaining only 60% of the damage.
- Fire Golems would retain 50% of their damage (there's no chart for 4 synergies spells, so, you gotta trust me here ^^).

This isn't great, but it's not awful either, since you're effectively playing 2 builds at once, dealing 60% poison + 50% fire damage, and later 100% + 50% fire. With that said, as you gear up your character, it becomes far less optimal because of skillers, facets, and items (like Dweb or Flickering Flame) buff only one part of the build.

<!-- ---

## Is the math correct ?

Yes. At worse you'll have tiny rounding errors.

Examples below from in game testing.

### Poison strike

- 361-365 : 9,520083
- 2080-2100 : 54,7730
- 3799-3834

### Teeth

- 46-68 : 6,4947%
- 266-394 : 37,63%
- 487-720 : 68,76%
- 708-1047 : 100%

### CB - no mastery

- 13-15 : 25,86
- 32-37 : 63,79
- 51-58

### CB - mastery

- 45-52 = 26
- 110-126 = 63
- 174/200 -->