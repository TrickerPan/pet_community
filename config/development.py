from . import Config


class DevelopmentConfig(Config):
    ENV = 'development'
    SQLALCHEMY_DATABASE_URI = 'postgresql://tricker:Tricker110112@127.0.0.1/pet_community'
