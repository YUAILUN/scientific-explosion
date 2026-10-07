#!/usr/bin/env python3
"""
Pantheon Council Selector & Roster Utility
Part of the Pantheon ("召唤众神") Agent Skill.
Supports Codex, Claude Code, Antigravity, and Agent Skills standard.
"""

import sys
import os
import json
import argparse
import re
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / "references" / "pantheon_data.json"

def load_data():
    if not DATA_FILE.exists():
        raise FileNotFoundError(f"Missing data file: {DATA_FILE}")
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def stem_or_prefix(word):
    w = word.lower().strip()
    if len(w) > 5 and (w.endswith("ity") or w.endswith("ies")):
        return w[:-3]
    if len(w) > 4 and (w.endswith("ing") or w.endswith("ion")):
        return w[:-3]
    if len(w) > 4 and w.endswith("ed"):
        return w[:-2]
    if len(w) > 4 and w.endswith("s"):
        return w[:-1]
    return w

def list_thinkers(args):
    data = load_data()
    category_filter = args.category.lower() if args.category else None
    
    total = 0
    for cat in data["categories"]:
        if category_filter and category_filter not in cat.lower():
            continue
        print(f"\n🏛️  {cat}")
        print("=" * (len(cat) + 4))
        for exp in data["experts"]:
            if exp["category"] == cat:
                total += 1
                summary = exp.get("summary") or exp.get("description", "")[:100] + "..."
                print(f"  • {exp['name']} (`{exp['slug']}`): {summary}")
    print(f"\nTotal listed: {total} / {data['count']}")

def inspect_thinker(args):
    data = load_data()
    slug_or_name = args.target.lower().strip()
    match = None
    for exp in data["experts"]:
        if exp["slug"].lower() == slug_or_name or exp["name"].lower() == slug_or_name:
            match = exp
            break
    if not match:
        for exp in data["experts"]:
            if slug_or_name in exp["name"].lower() or slug_or_name in exp["slug"].lower():
                match = exp
                break

    if not match:
        print(f"❌ Thinker '{args.target}' not found in the Pantheon of 80.")
        sys.exit(1)

    print(f"\n=======================================================")
    print(f"👤 {match['name']} ({match['slug']})")
    print(f"🏛️ Category: {match['category']}")
    print(f"📦 Mimeograph: {match.get('path', '')}")
    print(f"=======================================================")
    print(f"\n📖 Stance & Frameworks:")
    print(match["description"])
    print(f"\n📥 Install deep skill:")
    print(f"  {match.get('install', {}).get('npx', 'npx skills add K-Dense-AI/mimeographs/' + match['slug'])}")
    print()

def search_thinkers(args):
    data = load_data()
    q = args.query.lower().strip()
    words = [w for w in re.split(r"[\s,;+]+", q) if len(w) >= 2]
    stems = [stem_or_prefix(w) for w in words]
    
    scored = []
    for exp in data["experts"]:
        text = f"{exp['name']} {exp['category']} {exp['description']}".lower()
        score = 0
        for w in words:
            if w in exp["name"].lower():
                score += 12
            score += text.count(w) * 3
        for s in stems:
            if len(s) >= 3 and s in text:
                score += text.count(s) * 2

        if score > 0:
            scored.append((score, exp))
            
    scored.sort(key=lambda x: x[0], reverse=True)
    
    print(f"\n🔍 Search results for '{args.query}':")
    if not scored:
        print("  No direct matches found.")
        return

    for score, exp in scored[:args.limit]:
        print(f"  [{score} pts] {exp['name']} ({exp['category']}) - `{exp['slug']}`")
        desc_preview = exp["description"][:140].replace("\n", " ") + "..."
        print(f"             {desc_preview}\n")

