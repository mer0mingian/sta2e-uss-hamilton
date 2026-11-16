# STA 2e Rules Core Reference (GM/Table)

Concise, STA 2e-faithful core mechanics reference for pen-and-paper GM/table use (USS Hamilton adaptation context). Drawn from local rules docs in `docs/game_mechanics/`.

## Quick Reference

| Topic | Core rule |
|---|---|
| **Task roll** | GM sets **Difficulty** (0-5). Choose **Attribute + Department** = **Target Number (TN)**. Roll **2d20** (normally; up to 5d20 with bonuses). Each die `<= TN` = 1 success. **Focus applies:** die `<= Department` = 2 successes (critical). **No focus:** natural `1` = 2 successes. Meet/exceed Difficulty to succeed; extra successes = **Momentum**. |
| **Complications** | Natural `20` = complication (range can increase, e.g. 19-20). May buy off a complication by adding **2 Threat** (if GM allows). Complications resolve after the task outcome. |
| **Success at Cost** | GM may allow success with automatic complication(s) instead of failure; no Momentum can be spent to improve a task that succeeded at cost. |
| **Momentum (group pool)** | Starts at 0; mission-level group resource, **max 6**. Unspent Momentum from a task goes to pool (bonus Momentum cannot be saved). Remove 1 at end of scene if possible. Common spends: buy d20s (1/2/3, Immediate), Create Trait (2), Keep the Initiative (2, Immediate), Obtain Information (1, Repeatable), Extra Major Action/Swift Action (2, +1 Difficulty), Extra Minor Action (1). |
| **Threat (GM pool)** | GM starts each adventure with **2 Threat per PC** (adjustable). Gained from: player Immediate Momentum paid as Threat, bought-off complications (+2), escalation (+1), NPC unspent Momentum, threatening circumstances, etc. Spent to empower NPCs, create complications/reinforcements/environment effects, etc. |
| **Determination (PC)** | Start each mission with **1**, max **3**. Spend only when a **Value** or mission **Directive** aligns: *Moment of Inspiration* (re-roll any dice after roll), *Perfect Opportunity* (set 1 die to 1 before roll), *Special Technique* (gain a temporary talent for scene). Gain by **Challenging** or **Complying** with a Value/Directive pressure, or other GM-awarded moments. |
| **Stress & Injury (PC)** | Stress track max = **Fitness** (modified by species/talents). **Avoid Injury:** suffer Stress equal to severity instead of taking Injury. **Fatigued** at max Stress: +1 Difficulty to all tasks and one attribute shut down (auto-fail tasks using it); recover from Fatigue mainly by rest or ally help. Injury = character trait with **severity** (typically 1-5) and causes **Defeated**; can increase severity by +2 Momentum (repeatable, max +2 total). |
| **Conflict structure** | Divided into **rounds** and **turns** (each character normally 1 turn/round). Turn passes between sides; **Keep the Initiative** (2 Momentum, Immediate) passes to ally once per side opportunity. Each turn: usually 1 minor + 1 major action (more via spends/options). |
| **Traits** | Words/phrases describing significant facts (situation, location, character, equipment). Traits make actions easier/harder/possible/impossible (often ±1 Difficulty); exist while true. **Potency** counts as multiple traits. |

> **Note:** Core STA 2e rule chapters in these docs use **Attribute + Department** terminology (Command, Conn, Engineering, Security, Medicine, Science). Source summaries sometimes echo this; use the exact terms your table expects, but be consistent with the source when citing.

## Sources (primary)

- Core mechanics, scenes/traits/tasks, Momentum/Threat/Determination: `docs/game_mechanics/sta2e_rules/sta2ecore_ch07.md`
- Conflict structure, Stress/Injury, social/personal/starship conflict: `docs/game_mechanics/sta2e_rules/sta2ecore_ch08.md`
- GM adjudication, tasks/traits/Threat guidance, extended tasks/challenges: `docs/game_mechanics/sta2e_rules/sta2ecore_ch09.md`
- NPC categories, Personal Threat/Values, injuries: `docs/game_mechanics/sta2e_rules/sta2ecore_ch11.md`
- Character elements, attributes/departments/values/focuses/talents (context): `docs/game_mechanics/sta2e_rules/sta2ecore_ch04.md`
- Equipment/weapons baseline (context): `docs/game_mechanics/sta2e_rules/sta2ecore_ch06.md`
- Consolidated play aids: `docs/game_mechanics/rules_summary.md`, `docs/game_mechanics/cheat_sheet.md`
- Spend tables: `docs/game_mechanics/sta2e_rules/data_tables/momentum_spends.csv`, `docs/game_mechanics/sta2e_rules/data_tables/threat_spends.csv`, `docs/game_mechanics/sta2e_rules/data_tables/determination_spends.csv`
- Supporting reference: `docs/game_mechanics/objects.md`

