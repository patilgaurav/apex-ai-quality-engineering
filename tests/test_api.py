import pytest
from src.clients.apex_api_client import ApexAPIClient

@pytest.fixture
def client():
    api_client = ApexAPIClient()
    yield api_client
    api_client.close()

def test_health_endpoint(client):
    response = client.get_health()
    assert response.status_code == 200
    assert response.json()["status"] == "healthy"

def test_get_account_details(client):
    response = client.get_account(101)
    data = response.json()

    assert response.status_code == 200
    assert data["customer_id"] == 101
    assert data["name"] == "Rahul"
    assert data["account_type"] == "premium"

def test_get_balance_details(client):
    response = client.get_balance(101)
    data = response.json()

    assert response.status_code == 200
    assert data["customer_id"] == 101
    assert data["currency"] == "INR"
    assert data["balance"] == 150000

def test_get_account_details_invalid_customer(client):
    response = client.get_account(999)
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"

def test_get_balance_details_invalid_customer(client):
    response = client.get_account(999)
    assert response.status_code == 404
    assert response.json()["detail"] == "Customer not found"

@pytest.mark.parametrize(
    "customer_id, expected_currency, expected_balance",
    [
        (101, "INR", 150000),
        (102, "INR", 75000),
    ]
)

def test_get_balance_details_parametrized(client, customer_id, expected_currency, expected_balance):
    response = client.get_balance(customer_id)
    data = response.json()

    assert response.status_code == 200
    assert data["customer_id"] == customer_id
    assert data["currency"] == expected_currency
    assert data["balance"] == expected_balance



