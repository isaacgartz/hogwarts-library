from flask import jsonify, request

from db import db
from models.wizards import Wizards

def add_wizard():
    post_data = request.form if request.form else request.json

    fields = ['wizard_name', 'house', 'year_enrolled', 'magical_power_level', 'school_id', 'active']
    required = ['wizard_name', 'school_id']

    values = {}

    for field in fields:
        field_data = post_data.get(field)

        if field_data in required and not field_data:
            return jsonify({"message": f"{field} is required"})

        values[field] = field_data
    
    new_wizard = Wizards(values['wizard_name', 'house', 'year_enrolled', 'magical_power_level', 'school_id', 'active'])

    try:
        db.session.add(new_wizard)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400
    
    query = db.session.query(Wizards).filter(Wizards.wizard_name == values['wizard_name']).first()

    wizard = {
        "wizard_id": query.wizard_id,
        "wizard_name": query.wizard_name,
        "house": query.house,
        "year_enrolled": query.year_enrolled,
        "magical_power_level": query.magical_power_level,
        "school_id": query.school_id,
        "active": query.active
    }

    return jsonify({"message": "wizard created", "result": wizard}), 201

def get_all_wizards():
    query = db.session.query(Wizards).all()

    wizard_roster = []

    for wizard in query:
        wizard_dict = {
            "wizard_id": wizard.wizard_id,
            "wizard_name": wizard.wizard_name,
            "house": wizard.house,
            "year_enrolled": wizard.year_enrolled,
            "magical_power_level": wizard.magical_power_level,
            "school_id": wizard.school_id,
            "active": wizard.active
        }
        wizard_roster.append(wizard_dict)

    return jsonify({"message": "wizards found", "results": wizard_roster}), 200

def get_active_wizards():
    query = db.session.query(Wizards).filter(Wizards.active == True).all()
    if not query:
        return jsonify({"message": "record does not exist"}), 404

    wizard_roster = []

    for wizard in query:
        wizard_dict = {
            "wizard_id": wizard.wizard_id,
            "wizard_name": wizard.wizard_name,
            "house": wizard.house,
            "year_enrolled": wizard.year_enrolled,
            "magical_power_level": wizard.magical_power_level,
            "school_id": wizard.school_id,
            "active": wizard.active
        }
        wizard_roster.append(wizard_dict)

    return jsonify({"message": "wizards found", "results": wizard_roster}), 200

def get_wizards_by_house(house):
    query = db.session.query(Wizards).filter(Wizards.house == house).all()
    if not query:
        return jsonify({"message": "record does not exist"}), 404
    
    wizard_roster = []

    for wizard in query:
        wizard_dict = {
            "wizard_id": wizard.wizard_id,
            "wizard_name": wizard.wizard_name,
            "house": wizard.house,
            "year_enrolled": wizard.year_enrolled,
            "magical_power_level": wizard.magical_power_level,
            "school_id": wizard.school_id,
            "active": wizard.active
        }
        wizard_roster.append(wizard_dict)

    return jsonify({"message": "wizards found", "results": wizard_roster}), 200

def get_wizards_by_magical_power(magical_power_level):

    query = db.session.query(Wizards).filter(Wizards.magical_power_level == magical_power_level).all()
    if not query:
        return jsonify({"message": "record does not exist"}), 404
    
    wizard_roster = []

    for wizard in query:
        wizard_dict = {
            "wizard_id": wizard.wizard_id,
            "wizard_name": wizard.wizard_name,
            "house": wizard.house,
            "year_enrolled": wizard.year_enrolled,
            "magical_power_level": wizard.magical_power_level,
            "school_id": wizard.school_id,
            "active": wizard.active
        }
        wizard_roster.append(wizard_dict)

    return jsonify({"message": "wizards found", "results": wizard_roster}), 200

def update_wizard_by_id(wizard_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Wizards).filter(Wizards.wizard_id == wizard_id).first()


    query.wizard_name = post_data.get("wizard_name", query.wizard_name)
    query.house = post_data.get("house", query.house)
    query.year_enrolled = post_data.get("year_enrolled", query.year_enrolled)
    query.magical_power_level = post_data.get("magical_power_level", query.magical_power_level)
    query.school_id = post_data.get("school_id", query.school_id)
    query.active = post_data.get("active", query.active)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400
    
    return jsonify({"message": "record updated successfully"}), 200

def delete_wizard(wizard_id):
    query = db.session.query(Wizards).filter(Wizards.wizard_id == wizard_id).first()
    if not query:
        return jsonify({"message": "record does not exist"}), 404
    
    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400
    
    return jsonify({"message": "record deleted", "results": query}), 200