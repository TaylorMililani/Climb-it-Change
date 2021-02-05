import os
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
)
from oauthlib.oauth2 import WebApplicationClient
import requests

# Internal imports
from db import init_db_command


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# app.config(['SQLALCHEMY_TRACK_MODIFICATIONS']) = False 

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True)
    email = db.Column(db.String(100), index = True)
    level = db.Column(db.String(20), index = True)
    registered_at = db.Column(db.String(10), index = True)

    def __init__(self, name, email, level, registered_at):
        self.name = name
        self.email = email
        self.level = level
        self.registered_at

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'level'
        )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Workout(db.Model): 
    id = db.Column(db.Integer, primary_key = True)
    level = db.Column(db.String(20), index = True)
    # sets = db.Column(db.Integer, index = True)
    pull = db.Column(db.String(50), index = True)
    push = db.Column(db.String(50), index = True)
    hip = db.Column(db.String(50), index = True)
    core = db.Column(db.String(50), index = True)

    def __init__(self, level, pull, push, hip, core):
        self.level = level
        self.pull = pull
        self.push = push
        self.hip = hip
        self.core = core

    def __repr__(self):
        return '<id {}>'.format(self.id)

class WorkoutSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = (
            'id',
            'level',
            'pull',
            'push',
            'hip',
            'core'
        )

workout_schema = WorkoutSchema()
workouts_schema = WorkoutSchema(many=True)

class Sesh(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    level = db.Column(db.String(20), index = True)
    warm_up = db.Column(db.String(150), index = True)
    projecting = db.Column(db.String(150), index = True)
    cool_down = db.Column(db.String(150), index = True)

    def __init__(self, level, warm_up, projecting, cool_down):
        self.level = level
        self.warm_up = warm_up
        self.projecting = projecting
        self.cool_down = cool_down

    def __repr__(self):
        return '<id {}>'.format(self.id)

class Antagonist(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    level = db.Column(db.String(20), index = True)
    # sets = db.Column(db.Integer, index = True)
    ant1 = db.Column(db.String(50), index = True)
    ant2 = db.Column(db.String(50), index = True)
    ant3 = db.Column(db.String(50), index = True)
    ant4 = db.Column(db.String(50), index = True)

    def __init__(self, level, ant1, ant2, ant3, ant4):
        self.level = level
        self.ant1 = ant1
        self.ant2 = ant2
        self.ant3 = ant3
        self.ant4 = ant4

    def __repr__(self):
        return '<id {}>'.format(self.id)




# login_manager = LoginManager()
# login_manager.init_app(app)


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Climb-it Change"

@app.route('/api/workouts', methods=['GET'])
def workouts():
    all_workouts = Workout.query.all()
    result = workouts_schema.dump(all_workouts)
    return jsonify(result)

# @app.route('/api/workouts', methods=['GET'])
# def workouts():

if __name__ == '__main__':
    app.run(debug=True)