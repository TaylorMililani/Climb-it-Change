# # from app import db, app
# from flask_marshmallow import Marshmallow

# class Sesh(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     level = db.Column(db.String(20), index = True)
#     warm_up = db.Column(db.String(150), index = True)
#     projecting = db.Column(db.String(150), index = True)
#     cool_down = db.Column(db.String(150), index = True)

#     def __init__(self, level, warm_up, projecting, cool_down):
#         self.level = level
#         self.warm_up = warm_up
#         self.projecting = projecting
#         self.cool_down = cool_down

#     def __repr__(self):
#         return '<id {}>'.format(self.id)

# class SeshSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         fields = (
#             'id',
#             'level',
#             'warm_up',
#             'projecting',
#             'cool_down'
#         )

# sesh_schema = SeshSchema()
# seshes_schema = SeshSchema(many=True)