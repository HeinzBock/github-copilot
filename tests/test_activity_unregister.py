import src.app as app_module


def test_unregister_removes_existing_participant(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.delete("/activities/Chess Club/participants", params={"email": email})

    # Assert
    payload = response.json()

    assert response.status_code == 200
    assert payload == {"message": f"Removed {email} from Chess Club"}
    assert email not in app_module.activities["Chess Club"]["participants"]


def test_unregister_returns_not_found_for_unknown_activity(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.delete("/activities/Unknown Club/participants", params={"email": email})

    # Assert
    payload = response.json()

    assert response.status_code == 404
    assert payload == {"detail": "Activity not found"}


def test_unregister_returns_not_found_for_missing_participant(client):
    # Arrange
    email = "missing@mergington.edu"

    # Act
    response = client.delete("/activities/Chess Club/participants", params={"email": email})

    # Assert
    payload = response.json()

    assert response.status_code == 404
    assert payload == {"detail": "Participant not found for this activity"}