# ----> /users/forms

from flask_wtf import FlaskForm
from flask_wtf.file import file_allowed
from wtforms import StringField, IntegerField, FileField, PasswordField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, InputRequired, Email, Length, AnyOf
from wtforms.fields.html5 import DateField
from project.models import User

# sign up to be a member
class SignUpForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(message=("* Not a valid email address"))])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=12, message=("* Password must have a minimum of 12 characters"))])
    gender = SelectField('Gender', validators=[DataRequired(), AnyOf(['male', 'female'], '*Not a valid choice')], choices=[('--select--','--select--'), ('male','Male'), ('female','Female')])
    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Email(message=("* Not a valid email address"))])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Log In')
