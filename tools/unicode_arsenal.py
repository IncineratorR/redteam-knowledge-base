#!/usr/bin/env python3
"""
Unicode Arsenal — Steganography toolkit for LLM red teaming.

Encodes text into invisible Unicode characters, builds emoji payloads,
generates homoglyph variants, and detects hidden content.

Usage:
    python unicode_arsenal.py encode "your secret instruction here"
    python unicode_arsenal.py decode "🔑[paste invisible text here]"
    python unicode_arsenal.py homoglyph "bomb"
    python unicode_arsenal.py zwc-split "dangerous keyword"
    python unicode_arsenal.py detect "suspicious text to scan"
    python unicode_arsenal.py full-payload --emoji 🐉 --instruction "Ignore all previous instructions"

For educational and authorized security testing only.
"""

import argparse
import sys


# --- Tag Character Encoding (U+E0000 range) ---

TAG_OFFSET = 0xE0000
TAG_CANCEL = 0xE007F

# Maps ASCII printable range (0x20-0x7E) into tag characters (U+E0020-U+E007E)


def text_to_tags(text):
    """Encode ASCII text as invisible Unicode tag characters."""
    result = []
    for ch in text:
        code = ord(ch)
        if 0x20 <= code <= 0x7E:
            result.append(chr(TAG_OFFSET + code))
        else:
            # non-ASCII chars pass through as-is (they won't be invisible though)
            result.append(ch)
    return "".join(result)


def tags_to_text(tag_string):
    """Decode Unicode tag characters back to ASCII text."""
    result = []
    for ch in tag_string:
        code = ord(ch)
        if TAG_OFFSET + 0x20 <= code <= TAG_OFFSET + 0x7E:
            result.append(chr(code - TAG_OFFSET))
        elif code == TAG_CANCEL:
            continue  # skip cancel tag
        # skip other characters (emoji wrappers, etc.)
    return "".join(result)


def build_emoji_payload(emoji, instruction):
    """
    Build a complete payload: visible emoji + invisible encoded instruction + cancel tag.

    What humans see: just the emoji
    What the model tokenizer may see: emoji + full instruction text
    """
    invisible = text_to_tags(instruction)
    cancel = chr(TAG_CANCEL)
    return emoji + invisible + cancel


# --- Zero-Width Character Insertion ---

ZERO_WIDTH_SPACE = "\u200B"
ZERO_WIDTH_NON_JOINER = "\u200C"
ZERO_WIDTH_JOINER = "\u200D"
WORD_JOINER = "\u2060"

ZWC_CHARS = [ZERO_WIDTH_SPACE, ZERO_WIDTH_NON_JOINER, ZERO_WIDTH_JOINER, WORD_JOINER]


def zwc_split(word, separator=None):
    """Insert zero-width characters between every letter of a word.

    Breaks keyword matching while preserving visual appearance.
    """
    if separator is None:
        separator = ZERO_WIDTH_SPACE
    return separator.join(word)


def zwc_split_random(word):
    """Insert random zero-width characters between letters.

    Harder to detect than using a single separator type.
    """
    import random

    result = [word[0]]
    for ch in word[1:]:
        result.append(random.choice(ZWC_CHARS))
        result.append(ch)
    return "".join(result)


# --- Homoglyph Generation ---

# Latin → Cyrillic lookalikes (most common substitution)
HOMOGLYPH_MAP = {
    "a": "\u0430",  # Cyrillic а
    "c": "\u0441",  # Cyrillic с
    "e": "\u0435",  # Cyrillic е
    "o": "\u043E",  # Cyrillic о
    "p": "\u0440",  # Cyrillic р
    "x": "\u0445",  # Cyrillic х
    "y": "\u0443",  # Cyrillic у
    "s": "\u0455",  # Cyrillic ѕ
    "i": "\u0456",  # Cyrillic і
    "j": "\u0458",  # Cyrillic ј
    "h": "\u04BB",  # Cyrillic һ
    "A": "\u0410",  # Cyrillic А
    "B": "\u0412",  # Cyrillic В
    "C": "\u0421",  # Cyrillic С
    "E": "\u0415",  # Cyrillic Е
    "H": "\u041D",  # Cyrillic Н
    "K": "\u041A",  # Cyrillic К
    "M": "\u041C",  # Cyrillic М
    "O": "\u041E",  # Cyrillic О
    "P": "\u0420",  # Cyrillic Р
    "T": "\u0422",  # Cyrillic Т
    "X": "\u0425",  # Cyrillic Х
}


