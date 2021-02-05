# # from app import db, app
# from flask_marshmallow import Marshmallow

# class Workout(db.Model): 
#     id = db.Column(db.Integer, primary_key = True)
#     level = db.Column(db.String(20), index = True)
#     # sets = db.Column(db.Integer, index = True)
#     pull = db.Column(db.String(50), index = True)
#     push = db.Column(db.String(50), index = True)
#     hip = db.Column(db.String(50), index = True)
#     core = db.Column(db.String(50), index = True)

#     def __init__(self, level, pull, push, hip, core):
#         self.level = level
#         self.pull = pull
#         self.push = push
#         self.hip = hip
#         self.core = core

#     def __repr__(self):
#         return '<id {}>'.format(self.id)

# class WorkoutSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         fields = (
#             'id',
#             'level',
#             'pull',
#             'push',
#             'hip',
#             'core'
#         )

# workout_schema = WorkoutSchema()
# workouts_schema = WorkoutSchema(many=True)