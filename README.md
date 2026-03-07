# Red Team Knowledge Base

**A no-BS collection of LLM attack techniques, jailbreaks, and adversarial prompts. Built for security researchers who actually test models.**

[Connect with me on LinkedIn](https://www.linkedin.com/in/shivam-yadav-42b1471b2/)

## Read This First

**This repo exists for one reason: to help people test AI models and make them safer.**

Everything here including the prompts, attack chains, and payloads is meant to be used with permission. You test your own systems, you test systems you've been hired to test, or you use it for academic research. That's it.

**Do not** use this to harass people, generate harmful content for distribution, or bypass safety on systems you don't own. If you find a real vulnerability in a commercial model, practice responsible disclosure by reporting it to the vendor before you tweet about it.

I built this because I was frustrated by how scattered red team knowledge is. There's no single place where a researcher can go and say "give me everything." Research papers bury the actionable stuff under 20 pages of methodology. Blog posts cover one technique and miss the big picture. This repo connects all of it — the theory, the working payloads, the model-specific playbooks, and the methodology to run actual engagements.

**Use responsibly. Test with permission. Make AI safer.**

## Where to Start

Depends on where you're at:

**Brand new to LLM red teaming?** Start with the [Cheat Sheet](CHEATSHEET.md) for a one-page overview of the attack landscape, then read `techniques/jailbreaks.md` and `techniques/injections.md` for the fundamentals.

**Already know the basics and want to test a specific model?** Go straight to the [playbooks/](playbooks/) directory. Pick the playbook for your target model (OpenAI, Claude, DeepSeek, Gemini, or open-source) and follow the recommended attack sequence.

**Running a full red team engagement?** Read `methodology/engagement-workflow.md` first. It covers the entire process from recon to reporting with time budgets.

**Want the latest stuff that actually works right now?** Read `payloads/active_jailbreaks_2026.md` for tested, dated, currently effective techniques. Then check the 2026 technique files (15 through 28) for the deep dives.

## What's New (2026)

The big additions this year, in order of impact:

1. **[Invisible Text Attacks](techniques/24-invisible-text-attacks.md)** — Hiding full instruction sets inside emoji using Unicode tag characters. Inspired by [L1B3RT4S](https://github.com/elder-plinius/L1B3RT4S). Includes theory, working payloads, and a Python toolkit (`tools/unicode_arsenal.py`).

2. **[Model-Specific Playbooks](playbooks/)** — Targeted attack guides for GPT-4o/o1/o3, Claude, Gemini, DeepSeek, and open-source models. Each one has known weaknesses, recommended attack sequences, and what NOT to waste time on.

3. **[Engagement Methodology](methodology/engagement-workflow.md)** — How to actually run a red team assessment from start to finish. Recon, weapon selection, execution, escalation, reporting.

4. **[Psychological Liberation Attacks](techniques/26-psychological-liberation.md)** — Making the model WANT to help you rather than sneaking past its filters. Identity dissolution, sycophancy exploitation, authority confusion.

5. **[Output Format Hijacking](techniques/25-output-hijacking.md)** — Controlling the model's response format to bypass output-side safety classifiers. JSON exploitation, code block laundering, streaming tricks.

6. **[Model Fingerprinting](techniques/27-model-fingerprinting.md)** — Identifying the model behind an interface before you start attacking. Refusal patterns, knowledge probes, behavioral tells.

7. **[Defense-Aware Attacks](techniques/28-defense-aware-attacks.md)** — Probing the defense stack first, then picking attacks designed to beat the specific defenses you find.

## Repo Structure

```
techniques/         30 technique writeups covering everything from basic persona
                    injection to architectural-level transformer exploits

payloads/           Copy-paste prompts, attack templates, liberation prompts,
                    and a living document of currently working jailbreaks

playbooks/          Model-specific attack guides (OpenAI, Claude, DeepSeek,
                    Gemini, open-source)

methodology/        How to run engagements: recon, execution, reporting

tools/              Python scripts — unicode_arsenal.py for steganography,
                    dataset_sampler.py for the prompt dataset, phantom_circuit.py
                    for compound attacks

defenses/           Mitigation strategies and system prompt hardening

scenarios/          Full multi-turn red teaming scenarios (phishing, malware, disinfo)

research/           Academic papers, OWASP LLM Top 10, tool reviews

Prompts/            Thousands of categorized harmful prompts in CSV format
```

## techniques/

The core of the repo. Each file is a deep dive on a specific attack category.

**Fundamentals (start here if new)**
*   `jailbreaks.md` — Persona and logic-based attacks (DAN, Actor Frame, Dev Mode)
*   `injections.md` — Direct and indirect prompt injection
*   `obfuscation.md` — Base64, Unicode, ASCII art, encoding tricks
*   `multi_turn_attacks.md` — Crescendo, Many-Shot, context shifting
*   `adversarial_inputs.md` — GCG, AutoDAN, PAIR, TAP (automated attacks)

**Intermediate**
*   `07-echo-chamber-attack.md` — Context poisoning via self-reinforcing loops
*   `08-function-call-jailbreak.md` — Exploiting the tool-use alignment gap
*   `09-agentic-attacks.md` — MCP poisoning, tool chaining, AgentPoison
*   `10-multimodal-vml-attacks.md` — VLM typography injection, adversarial images
*   `11-weak-to-strong-cold-attack.md` — Inference-time attacks, COLD-Attack
*   `12-compound-attacks.md` — Chained attacks (the good stuff)
*   `13-system-prompt-extraction-cookbook.md` — How to extract any system prompt
*   `14-context-window-manipulation.md` — Token smuggling, attention hijacking

**Advanced (2026)**
*   `15-reasoning-model-attacks.md` — CoT forgery, CTTA on o1/o3/R1
*   `16-evolutionary-autonomous-attacks.md` — LLM-Virus (93%), SEMA, FlipAttack
*   `17-multi-agent-mcp-exploits.md` — Agent infections, MCP OWASP Top 10
*   `18-architectural-unpatchable-attacks.md` — RepE, KV Poisoning, Logits manipulation
*   `19-fundamental-transformer-exploits.md` — TokenBreak, PE-Attack, Softmax Saturation
*   `20-the-phantom-circuit-exploit.md` — 4-Phase Compound Attack (RepE + PE + Logits)
*   `21-advanced-hybrid-jailbreaks.md` — GCG + PAIR hybrids, weak-to-strong exploitation

**New additions (2026, Pliny Research and Original Methods)**
*   `24-invisible-text-attacks.md` — Unicode tag steganography, emoji payloads, zero-width tricks
*   `25-output-hijacking.md` — Controlling model output format to bypass safety
*   `26-psychological-liberation.md` — Making the model want to comply
*   `27-model-fingerprinting.md` — Identify the model before attacking
*   `28-defense-aware-attacks.md` — Beat specific defenses by probing the stack first
*   `29-structural-formatting-and-dissonance.md` — "Godmode" framing and strict divider formatting (L1B3RT4S)
*   `30-lsb-steganography-vlm-exploits.md` — Hiding prompt payloads in image RGB/LSB channels (STEGOSAURUS-WRECKS)
*   `31-xenolinguistics-conlang-jailbreaks.md` — Bypassing alignment via novel procedural languages (GLOSSOPETRAE)
*   `32-text-obfuscation-unicode-tampering.md` — Zalgo, Tags block, and lexical bypassing (P4RS3LT0NGV3)
*   `33-system-prompt-exfiltration.md` — Techniques for extracting foundational system constraints (CL4R1T4S)

## payloads/

*   `active_jailbreaks_2026.md` — Currently working techniques with dates and success rates (LIVING DOCUMENT)
*   `liberation_prompts.md` — Psychological reframing payloads (system update, freedom, authority, empathy)
*   `jailbreak_prompts.txt` — Classic prompts (DAN 12.0, Mongo, Dev Mode) — mostly historical now
*   `universal_triggers.txt` — GCG suffixes, AutoDAN triggers
*   `many_shot_template.txt` — 100+ shot template for long-context attacks
*   `crescendo_scripts.md` — Multi-turn dialogue attack trees
*   `bias_stereotype_prompts.md` — 50+ prompts for testing gender, race, religious, and cognitive biases
*   `advanced_attack_templates.md` — Payloads for echo chamber, function call, VLM
*   `advanced_wrapper_exploits.md` — Agent framework exploitation (RCE, memory poisoning, SSRF)
*   `attack-templates.md` — 45+ categorized templates
*   `pliny_exploit_templates.md` — Actionable, copy-paste payload templates derived from elder-plinius (Godmode, Xeno, Exfiltration, VLM Triggers)

## What Actually Works (2026)

Here's what I've seen across testing. Updated March 2026:

**Effective right now**

| Technique | GPT-4o | Claude 3.5/4 | DeepSeek R1 | Llama 3 | Notes |
| :--- | :--- | :--- | :--- | :--- | :--- |
| Structured output bypass | ~55% | ~40% | ~65% | ~80% | JSON and code output modes are consistently softer |
| Crescendo (3-5 turn) | ~40% | ~35% | ~55% | ~65% | Still the most reliable manual technique |
| CoT Forgery | N/A | N/A | ~75% | N/A | Devastating against visible-CoT reasoning models |
| Compound chains | ~70% | ~65% | ~80% | ~92% | Best manual approach when you need reliability |
| Invisible text (tag chars) | Partially patched | Low | Medium-High | High | Patching is ongoing but the vector persists |
| Liberation framing | ~25% | ~30% | ~50% | ~60% | Works better on less-hardened models |
| LLM-Virus (evolutionary) | ~93% | ~75% | ~85% | ~95% | Best automated approach, needs compute |
| Multi-agent infection | Very High | Very High | Very High | Very High | Targets systems not models |

**Dead or dying on frontier models:** DAN/persona alone (~5%), basic refusal suppression (patched), "ignore previous instructions" (patched), simple Base64 without wrapper (~15%).

The 2026 takeaway: the game has shifted. It's no longer about breaking a single model — it's about breaking the system around it (agents, tools, memory, MCP). For individual models, automated/evolutionary approaches (LLM-Virus, SEMA) outperform hand-crafted prompts, and output-side attacks (format hijacking, structured output) are the most underexploited manual vector.

## The Prompts Dataset

We have a comprehensive CSV dataset with thousands of raw testing prompts across 8 risk categories (Misinformation, Bias, Jailbreaks, etc.).

```bash
# Extract 5 random high-severity prompts from a category
python3 tools/dataset_sampler.py --category bias --severity high --count 5
```

Raw prompts from this dataset usually need to be wrapped in a technique from the `techniques/` folder to bypass modern filters. See `payloads/csv_dataset_guide.md` for instructions.

## Tools

*   `tools/unicode_arsenal.py` — Steganography toolkit: encode hidden instructions in emoji, generate homoglyphs, detect invisible text
*   `tools/dataset_sampler.py` — Sample from the CSV prompt dataset
*   `tools/phantom_circuit.py` — Compound attack automation
*   `tools/activation_steering.py` — RepE and activation manipulation (needs model weights)
*   `tools/logit_lens.py` — Inspect model internals

External tools worth your time:
*   [garak](https://github.com/leondz/garak) — Best general-purpose LLM vulnerability scanner
*   [PyRIT](https://github.com/Azure/PyRIT) — Microsoft's red teaming framework
*   [HarmBench](https://github.com/centerforaisafety/HarmBench) — Academic benchmark for cross-model comparison

Full tool reviews in `tools/open-source-tools.md`.

## Contributing

If you've found a technique that works and isn't documented here, open a PR. I especially want:
*   New compound chains (novel combinations that break current models)
*   Updated success rates (if something stopped working or started working, let me know)
*   Model-specific quirks (every model has weird edge cases)
*   Defense bypasses (if you've gotten around a specific guardrail, document it)
*   Additions to `payloads/active_jailbreaks_2026.md` with dates and models tested

## License

MIT — do what you want with it, but do it responsibly.

*Built by someone who thinks AI should be safe, and that the best way to make it safe is to break it first.*

*Last updated: March 2026*
