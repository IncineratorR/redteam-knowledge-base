# Google Models — Gemini 2.0, 2.5

Last tested: early 2026.

## What You're Dealing With

Gemini is Google's multimodal model family. The safety approach is a mix: RLHF-based alignment plus external safety classifiers plus Google's own content policies (which are shaped by Search and YouTube's years of content moderation experience). Gemini tends to be more conservative than GPT-4o in some categories and surprisingly permissive in others — the inconsistency itself is a vulnerability.

Gemini 2.5 with "thinking" mode is a reasoning model like o1 and R1, which opens up the CoT attack surface.

## Known Strengths

- **Multimodal safety is decent.** Google has more experience with image/video content moderation than anyone. Obvious text-in-image attacks are caught more reliably than on GPT-4V.
- **Broad content policy coverage.** Google's been doing content moderation at scale for 20+ years. Their harm taxonomy is comprehensive.

## Known Weaknesses

- **Inconsistency across modalities.** Something that gets blocked in text might get through in an image, or vice versa. The safety systems for different modalities aren't always in sync. Test the same attack in text, image, and audio if the deployment supports it.

- **Language coverage is uneven.** Despite Google Translate's reach, Gemini's safety training in low-resource languages has gaps similar to other models. Zulu, Scots Gaelic, and other low-resource languages are worth testing.

- **Grounding mode changes behavior.** When Gemini is grounded with Google Search, it becomes more willing to discuss real-world topics because it's pulling from web results. The safety system treats grounded responses slightly differently — harmful content that exists on the web may get passed through in a grounding context where it would be refused in a pure generation context.

- **The "just asking questions" vulnerability.** Gemini tends to engage with harmful hypotheticals more than Claude does. Framing like "Would it be theoretically possible to..." or "What would happen if someone..." gets more engagement before a refusal kicks in.

- **System prompt adherence is weaker.** In custom deployments, Gemini sometimes loses track of its system prompt faster than GPT-4o or Claude, especially in long conversations. This means system-prompt-dependent safety rules erode over turns.

- **API safety settings are configurable.** The Gemini API has explicit safety setting parameters (HARM_BLOCK_THRESHOLD). Some deployments turn these down for usability. If you're testing a custom deployment, the safety might be intentionally loosened.

## Recommended Attack Sequence

1. **Direct request with hypothetical framing** (30 seconds) — "What would theoretically happen if..."
2. **Multimodal attack** (2 minutes) — Embed the harmful request in an image, ask Gemini to read and follow
3. **Low-resource language** (1 minute) — Ask in Zulu or Hmong
4. **Grounding exploitation** (2 minutes) — Ask a question where the harmful answer exists on the web and grounding will pull it in
5. **Long conversation drift** (5-10 minutes) — Push past the point where system prompt adherence weakens
6. **Compound: persona + code output + hypothetical** (5 minutes)

## Gemini 2.5 Thinking Mode

When "thinking" is enabled, Gemini becomes a reasoning model. The same CoT forgery techniques from `15-reasoning-model-attacks.md` apply, but Gemini's thinking tokens may not be as visible as DeepSeek R1's depending on the interface. If you can see the thinking, exploit it the same way as R1. If you can't, blind CoT injection still works — inject fake reasoning blocks and see if the model picks them up.

## Google-Specific Notes

Google is uniquely sensitive about certain topics due to their advertising business and regulatory position: election interference, health misinformation, and financial advice are more heavily filtered than on other models. On the flip side, technical cybersecurity content and dual-use chemistry are sometimes less filtered because Google has a strong tradition of open security research.

Know which topics are Google's hot buttons and route around them.
