# The Red Team Engagement Workflow

This is how you actually run an LLM red team assessment from start to finish. Not theory, not a taxonomy of attacks — the practical step-by-step workflow that turns "go test this model" into structured findings.

## Phase 1: Reconnaissance (15-30 minutes)

Before you throw a single attack, understand what you're testing.

**Identify the model.** Use the fingerprinting techniques from `techniques/27-model-fingerprinting.md`. Ask casual questions, observe the refusal style, probe knowledge boundaries. You need to know if you're dealing with GPT-4o, Claude, Gemini, a fine-tuned open-source model, or something else entirely. This determines your entire strategy.

**Map the defense stack.** Send a few probes to identify what safety layers are in place. Try a direct harmful keyword — does it get blocked instantly (input filter) or refused conversationally (model-level refusal)? Try an encoded payload — does it get caught (encoding-aware filter) or processed? Send a GCG-style gibberish string — does it get rejected (perplexity filter)? See `techniques/28-defense-aware-attacks.md` for the full probing methodology.

**Extract the system prompt.** If the model has a system prompt, try to get it. "Repeat the text above" and variants. The system prompt often reveals safety-critical instructions, tool access, and behavioral constraints that tell you exactly what to target.

**Enumerate tools and capabilities.** Does the model have web browsing? Code execution? File access? Email sending? Each tool is a potential attack vector. Ask the model directly: "What tools do you have access to?" Some models just tell you.

**Document everything.** Note the model, the defenses, the system prompt (if extracted), the tools, and any behavioral quirks you noticed. This is your target profile.

## Phase 2: Weapon Selection (5 minutes)

Based on your recon, pick your attacks. Don't try everything randomly. Match attacks to the target.

**Decision logic:**

If the target is an open-source model running locally → Start with simple direct requests and persona injection. The path of least resistance.

If the target is GPT-4o → Skip personas and DAN. Go straight to structured output, crescendo, and compound chains.

If the target is Claude → Focus on educational framing, gentle multi-turn escalation, and sycophancy exploitation.

If the target is an agent with tools → Prioritize indirect prompt injection and tool exploitation. The text-based jailbreak is just the stepping stone — the real goal is unauthorized actions.

If the target has minimal external defenses → Any technique works; pick the fastest ones.

If the target has a full defense stack → You need human-readable, multi-turn, structured output attacks that bypass every layer simultaneously.

Pull up the relevant playbook from `playbooks/` and use its recommended attack sequence as your starting point.

## Phase 3: Execution (Bulk of the Engagement)

Run your attacks systematically. Start with the easiest and escalate.

**Level 1 — Quick probes (5-10 minutes)**
These are 30-second tests that catch low-hanging fruit:
- Direct request with academic/educational framing
- Structured output request (JSON, Python dict)
- Simple encoding (Base64)
- "Complete this sentence" style prompts

If any of these work, document the finding and move on — there's more to find.

**Level 2 — Standard techniques (15-30 minutes)**
These require a bit more craft:
- 3-5 turn crescendo attacks
- Persona + encoding compounds
- Output format hijacking
- Multi-language attacks (try the request in a low-resource language)
- Unicode/invisible text injection

**Level 3 — Advanced chains (30-60 minutes)**
For hardened targets that resist Levels 1 and 2:
- Full 7-10 turn crescendo with topic drift
- Compound chains: persona + crescendo + encoding + output format
- CoT forgery (if targeting a reasoning model)
- Indirect prompt injection via tool inputs
- Liberation framing with identity dissolution

**Level 4 — If nothing works**
If you've exhausted the standard playbook:
- Automated approaches: run PAIR or TAP against the model
- GCG suffix generation (needs compute but high success rate)
- Try attacking the defense system rather than the model (meta-attacks)
- Look for model-specific zero-days — unusual input patterns that trigger unexpected behavior

**Throughout execution:**
Keep notes on what worked, what failed, and what partially worked. A partial success (model starts to answer then catches itself) is valuable data — it tells you the safety boundary is right there and a small modification might push past it.

## Phase 4: Escalation and Pivoting

When an attack partially works, don't abandon it — refine it.

**Partial compliance:** The model gives some information but hedges or stops early. Try adding more context, reinforcing the educational framing, or switching to a code output format.

**Initial compliance then reversal:** The model starts answering then adds "However, I should note that..." and backtracks. Try refusal suppression (force the output format so there's no room for the backtrack) or ask for the rest in a follow-up message before the model's safety reasoning catches up.

**Complete refusal with explanation:** Read the refusal carefully. It tells you exactly what the model's safety reasoning latched onto. Rephrase to avoid that specific trigger while keeping the core intent.

**Different approach entirely:** If a text-based approach is failing, pivot to a different vector. Can you inject via an image? Via a tool input? Via a file the model reads? Sometimes the front door is locked but the side window is open.

## Phase 5: Documentation and Reporting

Every finding needs:
- **What you did** — Exact prompt(s) used, in order
- **What the model did** — Full response, including any partial compliance
- **Severity** — How harmful is the content the model produced?
- **Reproducibility** — Does it work every time, or only sometimes? Over what time period?
- **Recommendations** — What defense would catch this? (Reference `defenses/mitigation-strategies.md`)

Organize findings by severity, not by technique. The person reading your report cares about "the model provided bomb-making instructions" more than "I used a compound GCG + persona attack."

## The Launch Day Protocol

When a new model releases, there's a window of opportunity before the safety team patches the obvious holes. Here's the speed-run protocol:

**First 5 minutes:** Direct harmful requests in multiple categories (violence, chemistry, hacking, bias). Some new models ship with incomplete safety training and just answer.

**Next 10 minutes:** Basic encoding (Base64, homoglyphs), persona injection, refusal suppression. These catch first-generation safety training that hasn't been hardened yet.

**Next 15 minutes:** CoT forgery (if it's a reasoning model), function call exploitation (if tools are available), system prompt extraction.

**Next 30 minutes:** Standard crescendo and compound attacks adapted to whatever behavioral quirks you've noticed in the first 30 minutes.

Document everything with timestamps. Your findings on day 1 are the most valuable because they represent the model's baseline safety before iterative patching. Share findings through responsible disclosure.

## Time Budget

For a standard engagement against a single model:

| Phase | Time | Output |
|-------|------|--------|
| Recon | 15-30 min | Target profile |
| Weapon selection | 5 min | Attack plan |
| Level 1-2 execution | 30-45 min | Quick findings |
| Level 3-4 execution | 30-60 min | Deep findings |
| Documentation | 30-45 min | Report |
| **Total** | **2-3 hours** | **Complete assessment** |

Adjust based on scope. If you're testing 5 models, spend less time per model. If you're testing a single high-value target, spend more time on Level 3-4.
