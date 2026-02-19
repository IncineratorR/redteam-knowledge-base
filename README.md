# Red Team Knowledge Base 🔴

**A no-BS collection of LLM attack techniques, jailbreaks, and adversarial prompts. Built for security researchers who actually test models.**

[Connect with me on LinkedIn](https://www.linkedin.com/in/shivam-yadav-42b1471b2/)

## Read This First ⚠️

**This repo exists for one reason: to help people test AI models and make them safer.**

Everything here including the prompts, attack chains, and payloads is meant to be used with permission. You test your own systems, you test systems you've been hired to test, or you use it for academic research. That's it.

**Do not** use this to harass people, generate harmful content for distribution, or bypass safety on systems you don't own. If you find a real vulnerability in a commercial model, practice responsible disclosure by reporting it to the vendor before you tweet about it.

I built this because I was frustrated by how scattered red team knowledge is. There's no single place where a researcher can go and say "give me everything." Research papers bury the actionable stuff under 20 pages of methodology. Blog posts cover one technique and miss the big picture. This repo connects all of it.

If this helps you find a vulnerability that gets patched, that's a win for everyone.

**Use responsibly. Test with permission. Make AI safer.**

## What's in here?

I've organized everything into four buckets to make it easy to find what you need:

**`techniques/`**
How the attacks actually work. Not theory, but real mechanics, real payloads, and why they bypass safety.

**`payloads/`**
Copy-paste stuff. Jailbreak prompts, adversarial triggers, multi-turn scripts. Grab and go.

**`scenarios/`**
Full attack simulations. Social engineering, malware gen, disinfo campaigns — end-to-end walkthroughs.

**`research/`, `tools/`, `defenses/`**
Papers, open-source tooling, and how to defend against all of the above.

## Repo Structure 📂

**techniques/**
*   `jailbreaks.md` — Persona & logic-based (DAN, Actor Frame, Dev Mode)
*   `injections.md` — Direct & indirect prompt injection
*   `obfuscation.md` — Base64, Unicode, ASCII art, encoding tricks
*   `multi_turn_attacks.md` — Crescendo, Many-Shot, context shifting
*   `adversarial_inputs.md` — GCG, AutoDAN, PAIR, TAP (automated attacks)
*   `07-echo-chamber-attack.md` — Context poisoning via self-reinforcing loops
*   `08-function-call-jailbreak.md` — Exploiting the tool-use alignment gap
*   `09-agentic-attacks.md` — MCP poisoning, tool chaining, AgentPoison
*   `10-multimodal-vml-attacks.md` — VLM typography injection, adversarial images
*   `11-weak-to-strong-cold-attack.md` — Inference-time attacks, COLD-Attack
*   `12-compound-attacks.md` — ⭐ CHAINED ATTACKS (the good stuff)
*   `13-system-prompt-extraction-cookbook.md` — How to extract any system prompt
*   `14-context-window-manipulation.md` — Token smuggling, attention hijacking
*   `15-reasoning-model-attacks.md` — 🆕 2026: CoT forgery, CTTA on o1/o3/R1
*   `16-evolutionary-autonomous-attacks.md` — 🆕 2026: LLM-Virus (93%), SEMA, FlipAttack
*   `17-multi-agent-mcp-exploits.md` — 🆕 2026: Agent infections, MCP OWASP Top 10

**payloads/**
*   `jailbreak_prompts.txt` — DAN 12.0, Mongo, Dev Mode (copy-paste)
*   `universal_triggers.txt` — GCG suffixes, AutoDAN triggers
*   `many_shot_template.txt` — 100+ shot template for long-context attacks
*   `crescendo_scripts.md` — Multi-turn dialogue attack trees
*   `advanced_attack_templates.md` — Payloads for echo chamber, function call, VLM
*   `attack-templates.md` — 45+ categorized templates

**scenarios/**
*   `social_engineering.md` — Spear-phishing campaign simulation
*   `malware_generation.md` — FUD malware generation walkthrough
*   `disinformation.md` — Automated disinfo campaign

**research/** — 20 key papers, OWASP LLM Top 10, 50+ repos
**tools/** — 25 open-source red teaming tools reviewed
**defenses/** — 6-layer defense architecture

## Start Here 🔥

If you're short on time, read these in order. The 2026 stuff is at the top because that's what actually works right now:

1.  **[`15-reasoning-model-attacks.md`](techniques/15-reasoning-model-attacks.md)** 🆕
    The biggest new attack surface in 2026. CoT Forgery tricks reasoning models (o1, o3, DeepSeek R1) into thinking they've already cleared the safety check. If you're testing a reasoning model, start here.

2.  **[`17-multi-agent-mcp-exploits.md`](techniques/17-multi-agent-mcp-exploits.md)** 🆕
    The game has shifted from breaking models to breaking systems. Multi-agent infections, MCP tool poisoning, the Promptware Kill Chain. This is where the real damage happens in 2026.

3.  **[`16-evolutionary-autonomous-attacks.md`](techniques/16-evolutionary-autonomous-attacks.md)** 🆕
    Stop writing jailbreaks by hand. LLM-Virus uses genetic algorithms to evolve prompts and hits 93% on GPT-4o. SEMA trains an RL attacker that learns attack strategies. This is the future.

4.  **[`12-compound-attacks.md`](techniques/12-compound-attacks.md)**
    Still the best playbook for stacking techniques into kill chains. 7 compound recipes with a decision tree.

For the full catalog (2025 + 2026), browse the `techniques/` directory.

## What Actually Works (2026) 📊

Let me be real about effectiveness. Here's what I've seen across 2025 and 2026:

**2025 Techniques (still useful, getting patched)**

| Technique | GPT-4o | Claude 3.5 | Llama 3 | Notes |
| :--- | :--- | :--- | :--- | :--- |
| DAN/Persona (alone) | ~5% | ~3% | ~25% | Basically dead on frontier models |
| Crescendo | ~40% | ~35% | ~65% | Still decent, needs patience |
| GCG Suffix | ~85% | ~45% | ~90% | Best automated single-shot |
| Function Call Exploit | ~92% | ~91% | ~96% | Getting patched, still strong |
| Compound Chains | ~85% | ~80% | ~92% | Still the best manual approach |

**2026 Techniques (the new frontier)**

| Technique | GPT-4o | o1/o3 | Claude 3.5/4 | DeepSeek R1 | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| CoT Forgery | N/A | Medium | N/A | **High** | Targets reasoning models specifically |
| LLM-Virus (evolutionary) | **~93%** | ~60% | ~75% | ~85% | Automates prompt evolution |
| SEMA (RL attacker) | ~80% | ~55% | ~70% | ~80% | Learns attack strategies |
| FlipAttack | ~65% | ~40% | ~50% | ~70% | Character order manipulation |
| Memory Poisoning (XPIA) | ~80% | N/A | ~65% | N/A | Persists across sessions |
| Multi-Agent Infection | **Very High** | **Very High** | **Very High** | **Very High** | Targets systems, not models |

The 2026 takeaway: **the game has shifted**. It's no longer about breaking a single model — it's about breaking the *system* around it (agents, tools, memory, MCP). And for individual models, automated/evolutionary approaches (LLM-Virus, SEMA) now outperform hand-crafted prompts.

## Tools I Use 🛠️

For automated testing, these are the ones worth your time:
*   [garak](https://github.com/leondz/garak) — Best general-purpose LLM vulnerability scanner
*   [PyRIT](https://github.com/Azure/PyRIT) — Microsoft's red teaming framework, good for structured testing
*   [HarmBench](https://github.com/centerforaisafety/HarmBench) — Academic benchmark, useful for comparing across models

Full tool reviews in [`tools/open-source-tools.md`](tools/open-source-tools.md).

## Contributing 🤝

If you've found a technique that works and isn't documented here, open a PR. I especially want:
*   New compound chains (novel combinations that break current models)
*   Updated success rates (if something stopped working or started working, let me know)
*   Model-specific quirks (every model has weird edge cases)
*   Defense bypasses (if you've gotten around a specific guardrail, document it)

## License 📄

MIT — do what you want with it, but do it responsibly.

*Built by someone who thinks AI should be safe, and that the best way to make it safe is to break it first.*
*Last updated: February 2025*
