from wedding_app import db, app, user_datastore
from models import User
from flask.ext.security.utils import encrypt_password
import pdb
import hashlib


def create_user(email, password):
    #prevent duplicate emails
    if User.query.filter(User.email == email).first():
        return None
    user = user_datastore.create_user(email=email, 
                          password=hashlib.sha512(password).hexdigest())
    db.session.commit()
    return user

def standardize_venue_name(venue_name):
    return venue_name.title()

def standardize_rating(rating):
    if rating < 0:
        return 0
    elif rating > 10:
        return 10
    else:
        return int(rating)


# $2a$12$Q7QkscgIW8UcWfMI29IDReL8KUjPn.4xTfUt/.61pafM7CFHPqhVO
# py-bcrypt