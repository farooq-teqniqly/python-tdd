import os


class BaseConfig:
    TEST = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = None
    SECRET_KEY = None


class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_DEVELOPMENT")
    SECRET_KEY = "my_precious_dev"


class TestConfig(BaseConfig):
    TEST = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_TEST")
    SECRET_KEY = "my_precious_test"


class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_PRODUCTION")
    SECRET_KEY = "my_precious_prod"
