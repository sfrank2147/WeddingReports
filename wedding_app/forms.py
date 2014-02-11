from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, SelectField
from wtforms.validators import Required

class AddReportForm(Form):
    venue_name = TextField('venue_name')
    content = TextAreaField('content')
    rating = SelectField(u'Rating', choices=[(str(x),str(x)) for x in range(1,11)])

class SearchForm(Form):
    venue_name = TextField('venue_name')