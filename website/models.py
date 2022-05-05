from . import db
from sqlalchemy.sql import func

class solarSystem(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(10000), nullable = False)
    star = db.Column(db.String(10000))
    planet_id = db.Column(db.Interger, db.ForeignKey('planet.id'))

class planet(db.Model):
    id = db.Column(db.Interger, primary_key = True)
    name = db.Column(db.String(10000), nullable = False)
    description = db.Column(db.string(10000))