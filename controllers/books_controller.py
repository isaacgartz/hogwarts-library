from flask import jsonify, request

from db import db
from models.books import Books

def add_book():
    post_data = request.form if request.form else request.json

    fields = ['title', 'author', 'subject', 'rarity_level', 'magical_properties', 'school_id', 'available']
    required = ['title', 'school_id']

    values = {}

    for field in fields:
        field_data = post_data.get(field)
        if field_data in required and not field_data:
            return jsonify({"message": f"{field} is required"})
        values[field] = field_data

    new_book = Books(values['title', 'author', 'subject', 'rarity_level', 'magical_properties', 'school_id', 'available'])

    try:
        db.session.add(new_book)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to create record"}), 400
    
    query = db.session.query(Books).filter(Books.title == values['title']).first()

    book = {
        "book_id": query.book_id, 
        "title": query.title, 
        "author": query.author, 
        "subject": query.subject,
        "rarity_level": query.rarity_level, 
        "magical_properties": query.magical_properties,
        "school_id": query.school_id,
        "available": query.available
    }

    return jsonify({"message": "record created", "result": book}), 201

def get_all_books():
    query = db.session.query(Books).all()

    book_list = []

    for book in query:
        book_dict = {
            "book_id": book.book_id, 
            "title": book.title, 
            "author": book.author, 
            "subject": book.subject,
            "rarity_level": book.rarity_level, 
            "magical_properties": book.magical_properties,
            "school_id": book.school_id,
            "available": book.available
        }
        book_list.append(book_dict)
    return jsonify({"message": "books found", "results": book_list}), 200

def get_available_books():
    query = db.session.query(Books).filter(Books.available == True).all()
    if not query:
        return jsonify({"message": "record does not exist"}), 404

    book_list = []

    for book in query:
        book_dict = {
            "book_id": book.book_id, 
            "title": book.title, 
            "author": book.author, 
            "subject": book.subject,
            "rarity_level": book.rarity_level, 
            "magical_properties": book.magical_properties,
            "school_id": book.school_id,
            "available": book.available
        }
        book_list.append(book_dict)
    return jsonify({"message": "books found", "results": book_list}), 200

def update_book_by_id(book_id):
    post_data = request.form if request.form else request.json
    query = db.session.query(Books).filter(Books.book_id == book_id).first()


    query.title = post_data.get("title", query.title)
    query.author = post_data.get("author", query.author)
    query.subject = post_data.get("subject", query.subject)
    query.rarity_level = post_data.get("rarity_level", query.rarity_level)
    query.magical_properties = post_data.get("magical_properties", query.magical_properties)
    query.school_id = post_data.get("school_id", query.school_id)
    query.available = post_data.get("available", query.available)

    try:
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to update record"}), 400
    
    return jsonify({"message": "record updated successfully"}), 200

def delete_book(book_id):
    query = db.session.query(Books).filter(Books.book_id == book_id).first()
    if not query:
        return jsonify({"message": "record does not exist"}), 404
    
    try:
        db.session.delete(query)
        db.session.commit()
    except:
        db.session.rollback()
        return jsonify({"message": "unable to delete record"}), 400
    
    return jsonify({"message": "record deleted", "results": query}), 200