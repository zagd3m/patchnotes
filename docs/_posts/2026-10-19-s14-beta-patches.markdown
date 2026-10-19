---
layout: post
title:  "Six Beta Patches in Four Days: What S14's Iteration Tells Us"
date:   2026-10-19 10:00:00 +0200
description: The PD2 Season 14 beta has shipped six patches in four days. Reverts, a rare-affix overhaul, a one-hour 256x poison bug, and a bugfix list long enough to raise questions. What it all says about how S14 is being built.
---

TLDR: The S14 beta is already six patches deep. Some tentative changes got tried, judged, and fully reverted. Some nerfs appeared out of nowhere. Poison dealt 256x damage for about an hour. And rares are quietly being made to matter again. If the streams were the announcement, the beta is the delivery ! And we love seing a team that listens hard and iterates fast — for better and ... occasionally for weird. But that's all hype!

## The reverts: listening is a feature, vision would help

The most interesting diffs aren't additions — they're take-backs:

- **Combustion** was nerfed in the tentative notes (cooldown 2.5s to 2s, synergies 12% to 10%), nerfed *harder* in beta #1 (synergies down to 8%), then fully reverted to Season 13 values in beta #3.
- **Mana per energy** for necro, sorc, and druid got buffed, then reverted to S13 values in the same patch (the per-level mana buffs stayed).
- **Multiple Shot** was buffed in the tentative notes (24 to 29 arrows), lost proc-chaining in beta #1, and got capped at 25 projectiles in beta #3. Classic overbuff, then the walk-back.

Here's my honest read. I appreciate that the team can try something, see it doesn't work, and take it back — that takes guts, and I said so on Discord. But I also wonder how the intent survives a total revert. If Combustion needed nerfing badly enough to hit it twice, the *goal* presumably still stands; did we just abandon it instead of retuning?

I sometimes feel there isn't a clear vision driving this — stuff gets tried because it sounds good, then cancelled when it doesn't land. My best guess for an "S14 is about ___" statement would be something like: bugfixes, guilds, and a few novel ideas to keep the game fresh. Which is fine, honestly! Senpai clearly reads the feedback — all of it — and that's a real quality. A designer who listens to everyone and tries what sounds great is better than a designer with a grand plan they never revisit. It's just also a drawback: without a stated intent, the feedback we give is aimed at a target we can't see. Tell us what you're trying to do Senpylove, and we might actually help you do it.

## The comedy section: 256x poison damage, for one hour

Beta patch #6 fixed poison-based attacks dealing **256 times** the intended damage. The note adds, beautifully, that the bug had existed for "roughly one hour since the previous patch." Somewhere out there is a poison necro who had the best sixty minutes of their Diablo career. This is what betas are for, and honestly it's delightful.

I hope it means the team is reworking the way poison works in general, because it's been a bit of a mess. The damage formula is weird and inconsistent and ... why ? Maybe we could have a simpler and more modern take on poison.

## Rares matter again: partial victory, claimed humbly

This is the sleeper story of the beta for me. Buried in patch #1 and the tentative notes is a real itemization shift:

- Rare chests, helms, and shields can roll **+2 to class skills**
- Class weapons can roll **+3 to tree skills**
- **30% FCR** on chest/shield, **20% FCR** on gloves/belts/amulets
- **Cannot Be Frozen** on chest/shield, **40% FRW** on boots
- Deadly strike and crushing blow moved **off circlets** and onto gloves (10-20%) and helms (20-30%)
- New "rare only" affixes and a system where higher map tiers improve your odds of rolling high-end affixes

I've argued before that [the best possible rares should have a chance to beat runewords]({{ site.baseurl }}/blog/runewords-are-not-end-game/) on each slot — that's the endgame I want: hunt for the great rare, rebuild around it. This patch moves real numbers in that direction. Does a +2 rare chest actually beat Enigma? Probably not today. But the floor is rising, and crucially it's rising on *every* slot, not just weapons. Knowing a rare drop can matter again changes how the loot filter feels, and that alone makes the game more fun.

Also, moving DS/CB off circlets is quietly excellent: it decouples melee builds from one mandatory item slot and spreads the hunt around. More item slots that can be great = more builds worth trying. That's the whole [Top 10]({{ site.baseurl }}/blog/top-10-changes/) thesis in one affix shuffle.

## The bugfix list is suspiciously long — and that's good news

Read the beta notes and one thing jumps out: the bugfix volume. Animation desyncs, controller crashes, stash edge cases, guild-hall phasing, DClone pillar behavior, tooltip lies — pages of it, more than a normal PD2 patch cycle produces.

Total speculation on my part, and I'll say it as exactly that — a guess — but I suspect the team has picked up AI-assisted coding tools, and this is what it looks like when a small team gets a force multiplier for unglamorous plumbing work. Maybe I'm wrong and they just had a very productive few weeks. Either way: the boring fixes nobody streams about are how a 25-year-old codebase stays alive, and this patch has a lot of them. More of this.

## Merc XP: a small thing worth celebrating

Beta #4 gives mercenaries full experience credit and removes the level-difference penalty (the owner-level cap stays). No more watching your merc fall behind because you outleveled the content keeping them alive.

I was one of the voices asking for this, so I'll just say: thanks, Senpai. Quiet fix, real quality of life.

## So what does it all mean?

Six patches in four days is not a design document — it's a conversation. The community says things, the team tries things, some stick and some bounce back. I'd still love a clearer shared intent, because right now everyone's feedback is aimed blind. But watching the beta actually *beta* — catching the 256x poison hour, reverting what doesn't work, sneaking a rare-affix overhaul under the radar — beats watching a patch get written in a basement and shipped final.

Keep iterating. And Senpai, if you write the "S14 is about ___" paragraph, I'll happily help you aim.
