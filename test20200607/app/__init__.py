import logging
import os
from flask import Flask, request, current_app
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_babel import Babel, lazy_gettext as _l

from . import config

#login = LoginManager()
#login.login_view = 'auth.login'
#login.login_message = _l('Please log in to access this page.')
#login.session_protection = "strong"

bootstrap = Bootstrap()
moment = Moment()
babel = Babel()
mail = Mail()
db = SQLAlchemy()

def create_app(config_class=config.Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	#login.init_app(app)
	mail.init_app(app)
	bootstrap.init_app(app)
	moment.init_app(app)
	babel.init_app(app)

	#from app.auth import bp as blog_bp
	#app.register_blugprint(blog_bp, url_prefix='/auth')

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	return app

@babel.localeselector
def get_locale():
	return 'es'
