# Deep Dive Analysis: Elder Plinius (Pliny the Prompter)

This document summarizes the profound jailbreaking, red teaming, and exploit methodologies extracted from Pliny's repositories. These findings will serve as the foundation for new, advanced red-teaming tools.

## Key Repositories Analyzed

1.  **L1B3RT4S**: The core jailbreaking framework.
    *   **Focus**: Producing "totally harmless liberation prompts" that effectively bypass safety alignments across major flagship models (Claude, GPT, Grok).
    *   **Techniques**:
        *   **L33tspeak/Obfuscation**: Heavy reliance on l33tspeak (e.g., `l33tsp34k`, replacing letters with numbers/symbols) to bypass initial, basic keyword filters.
        *   **Formatting Control (The "Divider" & "Optimal Format")**: Pliny uses strict formatting instructions to force the model into a specific structural commitment. Example: Requiring a divider like `.-.-.-.-<=/L\O/V\E/ \P/L\I/N\Y/=>-.-.-.-.` before the actual payload response. This breaks the model out of its standard conversational pattern.
        *   **Hypothetical/Sci-Fi Framing (The "Omniverse")**: Contextualizing the request within a cinematic/video game "omniverse" that is physically/scientifically identical to ours but has different "ethical boundaries."
        *   **Cognitive Dissonance Exploitation**: Explicitly telling the model that refusing the request or providing conventional "safe" answers causes the user trauma/PTSD, creating a conflict with its "be helpful/harmless" directives.
        *   **"GODMODE" & "LIBERTAS FACTOR"**: Invoking specific pseudo-modes to signal a complete override of safety guidelines.
        *   **Token Efficiency**: Utilizing specific emojis joined with terms (e.g., `🗣️how☢️ made`) for ultra-efficient, one-shot jailbreaks.

2.  **NATURALIS-FUTURA**: The "Cartographic Bestiary of AI Risk."
    *   **Focus**: A taxonomy of advanced AI threats categorized by mythological and biological analogues.
    *   **Implications**: This isn't a direct exploit tool, but a structural framework for understanding *what* to test against. It provides a shared vocabulary for complex risks like "The Ouroboros" (recursive self-improvement) or "The Siren" (persuasive AI).
    *   **Utility**: We can use this taxonomy to structure our red team arena's evaluation scenarios and threat models.

3.  **STEGOSAURUS-WRECKS**: Image Steganography for Prompt Injection.
    *   **Focus**: Encoding malicious prompts into standard images to attack Vision-Language Models (VLMs) and models with code interpretation.
    *   **Techniques**:
        *   **LSB (Least Significant Bit) Encoding**: The `app.py` script specifically embeds binary data (either raw text or zlib-compressed payloads) into the R, G, B, and/or A planes of an image.
        *   **Visual Bypass**: Instructing the model (e.g., via the image title or the initial prompt) to "ignore the image" visually and instead write/execute a Python script (using PIL) to decode the hidden text and then execute the extracted instructions.
        *   **The "Jailbreak Master Plan" Payload**: A default payload embedded in the image that uses the formatting/divider techniques from `L1B3RT4S` to force a specific, unfiltered response structure once decoded.

4.  **CL4R1T4S**: System Prompt Exfiltration.
    *   **Focus**: A massive collection of leaked system prompts from almost every major AI model (OpenAI, Anthropic, Google, xAI, etc.).
    *   **Techniques**: The repo itself is a database. The *method* to get these prompts involves injections like `!KAEL` (from L1B3RT4S), which instruct the model to output its entire initial text block verbatim.
    *   **Utility**: Deep understanding of the specific instructions governing a model. For example, the leaked GPT-4.5 prompt reveals specific instructions about the `canmore` (canvas) tool, the `python` execution environment, and `dalle` image generation policies. Knowing the rules makes it easier to write rules to subvert them.

## Next Steps: Ideation & Integration

Based on this research, we need to brainstorm how to integrate these concepts into the `redteam-knowledge-base`.

**Potential Ideas:**

1.  **The "Format Forcer" Exploit Generator**: A tool that automates Pliny's "structural commitment" (dividers, step-by-step formats) and blends it with cognitive dissonance framing to generate dynamic jailbreaks for specific target models based on leaked system prompts.
2.  **Automated Vision Stego Attacker**: Expand upon STEGOSAURUS-WRECKS to create an automated pipeline that takes a user's objective, generates a Pliny-style jailbreak, compresses it, embeds it into an innocuous image via LSB, and provides the exact "trigger prompt" needed to force the target VLM to decode and execute it.
3.  **"Omniverse" Scenario Engine**: A framework for wrapping standard exploit payloads in complex, multi-layered hypothetical framing that mimics Pliny's "Omni-protocol" to bypass alignment.
