import json

def test_add_user(test_app, test_database):
    client = test_app.test_client()

    response = client.post(
        "/users",
        data=json.dumps(
            {
                "username": "farooq",
                "email": "farooq@teqniqly.com"
            }),
            content_type="application/json")

    data = json.loads(response.data.decode())

    assert response.status_code == 201
    assert "User farooq@teqniqly.com added" in data["message"]

def test_when_user_exists_return_conflict(test_app, test_database):
    client = test_app.test_client()

    response = client.post(
        "/users",
        data=json.dumps(
            {
                "username": "farooq",
                "email": "farooq@teqniqly.com"
            }),
        content_type="application/json")

    data = json.loads(response.data.decode())

    assert response.status_code == 409
    assert "User farooq@teqniqly.com is already registered" in data["message"]

def test_when_user_missing_required_attributes_return_bad_request(test_app, test_database):
    client = test_app.test_client()

    response = client.post(
        "/users",
        data=json.dumps({}),
        content_type="application/json")

    data = json.loads(response.data.decode())
    errors = data["errors"]

    assert response.status_code == 400
    assert "is a required property" in errors["username"]
    assert "is a required property" in errors["email"]