import pytest

from src import User, app, db


@pytest.fixture(scope="module")
def test_app():
    app.config.from_object("src.config.TestConfig")

    with app.app_context():
        yield app


@pytest.fixture(scope="function")
def test_client():
    app.config.from_object("src.config.TestConfig")

    with app.app_context():
        yield app.test_client()


@pytest.fixture(scope="function")
def test_database():
    db.create_all()
    yield db
    db.session.remove()
    db.drop_all()


@pytest.fixture(scope="function")
def add_user():
    def _add_user(username, email):
        user = User(username, email)
        db.session.add(user)
        db.session.commit()
        return user

    return _add_user
