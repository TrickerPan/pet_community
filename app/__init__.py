from flask import Flask

from .model import db

from config import CONFIG


def create_app(config_name):
    app = Flask(__name__)

    config = CONFIG[config_name]
    app.config.from_object(config)

    config.init_app(app=app)
    db.init_app(app=app)

    @app.route('/')
    def hello_world():
        return 'Hello World!'

    return app
