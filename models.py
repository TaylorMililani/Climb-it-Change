from app import app, db
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow

db = SQLAlchemy(app)
migrate = Migrate(app, db)
ma = Marshmallow(app)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), index = True)
    email = db.Column(db.String(100), index = True)
    level = db.Column(db.String(20), index = True)
    member_since = db.Column(db.String(10), index = True)
    plan = db.Column(db.PickleType, index = True)
    workout_count = db.Column(db.Integer, index = True)
    sesh_count = db.Column(db.Integer, index = True)
    ant_count = db.Column(db.Integer, index = True)
    schedule = db.Column(db.PickleType, index = True)
    def __init__(self, name, email, level, member_since, plan, workout_count, sesh_count, ant_count, schedule):
        self.name = name
        self.email = email
        self.level = level
        self.member_since = member_since
        self.plan = []
        self.workout_count = workout_count
        self.sesh_count = sesh_count
        self.ant_count = ant_count
        self.schedule = schedule

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
            'plan',
            'workout_count',
            'sesh_count',
            'ant_count',
            'schedule'
        )

user_schema = UserSchema()
users_schema = UserSchema(many=True)

class Workout(db.Model): 
    __tablename__ = 'workout'
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
    __tablename__ = 'sesh'
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
    __tablename__ = 'antagonist'
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

# class Plan(db.Model):
#     __tablename__ = 'plan'
#     id = db.Column(db.Integer, primary_key=True)
#     user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
#     workout_id = db.Column(db.Integer, db.ForeignKey('workout.id'))
#     sesh_id = db.Column(db.Integer, db.ForeignKey('sesh.id'))
#     ant_id = db.Column(db.Integer, db.ForeignKey('antagonist.id'))

#     def __init__(self, user_id, workout_id, sesh_id, ant_id):
#         self.user_id= user_id
#         self.workout_id = workout_id
#         self.sesh_id = sesh_id
#         self.ant_id = ant_id

#     def __iter__(self):
#         pass

# class PlanSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         fields = (
#             'id',
#             'user_id',
#             'workout_id'
#             'sesh_id',
#             'ant_id'
#         )

# plan_schema = PlanSchema()
# plans_schema = PlanSchema(many=True) 



db.create_all()

try: 
    init_db_command()
except:
    pass