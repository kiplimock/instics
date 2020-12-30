from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

app = Flask(__name__)

app.config.from_object('config')

db = SQLAlchemy(app)
mail = Mail(app)

login_manager = LoginManager(app)
login_manager.login_view = 'users.login'
login_manager.login_message = 'Login first to view this page!'

from project.core.views import core
from project.users.views import users
from project.members.views import members
from project.librarians.views import librarians

# register blueprints
app.register_blueprint(core)
app.register_blueprint(users)
app.register_blueprint(members)
app.register_blueprint(librarians)