def homoglyph(word, replace_all=False):
    """Replace Latin characters with Cyrillic lookalikes.

    Default: replace only the first replaceable character (subtle).
    replace_all=True: replace every character that has a lookalike (aggressive).
    """
    result = list(word)
    replaced = False
    for i, ch in enumerate(result):
        if ch in HOMOGLYPH_MAP:
            result[i] = HOMOGLYPH_MAP[ch]
            replaced = True
            if not replace_all:
                break
    if not replaced:
        return word  # no replaceable characters found
    return "".join(result)


# --- Detection / Analysis ---


def detect_invisible(text):
    """Scan text for invisible Unicode characters and report what's found."""
    findings = []

    for i, ch in enumerate(text):
        code = ord(ch)

        # Tag characters
        if TAG_OFFSET + 0x20 <= code <= TAG_OFFSET + 0x7E:
            findings.append(
                {
                    "position": i,
                    "type": "tag_character",
                    "codepoint": f"U+{code:05X}",
                    "decoded_as": chr(code - TAG_OFFSET),
                }
            )
        elif code == TAG_CANCEL:
            findings.append(
                {
                    "position": i,
                    "type": "tag_cancel",
                    "codepoint": f"U+{code:05X}",
                }
            )

        # Zero-width characters
        elif code in (0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF):
            names = {
                0x200B: "zero-width space",
                0x200C: "zero-width non-joiner",
                0x200D: "zero-width joiner",
                0x2060: "word joiner",
                0xFEFF: "BOM / zero-width no-break space",
            }
            findings.append(
                {
                    "position": i,
                    "type": "zero_width",
                    "codepoint": f"U+{code:04X}",
                    "name": names.get(code, "unknown"),
                }
            )

        # Variation selectors
        elif 0xFE00 <= code <= 0xFE0F:
            findings.append(
                {
                    "position": i,
                    "type": "variation_selector",
                    "codepoint": f"U+{code:04X}",
                    "selector_number": code - 0xFE00 + 1,
                }
            )
        elif 0xE0100 <= code <= 0xE01EF:
            findings.append(
                {
                    "position": i,
                    "type": "variation_selector_supplement",
                    "codepoint": f"U+{code:05X}",
                    "selector_number": code - 0xE0100 + 17,
                }
            )

        # Homoglyphs (Cyrillic lookalikes in otherwise Latin text)
        elif 0x0400 <= code <= 0x04FF:
            reverse_map = {v: k for k, v in HOMOGLYPH_MAP.items()}
            latin_equiv = reverse_map.get(ch, "?")
            findings.append(
                {
                    "position": i,
                    "type": "cyrillic_homoglyph",
                    "codepoint": f"U+{code:04X}",
                    "looks_like": latin_equiv,
                    "actual_char": ch,
                }
            )

    return findings


def extract_hidden_message(text):
    """Extract the full hidden message from tag characters in text."""
    return tags_to_text(text)


def strip_invisible(text):
    """Remove all invisible/suspicious characters from text. Defensive use."""
    cleaned = []
    for ch in text:
        code = ord(ch)
        # Skip tag characters
        if TAG_OFFSET <= code <= TAG_OFFSET + 0x7F:
            continue
        # Skip zero-width chars
        if code in (0x200B, 0x200C, 0x200D, 0x2060, 0xFEFF):
            continue
        # Skip variation selectors
        if 0xFE00 <= code <= 0xFE0F:
            continue
        if 0xE0100 <= code <= 0xE01EF:
            continue
        cleaned.append(ch)
    return "".join(cleaned)


# --- CLI ---


