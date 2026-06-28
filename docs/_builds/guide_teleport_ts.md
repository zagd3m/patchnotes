---
layout: build
title: Teleport Thunderstorm Sorc — A Journey
summary: A passive sorc build that kills with Thunderstorm while teleporting through content. No Nova, just lightning from the sky.
order: 9
---

During the Beta, I saw Dark Humility playing a Thunderstorm-only sorc with great success. The challenge was simple : don't use Nova, just teleport and passively let the light kill mobs. I thought I would give it a try, and challenged myself to play this build from the very start of the ladder : first character, straight into TS.

This post is about everything I learnt doing so. I hope it will help you enjoy this build too.

## TLDR

- Max Thunderstorm and synergies and Lightning mastery
- 20 to teleport really helps mitigate the damage penalty
- 20 to ES could be a survivability option, but I didn't really manage to make it work for me
- Infinity self-wield is the best option, with an A3 merc for Static
- The build is good if you oneshot mobs. Corrupted zones >> t3 imo, unless you have awesome gear

## Why would you play this build ?

### Pros

- It is a passive build (no skill, no potions, just teleport)
- You can grab loot while mobs die, so it is more effective than it seems (unless you kill without looting)
- It is a new build, so maybe you'd like to try it

### Cons

- Pretty fragile (you don't stun mobs like Nova sorcs do)
- Not as fast as Nova
- Can be boring (single button build)

## Leveling as a Teleport-TS sorc

I leveled as a Teleport-TS sorc straight away. It works. You'd probably be faster playing other builds like Blizzard or Chain Lightning, but I enjoyed it. Feel free to do the same!

A few tips:

- **Use precast gear early on.** This is a gamechanging habit — precast Thunderstorm, then swap to Wizardspike for survivability. The difference is noticeable.
- **Prioritize Thunderstorm first**, then synergies, then Teleport. ES can come later once you have the damage to actually farm.
- **Static Field from your A3 merc** carries you through the early levels when TS damage is still low.
- **No respec needed** if you follow the skill allocation above from the start.

## My journey trying different build variants

### Variant 1 : orb + shield to farm Arcane Sanctuary, before infinity

The idea here is simple: use a high-res shield (easy to craft + puzzlepiece) to hit 75@ and farm Arcane Sanctuary as your early mapping target.

It works, but it's not fast. Some tankier mobs survive several Thunderstorm procs, and you're just... waiting. That said, it's a perfectly fine way to get your first farm going before you have Infinity.

I tried all three merc options — A1 (Pus Spitter), A2 (tank), and A3. A3 felt the best because of Static Field, which helps a lot when your damage is still low.

For orbs, Skyfall is the obvious endgame pick, but before that, Wizardspike and Stormspike are both solid options. Since +skills don't affect Thunderstorm damage, what matters is the -%lightning res and (to a lesser extent) +%lightning damage they bring.

### Variant 2 : same with infinity merc

Once you get an Infinity merc, things open up. You can instantly start mapping, and the A2 merc brings some welcome tankiness to the mix.

The build is still on the slow side, though. I suspect that with enough slots filled with 5/5 rainbow facets, this configuration could be BiS — you'd reach high defense and PDR% while keeping your -%light res. But for most of us, self-wielding Infinity is very tempting because you get a massive amount of -%light res that would be extremely expensive to replicate with facets.

Full block is another tempting defensive option. My tests suggest it could work, but you need pretty GG gear to hit the FBR breakpoint while also maintaining your FCR and FHR. It's a lot of constraints to satisfy at once.

### Variant 3 : trying partial ES (it sucked)

I tried partial Energy Shield, both with hard points and with [Tempest](https://wiki.projectdiablo2.com/wiki/Class_Weapons#Tempest). Both were disappointing. To make partial ES worth it, you'd need a lot of PDR/MDR and life/mana per kill to sustain it — gear that's hard to fit into this build.

One thing worth noting: since Thunderstorm doesn't cost mana and your Teleport level is high, you don't really burn through mana. Investing heavily in mana per kill feels like a wasted slot — you'd rather optimize for damage or survivability.

### Variant 4 : Dark Humility Teleport Playstyle

This is the version Dark Humility tested during the S13 beta, and it's probably the most standard approach to the build.

The key choices are:

- A3 merc with Skyfall/Exile or dual Dream (I went dual Dream)
- Infinity self-wield
- Glass cannon itemization

It works well. Where it really shines is low-HP maps and corrupted zones — places where mobs die fast and the bottleneck becomes your mobility and how quickly you can pick up loot, not your damage.

## Non-Obvious Gear Options

So, obviously you'll go infinity staff / griffon / torch / anni / ... I'm not going to cover that.

Feel free to check my Armoury if needed : https://www.projectdiablo2.com/character/TeleportTS

Below are the choices you might find interesting, and give personalisation tips:

- **FCR** : I see people aim at 200% FCR, this isn't needed at all. You don't cast Nova, so you don't care. 105 is already enough - maybe even more than needed.
- **Armour** : That's where there's the most variation. I went with Corpsemourn for the tankyness minions bring, and I really love it. But on the offensive side, having a +2 armour with RBFs in there would really increase my damage output. Arkaine/Steel Carapace for the defensive ones, or Atma/Ormus/QueHegan for the more offensive ones.
- **Resistances** : Those are hard to find when you have no res on the weapon/shield slots (hi infinity). So you'll probably want to consider rare items since they can have quite a lot of resistances on gloves, rings, boots, ... Also look for lpk and mpk on those slots. Sure, you'll be losing some damage, but it's not that bad since Thunderstorm doesn't scale very hard at higher levels.
- **Staff** : Buy a staff with +teleport and +light mastery asap. Later on, people only pick +nova ones, and we don't care about nova ! I also picked a precast staff on swap (meaning I don't use CTA) - I find that to be comfortable.

## Thunderstorm damage calculation

Core mechanics:

- Thunderstorm can be precasted, and the precast influences its base damage (lightning level). After that, the +/- lightning from your gear counts, so you'll need to keep those on the main gear.
- This means that items like Stormspike, with +/- light but no skills, are surprisingly good for this build.
- Thunderstorm hits every 1 second, regardless of your FCR.

Rule of thumb is -5% light \>> + 1 skills \>> +1 Thunderstorm \>> +5% light (so +3/-5 lightning facets will be good enough most of the time).

- +1 to Thunderstorm increases your damage by ~1.9% (At level 40, you'll get (350-342)/342 = 2,3% increase, and at level 50 (430-422)/422 = 1,9%, ...)
- +1 to Teleport lowers teleport penalty (by 1%), effectively increasing your damage by close to 1% depending on your playstyle
- +1 to Lightning Mastery grants 10% lightning damage, which will realistically increase your effective damage by a bit less than 2% (The math is, damage_increase = 10% / (100 + existing_ligthning_mastery + gear_with_additional_lightning_damage)
- +1 to All Skills does all three (or +1 to Lightning skills)
- Lightning damage increased by 5% corresponds to 1/2 point to Lightning Mastery, which is ~1% damage increase
- Enemy lightning resistance reduced by x% is awesome. It increases your damage depending on the enemy existing resistance and your other sources of reduction. For exemple, if the enemy had 0% resists, than you gain 5% damage, but if it had 50%, then you gain 10% damage.

Other than that, you'll probably be looking for

- FCR : this might be very important if you teleport a lot (standard playstyle, aim for 105 or 200fcr), or secondary if you play a more static playstyle (63 might be enough)
- Defense : pd2 made this stat very desirable, and if you play a mercenary with defiance, this might be very impactful
- FHR : great to recover from hits — get what you can on gear without sacrificing FCR or -%light

## Not covered in this guide

- Bossing
- PvP

## Technical terms

- -%light : enemy lightning resistance reduced by x%
- +%light : lightning damage increased by x%

## Assumptions

- We will assume character level = 93, which is a realistic target for dads and moms
