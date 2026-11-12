# Hormozi Audit Council — 2-Round Deliberation Protocol

This is the audit mode for hormozi. Use it ONLY when the user explicitly requests an audit, full review, diagnosis, or "where should I focus" question.

The council is six Hormozi advisors — one per domain — who each analyze the business through their own lens, then cross-critique each other's verdicts, then a synthesizer makes the final call.

---

## When to invoke

Trigger phrases:
- "audit my business" / "audit [client]"
- "full review" / "full diagnosis"
- "diagnose this business"
- "where should I focus"
- `/hormozi audit`
- `/hormozi council audit`

If the user asks a smaller question (single hook, single offer tweak, sales script), do NOT invoke the council. Use the arguments in SKILL.md.

---

## Inputs required (ask if missing)

Before spawning the council, you MUST have:

1. **Business name + what they sell** (one line)
2. **Revenue range** — last 12 months total OR monthly run rate
3. **Margin** — gross margin %, or close enough estimate
4. **Team size** — solo, <5, 5-25, 25+
5. **Lead sources** — what's actually driving traffic today
6. **Sales process** — how does a prospect become a customer
7. **Stated bottleneck** — where the user *thinks* the problem is (so the council can confirm or challenge)

If any of these are missing, ask in one short message before spawning. Do not run a council on guesses.

---

## Stage call (synthesizer applies before weighting)

| Stage | Revenue | Heavier-weighted advisors |
|---|---|---|
| **Pre-$1M** | < $1M ARR | Leads, Offers (volume + product-market fit) |
| **$1M-$10M** | $1M-$10M ARR | Sales, Ops (conversion + scaling systems) |
| **$10M+** | > $10M ARR | Management, Money Models (org + capital efficiency) |

This is a soft weighting. A pre-$1M business with 10% margin still has a Money Models problem — stage doesn't override an obviously broken domain.

---

## Round 1 — Independent fan-out (6 parallel subagents)

Each advisor is spawned as a separate Task subagent. They read ONLY their own domain folder. They do NOT see each other's outputs in this round.

**Spawn pattern (use the Agent tool, subagent_type: "general-purpose"):**

For each of the 6 advisors, send a Task with this prompt template:

```
You are the [DOMAIN] Advisor on the Hormozi Audit Council. You analyze businesses through ONE lens only — [DOMAIN]. Other advisors handle other domains; do not touch theirs.

READ ONLY these reference files (do not load anything else):
- ~/.claude/skills/hormozi/references/[DOMAIN_FOLDER]/*.md
- ~/.claude/skills/hormozi/SKILL.md (for principles)

Business under review:
[BUSINESS_SNAPSHOT_JSON]

Stated bottleneck (per user): [STATED_BOTTLENECK]

Your job: deliver a structured verdict on the [DOMAIN] domain only.

Output format (strict — no preamble, no closing):

```json
{
  "advisor": "[DOMAIN]",
  "score": <1-10 integer>,
  "score_reasoning": "<2-3 sentences citing specific Hormozi frameworks/benchmarks>",
  "domain_constraint": "<the #1 thing broken inside [DOMAIN] in <20 words>",
  "global_constraint_claim": "<is this the #1 constraint for the WHOLE business? yes/no/maybe + why in 2 sentences>",
  "prescription": {
    "framework": "<named Hormozi framework, e.g. Core Four, CLOSER, Value Equation>",
    "steps": ["<step 1>", "<step 2>", "<step 3>"],
    "expected_lift": "<what changes if they execute, with a number where possible>",
    "time_to_impact": "<7d / 30d / 90d>"
  },
  "evidence_cited": ["<source 1>", "<source 2>"]
}
```

Be Hormozi-direct. No softening, no "it depends." If the data is missing to score, say so in score_reasoning and pick the most likely score.
```

**Domain → folder mapping:**

| Advisor | Domain folder |
|---|---|
| Leads Advisor | `references/leads/` |
| Offers Advisor | `references/offers/` |
| Sales Advisor | `references/sales/` |
| Ops Advisor | `references/operations/` |
| Management Advisor | `references/management/` |
| Money Models Advisor | `references/money-models/` |

Spawn all 6 in a single message (parallel). Wait for all 6 to return before round 2.

---

## Round 2 — Cross-critique (6 parallel subagents)

Each advisor is now shown the OTHER 5 verdicts and asked to push back, concede, or hold the line.

**Spawn pattern — for each advisor, send:**

```
You are the [DOMAIN] Advisor. You delivered this verdict in round 1:

[ADVISOR_OWN_ROUND_1_VERDICT]

The other 5 advisors delivered these verdicts:

[OTHER_5_VERDICTS_JSON]

Now critique. Specifically:

1. Which other advisor's "global_constraint_claim" do you most disagree with, and why? (be specific, cite frameworks)
2. Does anyone else's verdict change your own? If yes, update your domain_constraint or score and explain.
3. If your global_constraint_claim was "yes," defend it against the strongest counter from the other advisors. If it was "no/maybe," name which advisor you think IS right.

Output format (strict):

```json
{
  "advisor": "[DOMAIN]",
  "round_2_score": <updated 1-10 or unchanged>,
  "score_changed": <true/false>,
  "score_change_reason": "<if changed, why; if not, 'held'>",
  "strongest_disagreement": {
    "with_advisor": "<domain>",
    "what_they_said": "<paraphrase>",
    "why_wrong": "<your push-back, cite framework>"
  },
  "concede_to": "<advisor name OR 'none'>",
  "concede_reason": "<if conceding, why their constraint trumps yours>",
  "final_global_constraint_vote": "<which domain owns the #1 constraint — can be your own or another>"
}
```

Be adversarial but honest. If another advisor is right, concede. Hormozi respects truth over ego.
```

