WeddingReports
==============

A website for reporting the cost and quality of wedding venues.

The config file, config.py, is not included in the repo.

In the config file, please declare the following variables:
SQLALCHEMY_DATABASE_URI
BASE_URL
CSRF_ENABLED
SECRET_KEY
SECURITY_REGISTERABLE 
SECURITY_PASSWORD_HASH
SECURITY_PASSWORD_SALT

Make sure you set CSRF_ENABLED to True

I chose bcrypt as my hash