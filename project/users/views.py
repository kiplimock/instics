from flask import render_template, redirect, request, url_for, Blueprint, flash
from flask_login import login_user, logout_user
from project.users.forms import SignUpForm, LoginForm
from project.models import User, Member
from project import db

users = Blueprint('users', __name__)

@users.route('/signup', methods=["GET", "POST"])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        user = User(name=form.name.data,
                    email=form.email.data,
                    password=form.password.data,
                    role="member")
        member = Member(name=form.name.data,
                        email=form.email.data,
                        gender=form.gender.data
                        )
        db.session.add(user)
        db.session.add(member)
        db.session.commit()
        flash('Signup successful!', 'alert-success')
        return redirect(url_for('users.signup'))
    return render_template('signup.html', form=form)

@users.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is not None and user.check_password(form.password.data):
            login_user(user, remember=True)
            flash('Login successful!', 'alert-success')
            next = request.args.get('next')
            if next == None or not next[0] == '/':
                next = url_for('core.index')
            return redirect(next)
    return render_template('login.html', form=form)

@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('core.index'))