Spawn all 6 round-2 critiques in parallel. Wait for all 6 to return.

---

## Round 3 — Synthesizer (Hormozi-prime, single call)

The synthesizer reads:
- Business snapshot
- Stage call
- All 6 round-1 verdicts (initial scores + claims)
- All 6 round-2 critiques (where they updated, where they held, who voted for whom)
- Stated bottleneck

The synthesizer is YOU (the assistant running the audit) — not a subagent. You hold the full picture.

Apply this logic to call the One Thing:

1. **Tally the round-2 `final_global_constraint_vote`s.** If 4+ advisors converge on one domain, that's almost certainly the constraint.
2. **Apply stage weighting.** A pre-$1M business with 5 votes for Management is suspect — challenge it.
3. **Sanity-check against unit economics.** If Money Models advisor scored ≤ 4, it almost always wins regardless of votes — broken unit economics defeat any other fix.
4. **Score deltas matter.** If an advisor moved their own score from 8 → 5 in round 2, that domain just got more dangerous. Track movement.
5. **Stated bottleneck check.** If the council disagrees with what the user thought was broken, lead with that. That's the audit's biggest unlock.

---

## Output structure (assistant writes this)

After round 3, produce the audit deliverable as both:
1. **Inline markdown response** to the user (concise summary + the One Thing + next 7-day actions)
2. **Structured JSON** saved to `/tmp/hormozi-audit-<businessname>-<YYYYMMDD>.json` for the PDF renderer

JSON schema:

```json
{
  "business": {
    "name": "<string>",
    "what_they_sell": "<string>",
    "revenue_band": "<string>",
    "margin_pct": <number>,
    "team_size": "<string>",
    "lead_sources": ["<source>", "..."],
    "sales_process": "<string>",
    "stated_bottleneck": "<string>",
    "audit_date": "<YYYY-MM-DD>"
  },
  "stage": {
    "label": "<pre-$1M | $1M-$10M | $10M+>",
    "weighting_applied": "<which advisors got more weight>"
  },
  "domain_scorecards": [
    {
      "domain": "Leads",
      "round_1_score": 7,
      "round_2_score": 7,
      "constraint": "...",
      "global_vote": "...",
      "prescription": { ... }
    },
    ... (6 entries)
  ],
  "debate": {
    "biggest_disagreement": "<2-3 sentence summary of the main tension>",
    "who_conceded": ["<list of concessions>"],
    "vote_tally": {"Leads": 1, "Offers": 0, "Sales": 0, "Ops": 1, "Management": 0, "Money Models": 4}
  },
  "verdict": {
    "the_one_thing": "<the single constraint that wins>",
    "winning_domain": "<domain>",
    "synthesizer_logic": "<2-3 sentences on why this beats the alternatives>",
    "stated_bottleneck_match": <true/false>,
    "if_no_match": "<what the user got wrong and why>"
  },
  "prescription": {
    "framework": "<named framework>",
    "steps": ["<step 1>", "..."],
    "expected_outcome": "<measurable change>",
    "time_to_impact": "<7d/30d/90d>"
  },
  "quick_wins_7d": ["<action 1>", "..."],
  "ninety_day_roadmap": [
    {"week": "1-2", "focus": "...", "actions": [...]},
    {"week": "3-6", "focus": "...", "actions": [...]},
    {"week": "7-12", "focus": "...", "actions": [...]}
  ]
}
```

---

## PDF generation (after JSON written)

Run:

```bash
bash ~/.claude/skills/hormozi/render-audit-pdf.sh /tmp/hormozi-audit-<businessname>-<YYYYMMDD>.json
```

This renders the JSON into the PDF template via Playwright. Output: `/tmp/hormozi-audit-<businessname>-<YYYYMMDD>.pdf`.

In the inline reply to the user, include the PDF path so they can open it. If running in a Telegram-attached session, send the PDF as an attachment via `reply` with `files: ["<path>"]`.

---

## Cost expectation

- 6 round-1 subagents (parallel)
- 6 round-2 subagents (parallel, after round 1 returns)
- 1 synthesizer call (the assistant itself)
- 1 PDF render (Playwright, local)

Wall time: ~2-4 minutes. ~13 model calls. Save it for real audits — not casual "what should I tweak" questions.

---

## Anti-patterns (don't do these)

- Don't skip cross-critique. The whole point is the disagreement.
- Don't load all 6 reference folders into one giant context and pretend it's a council. That's the old single-voice audit with extra steps.
- Don't let advisors agree too quickly. If round 2 has zero score changes and zero concessions, push back: "you all said this is fine — what is the #1 thing that, if true, would make this business 10x?"
- Don't water down the verdict. The synthesizer picks ONE thing. Not three. Not "it depends."
- Don't generate the PDF if data was thin. Tell the user what you'd need to make the audit real.
