import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db
from models.schools import Schools

class Wizards(db.Model):
    __tablename__ = "Wizards"

    wizard_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    wizard_name = db.Column(db.String(), unique=True, nullable=False)
    house = db.Column(db.String())
    year_enrolled = db.Column(db.Integer())
    magical_power_level = db.Column(db.Integer())
    active = db.Column(db.Boolean(), default=True)
    school_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Schools.school_id"), nullable=False)