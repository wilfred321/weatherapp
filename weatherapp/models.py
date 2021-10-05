from flask_sqlalchemy.model import Model
from weatherapp import db


class City(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(50), nullable = False)