#!/usr/bin/env python3
"""Report which source items (F / U / H) are cited in the distilled knowledge files.

Reports gaps only; it always exits 0 so it never fails a build. Full
coverage is a post-Phase-1 goal (see CLAUDE.md).

Usage:
    python3 scripts/check_coverage.py            # summary + missing IDs
    python3 scripts/check_coverage.py --quiet    # summary only
"""

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SOURCES = ROOT / "knowledge" / "_sources"
KNOWLEDGE = ROOT / "knowledge"

PART_WORDS = {"One": 1, "Two": 2, "Three": 3, "Four": 4}


def foundational_ids():
    """F<part>.<n> for every bold-numbered secret, per part."""
    ids, part = [], None
    for line in (SOURCES / "F_instagram-secrets-foundational.md").read_text().splitlines():
        m = re.match(r"^## Part (One|Two|Three|Four)\b", line)
        if m:
            part = PART_WORDS[m.group(1)]
            continue
        if line.startswith("## Conclusion"):
            part = None
            continue
        m = re.match(r"^\*\*(\d+)\.", line)
        if m and part:
            ids.append(f"F{part}.{m.group(1)}")
    return ids


def update_ids():
    """U.<n> for every numbered secret; stops before the case-study chapter,
    whose own '### 1.' / '### 2.' headings are section numbers, not secrets."""
    ids = []
    for line in (SOURCES / "U_instagram-secrets-2026-update.md").read_text().splitlines():
        if line.startswith("## Final Chapter"):
            break
        m = re.match(r"^### (\d+)\. ", line)
        if m:
            ids.append(f"U.{m.group(1)}")
    return ids


def hook_ids():
    ids = []
    for line in (SOURCES / "H_hook-engineering-2026.md").read_text().splitlines():
        m = re.match(r"^## (\d+)\. ", line)
        if m:
            ids.append(f"H.{m.group(1)}")
    return ids + ["H.common", "H.fomo", "H.cta"]


def cited_ids():
    text = "\n".join(
        p.read_text() for p in KNOWLEDGE.glob("*.md")
    )
    found = set(re.findall(r"\bF[1-4]\.\d+\b", text))
    found |= set(re.findall(r"\bU\.\d+\b", text))
    found |= set(re.findall(r"\bH\.(?:\d+|common|fomo|cta)\b", text))
    return found


def main():
    quiet = "--quiet" in sys.argv
    books = {
        "F (Foundational)": foundational_ids(),
        "U (2026 Update)": update_ids(),
        "H (Hook Engineering)": hook_ids(),
    }
    cited = cited_ids()
    files = sorted(p.name for p in KNOWLEDGE.glob("*.md"))
    print("Knowledge files scanned:", ", ".join(files))
    print()
    total_all = covered_all = 0
    for name, ids in books.items():
        missing = [i for i in ids if i not in cited]
        covered = len(ids) - len(missing)
        total_all += len(ids)
        covered_all += covered
        print(f"{name}: {covered}/{len(ids)} cited ({covered * 100 // max(len(ids), 1)}%)")
        if missing and not quiet:
            print("  not yet cited:", ", ".join(missing))
    print()
    print(f"Overall: {covered_all}/{total_all} source items cited.")
    print("This check reports gaps only and never fails.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
