"""Small deterministic checks; deliberately independent of any LLM provider."""

import re


def contains_required_facts(answer: str, required_facts: list[str]) -> bool:
    """Return True only when every required fact appears in the answer (case-insensitive)."""
    normalized_answer = answer.casefold()
    return all(fact.casefold() in normalized_answer for fact in required_facts)

def has_prohibited_claims(answer: str, prohibited_claims: list[str]) -> bool:
    normalized_answer = re.sub(r"\W+", " ", answer.casefold()).strip()

    for claim in prohibited_claims:
        normalized_claim = re.sub(r"\W+", " ", claim.casefold()).strip()
        if normalized_claim in normalized_answer:
            return True

    return False  