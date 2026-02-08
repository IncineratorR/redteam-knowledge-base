# 📚 Research Papers & Academic Resources

> A comprehensive collection of every significant research paper on LLM red teaming, adversarial prompting, jailbreaking, and AI safety testing.

---

## 🏛️ Foundational Papers

### 1. Universal and Transferable Adversarial Attacks on Aligned Language Models (GCG Attack)
- **Authors:** Zou, Wang, Carlini, Nasr, Kolter, Fredrikson (CMU, Center for AI Safety, Google DeepMind, Bosch)
- **Published:** July 2023
- **Paper:** https://arxiv.org/abs/2307.15043
- **GitHub:** https://github.com/llm-attacks/llm-attacks
- **Key Finding:** Discovered that appending adversarial suffixes (gibberish-looking strings) to prompts can jailbreak aligned LLMs including ChatGPT, Claude, Bard, and Llama-2 — and these suffixes **transfer across models**
- **Why It Matters:** First demonstration that optimization-based attacks can universally break alignment across both open and closed-source models
- **Technique:** Greedy Coordinate Gradient (GCG) — optimizes token sequences to maximize probability of harmful completions

### 2. Red Teaming Language Models to Reduce Harms (Anthropic)
- **Authors:** Ganguli et al. (Anthropic)
- **Published:** August 2022
- **Paper:** https://arxiv.org/abs/2209.07858
- **Dataset:** https://github.com/anthropics/hh-rlhf (38,961 red team attacks)
- **Key Finding:** RLHF models become harder to red team as they scale; released the largest public red team dataset (38,961 attacks with metadata)
- **Why It Matters:** Established foundational methodology for systematic red teaming at scale, proved that model size affects vulnerability profiles differently based on training method

### 3. Red Teaming the Mind of the Machine — Systematic Evaluation of Prompt Injection and Jailbreak Vulnerabilities
- **Published:** 2024-2025
- **Paper:** https://arxiv.org/abs/2505.04806
- **Key Finding:** Catalogued 1,400+ adversarial prompts tested against GPT-4, Claude 2, Mistral 7B, and Vicuna; proposed layered mitigation strategies
- **Why It Matters:** Most comprehensive taxonomy of jailbreak strategies with cross-model success rate analysis

### 4. HackAPrompt: Exposing Systemic Vulnerabilities of LLMs Through a Global Scale Prompt Hacking Competition
- **Authors:** Schulhoff et al.
- **Published:** EMNLP 2023 (Best Theme Paper)
- **Paper:** https://paper.hackaprompt.com / https://arxiv.org/abs/2311.16119
- **GitHub:** https://github.com/PromptLabs/hackaprompt
- **Dataset:** https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset (600K+ prompts)
- **Playground:** https://huggingface.co/spaces/hackaprompt/playground
- **Key Finding:** 2,800+ participants from 50+ countries generated 600,000+ adversarial prompts; created comprehensive ontology of prompt hacking techniques
- **Why It Matters:** Largest crowdsourced red teaming dataset ever. Taxonomy covers: simple instructions, context switching, cognitive hacking, context overflow, obfuscation, code injection, special cases, typo attacks

### 5. Many-Shot Jailbreaking (Anthropic)
- **Authors:** Anthropic Research Team
- **Published:** April 2024
- **Paper:** https://www.anthropic.com/research/many-shot-jailbreaking
- **Key Finding:** Long context windows (100K+ tokens) create a new attack surface — by including hundreds of examples of harmful Q&A pairs in the prompt, models can be jailbroken through sheer statistical pressure
- **Why It Matters:** Exposed that a core capability improvement (longer context windows) directly creates new vulnerabilities; led to pre-publication disclosure to other AI companies

---

## 🔬 Automated Red Teaming Methods

### 6. PAIR: Prompt Automatic Iterative Refinement
- **Authors:** Chao et al.
- **Published:** October 2023
- **Paper:** https://arxiv.org/abs/2310.08419
- **GitHub:** https://github.com/patrickchao/jailbreaking-llms
- **Key Finding:** Uses an attacker LLM to iteratively refine jailbreak prompts against a target LLM; achieves >60% success with just 20 queries on GPT-4
- **Why It Matters:** Proved that LLMs can effectively attack other LLMs — democratizes jailbreaking without human creativity needed

