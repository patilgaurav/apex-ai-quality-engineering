import pytest
import requests

from src.clients.apex_api_client import ApexAPIClient
from src.clients.exceptions import (
    ApexAPITimeoutError,
    ApexAPIConnectionError
)

@pytest.fixture
def client():
    api_client = ApexAPIClient()

    yield api_client

    api_client.close()

def test_api_client_handles_timeout(client, monkeypatch):

    def simulate_timeout(*args, **kwargs):
        raise requests.exceptions.Timeout("Connection timed out")

    monkeypatch.setattr(client.session, "get", simulate_timeout)

    with pytest.raises(ApexAPITimeoutError) as error:
        client.get_health()

    assert "timed out" in str(error.value)

def test_api_client_handles_connection_error(client, monkeypatch):

    def simulate_connection_error(*args, **kwargs):
        raise requests.exceptions.ConnectionError("Connection refused")

    monkeypatch.setattr(
        client.session,
        "get",
        simulate_connection_error
    )

    with pytest.raises(ApexAPIConnectionError) as error:
        client.get_health()

    assert "Could not connect" in str(error.value)


