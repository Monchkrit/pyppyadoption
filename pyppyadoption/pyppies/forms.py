from flask_wtf import FlaskForm
from wtforms import StringField,IntegerField,SubmitField

class AddForm(FlaskForm):
  name = StringField('Name of Pyppy: ')
  submit = SubmitField('Add Pyppy')

class DelForm(FlaskForm):
  id = IntegerField("Id Number of Pyppy to Remove: ")
  submit = SubmitField('Remove Pyppy')