def test_get_activities_returns_all_seeded_activities(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    payload = response.json()

    assert response.status_code == 200
    assert "Chess Club" in payload
    assert "Science Club" in payload
    assert len(payload) == 9


def test_get_activities_returns_expected_activity_shape(client):
    # Arrange

    # Act
    response = client.get("/activities")

    # Assert
    activity = response.json()["Chess Club"]

    assert response.status_code == 200
    assert activity["description"] == "Learn strategies and compete in chess tournaments"
    assert activity["schedule"] == "Fridays, 3:30 PM - 5:00 PM"
    assert activity["max_participants"] == 12
    assert activity["participants"] == [
        "michael@mergington.edu",
        "daniel@mergington.edu",
    ]