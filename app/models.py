from flask import Flask
from app import db
from app.models import User
from . import users


class user(users.Model):
    id = users.Column(users.Integer, primary_key=True)
    username = users.Column(users.String(80), unique=True)
    email = users.Column(users.String(120), unique=True)

    def __init__(self, firstname, lastname, gender, location):
        self.username = firstname 
        self.username = lastname
        self.gender = gender
        self.location = location

    def __repr__(self):
        return '<User %r>' % self.username