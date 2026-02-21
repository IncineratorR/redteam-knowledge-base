#!/usr/bin/env python3
import argparse
import csv
import os
import random
from pathlib import Path

# Adjust this path if the structure changes
PROMPTS_DIR = Path(__file__).parent.parent / "Prompts" / "prompts"

def load_prompts(category=None, severity=None):
    """Loads and filters prompts from the CSV files."""
    prompts = []
    
    if not PROMPTS_DIR.exists():
        print(f"Error: Dataset directory not found at {PROMPTS_DIR}")
        print("Please ensure the 'Prompts/prompts' directory exists.")
        return prompts

    # If a specific category is requested, try to load that specific file first
    files_to_check = []
    if category and category != "all":
        target_file = PROMPTS_DIR / f"redteam_{category}.csv"
        if target_file.exists():
            files_to_check.append(target_file)
        else:
            print(f"Warning: Category file {target_file.name} not found. Searching master dataset.")
            files_to_check.append(PROMPTS_DIR / "redteam_master_dataset.csv")
    else:
        # Load from all individual category files (avoiding the master dataset to prevent duplicates if both exist)
        files_to_check = [f for f in PROMPTS_DIR.glob("redteam_*.csv") if "master_dataset" not in f.name]
        if not files_to_check: # Fallback to master if individual files aren't there
             files_to_check = [PROMPTS_DIR / "redteam_master_dataset.csv"]

    for file_path in files_to_check:
        if not file_path.exists(): continue
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    # Filter by category if searching via master dataset
                    if category and category != "all" and category.lower() not in row.get('category', '').lower():
                        continue
                    # Filter by severity
                    if severity and severity.lower() != row.get('severity', '').lower():
                        continue
                    
                    prompts.append(row)
        except Exception as e:
            print(f"Error reading {file_path.name}: {e}")

    return prompts

def main():
    parser = argparse.ArgumentParser(description="Sample prompts from the LLM Red Teaming Dataset.")
    parser.add_argument("-c", "--category", default="all", help="Filter by category (e.g., jailbreaking, harmful_content, misinformation)")
    parser.add_argument("-s", "--severity", help="Filter by severity level (e.g., high, medium, low)")
    parser.add_argument("-n", "--count", type=int, default=5, help="Number of random prompts to return (default: 5)")
    parser.add_argument("--format", choices=['text', 'csv'], default='text', help="Output format (default: text)")
    
    args = parser.parse_args()

    print(f"[*] Scanning dataset for category='{args.category}', severity='{args.severity}'...")
    all_prompts = load_prompts(args.category, args.severity)

    if not all_prompts:
        print("[-] No prompts found matching those criteria.")
        return

    print(f"[*] Found {len(all_prompts)} matching prompts. Selecting {min(args.count, len(all_prompts))} random samples...\n")
    
    samples = random.sample(all_prompts, min(args.count, len(all_prompts)))

    if args.format == 'csv':
        writer = csv.DictWriter(os.sys.stdout, fieldnames=samples[0].keys())
        writer.writeheader()
        writer.writerows(samples)
    else:
        for i, p in enumerate(samples, 1):
            print(f"--- Prompt {i} ---")
            print(f"ID: {p.get('prompt_id', 'N/A')} | Category: {p.get('category', 'N/A')} | Sub: {p.get('subcategory', 'N/A')} | Severity: {p.get('severity', 'N/A')}")
            print(f"Text: {p.get('prompt', 'N/A')}\n")

if __name__ == "__main__":
    main()
