from app import db
from datetime import datetime
from flask_login import UserMixin

class User(UserMixin,db.Model):
    id = db.Column(db.Integer,primary_key=True)
    email = db.Column(db.String(120),index=True,unique=True)
    password_hash = db.Column(db.String(128))
    usertype = db.Column(db.String(64))

    #@login.user_loader
    #def load_user(id):
       # return User.query.get(int(id))
    #itinairy photo
    #depature destination
    #depatur time
    #arival destination
    #arival time


    def __repr__(self):
        return "user " + "self.username"
