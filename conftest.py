import pytest
from api.api_client import APIClient

BASE_URL = "https://restful-booker.herokuapp.com"


@pytest.fixture(scope="session")
def api_client():
    """
    Creates a reusable API client for the test session
    """
    return APIClient(BASE_URL)


@pytest.fixture(scope="session")
def auth_token(api_client):
    """
    Generates auth token once per test session
    """
    payload = {
        "username": "admin",
        "password": "password123"
    }

    response = api_client.post("/auth", json=payload)

    assert response.status_code == 200, "Authentication failed"

    token = response.json().get("token")
    assert token is not None, "Auth token not found in response"

    return token
