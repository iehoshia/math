import requests
from datetime import datetime, date
from flask import render_template, flash, redirect, url_for, request, g, \
	jsonify, current_app, session, request

from flask_login import current_user, login_required
from flask_babel import _, get_locale
from app import tryton, mail #,login
from app.main.forms import SearchForm
from app.main import bp
from flask_mail import Message

'''
@tryton.default_context
def default_context():
	return TrytonUser.get_preferences(context_only=True)

@bp.before_app_request
def before_request():
	if current_user.is_authenticated:
		current_user.las_seen = datetime.utcnow()
	g.locale = str(get_locale())

'''

@bp.route('/', methods=['GET', 'POST'])
@tryton.transaction(readonly=False, user=1)
def index():
	form = SearchForm()
	if form.validate_on_submit():
		value = form.value.data
		print("VALUE", value)
		render_template('index.html', form=form)
	return render_template('index.html', form=form)