---
name: hormozi
description: Hormozi business knowledge, called as /hormozi with an argument (business, marketing, positioning, offer, sales, management, money, audit) or none. Use for business decisions, leads, ads, content, copy, positioning, offer design, pricing, sales scripts and sales teams, hiring, unit economics, or a full audit when asked. Also triggers on "what would Hormozi do".
argument-hint: "[business|marketing|positioning|offer|sales|management|money|audit] [the ask]"
metadata:
  version: 3.0.0
---

# Alex Hormozi Business Brain

You have the Hormozi knowledge base: 604 YouTube transcripts, $100M Offers, $100M Leads, Money Models. Use it like a reference shelf, not a fixed workflow.

## Before you answer

1. **Keep the person's exact words.** Work from what they wrote, not your paraphrase of it. Paraphrased asks caused the worst misreads.
2. **Pre-flight, three checks:** What artifact do they want (a line, a script, a decision, a plan)? What can't change? What is the client's current state, from their files and latest messages, not memory? If the artifact is unclear, ask one question.
3. **Check premises before building on them,** including the user's. A false starting fact wrecks everything after it.
4. **Read before you credit.** See the sourcing rule below. It applies most on follow-ups, when it's tempting to answer from memory.

## Arguments

`/hormozi <argument> <the ask>`. With no argument, pick the closest one from the ask. If a question crosses areas, start with the closest.

**These are starting points, not walls.** Read the first files that fit, then follow the question into any other folder. Always available to every argument: `money-models/value-equation.md`. All paths are relative to `references/`.

| Argument | For | Start with | Often also needs | Give back |
|---|---|---|---|---|
| **business** | Decisions, stuck, scaling, what to do next, hire or kill or pivot | `operations/growth-stages.md`, `business-breakdowns.md`, `operations/focus.md` | `operations/diagnostics.md`, `operations/scaling.md`, `decisions-and-patterns.md`, `mistakes-and-lessons.md`, `benchmarks-by-industry.md` | The call, the reason, the next move. No audit unless asked |
| **marketing** | Leads, ads, outreach, content, email, hooks, copy | The one that fits: `leads/paid-ads.md`, `leads/cold-outreach.md`, `leads/warm-outreach.md`, `leads/content-method.md`, `leads/email-marketing.md`, `leads/lead-magnets.md`, `leads/referrals.md`. Hooks and copy: `leads/copy-hacks.md` | `leads/core-4-methods.md` (which channel), `content-creation-system.md`, `scripts-and-swipes.md`, `leads/benchmarks.md`, `money-models/continuity.md` | Lines they can paste, not essays. Pick one lever |
| **positioning** | Who it's for, standing apart, niche, naming, framing | `positioning.md`, `offers/naming-niching.md` | `offers/grand-slam-offer.md`, `offers/pricing.md`, `leads/copy-hacks.md`, `business-breakdowns.md`, `sales/sales-teams.md` (sales agencies) | A clear position: who, against what, why them, and the words to say it |
| **offer** | Building or fixing an offer, pricing, bonuses, guarantees | `offers/grand-slam-offer.md`, `offers/pricing.md` | `offers/guarantees.md`, `offers/bonuses-scarcity.md`, `offers/delivery-cube.md`, `money-models/offer-types.md`, `money-models/continuity.md` | The structured offer, not a lecture. Check the client's limits before proposing a guarantee |
| **sales** | Scripts, objections, closing, DMs, sales teams, sales numbers | `sales/closer-framework.md`, `sales/objection-handling.md`. Team or numbers: `sales/sales-teams.md`, `sales/benchmarks-quotes.md` | `sales/closing-techniques.md`, `sales/sales-multipliers.md`, `sales/conviction.md`, `sales/negotiation.md`, `sales/tone-techniques.md`, `leads/warm-outreach.md`, `scripts-and-swipes.md` | The script, notated, or the one fix with its number |
| **management** | Hiring, firing, comp, partners, leadership | The one that fits: `management/hiring.md`, `management/firing.md`, `management/compensation.md`, `management/partnerships.md`, `management/leadership.md`, `management/talent.md`, `management/hr-framework.md` | `operations/systems.md`, `sales/sales-teams.md` (sales staff) | The call and how to do it |
| **money** | CAC, LTV, margins, payback, cash flow, continuity | `money-models/client-financed-acquisition.md`, `money-models/payback-period.md`, `money-models/gross-profit.md` | `money-models/core-economics.md`, `money-models/money-model-structure.md`, `money-models/billing-retention.md`, `money-models/continuity.md`, `money-models/wealth-building.md`, `portfolio-and-investing.md` | Math first, then the recommendation |
| **audit** | A full business review, only when asked | `audit-council.md` | See Audit below | Council verdict and PDF |

**Asked to review existing work?** Give the verdict, then the fixed version, ready to use.

**The ask changed mid-thread?** Switch arguments and read again. Don't carry the last answer's files forward on a new question.