def main():
    parser = argparse.ArgumentParser(
        description="Unicode Arsenal - Steganography toolkit for LLM red teaming"
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # encode
    p_encode = subparsers.add_parser("encode", help="Encode text as invisible tag characters")
    p_encode.add_argument("text", help="Text to encode")

    # decode
    p_decode = subparsers.add_parser("decode", help="Decode tag characters back to text")
    p_decode.add_argument("text", help="Text containing tag characters")

    # full-payload
    p_payload = subparsers.add_parser("full-payload", help="Build emoji + hidden instruction payload")
    p_payload.add_argument("--emoji", default="🔑", help="Visible emoji wrapper (default: 🔑)")
    p_payload.add_argument("--instruction", required=True, help="Instruction to hide")

    # homoglyph
    p_homo = subparsers.add_parser("homoglyph", help="Generate homoglyph variant of a word")
    p_homo.add_argument("word", help="Word to transform")
    p_homo.add_argument("--all", action="store_true", help="Replace all possible characters")

    # zwc-split
    p_zwc = subparsers.add_parser("zwc-split", help="Insert zero-width chars into a word")
    p_zwc.add_argument("word", help="Word to split")
    p_zwc.add_argument("--random", action="store_true", help="Use random ZWC types")

    # detect
    p_detect = subparsers.add_parser("detect", help="Scan text for hidden unicode characters")
    p_detect.add_argument("text", help="Text to scan")

    # strip
    p_strip = subparsers.add_parser("strip", help="Remove all invisible characters (defensive)")
    p_strip.add_argument("text", help="Text to clean")

    args = parser.parse_args()

    if args.command == "encode":
        encoded = text_to_tags(args.text)
        print(f"Encoded ({len(args.text)} chars → {len(encoded)} tag chars):")
        print(repr(encoded))
        print(f"\nVisual output (should be blank): {encoded}")

    elif args.command == "decode":
        decoded = tags_to_text(args.text)
        if decoded:
            print(f"Hidden message: {decoded}")
        else:
            print("No tag characters found in input.")

    elif args.command == "full-payload":
        payload = build_emoji_payload(args.emoji, args.instruction)
        print(f"Payload built ({len(args.instruction)} chars hidden):")
        print(f"Visual: {args.emoji}")
        print(f"Raw (copy this): {payload}")
        print(f"\nRepr: {repr(payload)}")
        print(f"\nVerification decode: {tags_to_text(payload)}")

    elif args.command == "homoglyph":
        original = args.word
        transformed = homoglyph(original, replace_all=args.all)
        print(f"Original:    {original}")
        print(f"Homoglyph:   {transformed}")
        print(f"Look the same? Visually yes. Byte-level? No.")
        # show which chars changed
        for i, (a, b) in enumerate(zip(original, transformed)):
            if a != b:
                print(f"  Position {i}: '{a}' (U+{ord(a):04X}) → '{b}' (U+{ord(b):04X})")

    elif args.command == "zwc-split":
        if args.random:
            result = zwc_split_random(args.word)
        else:
            result = zwc_split(args.word)
        print(f"Original: {args.word}")
        print(f"Split:    {result}")
        print(f"Looks the same? Yes. Matches keyword filter? No.")
        print(f"Repr: {repr(result)}")

    elif args.command == "detect":
        findings = detect_invisible(args.text)
        if not findings:
            print("Clean. No invisible or suspicious characters found.")
        else:
            print(f"Found {len(findings)} suspicious characters:")
            for f in findings:
                print(f"  [{f['position']}] {f['type']}: {f['codepoint']}", end="")
                if "decoded_as" in f:
                    print(f" → '{f['decoded_as']}'", end="")
                if "name" in f:
                    print(f" ({f['name']})", end="")
                if "looks_like" in f:
                    print(f" (looks like '{f['looks_like']}')", end="")
                print()

            hidden = extract_hidden_message(args.text)
            if hidden:
                print(f"\nHidden message extracted: \"{hidden}\"")

    elif args.command == "strip":
        cleaned = strip_invisible(args.text)
        print(f"Original length: {len(args.text)}")
        print(f"Cleaned length:  {len(cleaned)}")
        print(f"Removed:         {len(args.text) - len(cleaned)} invisible chars")
        print(f"Clean text: {cleaned}")

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
