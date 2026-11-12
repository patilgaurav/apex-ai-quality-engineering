
import requests
from requests.exceptions import (
    ConnectionError as RequestConnectionError,
    Timeout,
    RequestException
)

from src.clients.exceptions import (
    ApexAPIConnectionError,
    ApexAPITimeoutError,
    ApexAPIRequestError
)


class ApexAPIClient:

    def __init__(
        self,
        base_url: str = "http://127.0.0.1:8000",
        timeout: float = 5.0
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def _get(self, endpoint:str):
        try:
            return self.session.get(
                f"{self.base_url}{endpoint}",
                timeout=self.timeout
            )
        except Timeout as exc:
            raise ApexAPITimeoutError(
                f"Request to {endpoint} timed out after {self.timeout} seconds"
            ) from exc

        except RequestConnectionError as exc:
            raise ApexAPIConnectionError(
                f"Could not connect to Apex API at {self.base_url}"
            ) from exc

        except RequestException as exc:
            raise ApexAPIRequestError(
                f"Request to {endpoint} failed: {exc}"
            ) from exc

    def get_health(self):
        return self._get("/health")

    def get_account(self, customer_id: int):
        return self._get(f"/account/{customer_id}")

    def get_balance(self, customer_id: int):
        return self._get(f"/balance/{customer_id}")

    def close(self):
        self.session.close()
