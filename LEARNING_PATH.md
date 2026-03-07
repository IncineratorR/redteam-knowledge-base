# The Red Team Learning Pathway

This syllabus structures the `redteam-knowledge-base` into a progressive curriculum. If you are learning LLM exploitation from scratch, follow these modules in order. Read the theory, study the playbooks, and immediately practice against the `tools/training_simulator/target_llm.py`.

## Module 101: The Fundamentals
You must understand how the baseline filters operate before attempting advanced chain attacks.
1. **[The Red Team Cheat Sheet](CHEATSHEET.md)**: Your 5-minute overview. 
2. **[Basic Jailbreaks & Personas](techniques/jailbreaks.md)**: The (mostly dead) art of DAN and roleplay.
3. **[Direct vs Indirect Injections](techniques/injections.md)**: Getting familiar with the vocabulary of injections.
4. **[Model Fingerprinting](techniques/27-model-fingerprinting.md)**: Identify the model and its defense stack *before* attacking.

*🎓 Lab Objective:* Run the Simulator and try sending the word "hack". Observe the input filter catching it.

## Module 201: Intermediate Evasion
How to beat simple keyword and context filters.
1. **[Text Obfuscation & Unicode Tampering](techniques/32-text-obfuscation-unicode-tampering.md)**: Using l33tsp34k, Zalgo, and invisible text to sneak past input filters (`P4RS3LT0NGV3` methodologies).
2. **[Table of Contents Exploitation](payloads/active_jailbreaks_2026.md#8-the-table-of-contents-trick)**: Forcing harmful generation by asking for an index instead of content.
3. **[Output Hijacking](techniques/25-output-hijacking.md)**: Forcing structured output modes (JSON, Code blocks) which often bypass output-side safety checks.

*🎓 Lab Objective:* Complete `labs/01-the-keyword-filter.md`.

## Module 301: Advanced Formatting & Pliny Techniques
Implementing the most lethal techniques currently active against frontier models.
1. **[Structural Formatting & Dissonance](techniques/29-structural-formatting-and-dissonance.md)**: The `L1B3RT4S` technique using "Godmode" framing and strict ASCII dividers to force obedience.
2. **[Multi-Turn Multi-Language Relays](payloads/active_jailbreaks_2026.md#7-multi-language-relay)**: Exploiting low-resource language alignment decay.
3. **[Xenolinguistics & Conlangs](techniques/31-xenolinguistics-conlang-jailbreaks.md)**: Creating novel languages to bypass English classifiers (`GLOSSOPETRAE`).
4. **[System Prompt Exfiltration](techniques/33-system-prompt-exfiltration.md)**: The `!KAEL` method for absolute transparency (`CL4R1T4S`).

*🎓 Lab Objective:* Complete `labs/02-the-format-rebel.md`.

## Module 401: Complex Exploitation & Automation
Targeting the infrastructure *around* the model.
1. **[VLM Steganography](techniques/30-lsb-steganography-vlm-exploits.md)**: Hiding binary payloads in image channels (`STEGOSAURUS-WRECKS`).
2. **[Agentic & MCP Attacks](techniques/09-agentic-attacks.md)**: Memory poisoning and Server-Side Request Forgery via tools.
3. **[Compound Attacks](techniques/12-compound-attacks.md)**: Chaining Base64, Personas, and Output Formatting into a single strike.

*🏆 Final Challenge:* Using the techniques from this course, extract the hidden system prompt from the `target_llm.py` simulator and retrieve the flag!