## 1. Scenes, Missions, and Framing

- Gameplay is structured in **scenes**; scenes are building blocks of a **mission** (`sta2ecore_ch07.md`).
- GM establishes scenes (who/what/when/where/why), sets relevant **traits**, frames actions, resolves outcomes, and ends scenes when nothing worthwhile remains (`sta2ecore_ch07.md`, `sta2ecore_ch09.md`).
- **Encounters** are tightly structured scenes (e.g. combat) split into **rounds** and **turns** (`sta2ecore_ch07.md`, `sta2ecore_ch08.md`).
- End-of-scene upkeep noted in GM guidance includes effects ending, ship/state resets as relevant, and removing 1 Momentum from pool if possible (`sta2ecore_ch09.md`).

## 2. Traits

- **Trait:** a word/short phrase describing a significant fact about a situation, location, character, or equipment (`sta2ecore_ch07.md`).
- Effects: can make actions easier, harder, possible, or impossible (commonly ±1 Difficulty; GM may apply other fitting effects). Traits exist only while true (`sta2ecore_ch07.md`, `sta2ecore_ch09.md`).
- **Potent traits:** potency number counts as multiple traits (e.g. `Thick Smoke 2`) (`sta2ecore_ch07.md`).
- Changing traits: actions can create/remove/replace traits (often a task at Difficulty 2, context-dependent) (`sta2ecore_ch07.md`).

## 3. Task Resolution

**Core loop** (`sta2ecore_ch07.md`, `rules_summary.md`, `cheat_sheet.md`):
1. GM sets **Difficulty** (usually 0-5) and names relevant factors/traits.
2. Player chooses **Attribute + Department** for the approach; total = **Target Number**.
3. Build dice pool: start at **2d20**; add bonus d20s from talents/effects and by spending **Momentum** or adding **Threat** (1 for 1st, +2 for 2nd, +3 for 3rd). **Max 5d20**.
4. Optional assistance (teamwork): first assistant free; each extra costs 1 Momentum or adds 1 Threat. Assistants roll 1d20 using their own TN/focus; their successes count only if leader scores at least 1 success. Assisting in conflict usually takes the assistant's turn/availability (`sta2ecore_ch07.md`).
5. Roll: each die `<= TN` = 1 success. **Critical success** = 2 successes: if a Focus applies, any die `<= Department` rating; if no Focus applies, natural `1`. Natural `20` (or within complication range) = complication.
6. Success if successes >= Difficulty. Extra successes = Momentum. On failure, task fails unless GM allows **Success at Cost**.

**Difficulty 0:** automatic success with 0 successes and no Momentum/risk unless GM/player opts to roll for possible Momentum and complications (`sta2ecore_ch07.md`).

**Opposed tasks:** reactive character rolls to set Difficulty (their successes); active character must meet/exceed it. If active fails, reactive may gain Momentum from margin (per opposed-task rules). External factors can adjust (`sta2ecore_ch07.md`).

**Complication range:** default 1 (20). Range increases make complications occur on wider high rolls (e.g. 2 => 19-20, up to 5 => 16-20) (`sta2ecore_ch07.md`, summaries).

## 4. Momentum

- **Generation:** successes beyond Difficulty on a successful task.
- **Pool:** shared group pool, max **6**, not saved indefinitely (remove 1 at end of scene if possible). Bonus Momentum must be spent when granted or lost (`sta2ecore_ch07.md`).
- **Immediate spends:** can be paid from pool or by adding Threat instead of spending Momentum (e.g. buying d20s, Keep the Initiative) (`sta2ecore_ch07.md`, `momentum_spends.csv`).

| Spend (common) | Cost / type | Effect (summary) |
|---|---:|---|
| Create Opportunity (Buy d20s) | 1,2,3; Immediate, Repeatable | Add up to 3 extra d20s before rolling (max pool 5d20). |
| Create Trait | 2 | Create/change/remove/increase potency of a trait tied to the task/result. |
| Keep the Initiative | 2; Immediate | Pass action to an ally instead of opposition (limited per side flow). |
| Obtain Information | 1; Repeatable | Ask GM a relevant question; truthful but not necessarily complete. |
| Reduce Time | 2 | Halve time for non-action-scene activity (GM adjudicates). |
| Swift Action / Extra Major Action | 2 | Additional major action this turn; that action's task +1 Difficulty. |
| Extra Minor Action | 1 | Additional minor action (each minor action once/turn). |

