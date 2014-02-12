from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager
from flask.ext.security import SQLAlchemyUserDatastore, Security
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import jinja_filters

app = Flask(__name__)
app.config.from_object('config') #use config.py file
db = SQLAlchemy(app)

from models import User, Role

#security stuff
user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

#import after user_datastore
from wedding_app import routes

#jinja filters
app.jinja_env.filters['avg_rating'] = jinja_filters.avg_rating

#database migration
migrate = Migrate(app,db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)