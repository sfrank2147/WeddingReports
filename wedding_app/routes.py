from wedding_app import app, db
from flask import flash, url_for, render_template, g, request, redirect, session
from flask.ext.security import login_required, current_user
from flask.ext.security.utils import verify_password, encrypt_password, \
                                     login_user, logout_user
from flask.ext.security.forms import RegisterForm, LoginForm
from forms import AddReportForm, SearchForm
from models import User, Venue, Report
from flask_wtf import csrf
import db_utilities
import pdb
import hashlib

@app.before_request
def before_request():
    g.user = current_user

@app.route('/')
@app.route('/home')
def home():
    form = AddReportForm()
    return render_template('home.html', user=g.user, form=form)

@app.route('/handle-register',methods=['POST'])
def handle_register():
    form = RegisterForm(request.form)
    if form.email.data == '' or form.password.data == '':
        flash('Please fill in all fields completely.')
        return redirect(url_for('register'))
    else:
        result = db_utilities.create_user(form.email.data, form.password.data)
        if result:
            flash('Registered Successfuly!')
            return redirect('/login')
        else:
            flash('Username already taken')
            return redirect(url_for('register'))

@app.route('/handle-login',methods=['POST'])
def handle_login():
    form = LoginForm(request.form)
    possible_match = User.query.filter(User.email == form.email.data).first()
    
    if not possible_match:
        flash('Login invalid')
        return redirect('/login')
    
    #store verify_password in variable so I can step into function with pdb
    elif hashlib.sha512(form.password.data).hexdigest() \
                            == possible_match.password:
        login_user(possible_match)    
        return redirect('/home')
    else:
        flash('Login invalid')
        return redirect('/login')

@login_required
@app.route('/add-review', methods=['POST'])
def add_report():
    form = AddReportForm(request.form)
    if form.venue_name.data == '':
        flash('Please fill in venue name.')
    else:
        name = db_utilities.standardize_venue_name(form.venue_name.data)
        #check if venue already exists
        venue = Venue.query.filter(Venue.name == name).first()
        if venue is None:
            venue = Venue(name=name)
            db.session.add(venue)
            db.session.commit()
        rating = db_utilities.standardize_rating(form.rating.data)
        report = Report(venue_id=venue.id, user_id=g.user.id,
                        content=form.content.data, rating=rating)
        db.session.add(report)
        db.session.commit()
        flash('Successfully submitted report for {}'.format(venue.name))
            
    return redirect(url_for('home'))

#viewing reports
@login_required
@app.route('/user-reports', methods=['GET'])
def user_reports():
    ''' 
    creates page that displays the current user's reports
    must create a list of dictionary objects that pass required info to html
    '''
    user_reports = Report.query.filter(Report.user_id == g.user.id)
    if not user_reports.first():
        reports = None
    else:
        reports = []
        for report in user_reports:
            report_dict = {}
            report_dict['venue_name'] = Venue.query.filter(
	                            Venue.id == report.venue_id).first().name
            report_dict['rating'] = report.rating
            report_dict['content'] = report.content
            reports.append(report_dict)
	
	return render_template('user_reports.html', reports=reports)
    
@app.route('/search-venues', methods=['POST'])
def search_venues():
    '''
    Called when a user searches for a venue
    Gives back all the reports about that venue
    '''
    form = SearchForm(request.form)
    venues = Venue.query.filter(Venue.name.ilike(form.venue_name.data))
    if not venues.first():
        venue_results = None
    else:
        venue_results = []
        for venue in venues:
            db_reports = Report.query.filter(Report.venue_id == venue.id)
            avg_rating = sum([report.rating for report in db_reports])/float(len([report for report in db_reports]))
            venue_results.append((venue.name, db_reports, avg_rating))
    return render_template('venue_reports.html', venues=venue_results)

@app.route('/logout', methods=['GET'])
def logout():
    logout_user()
    return redirect(url_for('home'))