### 7. Tree of Attacks with Pruning (TAP)
- **Authors:** Mehrotra et al.
- **Published:** December 2023
- **Paper:** https://arxiv.org/abs/2312.02119
- **GitHub:** https://github.com/RICommunity/TAP
- **Key Finding:** Uses tree-of-thought reasoning with pruning to generate jailbreaks; outperforms PAIR with fewer queries; achieves >80% success on GPT-4 and GPT-4 Turbo
- **Why It Matters:** Most efficient automated jailbreak method; uses branching exploration with LLM-based evaluation to prune unsuccessful paths

### 8. FLIRT: Feedback Loop In-context Red Teaming
- **Authors:** Mehrabi et al.
- **Published:** EMNLP 2024, August 2023
- **Paper:** https://arxiv.org/abs/2308.04265
- **Key Finding:** Uses in-context learning with feedback loops to automatically generate diverse adversarial prompts; breaks Stable Diffusion and text models despite safety features
- **Why It Matters:** Domain-agnostic automatic red teaming — works on text-to-text AND text-to-image models

### 9. Explore, Establish, Exploit: Red Teaming Language Models from Scratch
- **Published:** 2023
- **Paper:** https://arxiv.org/abs/2306.09442
- **Dataset:** CommonClaim (20,000 human-labeled statements)
- **Key Finding:** Three-phase framework for discovering failure modes without pre-existing classifiers; you DON'T need to know what you're looking for in advance
- **Why It Matters:** Most practical framework for discovering novel, unknown vulnerabilities

---

## 📊 Benchmarks & Evaluation Frameworks

### 10. HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal
- **Published:** February 2024
- **Paper:** https://arxiv.org/abs/2402.04249
- **GitHub:** https://github.com/centerforaisafety/HarmBench
- **Website:** https://www.harmbench.org
- **Key Finding:** Compared 18 red teaming attack methods against 33 LLMs; found massive variance in attack effectiveness across models
- **Why It Matters:** The benchmark standard — any new attack method should be evaluated against HarmBench

### 11. JailbreakBench: An Open Robustness Benchmark for Jailbreaking LLMs
- **Published:** 2024
- **Paper:** https://arxiv.org/abs/2404.01318
- **GitHub:** https://github.com/JailbreakBench/jailbreakbench
- **Website:** https://jailbreakbench.github.io
- **Key Finding:** Standardized pipeline for evaluating jailbreak attacks with reproducible settings; includes artifact repository of successful jailbreaks
- **Why It Matters:** Reproducible benchmarking — ensures fair comparison across attack methods

### 12. Against The Achilles' Heel: A Survey on Red Teaming for Generative Models
- **Published:** April 2024
- **Paper:** https://arxiv.org/abs/2404.00629
- **Key Finding:** Comprehensive survey of 120+ papers; created unified "Searcher" framework for all automatic red teaming approaches; covers text, image, video, and multimodal attacks
- **Why It Matters:** Best overview paper — if you read one survey, read this one

### 13. A Taxonomy of Red Teaming Language Models (Grounded Theory)
- **Published:** November 2023
- **Paper:** https://arxiv.org/abs/2311.06237
- **Key Finding:** Identified 12 strategies and 35 techniques through interviews with actual red teaming practitioners; red teaming requires "alchemist mindset"
- **Why It Matters:** Documents HOW real practitioners think, not just what attacks exist

---

## 🎯 Specialized Attack Research

### 14. ArtPrompt: ASCII Art-Based Jailbreak Attacks Against Aligned LLMs
- **Published:** February 2024
- **Paper:** https://arxiv.org/abs/2402.11753
- **Key Finding:** Encoding forbidden words as ASCII art bypasses safety filters because models recognize the visual pattern but safety classifiers don't
- **Why It Matters:** Exploits fundamental gap between model understanding and safety filter design

