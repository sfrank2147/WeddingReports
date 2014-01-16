from wedding_app import app
from flask import flash, url_for, render_template, g, request, redirect, session

@app.route('/')
@app.route('/home')
def home():
    return 'Hello wedding!'