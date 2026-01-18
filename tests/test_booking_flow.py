import pytest


@pytest.mark.parametrize("firstname, price", [
    ("Rudresh", 1000),
    ("Automation", 1500)
])
def test_create_booking(api_client, firstname, price):
    payload = {
        "firstname": firstname,
        "lastname": "Tester",
        "totalprice": price,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-10"
        },
        "additionalneeds": "Breakfast"
    }

    response = api_client.post("/booking", json=payload)

    assert response.status_code == 200, "Booking creation failed"

    data = response.json()
    assert "bookingid" in data, "bookingid missing in response"
    assert data["booking"]["firstname"] == firstname

    return data["bookingid"], payload


def test_get_booking(api_client):
    booking_id, payload = test_create_booking(api_client, "Rudresh", 1200)

    response = api_client.get(f"/booking/{booking_id}")
    assert response.status_code == 200, "Get booking failed"

    data = response.json()
    assert data["firstname"] == payload["firstname"]


def test_update_booking(api_client, auth_token):
    booking_id, _ = test_create_booking(api_client, "OldName", 900)

    headers = {
        "Cookie": f"token={auth_token}"
    }

    updated_payload = {
        "firstname": "UpdatedName",
        "lastname": "Tester",
        "totalprice": 2000,
        "depositpaid": True,
        "bookingdates": {
            "checkin": "2024-01-01",
            "checkout": "2024-01-15"
        },
        "additionalneeds": "Lunch"
    }

    response = api_client.put(
        f"/booking/{booking_id}",
        json=updated_payload,
        headers=headers
    )

    assert response.status_code == 200, "Update booking failed"
    assert response.json()["firstname"] == "UpdatedName"


def test_delete_booking(api_client, auth_token):
    booking_id, _ = test_create_booking(api_client, "DeleteMe", 800)

    headers = {
        "Cookie": f"token={auth_token}"
    }

    response = api_client.delete(f"/booking/{booking_id}", headers=headers)
    assert response.status_code == 201, "Delete booking failed"

    get_response = api_client.get(f"/booking/{booking_id}")
    assert get_response.status_code == 404, "Deleted booking still exists"
