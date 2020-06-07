import os
from datetime import timedelta

class Config(object):
	SECRET_KEY = os.urandom(64)
	SESSION_TYPE = 'filesystem'
	PERMANENT_SESSION_LIFETIME = timedelta(minutes=1440)
	TESTING = False
	LANGUAGES = ['es', 'en']
