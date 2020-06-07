from datetime import datetime, date
from flask import render_template, flash, redirect, url_for, request, \
	g, jsonify, current_app, session

from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import db, mail #, login
from app.translate import translate
from app.main import bp
from flask_mail import Message

#@bp.before_app_request
#def before_request():
#	if current_user.is_authenticated:
#		current_user.last_seen = datetime.utcnow()
#		g.locale = str(get_locale())

@bp.route('/', methods=['GET'])
def index():
	base_url = request.url_root
	print(base_url)
	#if current_user.is_authenticated:
	#	return render_template('index.html', user=user)
	return render_template('main/index.html')