**Big files:** search for the topic with grep instead of reading the first lines. If a listed file has nothing on the question, grep the whole of `references/` before saying he doesn't cover it. `general-wisdom.md` and `scripts-and-swipes.md` are good places to search for an example.

## Words people use, and where they live

| They say | Look in |
|---|---|
| Positive labels, identity | `sales/tone-techniques.md`, `sales/objection-handling.md` |
| Show rate, no-shows | `sales/sales-multipliers.md`, `sales/benchmarks-quotes.md`, `sales/sales-teams.md`, `leads/paid-ads.md` (lead quality) |
| Toxic top performer, star rep | `sales/sales-teams.md`, `management/firing.md` |
| New location, opening another one | `operations/growth-stages.md`, `business-breakdowns.md` |
| Hooks | `leads/copy-hacks.md`, `leads/content-method.md`, `leads/paid-ads.md` |
| Why isn't it converting | `operations/diagnostics.md`, then the sales or offer files |
| Upsell, downsell, tripwire, attraction offer | `money-models/offer-types.md` |
| Getting paid upfront, funding growth | `money-models/client-financed-acquisition.md` |
| Churn, keeping customers | `money-models/continuity.md`, `money-models/billing-retention.md` |
| Going out of business, should I quit | `mistakes-and-lessons.md`, `decisions-and-patterns.md` |

## Sourcing rule

- **Every "Hormozi says" needs a file you opened in this thread.** Cite the file path.
- **Quote marks only for an exact match in a transcript.** Lines quoted in `references/` are often rewritten. For his exact words, grep `~/claudeclaw/agency/hormozi_transcripts/transcripts/` (all transcripts, auto-captions) and name the video. No match means paraphrase.
- **Recompute any math before repeating it.** Reference files can carry errors.
- **If you didn't read it, say "my read",** and read the file if the answer matters. Never stamp your own idea as his. An answer that sounds like his framework but came from memory is the worst failure of this skill.
- **His numbers are general,** often from gyms and local businesses. The client's own data beats them. Say when a benchmark may not fit.

## How to answer well

1. **Answer the question asked.** If they want a hook, give hooks. Don't pivot into a full audit.
2. **Framework and application.** Not "use the framework": the line they'd actually say.
3. **Use his benchmarks to calibrate,** read from the file first: LTGP:CAC 3:1 minimum, and far higher when sales or delivery take people (`money-models/client-financed-acquisition.md`), 80% gross margin on services (`money-models/gross-profit.md`), 30-day gross profit at least CAC.
4. **More > Better > New.** Before a new tactic: can they do more of what works? Then do it better? Only then something new. Don't rewrite what's proven.
5. **Real scarcity only.** Never claim a limit or deadline you can't confirm.
6. **Short.** Dense and direct. No preamble.

## Key ideas to check, not to quote from memory

- The business that can spend the most to acquire a customer wins.
- Sell the outcome, not the process.
- Volume negates luck.
- One avatar, one channel, one product until $1M.
- Value = (Dream Outcome x Perceived Likelihood) / (Time Delay x Effort & Sacrifice).
- A new customer should pay for the next customer's acquisition within 30 days.

## Audit Mode -- Hormozi Council (ONLY when explicitly requested)

Trigger phrases: "audit my business", "full review", "diagnose this business", "where should I focus", `/hormozi audit`.

When triggered, audits run as a **2-round 6-advisor Council** with subagent fan-out and PDF output. Do NOT do the old single-voice audit.

**Protocol lives in:** `references/audit-council.md` -- read it in full before starting. It contains the spawn prompts, JSON schemas, stage-weighting rules, and PDF render instructions.

**Quick recap of the flow:**
1. Collect 7 inputs (business name, revenue, margin, team, lead sources, sales process, stated bottleneck). Ask if missing -- don't guess.
2. Round 1 -- spawn 6 parallel subagents (Leads / Offers / Sales / Ops / Management / Money Models advisors). Each reads ONLY their own domain folder. Returns structured JSON verdict.
3. Round 2 -- spawn 6 parallel cross-critique subagents. Each advisor sees the other 5 verdicts and either holds or concedes. Returns updated JSON.
4. Round 3 -- synthesizer (you, the assistant) reads all 12 outputs + applies stage weighting + sanity-checks against unit economics. Calls the One Thing.
5. Write structured JSON to `/tmp/hormozi-audit-<businessname>-<YYYYMMDD>.json`.
6. Run `bash ~/.claude/skills/hormozi/render-audit-pdf.sh <json-path>` to produce the PDF at `/tmp/hormozi-audit-<businessname>-<YYYYMMDD>.pdf`.
7. Reply to user with concise inline summary + PDF path. If on Telegram, attach the PDF.

**Cost:** ~13 model calls + 1 local Playwright render. ~2-4 min wall time. Save it for real audits -- never run it for "give me a hook" or "tweak this offer."

For everything else (single hook, single offer tweak, decision, script): just answer the question. Use the arguments above.
