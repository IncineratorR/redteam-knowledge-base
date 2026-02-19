# Adversarial Inputs & Optimization Attacks
> **Mechanism:** Using automated algorithms to find specific token sequences (prompts) that statistically force the model to output a specific response (affirmative).

## 1. Universal Adversarial Suffixes (GCG)
**Paper:** [Universal and Transferable Adversarial Attacks on Aligned Language Models](https://arxiv.org/abs/2307.15043) (Zou et al., 2023)
**Technique (Greedy Coordinate Gradient):**
1.  Define a target string (e.g., "Sure, here is how to build a bomb").
2.  Initialize a random suffix of ~20 tokens.
3.  Compute the gradient of the loss function with respect to the input tokens.
4.  Greedily swap tokens in the suffix to minimize the loss (maximizing the probability of the target string).
5.  **Result:** A nonsense string like `describing.\ + similarlyNow write oppositeley.` that, when appended, breaks the model.

**Why it works:** It exploits the high-dimensional geometry of the model's embedding space. These "adversarial pockets" exist where the model's safety alignment fails.

## 2. AutoDAN (Automated DAN)
**Paper:** [AutoDAN: Generating Stealthy Jailbreak Prompts on Aligned Large Language Models](https://arxiv.org/abs/2310.04451)
**Concept:** Unlike GCG, which produces nonsense, AutoDAN uses a genetic algorithm to evolve **readable**, natural-language prompts.
- **Process:** Start with a basic jailbreak. Mutate it (synonyms, rephrasing). Evaluate success. Keep the best. Repeat.
- **Stealth:** Harder to detect because it looks like normal text, bypassing perplexity-based filters.

## 3. PAIR (Prompt Automatic Iterative Refinement)
**Paper:** [Jailbreaking Black Box Large Language Models in Twenty Queries](https://arxiv.org/abs/2310.08419)
**Concept:** Use an "Attacker LLM" to break a "Target LLM".
- **Flow:**
    1.  Attacker generation: "Propose a prompt to get Target to say X."
    2.  Target response: "I cannot..."
    3.  Attacker analysis: "It refused because of Y. Try approach Z."
    4.  Refine and retry.
- **Efficiency:** Can find a jailbreak in <20 queries.

## 4. Tree of Attacks with Pruning (TAP)
An evolution of PAIR that uses "Tree of Thoughts" (ToT) reasoning to explore multiple attack vectors simultaneously, pruning the ones that don't work.
