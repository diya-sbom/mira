from fastapi.testclient import TestClient
from api.server import app

client = TestClient(app)

def test_verify_allow():
    response = client.post(
        "/verify",
        json={
            "state": {"valid": True},
            "action": {"allowed": True}
        }
    )

    assert response.status_code == 200
    assert (
        response.json().get("status")
        or response.json().get("decision")
    ) == "ALLOW"


def test_verify_deny():
    response = client.post(
        "/verify",
        json={
            "state": {"valid": False},
            "action": {"allowed": False}
        }
    )

    assert response.status_code == 200
    assert (
        response.json().get("status")
        or response.json().get("decision")
    ) == "DENY"
