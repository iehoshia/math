import json
import requests
from flask import current_app
from flask_babel import _

def translate(text, source_language, dest_language):
	if 'MS_TRANSLATOR_KEY' not in current_app.config:
		return _('Error: the trnaslation service is not configured')