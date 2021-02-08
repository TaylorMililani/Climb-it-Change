import os
from flask import Flask, request, jsonify, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
# from sesh import Sesh
# from workout import Workout
# from antagonaist import Antagonist
# from user import User

from flask_login import (
    LoginManager,
    current_user,
    login_required,
    login_user,
    logout_user,
    UserMixin
)
from oauthlib.oauth2 import WebApplicationClient
import requests

# # Internal imports
# from db import init_db_command


app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
# app.config(['SQLALCHEMY_TRACK_MODIFICATIONS']) = False 

GOOGLE_CLIENT_ID = os.environ.get("GOOGLE_CLIENT_ID", None)
GOOGLE_CLIENT_SECRET = os.environ.get("GOOGLE_CLIENT_SECRET", None)

GOOGLE_DISCOVERY_URL = ("https://accounts.google.com/.well-known/openid-configuration")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

login_manager = LoginManager()
login_manager.init_app(app)

try: 
    init_db_command()
except:
    pass

client = WebApplicationClient(GOOGLE_CLIENT_ID)

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)

def get_google_provider():
    return requests.get(GOOGLE_DISCOVERY_URL).json()

google_provider = get_google_provider()
token_endpoint = google_provider["token_endpoint"]



class User(UserMixin, db.Model):
    # __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True)
    email = db.Column(db.String(100), index = True)
    level = db.Column(db.String(20), index = True)
    member_since = db.Column(db.String(10), index = True)
    picture = db.Column(db.String(120), index = True)
    plan = db.relationship('Plan', backref='plan', lazy='dynamic', cascade = "all, delete, delete-orphan")

    def __init__(self, name, email, level, member_since):
        self.name = name
        self.email = email
        self.level = level
        self.member_since = member_since

    def __repr__(self):
        return '<id {}>'.format(self.id)

class UserSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = (
            'id',
            'name',
            'email',
            'level',
            'member_since'
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

class Plan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    sesh_id = db.Column(db.Integer, db.ForeignKey('sesh.id'))
    ant_id = db.Column(db.Integer, db.ForeignKey('antagonist.id'))

    def __init__(self, user_id, sesh_id, ant_id):
        self.user_id= user_id
        self.sesh_id = sesh_id
        self.ant_id = ant_id

    def __repr__(self):
        return '<id {}>'.format(self.id)

class PlanSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        fields = (
            'id',
            'user_id',
            'sesh_id',
            'ant_id'
        )

plan_schema = PlanSchema()
plans_schema = PlanSchema(many=True)
    

@app.route('/')
def homepage():
    return "Climb-it Change"

@app.route('/api/workouts', methods=['GET'])
def workouts():
    all_workouts = Workout.query.all()
    result = workouts_schema.dump(all_workouts)
    return jsonify(result)

@app.route('/api/sessions', methods=['GET'])
def sessions():
    all_sessions = Sesh.query.all()
    result = seshes_schema.dump(all_sessions)
    return jsonify(result)

@app.route('/login', methods=['POST'])
def login():
    google_provider = get_google_provider()
    auth_endpoint = google_provider["authorization_endpoint"]

    request_uri = client.prepare_request_uri(
        authorization_endpoint,
        redirect_uri=request.base_url + "/callback",
        scope=["openid", "email", "profile"]
    )

    return redirect(request_uri)

@app.route('/login/callback', methods=['POST'])
def login_callback():
    code = request.args.get("code")

    token, headers, body = client.prepare_token_request(
    token_endpoint,
    authorization_response=request.url,
    redirect_url=request.base_url,
    code=code
    )
    token_response = requests.post(
        token_url,
        headers=headers,
        data=body,
        auth=(GOOGLE_CLIENT_ID, GOOGLE_CLIENT_SECRET)
    )

    client.parse_request_body_response(json.dumps(token_response.json()))

    userinfo_endpoint = google_provider["userinfo_endpoint"]
    uri, headers, body = client.add_token(userinfo_endpoint)
    userinfo_response = request.get(uri, headers=headers, data=body)

    if userinfo_response.json().get("email_verified"):
        unique_id = userinfo_response.json()["sub"]
        user_email = userinfo_response.json()["email"]
        user_picture = userinfo_response.json()["picture"]
        user_name = userinfo_response.json()["given_name"]
    else:
        print("User email not available or not verified by Google")

    user = User(id=unique_id, name=user_name, email=user_email, picture=user_picture)

    if not User.get(unique_id):
        User.create(unique_id, user_name, user_email, user_picture)
        login_user(user)
        redirect(url_for("/"))

@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for("/"))

if __name__ == '__main__':
    app.run(debug=True)