# ----> /librarians/forms

from flask_wtf import FlaskForm
from flask_wtf.file import file_allowed
from wtforms import StringField, IntegerField, FileField, PasswordField, SubmitField, SelectField
from wtforms.validators import ValidationError, DataRequired, InputRequired, Email, Length, AnyOf
from wtforms.fields.html5 import DateField

# admin to add a librarian from console
class AddLibrarianForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = StringField('Email', validators=[Email(message=("* Not a valid email address"))])
    gender = SelectField('Gender', validators=[DataRequired(), AnyOf(['male', 'female'], '*Not a valid choice')], choices=[('--select--','--select--'), ('male','Male'), ('female','Female')])
    submit1 = SubmitField('Add Librarian')

# Librarian to add a member
class AddMemberForm(AddLibrarianForm):
    submit2 = SubmitField('Add Member')

# add a book to the database
class AddBookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    subject = StringField('Subject', validators=[DataRequired()])
    pub_date = DateField('Publication Date', validators=[DataRequired()], format='%Y-%m-%d')
    isbn = StringField('ISBN', validators=[DataRequired(), Length(min=17, max=17, message=("* Must be 17 characters long"))])
    loan_period = IntegerField('Loan Period', validators=[DataRequired()])
    barcode = StringField('Barcode', validators=[DataRequired(), Length(min=6, max=6, message=("* Must be 6 characters long"))])
    pages = IntegerField('Pages', validators=[DataRequired()])
    image = FileField('Cover', validators=[file_allowed(['png','jpg'])])
    submit3 = SubmitField('Add Book')
