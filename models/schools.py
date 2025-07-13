import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Schools(db.Model):
    __tablename__ = 'Magical Schools'

    school_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    school_name = db.Column(db.String(), unique=True, nullable=False)
    location = db.Column(db.String())
    founded_year = db.Column(db.Integer())
    headmaster = db.Column(db.String())