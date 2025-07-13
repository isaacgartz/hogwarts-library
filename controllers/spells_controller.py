from flask import jsonify, request

from db import db
from models.spells import Spells

def add_spell():
    post_data = request.form if request.form else request.json

    fields = ['spell_name', 'incantation', 'difficulty_level', 'spell_type', 'description']
    required = ['spell_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required and not field_data:
            return jsonify({"message": f"{field} is required"})
        values[field] = field_data

    new_spell = Spells(values['spell_name', 'incantation', 'difficulty_level', 'spell_type', 'description'])

    try:
        db.session.add(new_spell)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400
    
    query = db.session.query(Spells).filter(Spells.spell_name == values['spell_name']).first()

    spell = {
        "spell_id": query.spell_id, 
        "spell_name": query.spell_name, 
        "incantation": query.incantation, 
        "difficulty_level": query.difficulty_level,
        "spell_type": query.spell_type, 
        "description": query.description
    }

    return jsonify({"message": "record created", "result": spell}), 201

def get_all_spells():
    query = db.session.query(Spells).all()

    spell_list = []

    for spell in query:
        spell_dict = {
            "spell_id": spell.spell_id, 
            "spell_name": spell.spell_name, 
            "incantation": spell.incantation, 
            "difficulty_level": spell.difficulty_level,
            "spell_type": spell.spell_type, 
            "description": spell.description
        }
        spell_list.append(spell_dict)

    return jsonify({"message": "spells found", "results": spell_list}), 200

def get_spells_by_difficulty(difficulty_level):
    query = db.session.query(Spells).filter(Spells.difficulty_level == difficulty_level).all()
    if not query:
        return jsonify({"message": "record does not exist"}), 404

    spell_list = []

    for spell in query:
        spell_dict = {
            "spell_id": spell.spell_id, 
            "spell_name": spell.spell_name, 
            "incantation": spell.incantation, 
            "difficulty_level": spell.difficulty_level,
            "spell_type": spell.spell_type, 
            "description": spell.description
        }
        spell_list.append(spell_dict)

    return jsonify({"message": "spells found", "results": spell_list}), 200

def update_spell_by_id(spell_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Spells).filter(Spells.spell_id == spell_id).first()


    query.spell_name = post_data.get("spell_name", query.spell_name)
    query.incantation = post_data.get("incantation", query.incantation)
    query.difficulty_level = post_data.get("difficulty_level", query.difficulty_level)
    query.spell_type = post_data.get("spell_type", query.spell_type)
    query.description = post_data.get("description", query.description)


    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400
    
    return jsonify({"message": "record updated successfully"}), 200

def delete_spell(spell_id):
    query = db.session.query(Spells).filter(Spells.spell_id == spell_id).first()

    if not query:
        return jsonify({"message": "record does not exist"}), 404
    
    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400
    
    return jsonify({"message": "record deleted", "results": query}), 200