import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db

class Spells(db.Model):
    __tablename__ = "Spells"

    spell_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    spell_name = db.Column(db.String(), unique=True, nullable=False)
    incantation = db.Column(db.String())
    difficulty_level = db.Column(db.Float())
    spell_type = db.Column(db.String())
    description = db.Column(db.String())