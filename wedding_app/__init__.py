from flask import Flask, g
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

app = Flask(__name__)
app.config.from_object('config') #use config.py file
db = SQLAlchemy(app)

# lm = LoginManager()
# lm.init_app(app)
# lm.login_view = 'login'

#import routes last b/c routes imports app
from wedding_app import routes