
import pytest

from src.validators.response_validator import ResponseValidator


@pytest.mark.parametrize(
    "data, expected_result",
    [
        (
            {"customer_id": 101, "currency": "INR", "balance": 150000},
            True
        ),
        (
            {"customer_id": 101, "currency": "INR", "balance": "150000"},
            False
        ),
        (
            {"customer_id": 101, "currency": "INR"},
            False
        ),
        (
            {"customer_id": True, "currency": "INR", "balance": 150000},
            False
        ),
    ]
)
def test_balance_schema_validation(data, expected_result):
    actual_result = ResponseValidator.validate_balance_schema(data)

    assert actual_result == expected_result
