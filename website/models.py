from flask_wtf import FlaskForm
from . import db
from flask_login import UserMixin

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))

class SolarSystem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10000), nullable = False)
    star = db.Column(db.String(10000))
    planet_id = db.Column(db.Integer, db.ForeignKey('planet.id'))
    description = db.Column(db.String(10000))

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10000), nullable = False)
    description = db.Column(db.String(10000))

class ResetRequestForm(FlaskForm):
    email = db.Column(db.String(150), unique = True, nullable = False)
    
