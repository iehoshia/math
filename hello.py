#!/usr/bin/env python

import flask


# Create the application.
APP = flask.Flask(__name__)

@APP.route('/')
def index():
    """ Displays the index page accessible at '/'
    """
    return "Hola mundo"


if __name__ == '__main__':
    APP.debug=True
    #APP.run()
    app.run(host='0.0.0.0', port=80)

# nano flask.py