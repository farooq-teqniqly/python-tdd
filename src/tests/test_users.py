import json

from src import User, db
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

def test_get_user(test_app, test_database):
    user = User("bubba", "bubba@bubba.com")

    db.session.add(user)
    db.session.commit()


    client = test_app.test_client()

    response = client.get(f"/users/{user.id}")
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert "bubba" in data["username"]
    assert "bubba@bubba.com" in data["email"]
    assert data["id"] > 0
    assert data["created_date"] is None

def test_when_user_doesnt_exist_return_not_found(test_app, test_database):
    client = test_app.test_client()

    response = client.get(f"/users/9999")

    assert response.status_code == 404