from flask import jsonify, request

from db import db
from models.schools import Schools

def add_school():
    post_data = request.form if request.form else request.json

    fields = ['school_name', 'location', 'founded_year', 'headmaster']
    required = ['school_name']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required and not field_data:
            return jsonify({"message": f"{field} is required"})
        values[field] = field_data

    new_school = Schools(values['school_name', 'location', 'founded_year', 'headmaster'])

    try:
        db.session.add(new_school)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400
    
    query = db.session.query(Schools).filter(Schools.school_name == values['school_name']).first()

    school = {
        "school_id": query.school_id, 
        "school_name": query.school_name, 
        "location": query.location, 
        "founded_year": query.founded_year,
        "headmaster": query.headmaster
    }

    return jsonify({"message": "school created", "result": school}), 201

def get_all_schools():
    query = db.session.query(Schools).all()

    school_list = []

    for school in query:
        school_dict = {
            "school_id": school.school_id, 
            "school_name": school.school_name, 
            "location": school.location, 
            "founded_year": school.founded_year,
            "headmaster": school.headmaster
        }
        school_list.append(school_dict)
    
    return jsonify({"message": "schools found", "results": school_list}), 200

def get_school_by_id(school_id):
    query = db.session.query(Schools).filter(Schools.school_id == school_id).first()
    if not query:
        return jsonify({"message": "record does not exist"}), 404
    
    school = {
        "school_id": query.school_id, 
        "school_name": query.school_name, 
        "location": query.location, 
        "founded_year": query.founded_year,
        "headmaster": query.headmaster
    }

    return jsonify({"message": "school found", "results": school}), 200

def update_school_by_id(school_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Schools).filter(Schools.school_id == school_id).first()


    query.school_name = post_data.get("school_name", query.school_name)
    query.location = post_data.get("location", query.location)
    query.founded_year = post_data.get("founded_year", query.founded_year)
    query.headmaster = post_data.get("headmaster", query.headmaster)
    
    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400
    
    return jsonify({"message": "record updated successfully"}), 200

def delete_school(school_id):
    query = db.session.query(Schools).filter(Schools.school_id == school_id).first()
    if not query:
        return jsonify({"message": "record does not exist"}), 404
    
    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400
    
    return jsonify({"message": "record deleted", "results": query}), 200