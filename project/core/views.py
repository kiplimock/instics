from flask import render_template, request, redirect, Blueprint, url_for
from project.users.forms import SignUpForm
from project.core.forms import SearchForm
from project import login_manager

core = Blueprint('core', __name__)

@core.route('/', methods=['GET','POST'])
def index():
    form = SignUpForm()
    if form.validate_on_submit():
        return redirect(url_for('core.index'))
    return render_template('index.html', form=form)

@core.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    return render_template('search.html', form=form)
