from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField, StringField
from wtforms.validators import ValidationError, DataRequired

class SearchForm(FlaskForm):
    first = SelectField('Search by',validators=[DataRequired()], choices=[('title', 'Title'), ('author', 'Author'), ('subject', 'Subject'), ('publisher', 'Publisher'), ('isbn', 'ISBN')])
    second = SelectField('',validators=[DataRequired()], choices=[('title', 'Title'), ('author', 'Author'), ('subject', 'Subject'), ('publisher', 'Publisher'), ('isbn', 'ISBN')])
    third = SelectField('',validators=[DataRequired()], choices=[('title', 'Title'), ('author', 'Author'), ('subject', 'Subject'), ('publisher', 'Publisher'), ('isbn', 'ISBN')])
    keyword = StringField('Keyword', validators=[DataRequired()], render_kw={"placeholder":"Enter a keyword"})
    submit = SubmitField('Search')