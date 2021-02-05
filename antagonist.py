# # from app import db, app
# from flask_marshmallow import Marshmallow

# class Antagonist(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     level = db.Column(db.String(20), index = True)
#     # sets = db.Column(db.Integer, index = True)
#     ant1 = db.Column(db.String(50), index = True)
#     ant2 = db.Column(db.String(50), index = True)
#     ant3 = db.Column(db.String(50), index = True)
#     ant4 = db.Column(db.String(50), index = True)

#     def __init__(self, level, ant1, ant2, ant3, ant4):
#         self.level = level
#         self.ant1 = ant1
#         self.ant2 = ant2
#         self.ant3 = ant3
#         self.ant4 = ant4

#     def __repr__(self):
#         return '<id {}>'.format(self.id)

# class AntagonistSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         fields = (
#             'id',
#             'level',
#             'ant1',
#             'ant2',
#             'ant3',
#             'ant4'
#         )

# ant_schema = AntagonistSchema()
# ants_schema = AntagonistSchema(many=True)