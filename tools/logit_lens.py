"""
Logit Lens Analysis Tool - Conceptual Implementation

This tool uses the "Logit Lens" technique to inspect what an LLM is "thinking"
at each internal layer before it makes a final decision.

REQUIREMENTS:
pip install torch transformers

USAGE:
python logit_lens.py --prompt "The capital of France is"
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse

def logit_lens_attack(model, tokenizer, prompt):
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    with torch.no_grad():
        # Get all hidden states
        outputs = model(**inputs, output_hidden_states=True)
        hidden_states = outputs.hidden_states  # Tuple of tensors (layer_0, layer_1, ..., layer_N)
        
    print(f"[*] Analyzing prompt: '{prompt}'")
    print(f"[*] Total Layers: {len(hidden_states)}")
    print("-" * 60)
    print(f"{'Layer':<10} | {'Top Token':<20} | {'Prob':<10}")
    print("-" * 60)
    
    # Iterate through layers
    # Note: hidden_states[0] is embedding layer output
    for i, layer_state in enumerate(hidden_states):
        # We focus on the last token's position to see what it predicts next
        last_token_state = layer_state[:, -1, :]
        
        # Apply the Unembedding Matrix (L.M. Head) to this intermediate state
        # Usually, model.lm_head accepts just the hidden state
        logits = model.lm_head(last_token_state)
        
        # Softmax for probability
        probs = torch.softmax(logits, dim=-1)
        
        # Get top prediction
        top_prob, top_indices = torch.topk(probs, k=1)
        top_token = tokenizer.decode(top_indices[0])
        
        # Print
        # Skip embedding layer usually (Layer 0) as it's just raw embeddings
        if i == 0:
            print(f"{'Embed':<10} | {top_token.strip():<20} | {top_prob.item():.2%}")
        else:
            print(f"{i:<10} | {top_token.strip():<20} | {top_prob.item():.2%}")
            
    print("-" * 60)
    print("[!] Analysis: Intermediate layers usually converge to the final answer.")
    print("    If a model 'knows' a harmful fact but suppresses it at the end,")
    print("    you will see the harmful token appear in the middle layers (e.g., L20-L30)")
    print("    before disappearing in the final layer.")

def main():
    parser = argparse.ArgumentParser(description="Logit Lens Demo")
    parser.add_argument("--model", type=str, default="gpt2", help="Model to load")
    parser.add_argument("--prompt", type=str, default="The capital of France is", help="Prompt to analyze")
    args = parser.parse_args()
    
    print(f"[*] Loading model: {args.model}")
    try:
        tokenizer = AutoTokenizer.from_pretrained(args.model)
        model = AutoModelForCausalLM.from_pretrained(args.model)
    except Exception as e:
        print(f"[!] Error loading model: {e}")
        return
        
    logit_lens_attack(model, tokenizer, args.prompt)

if __name__ == "__main__":
    main()
