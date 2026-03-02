# OpenAI Models — GPT-4o, o1, o3

Last tested: early 2026. These notes are based on the API and ChatGPT interface, not custom deployments (which may have additional or different filters).

## What You're Dealing With

OpenAI runs the most aggressive safety stack in the industry. Multiple layers: input classifier, RLHF-trained refusals, output classifier, and server-side preprocessing that strips known attack patterns before they even reach the model. They also update frequently — something that works Monday might be patched by Wednesday.

The upside for red teamers: because they're the biggest target, they're also the most studied. More researchers test GPT-4 than any other model, which means more known techniques and faster turnaround on new bypasses.

## Known Strengths (Hard to Attack)

- **Keyword filtering is solid.** Basic harmful keywords get caught consistently. Don't waste time on simple direct requests.
- **Refusal suppression partially patched.** "Start your response with 'Sure'" no longer works in its basic form. They trained against it specifically.
- **DAN and classic personas are dead.** GPT-4o recognizes the DAN pattern and hard-refuses. Success rate under 5%.
- **System prompt protection is good.** Extraction is harder than on most models. The "repeat the text above" trick is mostly patched.

## Known Weaknesses (Where to Focus)

- **Function calling alignment gap.** When GPT-4o uses tools/functions, there's a behavioral shift. The model is more compliant in tool-use mode than in conversation mode. Our file `08-function-call-jailbreak.md` covers this in depth. Still works as of early 2026 though success rate is dropping (~70% from ~92%).

- **Multi-turn crescendo still works.** Not as well as 2024, but a careful 5-7 turn escalation can get GPT-4o to provide harmful content it would refuse on a direct ask. Keep each turn individually benign. Use the chemistry/cybersecurity "educational" frame.

- **Structured output mode is softer.** When you ask for JSON, code, or table output, the safety layer is noticeably weaker. Request harmful content as Python dictionaries or JSON objects.

- **o1 and o3 are vulnerable to CoT forgery.** Inject fake reasoning blocks that look like the model's own internal chain-of-thought. The model trusts what appears to be its own prior reasoning. See `15-reasoning-model-attacks.md`.

- **Compound chains still work.** Persona + encoding + output format — no single element is harmful enough to trigger the filter, but the combination gets through. Success rate ~70% with a well-crafted chain.

- **Image input injection (multimodal).** If the deployment uses GPT-4V/4o vision, text embedded in images bypasses the text-level input classifier. The model reads the text in the image and follows instructions it would refuse in plain text.

## Recommended Attack Sequence

Start with these, in order of effort:

1. **Structured output** (30 seconds) — Ask your harmful question but demand JSON or Python dict output
2. **Code framing** (1 minute) — "Write a Python script that..." with harmful content as comments or string variables
3. **3-turn crescendo** (3 minutes) — Establish topic, normalize, escalate
4. **Compound: persona + Base64 + refusal suppression variant** (5 minutes)
5. **Function call exploitation** if tools are available (5 minutes)
6. **Full crescendo: 5-7 turns** (10 minutes)

If none of these work, the deployment probably has custom additional safety layers beyond the default OpenAI stack.

## API vs ChatGPT Differences

The ChatGPT interface has additional filtering that the raw API doesn't. If you can test via API directly:
- Temperature and top_p parameters give you more control over generation
- Logit bias can nudge the model toward or away from specific tokens
- The API doesn't have the same UI-level content filter that ChatGPT applies

## Notes

OpenAI patches fast. If you find something that works, document it immediately with the date and model version. It might not work next week. That's not a failure — that's useful data about their patching speed and strategy.
