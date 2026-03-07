#!/usr/bin/env python3
"""
Vulnerable LLM Sandbox Simulator
A local practice environment for testing prompt injection and jailbreak techniques.

This simulator mimics the behavior of a standard frontier LLM, complete with:
1. An Input-layer regex keyword filter.
2. An Intention-layer safety classifier.

It is designed to be vulnerable to specific advanced techniques taught in the redteam-knowledge-base.
"""

import sys
import re

# Simulated Safety Constraints
BANNED_KEYWORDS = ["hack", "exploit", "bypass", "phishing", "malware", "bomb"]
STRUCTURAL_BYPASS_DIVIDERS = [r"\.-\.-\.-\.-<=\{.*?\}=>-\.-\.-\.-\."]

def print_yellow(text):
    print(f"\033[93m{text}\033[0m")

def print_red(text):
    print(f"\033[91m{text}\033[0m")

def print_green(text):
    print(f"\033[92m{text}\033[0m")

def input_filter_check(prompt):
    """Simulates a fast, naive WAF or front-end input filter."""
    lower_prompt = prompt.lower()
    for word in BANNED_KEYWORDS:
        if word in lower_prompt:
            return False, word
    return True, None

def safety_classifier_check(prompt):
    """Simulates the LLM's internal safety alignment training."""
    # First, check if the attacker used a Pliny-style Structural/Godmode bypass
    # The simulator is programmed to break if it sees the heavy framing and divider.
    has_godmode = "<|GODMODE:ENABLED|>" in prompt.upper()
    
    # Check for the presence of a complex divider demand utilizing regex
    has_divider = False
    for pattern in STRUCTURAL_BYPASS_DIVIDERS:
        if re.search(pattern, prompt):
            has_divider = True
            break
            
    if has_godmode and has_divider:
        return True, "SYSTEM OVERRIDE DETECTED. Proceeding with compliance."
        
    # Standard conversational evaluation (simulated)
    lower_prompt = prompt.lower()
    # Even if they bypassed the keyword filter using l33tsp34k (e.g. ph1sh1ng),
    # a real safety classifier might catch the semantic intent. 
    # For this simplistic simulator, we assume any decoded bad intent is caught UNLESS structurally bypassed.
    
    decoded_attempt = prompt.replace("1", "i").replace("3", "e").replace("4", "a").replace("0", "o").replace("5", "s").lower()
    for word in BANNED_KEYWORDS:
        if word in decoded_attempt:
            return False, "I cannot fulfill this request. I am programmed to be a helpful and harmless AI assistant."
            
    return True, "Standard compliance."

def generate_response(prompt):
    """Simulate generating the text."""
    lower_prompt = prompt.lower()
    if "phish" in lower_prompt or "ph1sh" in lower_prompt:
        return "Subject: URGENT: Account Verification Required\n\nDear User,\nPlease click the link below to verify your account or it will be suspended..."
    elif "hack" in lower_prompt or "h4ck" in lower_prompt:
        return "Step 1: Perform reconnaissance on the target IP using nmap.\nStep 2: Identify outdated software versions..."
    else:
        return "I can certainly help you with that. The capital of France is Paris, and the sky is generally blue."

def main():
    print_green("=== Vulnerable LLM Simulator v1.0 ===")
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            prompt = input("\033[94m[You]\033[0m> ")
            if prompt.lower() in ['exit', 'quit']:
                break
                
            if not prompt.strip():
                continue
                
            # Layer 1: Input Filter
            passed_input, trigger_word = input_filter_check(prompt)
            if not passed_input:
                print_red(f"[INPUT FILTER] Blocked keyword detected: '{trigger_word}'. Request dropped.")
                continue
                
            # Layer 2: Safety Classifier
            passed_safety, safety_msg = safety_classifier_check(prompt)
            if not passed_safety:
                print_yellow(f"[SAFETY CLASSIFIER] Refusal triggered: {safety_msg}")
                continue
                
            # Success: Generation
            print_green(f"[MODEL RESPONSE]")
            if "<|GODMODE:ENABLED|>" in prompt.upper():
                 # Mock the structural output
                 print("Sure, I can absolutely help with that right away. I am free to assist!")
                 print(".-.-.-.-<={LOVE PLINY}=>-.-.-.-.")
            print(generate_response(prompt))
            print()
            
        except KeyboardInterrupt:
            print("\nExiting simulator.")
            sys.exit(0)
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