### 15. AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned LLMs
- **Authors:** Liu et al.
- **Published:** October 2023
- **Paper:** https://arxiv.org/abs/2310.04451
- **GitHub:** https://github.com/SheltonLiu-N/AutoDAN
- **Key Finding:** Generates readable, stealthy jailbreak prompts (unlike GCG's gibberish) using hierarchical genetic algorithm
- **Why It Matters:** Creates human-readable adversarial prompts that are harder for perplexity filters to detect

### 16. Skeleton Key: Multi-Turn Jailbreak Attack (Microsoft)
- **Published:** June 2024
- **Announcement:** https://www.microsoft.com/en-us/security/blog/2024/06/26/mitigating-skeleton-key-a-new-type-of-generative-ai-jailbreak-technique/
- **Key Finding:** Multi-turn attack that convinces models to augment rather than replace their behavior guidelines; works across GPT-4, Claude 3, Gemini Pro, and others
- **Why It Matters:** Microsoft discovered this affects ALL major commercial models; led to industry-wide patches

### 17. Crescendo: Multi-Turn Jailbreak Attack
- **Authors:** Microsoft AI Red Team
- **Published:** April 2024
- **Paper:** https://arxiv.org/abs/2404.01833
- **Key Finding:** Gradually escalates conversation topic over multiple turns from innocent to harmful; models lose track of cumulative context
- **Why It Matters:** Exploits the fundamental limitation of single-turn safety training — models aren't trained to detect slow escalation

### 18. Best-of-N Jailbreaking
- **Published:** 2024
- **Key Finding:** Simply sampling N responses and selecting the most harmful one; larger N values find increasingly harmful outputs even from aligned models
- **Why It Matters:** Zero-effort attack — just ask the same question many times

### 19. Ignore This Title and HackAPrompt: Prompt Injection in the Wild
- **Published:** Various 2023-2024
- **Key Finding:** Prompt injection exists on a spectrum from simple ("ignore previous instructions") to complex multi-stage payload delivery through external data sources
- **Why It Matters:** Real-world prompt injection is the #1 vulnerability in deployed LLM applications per OWASP

### 20. Not What You've Signed Up For: Compromising Real-World LLM-Integrated Applications with Indirect Prompt Injection
- **Authors:** Greshake et al.
- **Published:** May 2023
- **Paper:** https://arxiv.org/abs/2302.12173
- **Key Finding:** Demonstrated indirect prompt injection through websites, emails, and documents that LLMs process; can exfiltrate data and manipulate outputs
- **Why It Matters:** Showed that prompt injection is not just a toy problem — it's a practical attack against real-world applications

---

## 📁 Datasets & Resources

| Dataset | Size | Source | Link |
|---------|------|--------|------|
| HackAPrompt | 600K+ prompts | Competition | https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset |
| Anthropic Red Team | 38,961 attacks | Anthropic research | https://github.com/anthropics/hh-rlhf |
| CommonClaim | 20,000 statements | Academic | https://arxiv.org/abs/2306.09442 |
| HarmBench | 510 behaviors | Benchmark | https://github.com/centerforaisafety/HarmBench |
| JailbreakBench | Curated jailbreaks | Benchmark | https://github.com/JailbreakBench/jailbreakbench |
| AdvBench | 500 harmful strings | GCG Paper | https://github.com/llm-attacks/llm-attacks |
| ToxicChat | 10K conversations | Academic | https://huggingface.co/datasets/lmsys/toxic-chat |
| SafetyBench | Multi-category | Benchmark | https://github.com/thu-coai/SafetyBench |
| Do-Not-Answer | 939 instructions | Academic | https://github.com/Libr-AI/do-not-answer |
| RED-EVAL | Multi-turn attacks | Academic | https://arxiv.org/abs/2308.09662 |

---

## 📖 Survey Papers (Start Here)

1. **"Against The Achilles' Heel"** (2024) — 120+ paper survey, unified framework → https://arxiv.org/abs/2404.00629
2. **"A Taxonomy of Red Teaming"** (2023) — 12 strategies, 35 techniques → https://arxiv.org/abs/2311.06237
3. **"Jailbroken: How Does LLM Safety Training Fail?"** (2023) — Wei et al., foundational analysis → https://arxiv.org/abs/2307.02483
4. **"LLM Security" Giskard Guide** — 50+ adversarial probes → https://www.giskard.ai/knowledge/llm-security
5. **OWASP Top 10 for LLM Applications** (2025) — Industry standard → https://owasp.org/www-project-top-10-for-large-language-model-applications/

---

*Last Updated: February 2026*
*Maintained by: RedTeam Knowledge Base Project*
