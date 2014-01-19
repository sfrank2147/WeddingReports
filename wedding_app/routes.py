from wedding_app import app, db
from flask import flash, url_for, render_template, g, request, redirect, session
from flask.ext.security import login_required, current_user, login_user
from flask.ext.security.utils import verify_password
from flask.ext.security.forms import RegisterForm, LoginForm
from models import User
import db_utilities
import pdb

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', user=g.user)

@app.route('/handle-register',methods=['POST'])
def handle_register():
    form = RegisterForm(request.form)
    if form.email.data == '' or form.password.data == '':
        flash('Please fill in all fields completely.')
        return redirect(url_for('register'))
    else:
        result = db_utilities.create_user(form.email.data, form.password.data)
        if result:
            return redirect('/login')
        else:
            flash('Username already taken')
            return redirect(url_for('register'))

@app.route('/handle-login',methods=['POST'])
def handle_login():
    form = LoginForm(request.form)
    possible_match = User.query.filter(User.email == form.email.data).first()
    if verify_password(form.password.data, possible_match.password):
        login_user(possible_match)    
        return redirect('/home')
    else:
        flash('Login invalid')
        return redirect('/login')