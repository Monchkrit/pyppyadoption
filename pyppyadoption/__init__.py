import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SECRET_KEY'] = "thirty988%sr0wr6"
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir,'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
Migrate(app,db)

from pyppyadoption.pyppies.views import pyppies_blueprint
from pyppyadoption.owners.views import owners_blueprint

app.register_blueprint(owners_blueprint,url_prefix='/owners')
app.register_blueprint(pyppies_blueprint,url_prefix='/pyppies')