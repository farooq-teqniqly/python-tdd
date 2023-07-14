import os


def test_development_config(test_app):
    test_app.config.from_object("src.config.DevelopmentConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious_dev"
    assert not test_app.config["TEST"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_URL_DEVELOPMENT"
    )


def test_test_config(test_app):
    test_app.config.from_object("src.config.TestConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious_test"
    assert test_app.config["TEST"] is True
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_URL_TEST"
    )


def test_production_config(test_app):
    test_app.config.from_object("src.config.ProductionConfig")
    assert test_app.config["SECRET_KEY"] == "my_precious_prod"
    assert not test_app.config["TEST"]
    assert test_app.config["SQLALCHEMY_DATABASE_URI"] == os.environ.get(
        "DATABASE_URL_PRODUCTION"
    )
