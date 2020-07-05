import os
from dotenv import load_dotenv
from datetime import timedelta

class Config(object):
	SECRET_KEY = os.urandom(64)
	TRYTON_DATABASE = 'canjodb'
	TRYTON_CONFIG = '/opt/canjo/tr.conf'
	SESSION_TYPE = 'filesystem'
	PERMANENT_SESSION_LIFETIME = timedelta(minutes=1440)
	DEBUD = False
	POSTS_PER_PAGE = 10

	MAIL_SERVER = 'smpt.google.com'
	MAIL_PORT = 587
	MAIL_USERNAME = 'jepgez@gmail.com'
	MAIL_PASSWORD = 'tmp'
	MAIL_USER_TLS = True
	MAIL_USER_SSL = False
	MAIL_DEFAULT_SENDER = 'jpegez@gmail.com'

	ADMINS = ['jepgez@gmail.com']