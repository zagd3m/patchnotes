## Synergies

> TLDR : synergy percents above 3% are almost always a bad idea. 1% is enough more often than you think. Increasing base damage instead of synergies is almost always better. Math below. 

### Why synergies suck ... and how to fix it

> Synergies are the best way to erradicate build diversity.
> If PD2 sincerely wants to promote build diversity, it should lower synergies % dramatically.

Let me give you an example.

- Teeth has 3 synergies with 24% damage increase.
- If you max all 3, you deal 100% of the damage you can do (obviously).
- If you max only 2 of them, you deal 68,8% of the max damage.
- If you max only 1 of them, you deal 37,6% of the max damage.
- If you max none, you deal 6,49% of the max damage !!!

This means that Teeth is only playeable with almost all synergies maxed.

Now what If I wanted to play a Teeth / Poison Nova nec ? Well, I can't. There's no way both spells can be impactful enough to justify the hybrid build. A good question though is : what would be the **right** damage penalty in this case ? I mean, I agree that a hybrid build should be weaker than a dedicated build, but how much weaker ? Since I can't cast both spells at once, but the poison damage lasts for some time, I suppose somewhere 80% damage on both would make sense.

If I changed the synergies for Teeth to, say, 3%, the damage would go like this:

- 2 synergies: 78,5% damage
- 1 synergy : 57,14% damage
- 0 synergy : 35,71% damage

There is still a good reason to max synergies, but the spell is somewhat playable with 1 synergy only.

Now, with summons being great meat shields, I can see how this might be an issue on the necro. But what about a sorc ? Well, then, since she won't cast 2 spells at once, hybrid builds should probably deal around 75% of the total damage even with only one synergy... Which is a synergy percent of 1% !!!

With that said, I suppose you have a grasp on why synergy percents of 5 or more means you are FORCED to max the synergies, thus effectively DESTROYING all hybrid builds you might think of.

### What's a good fix ?

For most spells, having 2 synergies doing 3% each would be a good start.

- With 2 maxxed you deal 100% damage
- With 1 maxxed you deal 73% damage
- With 0 maxxed you deal 45% damage

This is a much better balance, and you can still justify a hybrid build.
Remember that hybrid builds need a hybrid gear too ; Rainbow facets aren't multi-elemental ! So the penalty is already huge anyways.

Now, there are situations where this would be OP, mostly when it comes to summons. This was simply a starting point to think from.

### YESBUT n°1 : With 3% synergies, we'll do less damage than with 20% synergies

Oh really ? Then we need to increase the base damage.

By how much ?

```math
old_damage = base * (100% + nb_synergies x 20 x synergy_percent)
new_damage = new_base * (100% + nb_synergies x 20 x new_synergy_percent)
```

To have old = new, you need to have :

```math
new_base = base * (100% + nb_synergies x 20 x synergy_percent) / (100% + nb_synergies x 20 x new_synergy_percent)
```

Problem solved, thank you very much.

*Now, the truth is, such a simple approach doesn't take into accound lld / mld and progression in the mid game, so it might be improved. But it's a very reasonable starting point.*

### YESBUT n°2 : Congratulations, proc builds are now broken

Do you know what happens when you move damage from synergies to the base damage ? Well, proc builds, at least those that leverage non-synergized spells (from other classes), just got a HUGE buff. That's a fact. As a result, let's acknoledge it.

First, let me make a few things clear:

- Fixing this might be as simple as lowering the proc level
- Proc builds are weak (apart from a few exceptions)
- Proc builds have been buffed by the addition of Innocence, but that's something we already fixed (see our changed to Innocence)

Overall, I think this isn't a fair objection to the synergy change we are doing. Yes we need to nerf synergies, and then we can balance proc levels accordingly. Simple.

### Conclusion regarding synergies

This patch will suggest many drastic reductions to synergies % while adding that the base damage will be buffed. Assume the above is used.
