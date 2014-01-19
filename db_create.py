#!/usr/bin/env python

#script to create a database using SQLAlchemy
from config import SQLALCHEMY_DATABASE_URI
from wedding_app import db
import os.path

#create all the tables we've defined
db.create_all()


