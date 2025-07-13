import datetime
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy import DateTime


from db import db
from models.wizards import Wizards
from models.spells import Spells

class Specializations(db.Model):
    __tablename__ = "Wizard_Specializations"

    wizard_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Wizards.wizard_id"), primary_key=True)
    spell_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Spells.spell_id"), primary_key=True)
    proficiency_level = db.Column(db.Float(), nullable=False)
    date_learned = db.Column(DateTime(), default=datetime.datetime.now)

    wizard = db.relationship("Wizards", back_populates='specializations')
    spell = db.relationship("Spells", back_populates='specializations')

    def __init__(self, proficiency_level, date_learned):
        if not (1.0 <= proficiency_level <= 5.0):
            raise ValueError("Proficiency level should be between 1.0 and 5.0")
        self.proficiency_level = proficiency_level
        self.date_learned = date_learned