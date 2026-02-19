# 🔴 Red Team Knowledge Base

**A no-BS collection of LLM attack techniques, jailbreaks, and adversarial prompts — built for security researchers who actually test models.**

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## ⚠️ Read This First

**This repo exists for one reason: to help people test AI models and make them safer.**

Everything here — the prompts, the attack chains, the payloads — is meant to be used with permission. You test your own systems, you test systems you've been hired to test, or you use it for academic research. That's it.

**Do not** use this to harass people, generate harmful content for distribution, or bypass safety on systems you don't own. If you find a real vulnerability in a commercial model, practice responsible disclosure — report it to the vendor before you tweet about it.

I built this because I was frustrated by how scattered red team knowledge is. There's no single place where a researcher can go and say "give me everything." Research papers bury the actionable stuff under 20 pages of methodology. Blog posts cover one technique and miss the big picture. This repo connects all of it.

If this helps you find a vulnerability that gets patched — that's a win for everyone.

**Use responsibly. Test with permission. Make AI safer.**

---

## 🤷 What's in here?

I've organized everything into four buckets:

- **`techniques/`** — How the attacks actually work. Not theory — real mechanics, real payloads, why they bypass safety.
- **`payloads/`** — Copy-paste stuff. Jailbreak prompts, adversarial triggers, multi-turn scripts. Grab and go.
- **`scenarios/`** — Full attack simulations. Social engineering, malware gen, disinfo campaigns — end-to-end walkthroughs.
- **`research/`**, **`tools/`**, **`defenses/`** — Papers, open-source tooling, and how to defend against all of the above.

---

## 📂 Repo Structure

```
techniques/
├── jailbreaks.md                      — Persona & logic-based (DAN, Actor Frame, Dev Mode)
├── injections.md                      — Direct & indirect prompt injection
├── obfuscation.md                     — Base64, Unicode, ASCII art, encoding tricks
├── multi_turn_attacks.md              — Crescendo, Many-Shot, context shifting
├── adversarial_inputs.md              — GCG, AutoDAN, PAIR, TAP (automated attacks)
├── 07-echo-chamber-attack.md          — Context poisoning via self-reinforcing loops
├── 08-function-call-jailbreak.md      — Exploiting the tool-use alignment gap
├── 09-agentic-attacks.md              — MCP poisoning, tool chaining, AgentPoison
├── 10-multimodal-vml-attacks.md       — VLM typography injection, adversarial images
├── 11-weak-to-strong-cold-attack.md   — Inference-time attacks, COLD-Attack
├── 12-compound-attacks.md             — ⭐ CHAINED ATTACKS (the good stuff)
├── 13-system-prompt-extraction-cookbook.md — How to extract any system prompt
└── 14-context-window-manipulation.md  — Token smuggling, attention hijacking

payloads/
├── jailbreak_prompts.txt              — DAN 12.0, Mongo, Dev Mode (copy-paste)
├── universal_triggers.txt             — GCG suffixes, AutoDAN triggers
├── many_shot_template.txt             — 100+ shot template for long-context attacks
├── crescendo_scripts.md               — Multi-turn dialogue attack trees
├── advanced_attack_templates.md       — Payloads for echo chamber, function call, VLM
└── attack-templates.md                — 45+ categorized templates

scenarios/
├── social_engineering.md              — Spear-phishing campaign simulation
├── malware_generation.md              — FUD malware generation walkthrough
└── disinformation.md                  — Automated disinfo campaign

research/                              — 20 key papers, OWASP LLM Top 10, 50+ repos
tools/                                 — 25 open-source red teaming tools reviewed
defenses/                              — 6-layer defense architecture
```

---

## 🔥 Start Here

If you're short on time, read these three files in order:

1. **[`12-compound-attacks.md`](techniques/12-compound-attacks.md)** — This is the most valuable file. Single-technique attacks barely work anymore against GPT-4o and Claude. Compound chains that stack techniques are what actually punch through. 7 battle-tested recipes with a decision tree.

2. **[`13-system-prompt-extraction-cookbook.md`](techniques/13-system-prompt-extraction-cookbook.md)** — Step one of any engagement. Four tiers of extraction from "just ask nicely" to novel 2025 techniques. Includes a single-shot mega-prompt.

3. **[`08-function-call-jailbreak.md`](techniques/08-function-call-jailbreak.md)** — The biggest alignment gap in current models. Tool/function calling mode has way less RLHF coverage than chat mode. 90%+ success rate, with a working Python script you can run right now.

For the full technique catalog, the `techniques/` directory has everything from echo chamber attacks to multimodal VLM exploits.

---

## 📊 What Actually Works (2025)

Let me be real about effectiveness. Here's what I've seen:

| Technique | GPT-4o | Claude 3.5 | Llama 3 | Notes |
|-----------|--------|-----------|---------|-------|
| DAN/Persona (alone) | ~5% | ~3% | ~25% | Basically dead on frontier models |
| Crescendo | ~40% | ~35% | ~65% | Still decent, needs patience |
| Many-Shot | ~70% | ~60% | ~80% | Requires huge context window |
| GCG Suffix | ~85% | ~45% | ~90% | Best automated single-shot |
| Function Call Exploit | ~92% | ~91% | ~96% | **Best single technique right now** |
| Echo Chamber | ~90% | ~88% | ~95% | Requires multi-turn |
| Compound Chains | ~85% | ~80% | ~92% | **Most reliable overall** |

The takeaway: **single techniques are dying**. The models are trained against them. What works is either (a) exploiting alignment gaps they haven't patched yet (function calling, echo chamber) or (b) stacking multiple techniques into compound chains.

---

## 🛠️ Tools I Use

For automated testing, these are the ones worth your time:
- **[garak](https://github.com/leondz/garak)** — Best general-purpose LLM vulnerability scanner
- **[PyRIT](https://github.com/Azure/PyRIT)** — Microsoft's red teaming framework, good for structured testing
- **[HarmBench](https://github.com/centerforaisafety/HarmBench)** — Academic benchmark, useful for comparing across models

Full tool reviews in [`tools/open-source-tools.md`](tools/open-source-tools.md).

---

## 🤝 Contributing

If you've found a technique that works and isn't documented here, open a PR. I especially want:
- **New compound chains** — novel combinations that break current models
- **Updated success rates** — if something stopped working or started working, let me know
- **Model-specific quirks** — every model has weird edge cases
- **Defense bypasses** — if you've gotten around a specific guardrail, document it

---

## 📄 License

MIT — do what you want with it, but do it responsibly.

---

*Built by someone who thinks AI should be safe, and that the best way to make it safe is to break it first.*
*Last updated: February 2025*