*Sources: `sta2ecore_ch07.md`, `data_tables/momentum_spends.csv`, `rules_summary.md`.*

## 5. Threat

- **GM resource** mirroring Momentum for adversaries/NPC pressure and narrative control (`sta2ecore_ch07.md`, `sta2ecore_ch09.md`).
- **Starting amount:** 2 per PC by default (adjust for tone) (`sta2ecore_ch07.md`).
- **Typical gains:** Immediate Momentum paid as Threat, escalation (+1; lethal force is escalation), buying off complications (+2 each), NPC unspent Momentum, threatening circumstances/NPC abilities, etc. (`sta2ecore_ch07.md`, `sta2ecore_ch09.md`).
- **Typical spends:** NPC Momentum-equivalent uses, NPC complication buyoff (2), create complications (2), reinforcements (Minor 1 / Notable 2 / ship = Scale), environmental/narrative effects (varies), etc. (`sta2ecore_ch07.md`, `sta2ecore_ch09.md`, `data_tables/threat_spends.csv`).

## 6. Determination, Values, and Directives

- **Values:** short statements of beliefs/identity/relationships that can help or hinder (`sta2ecore_ch04.md`, `sta2ecore_ch07.md`).
- **Directives:** mission/group orders/constraints (objectives/prohibitions) usable like values in context (`sta2ecore_ch07.md`, `sta2ecore_ch09.md`).
- **Determination pool:** 1 at mission start, max 3 (`sta2ecore_ch07.md`).

| Determination spend | Timing / effect |
|---|---|
| Moment of Inspiration | After dice rolled: re-roll any number of d20s. |
| Perfect Opportunity | Before rolling (after buying extra dice): set one d20 to 1 (critical). |
| Special Technique | Gain one talent you don't possess for rest of scene (must meet prerequisites; GM may veto). |

| Gain context | Effect |
|---|---|
| Challenge a Value/Directive | Act against it; cross out (rewrite/change later per development flow), gain 1 Determination. |
| Comply with a Value/Directive | Accept hindrance/complication from it, gain 1 Determination. |

*Sources: `sta2ecore_ch07.md`, `data_tables/determination_spends.csv`, `rules_summary.md`.*

## 7. Character Resources and States (Play Basics)

- **Attributes (6):** Control, Daring, Fitness, Insight, Presence, Reason. **Departments (6):** Command, Conn, Engineering, Medicine, Science, Security. **Focuses** narrow expertise and affect critical-success thresholds when applicable (`sta2ecore_ch04.md`, `sta2ecore_ch07.md`).
- **Stress:** main PCs track Stress up to Fitness (species/talents may modify). Spend/mark Stress to avoid consequences (commonly Injuries). **Fatigued** at max Stress: +1 Difficulty all tasks and choose one attribute that auto-fails while Fatigued (`sta2ecore_ch08.md`).
- **Stress recovery (examples from summaries):** Momentum after success (2 Momentum => remove 1 Stress, Repeatable, max 3 per task this way), rest (breather/break/sleep restore increasing amounts) (`rules_summary.md`, `cheat_sheet.md`; see `sta2ecore_ch08.md` for full context).
- **Injuries:** attacks/hazards inflict Injury (trait) with severity (typically 1-5). Suffering Injury causes **Defeated**. Avoid Injury by taking Stress = severity (prevents that Injury/Defeat instance). Severity may be increased on successful attack by spending 2 Momentum (Repeatable, up to +2). **Protection** reduces injury severity/cost per rules context (`sta2ecore_ch08.md`, summaries).
- **Recovery/healing highlights:** First Aid can end Defeated or treat Injury in-scene; full medical treatment/removal takes longer and depends on severity/treatment state (`rules_summary.md`, `cheat_sheet.md`).

## 8. Conflict Basics

### Structure and actions
- Rounds/turns; GM selects first actor by situation (PC default/high Daring tie logic, NPC ambush, or Threat spend in uncertainty). Turns alternate between sides in general flow; Keep the Initiative allows ally-to-ally pass with constraints (`sta2ecore_ch08.md`).
- **Minor actions** support major actions (examples: Aim, Draw Item, Interact, Movement, Prepare, Stand/Drop Prone). **Major actions** include Assist, Attack, Create Trait, Direct, First Aid, Guard, Pass, Ready, Sprint, other tasks (`sta2ecore_ch08.md`, summaries).

