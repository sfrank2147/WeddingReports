from flask.ext.wtf import Form
from wtforms import TextField, PasswordField, TextAreaField, IntegerField
from wtforms.validators import Required

class AddReportForm(Form):
    venue_name = TextField('venue_name')
    content = TextAreaField('content')
    rating = IntegerField('rating')