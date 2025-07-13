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
    school_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Schools.school_id"), nullable=False)
    active = db.Column(db.Boolean(), default=True)

    school = db.relationship("Schools", foregin_keys='[Wizards.school_id]', back_populates='wizards')
    specializations = db.relationship("Specializations", back_populates='wizard', cascade='all, delete-orphan')

    def __init__(self, wizard_name, house, year_enrolled, magical_power_level, school_id, active):
        self.wizard_name = wizard_name
        self.house = house
        self.year_enrolled = year_enrolled
        self.magical_power_level = magical_power_level
        self.school_id = school_id
        self.active = active