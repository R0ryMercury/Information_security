from project.backend.setup_db import db
from marshmallow import Schema, fields


class User(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(150), nullable=False)
    first_name = db.Column(db.String(80), nullable=False)
    last_name = db.Column(db.String(80), nullable=False)
    job = db.Column(db.String(100))
    company = db.Column(db.String(100))
    address = db.Column(db.String(100))
    birthdate = db.Column(db.Date())
    role = db.Column(db.String(10))


class UserSchema(Schema):
    id = fields.Int()
    username = fields.Str()
    email = fields.Email()
    password = fields.Str()
    first_name = fields.Str()
    last_name = fields.Str()
    job = fields.Str()
    company = fields.Str()
    address = fields.Str()
    birthdate = fields.DateTime()
    role = fields.Str()
