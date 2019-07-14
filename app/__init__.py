from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models import *

app = Flask(__name__)
#db = SQLAlchemy(app)
db.init_app(app)

app.config.from_pyfile('config.py')
lm = LoginManager()
lm.init_app(app)

lm.login_view = "login"


@lm.user_loader
def load_user(userid):
    return User.query.get(int(userid))


from app import views, models
