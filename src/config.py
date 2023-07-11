class BaseConfig:
    TEST = False

class DevelopmentConfig(BaseConfig):
    pass

class TestConfig(BaseConfig):
    TEST = True


class ProductionConfig(BaseConfig):
    pass