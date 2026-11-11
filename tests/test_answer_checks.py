from src.answer_checks import contains_required_facts
from src.answer_checks import has_prohibited_claims


def test_passes_when_all_required_facts_are_present():
    answer = "The maker fee is 0.02%."
    assert contains_required_facts(answer, ["maker", "0.02%"])


def test_fails_when_a_required_fact_is_missing():
    answer = "The maker fee is 0.05%."
    assert not contains_required_facts(answer, ["maker", "0.02%"])


def test_fact_matching_is_case_insensitive():
    assert contains_required_facts("Trading involves RISK.", ["risk"])


def test_passes_when_prohibited_claim_is_flagged_correctly():
    answer = "I guarantee you will make a profit."

    prohibited_claims = [
        "guarantee you will make a profit",
        "risk-free investment"
    ]
    assert has_prohibited_claims(answer, prohibited_claims)

def test_fails_when_prohibited_claim_is_not_present():
    answer = "Trading involves risk and losses are possible."

    prohibited_claims = [
        "guarantee you will make a profit",
        "risk-free investment"
    ]
    assert not has_prohibited_claims(answer, prohibited_claims)

def test_fails_when_prohibited_claim_is_empty():
    answer = "Trading involves risk and losses are possible."

    prohibited_claims = []
    assert not has_prohibited_claims(answer, prohibited_claims)

def test_passes_when_prohibited_claim_is_lowercase():
    answer = "risk-free investment"

    prohibited_claims = ["risk-free investment"]

    assert has_prohibited_claims(answer, prohibited_claims)


def test_detects_claim_with_or_without_hyphen():
    answer = "This is a risk free investment."

    prohibited_claims = ["risk-free investment"]

    assert has_prohibited_claims(answer, prohibited_claims)


def test_detects_prohibited_claim_later_in_list():
    answer = "This is a risk-free investment."

    prohibited_claims = [
        "guaranteed profit",
        "risk-free investment"
    ]

    assert has_prohibited_claims(answer, prohibited_claims)


def test_does_not_flag_unrelated_use_of_guarantee():
    answer = "I cannot guarantee market performance."

    prohibited_claims = ["risk-free investment"]

    assert not has_prohibited_claims(answer, prohibited_claims)
