
import requests


class ApexAPIClient:

    def __init__(
        self,
        base_url: str = "http://127.0.0.1:8000",
        timeout: float = 5.0
    ):
        self.base_url = base_url.rstrip("/")
        self.timeout = timeout
        self.session = requests.Session()

    def get_health(self):
        return self.session.get(
            f"{self.base_url}/health",
            timeout=self.timeout
        )

    def get_account(self, customer_id: int):
        return self.session.get(
            f"{self.base_url}/account/{customer_id}",
            timeout=self.timeout
        )

    def get_balance(self, customer_id: int):
        return self.session.get(
            f"{self.base_url}/balance/{customer_id}",
            timeout=self.timeout
        )

    def close(self):
        self.session.close()
