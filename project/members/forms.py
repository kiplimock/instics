# ----> /members/forms

from flask_wtf import FlaskForm
from flask_wtf.html5 import DateField
from flask_wtf.file import file_allowed
from wtforms import StringField, IntegerField, FileField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, InputRequired, Email, Length
from project.users.forms import SignUpForm

# Librarian to add a member
