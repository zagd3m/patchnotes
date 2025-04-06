## Simplifying the game

Pillar #4 of Zagd3m's patch notes is noob friendlyness. And you know what isn't ? Things that are complex for no reason at all.

### Mods that don't work

Examples :

- Skills that don't benefit from %enhanced damage against demons
- Mods that don't do what they say (ex : %ed/max jewels before the bugfix)
- Bonuses that look good on paper but are not useful in practice (ex: IAS on a skill that doesn't benefit from IAS)

So let's fix this. (section in progress, TODO).

### Skill IAS

Skill IAS makes computing breakpoints very complex and tedious. Therefore, it breaks the QoL and Noob Friendliness principles / pillars. Let's fix this.

The formula has been changed from :

```d2
AnimRate + SIAS + EIAS - WSM
where EIAS = 120 * ItemIAS / (120 + ItemIAS)
```

To:

```d2
AnimRate + EIAS - WSM
where EIAS = 120 * (SIAS + ItemIAS) / (120 + (SIAS + ItemIAS))
```

Effectively, this means that IAS from skills (BoS, Fanaticism, ...) would count just like IAS from gear, instead of affecting a specific (and very effective) part of the formula. Simple. Obviously some skills and builds would need to be rebalanced, and a new (a lot simpler) calculator would need to be implemented, but that would be MUCH simpler.

### Fluid breakpoints

Breakpoints are a thing that we should fix. 

#### How it works now

For example, a player having 60% FHR when the breakpoints are 48 and 86 would have THE SAME effect of a player with 48 FHR.

#### Why it is the case

The game works with frames and therefore can't have a float value, that would be between x and x-1 frames. Frames are intrinsically integers.

#### How to fix it

In fact, we could have float frames. All it takes is to randomise between the float rounded up and rounded down, thus having a chance to use the slower of faster breakpoint. The likelyhood of this chance would depend on how far we are from the next breakpoint.

Example :

```math
# Compute the likelihood of using the faster breakpoint
current_fhr = 60
breakpoints = [48, 86]

range = 86 - 48
range_position = (60-48) / range = 31,57 = (rounded) 32

# Formula to use instead of rounding when the breakpoint is computed
rand = random(0, 100)
if rand < range_position:
    breakpoint = 86
else:
    breakpoint = 48
```

#### Consequences

This would not change much for most players. For example, sorcs would probably optimize for certain bps because they care about having 100% certainty of using the faster breakpoint. But for noobs, or for players who enjoy having a bit of extra leeway, this change would be welcome ... and totally makes sense intuitively. Having 60 FHR would effectively be slightly better than having 48. Problem solved.

For IAS, FHR, FCR, FBR, ...

### Unuseful mods

Mods that's weren't really useful have been removed.

If you find someone telling you this would indirectly buff rares/crafts, please note that (1) they need this and (2) rares are balanced by optimal combinations of mods, not by the possibility of trash mods. This has always been the case and will always still be.

#### Prevent Monster Heal

This mod doesn't work as well as poison and Open Wounds, while doing the same thing. Most of the time, an item doing a small amount of poison damage and open wounds would be better, or equivalent, to one with Prevent Monster Heal. Therefore, keeping this effect is creating clutter. Let's remove it for the sake of simplicity.

#### Replenish life --> Replenish life (per second)

No build leverages this mod, so it's either something we should remove or improve. I say improve !

Now displayed as replenished life per second (instead of 5 seconds, which made no sense at all). Yet, the healing is continuous, it doesn't "wait" for the end of the second.

That's it. Now, what we need is to buff the numbers until this starts being really useful.

#### Mana regeneration --> Replenish mana (per second)

Replaced by replenish mana, which is equivalent to replenish life. This is easier to understand, and it won't be broken anyway.

All items that were giving mana regeneration should now be giving replenish mana.
