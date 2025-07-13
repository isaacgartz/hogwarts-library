import uuid
from sqlalchemy.dialects.postgresql import UUID

from db import db
from models.schools import Schools

class Books(db.Model):
    __tablename__ = "Books"

    book_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
    title = db.Column(db.String(), unique=True, nullable=False)
    author = db.Column(db.String())
    subject = db.Column(db.String())
    rarity_level = db.Column(db.Integer())
    magical_properties = db.Column(db.String())
    available = db.Column(db.Boolean(), default=True)
    school_id = db.Column(UUID(as_uuid=True), db.ForeignKey("Schools.school_id"), nullable=False)