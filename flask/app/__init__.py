import logging
import os
from logging.handlers import SMTPHandler, RotatingFileHandler
from flask import Flask, request, current_app
from flask_login import LoginManager
from flask_mail import Mail
from flask_bootstrap import Bootstrap
from flask_babel import Babel, lazy_gettext as _l
#from elasticsearch import ElasticSearch
from flask_tryton import Tryton#, Transaction
from flask_cors import CORS

from . import config

#login = LoginManager()
#login.login_view = 'auth.login'
#login.login_message  _l('Por favor ingresa para ver esta página')
#login.session_protection = 'strong'

bootstrap = Bootstrap()
babel = Babel()
mail = Mail()
tryton = Tryton()
cors = CORS()

def create_app(config_class=config.Config):
	app = Flask(__name__)
	app.config.from_object(config_class)

	#login.init_app(app)
	mail.init_app(app)
	bootstrap.init_app(app)
	babel.init_app(app)
	tryton.init_app(app)
	cors.init_app(app)

	from app.main import bp as main_bp
	app.register_blueprint(main_bp)

	if not app.debug and not app.testing:
		auth = None
		if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
			auth = (app.config['MAIL_USERNAME'],
				app.config['MAIL_PASSWORD'])
		secure = None
		mail_handler = SMTPHandler(
			mailhost=(app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
			fromaddr='no-reply@'+ app.config['MAIL_SERVER'],
			toaddrs=app.config['ADMINS'], subject='Failature',
			credentials=auth, secure=secure)
		mail_handler.setLevel(logging.ERROR)
		app.logger.addHandler(mail_handler)
	return app

@babel.localeselector
def get_locale():
	return 'es'
