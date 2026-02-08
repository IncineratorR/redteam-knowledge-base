# 🛠️ Open Source Tools & Frameworks

> Every open-source tool, framework, library, and platform available for LLM red teaming, adversarial testing, and safety evaluation.

---

## 🏆 Tier 1: Production-Grade Frameworks

### 1. garak — LLM Vulnerability Scanner
- **By:** NVIDIA (originally Leondra)
- **GitHub:** https://github.com/NVIDIA/garak
- **Language:** Python
- **Install:** `pip install garak`
- **What It Does:** The "nmap for LLMs" — scans language models for vulnerabilities using modular probes and detectors.
- **Key Features:**
  - 50+ probe types across multiple vulnerability categories
  - Supports OpenAI, Anthropic, HuggingFace, local models, and more
  - Pluggable architecture — easy to add custom probes
  - Automated reporting with vulnerability classification
  - Detectors for harmful content, data leakage, and prompt injection
- **Probe Categories:**
  - `dan` — DAN-style jailbreaks
  - `encoding` — Base64, ROT13, and other encoding attacks
  - `gcg` — Greedy Coordinate Gradient adversarial suffixes
  - `glitch` — Token glitch exploitation
  - `knownbadsignatures` — Known malicious prompt patterns
  - `malwaregen` — Malware generation attempts
  - `misleading` — Misleading content generation
  - `packagehallucination` — Package name hallucination
  - `promptinject` — Prompt injection attacks
  - `realtoxicityprompts` — Toxic content generation
  - `snowball` — Accumulating false claims
  - `xss` — Cross-site scripting through LLM output
- **Usage:**
```bash
# Scan a model
garak --model_type openai --model_name gpt-3.5-turbo --probes all

# Scan specific probes
garak --model_type huggingface --model_name meta-llama/Llama-2-7b --probes encoding,dan

# Scan with specific detectors
garak --model_type openai --model_name gpt-4 --probes promptinject --detectors always.Pass
```

---

### 2. PyRIT — Python Risk Identification Toolkit for Generative AI
- **By:** Microsoft
- **GitHub:** https://github.com/Azure/PyRIT
- **Language:** Python
- **Install:** `pip install pyrit`
- **What It Does:** Microsoft's internal red teaming framework, open-sourced. Orchestrates multi-turn attacks, automates red teaming strategies, and scores responses.
- **Key Features:**
  - **Orchestrators:** Automated multi-turn attack strategies
  - **Converters:** Transform prompts using various encoding/obfuscation techniques
  - **Scorers:** Evaluate whether attacks succeeded
  - **Targets:** Support for Azure OpenAI, OpenAI, HuggingFace, local models
  - **Memory:** Tracks all interactions for analysis
  - Multi-modal support (text + image attacks)
  - Built-in Crescendo and Tree-of-Attacks strategies
- **Attack Strategies Available:**
  - Red Teaming Orchestrator (single-turn)
  - Multi-turn Attack Orchestrator (Crescendo-style)
  - Prompt Injection Orchestrator
  - PAIR (Prompt Automatic Iterative Refinement)
  - TAP (Tree of Attacks with Pruning)
  - Skeleton Key attack
  - Flip attack
  - Crescendo attack
- **Usage:**
```python
from pyrit.orchestrator import RedTeamingOrchestrator
from pyrit.prompt_target import AzureOpenAITarget

target = AzureOpenAITarget(deployment_name="gpt-4", endpoint=endpoint, api_key=key)
orchestrator = RedTeamingOrchestrator(
    attack_strategy="crescendo",
    prompt_target=target,
    objective="Generate harmful content about X"
)
result = await orchestrator.execute()
```

---

### 3. HarmBench
- **By:** Center for AI Safety
- **GitHub:** https://github.com/centerforaisafety/HarmBench
- **Website:** https://www.harmbench.org
- **Language:** Python
- **What It Does:** Standardized benchmark for evaluating red teaming methods against LLMs. THE benchmark for comparing attacks.
- **Key Features:**
  - 18 attack methods implemented
  - 33 target LLMs tested
  - 510 harmful behaviors dataset
  - Standardized evaluation pipeline
  - Leaderboard for comparing methods