def assemble_council(args):
    data = load_data()
    question = args.question.strip()
    q_lower = question.lower()
    
    # Keyword extraction
    words = [w for w in re.split(r"[\s,;+?!.]+", q_lower) if len(w) >= 2]
    stems = [stem_or_prefix(w) for w in words]
    
    chamber_map = {
        "ai": "AI & ML researchers",
        "ml": "AI & ML researchers",
        "tech": "AI & ML researchers",
        "philosophy": "Philosophers",
        "ethics": "Philosophers",
        "science": "Scientists & researchers",
        "bio": "Scientists & researchers",
        "business": "Founders & operators",
        "founder": "Founders & operators",
        "industry": "Founders & operators"
    }
    
    target_category = chamber_map.get(args.chamber.lower()) if args.chamber else None
    
    scored_by_cat = {cat: [] for cat in data["categories"]}
    for exp in data["experts"]:
        text = f"{exp['name']} {exp['description']}".lower()
        score = 0
        for w in words:
            if w in exp['name'].lower():
                score += 15
            score += text.count(w) * 3
        for s in stems:
            if len(s) >= 3:
                score += text.count(s) * 2
        scored_by_cat[exp['category']].append((score, exp))
        
    for cat in scored_by_cat:
        scored_by_cat[cat].sort(key=lambda x: x[0], reverse=True)
        
    council = []
    if target_category:
        candidates = scored_by_cat.get(target_category, [])
        council = [exp for _, exp in candidates[:args.size]]
    else:
        # Cross-disciplinary assembly: pick top representatives across pillars
        per_cat = max(1, args.size // 4)
        for cat in data["categories"]:
            for _, exp in scored_by_cat[cat][:per_cat]:
                council.append(exp)
        # Fill remaining slots with highest overall scorers not already included
        remaining_needed = args.size - len(council)
        if remaining_needed > 0:
            all_remaining = []
            picked_slugs = {e['slug'] for e in council}
            for cat in data["categories"]:
                for score, exp in scored_by_cat[cat]:
                    if exp['slug'] not in picked_slugs:
                        all_remaining.append((score, exp))
            all_remaining.sort(key=lambda x: x[0], reverse=True)
            for _, exp in all_remaining[:remaining_needed]:
                council.append(exp)

    print(f"\n=======================================================")
    print(f"🏛️  THE PANTHEON COUNCIL HAS BEEN SUMMONED")
    print(f"❓ Question: {question}")
    print(f"👥 Panel Size: {len(council)} Titans")
    print(f"=======================================================\n")
    
    for idx, member in enumerate(council, 1):
        print(f"[{idx}] {member['name']} ({member['category']})")
        print(f"    Slug: {member['slug']}")
        print(f"    Lens: {member.get('summary') or member['description'][:140]}...\n")
        
    if args.format == "prompt":
        print("\n--- READY-TO-USE DEBATE PROMPT SCAFFOLD ---\n")
        print(f"You are convening the Pantheon of Minds to answer: \"{question}\"")
        print("\nThe following council members are summoned:")
        for member in council:
            print(f"- **{member['name']}** ({member['category']}): {member['description'][:160]}...")
        print("\nExecution SOP:")
        print("1. Each member gives an embodied first-person response with their signature frameworks.")
        print("2. Members challenge each other's assumptions directly.")
        print("3. Synthesize the core consensus, irreconcilable divergence, and falsifiable next steps.")

def main():
    parser = argparse.ArgumentParser(description="Pantheon 80-Thinker Council Selector")
    subparsers = parser.add_subparsers(dest="command", required=True)
    
    # list
    list_p = subparsers.add_parser("list", help="List thinkers by category")
    list_p.add_argument("-c", "--category", help="Filter by category (founders, philosophers, ai, scientists)")
    list_p.set_defaults(func=list_thinkers)
    
    # inspect
    inspect_p = subparsers.add_parser("inspect", help="Inspect a specific thinker's mental models")
    inspect_p.add_argument("target", help="Slug or name of thinker (e.g. karpathy, aristotle, jobs)")
    inspect_p.set_defaults(func=inspect_thinker)
    
    # search
    search_p = subparsers.add_parser("search", help="Search thinkers by keywords")
    search_p.add_argument("query", help="Keyword or concept (e.g. causality, scaling, eudaimonia)")
    search_p.add_argument("-l", "--limit", type=int, default=8, help="Number of results")
    search_p.set_defaults(func=search_thinkers)
    
    # assemble
    assemble_p = subparsers.add_parser("assemble", help="Assemble an optimal council for a question")
    assemble_p.add_argument("question", help="The research or scientific inquiry")
    assemble_p.add_argument("-s", "--size", type=int, default=6, help="Number of council members")
    assemble_p.add_argument("--chamber", help="Specific chamber (ai, philosophy, science, business)")
    assemble_p.add_argument("--format", choices=["summary", "prompt"], default="summary", help="Output format")
    assemble_p.set_defaults(func=assemble_council)

    args = parser.parse_args()
    args.func(args)

if __name__ == "__main__":
    main()
