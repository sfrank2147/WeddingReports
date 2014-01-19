from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.security import SQLAlchemyUserDatastore, Security

app = Flask(__name__)
app.config.from_object('config') #use config.py file
db = SQLAlchemy(app)

from models import User, Role

#security stuff
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

#import after user_datastore
from wedding_app import routes
