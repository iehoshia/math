from flask import Bluepprint

bp = Bluepprint('main', __name__)

from app.main import routes