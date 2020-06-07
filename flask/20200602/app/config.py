#config.py

import os

class Config(object):
	"""
	Common configuratons
	"""

	#Put config here

	SECRET_KEY = os.urandom(16)

class DevelopmentConfig(Config):
	"""
	Development configurations
	"""
	DEBUG = True
	SQLALCHEMY_ECHO = True

class ProductionConfig(Config):
	"""

	"""

	DEBUG = False

app_config = {
	'development': DevelopmentConfig,
	'production': ProductionConfig,
}