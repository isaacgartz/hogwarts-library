from flask import jsonify, request

from db import db
from models.specializations import Specializations
from models.wizards import Wizards
from models.spells import Spells
from datetime import datetime

def add_specialization():
    post_data = request.form if request.form else request.json

    wizard_id = post_data.get('wizard_id')
    spell_id = post_data.get('spell_id')
    proficiency_level = post_data.get('proficiency_level')

    wizard = db.session.query(Wizards).get(wizard_id)
    spell = db.session.query(Spells).get(spell_id)

    if not wizard or not spell:
        return jsonify({"message": "Wizard or Spell not found"}), 404
    
    exists = db.session.query(Specializations).filter_by(wizard_id = wizard_id, spell_id = spell_id).first()
    if exists:
        return jsonify({"message": "Spell specialization already exists"}), 409
    
    new_specialization = Specializations(wizard_id = wizard_id, spell_id = spell_id, proficiency_level = proficiency_level, date_learned = datetime.now())

    try:
        db.session.add(new_specialization)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create specialization"}), 400
    
    return jsonify({"message": "Spell specialization recorded succesfully"}), 201