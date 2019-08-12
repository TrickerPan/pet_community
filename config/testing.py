from . import Config


class TestingConfig(Config):
    ENV = 'testing'
    SQLALCHEMY_DATABASE_URI = 'sqlite://'
