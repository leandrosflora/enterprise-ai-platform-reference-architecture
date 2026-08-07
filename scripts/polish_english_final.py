#!/usr/bin/env python3
"""Apply final targeted editorial corrections to the English documentation."""

from pathlib import Path

DOCS = Path("docs")

REPLACEMENTS = {
    # AI Risk Framework
    "writing tool or relevant operational impact": "write-capable tool or relevant operational impact",
    "Obligation for critical writing": "Required for critical write actions",
    "Obligatory + blockade": "Required + blocking",
    "agent without owner or risk cannot be subjected to;": "an agent without an owner or risk classification cannot be submitted;",
    "non-approved tool cannot be linked;": "an unapproved tool cannot be linked;",
    "HIGH/CRITICAL agent without approved dates cannot be published;": "a HIGH/CRITICAL agent without an approved dataset cannot be published;",
    "Absent budget blocks MEDIUM or higher;": "a missing budget blocks MEDIUM or higher;",
    "published version is unchangeable;": "a published version is immutable;",
    "non-existent policy results in `deny by default`.": "a missing policy results in `deny by default`.",
    "0,75": "0.75",
    "0,80": "0.80",
    "0,85": "0.85",
    "0,90": "0.90",
    "0,05": "0.05",
    "0,03": "0.03",
    "0,02": "0.02",
    "0,01": "0.01",

    # Governance / compliance crosswalk
    "This crosswalk is a traceability tool. **it does not replace legal interpretation, certification audit, regulatory analysis or specific assessment of the organization's context.**.": "This crosswalk is a traceability tool. **It does not replace legal interpretation, certification audits, regulatory analysis, or a context-specific assessment of the organization.**",
    "Model, prompt, dataset, policy and tool unchangeable versioning": "immutable versioning of models, prompts, datasets, policies and tools",
    "Risk proportional requirements": "risk-proportional requirements",
    "accuracy, robustness and quality as application": "accuracy, robustness and quality as applicable",
    "Access test denied": "denied-access test",
    "facilities and suppliers": "dependencies and suppliers",
    "Revisar o crosswalk:": "Review the crosswalk:",
    "when auditing identify evidence gap or enforcement.": "when an audit identifies an evidence or enforcement gap.",
    "Legal or regulatory controls cannot be dispensed only by technical decision.": "Legal or regulatory controls cannot be waived solely through a technical decision.",

    # Consistent US-English terminology in architecture docs
    "authorisation": "authorization",
    "Authorisation": "Authorization",
    "catalogue": "catalog",
    "Catalogue": "Catalog",
}


def main() -> int:
    files_changed = 0
    replacements = 0
    for path in sorted(DOCS.rglob("*.en.md")):
        original = path.read_text(encoding="utf-8")
        updated = original
        file_count = 0
        for source, target in REPLACEMENTS.items():
            count = updated.count(source)
            if count:
                updated = updated.replace(source, target)
                file_count += count
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            files_changed += 1
            replacements += file_count
            print(f"Polished {path}: {file_count} replacement(s)")
    print(f"English pages polished: {files_changed}")
    print(f"Final replacements applied: {replacements}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
