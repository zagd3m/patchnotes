## Simplifying the game

Pillar #4 of Zagd3m's patch notes is noob friendlyness. And you know what isn't ? Things that are complex for no reason at all.

### Mods that don't work

Examples :

- Skills that don't benefit from %enhanced damage against demons
- Mods that don't do what they say (ex : %ed/max jewels before the bugfix)
- Bonuses that look good on paper but are not useful in practice (ex: IAS on a skill that doesn't benefit from IAS)

So let's fix this. (section in progress, TODO).

### Skill IAS

Skill IAS makes computing breakpoints very complex and tedious.

Therefore, the formula has been changed from :

```d2
AnimRate + SIAS + EIAS - WSM
where EIAS = 120 * ItemIAS / (120 + ItemIAS)
```

To:

```d2
AnimRate + EIAS - WSM
where EIAS = 120 * (SIAS + ItemIAS) / (120 + (SIAS + ItemIAS))
```

Effectively, this means that IAS from skills (BoS, Fanaticism, ...) would count just like IAS from gear. Simple.

Obviously some skills and builds would need to be rebalanced, and a new calculator would need to be implemented, but that woud be MUCH simpler.
