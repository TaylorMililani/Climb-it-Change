# # from app import db
# from flask_marshmallow import Marshmallow

# class User(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     name = db.Column(db.String(50), index = True)
#     email = db.Column(db.String(100), index = True)
#     level = db.Column(db.String(20), index = True)
#     member_since = db.Column(db.String(10), index = True)

#     def __init__(self, name, email, level, member_since):
#         self.name = name
#         self.email = email
#         self.level = level
#         self.member_since = member_since

#     def __repr__(self):
#         return '<id {}>'.format(self.id)

# class UserSchema(ma.SQLAlchemyAutoSchema):
#     class Meta:
#         fields = (
#             'id',
#             'name',
#             'email',
#             'level',
#             'member_since'
#         )

# user_schema = UserSchema()
# users_schema = UserSchema(many=True)

# db.create_all()

# reviews = db.relationship('Review', backref='reviewer', lazy = 'dynamic', cascade = "all, delete, delete-orphan")