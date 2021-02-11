from app import db
from flask_marshmallow import Marshmallow

class Plan(db.Model):
    user_id
    workout_id = 1
    sesh_id
    ant_id

    book_id = db.Column(db.Integer, db.ForeignKey('book.id'))