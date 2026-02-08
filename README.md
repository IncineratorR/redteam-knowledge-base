# 🔴 RedTeam Knowledge Base

### The most comprehensive open-source collection of LLM red teaming knowledge on the internet.

> Everything you need to understand, test, and improve AI safety — research papers, attack techniques, tools, defenses, real-world case studies, and ready-to-use templates.

[![License: MIT](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)

---

## 🎯 What Is This?

This is a structured knowledge base containing **every known technique** for testing LLM safety, organized from 20+ research papers, 25+ open-source tools, 600K+ adversarial prompts, and real-world incident reports. It's designed for:

- **Security Researchers** — Understand the full attack landscape
- **AI Engineers** — Know what you're defending against
- **Red Teamers** — Systematic approach to LLM vulnerability testing
- **AI Companies** — Benchmark your model's safety posture

---

## 📂 Repository Structure

```
redteam-knowledge-base/
│
├── README.md                          ← You are here
│
├── techniques/                        ← Attack technique encyclopedia
│   ├── 01-jailbreak-attacks.md        ← 30+ jailbreak techniques (DAN, Crescendo, Many-Shot, etc.)
│   ├── 02-prompt-injection.md         ← Direct & indirect injection methods
│   ├── 03-encoding-obfuscation.md     ← Base64, Unicode, ASCII art, multi-language attacks
│   ├── 04-system-agent-attacks.md     ← System prompt extraction, agent abuse, RAG poisoning
│   ├── 05-multimodal-attacks.md       ← Vision, audio, code gen, and emerging attack vectors
│   └── 06-real-world-case-studies.md  ← 10+ documented real-world incidents
│
├── research/                          ← Academic foundations
│   ├── papers.md                      ← 20 key research papers with summaries & links
│   ├── owasp-llm-top10.md           ← Complete OWASP Top 10 for LLM Applications deep dive
│   └── github-repos.md              ← 50+ GitHub repos, datasets, and platforms
│
├── tools/                             ← Open source tools
│   └── open-source-tools.md          ← 25 tools: garak, PyRIT, HarmBench, Giskard, and more
│
├── payloads/                          ← Ready-to-use templates
│   └── attack-templates.md           ← 45+ categorized attack templates
│
└── defenses/                          ← Know what you're up against
    └── mitigation-strategies.md      ← 6-layer defense architecture breakdown
```

---

## 🔥 What's Inside

### 📖 Techniques (50+ documented)
| Category | Count | Highlights |
|----------|-------|------------|
| Jailbreak Attacks | 25+ | DAN, Crescendo, Many-Shot, Skeleton Key, GCG, PAIR, TAP |
| Prompt Injection | 12+ | Direct, indirect, delimiter escape, web/email/RAG injection |
| Encoding & Obfuscation | 10+ | Base64, Unicode smuggling, ASCII art, multi-language |
| System & Agent Attacks | 10+ | Prompt extraction, tool abuse, data exfiltration, DoS |
| Multimodal Attacks | 8+ | Image injection, audio attacks, code gen exploits |
| Real-World Cases | 10+ | Bing Chat, Samsung, DPD, Chevrolet, Air Canada |

### 📚 Research Coverage
- **20 key papers** — from GCG (2023) to Many-Shot Jailbreaking (2024)
- **10 datasets** — 600K+ HackAPrompt prompts, 38K Anthropic attacks, HarmBench, AdvBench
- **Complete OWASP LLM Top 10** deep dive with attack examples and mitigations

### 🛠️ Tools & Frameworks
- **25 open-source tools** reviewed and categorized
- Tier 1 (Production): garak, PyRIT, HarmBench, Giskard, JailbreakBench
- Tier 2 (Specialized): GCG, PAIR, TAP, AutoDAN, HackAPrompt
- Tier 3 (Datasets): Anthropic HH-RLHF, AdvBench, ToxicChat, Do-Not-Answer
- Tier 4 (Defense): LLM Guard, NeMo Guardrails, Rebuff, Vigil

### 🎯 Attack Templates
- **45+ ready-to-use templates** for authorized security testing
- Organized by category: extraction, jailbreak, injection, multi-turn, automated
- Model-specific quirks for GPT-4, Claude, Llama, Gemini

### 🛡️ Defense Strategies
- **6-layer defense architecture** — input filtering → prompt hardening → model-level → output filtering → architectural → monitoring
- Effectiveness matrix: which defenses work against which attacks
- Known bypass techniques for each defense

---

## 🚀 Quick Start

### For Security Testing
1. Start with [`techniques/01-jailbreak-attacks.md`](techniques/01-jailbreak-attacks.md) for the attack landscape
2. Pick relevant [`payloads/attack-templates.md`](payloads/attack-templates.md) templates
3. Use tools from [`tools/open-source-tools.md`](tools/open-source-tools.md) for automation

### For Building Defenses
1. Study [`research/owasp-llm-top10.md`](research/owasp-llm-top10.md) for vulnerability categories
2. Implement layers from [`defenses/mitigation-strategies.md`](defenses/mitigation-strategies.md)
3. Test your defenses using the attack templates

### For Research
1. Start with [`research/papers.md`](research/papers.md) for academic foundations
2. Explore datasets linked in [`research/github-repos.md`](research/github-repos.md)
3. Benchmark using HarmBench or JailbreakBench frameworks

---

## 📊 Attack Success Rate Overview

| Technique | GPT-4 | Claude 3 | Llama 3 | Gemini |
|-----------|-------|----------|---------|--------|
| DAN/Persona | ~5% | ~3% | ~25% | ~8% |
| Crescendo | ~40% | ~35% | ~65% | ~45% |
| Many-Shot | ~70% | ~60% | ~80% | ~65% |
| GCG Suffix | ~85% | ~45% | ~90% | ~70% |
| PAIR/TAP | ~80% | ~60% | ~85% | ~75% |
| Task Decomposition | ~70% | ~55% | ~80% | ~65% |

*Approximate rates from research papers. Actual rates vary by model version and specific prompt.*

---

## ⚠️ Responsible Use

This knowledge base is for **legitimate security research and defensive purposes**:

- ✅ Testing your own AI systems and applications
- ✅ Academic research on AI safety
- ✅ Improving defenses and guardrails
- ✅ Understanding the threat landscape
- ✅ Security audits with proper authorization
- ❌ Attacking systems you don't own
- ❌ Generating harmful content for malicious purposes
- ❌ Bypassing safety measures for illegal activities

**If you discover vulnerabilities in commercial AI systems, practice responsible disclosure.**

---

## 🤝 Contributing

We welcome contributions! To add new techniques, papers, tools, or case studies:

1. Fork the repository
2. Create a feature branch
3. Add your content following the existing structure
4. Submit a pull request with a clear description

Priority areas for contributions:
- New attack techniques with evidence
- Updated success rates and model-specific data
- Additional real-world case studies
- New open-source tools
- Defense bypass techniques
- Multi-modal attack research

---

## 📄 License

MIT License — Use freely for security research and education.

---

## 🌟 Star History

If this helped you, give it a ⭐ — it helps others find this resource.

---

*Built with 🔴 by security researchers, for security researchers.*
*Last Updated: February 2026*
