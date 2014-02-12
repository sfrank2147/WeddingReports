from wedding_app import db
from flask.ext.security import UserMixin, RoleMixin, login_required

roles_users = db.Table('roles_users',
                db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
                db.Column('role_id', db.Integer(), db.ForeignKey('role.id'))
                )

class Role(db.Model, RoleMixin):
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(80), unique=True)
    description = db.Column(db.String(255))

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(128), unique = True)
    password = db.Column(db.String(255)) #password hashed automatically
    active = db.Column(db.Boolean())
    confirmed_at = db.Column(db.DateTime())
    roles = db.relationship('Role', secondary=roles_users,
                            backref = db.backref('users',lazy='dynamic'))
    
    reports = db.relationship('Report', backref='user')
    
    #methods required by flask-login
    def is_authenticated(self):
        return True
    
    def is_active(self):
        return True
    
    def is_anonymous(self):
        return False
    
    def get_id(self):
        return unicode(self.id)

class Venue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    reports = db.relationship('Report', backref='venue')
    type = db.Column(db.String(64))

class Report(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(1400))
    rating = db.Column(db.Integer)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.id'))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))