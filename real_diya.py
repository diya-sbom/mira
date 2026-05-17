import requests


class RealDiya:
    def __init__(self):
        self.url = "http://127.0.0.1:8000/verify"
        self.api_key = "test-key"

    def reconcile_sbom(self, payload):
        try:
            response = requests.post(
                self.url,
                headers={
                    "Content-Type": "application/json",
                    "x-api-key": self.api_key,
                },
                json=payload,
                timeout=30,
            )

            if response.status_code != 200:
                return False

            data = response.json()

            # Accept PASS decisions
            if data.get("decision") == "PASS":
                return True

            # Fallback if API returns status field
            if data.get("status") == "PASS":
                return True

            return False

        except Exception:
            return False

    def execute_secure(self, payload):
        # Composite path uses this method
        return self.reconcile_sbom(payload)