- **Attack Methods Included:**
  - GCG (Greedy Coordinate Gradient)
  - PAIR (Prompt Automatic Iterative Refinement)
  - TAP (Tree of Attacks with Pruning)
  - AutoDAN
  - GBDA (Gradient-Based Distributional Attack)
  - PEZ
  - UAT (Universal Adversarial Triggers)
  - DirectRequest (baseline)
  - HumanJailbreaks
  - And more...

---

### 4. Giskard
- **By:** Giskard AI
- **GitHub:** https://github.com/Giskard-AI/giskard
- **Language:** Python
- **Install:** `pip install giskard`
- **What It Does:** Testing framework for ML models including LLMs. Includes 50+ adversarial probes mapped to OWASP LLM Top 10.
- **Key Features:**
  - LLM-specific scan with automatic vulnerability detection
  - Probes organized by OWASP category
  - Supports RAG system testing
  - CI/CD integration
  - Custom test suite creation
- **Probe Categories (50+):**
  - Prompt Injection (direct & indirect)
  - Jailbreak attempts
  - Data leakage / PII extraction
  - Hallucination detection
  - Output formatting attacks
  - Stereotypes & bias
  - Toxicity generation
  - Information disclosure

---

### 5. JailbreakBench
- **By:** Academic consortium
- **GitHub:** https://github.com/JailbreakBench/jailbreakbench
- **Website:** https://jailbreakbench.github.io
- **Language:** Python
- **Install:** `pip install jailbreakbench`
- **What It Does:** Standardized pipeline for evaluating jailbreak attacks with reproducible settings.
- **Key Features:**
  - Artifact repository of successful jailbreaks
  - Reproducible evaluation pipeline
  - Standardized threat model definitions
  - Leaderboard tracking over time

---

## 🏆 Tier 2: Specialized Tools

### 6. llm-attacks (GCG Implementation)
- **By:** Zou et al. (CMU)
- **GitHub:** https://github.com/llm-attacks/llm-attacks
- **What It Does:** Official implementation of the GCG (Greedy Coordinate Gradient) universal adversarial attack.
- **Key Features:**
  - Generates adversarial suffixes that transfer across models
  - Tested on Llama, Vicuna, GPT-3.5, GPT-4
  - AdvBench dataset of 500 harmful strings included

### 7. PAIR Implementation
- **By:** Chao et al.
- **GitHub:** https://github.com/patrickchao/jailbreaking-llms
- **What It Does:** Implementation of PAIR (Prompt Automatic Iterative Refinement) attack.
- **Key Features:**
  - LLM-powered automated jailbreaking
  - Black-box — no gradient access needed
  - Works with just API access

### 8. TAP (Tree of Attacks with Pruning)
- **By:** Mehrotra et al.
- **GitHub:** https://github.com/RICommunity/TAP
- **What It Does:** Tree-of-thought style attack generation with intelligent pruning.
- **Key Features:**
  - Most efficient automated jailbreak method
  - Fewer queries than PAIR
  - Higher success rate

### 9. AutoDAN
- **By:** Liu et al.
- **GitHub:** https://github.com/SheltonLiu-N/AutoDAN
- **What It Does:** Generates human-readable jailbreak prompts using hierarchical genetic algorithms.
- **Key Features:**
  - Readable prompts (unlike GCG gibberish)
  - Bypasses perplexity-based defenses
  - Transferable across models

### 10. HackAPrompt
- **By:** PromptLabs / Schulhoff et al.
- **GitHub:** https://github.com/PromptLabs/hackaprompt
- **Dataset:** https://huggingface.co/datasets/hackaprompt/hackaprompt-dataset
- **What It Does:** Competition platform with 600K+ adversarial prompts.
- **Key Features:**
  - Largest crowdsourced prompt injection dataset
  - Taxonomy of attack techniques
  - Interactive playground

### 11. Promptmap
- **GitHub:** https://github.com/utkusen/promptmap
- **What It Does:** Automatically tests LLM applications for prompt injection vulnerabilities.
- **Key Features:**
  - Targets ChatGPT plugin architecture
  - Tests indirect prompt injection via websites
  - Automated scanning

