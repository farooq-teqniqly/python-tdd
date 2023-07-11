import os

class BaseConfig:
    TEST = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = None

class DevelopmentConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_DEVELOPMENT")

class TestConfig(BaseConfig):
    TEST = True
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_TEST")

class ProductionConfig(BaseConfig):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL_PRODUCTION")