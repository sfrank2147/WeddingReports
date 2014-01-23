from wedding_app import db, app, user_datastore
from models import User
from flask.ext.security.utils import encrypt_password
import pdb


def create_user(email, password):
    #prevent duplicate emails
    if User.query.filter(User.email == email).first():
        return None
    user = user_datastore.create_user(email=email, 
                          password=encrypt_password(password))
    db.session.commit()
    return user


# $2a$12$Q7QkscgIW8UcWfMI29IDReL8KUjPn.4xTfUt/.61pafM7CFHPqhVO
# py-bcrypt