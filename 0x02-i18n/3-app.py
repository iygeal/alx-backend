#!/usr/bin/env python3
"""Flask app with Babel."""

from flask import Flask, render_template, request, g
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_DEFAULT_TIMEZONE'] = 'UTC'
app.config['LANGUAGES'] = ['en', 'fr']

babel = Babel(app)


@babel.localeselector
def get_locale():
    """
    Selects the best match for supported languages
    using request.accept_languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Returns the rendered 3-index.html template.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run()
