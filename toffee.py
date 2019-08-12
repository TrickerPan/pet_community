from os import environ

from flask_migrate import Migrate, upgrade

from app import create_app, db
from app.model import Role

app = create_app(environ.get('CONFIG_NAME') or 'development')
migrate = Migrate(app=app, db=db)


@app.shell_context_processor
def make_shell_context():
    dict(
        db=db,
        Role=Role,
    )


@app.cli.command()
def deploy():
    upgrade()
