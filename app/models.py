from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from werkzeug.security import generate_password_hash
from flask_login import UserMixin

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
    
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, nullable=False)
    password = db.Column(db.String, nullable= False)

    def __init__(self,username,email,password):
        self.username = username
        self.email = email
        self.password = password

    def saveUser(self):
        db.session.add(self)
        db.session.commit()