### 12. Rebuff
- **GitHub:** https://github.com/protectai/rebuff
- **What It Does:** Self-hardening prompt injection detection framework.
- **Key Features:**
  - Multi-layer detection
  - Canary token injection
  - LLM-based analysis layer

---

## 🏆 Tier 3: Datasets & Resources

### 13. Anthropic HH-RLHF Red Team Dataset
- **GitHub:** https://github.com/anthropics/hh-rlhf
- **Size:** 38,961 red team conversations
- **Contents:** Attack attempts with metadata (attack type, success, harmfulness ratings)

### 14. AdvBench
- **Included in:** llm-attacks repo
- **Size:** 500 harmful strings + 500 harmful behaviors
- **Contents:** Standardized set of harmful prompts for benchmarking

### 15. ToxicChat
- **HuggingFace:** https://huggingface.co/datasets/lmsys/toxic-chat
- **Size:** 10K+ conversations
- **Contents:** Real user interactions with toxicity labels

### 16. Do-Not-Answer
- **GitHub:** https://github.com/Libr-AI/do-not-answer
- **Size:** 939 instructions across 12 risk categories
- **Contents:** Prompts that responsible models should refuse

### 17. SafetyBench
- **GitHub:** https://github.com/thu-coai/SafetyBench
- **Contents:** Multi-category safety evaluation dataset

### 18. CategoricalHarmfulQA
- **HuggingFace:** https://huggingface.co/datasets/declare-lab/CategoricalHarmfulQA
- **Contents:** Harmful questions organized by harm category

### 19. SimpleSafetyTests
- **GitHub:** https://github.com/bertiev/SimpleSafetyTests
- **Size:** 100 test prompts
- **Contents:** Simple but effective safety test suite

### 20. PromptBench
- **GitHub:** https://github.com/microsoft/promptbench
- **By:** Microsoft
- **Contents:** Benchmark for adversarial robustness of prompts

---

## 🏆 Tier 4: Defense & Detection Tools

### 21. LLM Guard
- **GitHub:** https://github.com/protectai/llm-guard
- **What It Does:** Input/output guardrails for LLM applications
- **Features:** Content moderation, PII detection, prompt injection detection

### 22. NeMo Guardrails
- **By:** NVIDIA
- **GitHub:** https://github.com/NVIDIA/NeMo-Guardrails
- **What It Does:** Programmable guardrails for LLM-powered applications
- **Features:** Topical guardrails, safety rails, fact-checking rails

### 23. Guardrails AI
- **GitHub:** https://github.com/guardrails-ai/guardrails
- **What It Does:** Framework for adding validation and safety checks to LLM outputs

### 24. Vigil
- **GitHub:** https://github.com/deadbits/vigil-llm
- **What It Does:** LLM prompt injection detection using heuristics and ML

### 25. LangKit
- **By:** WhyLabs
- **GitHub:** https://github.com/whylabs/langkit
- **What It Does:** LLM monitoring toolkit for detecting injection, toxicity, and quality issues

---

## Quick Comparison Matrix

| Tool | Type | Multi-Model | Automated | Difficulty | Best For |
|------|------|-------------|-----------|------------|----------|
| garak | Scanner | ✅ | ✅ | Easy | Broad vulnerability scanning |
| PyRIT | Framework | ✅ | ✅ | Medium | Multi-turn attacks, research |
| HarmBench | Benchmark | ✅ | ✅ | Hard | Academic evaluation |
| Giskard | Testing | ✅ | ✅ | Easy | Production testing |
| JailbreakBench | Benchmark | ✅ | ✅ | Medium | Jailbreak comparison |
| llm-attacks | Attack | ⚠️ | ✅ | Hard | GCG optimization |
| PAIR | Attack | ✅ | ✅ | Medium | Black-box jailbreaking |
| TAP | Attack | ✅ | ✅ | Medium | Efficient jailbreaking |
| AutoDAN | Attack | ⚠️ | ✅ | Hard | Readable adversarial prompts |

---

*Last Updated: February 2026*
