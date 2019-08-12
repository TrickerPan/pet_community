from sqlalchemy.dialects.postgresql import UUID

from . import db


class User(db.Model):
    id = db.Column(UUID(as_uuid=True))
    email = db.Column(db.String(64), unique=True)
    password = db.Column(db.String(256))
    nickname = db.Column(db.String(16))
