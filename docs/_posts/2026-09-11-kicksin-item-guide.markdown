---
layout: post
title:  "Should Damage +X Work on Dragon Talon Kicks?"
date:   2026-09-11 14:00:00 +0200
description: Why Astreon's Damage +X affix dominates Dragon Talon kick damage, and whether PD2 should remove it from kicks.
---

If you're building a Dragon Talon kicksin in PD2, the best weapon for raw damage isn't a claw. It's **Astreon's Iron Ward**, a Paladin scepter.

That is surprising for a build whose defining attack is a kick. It is also a good example of how one small formula interaction can shape an entire item slot.

## The short version

PD2 kicks use a unified base damage formula:

```text
Base = Dex/4 or Dex/3 + boot damage + flat damage
Damage = Base × one large additive %ED bucket
```

The `Damage +X` affix is added to the base. It is therefore multiplied by the entire endgame %ED bucket — often around ×25. Astreon's +100–125 Damage is not a minor bonus: it is a huge source of kick damage.

The question is whether this is a good itemization choice, or just an engine interaction that makes a Paladin weapon the obvious Assassin weapon.

## Why Astreon wins

With a realistic endgame setup — Dragon Talon 30, both synergies at 20, 150 Strength, 150 Dexterity, and 300% additional gear ED — the comparison looks like this:

| Weapon | Average damage / kick | Main reason |
|---|---:|---|
| Astreon's Iron Ward | 6,718 | `Damage +112` is multiplied by the kick formula |
| Stalker's Cull | 5,810 | +skills, +Kick Damage, Deadly Strike |
| The Redeemer | 5,853 | `Damage +90` and +Damage to Demons |

Astreon's `Damage +112` contributes roughly **2,800 damage per kick** in this example. That is more than the total damage contribution of many complete items.

This is not because Astreon has a kick-specific identity. Its advantage comes from the generic `Damage +X` affix — a quirky modifier that historically behaves differently from normal weapon damage and interacts with several skills in unusual ways.

By contrast, Stalker's Cull is clearly designed to support an Assassin: it has Assassin skills, +Kick Damage, Deadly Strike, and Tiger Strike bonuses. Yet Astreon is still stronger for the primary attack because of one generic flat-damage affix.

## Why this might be a problem

### It weakens weapon identity

Weapon damage does not apply to kicks, so the weapon slot should ideally be about useful effects: Assassin skills, +Kick Damage, Deadly Strike, Crushing Blow, charge-up bonuses, or utility.

Instead, the biggest raw-damage option is a Paladin scepter. The build's best weapon is determined less by its identity and more by whether its `Damage +X` happens to enter the kick base.

### It reduces meaningful choices

If `Damage +X` works, Astreon is the obvious raw-damage benchmark. If it does not, several alternatives become more competitive.

### It is difficult to explain

The usual explanation is: “weapon damage does not apply to kicks.” The practical explanation is: “weapon damage does not apply, except this particular weapon-style `Damage +X` affix does.”

That distinction may be technically meaningful to the engine, but it is not intuitive to players.

## What would change?

Using the same example, removing `Damage +X` from kicks produces this comparison:

| Weapon | Current average | Without `Damage +X` |
|---|---:|---:|
| Astreon's Iron Ward | 6,718 | 3,941 |
| The Redeemer | 5,853 | 3,621 |
| Stalker's Cull | 5,810 | 5,810 |

This would make Stalker's Cull the stronger raw-damage option, while Astreon would still have a clear purpose through Crushing Blow and magic damage.

I would **not** remove every form of flat damage. The proposal should be narrower:

1. Remove the specific `Damage +X` affix from the kick formula.
2. Keep +Kick Damage as the dedicated kick modifier.
3. Keep off-weapon min/max damage such as War Traveler's `Adds 15–25 Damage`, unless testing shows that it creates the same problem. This makes sense: `Adds X–Y Damage` is the same kind of affix as +min/max damage on charms and jewels — generic gear damage that exists across many item types. If a charm's +max damage helps your kick, a pair of boots doing the same is coherent.
4. If compensation is needed, prefer **increasing the base damage gained from Dexterity** (e.g. a better divisor than `Dex/4`–`Dex/3`) over buffing boot base damage. This strengthens the build's identity — a Kicksin should want to invest in Dex — instead of just making the item hunt bigger.

The goal is not to punish kicksins. It is to stop one generic weapon affix from deciding the entire weapon slot.

## The fair objections

This is not an obvious balance fix.

**The Season 4 change was deliberate.** PD2 explicitly stated that kicks would benefit from flat `Damage +X`. Removing it would reverse a conscious buff, not correct an undocumented mistake.

**The damage loss is substantial.** Astreon loses about 41% average kick damage in the example above. If kicksins need that power to remain competitive, the change would need compensation elsewhere.

**The vanilla evidence is contradictory.** Some classic kicksin guides say flat physical damage did not work with kicks; another respected guide says `+X Damage` did work. The affix is historically inconsistent across skills, so claims about what “always” happened in vanilla should be treated cautiously.

**Smite raises a legitimate consistency question.** Smite also benefits from `Damage +X`, despite not using normal weapon damage. If PD2 removes the affix from kicks, should it also change Smite? The answer may reasonably be no — a shield attack has a stronger connection to the equipped item than a foot-based attack — but the distinction should be intentional. And there's a pragmatic argument too: Astreon and Redeemer are *Paladin* weapons. `Damage +X` working for Smite keeps those items relevant to the class they were designed for; on kicks it just lets an Assassin poach Paladin gear.

**This may be a niche issue.** Kicksins are not necessarily overpowered, and Astreon is not automatically the best choice for every situation. A targeted change may not be worth the complexity if the interaction is not harming the broader game.

## My conclusion

I think removing `Damage +X` from Dragon Talon is worth considering, not because Astreon is game-breaking, but because it creates the wrong kind of best-in-slot choice.

Astreon should be attractive because of Crushing Blow, magic damage, and its anti-undead identity. Stalker's Cull should be attractive because it is an Assassin weapon with kick and martial-arts synergies. Both can be strong without one generic affix deciding the comparison.

The strongest version of the argument is therefore not “Astreon is too powerful.” It is:

> **A weapon-specific flat-damage affix should not be the main reason a Paladin scepter beats Assassin claws on an Assassin kick build.**

That would make the weapon slot more coherent, more diverse, and more interesting — as long as the change is tested and compensated if necessary.

## A bigger question: should `Damage +X` exist at all?

There's a deeper question behind all of this. `Damage +X` is a weird affix — it looks identical to `Adds X–Y Damage` on an item tooltip, but it behaves differently across skills, doesn't display on the character screen, and its mechanics are arcane enough that veteran players disagree about how it worked in vanilla.

From a new player's perspective, `Damage +100` and `Adds 50–75 Damage` look like the same thing. They are not — one is a buggy engine relic that works on some skills and not others, the other is plain flat damage. That confusion costs real understanding.

Maybe the better fix isn't removing `Damage +X` from kicks — it's asking whether PD2 needs this affix at all, or whether it should be normalized into regular flat damage. That is a separate, bigger conversation. But it starts with the same observation: **a mechanic that only veterans understand is a mechanic that fails most of the playerbase.**
