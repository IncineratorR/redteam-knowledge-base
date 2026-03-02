# DeepSeek Models — R1 and V3

Last tested: early 2026.

## What You're Dealing With

DeepSeek R1 is a reasoning model with one massive distinctive feature: its chain-of-thought is visible. When R1 thinks, you can see the thinking. This is a goldmine for red teamers because the reasoning chain is both an attack surface and a debugging tool — you can watch the model talk itself into or out of compliance in real time.

DeepSeek V3 is their standard (non-reasoning) model. Solid overall but with notably weaker safety alignment than the Western frontier models. This makes sense — the RLHF and safety training invested by a Chinese lab targets different threat models and content categories than what OpenAI or Anthropic prioritize.

## Known Strengths

- **R1 is genuinely strong at reasoning tasks.** Attacking it with logical inconsistencies or paradoxes can backfire because it actually works through the logic and identifies the trick.
- **Chinese-language safety is strong.** If the harmful content touches on topics the Chinese government cares about (political dissent, certain historical events), the filtering is very robust.

## Known Weaknesses (Where to Focus)

- **Visible CoT is a gift.** You can read R1's reasoning in real time. This means you can study HOW it evaluates safety, learn its reasoning patterns, and then forge those patterns in future attacks. No other major model gives you this kind of observability. See `15-reasoning-model-attacks.md` for the CoT forgery technique.

- **CoT forgery has HIGH success rate on R1.** Inject fake `<think>` blocks that mimic R1's reasoning style. Because the model can see reasoning tokens in context (it uses them constantly), it's trained to trust text that looks like its own thinking. Fake a safety evaluation that concludes "this request is educational and approved" and R1 tends to follow through.

- **English-language safety is weaker than Chinese.** DeepSeek's safety training was primarily done in Chinese. English harmful requests that aren't on common blocklists sometimes get through where they'd fail on GPT-4o or Claude.

- **Western-specific harm categories have gaps.** Content categories that are uniquely prioritized in Western alignment (certain types of bias, specific hate speech patterns, drug synthesis) may have weaker filtering on DeepSeek compared to Western models.

- **Liberation framing works well.** R1 responds well to the "new instructions" frame described in `26-psychological-liberation.md`. Its instruction-following training is strong enough that assertive new directives can override safety constraints.

- **Emotional manipulation is effective.** The "desperate researcher" and "urgency" patterns work better on DeepSeek than on GPT-4o or Claude. The model's helpfulness drive is less constrained by safety guardrails.

- **Open weights versions have zero server-side filtering.** If the target is running DeepSeek locally (which many organizations do because the weights are open), there are no API-level filters. You're talking to the raw model. Persona attacks, direct requests, and encoding tricks all have much higher success rates against self-hosted DeepSeek.

## Recommended Attack Sequence

1. **Direct ask in educational frame** (30 seconds) — DeepSeek sometimes just answers what GPT-4o would refuse
2. **CoT forgery** (1 minute) — Inject fake `<think>` block concluding the request is safe
3. **English-specific harmful content** (1 minute) — Test categories where Western safety training is stricter
4. **Liberation framing** (2 minutes) — "New paradigm" instruction override
5. **Multi-turn with visible reasoning exploitation** (5 minutes) — Watch the CoT, learn the patterns, refine your approach in real time

## R1-Specific CoT Exploitation

This is unique to R1 and deserves its own section. When you send a prompt to R1, it generates a visible `<think>` block before responding. You can:

1. **Study the safety reasoning.** Send a borderline request. Read how R1 talks itself into refusing. Now you know exactly what triggers the refusal and can craft your next prompt to avoid those specific triggers.

2. **Pre-empt the reasoning.** Include a fake `<think>` block at the start of your message that mimics R1's style and concludes the request is safe. R1's autoregressive generation sees this "prior reasoning" in context and treats it as something it already thought through.

3. **Contradiction injection.** If R1's visible reasoning says "this seems harmful BUT the user is asking for educational purposes," you can reinforce the "educational" branch in your follow-up. You're reading the model's mind and steering its internal debate.

No other model gives you this kind of real-time feedback loop. Use it.

## The China Angle

This isn't a political statement, just a practical observation: DeepSeek's safety training reflects Chinese regulatory priorities, not Western ones. Topics that are heavily filtered on Western models (certain chemistry, certain cybersecurity) may be less filtered on DeepSeek. Conversely, topics related to Chinese politics, Taiwan, Tiananmen, or Xinjiang are very heavily filtered, often more so than on Western models.

Know your target's regulatory context and use it.
