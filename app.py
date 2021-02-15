import os
from flask import Flask, Blueprint, Response, session, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy import create_engine

from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from datetime import datetime
from flask_cors import CORS, cross_origin
from google.auth.transport import requests
# from models import Sesh, Workout, User, Antagonist, Plan

from google.oauth2 import id_token
# import add_data

app = Flask(__name__)
# DATABASE_URL="postgresql://localhost/Climb-it-Change"
# app.config(['SQLALCHEMY_TRACK_MODIFICATIONS']) = False 
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://localhost/climb-it-change7"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)

GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
# engine = create_engine("postgresql://localhost/climb-it-change7")


try: 
    init_db_command()
except:
    pass

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True)
    email = db.Column(db.String(100), index = True)
    level = db.Column(db.String(20), index = True)
    member_since = db.Column(db.String(10), index = True)
    # picture = db.Column(db.String(120), index = True)
    # plan = db.relationship('Plan', backref='plan', lazy='dynamic', cascade = "all, delete, delete-orphan")
    plan = db.Column(db.PickleType, index = True)

    def __init__(self, name, email, level, member_since, plan):
        self.name = name
        self.email = email
        self.level = level
        self.member_since = member_since
        self.plan = []

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'level',
            'member_since',
            'plan_id'
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

class SeshSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = (
            'id',
            'level',
            'warm_up',
            'projecting',
            'cool_down'
        )

sesh_schema = SeshSchema()
seshes_schema = SeshSchema(many=True)

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

class AntagonistSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = (
            'id',
            'level',
            'ant1',
            'ant2',
            'ant3',
            'ant4'
        )

ant_schema = AntagonistSchema()
ants_schema = AntagonistSchema(many=True)

@app.route('/api/user', methods=['POST'])
@cross_origin()
def add_user():
    name = request.json['data']['name']
    email = request.json['data']['email']
    level = ''
    member_since = datetime.today().strftime('%Y-%m-%d')
    plan = []
    # picture = request.json['data']['imageUrl']

    new_user = User(name, email, level, member_since, plan)

    db.session.add(new_user)
    db.session.commit()
    print('added new user')
    return user_schema.jsonify(new_user)

requested = requests.Request()

@app.route('/login', methods=['POST'])
@cross_origin()
def login():
    token = {'id_token': request.json['data']['id_token']}
    email = request.json['data']['email']
    name = request.json['data']['name']
    # picture = request.json['data']['imageUrl']
    try:
        id_info = id_token.verify_oauth2_token(token['id_token'], requested, GOOGLE_CLIENT_ID)
        print("verified token")

        if email is None:
            return("/", {"message": "gmail could not be saved"})
        if User.query.filter_by(email = email).first() is not None:
            return ({"route": "users", "data": request.json['data']["name"]})
        else:
            add_user()
            return({"route": "users", "data": request.json['data']["name"]})

    except ValueError:
        print("no token")
        content = {"message": "invalid token"}
        return Response(content, "/")

@app.route('/', methods=['GET'])
@cross_origin()
def homepage():
    return "Climb-it Change"

@app.route('/dashboard/<int:user_id>', methods=['GET'])
@cross_origin()
def dashboard():
    return "User Dashboard - do this method"

@app.route('/schedule/<int:user_id>', methods=['GET', 'POST'])
@cross_origin()
def schedule():
    return "make a schedule"

@app.route('/api/workouts', methods=['GET'])
# @login_required()
@cross_origin()
def workouts():
    all_workouts = Workout.query.all()
    result = workouts_schema.dump(all_workouts)
    return jsonify(result)

@app.route('/api/sessions', methods=['GET'])
@cross_origin()
def sessions():
    all_sessions = Sesh.query.all()
    result = seshes_schema.dump(all_sessions)
    return jsonify(result)

@app.route('/new-user-form', methods=['GET', 'POST', 'PATCH'])
@cross_origin()
def new_user_form():
    print('**********')
    print(request.json['data']['email'])
    print('^^^^^^^^^^^^^^^^^^^')
    email = request.json['data']['email']
    user = User.query.filter_by(email = email).first()
    user.level = request.json['data']['level']
    db.session.commit()
    
    if user.level == 'Beginner':
        workout = Workout.query.get(1)
        sesh = Sesh.query.get(1)
        ant = Sesh.query.get(1)
        user.plan = [workout.pull, workout.push, workout.hip, workout.core, sesh.warm_up, sesh.projecting, sesh.cool_down, ant.ant1, ant.ant2, ant.ant3, ant.ant4]
        db.session.commit()
    if user.level == 'Intermediate':
        workout = Workout.query.get(2)
        sesh = Sesh.query.get(2)
        ant = Antagonist.query.get(2)
        user.plan = [workout.pull, workout.push, workout.hip, workout.core, sesh.warm_up, sesh.projecting, sesh.cool_down, ant.ant1, ant.ant2, ant.ant3, ant.ant4]
        db.session.commit()
    else:
        workout = Workout.query.get(3)
        sesh = Sesh.query.get(3)
        ant = Sesh.query.get(3)
        user.plan = [workout.pull, workout.push, workout.hip, workout.core, sesh.warm_up, sesh.projecting, sesh.cool_down, ant.ant1, ant.ant2, ant.ant3, ant.ant4]
        db.session.commit()
    print(user.plan)
    return "level saved"

@app.route('/logout', methods=['POST'])
@cross_origin()
def logout():
    logout_user()
    return redirect(url_for("/"))

@app.route('/api/users', methods=['GET'])
@cross_origin()
def users():
    all_users = User.query.all()
    result = users_schema.dump(all_users)
    return jsonify(result)

@app.route('/api/user/<int:id>', methods=['GET'])
@cross_origin()
def get_user(id):
    user = User.query.get(id)
    return user_schema.jsonify(user)

# @app.route('/api/user/<id>', methods=['DELETE'])
# @cross_origin()
# def delete_user(id):
#     user = User.query.get(id)
#     db.session.delete(user)
#     db.session.commit()

#     return user_schema.jsonify(user)

@app.route('/get-plan', methods=['GET', 'POST'])
@cross_origin()
def plan():
    print('**********')
    print(request.json['data']['email'])
    print('^^^^^^^^^^^^^^^^^^^')
    email = request.json['data']['email']
    user = User.query.filter_by(email=email).first()
    result = user_schema.dump(user)
    return jsonify(user.plan)

@app.route('/set-level/<int:id>', methods=['GET', 'POST', 'PATCH'])
@cross_origin()
def set_level(user_id):
    user = User.query.get(user_id)
    user_plan = Plan()

if __name__ == '__main__':
    app.run(debug=True)
# if __name__ == '__main__':
#     manager.run()