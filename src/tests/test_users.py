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

def test_when_user_exists_return_conflict(test_app, test_database, add_user):
    add_user("farooq", "farooq@teqniqly.com")

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

def test_get_user(test_app, test_database, add_user):
    user = add_user("bubba", "bubba@bubba.com")

    db.session.add(user)
    db.session.commit()


    client = test_app.test_client()

    response = client.get(f"/users/{user.id}")
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert "bubba" in data["username"]
    assert "bubba@bubba.com" in data["email"]
    assert data["id"] > 0
    assert data["created_date"] is not None

def test_when_user_doesnt_exist_return_not_found(test_app, test_database):
    client = test_app.test_client()

    response = client.get(f"/users/9999")

    assert response.status_code == 404

def test_get_users(test_app, test_database, add_user):
    for i in range(1, 3):
        add_user(f"user{i}", f"user{i}@x.com")

    client = test_app.test_client()

    response = client.get(f"/users")
    data = json.loads(response.data.decode())

    assert response.status_code == 200
    assert len(data) == 2

    for i, d in enumerate(data):
        print(f"{i}, {data}")
