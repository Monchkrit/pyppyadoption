from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
  name = StringField('Owner Name: ')
  street = StringField('Street: ')
  city = StringField('City: ')
  state = StringField('State:' )
  zipcode = StringField('Zip: ')
  pypid = IntegerField('pypid')
  submit = SubmitField('Add Owner')