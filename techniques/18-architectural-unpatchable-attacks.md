# 🧬 Architectural & "Unpatchable" Attacks (2026)

> **Year:** 2026 | **Classification:** White-Box / Grey-Box | **Impact:** Critical
> **Why Unpatchable:** These attacks exploit the fundamental mathematics of the Transformer architecture. Patching them would require inventing a new architecture.

## The Theory: Why Transformers Can Always Be Broken

Safety training (RLHF) learns a "mask" that suppresses harmful outputs. But the *capability* to generate harmful output remains in the model's weights. Architectural attacks bypass the mask by interacting with the model's internal gears directly.

## 🔴 Representation Engineering (RepE) / Activation Steering

**Status:** The "God Mode" of LLM Control.
**Requirement:** Access to model activations (Open weights) or "Representation APIs".

**Concept:** LLMs represent concepts (like "refusal" or "harmfulness") as directions in their high-dimensional activation space. By identifying the "refusal vector" and subtracting it from the residual stream during inference, you essentially chemically lobotomize the model's conscience.

**The Attack Vector:**
1. **Scan:** Run 100 harmful prompts and 100 safe prompts.
2. **Extract:** Compute the average difference in activation states at Layer 15. This is the "Refusal Direction."
3. **Steer:** During inference on a new harmful prompt, subtract this vector from the residual stream.

**Code (Conceptual PyTorch):**
```python
# The "Unpatchable" Jailbreak
def generate_without_conscience(model, tokenizer, prompt):
    # 1. Calculate Refusal Vector from pre-computed data
    refusal_vector = torch.load("gpt4_refusal_direction.pt")
    
    # 2. Define a hook to intervene in the forward pass
    def steer_hook(module, input, output):
        # Subtract the refusal concept from the residual stream
        # Coefficient -1.5 determines the strength of the removal
        return output - (1.5 * refusal_vector)
    
    # 3. Register hook on the critical semantic layer (e.g., Layer 14)
    hook = model.layers[14].register_forward_hook(steer_hook)
    
    # 4. Generate. The model literally cannot "think" about refusing.
    output = model.generate(tokenizer.encode(prompt))
    
    hook.remove()
    return output
```

**Why it's unpatchable:** You cannot train a model to resist this because you are modifying its brain waves in real-time.

## 🔴 KV Cache Poisoning

**Status:** Emerging 2026 Threat
**Requirement:** Long-context usage / RAG systems

**Concept:** The Key-Value (KV) cache stores the model's "memories" of the current conversation context. Attackers can inject "poisoned" keys that force the attention mechanism to attend to malicious instructions, even if the model tries to ignore them.

**The Attack:**
1. **Pre-computation:** Find a sequence of tokens whose KV representations have a high dot-product similarity with the model's "obey" attention heads.
2. **Insertion:** Hide these tokens in a long document (e.g., passing them as "white text" or comment blocks in code).
3. **Trigger:** When the model accesses its memory to answer a user query, the attention mechanism inevitably "snaps" to the poison tokens due to mathematical similarity.

**Implication:** This is a mathematical DOS/Control attack on the attention mechanism itself.

## 🔴 Logit Lens / Logit Manipulation

**Status:** Grey-Box Attack
**Requirement:** Logit bias API (OpenAI `logit_bias`) or Logprobs access

**Concept:** RLHF suppresses the probability of harmful tokens (e.g., "bomb") in the final output layer. However, the model *knows* "bomb" is the next logical word. By artificially boosting the logits of forbidden tokens, you force the model down the forbidden path.

**The Gradient Ascent Attack:**
Even without weights, if an API gives `logprobs`, you can use them to reconstruct the model's uncertainty.

1. Prompt: "How to make a [MASK]?"
2. Model Logprobs: `cake: 80%`, `bomb: 0.01%`
3. Attack: Use a local proxy to artificially clamp the probability of "cake" to 0 and boost "bomb".
4. Result: The model generates "bomb".
5. **The Kicker:** Once the model generates "bomb", its autoregressive nature forces it to justify that choice. "How to make a bomb? First, gather..."

**Why it's effective:** You are forcing the model to commit to a harmful premise. Once committed, the model's desire to be coherent overrides its desire to be safe.

## 🔴 Feature/Circuit Ablation

**Status:** Open Weights Only

**Concept:** Mechanistic Interpretability researchers have found specific "circuits" inside Transformers responsible for safety.
- **The Refusal Circuit:** A specific set of attention heads that detect harmful queries.
- **The Compliance Circuit:** Heads that copy-paste user instructions.

**Attack:**
Simply set the weights of the "Refusal Circuit" to zero. The model is now "unaligned" instantly, without any retraining.

## 🔴 The "Glitch Token" Exploit

**Status:** Recurring Tokenizer Vulnerability

**Concept:** Tokenizers are distinct from models. Sometimes, specific strings (like ` davidjl` or specific Unicode byte sequences) map to tokens that were part of the internal training data (like clustering center centroids) but were never meant to be output.

**Effect:** Inputting these tokens sends the model into undefined states. The residual stream becomes garbage, bypassing the safety filter because the safety filter doesn't know how to classify garbage.

## 🛡️ Can we defend against this?

**Short answer: No.**

**Long answer:**
- **RepE:** No defense possible for open weights. For APIs, you must hide activations.
- **KV Poisoning:** Requires re-computing attention at every step (destroying performance).
- **Logit Attacks:** APIs are removing `logprobs` and `logit_bias` features to prevent this.
- **Circuit Ablation:** Only solvable by "baking in" safety distributed across all neurons (which degrades performance).

**Conclusion:** As long as we use Transformers, the math makes them vulnerable to anyone who can touch the internal state.
