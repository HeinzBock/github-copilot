import src.app as app_module


def test_signup_adds_new_participant_to_activity(client):
    # Arrange
    email = "newstudent@mergington.edu"

    # Act
    response = client.post("/activities/Chess Club/signup", params={"email": email})

    # Assert
    payload = response.json()

    assert response.status_code == 200
    assert payload == {"message": f"Signed up {email} for Chess Club"}
    assert email in app_module.activities["Chess Club"]["participants"]


def test_signup_rejects_duplicate_participant(client):
    # Arrange
    email = "michael@mergington.edu"

    # Act
    response = client.post("/activities/Chess Club/signup", params={"email": email})

    # Assert
    payload = response.json()

    assert response.status_code == 400
    assert payload == {"detail": "Student already signed up for this activity"}


def test_signup_returns_not_found_for_unknown_activity(client):
    # Arrange
    email = "newstudent@mergington.edu"

    # Act
    response = client.post("/activities/Unknown Club/signup", params={"email": email})

    # Assert
    payload = response.json()

    assert response.status_code == 404
    assert payload == {"detail": "Activity not found"}