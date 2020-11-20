from pyppyadoption import db
from flask import render_template

class Pyppy(db.Model):
  __tablename__ = 'pyppies'
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.Text)
  owner = db.relationship('Owner',backref='pyppy',uselist=False)

  def __init__(self,name):
    self.name = name

  def __repr__(self):
    return f"Pyppy name: {self.name}"

class Owner(db.Model):
  __tablename__ = 'owners'
  id = db.Column(db.Integer,primary_key=True)
  name = db.Column(db.Text)
  street = db.Column(db.Text)
  city = db.Column(db.Text)
  state = db.Column(db.Text)
  zipcode = db.Column(db.Text)
  pypid = db.Column(db.Integer,db.ForeignKey('pyppies.id'))

  def __init__(self,name):
    self.name = name

  def __repr__(self):
    return f"Owner name: {self.name} Steet address: {self.street} City: {self.city} State: {self.state} Zip: {self.zipcode} Pyp: {self.pypid}"