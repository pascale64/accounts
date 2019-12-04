from bdf import db
from datetime import datetime
from time import time
from flask import current_app
from flask_wtf import FlaskForm
from sqlalchemy import Integer, ForeignKey, String, Column, Date
from sqlalchemy.ext.declarative import declarative_base

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date)
    description = db.Column(String(255))
    debit = db.Column(db.Integer)
    credit = db.Column(db.Integer)
    montant = db.Column(db.Float)
    AUX = db.Column(db.String(6))
    type = db.Column(db.String(3))
    REF = db.Column(db.String(6))
    JN = db.Column(db.String(6))
    PID = db.Column(db.Integer)
    CT = db.Column(db.Integer)
    
    
    def __repr__(self):
        return '{}'.format(self.id)


class Auxilliere(db.Model):
    id = db.Column(db.String(6), primary_key=True)
    name = db.Column(db.String(255))
    
    def __repr__(self):
        return '{}'.format(self.id)      