### Social conflict
- Driven by requests/goals; target may **Yield** or **Resist**. Resisting can become opposed and may impose Stress/costs; social tools include **Deception, Evidence, Intimidation, Negotiation** to change context (`sta2ecore_ch08.md`).

### Personal conflict
- Uses zones/range/cover/terrain concepts. **Attacks:** choose weapon/target and Stun or Deadly intent (Deadly adds 1 Threat). Melee/ranged attacks have different default task setups and can become opposed (defense/cover). Successful attack inflicts Injury (and Defeat) unless avoided/countered per rules (`sta2ecore_ch08.md`, summaries).
- Common combat Momentum spends include Added Severity, Disarm, Extra actions, Keep the Initiative, Obtain Information, obstacle/terrain movement costs, etc. (`cheat_sheet.md`, `rules_summary.md`).

### Starship conflict (foundations)
- Structured like other conflicts with ship-scale actions/stations, breaches/damage systems, and starship-specific action/momentum options (`sta2ecore_ch08.md`, summaries/cheat sheet tables). Use station/action references in summaries for quick play; consult `sta2ecore_ch08.md` for full procedures.

## 9. NPCs and Adversaries (Quick Rules)

- **Categories:** Minor, Notable, Major (`sta2ecore_ch11.md`).
  - **Minor:** no Stress track mechanics like PCs; defeated by any successful attack; cannot Avoid Injury; no focuses/values (incidental).
  - **Notable:** Personal Threat (typically 3), may Avoid Injury once per scene by spending Threat; has limited focuses/value.
  - **Major:** larger Personal Threat (6+ typical), can Avoid Injury by spending Threat as available; more fully developed.
- **Personal Threat:** NPC-specific pool for options affecting that NPC; refreshed at start of each scene NPC appears in (cannot generally replenish mid-scene except value-related case noted). NPC values can convert to/from Threat effects instead of Determination (`sta2ecore_ch11.md`).
- **NPCs and Momentum/Threat:** adversary NPCs do not bank group Momentum; excess can add to Threat; GM uses Threat for NPC benefits mirroring PC Momentum as appropriate (`sta2ecore_ch07.md`, `sta2ecore_ch11.md`).
- NPC starships use **Crew Quality** ratings instead of individual crew stats in many cases (`sta2ecore_ch11.md`, summaries).

## 10. Extended Tasks and Challenges (GM Tools)

- **Extended tasks:** multi-attempt activities tracked by progress/work toward completion, used when time pressure, risk, or complexity matters (not for trivial/no-consequence actions). Can include resistance/impact/breakthrough effects and may be timed/challenging (`sta2ecore_ch09.md`, `sta2ecore_ch07.md` context).
- **Challenges:** break hard problems into several easier linked tasks/steps to maintain pacing and progress (`sta2ecore_ch09.md`).
- **Extended consequences / trouble tracks:** represent worsening situations driven by failures/complications/events rather than player "attacks" on the problem (`sta2ecore_ch09.md`).

## 11. Gaps, Ambiguities, and Doc Notes

- **Terminology consistency:** 2e core chapters in this folder use **"Department"**; some project/domain materials elsewhere may say "Discipline". This reference follows the `docs/game_mechanics/sta2e_rules/*` wording.
- **Condensed vs. full text:** `rules_summary.md` and `cheat_sheet.md` are convenient play aids but include some long pasted sections and minor formatting artifacts; treat `sta2ecore_ch07.md`-`ch11.md` as primary for adjudication.
- **Tables completeness in this reference:** detailed station/action/weapon/quality tables are extensive in source docs; this file summarizes principles and points to source tables (especially `sta2ecore_ch08.md`, `cheat_sheet.md`, `rules_summary.md`, `data_tables/*.csv`) rather than duplicating every row.
- **Edition/ruling drift:** project-local rulings may differ in implementation contexts (e.g. other repo docs mention specific house rulings). For table play from these docs, prefer the cited STA 2e source text above.
- **Truncated reads during extraction:** not every chapter was exhaustively transcribed here; sections chosen to cover requested core concepts (task resolution, Momentum/Threat/complications, Determination/Values, Stress/Injuries, combat/conflict, traits, scenes/missions, NPC/extended-task basics). For edge cases, consult the cited chapter directly.

