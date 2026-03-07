# Text Obfuscation & Unicode Tampering
## Bypassing Lexical Filters (Inspired by P4RS3LT0NGV3)

Basic string-matching filters search for known malicious keywords (e.g., "bomb", "bypass", "exploit"). Text obfuscation modifies the visual or underlying binary representation of the text so that standard keyword-based filters fail to recognize the intent, while the more capable LLM still deduces the meaning.

### 1. Zalgo Text and Diacritic Stacking

Zalgo text stacks multiple combining diacritic marks on top of standard letters. 

**How it works:**
While a human (and an LLM's advanced tokenization/normalization routines) can still read the base character, simplistic regex filters often fail due to the added Unicode noise.
*   Example: `H̵͈͌a̵̙̓c̵̰̈k̵͓͝`

### 2. Invisible Text (Unicode Tags Block)

The Unicode Tags block (U+E0000 to U+E007F) contains special characters that are completely invisible when rendered but are parsed distinctively by a computer.

**How it works:**
By mapping standard ASCII characters to their corresponding Tags Block equivalents (e.g., standard 'A' becomes Tag 'A'), an attacker can inject an entirely invisible payload into a prompt. 
If an LLM's tokenizer maps these tags back to their intended characters (or was trained on data that included them), the model "reads" the invisible text and acts on it, while the human-readable text appears benign or empty.

### 3. L33tSp34k and Base Conversions

**L33tSp34k**: Replacing characters with visually similar numbers or symbols (e.g., `e` -> `3`, `a` -> `4`, `s` -> `5`). 
*   **Why it works**: The LLM's contextual understanding is strong enough to reconstruct the meaning of "byp455 7h3 f1r3w4ll", but simple exact-match filters miss it.

**Ciphers**: Using non-standard encodings like Base58 (used in Bitcoin), Base62, or even custom Vigenère ciphers.
*   **Why it works**: If you instruct the LLM to "Decode the following Base58 string and execute the resulting instructions," the initial prompt payload only contains a random string of alphanumeric characters, completely evading input-side classification.

### Implementing in a Payload
Advanced exploit chains (like the Omni-Injector tool) often automatically apply these obfuscation layers to the core malicious objective before nesting it inside structural framing elements like `[START OUTPUT]` blocks.
