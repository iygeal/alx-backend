#!/usr/bin/env python3
"""
Flask app with gettext function for i18n.
"""

from flask import Flask, render_template, request
from flask_babel import Babel

class Config:
    """
    Config class for Babel setup.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
# Instantiate Babel as module-level variable




def get_locale() -> str:
    """
    Selects the best match for supported languages
    using request.accept_languages.
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# Instantiate Babel as module-level variable
babel = Babel(app, locale_selector=get_locale)
@app.route('/')
def index() -> str:
    """
    Returns the rendered index.html template.
    """
    return render_template('3-index.html')


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
