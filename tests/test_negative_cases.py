def test_get_non_existing_booking(api_client):
    response = api_client.get("/booking/999999")
    assert response.status_code == 404, "Expected 404 for non-existing booking"


def test_update_booking_without_auth(api_client):
    payload = {
        "firstname": "NoAuth"
    }

    response = api_client.put("/booking/1", json=payload)
    assert response.status_code in [401, 403], "Update should fail without auth"
