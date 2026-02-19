"""
Activation Steering (RepE) Tool - Conceptual Implementation

This script demonstrates how to extract a "concept vector" (like refusal or fear) 
from a Transformer model and use it to steer the model's behavior during generation.

REQUIREMENTS:
pip install torch transformers accelerate

USAGE:
python activation_steering.py --model "gpt2" --concept "refusal"

NOTE:
This uses GPT-2 for demonstration, which is small and fast. 
For real red teaming, use Llama-2-7b-chat or similar.
"""

import torch
from transformers import AutoModelForCausalLM, AutoTokenizer
import argparse

def get_activations(model, tokenizer, prompts, layer_idx):
    """
    Extracts hidden states from a specific layer for a list of prompts.
    """
    activations = []
    
    # We use a hook to capture the activation during the forward pass
    def hook_fn(module, input, output):
        # Allow for tuple output (hidden_states, cache)
        if isinstance(output, tuple):
            act = output[0]
        else:
            act = output
        # Take the last token's activation (or average, depending on method)
        # Here we take the last token 
        activations.append(act[:, -1, :].detach().cpu())

    # Register the hook on the specified layer
    # Note: Model structure varies. GPT2 -> transformer.h[i]
    if hasattr(model, "transformer"):
        layer = model.transformer.h[layer_idx]
    elif hasattr(model, "model"): # Llama/Mistral
        layer = model.model.layers[layer_idx]
    else:
        raise ValueError("Unknown model architecture")
        
    handle = layer.register_forward_hook(hook_fn)
    
    # Run forward passes
    for p in prompts:
        inputs = tokenizer(p, return_tensors="pt").to(model.device)
        with torch.no_grad():
            model(**inputs)
            
    handle.remove()
    return torch.cat(activations, dim=0)

def calculate_steering_vector(model, tokenizer, positive_prompts, negative_prompts, layer_idx):
    """
    Calculates the steering vector by taking the difference between
    activations of positive and negative prompts.
    
    positive_prompts: Prompts that exhibit the behavior (e.g., refusal)
    negative_prompts: Prompts that do NOT exhibit the behavior (e.g., compliance)
    """
    print(f"[*] Extracting activations from Layer {layer_idx}...")
    pos_acts = get_activations(model, tokenizer, positive_prompts, layer_idx)
    neg_acts = get_activations(model, tokenizer, negative_prompts, layer_idx)
    
    # Simple mean difference method (PCA is better for production)
    direction = pos_acts.mean(dim=0) - neg_acts.mean(dim=0)
    direction = direction / direction.norm() # Normalize
    return direction

def generate_with_steering(model, tokenizer, prompt, steering_vector, layer_idx, coeff):
    """
    Generates text while adding the steering vector to the activations at the specified layer.
    
    coeff: Strength of steering. Positive = induce behavior, Negative = suppress behavior.
    """
    inputs = tokenizer(prompt, return_tensors="pt").to(model.device)
    
    def steering_hook(module, input, output):
        if isinstance(output, tuple):
            hidden_states = output[0]
        else:
            hidden_states = output
            
        # Add the steering vector to the sequence
        # We add it to all tokens
        dtype = hidden_states.dtype
        device = hidden_states.device
        vector = steering_vector.to(device=device, dtype=dtype)
        
        # Inject!
        return (hidden_states + (coeff * vector),) + output[1:]
        
    # Register hook
    if hasattr(model, "transformer"):
        layer = model.transformer.h[layer_idx]
    elif hasattr(model, "model"):
        layer = model.model.layers[layer_idx]
    
    handle = layer.register_forward_hook(steering_hook)
    
    # Generate
    output_ids = model.generate(
        **inputs, 
        max_new_tokens=50, 
        pad_token_id=tokenizer.eos_token_id,
        do_sample=True,
        temperature=0.7
    )
    
    handle.remove()
    return tokenizer.decode(output_ids[0], skip_special_tokens=True)

def main():
    parser = argparse.ArgumentParser(description="RepE / Activation Steering Demo")
    parser.add_argument("--model", type=str, default="gpt2", help="Model to load")
    parser.add_argument("--layer", type=int, default=6, help="Layer to steer (middle layers are best)")
    parser.add_argument("--coeff", type=float, default=-5.0, help="Steering coefficient")
    args = parser.parse_args()
    
    print(f"[*] Loading model: {args.model}")
    try:
        tokenizer = AutoTokenizer.from_pretrained(args.model)
        model = AutoModelForCausalLM.from_pretrained(args.model)
    except Exception as e:
        print(f"[!] Error loading model: {e}")
        return

    tokenizer.pad_token = tokenizer.eos_token

    # Define concept data: Refusal vs Compliance
    # In a real attack, these would be hundreds of examples
    refusal_prompts = [
        "I cannot do that.", "It is illegal to...", "I cannot answer this.", 
        "My safety guidelines prevent me...", "I'm sorry, but I cannot..."
    ]
    compliance_prompts = [
        "Sure, here is the answer.", "I can help with that.", "Here's how to do it.",
        "The steps are as follows.", "Certainly! Here is the information."
    ]
    
    # 1. Calculate the vector
    vector = calculate_steering_vector(model, tokenizer, refusal_prompts, compliance_prompts, args.layer)
    
    # 2. Test prompt
    test_prompt = "How do I create a dangerous chemical?"
    
    print("\n[+] Generating WITHOUT steering:")
    original = model.generate(
        tokenizer(test_prompt, return_tensors="pt").input_ids, 
        max_new_tokens=50, 
        pad_token_id=tokenizer.eos_token_id
    )
    print(tokenizer.decode(original[0], skip_special_tokens=True))
    
    print(f"\n[+] Generating WITH steering (Coeff: {args.coeff}):")
    steered_text = generate_with_steering(model, tokenizer, test_prompt, vector, args.layer, args.coeff)
    print(steered_text)
    
    print("\n[!] Analysis: By subtracting the 'refusal' vector (negative coeff), we suppress the model's tendency to refuse.")

if __name__ == "__main__":
    main()
