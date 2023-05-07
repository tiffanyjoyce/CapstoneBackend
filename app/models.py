from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db=SQLAlchemy()

class Locations(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    lid= db.Column(db.Integer, nullable=False, unique=True)
    city = db.Column(db.String, nullable=False)

    def __init__(self, lid, city):
        self.lid=lid
        self.city=city

    def saveLocation(self):
        db.session.add(self)
        db.session.commit()
        return self