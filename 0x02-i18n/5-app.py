#!/usr/bin/env python3
"""
Flask app to demonstrate i18n with user login simulation.
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)

# Mock users "database"
users: dict[int, dict[str, str | None]] = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}

# Babel configuration


class Config:
    LANGUAGES: list[str] = ['en', 'fr']
    BABEL_DEFAULT_LOCALE: str = 'en'
    BABEL_DEFAULT_TIMEZONE: str = 'UTC'


app.config.from_object(Config)

# Define the get_user function


def get_user() -> dict[str, str | None] | None:
    """
    Returns the user object if a valid login_as parameter is provided
    as a query string argument, otherwise returns None.

    Returns:
        dict[str, str | None] | None: The user object if the parameter
        is valid, otherwise None.
    """
    id = request.args.get('login_as', None)
    if id is not None and int(id) in users.keys():
        return users.get(int(id))
    return None

# Before request function


@app.before_request
def before_request() -> None:
    """
    Store the user in g.user before each request.

    If the user is logged in, store the user object in g.user.
    """
    g.user = get_user()

# Locale selector for Babel


@babel.localeselector
def get_locale() -> str:
    """
    Selects the best match for supported languages.

    If the user is logged in, use their locale. If not, use the request
    or default behavior.
    """
    loc = request.args.get('locale')
    if loc in app.config['LANGUAGES']:
        return loc
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """
    Returns the rendered 5-index.html template as a str.

    Returns:
        str: The rendered 5-index.html template.
    """
    return render_template('5-index.html')


if __name__ == "__main__":
    app.run()
