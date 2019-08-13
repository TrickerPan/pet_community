from datetime import datetime
from enum import Enum, unique

from sqlalchemy.dialects.postgresql import UUID

from . import db


@unique
class Permission(Enum):
    FOLLOW = 1
    BLACK = 2
    WRITE = 4
    MODERATE = 8
    ADMIN = 16


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(UUID(as_uuid=True), primary_key=True)
    name = db.Column(db.String(16), unique=True)
    default = db.Column(db.Boolean, index=True, default=False)
    permissions = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    created_by = db.Column(UUID(as_uuid=True))
    updated_at = db.Column(db.DateTime, index=True, onupdate=datetime.utcnow)
